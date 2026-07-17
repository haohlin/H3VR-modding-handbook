# GunGame

Use this route when the player should advance through a weapon progression on
kills and demote on death. Start by separating the map/gameplay space from the
generated progression pool; both must be tested against the active runtime.

> [!NOTE]
> **Core loop:** kills advance the weapon; death demotes the weapon. A map that
> feels right without its real pool, or a pool that resolves outside its enabled
> registry, is not a complete GunGame result.

~~~mermaid
flowchart LR
  gungame[GunGame] --> map[Map route]
  gungame --> pools[Weapon-pool route]
  map --> vr[Runtime test]
  pools --> registry[Active registry validation]
~~~

| Change | Open |
| --- | --- |
| Map layout, spawns, gameplay space | [Map authoring](map-authoring.md) |
| Progression weapons / generated data | [Weapon pools](weapon-pools.md) |
| General H3VR map | [Map overview](../maps/overview.md) |

## What kind of GunGame change are you making?

| If the player will notice… | Start with | Then prove |
| --- | --- | --- |
| Layout, spawns, lanes, or encounter space | [Map authoring](map-authoring.md) | Spawns, routes, progression combat, and VR performance |
| Progression weapons or generated data | [Weapon pools](weapon-pools.md) | IDs, feeds, physical compatibility, and the active registry |
| A wider scene concern | [General map overview](../maps/overview.md) | The generic map acceptance gate plus GunGame behavior |

## Sources and credit

- [Raw GunGame note](../sources/user-provided/2026-07-10-gungame-notes.md)
- [GunGame project](https://github.com/KacperObara/H3VR-GunGame)
- [Local map-tutorial snapshot](map-tutorial-snapshot.md)
