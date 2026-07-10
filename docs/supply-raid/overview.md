# Supply Raid

| Use this for | Keep separate |
| --- | --- |
| Supply Raid map/content authoring | Generic maps, GunGame maps, code-only mods |

~~~mermaid
flowchart LR
  sr[Supply Raid 1.3.0 reference] --> editor[Supply Raid Editor / SDK]
  editor --> map[Supply Raid map content]
  map --> package[Build + package]
  package --> test[Run Supply Raid test]
~~~

## Choose the branch

| Change | Open |
| --- | --- |
| Supply Raid scene / gameplay layout | [Map authoring](map-authoring.md) |
| General Unity map work | [H3VR map overview](../maps/overview.md) |
| Supply Raid source / SDK examples | [Packer Supply Raid 1.3.0](../../references/Packer/H3VR-Supply-Raid-SRE-1.3.0) |
| Supply Raid tool/release links | [Supply Raid source card](../sources/external/supply-raid.md) |

> ⚠️ This handbook pins SRE-1.3.0 as a reference. Treat it as an example and
> verify compatibility before using a newer H3VR, Unity, or Supply Raid release.

## Primary references

- [Supply Raid map authoring](map-authoring.md)
- [Supply Raid 1.3.0 source](../../references/Packer/H3VR-Supply-Raid-SRE-1.3.0)
- [Supply Raid SDK](../../references/Packer/H3VR-Supply-Raid-SRE-1.3.0/Supply%20Raid%20SDK)
- [Source card](../sources/external/supply-raid.md)

