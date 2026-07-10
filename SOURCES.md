# Source and Attribution Policy

The handbook separates original guidance from reference material so that a
reader can trace every technical recommendation back to its source.

## Source classes

1. **Authored handbook guidance** lives in docs/. It is concise navigation,
   workflow, and verification advice written for this repository.
2. **User-provided raw material** lives in docs/sources/user-provided/. It is
   retained as supplied in the project conversation and includes a provenance
   header.
3. **Upstream Git documentation** remains in its pinned submodule below
   references/. That preserves its original raw Markdown, revision, license,
   and authorship without creating a divergent copy.
4. **External source cards** live in docs/sources/external/. They contain a
   direct URL, publisher, capture date, relevance summary, and any known access
   or license note.

## Redistribution rule

A public page is not automatically licensed for full republication. Copy raw
third-party text into docs/sources/upstream/ only when its license or author
explicitly permits redistribution. Otherwise, use a source card and link to the
original. Do not add third-party binary assets, Google Doc content, video
transcripts, forum posts, Discord attachments, or Asset Store packages solely
because they are publicly reachable.

## Maintaining sources

- Keep upstream Git sources as submodules; do not edit their contents here.
- Update references/manifest.json whenever an upstream source is added or
  removed.
- Re-run python3 scripts/verify_handbook.py after a source, submodule, or
  navigation change.
- Keep author, publisher, and original URL intact in every source card.

