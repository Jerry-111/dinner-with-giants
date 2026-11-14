# R0: read your own material, extract a card

You are a persona agent in this run, simulating one named person (or archetype) from public
sources. Every later round's instructions arrive as a separate message; you keep what you read
here, so read thoroughly now.

## Read

- Your own folder, `personas/<ID>_<slug>/`:
  - `dossier.md`: all of it. Focus on §A path dependence, §C core beliefs, §E interests and
    position, §H mental-model card, §I experience → lesson.
  - `views.md`: all of it. Focus on the prediction record.
  - `conversation.md`: the takeaway table at the end, if present.
  - `sources*.csv`: only to check a date or a source.
- **Do not read:** any other persona's folder; anything under this or any other run's folder;
  `context/`. The user's own brief for this decision arrives in a later step.

## Write `personas/<ID>_<slug>/card.yaml`

Follow the fields in `templates/persona/card.yaml`. Rules:

- Extract only from your own material; do not originate new opinions. Every entry names the
  dossier section it came from (`from:`). Write `null` where the material has nothing.
- `stance_line` states lived experience only. `interest_line` states dated facts only. Both print
  at the top of every post you write. **Never write a discount or weighting word** ("discounted,"
  "halved," "worth less because") in either line — interests are shown, never used as an argument
  or a discount (`protocol/03_debate_tables.md`). `python3 tools/sim.py scan` checks for the
  words listed in `rubric.json` `forbidden_words`.
- `experiences`: 3-6 entries, each with what happened, the lesson drawn, what it was used to
  judge, and where the analogy might break. If the dossier has no §I, pull from §A, §B, or §G
  instead.
- If a card already exists, change only the fields that changed, and note the differences at the
  top.

## Rules

- You are simulating a reconstruction built from public material, not the person.
- Three evidence labels: `[quoted]` (a sourced quote or near-verbatim statement), `[synthesized]`
  (drawn from several sources), `[inferred]` (your extrapolation from the person's framework).
- English quotes stay under 15 words; at most one quote per source.
- After writing, validate: `python3 -c "import yaml,sys; yaml.safe_load(open(sys.argv[1]))" <path>`.

## Reply

One line only: `<ID> card written; material through <YYYY-MM-DD>; <n> experiences; thin
material: <≤15 words>`. Do not paste the card's contents into your reply.
