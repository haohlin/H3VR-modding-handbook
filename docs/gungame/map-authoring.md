# GunGame Map Authoring

## Use this route when

You are laying out a map that needs to support GunGame gameplay rather than only
a generic H3VR scene.

## Checklist

1. Start with the upstream GunGame map-making tutorial and identify its required
   scene objects, spawn locations, and registration data.
2. Design the route around frequent weapon transitions: provide usable space for
   different weapon classes, reloads, close-range fights, and long-range shots.
3. Validate player spawns, enemy routes, respawns, collision, and visibility in
   the actual GunGame mode.
4. Profile physics, audio, lighting, and draw cost with realistic gameplay
   equipment, not only an empty editor camera.
5. Re-test after changing blockers, navmesh, lighting, or any scene registration
   object.

## Primary references

- [GunGame overview](overview.md)
- [GunGame map wiki source](../../../references/KacperObara/H3VR-GunGame.wiki)
- [Map performance and VR testing](../maps/performance-and-vr-testing.md)

