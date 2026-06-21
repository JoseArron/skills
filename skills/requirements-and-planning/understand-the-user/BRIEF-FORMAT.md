# User Brief — format

A durable, skimmable picture of the user. It is a **project-wide living doc** (`USER-BRIEF.md`, under whatever root `/setup-skills` configured — `docs/agents/` by default): seeded once, maintained inline as you learn. Devoid of solution detail (that belongs in the PRD) and of UI detail (that belongs to `/ux-flows`).

Every claim carries a tag — `[E]` evidence (observed, told, or linked) or `[A]` assumption (a guess, still to validate). The tags are the point: a brief of all `[A]` is a list of things to go find out, not a finding.

Create only the sections whose move you ran. Keep it a brief, not a report.

## Two layers

- **Standing spine** — *Job*, *Personas*, *Mental model*, and the durable rows of the *Assumption ledger*. These describe **who the user is**, hold across features, and live in the project-wide `USER-BRIEF.md`.
- **Per-feature pass** — the *Journey (as-is → to-be)* and the feature-scoped assumptions/open questions a single feature raises. Produced when `understand-the-user` runs for that feature; `/to-prd` folds them into the PRD (journey → problem/solution, ledger → risks). Keep them with the feature's planning, not in the standing spine — but promote any *durable* user fact they surface back into the spine.

---

## Job

> When [situation], I want to [motivation], so I can [outcome].

One line per distinct job. The outcome, never the feature.

## Personas

One block per genuinely distinct user type:

**[Role / name]**
- Goal: … `[E/A]`
- Context: where / when, device, pressure … `[E/A]`
- Proficiency: domain … · tooling … `[E/A]`
- Pains: … `[E/A]`

_Illustration:_

**Dispatcher (night shift)**
- Goal: clear the morning queue before drivers arrive `[E]`
- Context: desktop, 5–6am, interrupted constantly by phone `[A]`
- Proficiency: deep domain, low patience for new tools `[E]`
- Pains: re-keys the same order into three systems `[E]`

## Mental model

How the user thinks it works, in their words. Note any term whose meaning differs from the system's, and hand that term to `/domain-modeling`.

## Assumption ledger

| Claim | Tag | Confidence | Impact | Action |
|---|---|---|---|---|
| drivers arrive ~6am | `[A]` | low | high | **validate** — ask 3 dispatchers |
| … | `[A]` | … | … | record as risk / open question |

Promote a claim to `[E]` once you have a source; cite it. Durable rows stay in the spine; feature-scoped ones travel with the feature.

## Journey: as-is → to-be _(per-feature)_

| # | As-is step | Friction | To-be step | Delta |
|---|---|---|---|---|
| 1 | … | ⚠ … | … | what improved |

Flag the steps where friction is worst; the to-be column has to beat them — that delta *is* the value of the work. This is per-feature; it flows into the PRD.

## Open questions

- The things you know you don't know. Send the costly ones to `/grilling` or a `/prototype` probe before they harden into wrong decisions.

## Downstream & back — who reads *and writes* this brief

The brief is the artifact the rest of the pipeline shares — but it's **living**, not frozen on first write:

- **`/grilling`** ⇄ the brief, **both ways**. Seed the grill with the brief's **open questions and `[A]` rows** as targets to attack — but the brief is *fuel, never a constraint*: the grill still invents its own questions, challenges even the `[E]` claims, and **writes back** what it learns about the user (promote `[A]`→`[E]`, add rows). The system glossary the grill forges via `/domain-modeling` is a *different* artifact — the agreed system language, not the user's goals — so the brief can't pre-empt it. Because the brief is problem-space and the grill's generative work is plan-space, feeding it the brief only stops the grill re-deriving *who the user is*; it never closes the plan questions.
- **`/to-prd`** maps the brief into a PRD: **job + personas → user stories** ("As a [persona], I want [job step], so that [outcome]"), **as-is/to-be → problem statement + solution**, **assumption ledger → risks / further notes**.
- **`/ux-flows`** and **`/ux-review`** read the **mental model** to design and audit against how the user actually thinks.
