# Custom Weapons → OtherLoader → Mason

| Use this for | Keep separate |
| --- | --- |
| Custom firearm / item | Unity authoring, asset loading, package flow |

~~~mermaid
flowchart LR
  unity[1. Unity object] --> loader[2. OtherLoader assets]
  loader --> mason[3. Mason / Stratum package]
  mason --> vr[4. H3VR VR test]
~~~

## Four gates

| Gate | Verify |
| --- | --- |
| **1 · Unity** | Controls, feeds, mounts, IDs, materials, audio, build inclusion |
| **2 · Loader** | Asset paths + load model match target OtherLoader version |
| **3 · Package** | Mason/Stratum version is stated; package/dependencies are correct |
| **4 · Runtime** | Item loads, spawns, interacts, and logs stay clean |

> ⚠️ The wiki labels OtherLoader/Mason packaging links legacy. Record the exact
> Unity, MeatKit, OtherLoader, Mason, and Stratum versions you verify.

## Primary references

- [Raw workflow note](../sources/user-provided/2026-07-10-custom-weapons-stratum-mason.md)
- [OtherLoader](https://github.com/devyndamonster/OtherLoader)
- [Mason docs](https://github.com/H3VR-Modding/Mason/tree/main/docs/src)
- [Stratum](https://github.com/H3VR-Modding/Stratum)
