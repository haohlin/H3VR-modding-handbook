# AI-in-the-Loop Unity Asset Inspection

Use this route when an existing scope, item, or package can answer a narrow
technical question, but its files are not source material to reuse. It turns
read-only inspection into a small, reviewable evidence set instead of a pile of
exported assets.

```text
Known package or bundle
  + source SHA-256
  + headless structural manifest
  + Unity batch audit
  + AI evidence review
  + targeted original implementation
  + Unity and H3VR validation
```

This is useful for questions such as: Which components cooperate to render a
PIP scope? Which material properties control a lens? Which references must be
recreated in a new MeatKit prefab? It is not a shortcut for visual judgement or
an asset-reuse pipeline.

## Safety and source boundary

Inspect only material you may access and evaluate. Keep game and third-party
assets out of public repositories, release packages, and source-control history
unless their license and permission explicitly allow them. Make new meshes,
textures, reticles, materials, and package content from original or licensed
work.

The durable research record should be a manifest with an input hash and a
written conclusion, not a raw rip. This supports peer review without exposing
or redistributing asset payloads.

## Repeatable inspection loop

### 1. Freeze one input

Choose one bundle or release archive. Record its SHA-256 before reading it. A
hash makes later conclusions traceable to the exact source that produced them.

### 2. Make a structural manifest

Run a headless parser that reports only configuration-oriented data:

- Unity version and object-type counts;
- asset and component names;
- selected serialized field paths related to scope, PIP, reticle, lens, camera,
  material, shader, and adjustment controls; and
- material/shader names and keywords.

The parser must stage inputs in disposable storage and not emit textures,
meshes, audio, or raw serialized payload to the project.

### 3. Cross-check in Unity batch mode

Load each candidate bundle in batch mode and record an independent list of
assets, component types, material shader names, and relevant serialized
property paths. Parser output alone can be incomplete when custom serialized
types lack type information. Unity’s batch mode provides a second source of
evidence without requiring an interactive editor session. [Unity command-line
arguments](https://docs.unity3d.com/Manual/command-line-arguments.html)

### 4. Give AI bounded evidence

Supply the agent with:

- inspection manifest and input hash;
- question being answered;
- H3VR/Unity version boundary; and
- current project constraints and source ownership.

Ask for evidence-backed relationships, missing information, and targeted next
checks. Good output distinguishes observed fields from hypotheses. It should not
claim a shader’s appearance, interaction feel, or package compatibility from
names alone.

### 5. Rebuild only what evidence supports

Create original Unity objects and scripts in the owning project. For a PIP
scope, verify separately: render camera, render texture, lens material,
reticle/zero path, adjustment interactions, prefab wiring, MeatKit inclusion,
and in-H3VR behavior. Keep implementation facts in the mod’s design and status
records.

### 6. Validate and remove disposable copies

Do not remove older research output until the replacement manifest has a known
input hash, completed parser pass, completed Unity audit, and reviewed result.
Then remove only exact obsolete directories that no active project or test uses.
Preserve manifest and conclusion; discard raw staged copies.

## Where AI helps and where a person decides

| AI can do reliably | Human judgement remains necessary |
| --- | --- |
| Compare manifests, find component/reference patterns, propose focused checks, draft scripts/tests, and detect missing package wiring | Lens appearance, reticle readability, ergonomic knob behavior, real depth/eye alignment, VR comfort, and public release approval |

Current AI editor integrations target newer Unity generations and should not be
treated as compatibility proof for legacy projects. Prefer a tool that produces
plain JSON plus a deterministic batch audit over a generic agent that edits a
project directly. UnityPy is suitable for structural inspection; AssetRipper is
an interactive investigation fallback when a manifest cannot answer the
question. [UnityPy](https://github.com/K0lb3/UnityPy) · [AssetRipper
documentation](https://assetripper.github.io/AssetRipper/) · [Unity AI getting
started](https://unity.com/blog/unity-ai-how-to-get-started)

## PIP-scope checklist

- [ ] Input SHA-256 recorded.
- [ ] Parser manifest complete; no raw asset payload retained in project.
- [ ] Unity batch audit complete for every candidate bundle.
- [ ] PIP camera, target texture, lens material, reticle path, and adjustment
      components identified or explicitly unknown.
- [ ] Original project implementation built through MeatKit.
- [ ] Unity package inspection and H3VR interaction test passed.
- [ ] Old disposable rips removed only after above evidence exists.

## Continue from here

- [Development Flow](development-flow.md) for project/runtime boundaries.
- [Custom items: Unity -> OLP -> Mason](weapons/custom-weapons-stratum-mason.md)
  for item/package authoring.
- [Package -> test -> release](releases/thunderstore.md) for public release
  gates.
