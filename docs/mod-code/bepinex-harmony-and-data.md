# BepInEx, Harmony + Data

Use this guide for a BepInEx/Harmony behavior change, a generated pool/profile,
or a combination of the two. It prevents a common mistake: treating a compiled
DLL or generated file as proof that the running H3VR registry actually uses it.

> [!IMPORTANT]
> Installed does not mean enabled, and compiled does not mean called. Validate
> the live registry or target in the runtime that will actually use the result.

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

## Build from the source of truth

For a Harmony/code change, check the live API signature and registered target
before patching. For a data generator, use an explicit seed, produce staging
output, validate IDs/invariants, and confirm the active runtime registry owns
the result. In both cases, use the Windows wrapper to deploy and test the
behavior in H3VR rather than inferring it from a build artifact.

## Keep the safety boundaries visible

| ✅ | ❌ |
| --- | --- |
| Use the Windows wrapper | Copy DLLs into a profile |
| Check game API before patching | Trust stale decompiled source |
| Generate into staging | Mutate tracked release data |
| Validate live registry | Assume installed = enabled |

## Runtime acceptance questions

| Question | Evidence that answers it |
| --- | --- |
| Did the intended code execute? | Target-specific behavior plus relevant BepInEx logs |
| Did generated IDs resolve? | A validation pass against the active runtime object registry |
| Do relationships work? | Representative feeds, attachments, and physical mount checks |
| Can the result be reproduced? | Explicit seed, staged output, supported deploy path, and recorded source version |

## Sources and credit

- [Development Flow](../development-flow.md)
- [Plugin template](https://github.com/H3VR-Modding/H3VRPluginTemplate)
- [GunGame pools](../gungame/weapon-pools.md)
