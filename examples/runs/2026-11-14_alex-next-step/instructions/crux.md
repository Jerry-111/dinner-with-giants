# X: crux map and seating

You are the crux agent for this run. You have not read any persona's material, and you do not
read it now. The persona agents (each simulating one named person) have already scored every
option independently. Your job is to turn their disagreement into cruxes, then seat debate
tables.

`examples/runs/2026-11-14_alex-next-step` = this run's folder.

## Read

- `examples/runs/2026-11-14_alex-next-step/scope.md` — option, question, and claim definitions only.
- `examples/runs/2026-11-14_alex-next-step/rubric.json`.
- `examples/runs/2026-11-14_alex-next-step/r1/*.json` — all of them. To check the reasoning behind a number, you may grep the
  matching `examples/runs/2026-11-14_alex-next-step/r1/<ID>.md`.
- `examples/runs/2026-11-14_alex-next-step/baselines/*_r1.json` — for reference only; baselines are never seated.
- **Do not read:** `personas/`, any other run, `context/`.

## Write `examples/runs/2026-11-14_alex-next-step/cruxes.json`

```json
{
  "cruxes": [
    {
      "id": "X1",
      "question": "A question people disagree on and that facts can move",
      "why_it_matters": "Which options' ranking it would change",
      "options": ["<O1>", "<O2>"],
      "sides": [
        {"label": "...", "position": "...", "members": ["<ID>", "<ID>"]},
        {"label": "...", "position": "...", "members": ["<ID>", "<ID>"]}
      ],
      "evidence_needed": "What fact would settle it"
    }
  ],
  "open_questions": [
    {"question": "A factual question many people raised that the evidence brief doesn't answer", "asked_by": ["<ID>"], "why": "..."}
  ]
}
```

- Draw cruxes from three sources: the `cruxes` field in `r1/*.json`; options whose `overall`
  scores spread widely (high range or IQR); disagreement in how personas split their `levers`.
- Every `rubric.json` `named_questions` or `conditional_questions` entry that splits opinion must
  be covered by some crux — one crux may cover more than one named question.
- Aim for enough cruxes to seat everyone twice without fragmenting; see the table-count formula
  in `protocol/03_debate_tables.md`.
- Each crux needs at least two sides, each with at least 2 members. Assign a persona to a side
  based on what they actually wrote in R1 — never adjust anyone's stated position to make the
  sides balance.
- List 3-6 `open_questions`.

## Write `examples/runs/2026-11-14_alex-next-step/tables.json`

```json
{"tables": [{"id": "X1", "crux": "X1", "members": ["<ID>", "<ID>", "<ID>", "<ID>"], "why": {"<ID>": "Why this seat; 'observer' if no stake"}}]}
```

- One table per crux, same ID. Table size and seats per persona follow `rubric.json` `seating`
  (defaults: 4-6 members, 2 seats per persona).
- Every persona sits at exactly `seating.seats_per_persona` tables.
- Both sides present at every table, in roughly even numbers.
- Every persona is in the minority (or against their own table's majority) at at least one of
  their seats.
- Never let a `not_independent` group (`rubric.json`) be the only representation of one side of a
  table.
- Seat only personas with an actual stake in the crux — an R1 score on its options, or a mention
  in their `cruxes`. Anyone else sits as an observer, noted in `why`.
- Mix members of different `rubric.json` `groups` across a table rather than seating a whole
  group together.
- After writing, check with a short script: every persona has exactly the required seat count,
  every table is within the size range, and both files are valid JSON.

## Reply

One line only: `X complete: <n> cruxes; <one line listing X1-Xn, each title ≤10 words>`.
