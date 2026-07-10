# Map Performance + VR Test

| Use this for | Output |
| --- | --- |
| Slow map, bad lighting, stuck Sosigs, release candidate | A VR-tested performance checklist |

~~~mermaid
flowchart LR
  collision[Collision] --> nav[Navmesh]
  nav --> bake[Light + probes + occlusion]
  bake --> load[Load in H3VR]
  load --> profile[SteamVR + logs]
  profile --> fix[Fix one bottleneck]
~~~

## Fast diagnosis

| Symptom | First check | Prefer |
| --- | --- | --- |
| Physics hitching | Collider count / complexity | Primitive colliders |
| Sosigs stuck | Navmesh vs collision | Re-bake after geometry changes |
| Gun goes black | Light-probe coverage | Add probes on travel path |
| Shiny / wrong reflections | Probe overlap | Baked, simple probe selection |
| Too many drawn rooms | Occlusion data | Bake / visualize occlusion |
| Bad flashlight | Shader/material | H3VR-compatible material path |

## VR test kit

| Bring | Why |
| --- | --- |
| Physics-heavy weapon | Collision + CPU load |
| Laser | Reveal real collider shape |
| Flashlight | Check shader response |
| Reflective weapon | Check light/reflection probes |
| SteamVR timing + BepInEx logs | Find CPU/GPU/runtime faults |

## Exit gate

- [ ] Move, collide, shoot, reload
- [ ] Spawn and fight Sosigs
- [ ] Walk every lighting transition
- [ ] Check quality settings deliberately
- [ ] Read logs after the run

## Primary references

- [Map authoring](overview.md)
- [Raw Prometheus notes](../sources/user-provided/2026-07-10-prometheus-map-modding-notes.md)
- [Alloy](../../references/Josh015/Alloy)

