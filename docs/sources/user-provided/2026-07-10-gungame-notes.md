# GunGame Notes

Source: GunGame description and tutorial links supplied in the project conversation.
Provided by: H3VR Modding Contributor
Captured: 2026-07-10
Redistribution: user-provided conversation material
Fidelity: Text-rich preservation record. It retains the supplied description,
attribution, and links instead of reducing them to the handbook navigation
guide.

## Mode description

The supplied introduction was:

"Awesome map provided by Marcel. Welcome to the GunGame mode."

As the player gets more kills, they receive different weapons. Dying results in
a demotion to a previous weapon. The note presents this as the core GunGame
loop to retain when making map or weapon-pool support.

## Supplied resources

- Tutorial for making maps:
  https://github.com/KacperObara/H3VR-GunGame/wiki/Map-making-Tutorial
- Tutorial for making weapon pools:
  https://docs.google.com/document/d/1QlgTxTHH6X-kRL-iym6_Q85BahqY2yBLZxHDJLtYkX4/edit

The handbook keeps a locally hosted, compact tutorial snapshot for browsing and
the pinned Git submodule for local source study. Those navigation aids do not
replace the supplied map and weapon-pool links above.

## Local development boundary

The local H3VR-Mods GunGameProgressions project is a deterministic data
generator. It must generate pools in Windows staging and validate them against
the active runtime object registry before a VR test. Map authoring remains a
separate Unity/Atlas or WurstMod route.
