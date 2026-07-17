# Layered Visual Markdown Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the handbook's terse reference-card presentation with clear, layered, source-backed GitHub Markdown while preserving every current route, fact, and credited source.

**Architecture:** Keep the current file tree and source archive. Apply one shared visual language to authored pages: a reader-facing outcome, a mental-model visual when it clarifies the work, an explained procedure, explicit validation, and credit at the end. Raw user-provided and external source records remain faithful evidence, rather than being rewritten as guides.

**Tech Stack:** GitHub Flavored Markdown, Mermaid, existing Markdown link verifier, Python unittest.

## Global Constraints

- Do not delete, move, or condense any source record, user-provided note, submodule, manifest entry, or provenance header.
- Do not copy third-party prose or visual assets; use original diagrams and the handbook's own prose.
- Windows remains authoritative for editing, building, packaging, deployment, logs, and VR validation.
- Markdown must render naturally on GitHub without a site generator, custom CSS, or generated navigation.
- Use GitHub callouts, Mermaid, tables, and collapsible detail only where each makes comprehension easier; no arbitrary cap on visuals or tables.
- Every authored action page ends with a concrete validation/result section and a credited source section.

---

### Task 1: Establish the visual-writing contract

**Files:**
- Modify: `docs/superpowers/specs/2026-07-17-reader-first-handbook-design.md:172-207`
- Modify: `SOURCES.md:3-8`
- Modify: `CONTRIBUTING.md:1-40`

**Interfaces:**
- Consumes: The repository source policy and preserved-source boundary.
- Produces: A contributor-visible contract for authored handbook pages.

- [x] **Step 1: Replace compactness rules with layered documentation rules**

Write the visual system as five layers: orientation, understanding, action,
verification, and evidence. Define Markdown components: callouts, diagrams,
tables, code blocks, and optional deep dives. State that authored guides may
be detailed and narrative, while source records remain faithful.

- [x] **Step 2: Update the source policy and contribution map**

Replace `Keep it compact; link primary sources` with a rule to teach in
layers, use original visual explanations, and link primary sources. Update the
guide contribution row to require the relevant route plus visual/validation
review, not an index-only edit.

- [x] **Step 3: Verify policy language is no longer minimalist**

Run: `rg -n 'Keep it compact|Compact, visual|one small diagram|short tables and diagrams' README.md SOURCES.md CONTRIBUTING.md docs`

Expected: no remaining mandatory compactness rule outside historical source
material or an explicitly revised design record.

- [x] **Step 4: Commit the contract**

Run:

```bash
git add SOURCES.md CONTRIBUTING.md docs/superpowers/specs/2026-07-17-reader-first-handbook-design.md
git commit -m "docs: define layered visual writing style"
```

### Task 2: Rebuild the GitHub entry and reader orientation pages

**Files:**
- Modify: `README.md:1-65`
- Modify: `docs/start-here.md:1-44`
- Modify: `docs/development-flow.md:1-56`
- Modify: `docs/using-the-handbook.md:1-52`
- Modify: `docs/navigation/index.md`
- Modify: `docs/navigation/mind-map.md`

**Interfaces:**
- Consumes: The shared visual-writing contract from Task 1 and existing route destinations.
- Produces: One coherent reader journey from repository landing page to authoritative workspaces and guide selection.

- [x] **Step 1: Write the README as a GitHub project landing page**

Add a project promise, reader boundary, three route cards, a workflow diagram,
what the handbook contains, how to use it online/local, source provenance, and
contribution/verification links. Keep every existing route reachable.

- [x] **Step 2: Turn orientation pages into guided reading experiences**

Give each page an outcome, a useful flow visual, a short explanatory narrative,
action/result checks, and sources. Use tables to compare choices and callouts
to protect the Windows-authoritative boundary.

- [x] **Step 3: Check route integrity**

Run: `python3 scripts/verify_handbook.py`

Expected: all current manifest and Markdown references validate.

- [x] **Step 4: Commit the entry experience**

Run:

```bash
git add README.md docs/start-here.md docs/development-flow.md docs/using-the-handbook.md docs/navigation
git commit -m "docs: enrich handbook entry experience"
```

### Task 3: Apply tutorial-quality presentation to core authoring routes

**Files:**
- Modify: `docs/weapons/custom-weapons-stratum-mason.md`
- Modify: `docs/maps/overview.md`
- Modify: `docs/maps/performance-and-vr-testing.md`
- Modify: `docs/mod-code/bepinex-harmony-and-data.md`

**Interfaces:**
- Consumes: Existing technical facts and credited source records.
- Produces: Detailed Unity/content, map, performance, and code/data reader routes with explicit workflow and validation.

- [x] **Step 1: Add purposeful route visuals and a reader outcome**

Keep existing facts. Precede mechanics with the job being solved, when the
route applies, prerequisites, and an original Mermaid lifecycle/decision
diagram. Use callouts for high-risk boundaries and tables for choices.

- [x] **Step 2: Explain the procedure rather than listing only gates**

For each route, preserve ordered actions, explain why each key action matters,
show expected artifacts/results, and finish with verification plus diagnosis.

- [x] **Step 3: Preserve OLP release/source distinction and credit**

Keep Sirdoggy, devyndamonster, tester, source snapshot, and published release
boundaries intact in the custom-item tutorial. Do not treat source HEAD as a
release.

- [x] **Step 4: Commit core route presentation**

Run:

```bash
git add docs/weapons docs/maps docs/mod-code
git commit -m "docs: enrich core authoring guides"
```

### Task 4: Apply the system to game-mode and release routes

**Files:**
- Modify: `docs/gungame/overview.md`
- Modify: `docs/gungame/map-authoring.md`
- Modify: `docs/gungame/weapon-pools.md`
- Modify: `docs/supply-raid/overview.md`
- Modify: `docs/supply-raid/map-authoring.md`
- Modify: `docs/releases/thunderstore.md`

**Interfaces:**
- Consumes: Existing GunGame, Supply Raid, and release guidance plus their credited references.
- Produces: Consistent explanation/how-to/release pages with workflows, choices, and validation.

- [x] **Step 1: Give each route a visible problem-to-result story**

Use a concise outcome section, a system or sequence diagram, direct action
steps, outcome/acceptance checks, and a source-credit footer. Keep links to
snapshots and raw notes where their exact original context matters.

- [x] **Step 2: Retain every existing technical boundary**

Keep branch, provenance, data ownership, Unity, package, and runtime caveats.
Do not simplify a constraint merely because it is visually restyled.

- [x] **Step 3: Commit game-mode and release presentation**

Run:

```bash
git add docs/gungame docs/supply-raid docs/releases
git commit -m "docs: enrich game mode and release guides"
```

### Task 5: Validate public-rendering and repository integrity

**Files:**
- Modify only if a verifier exposes broken Markdown links.
- Test: `tests/test_reference_manifest.py`
- Test: `scripts/verify_handbook.py`

**Interfaces:**
- Consumes: All prior presentation changes.
- Produces: A clean, source-preserving handbook ready for push to `main`.

- [x] **Step 1: Check Markdown structure and links**

Run:

```bash
git diff --check
python3 scripts/verify_handbook.py
python3 -m unittest tests/test_reference_manifest.py -v
```

Expected: no whitespace errors, all Markdown/source links resolve, and all 29
reference-manifest tests pass.

- [x] **Step 2: Inspect the authored-page coverage**

Run:

```bash
rg -l '^## (Outcome|What you will|Use this route|Goal)' README.md CONTRIBUTING.md docs --glob '*.md' --glob '!docs/sources/**' --glob '!docs/superpowers/**'
```

Expected: every rewritten authored route appears; raw/archive and historical
files remain excluded from the presentation requirement.

- [x] **Step 3: Commit and publish the verified result**

Run:

```bash
git add README.md SOURCES.md CONTRIBUTING.md docs
git commit -m "docs: polish handbook markdown presentation"
git push origin main
```
