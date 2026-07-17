# OtherLoaderPatched (OLP)

Source: Sirdoggy's OtherLoaderPatched release material, repository, and a
Discord release announcement transcript supplied to this handbook.
Original announcement author: Sirdoggy
Original announcement timestamp: 2026-04-10 00:50
Original venue: Discord; no message permalink supplied
Official package: https://thunderstore.io/c/h3vr/p/Sirdoggy/OtherLoaderPatched/
Official runtime source: https://gitlab.com/Sirdoggy/OtherLoaderPatched
Official MeatKit tools: https://github.com/sirdoggy45/MeatKit_OtherLoaderPatched/releases
Captured: 2026-07-17
Redistribution: attributed source card; third-party Discord text is not copied.

## Credit

- Sirdoggy: OtherLoaderPatched creator; source announcement author.
- devyndamonster: original OtherLoader creator.
- Meat Banana, J. Melon, Veryll, and jolly soldier bucket square: beta-testing
  and feedback credit from OLP release notes.

`sirdoggy45` is the publisher account for the OLP MeatKit-tools repository;
this card retains Sirdoggy's authorship credit.

## What this source establishes

OLP is a backwards-compatible replacement for original OtherLoader. When both
are installed, OLP takes priority. Existing OtherLoader mods need no dependency
rewrite solely to run for players with OLP installed.

For new MeatKit builds, OLP's updated tools add OLP as an implicit dependency
through the build root/item. Their generated manifest is the package-level
source of truth; check it before publishing.

## Release boundary versus source boundary

At capture, the public Thunderstore page identifies package dependency string
`Sirdoggy-OtherLoaderPatched-2.0.3`. Pinned runtime source commit
`e6568ce433cb596f7297e13d9ac2fedbf2528ddf` has manifest version `2.1.0`.
Treat that commit as development/source evidence, not proof `2.1.0` is publicly
released. Verify the actual Thunderstore package and installed manifest for a
release decision.

Pinned tool source commit `8fa8cf726f422cd92e0e24dba1daa21b61afa2e9` adds
`Sirdoggy-OtherLoaderPatched-2.0.0` through `OtherLoaderBuildRoot` and
`OtherLoaderBuildItem`. That is its declared minimum dependency at this pin.

## Handbook use

Use the [single custom-weapons route](../../weapons/custom-weapons-stratum-mason.md)
for author workflow, data setup, package checks, and runtime validation. Consult
the two pinned source repositories for implementation research; they remain
read-only reference material in this handbook.
