# H3VR Modding Handbook

An open, source-backed learning and reference library for H3VR modders. Use it
to choose the right modding route, study established projects, and find the
current source material behind maps, Unity content, custom weapons, BepInEx
plugins, GunGame, and packaging.

It is a handbook, not an H3VR development environment. The authoritative place
to edit, build, package, deploy, and VR-test a mod is the Windows H3VR-Mods or
MeatKit-Lite workspace.

## Use it online

You do not need to clone anything to start:

1. Open [Start Here](docs/start-here.md) and choose the kind of mod you want to
   make.
2. Follow the linked route guide: maps, Unity/MeatKit, custom weapons,
   BepInEx/data, GunGame, or release.
3. Use the [navigation index](docs/navigation/index.md) for direct links or the
   [mind map](docs/navigation/mind-map.md) to see how routes and tools connect.
4. Read the linked upstream source and source cards before following a
   compatibility-sensitive workflow.

For the complete online/local/reference workflow, read
[How to Use the Handbook](docs/using-the-handbook.md).

## Clone the full reference library

Clone with submodules when you want the original raw Markdown and source code
from the referenced projects:

~~~bash
git clone --recurse-submodules https://github.com/h3vr-modding/H3VR-modding-handbook.git
cd H3VR-modding-handbook
python3 scripts/verify_handbook.py
~~~

If you already cloned without the references:

~~~bash
git submodule update --init --recursive
python3 scripts/verify_handbook.py
~~~

The repository pins 27 upstream references at reviewed commits. They are not
automatically updated to each upstream's latest revision.

## Find the right material

| Goal | Start here |
| --- | --- |
| Make or improve a map | [Map overview](docs/maps/overview.md) |
| Diagnose map performance or prepare VR testing | [Map performance and VR testing](docs/maps/performance-and-vr-testing.md) |
| Make a custom firearm or Unity item | [Custom weapons, OtherLoader, Stratum, and Mason](docs/weapons/custom-weapons-stratum-mason.md) |
| Write a BepInEx/Harmony plugin or data generator | [Code and data mods](docs/mod-code/bepinex-harmony-and-data.md) |
| Work on GunGame maps or pools | [GunGame overview](docs/gungame/overview.md) |
| Package or release a mod | [Package, test, and release](docs/releases/thunderstore.md) |
| Read collected notes, external links, and raw source material | [Source archive](docs/sources/README.md) |
| Browse every major route and upstream project | [Navigation index](docs/navigation/index.md) |

## Understand the library

- **Guides** explain a route and its real-world validation steps.
- **User-provided notes** preserve collected project knowledge and links.
- **Source cards** point to external pages that cannot be republished here.
- **Git submodules** preserve original upstream repositories and their raw
  documentation. Do not edit them from this handbook.
- **The source manifest** lists every reference and requested pin:
  [references/manifest.json](references/manifest.json).

## Before you make a real mod change

Read [the development boundary](docs/development-flow.md). In short:

- Use this repository to learn and locate examples.
- Make Unity content edits in the real Windows MeatKit-Lite project.
- Make plugin/data changes in the real Windows H3VR-Mods project.
- Treat a build as incomplete until it has been packaged, deployed, tested in
  H3VR, and checked for runtime errors.

## Contribute or maintain a reference

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [the source policy](SOURCES.md).
Contributions should improve navigation, preserve attribution, and never add
game binaries, Unity caches, credentials, generated artifacts, or unlicensed
third-party copies.
