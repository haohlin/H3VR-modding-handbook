# H3VR Modding Handbook Topic Map

This map shows how the handbook subjects connect. Use it to build a mental
model or to spot a related concern; use [Handbook Navigation](index.md) when
you want a direct next link.

```mermaid
flowchart LR
  handbook[H3VR Modding Handbook]

  subgraph start[Start and environment]
    selector[Route selection]
    boundary[Windows-authoritative flow]
  end

  subgraph unity[Unity and MeatKit]
    items[Items and prefabs]
    scenes[Atlas and scenes]
    builds[MeatKit builds]
  end

  subgraph weapons[Custom weapons]
    olp[OtherLoaderPatched assets]
    stratum[Stratum]
    mason[Mason packaging]
  end

  subgraph maps[Maps and performance]
    tnh[Take and Hold layout]
    physics[Colliders and navmesh]
    lighting[Baked lighting and probes]
    profiling[SteamVR and VR validation]
  end

  subgraph code[Code and data mods]
    bepinex[BepInEx and Harmony]
    generator[Deterministic generators]
    registry[Active runtime registry]
  end

  subgraph modes[Game modes]
    gungame[GunGame: maps and pools]
    supplyraid[Supply Raid: SDK and content]
  end

  subgraph release[Release evidence]
    package[Package inspection]
    logs[Runtime logs]
    vrtest[VR test]
  end

  subgraph sources[Sources and provenance]
    authored[Authored guides]
    raw[User-provided notes]
    cards[External source cards]
    pins[29 pinned Git references]
  end

  handbook --> start
  handbook --> unity
  handbook --> weapons
  handbook --> maps
  handbook --> code
  handbook --> modes
  handbook --> release
  handbook --> sources

  unity --> weapons
  unity --> maps
  code --> modes
  weapons --> package
  maps --> vrtest
  modes --> vrtest
  package --> logs
  sources --> authored
  raw --> authored
  cards --> authored
  pins --> authored
```

## Read the connections correctly

- **Unity and MeatKit** are common foundations; they are not replacements for
  a particular item, map, or game-mode workflow.
- **OLP, Stratum, and Mason** meet in a custom-item package, but each has a
  different responsibility: runtime loading, content structure, and package
  construction.
- **GunGame and Supply Raid** inherit map/content concerns, then add
  mode-specific registration and runtime acceptance checks.
- **Source records and pins** support every route with traceable evidence. They
  do not prove a current release or a successful runtime test on their own.
