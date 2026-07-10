# Custom Weapons with OtherLoader, Stratum, and Mason

## Use this route when

You are creating a custom firearm or item in Unity and need to choose an asset
loading and package path.

## Workflow

1. Set up the real Windows MeatKit-Lite project with the required Unity and game
   references. Keep source assets and their meta files in the dedicated Unity
   content repository.
2. Implement and validate the weapon/object graph in Unity. Test controls,
   feeds, magazines, attachment mounts, colliders, materials, audio, object IDs,
   build-profile inclusion, and in-game interaction.
3. If the package needs on-demand asset loading, configure OtherLoader according
   to the exact OtherLoader version you target.
4. If the project uses Stratum/Mason, follow the Mason preparation,
   compilation, assets, dependencies, and packaging documentation for the exact
   Mason and Stratum versions installed.
5. Build/package in the selected toolchain, deploy through the correct runtime
   workflow, and VR-test before release.

## Compatibility rule

The maintained H3VR Modding Wiki currently categorizes its OtherLoader and
Mason packaging links as legacy. That does not make the supplied workflow
invalid; it means the guide must state the verified tool versions and must not
silently assume compatibility with a newer loader, package format, or Unity
setup.

## Do not skip

- Asset bundles are not a substitute for a test of object IDs, load order, or
  item-spawner availability.
- Mason/Stratum packaging is not a substitute for a Unity interaction test.
- A successful package is not a release until runtime logs and VR behaviour are
  clean.

## Primary references

- [Raw custom-weapons notes](../sources/user-provided/2026-07-10-custom-weapons-stratum-mason.md)
- [OtherLoader source](../../references/devyndamonster/OtherLoader)
- [Mason raw documentation](../../references/H3VR-Modding/Mason/docs/src)
- [Stratum source](../../references/H3VR-Modding/Stratum)
- [H3VR Modding Wiki custom-object source](../../references/H3VR-Modding/wiki/src/creating)

