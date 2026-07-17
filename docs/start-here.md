# Start Here

Use this page to choose one H3VR modding route before opening a project. Each
route tells you what belongs in Unity, code, data, a package, and a real H3VR
test.

> [!IMPORTANT]
> The handbook is the map. The authoritative Windows projects are where you
> edit, build, package, deploy, and validate the work.

## Pick the deliverable, not the tool

| I am changing… | Open this route | Finish condition |
| --- | --- | --- |
| A scene, prefab, material, mesh, audio, or MonoBehaviour | [Development flow](development-flow.md) | The correct Windows Unity or MeatKit-Lite workspace is selected |
| A map, T&H layout, lighting setup, or navmesh | [Map authoring](maps/overview.md) | The map survives a VR gameplay and performance pass |
| A firearm or item | [Custom items: Unity -> OLP -> Mason](weapons/custom-weapons-stratum-mason.md) | The item spawns, works, saves, and logs cleanly |
| BepInEx or Harmony behaviour | [Code and data mods](mod-code/bepinex-harmony-and-data.md) | The live target is verified and the plugin passes a runtime check |
| Generated pools or profiles | [Code and data mods](mod-code/bepinex-harmony-and-data.md) | Deterministic staged data reaches the active runtime registry |
| A GunGame map or progression pool | [GunGame](gungame/overview.md) | The correct branch passes its mode-specific runtime test |
| Supply Raid content | [Supply Raid](supply-raid/overview.md) | The Supply Raid scene and mode data load together |
| A Thunderstore package | [Package -> test -> release](releases/thunderstore.md) | Package contents and dependencies pass review before publication |

## The shared working loop

The implementation differs by route, but a completed change always has the
same evidence trail:

1. **Read the route and its boundaries.** Learn which source is authoritative
   and which compatibility or provenance caveat applies.
2. **Make the change in the real Windows project.** Keep Unity assets with
   their `.meta` files and use the project-supported build/deploy workflow.
3. **Inspect the produced artifact.** Check package contents, object IDs,
   registrations, dependencies, or scene data before treating a build as done.
4. **Run H3VR and observe the real interaction.** Use logs plus the relevant
   VR/gameplay test, not compilation alone.
5. **Commit intentional source and evidence.** Exclude Unity caches, bundles,
   profiles, and other generated noise.

> [!TIP]
> If two routes appear to apply, start with the deliverable the player will
> receive. A custom firearm is an item route even if it also includes code;
> follow the code guide only for its separate plugin/data concern.

## Continue learning

- [How to use the handbook](using-the-handbook.md) for online, local, and
  source-record reading modes.
- [Development flow](development-flow.md) for the Windows-authoritative
  workspace boundary.
- [Navigation index](navigation/index.md) for the complete topic map.
- [H3VR Modding Wiki source](https://github.com/H3VR-Modding/wiki) for upstream
  reference material.
