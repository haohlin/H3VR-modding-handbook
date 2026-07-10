# Contributing to the H3VR Modding Handbook

Thank you for helping make H3VR modding knowledge easier to find and safer to
reuse.

## What belongs here

- Clear route guides, checklists, and navigation improvements.
- User-provided notes with provenance headers.
- Attributed source cards for external documentation.
- New upstream Git repositories recorded as pinned submodules.
- Corrections that make a version, compatibility boundary, or validation step
  more explicit.

## What does not belong here

- H3VR assemblies, decompiled game source, Steam content, r2modman profiles, or
  credentials.
- Unity Library, Temp, Logs, obj, build output, release archives, or generated
  bundles.
- Third-party full text, packages, images, videos, or attachments without a
  redistribution license or author permission.
- Edits inside a reference submodule that should instead happen upstream.

## Add or update a source

1. Decide its source class using [SOURCES.md](SOURCES.md).
2. For an external page, add a short source card with Source, Provided by,
   Captured, and Redistribution metadata.
3. For an upstream Git repository, add it as a submodule under references/ and
   add its path, URL, and requested ref to references/manifest.json.
4. Update the navigation index and affected route guide.
5. Run:

~~~bash
python3 -m unittest tests/test_reference_manifest.py -v
python3 scripts/verify_handbook.py
~~~

6. Commit only the handbook files, manifest, and gitlink that belong to the
   change.

## Update a pinned submodule

Fetch and review the upstream source in its own directory, select the intended
commit or tag, stage the gitlink in this repository, and explain the reason for
the pin change in the commit. Do not use a broad update of all submodules.

~~~bash
git -C references/H3VR-Modding/Mason fetch origin
git -C references/H3VR-Modding/Mason checkout <reviewed-commit-or-tag>
git add references/H3VR-Modding/Mason
python3 scripts/verify_handbook.py
~~~

## Report a problem

When reporting a broken guide or source, include the handbook page, the source
URL or submodule path, the tool versions involved, the observed result, and any
relevant H3VR/BepInEx log excerpt. Never include credentials or proprietary game
files.

