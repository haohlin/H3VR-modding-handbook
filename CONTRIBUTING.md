# Contributing

Contributions should make a real H3VR route easier to understand without losing
the source, author, or version boundary behind it. Start by deciding whether
you are improving authored guidance, preserving supplied context, or pinning an
upstream reference.

> [!TIP]
> A strong documentation contribution gives the reader an outcome, a useful
> visual or decision aid, an observable validation step, and direct credit for
> the evidence it relies on.

~~~mermaid
flowchart LR
  change[Proposed change] --> type{What type?}
  type -->|Guide| guide[Edit route + visual flow + validation]
  type -->|External source| card[Add source card]
  type -->|Git project| submodule[Add pin + manifest]
  guide --> verify[Run verifier]
  card --> verify
  submodule --> verify
~~~

## Contribution map

| Change | Add / update |
| --- | --- |
| Guide improvement | Relevant route, a clear reader outcome, a useful visual/decision aid, verification, and updated navigation when the route changes |
| External source | Source card with provenance header |
| Upstream Git source | Submodule + manifest + navigation |
| Raw user note | Detailed user-provided source file + provenance; preserve substance, context, and links rather than replacing it with a summary, table, or diagram |

## Never add

| ❌ | Why |
| --- | --- |
| Game DLLs / Steam files / profiles | Not public reference material |
| Unity Library / Temp / bundles | Generated noise |
| Credentials | Security |
| Unlicensed third-party copies | Attribution / redistribution |

## Review the contribution as a reader would

| Ask | Good evidence |
| --- | --- |
| Can a new reader tell when this route applies? | Clear outcome and scope at the page start |
| Does the page explain a consequential decision? | A natural explanation plus a diagram/table where it clarifies |
| Does it prove completion? | Runtime, package, log, or source-verification result |
| Is the original work credited? | Author/publisher, direct source link, capture/pin context |
| Is the repository still clean? | No game files, caches, bundles, credentials, or copied third-party text |

## Verify

~~~bash
python3 -m unittest tests/test_reference_manifest.py -v
python3 scripts/verify_handbook.py
~~~

## Update one submodule

~~~bash
git -C references/H3VR-Modding/Mason fetch origin
git -C references/H3VR-Modding/Mason checkout <reviewed-commit-or-tag>
git add references/H3VR-Modding/Mason
python3 scripts/verify_handbook.py
~~~

Report a guide problem with: **page + source + tool versions + observed result +
safe log excerpt**.
