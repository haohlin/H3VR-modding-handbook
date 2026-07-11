---
name: h3vr-mod-development
description: Use when planning or carrying out an H3VR code, Unity/MeatKit, map, asset, package, test, or release change in the Windows-authoritative workflow.
---

# H3VR Mod Development

Use the authoritative Windows H3VR-Mods and MeatKit-Lite workspaces for real
development. This handbook is a guide and source archive, not a build or deploy
workspace.

## Choose the development route

```text
Requested change
├─ Runtime code, Harmony, configuration, or generated data
│  └─ Code/data route
└─ Prefab, scene, item, weapon, material, mesh, audio, or AssetBundle
   └─ Unity/MeatKit route — human in the loop
```

### Code/data route

Codex owns source research, implementation, tests, package validation, Git, and
log review. The human provides product intent and explicitly approves a public
release. Unity GUI work is not part of this route.

### Unity/MeatKit route — human in the loop

```text
Human: outcome + visual intent
  -> Codex: research, branch, scripts, IDs, metadata, tests
  -> Windows Unity: compile, runtime tests, MeatKit build/package
  -> Human only if needed: visual placement or subjective VR check
  -> Codex: validate package/logs, commit, push
  -> Human: approve publishing
```

Human manual work is limited to visual authoring, subjective VR feel, and release approval.

| Codex owns | Human owns only when needed |
| --- | --- |
| API/reference research, scripts, IDs, build metadata, automated prefab tests, headless Unity, MeatKit packaging, Git, logs | Mesh/art choices, materials, visual placement, final handling/reload/firing feel, public release approval |

Use the Unity GUI for visual authoring, hierarchy inspection, and drag-and-drop
references. Use batch Unity for repeatable work: compile, custom editor tests,
AssetDatabase checks, and MeatKit builds. `MeatKit.MeatKit.DoBuild` is the
built-in MeatKit build entry point; validate the chosen build profile first.

## Guardrails

- Windows is the source of truth; preserve its working tree and build against
  its installed H3VR assemblies.
- Keep each Unity content project under its existing `Assets/Projects` Git root.
- Close Unity before pull, branch-switch, or merge work. Save matching `.meta`
  files and never copy Unity assets by hand between projects.
- Treat a headless build as evidence for repeatable behavior, not for visual
  quality or subjective VR feel.
- Automate any manual operation that repeats: add an editor command and a
  headless-runtime test.
- Deploy or publish only after the required package checks and explicit human
  authorization.
