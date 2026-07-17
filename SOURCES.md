# Source Policy

This handbook teaches from credited evidence. Use the right record for the
material, retain author/publisher/context information, and make it possible for
a reader to return to the primary source.

> [!IMPORTANT]
> Rich, visual authored guidance is encouraged. Do not turn third-party work
> into an uncredited handbook rewrite, and do not flatten supplied notes until
> their original context and attribution disappear.

## Put each kind of material in the correct place

| Source type | Store it as | Rule |
| --- | --- | --- |
| Handbook guidance | `docs/` | Teach in layers: orient the reader, explain the system, show the work, verify the result, then link credited primary sources |
| User-provided text | `docs/sources/user-provided/` | Preserve detailed supplied information, context, and links; do not condense it into navigation prose or visual summaries |
| Upstream Git docs | `references/` submodule | Do not edit here; record the reviewed pin and remote in the manifest |
| External page, video, or document | `docs/sources/external/` card | Link and attribute it; do not copy full third-party text |

## Keep the evidence chain visible

| Add | Why it belongs in the record | Do not add |
| --- | --- | --- |
| Source URL, author/publisher, capture date, and scope | Lets a reader assess provenance and freshness | Unlicensed full third-party copies |
| Reviewed Git submodule pin and manifest entry | Makes the upstream snapshot reproducible | Game binaries or decompiled source |
| Original handbook explanation or diagram | Teaches without copying the upstream work | Unity caches or generated artifacts |
| Raw text the user supplied | Retains supplied context and links | Credentials or profile data |

> [!NOTE]
> A source pin establishes what was reviewed at one commit. A release page,
> installed manifest, and runtime test establish different facts. Keep those
> boundaries explicit, especially for version-sensitive loaders and packages.

## Maintain a source addition

1. Add the guide, source card, raw note, or submodule in the appropriate
   location above.
2. Record author/publisher, capture/review context, and a link back to the
   primary material.
3. Add or update the reference manifest and navigation only when the change
   introduces a source a reader needs to discover.
4. Run the handbook verifier and manifest tests.
5. Commit the handbook record and Gitlink only; never generated project output.

```bash
python3 -m unittest tests/test_reference_manifest.py -v
python3 scripts/verify_handbook.py
```
