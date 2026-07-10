#!/usr/bin/env python3
"""Validate the handbook's pinned references and navigation links."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "references" / "manifest.json"
GITMODULES_PATH = ROOT / ".gitmodules"
INDEX_PATH = ROOT / "docs" / "navigation" / "index.md"


def normalize_url(url: str) -> str:
    return url.rstrip("/").removesuffix(".git")


def run_git(*args: str) -> tuple[int, str, str]:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def load_manifest() -> list[dict[str, str]]:
    payload = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    sources = payload.get("submodules")
    if not isinstance(sources, list):
        raise ValueError("manifest key submodules must be a list")
    return sources


def load_gitmodules() -> dict[str, str]:
    text = GITMODULES_PATH.read_text(encoding="utf-8")
    entries: dict[str, str] = {}
    for section in re.split(r"(?=^\[submodule )", text, flags=re.MULTILINE):
        path_match = re.search(r"^\s*path = (.+)$", section, flags=re.MULTILINE)
        url_match = re.search(r"^\s*url = (.+)$", section, flags=re.MULTILINE)
        if path_match and url_match:
            entries[path_match.group(1).strip()] = url_match.group(1).strip()
    return entries


def verify_manifest(sources: list[dict[str, str]], gitmodules: dict[str, str]) -> list[str]:
    errors: list[str] = []
    paths = [source.get("path") for source in sources]
    urls = [source.get("url") for source in sources]
    if len(sources) != 27:
        errors.append(f"manifest has {len(sources)} sources, expected 27")
    if len(set(paths)) != len(paths):
        errors.append("manifest has duplicate paths")
    if len(set(urls)) != len(urls):
        errors.append("manifest has duplicate URLs")

    for source in sources:
        path = source.get("path")
        url = source.get("url")
        requested_ref = source.get("requestedRef")
        if not all(isinstance(value, str) and value for value in (path, url, requested_ref)):
            errors.append(f"invalid manifest entry: {source!r}")
            continue
        actual_url = gitmodules.get(path)
        if actual_url is None:
            errors.append(f"missing .gitmodules path: {path}")
        elif normalize_url(actual_url) != normalize_url(url):
            errors.append(f"URL mismatch for {path}: {actual_url} != {url}")

    extra_paths = sorted(set(gitmodules) - set(paths))
    if extra_paths:
        errors.append("unexpected .gitmodules paths: " + ", ".join(extra_paths))
    return errors


def verify_submodules(sources: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    for source in sources:
        path = ROOT / source["path"]
        if not path.exists():
            errors.append(f"missing submodule directory: {source['path']}")
            continue

        code, status, stderr = run_git("-C", str(path), "status", "--porcelain")
        if code != 0:
            errors.append(f"cannot inspect {source['path']}: {stderr}")
        elif status:
            errors.append(f"dirty submodule {source['path']}: {status}")

        code, origin, stderr = run_git("-C", str(path), "remote", "get-url", "origin")
        if code != 0:
            errors.append(f"cannot read origin for {source['path']}: {stderr}")
        elif normalize_url(origin) != normalize_url(source["url"]):
            errors.append(
                f"origin mismatch for {source['path']}: {origin} != {source['url']}"
            )
    return errors


def verify_handbook_links() -> list[str]:
    errors: list[str] = []
    documents = [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]
    for document in documents:
        text = document.read_text(encoding="utf-8")
        links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
        for link in links:
            target = unquote(link.split("#", 1)[0])
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            path = (document.parent / target).resolve()
            if not path.exists():
                relative = document.relative_to(ROOT)
                errors.append(f"broken handbook link in {relative}: {link}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--links-only",
        action="store_true",
        help="skip submodule worktree checks and validate navigation only",
    )
    args = parser.parse_args()

    try:
        sources = load_manifest()
        gitmodules = load_gitmodules()
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"handbook verification failed: {error}", file=sys.stderr)
        return 1

    errors = verify_manifest(sources, gitmodules)
    errors.extend(verify_handbook_links())
    if not args.links_only:
        errors.extend(verify_submodules(sources))

    if errors:
        print("handbook verification failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    mode = "links-only" if args.links_only else "complete"
    print(f"handbook verification passed ({mode}; {len(sources)} sources)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
