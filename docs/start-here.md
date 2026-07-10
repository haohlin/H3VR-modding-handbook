# Start Here

## Use this route when

Choose the route by the deliverable you are changing, not by which tutorial you
saw first.

| You want to change | Start with | Finish in |
| --- | --- | --- |
| A scene, prefab, material, mesh, texture, audio, or MonoBehaviour | [Unity and MeatKit flow](development-flow.md) | Windows MeatKit-Lite and an in-game test |
| A map, Take and Hold layout, lighting, or navigation | [Map overview](maps/overview.md) | Windows Unity plus VR performance test |
| A custom firearm or item | [Custom weapons](weapons/custom-weapons-stratum-mason.md) | Windows Unity, loader/package validation, VR interaction test |
| A BepInEx or Harmony behaviour change | [Code and data mods](mod-code/bepinex-harmony-and-data.md) | Windows H3VR-Mods build, package, deploy, log, and VR test |
| Generated mode data or loadout pools | [Code and data mods](mod-code/bepinex-harmony-and-data.md) | Windows staging output and active-registry validation |
| A GunGame map or progression pool | [GunGame overview](gungame/overview.md) | Correct map/pool route, then Windows runtime validation |
| A Thunderstore release | [Release flow](releases/thunderstore.md) | Verified package and explicit publish approval |

## First checks

1. Identify the source repository that owns the change.
2. Keep the Windows workspace authoritative for every edit that affects H3VR
   runtime behaviour.
3. Read the corresponding raw upstream documentation below references/ before
   changing a compatibility-sensitive object, loader, or package.
4. Treat successful compilation as one verification layer, not proof of correct
   in-game or VR behaviour.

## Primary references

- [Development flow](development-flow.md)
- [Navigation index](navigation/index.md)
- [H3VR Modding Wiki source](../../references/H3VR-Modding/wiki)
- [Source archive](sources/)

