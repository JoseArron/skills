---
name: understand-the-user
description: >
  Build and maintain a grounded picture of the project's users before designing
  solutions — personas, jobs-to-be-done, as-is/to-be workflows, and the
  assumptions under them, each tagged evidence or assumption. Use when kicking
  off a project or feature, before a PRD or user stories, when the team is
  guessing what users "want," or when another skill needs the user's goals or
  mental model.
---

# Understand the User

Establish who you're building for and what they're trying to get done — before any screen exists. The output is the **user brief**: a **project-wide living doc**.

This is **problem space**; designing the screens is `/ux-flows` (**solution space**). Research that drifts into UI is research cut short — finish the picture first.

## You are not the user

Every claim about the user is an **assumption** until grounded. Invented personas are theater. Tag each claim `[E]` evidence (observed, told, or pointed to) or `[A]` assumption (a guess) — and never launder an `[A]` into an `[E]`. The whole skill is a machine for turning assumptions into evidence, or marking the ones you can't.

## Run it as an interview

An **interview, not a one-shot generator** — closer to `/grilling` than to `/to-prd`. Don't ask it to "write personas"; that invents fiction. Invoke it with bare context — *who and what you're building* — and answer **one question at a time** as it builds the brief: who's the primary user, what are they getting done, walk me through how they do it today, *how do you know that — did you see it or assume it?* Same relentless one-at-a-time style as a grill, aimed at the **user** instead of the **plan**.

With real input already in hand — research notes, transcripts, analytics, a client's requirements — paste it in; it synthesizes from that and interviews you only to fill gaps and challenge the shaky parts.

## When it runs

Twice over a project's life, both writing the same brief:

- **Once at kickoff** — seed the brief before the first PRD writes user stories on guesses.
- **Per feature, as needed** — when a feature raises a user question `/grilling` can't reach. Grilling stress-tests the *plan*; this stress-tests *what you believe about the user*. Read the standing brief, refine it, fold back what you learn.

If you already hold a grounded picture, skip to `/to-prd`.

## The moves

Iterate, don't march — but by the end every move is accounted for.

**1 · Frame the job.** State the *job* before the feature: "When [situation], I want to [motivation], so I can [outcome]." People don't want a quarter-inch drill; they want a quarter-inch hole. The feature is your *bet* on doing the job better — name the job so you can later tell whether the bet paid. _Done when:_ the job reads as an outcome, with no solution smuggled into it.

**2 · Sketch the persona — lean and goal-shaped.** One short profile per genuinely distinct user type: their **goal**, **context** (where/when, what device, under what pressure), **proficiency** (with the domain *and* the tooling), and the **pains** they carry. Cut any demographic that wouldn't change a decision. _Done when:_ each line is tagged `[E]`/`[A]` and you can say why this type is distinct from the others.

**3 · Map the workflow: as-is → to-be.**
- **As-is** — the persona's *current* end-to-end workflow, step by step, including the workarounds. Mark every friction point.
- **To-be** — the same journey with your solution in it. The solution's value is the **delta**: friction removed, steps collapsed, waits killed.

The win often lives *between* steps — a handoff, a wait — where no screen exists, so map the journey, not a screen. _Done when:_ the to-be map is visibly better than as-is *at the marked pain points*. If it isn't, the solution is aimed wrong — say so.

**4 · Capture the mental model.** How does the persona *think* this works — their words, their categories, their cause-and-effect? Record it, because `/ux-flows` has to match it. Users get confused wherever their model and the system's diverge; hand any term whose meaning differs to `/domain-modeling`. _Done when:_ the model is written in the user's vocabulary, not the system's.

**5 · Audit the assumptions.** The spine. Collect every `[A]` from moves 1–4, plus anything the team treats as settled without proof, and place each in the grid:

| | Low impact | High impact |
|---|---|---|
| **High confidence** | note, move on | state it, build on it |
| **Low confidence** | record as a risk | **validate before building** |

Then handle the unknowns honestly:
- **Known unknowns** — questions you know you can't answer → validate the high-impact ones now (one interview question, a `/prototype` probe, a five-minute test); log the rest as open questions.
- **Unknown unknowns** — what you can't see from your desk → only contact with real users (and, later, `/ux-review`) surfaces these. The honest move is to declare the picture partial and design a cheap way to learn.
- **Unknown knowns** — the dangerous ones: "everybody knows" beliefs nobody checked. Drag them onto the list and tag them `[A]`.

_Done when:_ no high-impact, low-confidence assumption is left without either a validation plan or an explicit, written acceptance of the risk.

## Output: the user brief

The **standing spine** — personas, jobs, mental model, and durable user-level assumptions — lives in a project-wide **`USER-BRIEF.md`**, under whatever root `/setup-skills` configured (`docs/agents/` by default — check the `## Agent skills` block in `CLAUDE.md`/`AGENTS.md` for the **Artifacts root** line, then `domain.md` there for the detail). Created **lazily** — only the moves you actually ran — and **maintained inline** as you learn. Use the template in [BRIEF-FORMAT.md](./BRIEF-FORMAT.md).

The **per-feature parts** — this feature's as-is→to-be journey and its feature-scoped assumptions — belong with that feature's planning, where `/to-prd` folds them into the PRD (journey → problem/solution, assumption ledger → risks). Promote `[A]`→`[E]` in the standing brief whenever `/grilling` or `/prototype` resolves one.

On a cold start with no user knowledge yet, you may have nothing to write first — then `/grilling` comes first and the brief is its *precipitate*, not its input.

## Checklist before done

- [ ] Job stated as an outcome, before any feature.
- [ ] Each persona line tagged `[E]` vs `[A]` — nothing laundered.
- [ ] As-is map shows real friction; to-be map beats it *at those points*.
- [ ] Mental model written in the user's words.
- [ ] Every high-impact, low-confidence assumption has a validation plan or a written risk.
- [ ] Open questions and unknowns are on the page, not hidden.
- [ ] Standing spine written to `USER-BRIEF.md`; per-feature journey/assumptions handed to `/to-prd`.
