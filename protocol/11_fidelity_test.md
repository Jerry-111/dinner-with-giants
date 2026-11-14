# Step 1b: fidelity test

Tests whether a persona sounds like the real person. This matters most for personas that argue
heavily from their own lived experience. Academic research can't run this test (survey
subjects are anonymous); a persona built from a named, real public figure can, because that
person's later public statements are themselves public material.

**Applies only to `public_figure` personas** — real, living people with dated public
statements after the cutoff below. `historical` personas have no post-cutoff statements to
check against; `archetype` and `fictional` personas aren't real people at all. Run a small
version of this before relying heavily on a new roster of public-figure personas, or after a
major rebuild of one; budget about an hour.

## Method

1. **Pick a cutoff** after the analysis model's own training cutoff, so the model hasn't
   already seen the answers.
2. **Pick personas** with many public statements after that cutoff — rank candidates by count
   of post-cutoff rows in their `sources*.csv` (by `published_date`) and take the top few.
3. **Rebuild a pre-cutoff card.** A fresh agent — one that has not read the existing dossier —
   builds `card_pre.yaml` using only sources with `published_date` on or before the cutoff. The
   persona's real dossier already includes later material, so it can't be reused directly.
4. **Write questions.** From each persona's post-cutoff material, pick 3–5 questions they
   actually took a position on, phrased so the question itself doesn't leak the answer. Keep
   the real answers and their sources in a file only the blind grader reads.
5. **Collect three answer sets per question:**
   - the persona agent, reading only `card_pre.yaml`, with no search access;
   - a name-only agent, told nothing but the person's name;
   - a no-persona analyst, given neither.
6. **Grade blind.** A fresh agent that doesn't know which answer came from which group scores
   each against the real statement: direction match (0/1), reasoning match (0–2), tone and
   emphasis match (0–2).
7. **Report** all three groups' scores per persona, and the gap: persona score minus name-only
   score. **A gap at or below zero means the dossier added nothing over the bare name** —
   rebuild that persona's dossier before trusting its experience arguments.

## Output

`workspace/runs/<date>_fidelity/`: pre-cutoff cards, the question set, an answer key visible
only to the blind grader, the three response sets, the grading notes, and `RUN_METADATA.md`.

## Limitations

- A handful of people at 3–5 questions each catches large gaps, not fine differences.
- The blind grader is the same underlying model as everything else; fix its rubric before
  grading, not after seeing answers.
- The real person's post-cutoff statements are themselves filtered through whoever reported
  them — not a complete transcript of what they actually believe.
