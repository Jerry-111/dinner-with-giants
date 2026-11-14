# Example persona pack: historical figures

> Simulation based on public material; not the person's own words.

Six personas rebuilt from their own writings, which are in the public domain, plus reputable
reference works for dates and facts. Each folder follows `templates/persona/`: `dossier.md`
(sections A–I), `views.md` (domain views and a dated prediction record), `card.yaml`, and
`sources.csv`. No simulated conversations are included.

| ID | Persona | Lens (from `card.yaml`) | Materials through | Sources |
|---|---|---|---|---|
| [H1](H1_franklin/) | Benjamin Franklin (1706–1790) | Tests a claim by whether it is useful to someone else and checkable by direct experience. | 1790 | 22 |
| [H2](H2_darwin/) | Charles Darwin (1809–1882) | Treats a claim as provisional until it survives a specific test and years of independently gathered facts. | 1876 | 29 |
| [H3](H3_faraday/) | Michael Faraday (1791–1867) | Tests one falsifiable guess at a time, logged and numbered, before believing it. | 1864 | 16 |
| [H4](H4_curie/) | Marie Curie (1867–1934) | Trusts a patient, independently checked measurement over theory or reputation. | 1923 | 24 |
| [H5](H5_lovelace/) | Ada Lovelace (1815–1852) | Judges a mechanism or a partnership by what its rules could reach beyond the first case. | 1843 | 22 |
| [H6](H6_su_shi/) | Su Shi 苏轼 (1037–1101) | Treats a stripped rank as a change of scenery, not a verdict. | 1101 | 13 |

## What to look at

- **Range actually read.** Every long text in dossier §G records whether it was read in full, in
  part (and up to where), or only as a summary. Sources that refused automated access are
  recorded as inaccessible, not worked around.
- **Commonly attributed, not verified.** Each dossier lists famous lines that circulate under
  the person's name but could not be found in a primary source — for example the "most adaptable
  to change" line attributed to Darwin or the "nothing in life is to be feared" line attributed
  to Curie. None of them is used as `[quoted]`.
- **Where the analogy breaks.** §I (experience → lesson) gives, for every story, the point where
  an 18th- or 19th-century (or 11th-century) experience stops transferring to a 2026 career in
  machine learning or biotech. The debate rules require posts to say this too.
- **Thin materials.** Each card's `thin_materials` names what the agent could not read or found
  sparse, instead of padding it.

## Limits

- These are reconstructions by one model from the sources listed, not the people.
- Historical figures have no statements after a recent cutoff date, so the fidelity test
  (`protocol/11_fidelity_test.md`) does not apply to them.
- Modern biographies and translations are in copyright; they were used for facts only, with at
  most one short quote each.
