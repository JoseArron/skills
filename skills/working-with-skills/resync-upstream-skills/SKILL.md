---
name: resync-upstream-skills
description: Resync a selectively derived skills repository with its recorded upstream sources. Use when the user wants to pull upstream skill releases, reconcile renamed or changed skills, refresh third-party attribution, or audit whether local adaptations have drifted.
---

# Resync Upstream Skills

Treat the local repository as a **selective downstream**. Upstream provides
changes; the local repository owns its categories, deliberate renames,
integrations, terminology, and workflow choices.

## 1. Establish the Local Contract

Read the repository before reading upstream:

- `AGENTS.md` and `CLAUDE.md` for maintenance instructions and the configured
  agent root.
- `README.md` for category and installation conventions.
- `THIRD-PARTY.md`, license files, and equivalent attribution ledgers for the
  source-to-local map and recorded local adaptations.
- The relevant local `SKILL.md` files and their supporting resources.
- Recent Git history for prior sync commits, deliberate renames, and local
  edits that attribution prose does not fully explain.
- The repository's `zoom-out` skill, when present, then apply its map-first pass
  to the skills involved in this sync.

Record a working map of each source, its last synced release or commit, its
upstream path, its local path, its local name, and every adaptation that must
survive. This step is complete when every currently attributed local skill has
an upstream identity or is explicitly marked unresolved.

## 2. Resolve the Upstream Range

Use the user's requested release, tag, commit, or resource as the target. When
the user asks for the latest version, resolve the latest stable release from
the source itself.

Use primary evidence: release notes, tags, commit history, repository files,
and diffs between the recorded baseline and target. A release summary helps
locate changes; the actual files and history establish what changed.

When the attribution ledger lacks a baseline, inspect the local Git history to
identify the last sync. State any remaining baseline assumption before editing.
This step is complete when every source has an explicit baseline and target.

## 3. Build an Identity Map

Match skills by identity, not path alone. Use, in descending weight:

1. Explicit mappings in the attribution ledger.
2. Upstream rename or move history.
3. Frontmatter names and descriptions.
4. Shared content and Git ancestry.
5. References from other skills.

Classify every upstream change:

| Class | Meaning | Action |
| --- | --- | --- |
| Update | An already mapped skill or one of its supporting files changed | Adapt the change locally |
| Rename or move | An existing skill changed identity or location upstream | Remap it; prefer the upstream public name unless a recorded local exception still applies |
| New skill | No mapped local ancestor exists | Propose it and ask before adapting it |
| Removal | A mapped upstream skill disappeared | Report it and ask before deleting or retiring local work |
| Unrelated | The change does not belong to an attributed skill | Leave it outside the sync |

A new supporting file, rewritten body, split section, or renamed directory for
an existing skill is an **update**, not a new skill. For an apparent split or
merge, trace the content and purpose before classifying it. This step is
complete when every changed upstream path has exactly one classification.

## 4. Gate New Skills

For each genuinely new upstream skill, report:

- What it does and how upstream invokes it.
- Which local category fits and why.
- Which local skills overlap with it.
- Which local adaptations it would need.
- Whether any mapped update depends on it.

Ask the user whether to adapt each new skill. Keep that branch untouched until
approved. Continue already authorized updates to mapped skills when they do not
depend on the pending choice.

Treat ambiguous identity as a decision only when the evidence cannot separate
a rename from a new skill. Present the evidence and ask one focused question.

## 5. Adapt Mapped Changes

Port upstream intent while preserving the local contract:

- Keep local categories; installation may flatten them, but repository
  organization remains locally owned.
- Prefer upstream skill names after a rename. Preserve a different local name
  only when the ledger or user records it as deliberate.
- Reapply local tracker behavior, agent-root paths, command names, integrations,
  review gates, and terminology.
- Preserve local supporting files and additions unless the upstream change
  makes them obsolete and the local contract no longer needs them.
- Update frontmatter names, folder names, internal skill references, examples,
  and routing text together.
- Adapt prose and structure to local conventions instead of copying an entire
  upstream tree over the repository.

Inspect the final local file as a coherent skill whose current instructions
stand on their own. This step is complete when every mapped upstream change is
represented locally and every recorded adaptation still holds.

## 6. Reconcile the Repository

Update the attribution ledger with:

- The new upstream release or commit.
- Current upstream-to-local path mappings.
- Renames, moves, and concise notes for material local adaptations.
- Added or removed third-party files and any required license notice.

Then audit the complete local skill graph:

- Every folder name agrees with its skill's frontmatter name.
- Every referenced skill exists under its current name.
- Renamed skills leave no stale command names or old paths in live prose.
- Dependency and routing references point to available local skills.
- Agent-root, issue-tracker, and category terminology matches local setup.
- Existing upstream updates are not listed as newly introduced skills.

This step is complete when every local reference resolves or is explicitly
reported as an external or optional dependency.

## 7. Verify and Propagate

Validate every changed skill with the repository's validator or skills CLI.
Review the final diff against both the upstream range and the local contract.
Run targeted searches for stale names, source paths, release numbers, and local
terminology. Follow the repository's maintenance instructions for committing
and propagating the skills when the user's request authorizes those actions.

Report:

- Baseline and target for each source.
- Updated and renamed local skills.
- Local adaptations preserved or changed.
- New skills awaiting approval.
- Removals or unresolved identities awaiting a decision.
- Validation, propagation, and Git results.

The resync is complete when all mapped changes are adapted and verified, the
attribution ledger matches the resulting tree, and every pending new skill or
removal is clearly separated from completed work.
