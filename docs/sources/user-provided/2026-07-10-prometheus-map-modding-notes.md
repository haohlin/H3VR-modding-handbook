# Prometheus Map Modding Notes

Source: H3VR map-modding notes and transcript supplied in the project conversation.
Provided by: H3VR Modding Contributor
Captured: 2026-07-10
Redistribution: user-provided conversation material

## Resource list supplied with the notes

- H3VR Modding Wiki: https://h3vr-modding.github.io/wiki/
- WurstMod documentation: https://github.com/Nolenz/WurstMod/wiki/
- SteamVR frame timing: https://developer.valvesoftware.com/wiki/SteamVR/Frame_Timing
- Unity culling article: https://blogs.unity3d.com/2016/12/20/unitytips-cullinggroups-api/
- Runtime debugging tool: https://github.com/ManlyMarco/RuntimeUnityEditor
- BepInEx documentation: https://bepinex.github.io/bepinex_docs/
- Alloy shaders: https://github.com/Josh015/Alloy
- Garret Polk H3VR work: https://bitbucket.org/GarretPolk/h3vr/
- Unity reflection probes: https://docs.unity3d.com/Manual/AdvancedRefProbe.html

## Authoring and performance index

The supplied Prometheus material treats the level-root GameObject as the map
boundary and groups content by room. Global systems such as audio, generic
level setup, Take and Hold setup, map-wide colliders, and custom scripts live
near that root. Room objects use stable descriptive names to make debugging and
iteration practical.

### Take and Hold topics

- Bounds, nav blockers, barriers, cover, nodes, encryptions, turrets, attack
  vectors, defenders, supply points, panels, cases, tables, scoreboard, and
  respawn points.
- Test every encryption placement so targets are visible and shootable.
- Keep attacker spawns out of immediate sight but close enough to create useful
  combat timing.
- Set defender/player orientation deliberately using local transforms.
- Keep supply panels reachable and cases openable.

### World construction and physics

- Prefer simple primitive colliders. Avoid mesh colliders unless unavoidable;
  use convex, simplified forms when they are necessary.
- Floors, ceilings, and repeated grid geometry are candidates for shared box
  colliders. Validate collision placement with an in-game laser.
- Put static environmental colliders on the correct layer, do not make them
  triggers, and attach a physical-material component.
- Bake navmesh against the actual collision geometry. Check doors, stairs,
  narrow routes, elevated surfaces, and Sosig movement in game.

### Rendering and lighting

- Match H3VR-compatible Alloy shaders where needed for flashlight and material
  behaviour. Keep material count and transparent overdraw low.
- Prefer baked lighting for VR. Bakery, reflection probes, light probes, and
  occlusion data need to be inside the exported level hierarchy when their
  tooling requires it.
- Keep reflection probes few, baked, and simple. Avoid blended overlap where
  possible; use simple probe selection and cull inactive probes.
- Place light probes around dynamic-object travel paths. Carry a reflective
  weapon through rooms to spot light-probe gaps and bad transitions.
- Check HDR, bloom, quality settings, flashlight behaviour, and laser collision
  against the performance target rather than only in the Unity editor.

### Runtime and profiling

- Use custom scripts sparingly for camera range, visibility-driven audio,
  particles, animations, and reflection-probe culling.
- Use the non-HMD SteamVR frame-timing window for CPU/GPU timing.
- Enable BepInEx logging and Unity error output before testing.
- Test realistic physics-heavy weapons, attachments, lights, lasers, and
  movement. A map that looks fast while static can fail under active physics.

## Chapter index supplied with the transcript

00:00 Intro
01:38 Hierarchy
05:09 Take and Hold setup
05:25 Bounds
05:42 Nav blockers
06:19 Barriers
06:41 Cover
07:31 Node
07:47 Encryptions
10:00 Turrets
10:40 Attack vectors
12:36 Defenders
13:46 Supply points
14:04 Player spawn
14:24 Panels
15:15 Boxes
15:50 Tables
16:38 Scoreboard
18:12 Respawn point
18:42 Prefabs
20:39 Colliders and physics
22:33 Technie Collider Creator
24:15 Collider setup
25:26 Physical materials
27:43 Alloy shaders
31:53 Lighting
33:37 Bakery
37:54 Baking steps
41:48 Reflection probes
49:06 Light probes
55:43 Lights
57:50 Occlusion culling
59:44 Nav mesh
1:07:50 Audio
1:12:12 Reverb
1:13:54 Scripts
1:24:11 Debugging
1:27:01 SteamVR frame timing
1:28:23 BepInEx settings
1:29:24 VR in-game testing
1:31:22 Test guns
1:32:39 Brass reflections
1:33:07 Attachments and movement
1:35:10 Light probes
1:37:49 Lightmap resolution
1:40:01 HDR and bloom
1:42:13 Quality settings
1:43:02 Lasers
1:44:27 Flashlight

