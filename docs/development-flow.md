# Development Flow

## Workspace map

| Work | Authoritative place | This handbook |
| --- | --- | --- |
| H3VR APIs, plugins, data, package, deploy, logs | Windows H3VR-Mods | Route + reference only |
| Scenes, prefabs, assets, MeatKit builds | Windows MeatKit-Lite | Route + reference only |
| Unity content versioning | Dedicated Unity content repository | Explains the boundary |
| Tutorials and source examples | This repository | Yes |

~~~mermaid
flowchart LR
  handbook[Handbook / references] --> select[Select route]
  select --> win[Windows source workspace]
  win --> package[Build + package]
  package --> deploy[Deploy]
  deploy --> vr[VR test + logs]
  vr --> commit[Commit real source]
~~~

## Rules

| ✅ Do | ❌ Do not |
| --- | --- |
| Move Unity objects in Unity | Hand-copy Unity assets between projects |
| Commit assets with matching meta files | Commit Unity Library / Temp / bundles |
| Use the Windows wrapper to deploy | Copy DLLs directly into a profile |
| Treat submodules as read-only references | Edit nested reference projects here |
| Test the real interaction in H3VR | Call a compile a VR pass |

## Primary references

- [Start Here](start-here.md)
- [H3VR Modding Wiki: MeatKit](../references/H3VR-Modding/wiki/src/creating/meatkit)
- [H3VR Modding Wiki: scripting](../references/H3VR-Modding/wiki/src/creating/scripting)
- [MeatKit](../references/H3VR-Modding/MeatKit)
- [Source policy](../SOURCES.md)

