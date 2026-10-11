---
name: implement-spec
description: "Implement a ticketed spec with subagents in separate worktrees and integrate the result on one branch."
disable-model-invocation: true
---

# Implement the spec

Complete the supplied spec on one integration branch. Read tickets as a dependency graph: a ticket is ready when its blockers have landed and it has no active worker.

Read `AGENTS.md` and `CLAUDE.md` for the configured agent root and `{agentRoot}/issue-tracker.md` for ticket location and completion rules. Use `setup-skills` only if missing configuration prevents work; a supplied local spec and ticket directory can provide enough information to proceed.

Before applying a skill below, load it through the Skill tool when available; otherwise read its `SKILL.md`. Use internal subagent tools for workers, not user-owned chats. If delegation is unavailable, work through the same graph sequentially and state the limitation.

## Establish the graph and integration branch

1. Read the spec, every associated ticket, repository guidance, and the relevant glossary and ADRs. Record the baseline commit and ticket dependencies. Resolve missing blockers and cycles before dispatching their dependent work.
2. Inspect the checkout and attached worktrees. Preserve unrelated changes. Create or reuse a suitable integration branch from the agreed baseline, following the repository's branch convention. Never reset a dirty checkout to make its base match.
3. Agree testing seams from the spec or discussion before workers start. Give each ticket acceptance criteria, its validation commands, and ownership of shared fixtures or generated contracts. For generated files, identify authoritative inputs, the generation command, and the project's required generation order. Workers escalate a material change to these seams instead of independently renegotiating the whole plan.
4. Dispatch independent ready tickets up to available agent slots. Keep capacity for coordination and review. Serialize tickets that repeatedly edit the same files or share an unsettled contract even if the written graph omits that dependency.

Exploration is optional. When repeated investigation would otherwise slow workers, delegate a bounded question and save cited notes under `{agentRoot}/research/` or a shared temporary directory. Give later workers pointers rather than copies.

## Run workers

Each worker receives its ticket, spec pointer, integration base commit, worktree path, branch, relevant guidance, testing seams, and completion criteria.

Each worker:

- Uses its own clean worktree and branch based on the integration branch. Recreate or safely change an incorrect clean base; preserve uncommitted work for review.
- Implements only the assigned ticket and necessary dependencies already agreed in the graph.
- Uses `tdd` at the agreed seams, appropriate type and build checks, and meaningful acceptance checks. Tests should exercise behavior rather than reproduce implementation details.
- Runs `prune-cruft` when complexity, dead code, memoization, casts, or wrappers warrant it. Runs `audit-implementation` for controls, routing, queries, persistence, framework idioms, or tool choices. Add `audit-security` when the changed trust boundary requires it.
- Commits only its assigned work, as authorized by this implementation workflow, and reports the commit, checks, unresolved concerns, and any dependency changes. It does not independently land work or close shared tickets.

Communicate through file and commit pointers. Keep the coordinator's graph authoritative so a ticket is claimed once. Record claims and integration evidence through the tracker configuration. For local files, keep these coordinator edits on the integration branch so workers do not compete to update the same ticket metadata.

## Integrate one result at a time

Use one merger at a time, whether the coordinator or a dedicated subagent. Parallel workers do not imply parallel writes to the integration branch.

Immediately before landing each result, capture the integration tip. Refresh the worker branch against that tip, resolve conflicts by the spec and both sides' intent, and rerun affected checks. Land only the refreshed, checked result. If the tip changes before landing, repeat the refresh and affected verification.

For generated-file conflicts, reconcile the authoritative inputs first and regenerate outputs through the established command and order. Preserve source ownership rather than hand-merging generated artifacts. Run the repository's reproducibility check; if none exists, rerun generation and confirm it produces no further changes before accepting the result.

After landing, record the integrated commit and validation, then recompute the ready tickets. A ticket becomes ready when its dependencies are integrated, not when a worker reports that they are done.

Open a draft PR after the first landed commit only when the user requests a PR or the tracker completes work through PRs. Use `pr` for its body. Add closing references according to the tracker. When the host provides a PR attachment tool, attach every PR created. Avoid opening a PR for a local-only workflow.

## Finish the integrated result

Once all tickets have landed, pin the integration commit as target `T`. Run the project's required checks and integrated acceptance checks on that tree. Load `code-review` with the recorded baseline and target `T` so Standards and Spec review the same commit pair.

Give a bounded repair worker any actionable findings, then integrate and verify repairs through the same serialized process. Pin the resulting target, rerun affected checks, and review affected changes against that target. Before resolving tickets or reporting completion, confirm the integration tip still matches the validated and reviewed target. If it advances, pin the resulting tip and validate and review the affected changes before closure.

Update completion through `{agentRoot}/issue-tracker.md`: local tickets retain implementation and validation evidence; a PR-based workflow marks the PR ready once checks and review pass and leaves final closure to its merge rules. Do not report pending merge-dependent work as already closed.

Clean up worker worktrees after their commits and needed artifacts are preserved. For managed worktrees, use the host's archive lifecycle when available; identify only worktrees created or assigned for this effort. Preserve unrelated worktrees and unmerged work.

Report the integration branch, completed tickets, validation, review result, PR link if created, and any remaining external completion step.
