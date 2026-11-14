# Consult mode: how would they see this

For a single, specific question — "how would persona X see this choice" — without running the
full protocol.

## Steps

1. Read `workspace/context/`: the user's background, preferences, and latest feedback.
2. Read the persona's material:
   - `dossier.md` section H (mental-model card) and section E (interests and position).
   - `views.md`'s prediction record — shown to the user so they can see how this person's
     direction and timing calls have held up. The persona does not weaken its own answer
     because of it.
   - `conversation.md`'s takeaway table, if one exists.
   - If the question is about a topic area this persona has evaluated before, the relevant
     part of that evaluation.
3. If the question turns on a current fact (a role, a release, a funding event), search for it
   and date what you find. Don't answer a time-sensitive question from stale material.
4. Answer in this persona's own judgment style. Template: `templates/run/consult.md`.

## Output

- The one or two questions they would ask back first.
- Their judgment and reasoning, labeled `[quoted]` / `[synthesized]` / `[inferred]`.
- Where they would push back on the user.
- Interests and track record, as facts for the user to weigh: the persona's stake in the
  answer, and whether its past calls ran early or late. Shown, never applied as a discount by
  the persona or the agent (`AGENTS.md`).
- One screen, not a report.

## Panel mode

When the user wants to see where people disagree, pick two to four personas with genuinely different
lenses — for example, one who reasons from capital and valuation, one from platforms and cost
structure, one from hands-on experience and track record — and write one short, independent
take from each; they don't see each other's answers. Close with where they disagree and what
evidence would settle it.

This is lighter than a panel-sized full run (`00_overview.md`): no debate table, no scoring, no
crux mapping, just parallel short takes and a disagreement list. Reach for a real panel run
instead when the disagreement is worth an hour of structured argument, not three paragraphs.

## Saving a consult

If it's worth keeping, save it to `workspace/runs/<date>_consult_<topic>.md`.
