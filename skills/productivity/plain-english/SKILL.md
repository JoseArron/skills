---
name: plain-english
description: "Plain English house style for prose a person reads: second person, active voice, present tense, timeless wording (no currently, now, new), condition before instruction, key point first, jargon written around or defined once, no anthropomorphism, no claim you cannot check. Distilled from the Google developer documentation style guide. Use when writing or editing a code comment, docstring, ticket body, PR or commit description, README, doc, or any prose a colleague reads; when text reads stiff, vague, or hedged; or when asked to make writing clearer."
---

# Plain English

The reader gets one pass, cold, with nothing else open and nobody to ask. Every rule below buys
clarity on that pass.

These are the rules to write *toward*. `deslop-written` is the pass that strips AI tells out
afterwards. Write with this one, check with that one.

## Where this applies

Any prose a person reads: code comments and docstrings, commit messages, ticket bodies, PR
descriptions, READMEs, docs, chat replies, error and UI strings. Comments count. They are
documentation that happens to live in a source file, and they go stale the same way.

## 1. Second person, active voice

Address the reader as *you*. Name whoever performs the action.

| Write | Not |
|---|---|
| To retry the job, call `retryJob`. | The job can be retried. |
| You can override the timeout. | The timeout is allowed to be overridden. |

Passive voice hides the actor. If a sentence describes something being done, say who does it.

## 2. Present tense

Describe how things work in the present. Cut *will* and *would* from anything that describes
behavior.

| Write | Not |
|---|---|
| The server acknowledges the request. | The server will send an acknowledgment. |
| If you send an unsubscribe message, the server removes you from the list. | You can send an unsubscribe message. The server would then remove you. |

Future tense is right only for something that genuinely happens later: *the file is archived the
next time the backup runs.*

## 3. Timeless

Write what is true, not what changed. Words that pin text to the day it was written go stale
silently, and nobody notices until the text is lying.

**Cut on sight:** currently, now, new, newer, latest, soon, existing, old, older, eventually,
at present, as of this writing, does not yet, in the future.

| Write | Not |
|---|---|
| The emulator supports the following filters: | The emulator now supports the following filters: |
| These subcommands manage load balancing. | These new subcommands manage load balancing. |
| `getTotals` reads the ledger table. | `getTotals` now reads the ledger table instead of the view. |

The exception is text that is *about* a moment: release notes, changelogs, blog posts, incident
timelines. There, *new* and *soon* carry real information. If you have to date something anywhere
else, give the reference point: *the 14 January 2026 release adds a resource panel.*

## 4. Condition before instruction

Put the circumstance first, so a reader it does not apply to can skip the rest of the sentence.

| Write | Not |
|---|---|
| For more information, see the deployment guide. | See the deployment guide for more information. |
| To delete the whole invoice, click **Delete**. | Click **Delete** if you want to delete the whole invoice. |

## 5. Key point first, one idea at a time

Most important information first, in the sentence and in the paragraph. Readers do not reach the
end. One idea per paragraph, in the fewest sentences that hold it; a paragraph past five or six
sentences is usually two paragraphs.

Short sentences, one idea each. That is ASD-STE100 Simplified Technical English, and it is the
default register for everything here.

## 6. Jargon: write around it, or define it once

Jargon is a term that only lands for people already inside the group: *blast radius*, *shift left*,
*out-of-the-box*, *cutover*. So are vague catch-alls: *solution*, *support*, *workload*, *surface*.

Three fixes, in order of preference:

1. **Write around it.** *Hold a post-mortem* becomes *once the project ships, review what worked*.
2. **Replace it with the specific term.** *Blast radius* becomes *affected area*; *ingest* becomes
   *load*.
3. **Define it once, in parentheses, on first use.** *The standby is warm (already running, taking
   no traffic).*

Use the project's own words first. Whatever `GLOSSARY.md` under the configured agent root calls a
thing is what you call it. Do not invent a synonym for it.

## 7. No anthropomorphism

Software does not want, know, see, think, or try. Say what it does.

| Write | Not |
|---|---|
| The parser rejects the malformed row. | The parser doesn't like the malformed row. |
| `Delimiter` specifies where to split the string. | `Delimiter` tells the splitter where a string should be broken. |

## 8. No claim you cannot check

Drop superlatives you cannot back: *best*, *simplest*, *fastest*, *never*, *always*. Reach for
*ensure* and *guarantee* only when the thing is genuinely guaranteed.

| Write | Not |
|---|---|
| Batching cut p95 from 840 ms to 190 ms. | Batching makes it much faster. |
| Rate limiting helps prevent credential stuffing. | Rate limiting prevents credential stuffing. |

A security claim goes false the first time someone breaks it. *Helps with*, *is designed for*, and
a measured number all survive contact with reality.

## 9. Mechanics

- **Sentence case** for titles and headings: `Rotating the signing key`, not `Rotating The Signing Key`.
- **Code font** for anything that appears in code: identifiers, paths, flags, literals, values.
  Spell them exactly as the code spells them.
- **Repeat the domain noun** instead of a pronoun when the referent could be unclear a sentence
  later. Say *the Load*, not *it*.
- **Descriptive link text**: *see the deployment guide*, not *see here* or *click this link*.
- **Numbered lists** for sequences, **bulleted lists** for everything else.
- **No `please`**, and no exclamation marks.

## Code comments

Everything above applies. Two rules bite hardest here:

- Rule 3. A comment that narrates what the code *used to* do is a timeless violation with a longer
  fuse. Keep comments on present, load-bearing facts: a business rule, an invariant, a deliberately
  deferred decision. `concrete-naming` has the full comment-versus-commit-message test.
- For a comment documenting a callable (docstring, Javadoc, JSDoc), phrase the summary as what it
  does, in the third person: *Creates a task on the list*, not *Create a task on the list*.

## Self-check

Every rule above, applied to the text before you hand it back. Then, in order:

1. Grep the rule 3 list. Zero hits outside changelogs, release notes, and incident timelines.
2. Grep `will `, `would `, `can be `, `is being`. Rewrite each one present-tense and active.
3. Read the first sentence of every paragraph on its own. Do they carry the argument? If not, the
   key points are buried.
4. Every superlative, every *ensure* and *guarantee*: back it with a number or cut it.
5. Every term a new joiner would not know: written around, replaced, or defined once.
6. Read it aloud. Any sentence you would not say to a colleague gets rewritten.
7. Run `deslop-written` last, to strip what this pass does not cover.

## Source

Distilled from the [Google developer documentation style guide](https://developers.google.com/style/).
The rules above are the ones that change what gets written. That guide's A-to-Z word list is a
lookup rather than context: consult it at the source when one specific word is in question.
