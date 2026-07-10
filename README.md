# H3VR Modding Handbook

A private, source-backed handbook for H3VR modding routes: Unity/MeatKit
content, custom weapons, maps, BepInEx code, data generation, GunGame, and
Thunderstore packaging.

This is a macOS-hosted reference and documentation repository. It is not an
H3VR build, package, deployment, or VR-test workspace. The authoritative
environments are the Windows H3VR-Mods checkout and Windows MeatKit-Lite Unity
project.

## Start here

- [Choose a modding route](docs/start-here.md)
- [Understand the development boundary](docs/development-flow.md)
- [Browse the direct navigation index](docs/navigation/index.md)
- [View the route mind map](docs/navigation/mind-map.md)
- [Read the source policy](SOURCES.md)

## Clone with references

~~~bash
git clone --recurse-submodules git@github.com:h3vr-modding/H3VR-modding-handbook.git
~~~

To initialize references after a normal clone:

~~~bash
git submodule update --init --recursive
~~~

The checked-in submodule revisions are deliberate pins. Update an upstream only
when its change has been reviewed and the handbook source manifest is updated.

