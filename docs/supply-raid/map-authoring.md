# Supply Raid Map Authoring

Use this guide after confirming the relevant Supply Raid reference and SDK
boundary. You will author a scene and its mode-specific content, package the
intended assets, then validate the actual player and Sosig flow in Supply Raid.

> [!WARNING]
> Do not copy a whole reference project into production. Study the editor, SDK,
> and asset patterns, then keep your own authored source and matching `.meta`
> files under version control.

~~~mermaid
flowchart LR
  ref[Inspect SR Editor + SDK] --> scene[Author scene / content]
  scene --> mode[Configure Supply Raid mode data]
  mode --> build[Build package]
  build --> test[Run Supply Raid]
~~~

## Build from reference to runtime evidence

| Step | Confirm |
| --- | --- |
| **Reference** | SRE 1.3.0 editor/SDK path and target versions are known |
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
- [Supply Raid 1.3.0 source](https://github.com/Packer/H3VR-Supply-Raid/tree/SRE-1.3.0)
- [Supply Raid SDK](https://github.com/Packer/H3VR-Supply-Raid/tree/SRE-1.3.0/Supply%20Raid%20SDK)
- [General map performance + VR test](../maps/performance-and-vr-testing.md)
