# GunGame Weapon Pools

## Use this route when

You are selecting progression weapons, changing generated pools, or diagnosing
a GunGame loadout that is invalid for the active mod set.

## Pool checklist

1. Treat the active runtime object registry as the source of truth. Do not
   assume a static installed-mod list describes the player's enabled content.
2. Generate pool data deterministically with an explicit seed in Windows
   staging, not by mutating tracked release data.
3. Validate every referenced object ID and each generated progression before a
   runtime test.
4. For firearm loadouts, prefer a compatible magazine, then clip/speedloader,
   and use loose cartridges only when the firearm has no compatible feed.
5. Add an optic only after verifying a physical mount match. Exclude magnifiers
   and non-optic attachments unless the profile explicitly calls for them.
6. Preserve safe packaged fallback pools until runtime registry refresh is
   complete.

## Primary references

- [GunGame overview](overview.md)
- [Raw GunGame notes](../sources/user-provided/2026-07-10-gungame-notes.md)
- [GunGame project](../../references/KacperObara/H3VR-GunGame)
- [H3VR Modding Wiki source](../../references/H3VR-Modding/wiki)

