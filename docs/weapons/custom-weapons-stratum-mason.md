# Custom Weapons -> OtherLoaderPatched -> Mason

Use one route for a custom firearm or item. Build content in Unity, register it
with OtherLoaderPatched (OLP), package through MeatKit/Mason, then validate in
real H3VR on Windows.

~~~mermaid
flowchart LR
  content[Unity prefab + FVRObject] --> entry[ItemSpawnerEntry]
  entry --> root[OLP MeatKit build root]
  root --> package[Thunderstore package]
  package --> olp[OLP loads and registers item]
  olp --> test[Spawner + vault + VR test]
~~~

## OLP status and credit

OtherLoaderPatched is Sirdoggy's replacement for devyndamonster's original
OtherLoader. It preserves `h3vr.otherloader` and the public OtherLoader API so
existing OtherLoader content can run under OLP; it takes priority when both are
installed. Use OLP tools for a new build. Do not republish an existing mod only
to change its loader dependency.

The pinned OLP source currently contains a `2.1.0` manifest, but this is a
source snapshot, not publication proof. The source card records the published
Thunderstore boundary separately. Always inspect the generated manifest and
actual package page before shipping.

See [OLP source and credits](../sources/external/otherloader-patched.md).

## Authoring route

### 1. Make normal H3VR content

Create prefab, `FVRObject`, controls, feeds, mounts, materials, audio, and
matching metadata in the authoritative Windows Unity project. Give every
`FVRObject` a unique `ItemID`. Keep `SpawnedFromId` accurate: OLP uses it for
vaultability, details previews, and secondary-object resolution.

### 2. Create an `ItemSpawnerEntry`

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

### 3. Make one OLP build root

Create `MeatKit/Build Items/OtherLoader Root`, attach it to build profile, and
place one or more `OtherLoaderBuildItem`s in its First, Any, or Last lists.
Each child has a unique bundle name and owns its prefab, spawner-entry,
`FVRObject`, and related data assets.

For normal self-loading content, leave `SelfLoading` enabled. Tooling injects
the compatible `h3vr.otherloader` runtime dependency and calls OLP with the
profile's installed package path. Put genuine code-level requirements in
`BepinexDependancies`.

### 4. Choose loading model deliberately

| Model | Build output | Use | Runtime behavior |
| --- | --- | --- | --- |
| On-demand | `<bundle>` data plus `late_<bundle>` prefabs | Normal custom items | OLP loads metadata first, registers item, then resolves prefab bundle through Anvil when needed. |
| Immediate | One `<bundle>` with data and prefabs | Content requiring all assets at startup | OLP loads assets immediately; larger startup/memory cost. |

`OnDemand` is enabled by default in the OLP build item. Keep bundle names
globally distinctive: a conflicting internal bundle name can make OLP load the
wrong bundle or fail with a null asset-bundle result.

### 5. Use ordering only for own bundles

`First` bundles load serially, `Any` bundles load after First, and `Last`
bundles load after both. This is intra-mod ordering. Do not rely on
`LoadDependancies` for cross-mod readiness: current OLP source passes it into
the self-load call, but runtime registration does not consume it. Use real
BepInEx dependencies for code-level inter-mod ordering instead.

### 6. Build package and inspect result

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

## Player and runtime behavior

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

## Windows validation

1. Build/package through authoritative project workflow.
2. Start H3VR normally with OLP and package installed.
3. Confirm OLP starts without old-loader collision or bundle-name errors.
4. Confirm item appears in intended spawner page/category and tag view.
5. Spawn it; validate prefab, controls, feeds, mounts, audio, and all
   spawn-with/secondary relationships.
6. Save/load vault item; validate `SpawnedFromId`, preview, and secondary links.
7. Perform real VR interaction test; inspect BepInEx log before publishing.

## Fast diagnosis

| Symptom | First check |
| --- | --- |
| Item is uncategorized or absent | `EntryPath` page/category, entry's main object, OLP log. |
| Vault or preview wrong | `FVRObject.ItemID` and `SpawnedFromId`. |
| Secondary relationship missing | Referenced object IDs, then full-load linker log. |
| Bundle null/wrong assets | Duplicate internal bundle name; data/`late_` pair. |
| Works after restart but not hotload | Expected limitation; do not treat hotload as support. |

## Primary materials

- [OLP source and release record](../sources/external/otherloader-patched.md)
- [Pinned OLP runtime source](../../references/Sirdoggy/OtherLoaderPatched/README.md)
- [Pinned OLP MeatKit tools](../../references/Sirdoggy/MeatKit_OtherLoaderPatched/README.md)
- [Original OtherLoader](https://github.com/devyndamonster/OtherLoader)
- [Mason documentation](https://github.com/H3VR-Modding/Mason/tree/main/docs/src)
- [Stratum](https://github.com/H3VR-Modding/Stratum)
- [Original raw workflow note](../sources/user-provided/2026-07-10-custom-weapons-stratum-mason.md)
