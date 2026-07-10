# H3VR Map Authoring

| Use this for | Do not use this for |
| --- | --- |
| Atlas/WurstMod scenes, T&H layout, spawns, navmesh | Code-only plugins or weapon pools |

~~~mermaid
flowchart LR
  layout[Layout] --> play[Gameplay objects]
  play --> bake[Bake: nav / light / occlusion]
  bake --> export[Export]
  export --> vr[VR test]
~~~

## Build order

| # | Add | Quick rule |
| --- | --- | --- |
| 1 | **Map root + rooms** | One root; clear room names |
| 2 | **Gameplay** | Spawns, panels, cases, T&H data |
| 3 | **Collision** | Prefer primitive colliders + PMat |
| 4 | **Bake** | Navmesh → lighting/probes → occlusion |
| 5 | **VR test** | Player, Sosigs, interactions, performance |

## Take and Hold placement

| Group | Check |
| --- | --- |
| Attack vectors | Hidden from view; close enough to engage |
| Encryptions | Visible and shootable |
| Defenders / player | Correct local facing direction |
| Panels / cases | Reachable; cases open cleanly |
| Nav blockers / barriers | Match gameplay lanes |

## Export gate

- [ ] Player cannot fall through
- [ ] Sosigs navigate intended routes
- [ ] Panels, cases, encryptions, respawns work
- [ ] Map mode loads with no missing references
- [ ] VR run is acceptable

## Primary references

- [Performance + VR test](performance-and-vr-testing.md)
- [Raw Prometheus notes](../sources/user-provided/2026-07-10-prometheus-map-modding-notes.md)
- [Atlas samples](https://github.com/H3VR-Modding/AtlasSampleScenes)
- [WurstMod](https://github.com/Nolenz/WurstMod)
