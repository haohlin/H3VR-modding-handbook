# BepInEx, Harmony, and Data Mods

## Use this route when

You are creating a code plugin, patching an H3VR method, or generating runtime
data such as progression pools.

## Code-plugin checklist

1. Work in the Windows H3VR-Mods repository on a focused feature branch.
2. Run the local preflight and confirm the decompiled source cache matches the
   live managed assemblies before selecting a Harmony target.
3. Inspect the target signature from the generated read-only source cache.
4. Register every patch target in the build registry so verification catches
   game API drift.
5. Build, package, and deploy through the Windows wrapper. Do not copy DLLs
   directly into a profile.
6. VR-test the behaviour and inspect BepInEx logs before considering the change
   ready.

## Data-generator checklist

1. Make generation deterministic with an explicit seed.
2. Write output to staging, not tracked package source.
3. Validate generated IDs and invariants with repository tests.
4. Package through the normal wrapper and validate runtime data against active
   registries.

## Primary references

- [Development flow](../development-flow.md)
- [H3VR Plugin Template](../../references/H3VR-Modding/H3VRPluginTemplate)
- [H3VR Modding Wiki scripting source](../../references/H3VR-Modding/wiki/src/creating/scripting)
- [GunGame weapon pools](../gungame/weapon-pools.md)

