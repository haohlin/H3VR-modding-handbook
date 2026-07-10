# H3VR Map Authoring Overview

## Use this route when

You are creating or changing an H3VR map scene, Atlas/WurstMod layout, Take and
Hold data, player spawns, item spawners, Sosig behaviour, or map-wide Unity
objects.

## Authoring checklist

1. Select the mapping route and tool version first. Atlas is the current
   sample-based route; WurstMod is a valuable legacy reference for existing
   maps and Take and Hold structure.
2. Keep a clear root level object. Put map-global audio, scripts, generic-level
   setup, Take and Hold setup, and map-wide colliders under that boundary.
3. Group room content by stable descriptive names. Keep Generic and Take and
   Hold configuration separately switchable where export modes differ.
4. Place Take and Hold data deliberately: attacker vectors, blockers, barriers,
   cover, encryption zones, defenders, supply points, panels, cases, respawns,
   and scoreboard space all need in-game reachability tests.
5. Build collision for gameplay, not visual fidelity. Prefer primitive colliders
   and correct physical materials.
6. Bake and inspect navmesh, lighting, reflection probes, light probes, and
   occlusion after meaningful geometry changes.
7. Export through the selected map workflow and run actual in-game tests before
   treating an editor result as correct.

## Quality gates

- The player cannot fall through the world.
- Sosigs reach intended routes without spawning in walls or deadlocking.
- Encryptions, panels, cases, and respawns are visible and usable.
- Relevant map modes load with no missing references.
- A representative VR run shows acceptable physics, rendering, and audio
  performance.

## Primary references

- [Map performance and VR testing](performance-and-vr-testing.md)
- [Raw Prometheus notes](../sources/user-provided/2026-07-10-prometheus-map-modding-notes.md)
- [H3VR Modding Wiki mapping source](../../../references/H3VR-Modding/wiki/src/creating/mapping)
- [Atlas sample scenes](../../../references/H3VR-Modding/AtlasSampleScenes)
- [WurstMod source](../../../references/Nolenz/WurstMod)

