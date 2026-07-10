# GunGame Notes

Source: GunGame description and tutorial links supplied in the project conversation.
Provided by: H3VR Modding Contributor
Captured: 2026-07-10
Redistribution: user-provided conversation material

## Mode description

Welcome to the GunGame mode.

As the player gets more kills, they receive different weapons. Dying results in
demotion to a previous weapon.

## Supplied resources

- Map tutorial: https://github.com/KacperObara/H3VR-GunGame/wiki/Map-making-Tutorial
- Weapon-pool tutorial: https://docs.google.com/document/d/1QlgTxTHH6X-kRL-iym6_Q85BahqY2yBLZxHDJLtYkX4/edit
- Map attribution note: Awesome map provided by Marcel.

## Local development boundary

The local H3VR-Mods GunGameProgressions project is a deterministic data
generator. It must generate pools in Windows staging and validate them against
the active runtime object registry before a VR test. Map authoring remains a
separate Unity/Atlas or WurstMod route.

