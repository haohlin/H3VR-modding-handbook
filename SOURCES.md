# Source Policy

| Source type | Store it as | Rule |
| --- | --- | --- |
| Handbook guidance | docs/ | Keep it compact; link primary sources |
| User-provided text | docs/sources/user-provided/ | Keep provenance header |
| Upstream Git docs | references/ submodule | Do not edit here |
| External page / video / Doc | docs/sources/external/ card | Link + attribute; do not copy full text |

## Before adding material

| ✅ Add | ❌ Do not add |
| --- | --- |
| Source URL, author/publisher, capture date | Unlicensed full third-party copies |
| Reviewed Git submodule pin | Game binaries / decompiled source |
| Short original summary | Unity caches / generated artifacts |
| Raw text the user supplied | Credentials / profile data |

## Maintain

1. Add/update manifest + navigation.
2. Run the handbook verifier.
3. Commit the handbook file and gitlink only.

