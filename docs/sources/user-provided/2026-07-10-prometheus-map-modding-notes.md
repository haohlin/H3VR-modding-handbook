# Prometheus Map Modding Notes — Detailed Raw Record

Source: H3VR map-modding notes and transcript supplied in the project conversation.
Provided by: H3VR Modding Contributor
Captured: 2026-07-10
Redistribution: user-provided conversation material
Fidelity: Text-rich preservation record. This is source material, not the
handbook's condensed navigation guide.

The supplied material is a brain dump from the author of the Prometheus modded
map. It is intentionally detailed, including observations that were uncertain,
version-specific, or explicitly described as needing testing.

## Collected links and tools

H3VR Modding: https://h3vr-modding.github.io/wiki/

WurstMod: https://github.com/Nolenz/WurstMod/wiki/

SteamVR frame timing: https://developer.valvesoftware.com/wiki/SteamVR/Frame_Timing

Performance notes based on feedback from Anton: a Google Doc link was supplied
in the conversation but was truncated.

Unity culling code: https://blogs.unity3d.com/2016/12/20/

Runtime debugging tool: https://github.com/ManlyMarco/RuntimeUnityEditor

Unity scripting: https://docs.unity3d.com/550/Documentation/ScriptReference/

Garret Polk scripts: https://bitbucket.org/GarretPolk/h3vr/

Lighting: https://cgcookie.com/articles/art-of-lighting-in-blender

Reflection probes: https://docs.unity3d.com/Manual/AdvancedRefProbe.html

BepInEx troubleshooting: https://bepinex.github.io/bepinex_docs/

Alloy: https://github.com/Josh015/Alloy

The original note also named Technie Collider Creator, Bakery, a hidden-game-
object helper for Bakery, Asset Store assets, a Discord attachment, and several
truncated Asset Store/Google Doc URLs. Preserve those links in the external
source cards when a complete URL becomes available.

The original author tested on an Nvidia 2070 Super, Intel i7-6700K at 4 GHz,
and 32 GB DDR4-3000. That hardware is context, not a universal performance
target.

## Hierarchy and map root

Everything intended for export lives under one Level GameObject. The author
uses that Level object like a singleton: map-global audio, colliders spanning
the map, generic-level setup, Take and Hold setup, and scripts that walk child
objects belong near this root.

Rooms receive descriptive names. The point is not only level design; it makes
production and bug tracking possible. A note such as “bug is in tree room” is
more useful than searching an unstructured hierarchy.

Generic-level content and Take and Hold content are grouped separately. This
allows one group to be enabled and the other disabled when exporting/testing a
specific mode, rather than manually toggling every individual object.

## Take and Hold placement notes

Bounds exist on hold and supply data. The original author did not claim to know
their exact implementation; they were sized to cover the furthest useful area
and all visible combat space.

Nav blockers are the transparent walls that appear when a hold begins. Their
visual mesh and collider can differ. The collider needs the NavBlock layer and
must not be static because it is dynamic at runtime. Their renderer can use
custom materials.

Barriers are the smaller cover walls that rise during a hold. Cover points
teach the AI where it may hide. Put them where a Sosig can plausibly be between
the player and a useful obstruction, especially along likely entrances.

Keep the hold node low enough to reach. The source note used roughly 0.2 m
below normal placement rather than forcing the player to reach high.

Encryption placement needs repeated in-game testing. Static, stealth, and
regenerative encryption can place elements where the player cannot see or
shoot them. Avoid high/low extremes, ledges, simplified collision that does not
match the visual mesh, and spaces behind walls. Temporary/fake colliders can
block rays from selecting invalid ledges.

Turret placement was called uncertain in the source. Treat turrets as likely
AI destination/engagement positions and verify actual game behaviour.

Attack vectors are Sosig spawn locations. Keep them out of immediate player
view, but do not place them so far away that a hold timer progresses before
combat arrives. Grenade positions use forward direction, so inspect the local
arrow/orientation.

Defenders respawn at their positions when a hold resets. Their forward/local
orientation matters. Supply-point player spawn orientation matters as well.

Supply panels should stay reachable and grouped conveniently. Use at least the
number required by the character. Cases and tables need practical opening
orientation. The source note observed that tables may have no collision, so a
player may walk through one to reach an awkward case.

Put scoreboard space away from the active map when possible so occlusion can
remove it. Use simplified collision there because its static colliders are not
cheaply removed. The scoreboard may need manual rotation adjustment in runtime.

## Prefabs and collision

Unity 5.6 does not provide nested prefabs. The source strongly recommends
turning repeated modular geometry and even one-off hallway combinations into
prefabs. That makes broad lighting, mesh, or light-probe changes manageable and
keeps special pieces discoverable.

Physics is one of the largest H3VR performance costs. Do not use mesh colliders
unless necessary. If a mesh collider is necessary, use the simplest convex
form possible. Prefer boxes, spheres, cylinders, and other primitive colliders.

The source author described converting complex asset-pack meshes into a small
set of boxes and warned that early Prometheus versions used expensive mesh
colliders and performed poorly even on high-end GPUs. For grid layouts, large
overlapping floor/ceiling box colliders can replace many mesh colliders.

If the player falls through the world, inspect: static flag, Environment layer,
enabled collider, non-trigger setting, physical-material component, and spawn
height. If Sosigs fall, wiggle, or glue themselves to floors, inspect navmesh
height versus collider geometry.

Physical material is important. The material definition changes impact sound,
particles, deflection, penetration, and related behavior. The source suggests
always attaching a PMat component to a collider and using an editor check to
find colliders that lack one.

## Shaders, materials, and lighting

The source recommends matching the Alloy shader family when H3VR effects such
as flashlights need expected behavior. Non-Alloy materials can show square or
incorrect flashlight effects. Fewer materials reduce draw/set-pass calls; the
Prometheus example used a small material set, separating shiny floors from
non-shiny surfaces.

For indoor VR maps, use baked lighting where possible. Turn off realtime global
illumination; baked global illumination is the intended path. Realtime lights
and screen-space effects can be expensive in VR.

Bakery was used for lightmaps/light probes. Its hidden FTrace Lightmaps object
must be moved under the export Level hierarchy once so it is included in the
asset bundle. The source note warns that a Unity Light component marked baked
can become realtime in H3VR; use the Bakery light component for Bakery lights
instead of keeping both components.

The stated bake sequence is: bake navigation, render Bakery lighting and light
probes, render reflection probes, bake occlusion data, then export. For quick
lighting tests, reduce texels per unit and disable denoising; final bakes can
use higher settings. The source used low-to-moderate texture density to manage
map size and VRAM.

## Reflection probes and light probes

Reflection probes are baked camera-like snapshots. Keep them at likely player
positions, use the lowest useful resolution, and keep their coverage simple.
Blend mode over overlapping probes is expensive. Simple mode and deliberate
probe importance avoid repeated blending/search work.

The source warns that Unity may linearly search active reflection probes every
frame. It describes custom visibility/culling scripts that disable reflection
probes when their area cannot be seen, reducing active probes from many to only
the few near the player.

Light probes supply baked-light information to dynamic objects such as guns,
Sosigs, and particles. Place them around walls, corners, lights, and movement
space. A probe on the wrong side of a wall can make dynamic objects use lighting
from outside the playable space. Carry different guns through the level to find
black, wrong-color, or abrupt lighting transitions. More probes can improve
transitions; the original source considered them comparatively light on
performance.

## Occlusion and navmesh

Use Unity occlusion culling for rooms, halls, and distant scoreboard space.
Create a temporary camera to visualize what occlusion actually renders. Tune
smallest occluder/hole settings to map scale, then bake and inspect the result.

The source describes WurstMod loading/deleting a classic map while leaving old
navigation data. To avoid overlap, it moved the custom map to approximately
500,500 rather than origin. Do not move excessively far from origin: physics
precision degrades at large distances, with roughly 10 km given as the scale
where error becomes meaningful.

Bake navmesh using Sosig-scale settings. Test every doorway, stairs, raised
threshold, and room. Do not blindly mark ceilings unwalkable: the source found
that this could remove navigation below them. Mark only genuinely forbidden
surfaces, such as hazards, and then re-bake.

## Audio, reverb, and custom code

Startup sounds and ambient hums can be 2D. Positional machine sounds should use
3D blend with Doppler normally set to zero unless the Doppler effect is wanted;
otherwise Unity computes it continuously. Use custom rolloff so distant beeps
do not mix unnecessarily.

WurstMod reverb areas use box colliders, NoCollider layer, and priority rather
than blending. They may overlap. Test presets because names do not always
describe perceived room size.

Editor-only scripts remain Unity editor scripts. Runtime map code needs a DLL
placed beside WurstMod/plugins. The workflow described is edit code in Visual
Studio, compile DLL, let Unity reload it, then export/test. The source also
describes simple scripts for camera draw distance and visibility-driven audio,
particles, rotating components, and reflection-probe enablement.

## Debugging and VR test procedure

The Unity editor is useful for draw/set-pass inspection but cannot prove H3VR
performance. Use SteamVR’s desktop frame-timing window, not only the HMD graph.
Enable BepInEx console/logging and Unity error logging.

Test with a physics-heavy weapon, attachments, laser, flashlight, magazine,
and movement. Move and collide with the environment; static framerate is not
enough. Use a laser to inspect where collision exists rather than where a mesh
appears. Use flashlight behavior to check materials. Use reflective weapons and
brass to inspect reflection/light probes.

For Take and Hold testing, use an invulnerable/custom health setup, item
spawner, radar, and an appropriate character. Watch for spawned Sosigs outside
the map or inside collision. Test HDR, bloom, quality modes, shadows, lasers,
and flashlight behavior deliberately.

## Original chapter index

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

