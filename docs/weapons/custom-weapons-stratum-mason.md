# Custom Items: Unity -> OtherLoaderPatched -> Mason

Use this tutorial for a custom firearm or item that must appear in H3VR's item
spawner, work as a real object, and ship in a package. You will author the
content in Unity, register it with OtherLoaderPatched (OLP), package it through
MeatKit/Mason, then prove the result in the authoritative Windows environment.

> [!IMPORTANT]
> This is a new-content workflow. Existing OtherLoader mods do not need to be
> republished merely to change their loader dependency; OLP is designed to run
> existing content when a player has it installed.

## At a glance

| You are responsible for | OLP is responsible for | Mason/MeatKit is responsible for |
| --- | --- | --- |
| Prefab, `FVRObject`, item identity, relationships, and spawner intent | Loading item data, registering it, and resolving its asset bundle | Building the bundle/package and declaring generated dependencies |

~~~mermaid
flowchart LR
  subgraph unity[Author in Unity]
    prefab[Prefab + controls + assets]
    fvr[FVRObject + unique ItemID]
    entry[ItemSpawnerEntry]
  end
  subgraph package[Build a package]
    root[OLP MeatKit build root]
    bundle[Data bundle + late_ prefab bundle]
    manifest[Thunderstore manifest]
  end
  subgraph runtime[Validate in H3VR]
    loader[OLP loads and registers item]
    spawner[Spawner, vault, and tag view]
    vr[Real VR interaction + logs]
  end
  prefab --> fvr --> entry --> root --> bundle --> manifest --> loader --> spawner --> vr
~~~

## Know the loader boundary before you build

OtherLoaderPatched is Sirdoggy's replacement for devyndamonster's original
OtherLoader. It preserves `h3vr.otherloader` and the public OtherLoader API so
existing OtherLoader content can run under OLP; it takes priority when both are
installed. Use OLP tools for a new build.

> [!NOTE]
> The pinned OLP source currently contains a `2.1.0` manifest, but this is a
> source snapshot, not publication proof. The source card records the published
> Thunderstore boundary separately. Always inspect the generated manifest and
> actual package page before shipping.

See [OLP source and credits](../sources/external/otherloader-patched.md).

## Build the item in five deliberate steps

### 1. Make a normal H3VR object first

Create prefab, `FVRObject`, controls, feeds, mounts, materials, audio, and
matching metadata in the authoritative Windows Unity project. Give every
`FVRObject` a unique `ItemID`. Keep `SpawnedFromId` accurate: OLP uses it for
vaultability, details previews, and secondary-object resolution.

### 2. Describe how the item should reach the player

Use `MeatKit/Otherloader/SpawnerEntry`. Prefer assigning `MainObjectObj`,
`SpawnWithObjs`, and `SecondaryObjs`; OLP fills their IDs from the referenced
`FVRObject` assets while loading.

`EntryPath` follows this shape:

```text
{Page}/{Category-or-SubCategory}/{ItemID}
```

Choose page and category from actual H3VR item-spawner definitions. OLP maps a
valid path into a vanilla page/category; otherwise it places the item in an
uncategorized custom category. Empty `MainObjectID` makes a custom-category
entry, not a spawnable item.

Set only intentional spawn relationships:

- `SpawnWithIDs`: objects spawned with main item; OLP prioritizes ammo as the
  second object.
- `SecondaryObjectIDs`: details-panel secondary items.
- `IsDisplayedInMainEntry`: false only for intentional secondary-only entries.

### 3. Give OLP a build root and clean bundle ownership

Create `MeatKit/Build Items/OtherLoader Root`, attach it to build profile, and
place one or more `OtherLoaderBuildItem`s in its First, Any, or Last lists.
Each child has a unique bundle name and owns its prefab, spawner-entry,
`FVRObject`, and related data assets.

For normal self-loading content, leave `SelfLoading` enabled. Tooling injects
the compatible `h3vr.otherloader` runtime dependency and calls OLP with the
profile's installed package path. Put genuine code-level requirements in
`BepinexDependancies`.

> [!TIP]
> Treat the bundle name as a globally unique runtime identity. Two mods that
> share an internal bundle name can make OLP load the wrong bundle or return a
> null asset bundle even though the Unity build itself succeeded.

### Choose an asset-loading model deliberately

| Model | Build output | Use | Runtime behavior |
| --- | --- | --- | --- |
| On-demand | `<bundle>` data plus `late_<bundle>` prefabs | Normal custom items | OLP loads metadata first, registers item, then resolves prefab bundle through Anvil when needed. |
| Immediate | One `<bundle>` with data and prefabs | Content requiring all assets at startup | OLP loads assets immediately; larger startup/memory cost. |

`OnDemand` is enabled by default in the OLP build item. Keep bundle names
globally distinctive: a conflicting internal bundle name can make OLP load the
wrong bundle or fail with a null asset-bundle result.

### Use ordering only for your own bundles

`First` bundles load serially, `Any` bundles load after First, and `Last`
bundles load after both. This is intra-mod ordering.

> [!WARNING]
> Do not rely on `LoadDependancies` for cross-mod readiness: current OLP source
> passes it into the self-load call, but runtime registration does not consume
> it. Use real BepInEx dependencies for code-level inter-mod ordering instead.

### 4. Inspect the package, not just the build result

Updated OLP MeatKit tools make `OtherLoaderBuildRoot` and
`OtherLoaderBuildItem` contribute `Sirdoggy-OtherLoaderPatched-2.0.0` to the
generated Thunderstore dependency list. That is tool-source minimum evidence,
not a reason to hard-code a version in another workflow.

Before release, inspect generated `manifest.json`:

1. It contains OLP dependency from current tool release.
2. It does not add old OtherLoader solely because OLP is present.
3. Package includes manifest, README, icon, plugin/asset payload, and intended
   dependencies only.
4. Build profile passed validation with unique bundle names and complete assets.

### 5. Test player and runtime behavior in H3VR

Players can install OLP beside an old OtherLoader install. OLP's bootstrapper
temporarily disables original `OtherLoader.dll` when it recognizes its manifest,
then restores it after OLP initializes. This prevents duplicate-loader startup;
players should not manually rename loader DLLs.

OLP also adds custom-category spawner UI, item sorting/grouping settings,
Unlockathon/ItemUnlocker features, and item-spawner refresh after loading. Those
are runtime features, not authoring substitutes.

Experimental `Ctrl+O` hotloading exists in current source but is not a release
test path. Many mods are not safe to load after H3VR startup. Restart H3VR for
normal validation.

## Acceptance pass

| Check | Observable result |
| --- | --- |
| Build/package | The authoritative project workflow completes and output is inspected |
| Loader startup | OLP starts without old-loader collision or bundle-name errors |
| Spawner and tag view | Item appears in the intended page/category with correct details |
| Core object | Prefab, controls, feeds, mounts, and audio behave as intended |
| Relationships | Spawn-with and secondary items are present and correctly linked |
| Vault | Save/load preserves `SpawnedFromId`, preview, and secondary links |
| Real interaction | A VR session succeeds and the BepInEx log contains no relevant errors |

## Diagnose the first useful symptom

| Symptom | First check |
| --- | --- |
| Item is uncategorized or absent | `EntryPath` page/category, entry's main object, OLP log. |
| Vault or preview wrong | `FVRObject.ItemID` and `SpawnedFromId`. |
| Secondary relationship missing | Referenced object IDs, then full-load linker log. |
| Bundle null/wrong assets | Duplicate internal bundle name; data/`late_` pair. |
| Works after restart but not hotload | Expected limitation; do not treat hotload as support. |

## Sources and credit

- [OLP source and release record](../sources/external/otherloader-patched.md)
- [Pinned OLP runtime source](../../references/Sirdoggy/OtherLoaderPatched/README.md)
- [Pinned OLP MeatKit tools](../../references/Sirdoggy/MeatKit_OtherLoaderPatched/README.md)
- [Original OtherLoader](https://github.com/devyndamonster/OtherLoader)
- [Mason documentation](https://github.com/H3VR-Modding/Mason/tree/main/docs/src)
- [Stratum](https://github.com/H3VR-Modding/Stratum)
- [Original raw workflow note](../sources/user-provided/2026-07-10-custom-weapons-stratum-mason.md)
