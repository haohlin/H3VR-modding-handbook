# GunGame

**Rule:** kills advance the weapon; death demotes the weapon.

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

## Primary references

- [Raw GunGame note](../sources/user-provided/2026-07-10-gungame-notes.md)
- [GunGame project](https://github.com/KacperObara/H3VR-GunGame)
- [Local map-tutorial snapshot](map-tutorial-snapshot.md)
