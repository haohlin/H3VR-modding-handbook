# BepInEx, Harmony + Data

~~~mermaid
flowchart LR
  change[Code / data change] --> api[Check live API / registry]
  api --> build[Build + package]
  build --> deploy[Deploy with wrapper]
  deploy --> vr[VR test + logs]
~~~

| Work | Required checks |
| --- | --- |
| **Harmony / code** | Live signature, registered target, build, package, deploy, logs |
| **Data generator** | Explicit seed, staging output, IDs/invariants, active registry |
| **Both** | Windows authoritative workflow + runtime test |

## Do / do not

| ✅ | ❌ |
| --- | --- |
| Use the Windows wrapper | Copy DLLs into a profile |
| Check game API before patching | Trust stale decompiled source |
| Generate into staging | Mutate tracked release data |
| Validate live registry | Assume installed = enabled |

## Primary references

- [Development Flow](../development-flow.md)
- [Plugin template](../../references/H3VR-Modding/H3VRPluginTemplate)
- [GunGame pools](../gungame/weapon-pools.md)

