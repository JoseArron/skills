# Implement-spec paper evaluation

Evaluated 11 October 2026. This is a forward simulation of the saved skill, not an implementation run. No branches, worktrees, tickets, commits, or pull requests were changed.

## Answer

The skill handles the scenario's main coordination risks: shared-file ownership overrides a misleading unblocked label, workers remain isolated from unrelated dirty work, results land serially against the changing integration tip, and this local workflow opens no PR. Two gaps remain useful to fix: generated-contract conflict resolution needs an explicit source-of-truth rule, and final validation/review needs a pinned target commit.

## Scenario and execution plan

Input: approved spec, local Markdown tracker, A generates API types, B adds their consumer UI, and C adds analytics while touching some of the same generated files. A and C are labeled unblocked. Two completed workers arrive while the integration tip changes. The user's checkout contains unrelated changes. No PR is requested.

1. **Read configuration and freeze the starting point.** Read the spec, all three tickets, the tracker instructions, repository guidance, glossary, and relevant ADRs. Record baseline commit `S0`. Check the actual dependencies rather than trusting status labels. Read the existing checkout and attached worktrees without moving or resetting unrelated work. Create or reuse a clean integration worktree/branch from the agreed baseline. The skill requires preservation but does not mandate a particular branch name. [Implement-spec, lines 9-20](</C:/Users/josee/Code-Stuff/Projects/skills/skills/build-and-debug/implement-spec/SKILL.md:9>).
2. **Set the graph and file ownership.** B depends on A's integrated types. A and C do not qualify for simultaneous dispatch merely because both say unblocked: they share generated-file ownership or an unsettled contract. Serialize that work. Assign A the generated-contract change and document the boundary of C's later change. A safe default sequence is A, then C, then B if C changes the contract B consumes. If C's overlap is settled and does not change B's interface, B and C can run after A in separate worktrees; the scenario alone cannot prove that independence. Record the actual decision in the coordinator's graph. [Implement-spec, lines 17-20 and 36](</C:/Users/josee/Code-Stuff/Projects/skills/skills/build-and-debug/implement-spec/SKILL.md:17>).
3. **Agree validation before dispatch.** Give each worker acceptance criteria, commands, public testing boundaries, shared fixture/contract ownership, and completion rules. Examples for this simulation are API contract compatibility for A, the specified UI behavior for B, and analytics event behavior for C. These examples are proposals, not preapproved tests: adopt boundaries already covered by the approved spec/discussion, or settle missing ones once with the coordinator before writing tests. The `tdd` dependency expressly requires pre-agreed, user-confirmed boundaries. [Implement-spec, lines 19 and 26-34](</C:/Users/josee/Code-Stuff/Projects/skills/skills/build-and-debug/implement-spec/SKILL.md:19>), [TDD, lines 18-24](</C:/Users/josee/Code-Stuff/Projects/skills/skills/build-and-debug/tdd/SKILL.md:18>).
4. **Run isolated workers.** Give each worker its ticket, spec path, exact integration base, clean worktree, branch, relevant guidance, and validation ownership. Each implements its assigned scope, runs meaningful tests and relevant type/build checks, and invokes focused reviews when warranted. B's UI triggers audit-implementation; C's persistence/query work does too if present. Security review depends on a changed trust boundary. Each reports commits, checks, concerns, and dependency changes. Workers never merge or close shared tickets. [Implement-spec, lines 26-36](</C:/Users/josee/Code-Stuff/Projects/skills/skills/build-and-debug/implement-spec/SKILL.md:26>).

If A and C already completed concurrently, that history violates the dispatch rule. Preserve both results, record the missed overlap, and queue them serially. Do not discard C's work or treat worker completion as integrated completion. C still needs refresh, any source-contract correction, and verification after A lands.

## Landing two completed results while the tip changes

Assume ready result X was checked against `I0`, but the integration branch has advanced to `I1`.

1. One coordinator or merger captures `I1`, refreshes X onto it, resolves conflicts against the spec and both intents, and reruns affected checks.
2. If the integration tip changes to `I2` before landing, the `I1` results do not authorize landing. Refresh X against `I2` and repeat the affected verification.
3. Land X only after the fresh result passes. Record its integrated commit and evidence. Recompute readiness; only landing A unlocks B.
4. Take result Y from the queue. Capture the integration tip again, including X, then refresh and verify Y. Its original worker checks are insufficient. Never run two integration writers concurrently.

This is explicitly dictated by the skill. It is not necessary to refresh every unfinished worker whenever any ticket lands; the mandatory refresh occurs immediately before landing that result. [Implement-spec, lines 40-44](</C:/Users/josee/Code-Stuff/Projects/skills/skills/build-and-debug/implement-spec/SKILL.md:40>).

## Review and closure

- After A, B, and C land, run project-required checks and integrated acceptance checks. Give code-review the recorded baseline and the supplied spec. Its Standards and Spec agents independently review the integrated diff. Keep their reports separate. Repairs receive bounded tickets/workers and follow the same refresh, check, and serial-landing process. Rerun the checks and review areas those repairs affect. [Implement-spec, line 50](</C:/Users/josee/Code-Stuff/Projects/skills/skills/build-and-debug/implement-spec/SKILL.md:50>), [Code-review, lines 17-32 and 58-78](</C:/Users/josee/Code-Stuff/Projects/skills/skills/review-and-refactor/code-review/SKILL.md:17>).
- Open no PR: the scenario uses local Markdown and requests none. Store implementation commits, integrated commits, validation commands/results, and review evidence in local tickets according to their actual tracker rules. Completion is local; there is no pending PR merge requirement. [Implement-spec, lines 46 and 52](</C:/Users/josee/Code-Stuff/Projects/skills/skills/build-and-debug/implement-spec/SKILL.md:46>).
- Archive only this effort's managed worker worktrees after preserving commits and needed artifacts. Preserve unrelated dirty work, unrelated worktrees, and unmerged results. Report branch, ticket completion, checks, review findings or pass, and any real external step. [Implement-spec, lines 54-56](</C:/Users/josee/Code-Stuff/Projects/skills/skills/build-and-debug/implement-spec/SKILL.md:54>).

## Actionable gaps

### 1. Generated contracts need a source-of-truth instruction

The skill assigns ownership of generated contracts and tells workers to resolve conflicts by spec/intent, but it does not say to resolve authoritative generator inputs first and regenerate outputs. A worker can satisfy its wording by hand-merging generated files; ordinary type/build checks can pass while regeneration later removes the merged change. [Implement-spec, lines 19 and 42](</C:/Users/josee/Code-Stuff/Projects/skills/skills/build-and-debug/implement-spec/SKILL.md:19>).

Suggested addition: for generated files, identify authoritative inputs and the generation command in the dispatch brief. Resolve inputs, regenerate outputs, and verify regeneration is reproducible before accepting the result. Prefer project guidance when it specifies the generation order.

### 2. Final checks and reviews need one target commit

Landing checks compare the integration tip before landing, but the final phase records only the baseline. The code-review dependency uses `HEAD` in its diff and commit-list commands. If the integration branch advances during final checks or while the two review agents read it, evidence can refer to different target trees. [Implement-spec, lines 42 and 50](</C:/Users/josee/Code-Stuff/Projects/skills/skills/build-and-debug/implement-spec/SKILL.md:42>), [Code-review, lines 19-23](</C:/Users/josee/Code-Stuff/Projects/skills/skills/review-and-refactor/code-review/SKILL.md:19>).

Suggested addition: pin final integration commit `T`, run checks on its tree, and give both reviewers the same baseline/target commit pair. Before reporting completion, confirm the integration tip is still `T`; after repairs or unrelated tip changes, review and validate the affected changes before closure.

## Limits and supporting references

The exact local implementation status cannot be inferred from this abstract scenario. The bundled local tracker template defines `claimed`/`resolved` for wayfinding tickets, but does not define a general implementation-complete status. The skill correctly delegates completion to actual tracker rules; do not invent a status or claim closure from the example template. [Local tracker, lines 9-13 and 25-32](</C:/Users/josee/Code-Stuff/Projects/skills/skills/project-setup/setup-skills/issue-tracker-local.md:9>).

Dependencies read: `tdd`, `code-review`, `audit-implementation`, and the bundled local tracker/triage template. Focused audit details were not classified because this is a scheduling simulation with no implementation diff. No real tests or review agents ran.

## Resolution check

Checked the affected instructions on 11 October 2026 after the fixes. The initial simulation and findings above predate these edits; their original line pointers describe the evaluated version.

- **Generated contracts: addressed.** Implement-spec now requires reconciliation of authoritative inputs, regeneration through the established command/order, preservation of source ownership, and a reproducibility check. If the repository has no check, a second generation must produce no further changes. [Integration rule, line 44](</C:/Users/josee/Code-Stuff/Projects/skills/skills/build-and-debug/implement-spec/SKILL.md:44>).
- **Final target: addressed.** Implement-spec pins target `T`, runs checks on its tree, supplies the same baseline/target pair to code-review, pins repair results, and confirms the integration tip still matches the validated/reviewed target before closure. An advancing tip requires affected validation and review. Code-review resolves both revisions to SHAs, gives them to both agents, and reads source at the pinned target. [Completion rules, lines 52-56](</C:/Users/josee/Code-Stuff/Projects/skills/skills/build-and-debug/implement-spec/SKILL.md:52>), [review rules, lines 21-23](</C:/Users/josee/Code-Stuff/Projects/skills/skills/review-and-refactor/code-review/SKILL.md:21>).

The tracker section still delegates status and closure to the configured tracker while retaining local implementation/validation evidence. This targeted reread verifies that the written instructions address both findings. The evaluation remains simulation-only: no Git integration, generator, project checks, or real review agents ran.
