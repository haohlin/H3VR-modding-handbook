# GunGame Map Authoring

~~~mermaid
flowchart LR
  tutorial[Read GunGame map tutorial] --> layout[Build gameplay lanes]
  layout --> spawn[Check spawns + routes]
  spawn --> vr[Run GunGame in VR]
~~~

| Check | Pass condition |
| --- | --- |
| Weapon space | Supports close + long range weapons |
| Spawns / respawns | No traps, collisions, or bad facing |
| Enemy routes | Reliable combat pathing |
| Performance | Tested with real gameplay equipment |
| Registration | Works in GunGame, not only editor |

## Primary references

- [GunGame overview](overview.md)
- [Local map-tutorial snapshot](map-tutorial-snapshot.md)
- [Map performance + VR test](../maps/performance-and-vr-testing.md)
