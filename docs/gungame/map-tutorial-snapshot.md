# GunGame Map Tutorial Snapshot

**Local handbook version:** compact adaptation of the pinned GunGame wiki source.
It is readable on GitHub even when the upstream wiki/submodule page does not
render.

~~~mermaid
flowchart LR
  example[Start from ExampleScene] --> setup[Place + reference objects]
  setup --> package[Package map + optional pools]
  package --> test[Run GunGame]
~~~

## Required scene groups

| Group | Put it in | Configure |
| --- | --- | --- |
| **SosigSpawners** | Enemy spawn locations | Reference in MGR/SosigBehavior; set population, near/far exclusions, despawn distance, sight/hearing multipliers |
| **SosigWaypoints** | Patrol locations | Reference in SosigBehavior; rough patrol route |
| **PlayerSpawns** | Spawn/respawn locations | Reference in MGR and StartArea/InitialSpawn |
| **Weapon pools** | Mod package zip | Optional JSON; detected automatically; not tied to the map |
| **BufferWeaponsSpawnPos** | Hidden off-camera location | Next weapon + two magazines spawn here |
| **Music / Pause / Follower** | Desired gameplay location | Music optional; move PauseLever; PlayerFollower position does not matter |

## Build order

1. Start from the upstream ExampleScene/package.
2. Place spawners, waypoints, and player spawns.
3. Assign all references in MGR/SosigBehavior/StartArea.
4. Add optional pools and presentation objects.
5. Package and run GunGame; test spawns, patrols, respawns, and weapon flow.

## Source access

| Browser | Local clone |
| --- | --- |
| [Upstream GunGame repository](https://github.com/KacperObara/H3VR-GunGame) | references/KacperObara/H3VR-GunGame |
| [Upstream map wiki](https://github.com/KacperObara/H3VR-GunGame/wiki/Map-making-Tutorial) | references/KacperObara/H3VR-GunGame.wiki/Map-making-Tutorial.md |

## Primary references

- [GunGame map authoring](map-authoring.md)
- [GunGame overview](overview.md)
- [Raw GunGame note](../sources/user-provided/2026-07-10-gungame-notes.md)

