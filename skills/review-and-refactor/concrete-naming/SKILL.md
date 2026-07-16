---
name: concrete-naming
description: Naming and comment conventions that keep code readable without a change log baked into it — subject-first names for data (itemsCharged not chargedItems), verb-first names for actions (validateChargeOnInvoice not check), full domain terms instead of abbreviations or metaphors (PaymentTransactionLogService not PaymentJournalService), and comments that describe current behavior or business rules only — never git history, rename rationale, process notes, or which tool wrote the code. Use when naming a new type, class, method, or variable, when renaming something for clarity, when reviewing or writing code comments, when a teammate's edit reveals a naming pattern worth generalizing across a file, or when asked to "clean up naming," "make this read better," "why comment it that way," or "these names feel inconsistent."
---

# Concrete Naming

Every name and every comment should point at something real and current: a
domain noun, a business rule, a fact that is true right now. Not at process
(how the code got written), not at history (what it replaced), not at a
vague abstraction that could mean anything.

That splits into three habits: order data names subject-first, order action
names verb-first, and keep comments in the present tense.

## 1. Data: subject first, qualifier second

Types, classes, and variables name a *thing*. Lead with the concrete noun —
the entity or subject — then attach the qualifier (state, role, relation)
after it. Reading left to right should answer "what is this" before "what
happened to it" or "what kind of role does it play."

| Weak (qualifier first) | Strong (subject first) | Why |
|---|---|---|
| `chargedItems`, `refundedItems` | `itemsCharged`, `itemsRefunded` | Reads like a report column ("Items Charged: 4"), not an adjective-noun phrase |
| `PaymentJournalService` | `PaymentTransactionLogService` | Names the entity it operates on, not a metaphor for what that entity is |
| `LoadedInvoiceRecord` | `InvoiceRecordPopulated` | Entity first; "populated" is a state suffix, not a prefix modifier |
| `ChargeInputValidator` | `PaymentChargeValidator` | Uses the real entity name (`PaymentCharge`) that the rest of the codebase already uses, not a shorthand invented for this one class |

This is not "always reverse the word order" — it's "put the noun the reader
is scanning for at the front." A file full of `PaymentTransactionLog*` names
sorts and scans together; a file mixing `LoadedX`, `XPopulated`, `PendingX`,
`XPending` makes the reader hold every naming scheme in their head at once.

## 2. Actions: verb first, reads like a command

Methods and functions *do* something. Lead with the verb, in the imperative,
and let the rest of the name finish the sentence a caller would say out loud.
A terse or generic verb forces the reader to open the function body to find
out what it actually checks or returns — a fuller name answers that at the
call site.

| Weak | Strong | Why |
|---|---|---|
| `check(invoice, charges)` | `validateChargesOnInvoice(invoice, charges)` | Says what's being validated and against what, not just "some check happens" |
| `totalsFor(invoiceIds)` | `getTotalsPerInvoice(invoiceIds)` | "get" + noun + grouping reads as a full sentence fragment |
| `paymentTotalsFromEntries(entries)` | `getTotalsFromEntries(entries)` | This is a derivation, not a stored thing — verb-first matches its sibling `getTotalsPerInvoice` instead of looking like an unrelated naming scheme |

Data types are nouns because they sit still. Functions are verbs because
they act. Naming a function like a noun (`paymentTotalsFromEntries`) makes it
look like a value you could store, when it's actually a step you run.

## 3. Comments: what's true now, not how it got that way

A comment earns its place by telling the reader something the code can't say
on its own: a business rule, an invariant, a deliberately deferred decision,
or a concrete example that resolves an ambiguity. It loses its place the
moment it starts narrating the code's history instead of its present.

**Cut on sight** — anything that only makes sense to someone who was in the
room when the change was made:

```
// tx is no longer passed as a param since we now rely on AsyncLocalStorage
// per the transaction-scope design review
```
```
// renamed from PaymentJournalService — "journal" wasn't in our domain vocabulary
```
```
// switched from a manual date check to date-fns per the discussion in review
```

None of that is wrong, exactly — it's just misfiled. It belongs in the
commit message or the pull request description, which are append-only and
built for exactly this. A code comment lives inside the file it describes and
gets read by everyone who opens that file forever after; a rename's
rationale read by someone six months later, after three more renames, is not
information, it's noise that outlived its relevance. If the *why* still
matters architecturally, write it once in a design doc and let the comment
point at a stable business rule instead of the doc's history.

**Keep, because these describe a present, load-bearing fact:**

```
// a customer can't be charged twice for the same line item on one invoice
```
```
// for now the ceiling is billed + requested <= authorized;
// revisit once partial authorization ships
```
```
// rejects duplicate line items like [{sku: 'A', qty: 1}, {sku: 'A', qty: 2}]
// — caller should combine them first
```

The test: delete the comment and read the line cold. If what's missing is a
business rule, an edge case, or a "this is intentionally not the final
formula" flag, put the comment back. If what's missing is a story about the
code's past, leave it out — the diff and the commit message already told
that story, permanently, without rotting.

## Why this is worth the extra few seconds

A qualifier-first name and a subject-first name cost the same number of
characters. The difference only shows up when someone is scanning a file or
autocompleting: `StockMovement*` clusters together, `LoadedX` / `XPopulated`
/ `PendingX` doesn't cluster with anything. A history-comment costs nothing
to write and everything to maintain — it's accurate for exactly as long as
nobody touches the code again, then it silently starts lying. A comment about
a business rule stays true as long as the rule does.

## Self-check

Before committing a name or a comment, ask:

- **Type, class, or variable?** Does the first word answer "what is this,"
  not "what happened to it" or "what state is it in"?
- **Method or function?** Does it start with a verb, and would reading it
  aloud describe what the call site is actually asking for?
- **Full term or house shorthand?** Does the name match the entity name used
  elsewhere in the codebase, rather than inventing a new abbreviation or
  metaphor for this one spot?
- **Comment: rule or story?** If it explains a business rule, a deferred
  decision, or a genuinely ambiguous shape — keep it, short. If it explains
  how the code used to look, who asked for the change, or which tool wrote
  it — delete it; that belongs in the commit message.

One caveat: this is for greenfield naming, cleaning up drift, or
generalizing a pattern a teammate just modeled in their own edit — not for
unilaterally overriding a codebase's existing, consistent house style. If a
project already has a different convention applied consistently, match that
first.
