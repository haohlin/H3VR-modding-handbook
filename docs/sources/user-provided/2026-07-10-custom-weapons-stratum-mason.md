# Custom Weapons, Stratum, and Mason Notes

Source: Workflow note supplied in the project conversation.
Provided by: project contributor
Captured: 2026-07-10
Redistribution: user-provided conversation material
Fidelity: Text-rich preservation record. This keeps the supplied workflow,
context, and links; it is not a condensed handbook guide.

The original note was addressed to friends, compadres, and other item/gun
modders who were confused about Stratum and Mason. It called out that Ash,
Mason and Stratum's developer, had made new documentation available, and that
Ash was not in the Discord being discussed.

## Supplied workflow

1. Make the gun as normal, following Amity's custom-weapon tutorial from the
   `tutorials-guides` channel up to the point at which the asset bundles are
   made.
2. Set up the asset bundles for OtherLoader on-demand loading:
   https://github.com/devyndamonster/OtherLoader/wiki/Building-Mods-For-On-Demand-Loading
3. Compile and package using Mason, beginning with:
   https://h3vr-modding.github.io/Mason/getting_started/preparation.html

The intended order is important: make the weapon and its bundles first, make
those bundles suitable for OtherLoader on-demand loading next, then follow the
Mason preparation/packaging material. The note did not describe these as
interchangeable paths.

Mason documentation root:
https://h3vr-modding.github.io/Mason/

Companion tutorials supplied for indexing:

- https://docs.google.com/document/d/1bF66Tijdf5mwTXuIPWmnszSNMJ8u7Wxza9_PshheB2A/edit?tab=t.0#heading=h.im2jb6itwtrn
- https://docs.google.com/document/d/1DBrf71Lc8SAAlrHLuauq05LVkY8_P9VDsaixhhI55Xk/edit?tab=t.0
- https://docs.google.com/document/d/1sADJ-wmB0HYgY0kv44gt5ICAXejvUt1vnlCMC5KwXJk/edit?tab=t.0

The project conversation also requested that the FTW Arms Custom Weapons
tutorial be found and indexed with these sources. Its source card is kept
separately in `docs/sources/external/ftw-arms-custom-weapons.md`; this raw
record preserves the request and the workflow links that were supplied.

## Version caution

The maintained H3VR Modding Wiki currently places its OtherLoader on-demand
loading and Mason quick-start links under a legacy packaging heading. The
handbook records the supplied route, but an implementation or release guide
must name the Mason, Stratum, OtherLoader, MeatKit, and Unity versions it was
verified against.
