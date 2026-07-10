# Map Performance and VR Testing

## Use this route when

The map runs slowly, has lighting/collision issues, needs a performance budget,
or is ready for an in-game validation pass.

## Performance-first checklist

1. Simplify collision. Use boxes, spheres, and other primitives whenever they
   represent gameplay space adequately. Treat mesh colliders as exceptions.
2. Verify every static environmental collider has the intended layer, is not a
   trigger, and has a suitable physical material.
3. Bake navmesh against real collision. Test door widths, stairs, ceilings,
   ledges, and room transitions with Sosigs.
4. Prefer baked lighting in VR. Avoid unexpected realtime Unity lights in the
   exported game and keep transparent effects restrained.
5. Use reflection probes sparingly. Bake them, avoid unnecessary overlap, and
   keep renderer probe mode simple where possible.
6. Fill dynamic-object travel space with light probes. Test using reflective and
   non-reflective weapons rather than editor-only previews.
7. Bake and visualize occlusion. Room/hallway structure should hide work that
   the player cannot see.
8. Use a realistic physics-heavy weapon, attachments, laser, flashlight, and
   movement pattern for testing. Static editor framerate is not a VR budget.
9. Use SteamVR frame timing and BepInEx/Unity error logging to locate CPU, GPU,
   physics, and runtime failures.

## Interaction tests

- Use lasers to reveal collision versus visible geometry.
- Carry weapons through light-probe transitions and dark corners.
- Check flashlights against the chosen shader/material setup.
- Inspect radar and logs for out-of-bounds or stuck Sosigs.
- Test quality settings deliberately; HDR/bloom and physics load can expose
  problems hidden by an editor preview.

## Primary references

- [Map overview](overview.md)
- [Raw Prometheus notes](../sources/user-provided/2026-07-10-prometheus-map-modding-notes.md)
- [Collected external resources](../sources/external/collected-resources.md)
- [Alloy source](../../references/Josh015/Alloy)
- [H3VR Modding Wiki mapping source](../../references/H3VR-Modding/wiki/src/creating/mapping)

