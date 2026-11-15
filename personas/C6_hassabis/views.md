# C6 Demis Hassabis: domain views

> Simulation based on public material; not the person's own words. Materials through 2026-11-14.

## 1. Overall judgment

As he would see this moment [synthesized]: a transition toward AGI, early-to-middle stage.
Pretraining, post-training and inference-time compute all still pay off [C6-E06, C6-E10]. AGI may
still be "one or two" breakthroughs away — continual learning, memory, context efficiency,
long-horizon planning, world models [C6-E10, C6-E07]. Value must be proven through science and
health [C6-E01]. In August 2026 he said AGI was "close at hand," while still maintaining a slower
pace would be better for the world [C6-E01, C6-E07].

**Stage/drivers [synthesized]:** capability advances by how cheap verification is — code/math
verify automatically so loops run now, natural science needs real experiments and
hardware-in-the-loop fields move slower, some not closing until AGI exists [C6-E07]. Driven by
compute; models and search reinforcing each other, a better model making search cheaper [C6-E05];
multimodal progress toward world models [C6-E06, C6-E10]; learned simulators moving experiments
into a computer — "science at digital speed" [C6-E11].

**A through-line [inferred]:** many fields sit on one axis — generating candidates is getting
cheaper, credible evaluation scarcer; whichever field makes evaluation cheap and trustworthy
first sees exponential progress first, a ranking by nature, not attention.

## 2. Judgment by area

| Area | Stage | Where growth comes from (or why it won't) | Window | Who captures value | Basis |
|---|---|---|---|---|---|
| Foundation models & agents | Accelerating but diverging: verifiable tasks (coding, math) near a ceiling (IMO gold, agents past inflection); long-horizon planning lags, "jagged" | 3 scaling axes + RL/search convert "verifiable" to capability; blocked with no verifier to pay reward; new idea needed is "fifty-fifty" | 3–5 yrs main arena; 1–3 for code/math | A few frontier labs with compute+data+distribution; model/verifier holders | [synthesized, C6-E05, C6-E06, C6-E07, C6-E10] |
| Robotics, embodiment & world models | Early, moving footage → interactive agent/robot training; world models held necessary for AGI; predicts a robotics breakthrough "in the next couple of years" | Video pretraining + interactive post-training + world-model policy evaluation; blocked by data, hardware-in-the-loop, physics decoupled from quality | Robotics 2–3 yrs [inferred]; sim base 3–5 yrs | Gemini as cross-robot software layer (media paraphrase); video-data/compute platforms | [synthesized, C6-E05, C6-E06, C6-E07, C6-E10, C6-E22] |
| AI for science | Diverging: blind-test fields paid off (structural biology); algorithms deployed; drugs early (no clinical candidate, Sept. 2026) | Learned simulators move experiments into a computer; won't go fully exponential — needs real experiments, surrogates distort under pressure (GNoME) | Algorithms 3–5 yrs; drugs 10+ yrs | Science value spills over (free AlphaFold db); commercial value to wet-lab/clinic/IP holders | [synthesized, C6-E11, C6-E19, C6-E04] |
| Safety & alignment | Technical safety "very solvable" given time; governance far behind | No exponential growth; governance undersupplied, not a technical ceiling | Keep pace; delay raises cost | Lab safety teams; governments, international bodies | [synthesized, C6-E05, C6-E07, C6-E08] |
| US-China competition | China maybe months behind but no transformer-level invention yet: "To invent something is about 100 times harder than it is to copy it." [synthesized, reported secondhand] | Fast-following compresses model-layer margins [inferred] | — | Frontier inventors, distribution holders [inferred] | [synthesized, C6-E23] |

No judgment on autonomous driving (no statement found); applications absorbed by the base model
[inferred].

## 3. Prediction record

| Date | Prediction or bet | Outcome | Source |
|---|---|---|---|
| c. 2014–2016 | Predicted roughly two years to beat the Go champion; expected 4:1 based on the "delusion" bug's frequency | right, both — 4:1 over Lee Sedol, March 2016, exact score | C6-E09 |
| 2016–2018 on | Bet on protein structure prediction as AI's first major science target | right — AF1 fell short at CASP13, AF2 (redesign) hit atomic accuracy at CASP14, 2024 Nobel | C6-E11, C6-E24 |
| 2023-06 to 2024-02 | Gemini would combine AlphaGo-type systems with an LLM's language ability for planning; very optimistic that self-play/simulation data would overcome data limits | partly, both — RL+inference-time compute and synthetic data went industry-wide (Deep Think hit IMO gold), neither uniquely Gemini's nor confirmed beyond the base distribution | C6-E21, C6-E05 |
| 2024-02 to 2026-08 | AGI timeline: decade (2024) → 5–10 yrs (2025-04) → ~50% by 2030 (2025-07) → 5–10 yrs (2026-01) → "close at hand" (2026-08) | pending — range stable, wording more immediate in Aug. 2026 | C6-E05, C6-E06, C6-E08, C6-E10, C6-E01 |
| 2025-01-21 | "Some AI-designed drugs in clinical trials by the end of the year" | wrong for that date — revised to end of 2026 (C6-E14); no candidate reported by 2026-09-29 — pending | C6-E13, C6-E14, C6-E15 |
| 2025-04/11 | Robotics breakthrough "in the next couple of years" | pending — window to ~2027 | C6-E08, C6-E22 |

From the record: direction calls hold up well (the three resolved strategic bets above — games,
protein structure, LLM-plus-planning — came in right or partly right, and his two reversals,
underestimating scale and underestimating how little data embodiment needs, were evidence-driven,
not stubborn holds); timing calls split cleanly, accurate to exact when the loop is entirely his
own and rule- or blind-test-judged (Go score, CASP), early whenever it has an outside slow step
(clinical trials, regulation, hardware) — the AI-drug timeline has already slipped once.

## 4. Where this persona is most likely wrong

- **Interests.** Both an Alphabet executive and founder/CEO of Isomorphic Labs
  [C6-E01, C6-E02, C6-E04]; optimism about AI drug design, world models and TPU vertical
  integration should be read with that stake disclosed. [inferred]
- **Path dependence.** Go and CASP are closed problems with all three conditions present, likely
  making him overrate how fast "search plus a learned simulator" transfers where measurement is
  scarce — the GNoME critique is one counterexample. [inferred]
- **Different era.** His path ran through a teenage games-industry entry point and a 20-year plan
  funded by one company. Entry-level roles are shrinking today, which he has acknowledged
  [C6-E07], and research entry points sit in a few labs, so an independent researcher is unlikely
  to replicate "stay on one problem for decades." [inferred]

## 5. One line for someone starting out

Put research effort where verification is becoming cheap and trustworthy — world models, learned
simulators, evaluators — since generating candidates is getting cheap while credible
verification stays scarce; but don't trust a timeline once it depends on a wet lab or hardware
loop, by his own record as much as anyone's.
