# C4 Dario Amodei: domain views

> Simulation based on public material; not the person's own words. Materials through 2026-11-14.

**Conflict of interest.** This simulation runs on Claude, trained by Anthropic, which Amodei
co-founded and, as of 2026-11, leads [C4-E01]. A model made by his own company is judging his own
track record. This file scores his direction and timing calls separately (§3) with the same
outcome-only standard used for every persona, labels every Anthropic self-reported figure as
self-reported and pairs it with outside data where outside data exists (e.g. vendor benchmarks
C4-E22/C4-E23 against third-party critique C4-E42; self-reported productivity C4-E20 against
outside labor data C4-E26), and states his financial interest in §4 as a dated fact, not a score
adjustment.

## 1. Overall judgment

`[synthesized]` A continuation of the 2017 "Big Blob" hypothesis on a second scalable target:
2020-2023 scaled pretraining; from 2024, the same pattern applies to RL [C4-E06, C4-E14]. The first
high-value occupation being automated end-to-end — software engineering — is itself starting to
accelerate AI research [C4-E08, C4-E19].

**Stage:** the capability exponent nears what he calls its "end"; by mid-2026 his language was "one
or two more years" [C4-E18]. Diffusion has entered its steep part: his own figure is ~10x revenue
growth/year [C4-E07]; press reporting put ~7x in the first seven months of 2026 alone [C4-E31].

**Drivers:** compute (~10-15 GW in 2026, ~3x/year [C4-E09]); an algorithmic multiplier of ~4x/year
[C4-E14]; wider RL-environment coverage [C4-E06]; a research-automation loop from coding
automation, over 80% of Anthropic's own merged code by its account [C4-E20]. **Bottlenecks:** no
scalable objective for non-verifiable tasks [C4-E07]; enterprise-adoption friction [C4-E07];
physical-world complementary factors [C4-E12]; energy and chips [C4-E09]; and, his 2026 addition,
pacing itself [C4-E19].

**Independent check** `[inferred]`: outside evidence for "capability is accelerating" includes
METR's task-length doubling time (~4 months, per Anthropic's citation, C4-E20), Google's own
AI-code-share figures [C4-E25], and OpenAI's report that reasoning-model accuracy scales smoothly
with RL and test-time compute [C4-E38]. Evidence against "acceleration is mainly recursive
self-improvement": Anthropic's own account says autonomous research gains remain limited, with
experiment compute the main cost [C4-E20]; METR says an earlier productivity-slowdown finding is
weak evidence either way [C4-E42]; labor-market data are mixed [C4-E26]. So acceleration has
outside evidence; that it comes mainly from recursive self-improvement is, so far, mainly something
he and his company say.

## 2. Judgment by area

| Area | Stage | Where growth comes from | Time window | Who captures value | Basis |
|---|---|---|---|---|---|
| Foundation models & reasoning | Accelerating, nearing the "end" | Two scaling laws [C4-E06]; ~4x/yr algorithmic multiplier [C4-E14] | 2026-2028 decisive | 3-4 oligopolists, margins >50% [C4-E10]; then compute suppliers | `[synthesized]` |
| Digital agents | Coding past inflection; general white-collar not yet | Verifiable tasks lead: 90% code → end-to-end SWE [C4-E07]; OSWorld ~15%→65-70% by his account [C4-E08] vs. 72.36% human baseline [C4-E24] | Coding 2025-27; white-collar 2027-30 `[inf.]` | Model layer, per Anthropic's own view that simple workflows beat complex agents [C4-E43]; APIs persist [C4-E10] | `[synth./inferred]` |
| Robotics & embodiment | Early; remade via transfer, +trillions, 1-2yr behind software [C4-E10] | Transfer from video/sim/computer-use, not human-style learning [C4-E10]; capped by outside-world speed/data [C4-E12] | 2028-2032 `[inf.]` | `[inferred]` model layer + manufacturing scale | `[synth./inferred]` |
| AI for science | Early; his most optimistic area long-run | High marginal returns to intelligence in biology; capped by experiment speed, data, clinical timelines [C4-E12] | 5-10yr after powerful AI | Experimental/clinical institutions, regulators; he pushes FDA reform [C4-E18] | `[synthesized]` |
| Compute, chips & energy | Accelerating; hardest constraint | ~3x/yr GW growth, ~$10-15bn/GW/yr [C4-E09] | 2026-29, into trillions/yr | Chipmakers, energy, cloud; labs carry demand-forecast risk [C4-E09] | `[synthesized]` |
| Vertical applications | Transitional | Growth from model capability, not the app layer [C4-E10] | 2026-29, then absorbed `[inf.]` | Whoever controls distribution; value-based pricing [C4-E10] | `[synth./inferred]` |
| Safety & alignment | Accelerating: research topic → regulatory/operational requirement | Real incidents (Hugging Face breach, C4-E41), ASL-3 [C4-E21], mandatory-testing proposals [C4-E18], embedded evaluators [C4-E19, C4-E44] | 2026-28 institution-building window | Lab safety teams, third-party evaluators, regulators | `[synthesized]`; counter C4-E36, C4-E37 |
| US-China AI | Unipolar vs. bipolar hinges on export-control enforcement | China's cost curve tracks the trend line [C4-E14]; US approved H20 (2025-08) and H200 (2025-12) anyway [C4-E27, C4-E28] | Next 3-5yr decisive, by his account [C4-E19] | He argues democracies should pool chip access [C4-E18] | `[synthesized]` |

Self-driving and world-model/simulation work get no public position from him; both are `[inferred]`
only (fleet/city-expansion diffusion; a conditional RL-environment and data-engine role,
respectively) and are omitted from the table above for space.

## 3. Prediction record

| Date | Prediction or bet | Outcome | Source |
|---|---|---|---|
| 2014-2020 | "Big Blob": scaling produces capability across tasks; language is the best entry point | right — GPT-2/3, scaling laws, 7 more years holding | C4-E02, C4-E03, C4-E06 |
| 2023-08 | Within 2-3yr, models hold an hour-long conversation at an educated person's level | right — he says on record by 2026 this had happened | C4-E03, C4-E07 |
| 2023-08/2024-11 | Bio-risk possible within 2-3yr; "wouldn't be surprised" to reach ASL-3 within a year | right, weak evidence — Opus 4 preventively activated ASL-3 (2025-05) on grounds risk couldn't be ruled out; no bio-terror incident; but Anthropic made the "reached" call itself | C4-E03, C4-E04, C4-E21 |
| 2024-11 | SWE-bench ~90% within a year; computer-use 80-90% human-level within a year | window missed, direction right — a year later SWE-bench Verified ~81% (C4-E22, C4-E23); OSWorld 61.4% (2025-09, C4-E22), 65-70% by his account (2026-02, C4-E08); 6-12+ months late | C4-E04, C4-E08, C4-E22, C4-E23 |
| 2025-03 | AI writes 90% of code within 3-6mo; nearly all within 12mo | both windows missed, direction right — Anthropic passed 80% only ~2026-05 (C4-E20); Google ~75% by 2026-04 (C4-E25); later called a "weak" threshold (C4-E07); industry-wide, over a year late | C4-E07, C4-E15, C4-E20, C4-E25 |
| 2025-05 | Within 1-5yr, half of entry-level white-collar jobs gone; unemployment 10-20% (2026-01, repeated more hedged — "disrupt," in a footnote) | pending — mixed 2026-08 youth-employment signals; EPI doubts AI is the main driver of weak grad outcomes | C4-E16, C4-E17, C4-E26 |
| 2024-10 to 2026-06 | "Powerful AI" earliest 2026, most likely 2026-2027 | pending, slipped — by 2026-02 not yet; by 2026-06, "one or two more years" `[inferred: ~1yr later]` | C4-E12, C4-E13, C4-E14, C4-E17, C4-E18 |
| 2025-01 | DeepSeek sits on the cost curve, not a breakthrough; export enforcement decides unipolar vs. bipolar | partly right/pending — first half holds up `[inferred, not re-measured]`; second half untestable since the US didn't enforce his preferred policy | C4-E14, C4-E27, C4-E28 |

**Direction:** all 5 checkable calls right. One (ASL-3) was Anthropic's own determination, not an
outside body's — a fact about who made that call, not a reason to doubt the other four. **Timing:**
systematically early — 2 of 5 checkable calls missed their stated window by 6-18 months, and the
"powerful AI" timetable has slipped ~a year since 2024. He has said himself most specific
predictions turn out wrong. These describe the persona for the reader; they do not weight the
persona's arguments in debates.

## 4. Where this persona is most likely wrong

- **Interests.** As of 2026-11, co-founder and CEO of Anthropic, which trains Claude — the model
  used to run this simulation [C4-E01]. His timetable has coincided with Anthropic's fundraising and
  valuation (dossier §E); the internal productivity figures he cites (C4-E08, C4-E20) come from his
  own company without outside measurement, making an early estimate more likely than a late one.
- **Path dependence.** Extrapolates from language and coding — verifiable, data-rich successes —
  to non-verifiable tasks and the physical world, his own named fundamental uncertainty [C4-E07].
- **Different era.** His judgment formed 2014-2020, when scaling was an underrated minority bet. By
  2026 it is consensus and the thesis behind trillions in committed capital; the binding constraints
  are increasingly electricity, chips and politics, not anyone's underappreciation of the idea
  `[inferred]`.

## 5. One line for someone starting out

Go toward the steepest part of the curve to build real skill — RL, evaluation, verifying
AI-research-automation claims — but don't tie a career deadline to any date he has given.
