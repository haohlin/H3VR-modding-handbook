# Map Performance + VR Test

Use this guide when a map is slow, visibly wrong, leaves Sosigs stuck, or is
approaching a release decision. Reproduce one symptom, inspect the relevant
layer, change one likely cause, then run the same H3VR scenario again.

> [!NOTE]
> A high frame rate in an empty editor view is not a VR performance result. Test
> movement, Sosigs, a physics-heavy weapon, the game's lighting, and the
> quality settings a player will use.

| Use this for | Output |
| --- | --- |
| Slow map, bad lighting, stuck Sosigs, release candidate | A VR-tested performance checklist |

## Start from the symptom you can observe

| Symptom | First check | Prefer |
| --- | --- | --- |
| Physics hitching | Collider count / complexity | Primitive colliders |
| Sosigs stuck | Navmesh vs collision | Re-bake after geometry changes |
| Gun goes black | Light-probe coverage | Add probes on travel path |
| Shiny / wrong reflections | Probe overlap | Baked, simple probe selection |
| Too many drawn rooms | Occlusion data | Bake / visualize occlusion |
| Bad flashlight | Shader/material | H3VR-compatible material path |

~~~mermaid
flowchart LR
  symptom[Reproduce one symptom] --> inspect[Inspect the affected system]
  inspect --> isolate[Choose one likely bottleneck]
  isolate --> fix[Make one focused change]
  fix --> rebake[Re-bake affected data]
  rebake --> rerun[Repeat the same VR scenario]
  rerun -->|Still fails| inspect
  rerun -->|Passes| record[Record result]
~~~

## Build a purposeful VR test kit

| Bring | Why |
| --- | --- |
| Physics-heavy weapon | Collision + CPU load |
| Laser | Reveal real collider shape |
| Flashlight | Check shader response |
| Reflective weapon | Check light/reflection probes |
| SteamVR timing + BepInEx logs | Find CPU/GPU/runtime faults |

The kit turns a visual or performance complaint into evidence. For example, a
laser exposes real collider shape, while a flashlight and reflective weapon
show whether lighting/probes fail during a normal player path.

## Exit gate: evidence before release

- [ ] Move, collide, shoot, reload
- [ ] Spawn and fight Sosigs
- [ ] Walk every lighting transition
- [ ] Check quality settings deliberately
- [ ] Read logs after the run and record the first relevant failure signal

## Sources and credit

- [Map authoring](overview.md)
- [Raw Prometheus notes](../sources/user-provided/2026-07-10-prometheus-map-modding-notes.md)
- [Alloy](https://github.com/Josh015/Alloy)
