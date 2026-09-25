---
name: plain-tickets
description: Name and write tickets, issues, ADRs and board tasks so they land cold — a plain verb phrase for the name, never a codename, and reader-facing prose in short active sentences using only words the codebase already uses. Use when naming or renaming a ticket, issue, board task, ADR or branch; when writing a ticket's description or summary; when a name gets the reaction "what does that even mean"; or when asked to make a task read better.
---

# Plain tickets

A ticket name is read in a list, cold, months later, with nothing else open. That is the whole
budget. Everything here follows from it.

## The three names, and their different jobs

One ticket carries three names. They are not the same length and not the same job.

| Name | Length | Job |
| --- | --- | --- |
| **File slug** | 2–4 words after the number | Sort and find it on disk. `new-07-fix-missing-column.md` |
| **Board name** | 3–7 words, one clause | Point at the thing, in a list of thirty. `Split Missing into loss and lacking` |
| **H1** | one line, may add a clause after an em dash | Name the thing, then say what the change is. Body carries mechanics like endpoint moves and regen order — the H1 does not need to. |

Mechanics — how it ships, what it breaks, who rebases — go in the body. Never in the name.

## Naming: five tests, in order

**1. Is it a codename?** Delete it. "THE CUT", "Project Lighthouse", "the big one". A codename feels
like shared shorthand and is shorthand for exactly one person: whoever coined it. Everyone else
reads it and asks what it means. It also spreads — one codename reached 23 files and 53 mentions
before anyone said "what is the cut supposed to mean".

**2. Can you say it out loud as one sentence?** If the name has three clauses bolted together, it is
notes, not a name. `Stop the Missing column hiding loss, in one regen` fails. Two ideas and a build
step jammed into a title.

**3. Does it start with a verb and name a thing that exists?** The default shape is `Fix <the thing>`.
Reach for `Rename`, `Delete`, `Seed`, `Bring`, `Consolidate` when they are more exact. The thing
should be something the reader can point at — a column header, a field name, a screen, a table.

**4. Does every word appear in the codebase or on screen?** If a word only exists in a design doc,
an ADR, or your head, it does not go in the name. No build-step vocabulary either: `regen`, `seam`,
`cutover`, `fold`, `ledger`, `slice`. Those are how the work happens, not what is wrong.

**5. Would it still make sense to someone who has not read the ticket?** If not, it is not shorter,
it is just missing.

**6. Does the name accidentally claim the wrong kind of fix?** A name built around *where the bug
shows* can misdirect about *what changes*. `Fix the Missing column` names a real thing on screen, but
reads as a frontend display bug when the actual work is a three-way API contract break with a client
rename riding along. Naming the mechanism instead — what actually happens to the data — avoids this
without losing concreteness. `Split Missing into loss and lacking` says two things happen to one
value; nothing here can be mistaken for a CSS fix.

### Ambiguity beats brevity every time

A shorter name that can be read two ways is worse than a longer one that cannot.

`Fix missing counts` is shorter than `Fix the Missing column`. It is also worse: "missing counts"
reads as *counts that are missing* — which is a real, different defect. Capital-M **Missing** is the
column header on screen; lowercase *missing* is an adjective. One character of casing is doing work
the reader will not notice.

Before shortening, read the short version as if you had never seen the ticket. If a second meaning
appears, keep the longer name.

## Writing the reader-facing zones

Ticket descriptions, issue summaries, board copy, chat replies. Not the spec body, not code
comments.

Write them in `plain-english`: short active sentences, present tense, the project's own glossary
words, the key point first. Three rules sit on top of it, specific to tickets:

- **Lead with the defect in one sentence**, then the evidence, then the fix. Not the other way round.
- **Every claim names its symbol and path.** `loadTypeHasCustomer returns true for refill —
  client/apps/mobile/lib/load-plan.ts:16`. A claim with no path is a rumour.
- **Verify before filing.** Open the file. If the defect moved or was fixed, the ticket is wrong on
  arrival and everything downstream inherits the error.

## Worked example

The real path a ticket took, including the wrong middle step.

**Before.** `THE CUT — honest loss reporting: response shape, endpoint paths and names, in one regen`

Codename (test 1). Three clauses (test 2). `regen` is a build step (test 4). "the cut" meant *one
cutover*, which the name never says.

**First attempt.** `Stop the Missing column hiding loss, in one regen`

Still fails. `Stop X hiding Y` inverts the sentence to force the defect into the title, and `regen`
survived. The reaction was "it still sounds like words just placed together".

**Second attempt.** `Fix the Missing column`

Passes tests 1–5. Verb, three words, points at a real header on screen. But it fails test 6: it reads
as a frontend display bug, when most of the ticket is a backend contract break — a response-shape
rename, endpoint paths moving, a field rename — with a small client cleanup riding along. The
reaction was "if we're going with column it reads more like a display bug on the frontend, right?".
It was.

**Shipped.** `Split Missing into loss and lacking`

Names the mechanism, not the location. One merged value becomes two named ones —
`countVariance` (loss) and `emptiesLacking`. Nothing here can be misread as a calculation fix (nothing
is recalculated) or a display fix (the split happens in the API response, not the render). The three
contract breaks and the regen order still live in the body.

## Rewriting a description

**Before:** *"Taking the larger of the two hides theft whenever customers hold more empties than the
Branch has lost. The engine underneath is correct; the API named its results wrong."*

**After:** *"The page shows the larger of the two. So when customers hold more empties than the Depot
lost, the loss disappears from the screen. The calculation is correct. The API gave its results the
wrong names."*

What changed: one idea per sentence, "engine underneath" replaced with the plain "calculation",
Branch/Depot matched to the glossary, and the semicolon split into two sentences.

## Renaming something that already shipped

A name that spread costs a sweep. Do the whole sweep in one pass.

1. Change the board name and H1 first. Zero link cost.
2. Rename the file, then update every link to it.
3. Sweep the old nickname out of prose. Grep it. Ordinary-looking phrases are usually the nickname
   too.
4. Check nothing is left: the grep must return zero, not "a few harmless ones".
5. Back up first if the docs are not under version control.
