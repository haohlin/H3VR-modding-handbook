# GunGame Map Authoring

Use this guide to turn a general H3VR map into a GunGame combat space. The goal
is not only a valid scene: it is a progression-friendly sequence of lanes,
spawns, and enemy routes that stays fair across close and long-range weapons.

> [!IMPORTANT]
> Editor registration is not enough. Run GunGame in H3VR to prove the mode sees
> the map and the combat loop survives real progression equipment.

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

## Author from progression pressure outward

1. Read the local tutorial snapshot for mode-specific setup context.
2. Block lanes that remain interesting when the active weapon changes range.
3. Test spawns and respawns under real combat so no start is trapped, colliding,
   or unfairly aimed.
4. Walk enemy routes in a live run; a visually plausible lane is not enough if
   navigation breaks the encounter.
5. Repeat the representative performance test with the mode enabled.

## Acceptance evidence

| Area | What a pass looks like |
| --- | --- |
| Weapon variety | The space supports close and long-range progression weapons |
| Starts | Spawns and respawns have safe collision, facing, and escape routes |
| Enemy flow | Sosigs create reliable combat paths instead of dead ends |
| Performance | A real gameplay loadout passes the relevant VR checks |
| Mode registration | GunGame loads the map in runtime, not merely in the editor |

## Sources and credit

- [GunGame overview](overview.md)
- [Local map-tutorial snapshot](map-tutorial-snapshot.md)
- [Map performance + VR test](../maps/performance-and-vr-testing.md)
