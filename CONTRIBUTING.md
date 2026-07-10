# Contributing

~~~mermaid
flowchart LR
  change[Proposed change] --> type{What type?}
  type -->|Guide| guide[Edit docs + links]
  type -->|External source| card[Add source card]
  type -->|Git project| submodule[Add pin + manifest]
  guide --> verify[Run verifier]
  card --> verify
  submodule --> verify
~~~

## Contribution map

| Change | Add / update |
| --- | --- |
| Guide improvement | Route guide + navigation index |
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
