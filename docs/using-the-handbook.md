# How to Use the Handbook

Use this page to decide whether you should read online, clone the reference
library, inspect a source record, or open the real Windows workspace. It keeps
authored teaching, original evidence, and runtime work in their proper places.

## Choose a reading mode

| Mode | Use it when | First action | What it does not replace |
| --- | --- | --- | --- |
| **Browse** | You need a route or a documented decision | [Start Here](start-here.md) | The project/runtime test |
| **Study locally** | You need to search Markdown or inspect pinned examples | Clone with submodules | The authoritative source workspace |
| **Verify a source** | You need authorship, capture date, exact context, or a pin | [Source archive](sources/README.md) | A current compatibility check |
| **Build a mod** | You are changing code, content, data, or a package | Open the Windows workspace | This reference repository |

## Clone the library when research needs local search

```bash
git clone --recurse-submodules <repository-url>
cd H3VR-modding-handbook
python3 scripts/verify_handbook.py
```

| Need | Command | Expected result |
| --- | --- | --- |
| Initialize all references later | `git submodule update --init --recursive` | Every pinned source is available locally |
| Initialize one reference | `git submodule update --init references/H3VR-Modding/Mason` | The selected upstream project is available at its reviewed pin |
| Verify handbook integrity | `python3 scripts/verify_handbook.py` | Links, provenance, and reference records validate |

## Read each layer for what it is

| Content | What it gives you | How to treat it |
| --- | --- | --- |
| **Authored guides** | An explanation, visual model, procedure, and validation path | Use them as the first complete pass through a task |
| **Raw user-provided notes** | Detailed supplied context, caveats, and links | Preserve and consult them when original reasoning matters |
| **External source cards** | Attribution, capture context, scope, and direct links | Follow them to the publisher or upstream project |
| **Submodules** | A reviewed upstream source snapshot | Read-only evidence, not release/current-behavior proof |

> [!NOTE]
> A guide is allowed to teach deeply. It does not replace the source archive;
> it makes the source material easier to use without losing author credit or
> historical context.

## Before changing a real mod

Confirm this sequence is visible in your work:

1. A guide identifies the correct implementation route.
2. Primary sources resolve a version-sensitive or upstream question.
3. The authoritative Windows workspace owns the actual source change.
4. A package/build result is inspected before deployment.
5. H3VR, VR, and logs provide runtime evidence.

For read-only package research before authoring new Unity content, use
[AI-in-the-loop asset inspection](ai-in-the-loop-asset-inspection.md). It keeps
research evidence small and does not turn this public handbook into an asset
archive.

## Continue from here

- [Navigation index](navigation/index.md) for all routes and reference shelves.
- [AI-in-the-loop Unity asset inspection](ai-in-the-loop-asset-inspection.md)
  for manifest-first scope and package research.
- [Source archive](sources/README.md) for the retained detailed material.
- [Contributing](../CONTRIBUTING.md) for source, provenance, and verification
  expectations.
