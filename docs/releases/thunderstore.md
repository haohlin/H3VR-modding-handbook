# Package → Test → Release

Use this guide when a mod has reached the point where another player could
install it. A package is ready for publication only after its intentional
contents, dependencies, supported deployment, and real H3VR behavior have been
inspected.

> [!IMPORTANT]
> Publication is a separate decision. The final gate requires explicit user
> approval even after all technical checks pass.

| Gate | Must be true |
| --- | --- |
| Source | Intentional files only |
| Package | Manifest, README, icon, payload, dependencies correct |
| Deploy | Installed through supported workflow |
| Runtime | Interaction works; logs are clean |
| Publish | User explicitly approves release |

## Read the gates as evidence, not ceremony

1. **Source:** review the diff; keep intentional source, metadata, and docs,
   never caches, profiles, or generated Unity noise.
2. **Package:** inspect the manifest, README, icon, payload, and dependencies
   that a player will receive.
3. **Deploy:** install through the supported workflow so the runtime setup is
   repeatable.
4. **Runtime:** perform the relevant interaction/VR test and inspect logs.
5. **Publish:** record the result, then obtain explicit approval before any
   public release action.

## Release evidence checklist

| Evidence | What it answers |
| --- | --- |
| Reviewed source diff | Did only intentional files enter the release? |
| Generated manifest | Are package identity and dependencies correct? |
| Package contents | Will the player receive exactly the intended payload? |
| H3VR and log test | Does the shipped interaction work in the runtime? |
| Explicit approval | Is public publication authorized now? |

## Sources and credit

- [Development Flow](../development-flow.md)
- [H3VR Modding Wiki: Thunderstore](https://github.com/H3VR-Modding/wiki/tree/main/src/creating/thunderstore)
- [Mason packaging](https://github.com/H3VR-Modding/Mason/blob/main/docs/src/getting_started/packaging.md)
