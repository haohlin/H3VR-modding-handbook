# GunGame Weapon Pools

Use this guide for the data that determines GunGame progression. A pool is
correct only when its deterministic source data resolves through the active
runtime registry and every selected object remains physically usable in H3VR.

> [!IMPORTANT]
> The active runtime object registry is the source of truth. Installed content
> or a generated file on disk is not proof that GunGame can select the object.

~~~mermaid
flowchart LR
  registry[Active runtime registry] --> generate[Deterministic generation]
  generate --> validate[Validate IDs + feeds]
  validate --> test[Runtime pool test]
~~~

| Rule | Use |
| --- | --- |
| Source of truth | Active runtime object registry |
| Generation | Explicit seed; staging output |
| Feeds | Magazine → clip/speedloader → cartridges |
| Optics | Verified physical mount only |
| Fallbacks | Keep safe pools until registry refresh completes |

## Build a pool as a reproducible data product

1. Read the active runtime registry rather than a stale list or decompiled
   snapshot.
2. Generate from an explicit seed into staging output, so a candidate pool can
   be reproduced and inspected.
3. Validate object IDs and firearm feeds: magazine first, then clip/speedloader,
   then cartridges where applicable.
4. Include optics only when a real physical mount is verified.
5. Keep a safe fallback pool while the registry refreshes, then run the result
   against the enabled content set.

## Exit gate: what the runtime must prove

- [ ] Every object ID resolves
- [ ] Every gun has compatible feed
- [ ] Attachments physically fit
- [ ] Pool is tested against enabled content

## Sources and credit

- [GunGame overview](overview.md)
- [Raw GunGame note](../sources/user-provided/2026-07-10-gungame-notes.md)
- [GunGame project](https://github.com/KacperObara/H3VR-GunGame)
