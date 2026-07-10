# Start Here

## Choose the deliverable

| Deliverable | Route | Finish on |
| --- | --- | --- |
| Scene, prefab, material, mesh, audio, MonoBehaviour | [Unity / MeatKit flow](development-flow.md) | Windows MeatKit-Lite |
| Map, T&H layout, lighting, navmesh | [Maps](maps/overview.md) | Windows Unity + VR |
| Firearm or item | [Custom weapons](weapons/custom-weapons-stratum-mason.md) | Unity + loader/package + VR |
| BepInEx / Harmony behaviour | [Code mods](mod-code/bepinex-harmony-and-data.md) | Windows H3VR-Mods |
| Generated pools / profiles | [Data mods](mod-code/bepinex-harmony-and-data.md) | Windows staging + runtime registry |
| GunGame map or pool | [GunGame](gungame/overview.md) | Correct branch + runtime test |
| Thunderstore package | [Release](releases/thunderstore.md) | Verified package |

~~~mermaid
flowchart TD
  choose{What changes?}
  choose -->|Unity object / content| unity[MeatKit-Lite]
  choose -->|Map| maps[Map guide]
  choose -->|Gun / item| weapon[Weapon guide]
  choose -->|Code / data| code[H3VR-Mods]
  choose -->|GunGame| game[GunGame guide]
  choose -->|Release| release[Release guide]
~~~

## Always do this

1. **Read** the route guide and its primary references.
2. **Edit** the authoritative Windows project.
3. **Build / package** with that project's workflow.
4. **Test** in H3VR; inspect logs.
5. **Commit** source, metadata, and docs — never caches or generated artifacts.

## Primary references

- [Development Flow](development-flow.md)
- [Navigation index](navigation/index.md)
- [How to use the handbook](using-the-handbook.md)
- [H3VR Modding Wiki source](../references/H3VR-Modding/wiki)

