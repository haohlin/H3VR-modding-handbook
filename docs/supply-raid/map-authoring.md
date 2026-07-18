# Supply Raid Map Authoring

Use this guide after confirming the relevant Supply Raid reference and SDK
boundary. You will author a scene and its mode-specific content, package the
intended assets, then validate the actual player and Sosig flow in Supply Raid.

> [!WARNING]
> Do not copy a whole reference project into production. Study the editor, SDK,
> and asset patterns, then keep your own authored source and matching `.meta`
> files under version control.

## Build from reference to runtime evidence

### Follow the owner baseline first

Packer's official package page gives the minimum mapper setup. Use the source
page for exact current instructions; its captured baseline is:

1. Install Unity `5.6.7f1`, set up MeatKit, and import Atlas.
2. Add basic Atlas Scene Settings to the scene, then import the Supply Raid SDK.
3. Place `SR_Scene` and at least two `SR_SupplyPoint` prefabs from the SDK.
4. Add the Supply Raid dependency to the build profile and build as a regular
   sandbox map.

For component-specific detail after that baseline, use Packer's official
[Supply Raid Wiki](https://thunderstore.io/c/h3vr/p/Packer/SupplyRaid/wiki/),
especially its Map Components, SDK, and Supply Points pages.

> [!NOTE]
> This is owner-provided published guidance, captured 2026-07-18. It is
> separate from the handbook's pinned SRE 1.3.0 study reference; verify the
> package/source version boundary before relying on either for a current build.

| Step | Confirm |
| --- | --- |
| **Reference** | Owner baseline is read; SRE 1.3.0 editor/SDK study path and target versions are known |
| **Scene** | Collision, navmesh, lighting, and gameplay lanes are usable |
| **Mode data** | Supply Raid-specific objects/config are included intentionally |
| **Package** | Correct scene/assets are in the package |
| **Runtime** | Supply Raid loads; player/Sosig flow works; logs are clean |

Each step depends on the previous one: scene quality cannot compensate for
missing mode data, and package contents cannot prove that Supply Raid registers
or runs the content correctly.

## Reuse safely and preserve ownership

| ✅ Do | ❌ Do not |
| --- | --- |
| Study the pinned Editor, SDK, and asset projects | Copy an entire reference project into production |
| Keep authored source + matching meta files | Commit Unity caches or generated bundles |
| Test in the actual Supply Raid mode | Assume a generic map test is enough |

## Sources and credit

- [Supply Raid overview](overview.md)
- [Official Supply Raid package / mapper baseline](https://thunderstore.io/c/h3vr/p/Packer/SupplyRaid/)
- [Official Supply Raid Wiki](https://thunderstore.io/c/h3vr/p/Packer/SupplyRaid/wiki/)
- [Supply Raid 1.3.0 source](https://github.com/Packer/H3VR-Supply-Raid/tree/SRE-1.3.0)
- [Supply Raid SDK](https://github.com/Packer/H3VR-Supply-Raid/tree/SRE-1.3.0/Supply%20Raid%20SDK)
- [Owner guidance and source/release boundary](../sources/external/supply-raid.md)
- [General map performance + VR test](../maps/performance-and-vr-testing.md)
