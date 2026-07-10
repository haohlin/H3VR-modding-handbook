# GunGame Weapon Pools

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

## Exit gate

- [ ] Every object ID resolves
- [ ] Every gun has compatible feed
- [ ] Attachments physically fit
- [ ] Pool is tested against enabled content

## Primary references

- [GunGame overview](overview.md)
- [Raw GunGame note](../sources/user-provided/2026-07-10-gungame-notes.md)
- [GunGame project](https://github.com/KacperObara/H3VR-GunGame)
