# How to Use the Handbook

## Select a mode

| Mode | Goal | First action |
| --- | --- | --- |
| **Browse** | Find a guide or source | [Start Here](start-here.md) |
| **Study locally** | Search raw Markdown / examples | Clone with submodules |
| **Build a mod** | Change real content or code | Open Windows workspace |

~~~mermaid
flowchart LR
  browse[Browse guide] --> refs[Primary references]
  clone[Clone submodules] --> search[Search source]
  build[Real mod work] --> windows[Windows workspace]
~~~

## Clone the library

~~~bash
git clone --recurse-submodules https://github.com/h3vr-modding/H3VR-modding-handbook.git
cd H3VR-modding-handbook
python3 scripts/verify_handbook.py
~~~

| Need | Command |
| --- | --- |
| Initialize all references later | git submodule update --init --recursive |
| Initialize one reference | git submodule update --init references/H3VR-Modding/Mason |
| Verify handbook | python3 scripts/verify_handbook.py |

## Read the library correctly

| Content | Meaning |
| --- | --- |
| **Guides** | Compact, visual route and validation checklist |
| **Raw notes** | Detailed user-provided text, context, caveats, and links; re-check version-sensitive claims |
| **Source cards** | External link + attribution |
| **Submodules** | Pinned upstream source; do not edit here |

The compact guides are indexes, not replacements for raw source material. When
you need the original reasoning, troubleshooting detail, or exact supplied
links, open the matching file in [Source archive](sources/README.md).

## Before changing a real mod

**Guide → primary source → Windows workspace → build/package → VR/log test.**

## Primary references

- [Start Here](start-here.md)
- [Navigation index](navigation/index.md)
- [Source archive](sources/README.md)
- [Contributing](../CONTRIBUTING.md)
