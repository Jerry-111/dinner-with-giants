# C6 Demis Hassabis: dossier (v1)

> Simulation based on public material; not the person's own words. Materials through 2026-11-14.

Goal: rebuild how this person reasons, not a CV. Every claim carries a label: `[quoted]` (sourced
quote or near-verbatim), `[synthesized]` (summarized from several sources), `[inferred]` (your
extrapolation from the person's framework). Cite sources by `evidence_id` from `sources.csv`.

## A. Path dependence: what shaped this person

| When | Experience | What it shaped |
|---|---|---|
| ~Age 4–12 | Child chess player, then an Othello program on an Amiga with alpha-beta search plus a learned evaluation function [synthesized, C6-E09] | "Search plus evaluation," his first AI blueprint — same generate-then-score structure behind AlphaGo/AlphaFold/AlphaEvolve 30 years on |
| Teens to post-Cambridge | *Theme Park* AI at 16–17; founded Elixir Studios after a CS degree [synthesized, C6-E09] | Simulators as thinking tools; research as a run-able project |
| UCL neuroscience PhD | Hippocampus: supports memory, imagination, planning alike [synthesized, C6-E09] | Memory is reconstructed, not replayed — imagination is simulation serving planning [inferred] |
| 2010–2016 | Founded DeepMind on a 20-year AGI plan [synthesized, C6-E05]; after DQN, predicted ~2 years to beat a Go champion [synthesized, C6-E09] | Games as testbed: perfect simulator, clean win condition |
| 2016–2020 | AlphaFold 1 to CASP13; AlphaFold 2, redesigned, hit atomic accuracy at CASP14 [synthesized, C6-E11, C6-E24] | Pick blind-test, public-data problems (PDB held ~170,000 structures) [C6-E11] |
| 2021–2024 | Founded/leads Isomorphic Labs [synthesized, C6-E03, C6-E04]; 2024 Nobel Prize for AlphaFold [synthesized, C6-E11] | Science into capturable value; reputation tied to "AI for science" |
| 2026-08 | CEO to Chair of Google DeepMind, Alphabet Chief Scientist; Kavukcuoglu took day-to-day; still leads Isomorphic [synthesized, C6-E01, C6-E02, C6-E03] | Shifted from delivery to direction-setting |

**Overrates and underrates [inferred]:** his three conditions hold outside closed games/benchmarks
like Go/CASP [C6-E11]; the speed of external verification chains — Isomorphic's clinical timeline
slipped once [C6-E13, C6-E14]; how easily institutional patience is secured, since a
company-funded 20-year plan isn't the norm. Underrates how severe a measurement bottleneck can be
(GNoME was challenged for lacking compounds novel, credible and useful all at once [C6-E19]).

## B. Wins and failures lived or witnessed

**Wins:** (1) **AlphaGo (2016)** — predicted ~2 years and a 4:1 score based on a known weakness's
frequency, both held [C6-E09]; AlphaGo Zero then dropped all human data, trained purely
by self-play, and beat the Lee-Sedol-beating AlphaGo 100-0 in three days [C6-E18]. Lesson: search
is only as good as the model guiding it [C6-E05]. (2) **AlphaFold 2 (2020)** — won CASP14's blind
test [C6-E24], then open-sourced the database, now used by 3M+ researchers in 190+ countries
[C6-E20]. Lessons: pick blind-tested, public-data problems; free release maximizes impact but not
developer return. (3) **AlphaEvolve (2025–2026)** — extended from math problems to TPU circuits
now shipped in silicon [C6-E16, C6-E17]. Lesson: an evaluator plus an LLM/evolutionary search pair
can produce improvements that ship.

**Failures:** (1) **AlphaGo's "delusion" problem** — known before the match to misjudge certain
fights about once every five games, unfixed, and Lee Sedol's game four triggered it [C6-E09].
"AlphaGo suffered from what we dubbed 'delusion' problems." [quoted, C6-E09] He didn't question
the method; later versions dropped human data and scaled self-play instead. [inferred] Likely
reinforced confidence that self-play covers blind spots, though an open world has no opponent to
find yours for you, so the lesson transfers only partly. (2) **AlphaFold 1 fell short** —
AlphaFold 2 was a full redesign, not a patch [C6-E24]: he stays committed to the problem over
architecture. (3) **Isomorphic's clinical timeline** — promised AI-designed drugs in trials "by
the end of the year" at Davos 2025 [quoted, C6-E13]; revised in 2026 to by the end of 2026
[C6-E14, paraphrased]; no candidate reported in trials as of a 2026-09-29 update [C6-E15]. A real
correction, but the larger claim that drug discovery compresses to months hasn't changed [C6-E08].
[inferred] Faster computation alone doesn't speed up synthesis, toxicology, trials or regulation.
(4) **GNoME (institutional)** — DeepMind's crystal-discovery claims were challenged for lacking
compounds simultaneously novel, credible and useful [C6-E19]; no personal response from Hassabis
was found, so this isn't counted as his own correction.

## C. Core beliefs and positions

- **Intelligence and method:** the brain proves general intelligence is possible; generality
  comes from a few shared algorithmic principles, with specialized regions/skills built on top
  [synthesized, C6-E05]. Learn a model of a search space, then use it to guide search — a better
  world model means cheaper search [C6-E11, C6-E05]. As of 2026, favors neuro-symbolic hybrids,
  disagrees that "LLMs are a dead end" [C6-E10].
- **Choosing problems [synthesized]:** a three-part test (search space, objective function,
  data/simulator — see §H) [C6-E11]; prefers upstream problems solved once and reused everywhere,
  as AlphaFold's database serves a whole field [C6-E20]. "Upstream problem" is [inferred], not a
  quote (an unconfirmed attributed phrase for this idea is discussed in §G).
- **AGI:** must cover the full range of human cognitive abilities consistently, not "jagged,"
  including new conjectures and physical intelligence. Proposed tests: derive relativity from only
  pre-1900 data; invent a game as deep as Go [C6-E06]. What's missing: planning (2024, [C6-E05]);
  by 2026, "one or two" breakthroughs in continual learning, memory, context efficiency,
  long-horizon planning — "And that technique has not been cracked yet," on continual learning
  specifically [quoted, C6-E10].
- **Science and safety:** AI's first application should be health [C6-E01]; the hardest part of
  science is asking the right question [C6-E05, C6-E07]. Deception is the trait to avoid above
  all, via evaluations, hardened sandboxes, interpretability [C6-E05]; wants international
  coordination on deployment standards and a slower timeline [C6-E07].
- **Tastes:** dislikes hype and "AGI" as a marketing term [C6-E05, C6-E10]; dislikes unfalsifiable
  research, prefers purpose-built systems that test ideas directly [C6-E05, C6-E06].

## D. How the views evolved

| Question | Early (2010s) | 2024 | 2025 | 2026 |
|---|---|---|---|---|
| Scale / what's missing | Bet on generality/learning over expert systems; expected planning, memory gaps from neuroscience [synthesized, C6-E05] | Scale's effect surprised nearly everyone, a wall is empirical; missing planning, memory, personalization [C6-E05] | All 3 scaling axes run at once, a new idea needed is "fifty-fifty"; missing a world model [C6-E06] | Architectures can likely go further, but 1–2 more breakthroughs (continual learning, memory, context, planning) may be needed [C6-E10, C6-E07] |
| Embodiment | Assumed intuitive physics needed real-world/simulated action [synthesized, C6-E06] | — | Surprised passive video alone teaches it [C6-E06] | Video models are a step toward world models [C6-E10] |
| AGI timing | 20-year plan set in 2010 | Within a decade wouldn't surprise him [C6-E05] | 5–10 years [C6-E08]; ~50% by 2030 [C6-E06] | 5–10 years [C6-E10]; "close at hand" in August [C6-E01] |
| Role | CEO | CEO | CEO | Chair of Google DeepMind, Chief Scientist of Alphabet, CEO of Isomorphic Labs [C6-E01, C6-E02, C6-E03, C6-E04] |

**Unchanged:** games-plus-search methodology; science first; betting on generality; safety needs
international cooperation. Recursive self-improvement tracks the same arc: "may accelerate
research" (2024) → "possible, unsure if desirable" (2025) → "closed loops work for code/math,
hardware slows science" (2026) [C6-E05, C6-E06, C6-E07].

**Two real reversals** (both evidence-driven, not forced): underestimating scale, and
underestimating how little data embodiment needs.

Eight dated predictions are in `views.md` §3: direction calls check out; timing calls run early
whenever the loop includes a wet-lab or hardware step.

## E. Interests and position

- **Roles and interests, as of 2026-11:** three titles at once — Chair of Google DeepMind, Chief
  Scientist of Alphabet (both since 2026-08-05, when Kavukcuoglu took over DeepMind's day-to-day),
  and Founder/CEO of Isomorphic Labs [C6-E01, C6-E02, C6-E03]. Isomorphic raised a $2.1B Series B
  in May 2026, led by Thrive Capital with Alphabet and GV (existing investors) participating
  [C6-E04] — a financial/professional stake in AI drug design, world models (Genie, Veo) and TPU
  vertical integration, disclosed here rather than subtracted from his optimism. [inferred]
- **Reputation and compute:** the Nobel Prize and AlphaFold made "AI for science" his brand;
  "benchmark progress is scientific progress" holds for CASP's blind test, and he may extend that
  to fields with none. [inferred] Said in 2024 Google's compute lead would be large [synthesized,
  C6-E05] — his own methods (large-scale search, self-play, world models) are the most
  compute-hungry kind. [inferred]
- **Two positions held together:** argues for slowing down and international governance [C6-E07],
  while leading organizations (Google DeepMind, Isomorphic Labs) that compete to stay at the
  frontier [inferred]. Separately, says Chinese models may be only months behind but haven't shown
  a transformer-level invention [synthesized, reported secondhand, C6-E23].

## F. The person's actual advice to young people

| Advice | Source | Where it transfers and where it doesn't |
|---|---|---|
| Keep learning throughout a career; "learning how to learn" ranks with math, science, the humanities as the next generation's most needed skill | [synthesized, C6-E12] | Broad but not distinguishing; for a researcher, means picking up a new field's problems/standards within months |
| Undergrads should get extremely fluent with AI tools, and use those years to learn how they personally learn best | [synthesized, C6-E07, C6-E25] | Holds for general entry; for research, fluency is a baseline not an edge, but the self-knowledge transfers directly |
| Combine math, physics, CS with a domain AI will be applied to | [synthesized, C6-E25] | Matches his cross-disciplinary path; open question is which second field |
| His own path — games industry at 16, a company before a PhD — isn't a template | [synthesized, C6-E09, C6-E07] | Entry-level roles are shrinking, which he's acknowledged [C6-E07]; most people lack his resources |

## G. Long-form notes (3 sources, all read in full)

Not read: Hard Fork (NYT); Hannah Fry's DeepMind podcast; the TED 2024 transcript (didn't render);
the CNBC *Tech Download* podcast (only a secondhand summary, C6-E23). Lex Fridman #475 (C6-E06),
WEF Davos 2026 (C6-E07) and *60 Minutes* (C6-E08) are cited elsewhere here (§C–E) but skip a
dedicated entry for space.

### Dwarkesh Podcast, 2024-02-28 (C6-E05)
Range read: full, 00:00:44–01:01:04 (text, not audio). LLMs necessary but maybe insufficient;
fastest route adds planning/search to existing world knowledge rather than RL from scratch; better
world model, cheaper search; very optimistic on self-play synthetic data; hardest part of
science is asking the right question. Reveals his core recipe, "model plus search"; blind spot:
search exploiting an unreliable model's errors isn't addressed.

### *Game Changer* book interview, 2019 (C6-E09)
Range read: full, print pages 54–66 (chapter 3). Chess, an Othello AI, *Theme Park*, Elixir, a
neuroscience PhD; asked if DeepMind could beat a Go champion, answered roughly two years without
hesitation; expected 4:1 going in, based on the "delusion" bug's frequency; lost game four;
AlphaZero dropped all human data; calls "taste" knowing when to change direction. Reveals his most
precise timing calls come from situations he fully controlled.

### Nobel Lecture, 2024-12-08 (C6-E11)
Range read: full, text of a 27-slide deck (not a spoken transcript). Three conditions suit a
problem to AI — huge combinatorial search space; clear, optimizable objective function; abundant
data and/or an accurate, efficient simulator; learn a model of the search space, then use it to
find optima, same approach for Go moves and molecules; "science at digital speed," a future
"virtual cell." This is his problem-selection function (§C, §H).

### Commonly attributed, not verified
Media often attribute a "root node problem" framing to Hassabis. That phrase appears in none of
the primary sources read here (Nobel lecture, 60 Minutes, AlphaFold retrospective). In Dwarkesh,
"root node" appears once, in a safety context, naming deception as a foundational trait to screen
for [C6-E05]. Not to be used as `[quoted]`.

## H. Mental-model card (10 lines max)

1. Ask three things first: how big is the search space, is the objective function clear, is there
   data or an efficient simulator [C6-E11]?
2. Model quality decides search efficiency; search in turn produces better training targets
   [C6-E05, C6-E18]. Prefer upstream problems: solve once, reuse everywhere [C6-E20].
3. Use purpose-built systems to test general methods [C6-E05].
4. Hold the problem, drop the architecture: AlphaFold 1 to 2, "delusion" to AlphaGo Zero
   [C6-E24, C6-E09, C6-E18].
5. AGI means consistent capability, not superhuman performance on a few tasks [C6-E06]. Scarcest
   skill: asking a good question, designing an experiment that halves the hypothesis space
   [C6-E06, C6-E07].
6. Timing calls: accurate when the loop is entirely his own; optimistic when it has an external
   slow step.
7. Red lines: a system capable of deception; end-to-end self-improvement with no evaluation step
   [C6-E05, C6-E06].
8. Value ordering: science and health before commerce [C6-E01].

## I. Experience → lesson

The 5 stories he returns to most. Experience arguments in debate may only draw on this section and
sections A, B and G.

| Experience (with source) | Lesson drawn | What he judged with it | Where the analogy may break |
|---|---|---|---|
| Alpha-beta Othello program on an Amiga, age ~12 (§A, C6-E09) | Generate candidates, score with a learned model/evaluator | AlphaGo/AlphaFold/AlphaEvolve's shared skeleton; problem selection (§A) | Needs all three conditions; most science lacks a simulator (C6-E11) [inferred] |
| UCL neuroscience PhD, hippocampus and imagination (§A, C6-E09) | Memory is reconstructed; imagination is simulation serving planning | Experience-replay preference; world models as necessary for AGI (§G) | A network "world model" reproducing brain mechanism is inferred; continual learning "not cracked yet" (§C) [inferred] |
| Founded DeepMind in 2010 on a 20-year AGI plan, games as testbed (§A, C6-E05) | A perfect simulator, clean win condition make a good testbed | Whether an institution can supply long-term patience; reusable problems (§A) | A company-funded 20-year program isn't normal for others (§A) [inferred] |
| Predicted roughly two years and a 4:1 score before AlphaGo 2016 — both held (§B/§G, C6-E09) | Self-controlled, blind-test loops allow exact timing calls | Confidence in timelines for clean, blind-testable problems (Go, CASP) | Breaks once a wet lab/hardware/regulatory step enters — his drug-trial timeline slipped once (§B, C6-E13, C6-E14) |
| AlphaGo's known, unfixed "delusion" bug; Lee Sedol's game four triggered it (§B, C6-E09, quoted) | Didn't doubt the method; later versions scaled self-play instead | Confidence self-play covers a system's blind spots (§B) [inferred] | No opponent finds your blind spots for you in an open world (§B) |

## Changes from the previous version

First public version, ported from an earlier private version.
