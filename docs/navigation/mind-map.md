# H3VR Modding Handbook Mind Map

The direct links are kept in the [navigation index](index.md) so they work in
plain-text viewers as well as on GitHub.

~~~mermaid
flowchart LR
  handbook[H3VR Modding Handbook]

  handbook --> start[Start and environment]
  start --> selector[Route selector]
  start --> boundary[Windows authoritative flow]

  handbook --> unity[Unity and MeatKit]
  unity --> item[Items and prefabs]
  unity --> atlas[Atlas and scenes]
  unity --> meatkit[MeatKit source]

  handbook --> weapons[Custom weapons]
  weapons --> implementation[Unity implementation]
  weapons --> otherloader[OtherLoaderPatched assets]
  weapons --> stratum[Stratum]
  weapons --> mason[Mason package flow]

  handbook --> maps[Maps and performance]
  maps --> tnh[Take and Hold layout]
  maps --> physics[Colliders and navmesh]
  maps --> lighting[Baked lighting and probes]
  maps --> profiling[SteamVR and VR validation]
  maps --> wurstmod[WurstMod reference]

  handbook --> code[Code and data mods]
  code --> bepinex[BepInEx and Harmony]
  code --> generator[Deterministic generators]
  code --> package[Build, package, deploy]

  handbook --> gungame[GunGame]
  gungame --> gungameMap[Map authoring]
  gungame --> pools[Weapon pools]
  gungame --> progression[Progression and demotion]

  handbook --> supplyraid[Supply Raid]
  supplyraid --> srEditor[Editor and SDK]
  supplyraid --> srMap[Map authoring]
  supplyraid --> srTest[Supply Raid runtime test]

  handbook --> release[Release]
  release --> logs[Runtime logs]
  release --> vrtest[VR test]
  release --> thunderstore[Thunderstore package]

  handbook --> sources[Sources and references]
  sources --> raw[User-provided raw notes]
  sources --> cards[External source cards]
  sources --> git[27 pinned Git submodules]
~~~
