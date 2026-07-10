# H3VR Modding Handbook

## Purpose

Create a private GitHub repository, `h3vr-modding/H3VR-modding-handbook`, that is a
macOS-hosted learning and documentation workspace for H3VR modding. It must
make the development routes, source material, practical Unity/map notes, and
upstream examples easy to find without becoming another production or runtime
workspace.

The Windows `<private-windows-development-root>\\H3VR-Mods` checkout and `MeatKit-Lite` Unity project
remain the authoritative build, package, deployment, and VR-test environments.
This repository never contains H3VR assemblies, credentials, build outputs, or
copied production Unity projects.

## Scope and delivery order

The handbook is a long-lived project, so it will be delivered in small,
reviewable stages:

1. Establish the handbook repository, source-provenance policy, inventory, and
   pinned upstream references as Git submodules.
2. Preserve the user's supplied map-modding/Prometheus transcript as raw
   Markdown and turn it into navigable map-authoring, performance, and VR-test
   checklists.
3. Add concise route guides for BepInEx/Harmony, data mods, MeatKit/Unity
   content, custom weapons, Stratum/Mason, maps, GunGame, Thunderstore releases,
   and troubleshooting. Each guide links to the authoritative source material
   and the relevant reference projects.
4. Maintain the handbook as new projects and releases are added; the handbook
   is not a substitute for current upstream documentation or real VR testing.

## Repository layout

```text
H3VR-modding-handbook/
├── README.md                         # orientation and development-flow boundary
├── SOURCES.md                        # provenance, licenses, and update policy
├── docs/
│   ├── start-here.md
│   ├── development-flow.md
│   ├── maps/
│   ├── unity-meatkit/
│   ├── weapons/
│   ├── gungame/
│   ├── mod-code/
│   ├── releases/
│   ├── troubleshooting/
│   └── sources/
│       └── user-provided/            # immutable raw material supplied by project contributor
├── references/                       # independently versioned Git submodules
│   ├── H3VR-Modding/
│   │   └── wiki/                     # source of h3vr-modding.github.io/wiki
│   ├── KacperObara/
│   │   └── H3VR-GunGame.wiki/         # Git source of GunGame map tutorial
│   ├── Packer/
│   └── cityrobo/
└── docs/superpowers/                 # design and implementation records
```

The current 22 reference repositories move into `references/` without changing
their individual repository histories or remotes. The superproject pins an
exact commit for each reference. `H3VR-Modding/wiki` is the raw Markdown source
for <https://h3vr-modding.github.io/wiki/>, so adding it as a submodule fulfils
the request to retain the wiki's source material without scraping the rendered
site.

## Source and attribution policy

There are three intentionally separate source classes:

| Class | Storage rule | Examples |
| --- | --- | --- |
| Authored handbook guidance | Normal Markdown in `docs/`, with sources near claims | workflows, checklists, concise explanations |
| User-provided raw material | Verbatim Markdown in `docs/sources/user-provided/`, with date and provenance header | Prometheus transcript and collected notes |
| Third-party/upstream material | Git submodule when the source is a Git repository; otherwise an attributed source card/link | H3VR-Modding wiki, Packer and cityrobo projects, Unity/Valve/BepInEx pages |

The handbook must not bulk-copy pages, Google Docs, forum posts, videos, Asset
Store assets, Discord attachments, or other third-party documentation unless
their license explicitly permits redistribution. A source card records the URL,
publisher, access date, intended use, and any known license or access warning.
The linked Unity 5.6 TextMesh Pro package is therefore catalogued as a source,
not redistributed from this repository.

## Custom weapons, Stratum, Mason, and GunGame sources

The handbook will add two focused routes.

### Custom weapons and packaging

`docs/weapons/custom-weapons-stratum-mason.md` will describe the user's
suggested route as an ordered, version-labelled checklist:

1. Create and implement the gun in Unity using the custom-weapon tutorial
   linked by the H3VR Modding Wiki.
2. Configure the asset bundles for OtherLoader on-demand loading when the mod
   needs that loading model.
3. Compile and package using Mason's preparation, compilation, asset, and
   packaging documentation.

The H3VR Modding Wiki currently labels its OtherLoader/Mason packaging links as
legacy. The handbook therefore must state the exact Mason and Stratum version
for which a workflow was verified, link to the current Mason source, and never
silently treat a legacy procedure as the current release path. The three
user-supplied Google Docs are indexed as external source cards. They are not
copied into the handbook without redistribution permission.

An online search did not identify a direct, independently verifiable "FTW Arms
Custom Weapons tutorial" URL. The source card records that result, points to
the custom-weapon tutorial that the H3VR Modding Wiki actually links, and can
be upgraded if a direct FTW Arms source URL is later supplied.

### GunGame

`docs/gungame/` will separate game-mode context, map authoring, weapon-pool
authoring, and the local GunGameProgressions development flow. It will retain
the user-provided mode description: player kills progress through weapons and
death demotes the player. The KacperObara GunGame wiki is added as a pinned
submodule because GitHub wikis are Git repositories; the supplied weapon-pool
Google Doc is an attributed source card. This route cross-links the Windows
authoritative GunGameProgressions source and makes clear that generated pools
must be validated against the player's actual installed content.

The source inventory will include these exact upstream entries:

| Topic | Source |
| --- | --- |
| Mason documentation | `https://h3vr-modding.github.io/Mason/` and the `H3VR-Modding/Mason` submodule |
| OtherLoader on-demand loading | `https://github.com/devyndamonster/OtherLoader/wiki/Building-Mods-For-On-Demand-Loading` |
| GunGame map tutorial | `https://github.com/KacperObara/H3VR-GunGame/wiki/Map-making-Tutorial` and the matching `.wiki.git` submodule |
| GunGame weapon pools | `https://docs.google.com/document/d/1QlgTxTHH6X-kRL-iym6_Q85BahqY2yBLZxHDJLtYkX4/edit` |
| User-supplied companion tutorial 1 | `https://docs.google.com/document/d/1bF66Tijdf5mwTXuIPWmnszSNMJ8u7Wxza9_PshheB2A/edit?tab=t.0#heading=h.im2jb6itwtrn` |
| User-supplied companion tutorial 2 | `https://docs.google.com/document/d/1DBrf71Lc8SAAlrHLuauq05LVkY8_P9VDsaixhhI55Xk/edit?tab=t.0` |
| User-supplied companion tutorial 3 | `https://docs.google.com/document/d/1sADJ-wmB0HYgY0kv44gt5ICAXejvUt1vnlCMC5KwXJk/edit?tab=t.0` |

## Development flow documentation

The entry guides must clearly distinguish these routes:

- BepInEx/Harmony code mods: develop and validate on Windows against the live
  game assemblies; package/deploy with the repository wrapper; VR test before a
  release.
- Data mods: keep generation deterministic and package the generated payload,
  not staging output.
- Unity/MeatKit content: edit the actual Windows Unity project and commit
  source assets plus `.meta` files to its dedicated repository; never copy the
  shared MeatKit project into the handbook.
- Maps: use the WurstMod/H3VR mapping source as a reference, with authored
  guides covering hierarchy, colliders, lighting, occlusion, navmesh, audio,
  profiling, and in-game VR validation.
- Custom weapons: separate the Unity implementation phase from the loader and
  packaging phase; capture the Mason/Stratum version that the packaging guide
  applies to.
- GunGame: distinguish map requirements from deterministic weapon-pool
  generation and test pools against active registries in the Windows runtime.

## Failure handling and verification

Submodule setup must fail loudly if a clone has a remote mismatch, local
changes, or an unresolved reference. It must not delete or reclone a reference
without preserving the existing checkout. A validation script/checklist will
confirm that every expected submodule is registered, at the intended pinned
commit, clean, and that the source inventory links resolve.

Documentation validation is intentionally lightweight: Markdown link checks
where possible, a reference-inventory check, and a review that authored claims
are labelled as guidance rather than guaranteed H3VR behaviour. Runtime,
Unity, build, package, and VR behaviour are validated only in their respective
authoritative Windows workflows.

## Acceptance criteria for the foundation

- A private `h3vr-modding/H3VR-modding-handbook` GitHub repository exists and has a
  clear README, source policy, and onboarding path.
- All 22 existing reference clones are represented as clean, pinned submodules
  under `references/`; `H3VR-Modding/wiki` is included. The GunGame wiki is
  added as one additional pinned reference submodule.
- The user-supplied Prometheus material and resource list are preserved with
  clear provenance, and the map guide links back to it.
- The repository says exactly where to edit Unity content, build a mod, and
  VR-test it, including the custom-weapon/Stratum/Mason and GunGame routes,
  without any claim that the handbook itself is buildable.
- No production H3VR, Unity, Steam, r2modman, secrets, generated artifacts, or
  third-party binary assets are copied into the handbook.
