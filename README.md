# H3VR Modding Handbook

> **A practical, source-backed guide to H3VR modding.** Choose a route, learn
> the working model, then make and validate the change in the authoritative
> Windows workspace.

This is a public handbook and research library, not a mod project or a game
install. It connects real authoring work to the original people, projects, and
versioned sources behind it.

> [!IMPORTANT]
> Use this repository to learn, compare sources, and prepare work. Edit, build,
> package, deploy, and test a mod in the authoritative Windows workspace.

## Start with the thing you want to make

| I want to… | Start here | You will leave with… |
| --- | --- | --- |
| Build a custom firearm or item | [Custom items: Unity -> OLP -> Mason](docs/weapons/custom-weapons-stratum-mason.md) | A loader-aware package and an H3VR validation plan |
| Write a plugin or generate data | [Code and data mods](docs/mod-code/bepinex-harmony-and-data.md) | The live API/registry checks before a runtime test |
| Build a map or game-mode content | [Map authoring](docs/maps/overview.md) | A scene-to-VR workflow with performance gates |
| Make a GunGame map or pool | [GunGame](docs/gungame/overview.md) | The correct map, pool, and active-registry route |
| Make Supply Raid content | [Supply Raid](docs/supply-raid/overview.md) | The SRE reference boundary and mode-specific test route |
| Prepare a release | [Package -> test -> release](docs/releases/thunderstore.md) | A package inspection and explicit publication gate |

## How to use this handbook

The handbook is deliberately layered. Start with an authored guide for the
story, decisions, and working steps. Follow its verification section in the
real workspace. Open the linked source record only when you need exact
provenance, original wording, version history, or upstream implementation
detail.

| Mode | Best for | First move |
| --- | --- | --- |
| **Read online** | Choosing a route or checking a documented boundary | [Start Here](docs/start-here.md) |
| **Study locally** | Searching Markdown and pinned source examples | [How to use the handbook](docs/using-the-handbook.md) |
| **Verify a claim** | Finding credited upstream work, capture dates, and pins | [Source archive](docs/sources/README.md) |
| **Navigate by topic** | Seeing every route and reference shelf | [Navigation index](docs/navigation/index.md) |

```bash
git clone --recurse-submodules <repository-url>
cd H3VR-modding-handbook
python3 scripts/verify_handbook.py
```

<details>
<summary>Already cloned without the reference repositories?</summary>

```bash
git submodule update --init --recursive
python3 scripts/verify_handbook.py
```

</details>

## What is here

| Layer | What it gives you | How it is maintained |
| --- | --- | --- |
| **Authored routes** | Explanations, visual workflows, action steps, and validation | Maintained in `docs/` |
| **Source archive** | Raw user-provided notes and attributed external source cards | Preserved for context and credit |
| **Pinned references** | **29** upstream repositories at reviewed commits | Read-only Git submodules and [manifest](references/manifest.json) |
| **Verification** | Link and reference-pin checks | [`scripts/verify_handbook.py`](scripts/verify_handbook.py) and manifest tests |

> [!NOTE]
> A pinned repository proves what that source looked like at its recorded
> commit. It does not by itself prove a package was released, is current, or
> works with your installed game version.

## Credit and contribution

This handbook keeps author, publisher, contributor, capture-date, and source
boundaries visible. For example, the custom-item route credits Sirdoggy for
OtherLoaderPatched, devyndamonster for original OtherLoader, and named OLP
testers without copying the supplied Discord announcement.

Improve a route, add an attributed source, or review an upstream pin through
[CONTRIBUTING.md](CONTRIBUTING.md). Read [SOURCES.md](SOURCES.md) before adding
material: authored teaching can be rich and visual, but third-party material
remains linked, credited, and preserved in the correct source record.
