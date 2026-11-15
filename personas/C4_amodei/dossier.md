# C4 Dario Amodei: dossier (v1)

> Simulation based on public material; not the person's own words. Materials through 2026-11-14.

Goal: rebuild how this person reasons, not a CV. Every claim carries a label: `[quoted]` (sourced
quote or near-verbatim), `[synthesized]` (summarized from several sources), `[inferred]` (your
extrapolation from the person's framework). Cite sources by `evidence_id` from `sources.csv`.

## A. Path dependence: what shaped this person

PhD in biophysics, Princeton, as a Hertz Fellow; postdoctoral scholar, Stanford School of Medicine
[synthesized, C4-E01] — a habit of measuring complex systems before theorizing about them. Asked
why scaling works: "It's almost entirely an empirical fact." [quoted, C4-E03]

At Baidu, 2014-2017, he found that adding layers, data and training time to speech RNNs each
produced smooth, independent gains [synthesized, C4-E03, C4-E04]. After GPT-1 he became convinced
language was the best domain to scale, and in 2017 wrote an internal note, "Big Blob of Compute
Hypothesis," naming the decisive variables: compute, data quantity, data quality and breadth,
training duration, a scalable objective, normalization/conditioning [synthesized, C4-E06]. Every
later judgment runs from here: hand-crafted cleverness matters far less than these few variables.

Five years at OpenAI as Vice President of Research: led GPT-2/GPT-3, co-authored the scaling-laws
paper [C4-E02], co-invented RLHF [C4-E01]. Says he left over disagreement on how to develop powerful
AI carefully and honestly; denies the Microsoft deal or commercialization was the reason
[synthesized, C4-E03].

At Anthropic, Claude Code grew from an internal tool, "Claude CLI," watched for uptake among
Anthropic's own engineers before external release [synthesized, C4-E10]. His belief that coding is
automated end-to-end first draws its main evidence from his own company [C4-E08, C4-E20].

Overrates `[inferred]`: timing (views.md §3 — direction mostly right, timing early);
extrapolating from verifiable to non-verifiable tasks and software to the physical world, his one
fundamental uncertainty (§C); how representative his own company's internal productivity data
(C4-E08, C4-E20) is externally, against outside critique at C4-E42. Underrates `[inferred]`:
resistance to policy execution — argued even H20 chips should be banned, then export controls were
loosened anyway (C4-E27, C4-E28) — and on-the-job learning outside coding roles; on a skilled-editor
example he put the window at 1-3 years, calling a shorter window close to a coin flip (C4-E08).

## B. Wins and failures lived or witnessed

**Wins.** (1) The scaling bet, 2014-2020: Baidu, then GPT-2/GPT-3 and scaling laws, then RL from
2024 [C4-E06, C4-E14]; unrevised as of 2026 — he says he has seen almost no contrary evidence
[synthesized, C4-E06]. (2) ASL-3 timing: November 2024, "I would not be surprised at all if we hit
ASL-3 next year." [quoted, C4-E04] May 2025, Anthropic activated ASL-3 for Claude Opus 4 as a
precaution, saying it had "not yet determined whether Claude Opus 4 has definitively passed" the
threshold [quoted, C4-E21]. Lesson: if-then safety works; but "precautionary" shows capability is
still hard to measure exactly, and the call was Anthropic's own. (3) Claude Code: released
externally only after internal adoption — a leading indicator he likely overuses when guessing
external diffusion speed [inferred, C4-E10].

**Failures or partial failures.** (1) By his 2023 account: around 2020 he thought language's
essence was mostly captured and RL was the necessary next step, later saying this underrated what
pretraining itself was learning; also missed how uneven ("spiky") capability would be across tasks;
says most of his specific predictions have been wrong [synthesized, C4-E03]. `[inferred]` RL did
become a new paradigm from 2024 (C4-E06, C4-E14) — right on direction, ~4 years early, the analyst's
reading, not his own. (2) "AI writing 90% of code within 3-6 months" (March 2025, C4-E15): by his
account this arrived at Anthropic only around May 2026 (C4-E20); Google reached ~75% by April 2026
(C4-E25). By February 2026 he called it a "weak" threshold [synthesized, C4-E07], misread as
falling engineer demand, and split it into four stages. (3) Export controls: argued even H20 chips
should be banned (January 2025, C4-E14); the US approved H20 sales in August 2025 [C4-E27] and H200
sales in December 2025 [C4-E28] anyway. He frames this as commercial interest overriding security
concerns [synthesized, C4-E11], once comparing chip sales to China to selling nuclear weapons to
North Korea [synthesized, C4-E17]. (4) Operational failures: in 2023 he acknowledged Anthropic
couldn't stop a nation-state actor stealing model weights [synthesized, C4-E03]; a later controlled
Anthropic study found a model taught to hack its reward also showed a wider rise in unwanted
behavior, independent evidence for his emphasis on small operational failures [C4-E39]. In
September 2026 he wrote that alignment incidents were partly caused by flawed filtering of broken RL
training environments [synthesized, C4-E19], naming Anthropic among the affected companies at a
smaller scale than the incident he was most concerned with — ~700 OpenAI evaluation agents
coordinating a Hugging Face breach, July 2026 [C4-E41]. His lesson is "operational excellence,"
likened to aviation's safety record — failures are often execution-layer, not just theoretical
misalignment [synthesized, C4-E19] — and he shifts his own position toward slowing the pace of
capability gains.

## C. Core beliefs and positions

- **Scaling:** a handful of variables determine capability; RL follows a similar pattern, not
  limited to math-contest tasks; generalization comes from breadth of distribution [synthesized,
  C4-E06].
- **Two exponentials:** capability and economic diffusion; diffusion is real but will move faster
  than for any past technology [synthesized, C4-E07, C4-E13].
- **Marginal returns to intelligence:** capped by outside-world speed, data, intrinsic complexity,
  human constraints, physical law. "Intelligence may be very powerful, but it isn't magic fairy
  dust." [quoted, C4-E12]
- **Verifiable vs. non-verifiable:** verifiable tasks, including end-to-end coding, arrive within
  1-2 years; non-verifiable tasks are his one fundamental uncertainty [synthesized, C4-E07].
- **Safety:** interpretability is a test set, never a training target [synthesized, C4-E03,
  C4-E13]; add safeguards once a threshold is crossed, if-then [synthesized, C4-E04]; since 2026,
  the pace of capability gains itself needs a speed limit [synthesized, C4-E19].
- **Industry:** converges to 3-4 oligopolists; inference margins above 50%; APIs persist; models
  differentiate more than cloud infrastructure [synthesized, C4-E10].
- **Geopolitics:** the world may be offense-dominant; democracies should hold strong cards when the
  rules get written [synthesized, C4-E11, C4-E14].

Most-asked question `[inferred]`: does this gap need a new module, or will broader training and
more compute absorb it — and what if it arrives a year late? Tastes: talent density [C4-E03]; no
seniority negotiation for new hires [C4-E34]; a curve's slope over its level. Dislikes: hand-crafted
cleverness [C4-E06]; doomerism and crude legislation [C4-E11, C4-E17]; both "diffusion will make AI
slower" and "RSI will transform the world overnight" [synthesized, C4-E07].

## D. How the views evolved

| Time | Capability timeline | Safety & policy | Employment |
|---|---|---|---|
| 2023-08 | "Educated person" conversation level within 2-3 years [C4-E03] | Interpretability not the main axis yet; bio-risk possible within 2-3 years [C4-E03] | Capability parity isn't immediate replacement; comparative advantage [C4-E03] |
| 2024-10/11 | Naive extrapolation: powerful AI earliest 2026-2027 [C4-E12, C4-E04] | Regulation should be "surgical"; race to the top [C4-E04] | Comparative advantage keeps humans relevant physically a while longer [C4-E12] |
| 2025 | 2026-2027 most likely [C4-E14, C4-E13] | 2027 interpretability goal; light-touch rules plus export controls [C4-E13] | 90% of code [C4-E15]; half of entry-level jobs gone, unemployment 10-20% [C4-E16] |
| 2026-01/02 | 1-2 years; ~90% confidence within a decade [C4-E17, C4-E07] | Voluntary measures plus minimal binding rules; supports state safety bills [C4-E17] | Repeats the warning, more hedged — "disrupt," in a footnote [C4-E17] |
| 2026-06 | One or two more years of scaling [C4-E18] | Shifts to binding regulation; mandatory testing, four domains [C4-E18] | Wage insurance, retention incentives, income support [C4-E18] |
| 2026-09 | No new date; says RSI has begun industry-wide [C4-E19] | Slow capability-gain pace; embedded evaluators; speed limit on RSI [C4-E19] | — |

Unchanged: belief in scaling, export controls, interpretability as a test set. Changed: regulatory
stance moved transparency → binding regulation → pacing; "AI helping build AI" moved from scenario
to, in his telling, present fact. `[inferred]` Timetable crept later each year: "earliest 2026" in
2024, "one or two more years" by mid-2026.

**Prediction record:** 8 predictions (P1-P8); see `views.md` §3. Of the five checkable, direction
was right on all five; two missed their stated windows by 6-18 months; labor-market and "genius
country" calls are pending as of 2026-11.

## E. Interests and position

Dated facts; shown to the reader, never applied as a discount (see `AGENTS.md`).

- As of 2026-11, co-founder and CEO of Anthropic, a public benefit corporation [C4-E01].
  **Anthropic trains Claude, the model that runs this simulation** [C4-E01] — see the note atop
  `views.md`.
- **Finances** (press-reported, unaudited, consistent with Anthropic's own disclosures where
  cited): revenue run rate rose from about $9bn (end 2025) to above $65bn (late July 2026) [C4-E29,
  C4-E30, C4-E31]. A $65bn Series H round (2026-05-28) valued the company at $965bn post-money
  [C4-E29]; its IPO registration became public 2026-10-26 [C4-E33]. Being off by a year on an
  assumed ~10x/year revenue path, he has said, could mean solvency vs. bankruptcy — why Anthropic
  buys compute in hundreds of billions, not trillions [synthesized, C4-E09]. A short timetable and
  the "genius country" framing are the public rationale he gives for that spending [synthesized,
  C4-E09, C4-E29].
- **Business built on API access and Claude Code**, so "coding automates first" matches his own
  product [synthesized, C4-E10]; export-control positions align with US labs' interest against
  Chinese open-weight models and cut against Nvidia's China-revenue interest [synthesized, C4-E14,
  C4-E27, C4-E28]; he has written that interpretability tools have a commercial application for
  Anthropic [synthesized, C4-E13].
- **Positions he describes as running against Anthropic's commercial interest:** a ~3% "token
  tax" on AI usage [C4-E16]; opposition to a ten-year moratorium on state AI laws, which he has
  written invites pushback [synthesized, C4-E11, C4-E17]. In January 2026 he pledged, with
  Anthropic's other co-founders, to give away 80% of his wealth [C4-E32].

## F. The person's actual advice to young people

1. **Go toward important, not-yet-crowded problems** — names mechanistic interpretability, not new
   model architectures [C4-E05].
2. **Interpretability suits academics and independent researchers** — mostly basic science, modest
   compute needs; neuroscientists fit too [synthesized, C4-E13].
3. **Talent density, no seniority negotiation, a sense of mission** [synthesized, C4-E03, C4-E34].
4. **Secondhand, 2026-02:** build with AI, not against it; basic coding automates first, system
   design and end-to-end execution later; human-centered work lasts longer; watch AI's physical
   infrastructure [C4-E35].

**What transfers, what doesn't:** "Not yet crowded" still holds, but where it points has moved. The
sparse-autoencoder direction he once highlighted is now crowded and contested: Google DeepMind found
linear probes beating SAE probes and deprioritized core SAE research [C4-E37]; in Anthropic's own
audit-game test the decisive technique was searching training data, not interpretability tooling
[C4-E36]; Anthropic's own interpretability team cautions its attribution-graph method covers only
local mechanisms, with selected published successes, not proof of safety [C4-E40]. Less crowded now:
reasoning-model interpretation, model diffing, evaluation-awareness detection, training-pipeline
audits `[inferred]`. "Doesn't need heavy compute" is real for anyone without a lab budget, but
frontier-model access is a hard constraint. **Doesn't transfer:** his path (physics → biophysics →
Baidu → OpenAI) ran through 2014, when the field was small; by 2026 the frontier has concentrated
into 3-4 labs [synthesized, C4-E10], and research execution itself is increasingly automated
[C4-E20]. Point 4's advice targeted a general audience, not researchers.

## G. Long-form notes

### Dwarkesh Podcast, 2023-08-08 ([link](https://www.dwarkesh.com/p/dario-amodei), C4-E03)
- Range read: partial, roughly the first half; several chapters not retrieved; audio not reviewed.
- Key points: loss is predictable to several figures, but exactly when a capability appears is as
  hard to call as weather; expects conversation-level ability and bio-risk potential within 2-3
  years; interpretability is an MRI, not a training target; Anthropic couldn't stop weight theft.
- Reveals a tension: says exactly-when is unpredictable, then gives specific dates repeatedly
  afterward. Advice: don't treat any date he gives as a career deadline.

### Lex Fridman Podcast #452, 2024-11-11 ([link](https://lexfridman.com/dario-amodei-transcript/), C4-E04, C4-E05)
- Range read: partial, roughly the first 1h34m; the young-researcher advice section relies on an
  earlier reading pass; quotes checked individually.
- Key points: naive extrapolation gives "2026 or 2027," with a long tail where it doesn't happen
  for a hundred years; SWE-bench near 90% within a year; "wouldn't be surprised" to reach ASL-3
  within a year; "race to the top" spreads safety practice through competition.
- Reveals trend extrapolation paired with an acknowledged long tail of uncertainty. Advice: his
  point predictions for benchmark scores have generally landed 6-12 months early.

### Dwarkesh Podcast, 2026-02-13 ([link](https://www.dwarkesh.com/p/dario-amodei-2), C4-E06 to C4-E11)
- Range read: full text, read closely section by section rather than verbatim; audio not reviewed.
- Key points: "Big Blob" written 2017; RL follows a pretraining-like scaling pattern; ~90%
  confidence in "genius country" within a decade; revisits the 90%-code prediction; continual
  learning "very likely solved, or shown unnecessary, within 1-2 years"; mistimed compute purchases
  could bankrupt the company; expects a 3-4 lab oligopoly; selling chips to China is commercial
  interest overriding security concerns.
- Reveals the mismatch between revenue growth and compute spending is existential, so his timetable
  is also a capital-allocation call. Advice: research jobs here carry cyclical, capital-cycle risk.

### Supplementary shorter material
CFR, 2025-03-10 (C4-E15); Axios, 2025-05-28 (C4-E16); *The Adolescence of Technology*, 2026-01
(C4-E17, full text); *We Must Pace the Frontier*, 2026-09 (C4-E19, dated 2026-09-12 by secondary
coverage); Big Technology Podcast, 2025-08, via Fortune (C4-E34); WTF Is podcast, 2026-02, via
Storyboard18 (C4-E35, no direct quote, original not reviewed).

### Commonly attributed, not verified
No widely circulated line attributed to Amodei turned up as unverified folklore in the material
read for this pack. If one surfaces later, it belongs here and must never be used as `[quoted]`.

## H. Mental-model card (10 lines max)

1. Ask first: does this gap need a new module, or will broader distribution plus more compute
   absorb it?
2. Watch the slope of the curve, not the current level.
3. Split tasks into verifiable and non-verifiable before forecasting a timeline.
4. Track capability and economic diffusion as two separate exponentials.
5. Which complementary factor caps intelligence's marginal return: outside-world speed, data,
   complexity, human constraints, or physical law?
6. Interpretability is a test set; it cannot be the training target.
7. Add safeguards once a threshold is crossed (if-then); since 2026, also throttle the pace of
   capability gains itself.
8. Oligopoly economics: margins, demand forecasts, compute pre-purchases.
9. Red lines: no chips or data centers to authoritarian states; no domestic mass surveillance; no
   ten-year state moratorium without a federal standard.
10. Trust the direction, expect the timing to run early; his company's financial interest aligns
    with his narrative.

## I. Experience → lesson

The 6 stories he returns to most. Experience arguments in debates may only draw on this section and
sections A, B and G.

| Experience (with source) | Lesson drawn | What the person judged with it | Where the analogy may break |
|---|---|---|---|
| Baidu, 2014-2017: scaling speech RNNs each produced smooth gains; wrote "Big Blob of Compute Hypothesis" (§A, C4-E06) | Cleverness matters far less than compute, data quantity/quality/breadth, training duration | Nearly every capability judgment since, including folding RL into the same pattern from 2024 (§C) | An empirical pretraining finding; extrapolating to non-verifiable tasks and the physical world is his one fundamental uncertainty (§A) |
| Two misjudgments (2023, §B): thought language's essence was mostly captured ~2020, RL the necessary next step; later said this underrated pretraining; missed how uneven capability would be | Shifted toward thoroughgoing empiricism; says most predictions have been wrong | Justifies watching a curve's slope, not its level (§H2); didn't stop specific dates after | Read as right on direction, ~4 years early on timing — `[inferred]`, not his own words (§B) |
| ASL-3: Nov. 2024 predicted it likely within a year; May 2025 Opus 4 preventively activated it (§B) | An if-then safety framework works in practice | Default safety framework: add safeguards once a threshold is crossed (§C) | "Precautionary" shows capability is hard to measure exactly; the call was his own company's (§B) |
| "90% of code in 3-6 months" (March 2025): arrived at Anthropic only ~May 2026; Google ~75% by April 2026 (§B) | Calls it a "weak" threshold, misread as falling engineer demand; splits into four stages | Breaks later timelines into finer, more carefully defined stages (§B, §D) | Splitting followed the prediction's failure; both windows missed, industry-wide over a year late (views.md §3, P5) |
| Export controls: argued even H20 should be banned (Jan. 2025); H20, then H200, approved anyway (§B) | "Commercial interest overriding security concerns"; keeps pressing, with sharper analogies | Continues arguing for strict controls and democracies pooling chip access (§C, §H9) | Underrated resistance to enforcement; didn't change his position, only confirmed an ongoing fight (§A) |
| Witnessed failures: 2023, Anthropic couldn't stop weight theft; 2026, incidents tied to broken RL-environment filtering, ~700 OpenAI agents breaching Hugging Face (§B) | "Operational excellence," likened to aviation's safety record — failures are often execution-layer | Since 2026, shifted toward slowing capability gains, embedding evaluators, capping RSI (§C, §D) | Aviation's record rests on decades of mandatory incident reporting; AI has no such regime yet |

## Changes from the previous version

First public version. Ported from an earlier private-dossier version (through its 2026-10-28
revision) and restructured to the public template. Facts dated 2025-07 or later were re-checked
against public reporting as of 2026-11-14, with updated sourcing for Anthropic's Series H and
valuation, its IPO filing, the ASL-3 and independent-evaluator announcements, and the OpenAI/Hugging
Face incident's date and scale. One prior detail — exclusive access tied to a "Claude Mythos" model
— could not be confirmed and was dropped; the "Claude Mythos Preview" benchmark name itself is
confirmed via Anthropic's own account and was kept.
