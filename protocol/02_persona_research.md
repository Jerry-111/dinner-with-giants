# Step 1: persona research

One **persona agent** per persona, run concurrently. The goal is to rebuild how this person
reasons, not to write a biography.

## Files per persona

| File | Contents | Template |
|---|---|---|
| `personas/<ID>_<slug>/dossier.md` | Sections A–I (below) | `templates/persona/dossier.md` |
| `personas/<ID>_<slug>/views.md` | Overall judgment, per-area judgment table, prediction record, where this persona is most likely wrong | `templates/persona/views.md` |
| `personas/<ID>_<slug>/conversation.md` | Simulated long conversation with the user, ending in a takeaway table — write only if the run calls for it | `templates/persona/conversation.md` |
| `personas/<ID>_<slug>/card.yaml` | Machine-readable summary, printed at the top of every prompt and every debate post | `templates/persona/card.yaml` |
| `personas/<ID>_<slug>/sources.csv` | Sources table, fixed columns | `templates/persona/sources.csv` |

Dossier sections A–I: (A) path dependence — what shaped this person; (B) at least two wins and
two failures, lived or witnessed, and the lesson drawn from each; (C) core beliefs and
positions; (D) how the views evolved; (E) interests and position, with dates — shown to the
reader, never applied as a discount (`AGENTS.md`); (F) the person's actual advice to people
starting out, and which parts transfer; (G) long-form notes from at least three long
interviews or texts, stating what range was actually read; (H) a mental-model card (variables
this person cares about, habitual heuristics, red lines); (I) experience → lesson — the 3–6
stories this person returns to most, each with its source, the lesson drawn, what they judged
with it, and where the analogy may break. **Experience arguments in debate may only draw on
section I (and A, B, G).** If an older dossier predates section I, backfill it before reuse.

The **prediction record** in `views.md` (4–8 dated predictions with outcomes) is the most
useful part of a persona: it tells the reader how far to trust this person's direction and
timing calls. It describes the persona for the reader — it is never used to weight that
persona's arguments in debate.

## Card rules

- Extract only from this persona's own folder; name the section every entry came from; missing
  is `null`.
- `stance_line` states lived experience only; `interest_line` states dated facts only. Neither
  carries an evaluative word — anything listed in `rubric.json`'s `forbidden_words` (for
  example "discount"). These two lines print at the top of every post this persona writes:
  write a discount into the card and you've told every other persona at the table to discount
  it for them. `tools/sim.py scan` checks this.

## Checking quotes

Before a persona is used, run `python3 tools/sim.py quotes <persona folder> --fetch`. It checks
that every `[quoted]` passage is under 15 words, cites an evidence id that exists in
`sources.csv`, and that no source supplies more than one quote; with `--fetch` it also looks for
each quote verbatim on its source page. Fix every error, and check by hand each quote it could
not find. CI runs the same check without `--fetch`.

## Choosing personas

`card.yaml`'s `kind` field is one of:

- **`historical`** — a real person no longer living, with an extensive public or archival
  record. A full dossier, including sourced experience arguments, is usually possible.
- **`public_figure`** — a real, living person with a substantial public record of their own
  views. Same as above, plus three obligations from `RESPONSIBLE_USE.md`: no judgments of the
  person's character (track records are dated predictions with outcomes and sources, not
  verdicts); every role, company, departure or deal carries a source and an "as of" date, and
  unconfirmed claims are dropped; links to the vendor of the model running the simulation are
  disclosed. Prefer this kind when the run needs a fidelity test — `11_fidelity_test.md`
  requires dated public statements after the analysis model's training cutoff, which only a
  living, currently-public person can have.
- **`archetype`** — a composite role (for example, "a risk-averse later-stage investor") not
  tied to any one real person. Cannot support sourced experience arguments: there is no real
  biography to cite. Stories in section I must be labeled illustrative or invented, never
  attributed to a real event.
- **`fictional`** — a named invented character. Same constraint as `archetype`: label
  everything illustrative.

Use `historical` and `public_figure` personas when an argument needs to rest on something that
actually happened to someone. Use `archetype` or `fictional` personas to cover a stance the
real roster is missing, or deliberately to contrast with real personas — never to pad the
headcount, and never with an invented story dressed up as sourced.

## Reusing and updating a persona

- Read the persona's existing files first; add only what changed — new interviews, a role
  change, a prediction that resolved — in roughly the last six months.
- New sources go in `sources_v<N>.csv`, numbered onward from the existing table (for example
  `H2-E30`).
- Add a "Changes from the previous version" note at the end of the dossier: what changed, why.
- Update the materials-through date at the top of every file, and the card.
- Refresh a persona before reuse whenever its material is more than about six months old and
  the run needs a time-sensitive judgment from it.

## Quality bar

- Strip the names, and the outputs should still differ in the variables each persona weighs,
  the arguments it makes, and what would change its mind.
- Be faithful to the person: if they would give aggressive advice, write that. Don't converge
  everyone toward safe consensus, and don't invent disagreement for variety.
- Scores reflect this person's actual judgment; interests don't self-discount it (`AGENTS.md`).
  The persona reports its interests; the reader does the discounting.
- Write the conversation as an opinionated exchange — like 30 real minutes with this person —
  not a checklist.
- For every judgment that matters, say what belief and what cost sits behind it.
- Judge how well a persona matches the real person with `11_fidelity_test.md`, not by feel.

## Essentials for the persona agent's prompt

- Read only: this persona's own folder, `scope.md`, the evidence brief, and
  `workspace/context/`. Not other personas' files, not previous runs' reports.
- Give the full output path.
- State the web-search budget (Round 1 default: 3 searches).
- Require a self-check before submitting: every claim labeled; quotes within the rules;
  `sources.csv` readable by a CSV parser; any JSON valid under `python3 -m json.tool`.
