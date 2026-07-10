# H3VR Modding Handbook

**Learn the route. Open the real workspace. Build and test on Windows.**

| Need | Open |
| --- | --- |
| Choose a route | [Start Here](docs/start-here.md) |
| Find a source/project | [Navigation index](docs/navigation/index.md) |
| See the whole flow | [Mind map](docs/navigation/mind-map.md) |
| Clone and search locally | [How to use this handbook](docs/using-the-handbook.md) |

## Pick your path

| I want to… | Guide |
| --- | --- |
| Make a map | [Maps](docs/maps/overview.md) |
| Improve map performance | [Performance + VR test](docs/maps/performance-and-vr-testing.md) |
| Make a gun or item | [Custom weapons](docs/weapons/custom-weapons-stratum-mason.md) |
| Write code or generate data | [BepInEx + data](docs/mod-code/bepinex-harmony-and-data.md) |
| Work on GunGame | [GunGame](docs/gungame/overview.md) |
| Make a Supply Raid map | [Supply Raid](docs/supply-raid/overview.md) |
| Package a release | [Release flow](docs/releases/thunderstore.md) |

## Online or local

| Mode | Use it when | Action |
| --- | --- | --- |
| **Online** | You need guidance or a link | Read a guide → open its primary source |
| **Local** | You want raw Markdown/source examples | Clone with submodules |
| **Real development** | You are changing a mod | Use the authoritative Windows workspace |

~~~mermaid
flowchart LR
  handbook[Handbook] --> learn[Learn + find sources]
  learn --> windows[Windows H3VR-Mods / MeatKit-Lite]
  windows --> build[Build + package]
  build --> vr[VR test + logs]
~~~

~~~bash
git clone --recurse-submodules https://github.com/h3vr-modding/H3VR-modding-handbook.git
cd H3VR-modding-handbook
python3 scripts/verify_handbook.py
~~~

> ⚠️ Do not build, deploy, or edit a release from this repository. It is a
> reference library. See [Development Flow](docs/development-flow.md).

## Reading rule

**Guides** use short tables and diagrams to help choose a route quickly.
**Source archive records** deliberately retain the detailed, text-rich material
supplied with the project, including context, caveats, and source links. Do not
replace an archive record with a condensed guide.

## Contribute

| Change | Read |
| --- | --- |
| Guide, source card, or submodule | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Attribution / redistribution | [SOURCES.md](SOURCES.md) |
| Collected notes and raw sources | [Source archive](docs/sources/README.md) |
