# Supply Raid Map Authoring

~~~mermaid
flowchart LR
  ref[Inspect SR Editor + SDK] --> scene[Author scene / content]
  scene --> mode[Configure Supply Raid mode data]
  mode --> build[Build package]
  build --> test[Run Supply Raid]
~~~

## Build checklist

| Step | Confirm |
| --- | --- |
| **Reference** | SRE 1.3.0 editor/SDK path and target versions are known |
| **Scene** | Collision, navmesh, lighting, and gameplay lanes are usable |
| **Mode data** | Supply Raid-specific objects/config are included intentionally |
| **Package** | Correct scene/assets are in the package |
| **Runtime** | Supply Raid loads; player/Sosig flow works; logs are clean |

## Reuse safely

| ✅ Do | ❌ Do not |
| --- | --- |
| Study the pinned Editor, SDK, and asset projects | Copy an entire reference project into production |
| Keep authored source + matching meta files | Commit Unity caches or generated bundles |
| Test in the actual Supply Raid mode | Assume a generic map test is enough |

## Primary references

- [Supply Raid overview](overview.md)
- [Supply Raid 1.3.0 source](../../references/Packer/H3VR-Supply-Raid-SRE-1.3.0)
- [Supply Raid SDK](../../references/Packer/H3VR-Supply-Raid-SRE-1.3.0/Supply%20Raid%20SDK)
- [General map performance + VR test](../maps/performance-and-vr-testing.md)

