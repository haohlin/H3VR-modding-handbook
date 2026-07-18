# H3VR Map Authoring

Use this guide for Atlas/WurstMod scenes, Take and Hold layouts, spawns,
lighting, navmesh, and the performance work that makes a map playable in VR.
It is not a plugin-only or weapon-pool workflow.

> [!IMPORTANT]
> A scene that looks correct in the Unity editor is not yet a map result. The
> acceptance test is movement, combat, interaction, performance, and logs in a
> real H3VR session.

| Use this for | Do not use this for |
| --- | --- |
| Atlas/WurstMod scenes, T&H layout, spawns, navmesh | Code-only plugins or weapon pools |

## Build the map from player experience outward

Start with readable player routes, sight lines, and combat lanes. Add gameplay
objects to spaces that support them, then make collision, navigation, lighting,
and occlusion agree with the final geometry.

### Atlas starting point

For a new Atlas scene, begin with the official [Atlas getting-started
requirements](https://h3vr-modding.github.io/wiki/creating/mapping/atlas/getting_started/1_requirements.html):
an existing MeatKit project with Atlas imported. Continue from its linked
**Basics** page for scene setup. This handbook adds workflow and validation
context; Atlas documentation remains the primary setup reference.

| # | Add | Quick rule |
| --- | --- | --- |
| 1 | **Map root + rooms** | One root; clear room names |
| 2 | **Gameplay** | Spawns, panels, cases, T&H data |
| 3 | **Collision** | Prefer primitive colliders + PMat |
| 4 | **Bake** | Navmesh → lighting/probes → occlusion |
| 5 | **VR test** | Player, Sosigs, interactions, performance |

> [!TIP]
> Re-bake navmesh, lighting/probes, or occlusion whenever a geometry change can
> affect it. Otherwise an editor-correct scene can hide a runtime mismatch.

## Place Take and Hold objects as a playable system

| Group | Check |
| --- | --- |
| Attack vectors | Hidden from view; close enough to engage |
| Encryptions | Visible and shootable |
| Defenders / player | Correct local facing direction |
| Panels / cases | Reachable; cases open cleanly |
| Nav blockers / barriers | Match gameplay lanes |

Each row is a player-facing promise: an attack vector should create an
engagement, a panel should be reachable, and a barrier should support the lane
rather than merely occupy the scene.

## Exit gate: what a playable map proves

- [ ] Player cannot fall through
- [ ] Sosigs navigate intended routes
- [ ] Panels, cases, encryptions, respawns work
- [ ] Map mode loads with no missing references
- [ ] VR run is acceptable with representative gameplay equipment and settings

## Sources and credit

- [Performance + VR test](performance-and-vr-testing.md)
- [Raw Prometheus notes](../sources/user-provided/2026-07-10-prometheus-map-modding-notes.md)
- [Atlas getting-started requirements](https://h3vr-modding.github.io/wiki/creating/mapping/atlas/getting_started/1_requirements.html)
- [Atlas samples](https://github.com/H3VR-Modding/AtlasSampleScenes)
- [WurstMod](https://github.com/Nolenz/WurstMod)
