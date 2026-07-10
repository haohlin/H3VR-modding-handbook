# Development Flow and Environment Boundary

## Use this route when

You need to decide where a task belongs, how changes become Git changes, or how
a reference example becomes a real H3VR mod change.

## Authoritative environments

| Concern | Authoritative location |
| --- | --- |
| H3VR managed assemblies, BepInEx code builds, package/deploy, logs, VR tests | Windows H3VR-Mods checkout |
| Unity scenes, objects, prefabs, assets, and MeatKit builds | Windows MeatKit-Lite workspace |
| Unity content Git source | Dedicated Unity content repository rooted at MeatKit-Lite Assets/Projects |
| Tutorials, source inspection, and upstream examples | This macOS handbook and its submodules |

The handbook is intentionally read-only with respect to live game development.
It may explain a workflow and pin source references, but it does not replace the
Windows build wrapper, live assemblies, Unity editor, r2modman profile, or VR
test.

## Daily flow

1. Inspect the relevant Windows repository status before editing.
2. Use Unity for Unity-owned moves and object edits so matching meta files stay
   synchronized.
3. Build and package with the established Windows workflow for the mod type.
4. Deploy only a packaged artifact.
5. Test the authored interaction in game and record log/runtime evidence.
6. Commit source assets, metadata, code, documentation, and configuration; do
   not commit generated bundles, caches, DLLs, artifacts, or credentials.

## Reference use

Submodules are learning material and source snapshots. Do not edit nested
repository contents from this superproject. Update a submodule pin only after
reviewing the upstream change and the handbook impact.

## Primary references

- [H3VR Modding Wiki: MeatKit source](../references/H3VR-Modding/wiki/src/creating/meatkit)
- [H3VR Modding Wiki: scripting source](../references/H3VR-Modding/wiki/src/creating/scripting)
- [MeatKit source](../references/H3VR-Modding/MeatKit)
- [Source policy](../SOURCES.md)

