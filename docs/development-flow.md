# Development Flow

Use this page to keep handbook research separate from the project that produces
the mod. It explains where a change belongs and what counts as a real result.

> [!IMPORTANT]
> Windows is authoritative for source editing, builds, packages, deployment,
> logs, and VR validation. This repository documents the workflow and pins
> references; it does not replace the Windows workspaces.

## Where work lives

| Work | Authoritative place | Handbook role | Evidence of completion |
| --- | --- | --- | --- |
| H3VR APIs, plugins, data, packages, deployment, and logs | Windows `H3VR-Mods` | Route and source context | Runtime behavior and log evidence |
| Scenes, prefabs, assets, and MeatKit builds | Windows `MeatKit-Lite` | Unity/loader workflow | Built content tested in H3VR |
| Unity-content versioning | Dedicated Unity-content repository | Boundary explanation | Source plus matching `.meta` files |
| Tutorials, source cards, and examples | This handbook | Public learning/reference library | Reviewed Markdown and source provenance |

## From question to verified change

```mermaid
flowchart LR
  handbook[Handbook: route and sources] --> scope[Choose the real workspace]
  scope --> edit[Edit authoritative source]
  edit --> inspect[Build or package, then inspect output]
  inspect --> deploy[Use the supported deployment workflow]
  deploy --> runtime[H3VR, VR, and log test]
  runtime --> evidence[Commit intentional source and results]
```

The important transition is between **understanding** and **editing**. The
handbook can explain the loader, package, or map system, but it cannot confirm
your installed profile, a Unity visual result, or a VR interaction. Those are
observations in the real runtime.

## Working agreement for Codex and humans

Use the [H3VR development skill](../skills/h3vr-mod-development/SKILL.md) when
working with Codex. The operating model changes slightly with the medium, not
with the quality bar:

| Change | Collaboration pattern | Human decision remains necessary when… |
| --- | --- | --- |
| Code or data | Codex inspects API/registry -> edits -> builds/packages -> reports evidence | A release or product decision changes scope |
| Unity content | Human establishes visual intent -> Codex automates repeatable work -> Unity/MeatKit test | The result depends on visual feel or subjective VR interaction |
| Release | Prepare, inspect, test, and document | The package is published publicly |

## Guardrails that prevent expensive mistakes

| Do | Why it matters | Do not |
| --- | --- | --- |
| Move Unity objects in Unity | Preserves references and editor state | Hand-copy Unity assets between projects |
| Commit assets with their matching meta files | Keeps stable GUID relationships | Commit `Library`, `Temp`, or generated bundles |
| Use the Windows wrapper to deploy | Keeps profiles and runtime setup reproducible | Copy DLLs directly into a profile |
| Treat submodules as read-only evidence | Preserves reviewed upstream snapshots | Edit nested reference projects in this handbook |
| Test the real interaction in H3VR | Compilation is not player behavior | Call a successful compile a VR pass |

## Verify the boundary before you begin

- You can name the Windows project that owns the change.
- You know the output artifact you will inspect: package, DLL, data staging
  result, scene, or registered runtime object.
- You have a player/runtime test and a log location in mind.
- You will commit only intentional source and documentation.

## Primary references

- [Start Here](start-here.md)
- [How to use the handbook](using-the-handbook.md)
- [H3VR Modding Wiki: MeatKit](https://github.com/H3VR-Modding/wiki/tree/main/src/creating/meatkit)
- [H3VR Modding Wiki: scripting](https://github.com/H3VR-Modding/wiki/tree/main/src/creating/scripting)
- [MeatKit](https://github.com/H3VR-Modding/MeatKit)
- [Source policy](../SOURCES.md)
