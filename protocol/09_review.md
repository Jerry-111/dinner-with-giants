# Review mode: put a draft in front of the room

For a draft you want torn apart before it meets its real audience: a research proposal, a paper,
a pitch, a product spec, an essay, a plan. Each persona reads it through its own path and finds
the problems that its experience makes it see. The value is in the different biases, so the
panel is picked for different lenses, and the critiques are kept apart until all of them are in.

Use `/deliberate` instead when you are choosing between options; use `/consult` for a quick
question.

## Inputs

- **The artifact.** A file (Markdown, plain text, the text of a PDF, a design doc) or pasted
  text. The orchestrator saves a copy as `artifact.md` in the run folder; reviewers read only
  that copy.
- **The brief** (`brief.md`): what the artifact is for, who its audience is, what the user wants
  checked, and what the user does not want to change.
- **The panel**: 3–5 personas with different `lens` lines in their `card.yaml`. Pick for
  difference, not for fame. For a startup pitch, for example: one persona who reasons from capital
  and valuation, one from platforms and cost, one from operating a company. For a research
  proposal: one from scale, one from lived experiments, one from evaluation.

## Steps

1. Create `workspace/runs/<YYYY-MM-DD>_review_<slug>/`; write `brief.md`; copy the artifact to
   `artifact.md`.
2. **Wave 1, independent critiques.** Launch one persona agent per persona, all at once. Each
   reads only its own persona folder, `brief.md` and `artifact.md`, and writes
   `critiques/<ID>.md` from `templates/run/review.md`. No persona sees another critique.
3. **Wave 2, cross-check.** Only when every critique is in, continue each persona agent and
   give it the other critiques. Each writes `cross/<ID>.md` from
   `templates/run/review_cross.md`: for every problem the others raised, agree or disagree with a
   one-line argument (no "partly"; split the point instead), plus at most one problem everyone
   missed. As at the debate tables, an argument counts; a headcount or a name does not.
4. **Synthesis.** A fresh editor agent that has not read the persona folders reads `brief.md`,
   `artifact.md`, `critiques/` and `cross/`, and writes `summary.md` from
   `templates/run/review_summary.md`:
   - the fix list: every distinct problem, its severity, who raised it, who disputed it and why,
     and a concrete fix, ordered by severity and by how well the argument survived the
     cross-check, not by how many personas raised it;
   - contested calls: where the lenses split, with each side's best argument (the user decides
     these);
   - what each lens saw that nobody else did;
   - what to keep.
5. **Optional second pass.** After the user revises, the same panel checks the new version, each
   persona only for the problems it raised.

## Rules

- Every persona file starts with the simulation notice; every claim carries a label.
- Quote the artifact sparingly (under 15 words); point to a section or line instead.
- Each problem says which experience it comes from (dossier §A, §B, §G or §I) and where that
  analogy may break. A problem with no basis in the persona's path is labeled `[inferred]`.
- Personas propose fixes; they do not rewrite the artifact. The user writes.
- Severity: **blocker** (the artifact fails its goal), **major** (a reader in the target
  audience would object), **minor** (polish).
- Interests are shown as dated facts and never used as a discount (`AGENTS.md`).

## Size and time

3–5 personas, two waves and a synthesis: about 10–30 minutes.

## Output

`workspace/runs/<YYYY-MM-DD>_review_<slug>/`: `brief.md`, `artifact.md`, `critiques/<ID>.md`,
`cross/<ID>.md`, `summary.md`.
