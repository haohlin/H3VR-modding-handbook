# Supply Raid

Use this route for Supply Raid map/content authoring. It keeps the general map
workflow separate from the Supply Raid Editor/SDK and the mode-specific runtime
test that proves a scene is actually usable in Supply Raid.

> [!IMPORTANT]
> Supply Raid reference material is version-sensitive. The handbook pins SRE
> 1.3.0 as evidence and does not claim that it is compatible with every newer
> H3VR, Unity, or Supply Raid release.

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

## Choose the branch that owns the question

| Change | Open |
| --- | --- |
| Supply Raid scene / gameplay layout | [Map authoring](map-authoring.md) |
| General Unity map work | [H3VR map overview](../maps/overview.md) |
| Supply Raid source / SDK examples | [Packer Supply Raid 1.3.0](https://github.com/Packer/H3VR-Supply-Raid/tree/SRE-1.3.0) |
| Supply Raid tool/release links | [Supply Raid source card](../sources/external/supply-raid.md) |

> ⚠️ This handbook pins SRE-1.3.0 as a reference. Treat it as an example and
> verify compatibility before using a newer H3VR, Unity, or Supply Raid release.

## The Supply Raid acceptance story

~~~mermaid
flowchart LR
  reference[Study SRE editor and SDK boundary] --> scene[Author scene and mode data]
  scene --> package[Build intended assets and scene]
  package --> load[Load in Supply Raid]
  load --> gameplay[Validate player and Sosig flow]
  gameplay --> logs[Inspect logs and record compatibility]
~~~

The scene, mode data, package contents, and runtime behavior are one result.
Passing a generic map test is valuable, but it cannot replace the Supply Raid
mode test.

## Sources and credit

- [Supply Raid map authoring](map-authoring.md)
- [Supply Raid 1.3.0 source](https://github.com/Packer/H3VR-Supply-Raid/tree/SRE-1.3.0)
- [Supply Raid SDK](https://github.com/Packer/H3VR-Supply-Raid/tree/SRE-1.3.0/Supply%20Raid%20SDK)
- [Source card](../sources/external/supply-raid.md)
