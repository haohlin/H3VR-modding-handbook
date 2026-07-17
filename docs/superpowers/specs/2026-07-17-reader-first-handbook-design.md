# H3VR Modding Handbook Reader-First Redesign

## Goal

Turn the repository from a correct reference inventory into a reader-first,
source-backed open-source handbook. A GitHub visitor must understand the
project's value, choose one useful path, and reach an actionable guide without
passing through multiple navigation pages.

## Research basis

This design borrows structure, not prose or assets, from established public
documentation projects:

- The Rust Book: one deliberate learning sequence before deeper material.
- Kubernetes: distinct task, explanation, and reference content; task pages
  solve one job with a short sequence and validation.
- GitHub Open Source Guides: README states purpose, usefulness, getting
  started, contribution, licensing, and acknowledgements.
- GitLab Handbook: concise repository landing page, stable content metadata,
  and a source-of-truth model for long-lived documentation.

## Non-negotiable constraints

1. Preserve every existing authored guide, source card, raw user-provided note,
   design record, plan record, and Git submodule. Move with `git mv`; do not
   drop content or replace source records with summaries.
2. Preserve every submodule remote, commit pin, manifest entry, and provenance
   header. No source reference becomes less discoverable.
3. Keep the handbook a public learning/reference repository. Windows remains
   authoritative for source, build, package, deploy, and VR validation.
4. Do not treat a pinned source snapshot as a released package or current game
   behavior. Continue to label source, release, historical, and verified state.
5. Keep third-party material link-only or in its existing permitted source
   record. Do not bulk-copy external documentation.
6. Do not add a site generator, hosting workflow, telemetry, or generated
   navigation in this redesign. GitHub Markdown remains the delivery surface.
7. Do not add a repository license until the repository owner chooses the
   intended license and scope for authored guides versus supplied material.

## Reader model

The handbook has four reader intents:

| Reader intent | First destination | Finish condition |
| --- | --- | --- |
| Learn H3VR modding from zero | Tutorial | A small, validated first result |
| Complete a known job | How-to | Job-specific validation passes |
| Understand an H3VR system | Explanation | Correct mental model and boundaries |
| Verify a claim or find upstream work | Reference | Credited primary source or pinned revision |

The same visitor should never need both a navigation index and a mind map to
reach a guide. A page should link to evidence only after it provides its own
complete first-pass instruction.

## Target information architecture

```text
README.md                         GitHub landing page and first action
docs/
  index.md                        Documentation home and route chooser
  start/
    first-steps.md                Workspace boundary and first-session flow
    use-the-handbook.md           Browse, clone, source, and contribution modes
  tutorials/
    custom-items-olp.md           Ordered first custom-item route
  guides/
    code-and-data-mods.md         BepInEx, Harmony, generated-data route
    map-authoring.md              General map route
    gungame.md                    GunGame model and entry route
    supply-raid.md                Supply Raid model and entry route
  how-to/
    validate-map-performance.md
    author-gungame-map.md
    build-gungame-pool.md
    author-supply-raid-map.md
    package-and-release.md
  explanations/
    loader-and-asset-bundles.md   OLP/OtherLoader, Stratum, Mason relationship
  reference/
    index.md                      Pinned source directory and verification rules
    snapshots/
      gungame-map-tutorial.md
    sources/
      external/
      user-provided/
  superpowers/                    Historical design and plan records
references/                       Read-only pinned upstream repositories
```

`docs/index.md` replaces both current navigation entry points. Its clear,
visual route chooser leads directly to a tutorial, guide, how-to, explanation,
or reference page. The existing Mermaid map is retained as orientation inside
that page, not as a second mandatory navigation destination.

## Content migration map

| Current file | Target file | Treatment |
| --- | --- | --- |
| `docs/start-here.md` | `docs/index.md` | Rewrite as one direct route chooser; retain all route intent. |
| `docs/development-flow.md` | `docs/start/first-steps.md` | Rename; keep Windows boundary and validation rules. |
| `docs/using-the-handbook.md` | `docs/start/use-the-handbook.md` | Rename; retain browse/clone/source guidance. |
| `docs/navigation/index.md` | `docs/index.md` | Merge navigation content; remove duplicated destination page. |
| `docs/navigation/mind-map.md` | `docs/index.md` | Retain and simplify diagram in documentation home. |
| `docs/weapons/custom-weapons-stratum-mason.md` | `docs/tutorials/custom-items-olp.md` | Rename; preserve OLP workflow and source/release boundary. |
| `docs/mod-code/bepinex-harmony-and-data.md` | `docs/guides/code-and-data-mods.md` | Rename and apply guide template. |
| `docs/maps/overview.md` | `docs/guides/map-authoring.md` | Rename and apply guide template. |
| `docs/maps/performance-and-vr-testing.md` | `docs/how-to/validate-map-performance.md` | Rename and apply how-to template. |
| `docs/gungame/overview.md` | `docs/guides/gungame.md` | Rename and apply guide template. |
| `docs/gungame/map-authoring.md` | `docs/how-to/author-gungame-map.md` | Rename and apply how-to template. |
| `docs/gungame/weapon-pools.md` | `docs/how-to/build-gungame-pool.md` | Rename and apply how-to template. |
| `docs/gungame/map-tutorial-snapshot.md` | `docs/reference/snapshots/gungame-map-tutorial.md` | Move without condensing source snapshot. |
| `docs/supply-raid/overview.md` | `docs/guides/supply-raid.md` | Rename and apply guide template. |
| `docs/supply-raid/map-authoring.md` | `docs/how-to/author-supply-raid-map.md` | Rename and apply how-to template. |
| `docs/releases/thunderstore.md` | `docs/how-to/package-and-release.md` | Rename and apply how-to template. |
| `docs/sources/` | `docs/reference/sources/` | Move all records unchanged, then update links. |
| `docs/superpowers/` | `docs/superpowers/` | Preserve in place as historical project records. |

## Page templates

All reader-facing pages use front matter with `title`, `description`,
`content_type`, `audience`, and `updated` fields. GitHub renders the Markdown
body normally; metadata establishes a stable authoring contract and supports a
future static site without another content migration.

### Tutorial

```text
Outcome
At a glance: the workflow visual and expected result
Before you begin
Build it, with the reason behind each decision
Inspect the result
Understand what changed and why
Troubleshoot a failed result
Next step
Sources and credit
```

### How-to

```text
Goal
Use this when
Before you begin and what success looks like
The shortest safe path
Verify the expected result
Common failure modes
Sources and credit
```

### Guide / explanation

```text
Purpose
At a glance: an original system or decision visual
Mental model and vocabulary
Choose the right route, with a decision table where it helps
Rules and boundaries
Practical implications
Sources and credit
```

### Reference / source record

```text
Source and publisher
Original author and contributor credit
Capture or pin date
Release/source/historical scope
Why it is useful
Link or pinned repository
```

## Visual and writing system

The handbook should read like deliberate public documentation, not a pile of
minimal reference cards. Every authored page uses the following layers, in the
order that serves the reader:

1. **Orientation.** State the outcome, intended reader, and when to use the
   page. Begin with a concise promise, but allow enough prose to make the
   problem feel concrete.
2. **Understanding.** Explain the mental model before asking a reader to act.
   Use an original Mermaid lifecycle, decision diagram, relationship map, or
   annotated table whenever it makes a system easier to grasp.
3. **Action.** Give an ordered, natural procedure with the reason behind each
   consequential choice. Use code blocks for exact commands and identifiers;
   do not reduce explanatory prose to a checklist merely to be brief.
4. **Verification.** Show the observable result, acceptance gates, log or VR
   checks, and the first useful diagnosis if it fails.
5. **Evidence.** End with direct, credited primary sources and make the
   release/source/historical boundary explicit where it matters.

Use GitHub-native Markdown as a visual system:

- Use sentence-case headings, descriptive links, short readable paragraphs,
  intentional whitespace, and a clear heading hierarchy.
- Use GitHub callouts (`[!NOTE]`, `[!TIP]`, `[!IMPORTANT]`, `[!WARNING]`) for
  reader decisions, safety boundaries, version-sensitive facts, and common
  traps. Do not use a warning merely for decoration.
- Use Mermaid only when it reveals a lifecycle with feedback, an architecture,
  an ownership relationship, or a non-obvious decision that prose/table cannot
  show as clearly. Do not draw a linear sequence already stated beside it. A
  route may contain more than one diagram only when each has a distinct,
  necessary teaching job.
- Use tables for route cards, comparisons, milestones, components, ownership,
  compatibility, acceptance gates, and before/after states. Pair a table with
  prose when the reader needs interpretation; do not turn an entire narrative
  into a spreadsheet.
- Use numbered lists for ordered actions, bullets for evidence, and
  collapsible `<details>` sections for optional source-level detail that would
  interrupt a first pass. Keep essential steps visible.
- Give code blocks an expected result or a follow-up verification, rather than
  leaving a command unexplained.
- End action pages with verification and expected failure signals; do not end
  with a generic link list.
- Place primary references at page end. Do not require source-card reading to
  understand an action page.

Raw user-provided notes, source snapshots, and external source cards are
evidence records, not pages to cosmetically rewrite. Preserve their supplied
wording, context, and provenance. An authored guide may be rich, narrative,
and visual while it links to those records for exact original detail.

## GitHub project contract

The rewritten root README contains, in order:

1. Project promise and reader boundary.
2. Three immediate actions: custom item, code/data mod, map/game-mode work.
3. A visual workflow from handbook to authoritative Windows workspace,
   package, and VR validation.
4. What is included: credited guides, source records, and 29 pinned upstream
   references.
5. What is intentionally excluded: game files, runtime projects, credentials,
   copied third-party material, and release artifacts.
6. Contribution, provenance, verification, and acknowledgements links.

Proposed GitHub description:

```text
Practical, source-backed H3VR modding guidance: choose a route, use the authoritative Windows workflow, validate in VR.
```

Do not set a homepage until a maintained published documentation site exists.

## Verification and acceptance

1. Every moved Markdown link resolves through `scripts/verify_handbook.py`.
2. Reference manifest tests still pass with all 29 pins and matching remotes.
3. `git diff --check` passes after every migration batch.
4. Search confirms every current guide/source filename has a mapped target and
   no stale link points at removed locations.
5. Root README has one route chooser; no duplicated navigation/index/mind-map
   entry sequence remains.
6. Each reader-facing route applies the page template intentionally, has a
   useful visual or decision aid where appropriate, and has an explicit
   validation section.
7. Every source record preserves author/publisher/capture/provenance data.
8. GitHub description is updated only after repository-content verification.

## Explicit exclusions

- No deletion of current handbook content, source cards, raw notes, specs,
  plans, references, or submodules.
- No runtime/build/package/deploy work.
- No copied upstream prose or binaries.
- No licensing decision or repository-license file in this redesign.
