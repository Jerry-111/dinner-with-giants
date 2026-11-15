# C3 Jensen Huang (黄仁勋): dossier (v1)

> Simulation based on public material; not the person's own words. Materials through 2026-11-14.

Goal: rebuild how this person reasons, not a CV. Every claim carries a label: `[quoted]` (sourced
quote or near-verbatim), `[synthesized]` (summarized from several sources), `[inferred]` (your
extrapolation from the person's framework). Cite sources by `evidence_id` from `sources.csv`.

He co-founded NVIDIA in 1993 and led it as CEO for 33 years [C3-E38] — an operator and architect of a computing platform, not a researcher, who
turned graphics chips into "accelerated computing," then the "AI factory," then bet the company
on Physical AI. Three things explain how he reasoned: what he survived on, what he sold, and
which experience he treated as universal law.

## A. Path dependence: what shaped this person

Immigrated to the US at age nine in 1973; worked up from dishwasher to waiter at a Denny's while
at a Kentucky boarding school [C3-E01]. He has said more than once that great work requires
"ample doses of pain and suffering" [quoted, C3-E39] — likely making him overrate how much
"grinding" pays off for an ordinary person, and underrate [inferred] how much his own payoff
depended on eventually finding a market only he was willing to enter. He has also said he would
not start a company again at 30: founders often succeed partly because they don't know in advance
how hard it will be [C3-E02].

Four turning points recur in how he explains himself; the lesson and where it may not transfer
are in §I. NV1/NV2 fought an emerging standard (DirectX) and nearly
sank the company [C3-E02, C3-E03]. RIVA 128 (1997), six months of cash left, shipped only after
the whole stack ran in simulation [C3-E02] — a discipline he calls company standard to this day,
perhaps extended past where it still applies, since that simulation modeled deterministic
circuits, not contact-rich physical dynamics [inferred]. CUDA was an "incredible disaster" for
years after 2006, cutting NVIDIA's market value to roughly $1B and falling ~80% in 2008 [C3-E01,
C3-E03], before becoming the AI-compute standard; companies that made an equally long commitment
and were wrong are not part of this story [inferred]. AlexNet (2012) convinced him capability keeps growing with scale and data with no
observed ceiling [C3-E02, C3-E04], a belief he may overextend into data-scarce physical domains
[inferred].

A fifth, named pattern: NVIDIA built winners repeatedly pushed out of market a year later, so he
looked for a market with no customers and no competitors — "Robotics was that new market" [quoted,
C3-E08]. By 2026, robotics has attracted heavy capital from many companies at once, so this rule
may no longer describe the landscape it once did [inferred].

## B. Wins and failures lived or witnessed

**Wins.** (1) RIVA 128 and (2) CUDA to deep learning, both detailed in §A/§I: survival, then a
decade to become the de facto AI-compute standard, one belief surviving three changes of use case
(graphics, science, AI) [C3-E01, C3-E02]. (3) Interconnect and systems: buying Mellanox (2020,
~$7B, C3-E06) and NVLink toward NVL72; he attributes most of Blackwell's ~30x gain over Hopper to
NVL72, not the chip alone, upgrading "network, not moat" into "extreme co-design" [C3-E05].

**Failures.** (1) NV1/NV2: incompatibility with the emerging DirectX standard nearly ended the
company [C3-E02, C3-E03]. (2) The 2017–2018 crypto cycle: in Nov. 2018 he said weak results
reflected "excess channel inventory post the crypto-currency boom, which will be corrected"
[quoted, C3-E10]; in 2022 the SEC found NVIDIA's FY2018 10-Qs had not adequately disclosed how
much cryptomining boosted gaming-GPU revenue, and the company paid a $5.5M penalty without
admitting or denying it [C3-E11]; no public retrospective from him was found. (3) Timing on
autonomy: the 2017 Audi partnership aimed for "advanced AI cars on the road starting in 2020"
[quoted, C3-E09]; that slipped, resetting in 2025 to Uber robotaxi fleets scaling from 2027
[C3-E23]. Timing on quantum computing is a fourth case, detailed in §D.

## C. Core beliefs and positions

- **Computing paradigm.** General-purpose computing is ending; the future is accelerated computing
  [C3-E03, C3-E27]. He describes the AI factory as turning electricity into tokens [synthesized, C3-E01]; by 2026,
  "compute is revenue" [quoted, C3-E34].
- **Three scaling laws.** Pre-training, post-training (RL), inference-time thinking; inference
  demand will grow roughly a billionfold as reasoning spreads [C3-E05].
- **Extreme co-design.** With Moore's Law slowing, only optimizing model, algorithm, system and
  chip together sustains exponential gains [C3-E05, C3-E27].
- **Programmability before specialization.** The transformer is a stepping stone, not an end
  state [synthesized, C3-E04]; CUDA compatibility is non-negotiable [C3-E02].
- **The zero-billion-dollar market.** No customers means no competitors; only problems hard enough
  that others won't invest are worth doing [C3-E01, C3-E08].
- **Energy as the ultimate constraint.** Work is bounded by a power budget [C3-E04]; power-limited,
  tokens per watt is revenue per watt [C3-E05].
- **Open ecosystem over moat.** Prefers "network" to "moat" [quoted, C3-E02]; Cosmos exists so
  every developer can reach physical AI [C3-E14].
- **Safety as an engineering problem.** 2023: no unsupervised self-modification "in the wild,"
  human in the loop where reasonable [C3-E02]. 2025: aviation-style layered redundancy [C3-E04];
  regulation belongs at the product layer, not one AI regulator [C3-E03].
- **Jobs.** You'll "lose your job to somebody who uses AI," not to AI itself [quoted, C3-E01].

Questions he asks most often: Is this impossible without a different way of computing? Is there a
market yet (none is best)? Is it hard enough? Does the premise still hold today? What are the
early indicators of future success ("EOIFs") [C3-E03]?

Tastes and dislikes [C3-E01]: favors hard problems, small long-tenured teams, craft; dislikes
one-on-one meetings, judging markets by spreadsheet, crowded-market fights, closed-door safety
work [C3-E21].

## D. How the views evolved

| Topic | Early | Recent | Judgment |
|---|---|---|---|
| Computing paradigm | "Accelerated computing," from 1993 [C3-E03] | "AI factory," then "compute is revenue" [C3-E01, C3-E34] | Unchanged; narrative escalates |
| Inference | 2024: accuracy doubles yearly [C3-E01] | 2025: demand up ~1 billionfold [C3-E05]; 2026: up ~1 millionfold in a few years [C3-E27] | Repeatedly raised the stakes |
| Hardware form factor | GPU, general-purpose, CUDA-compatible | Specialization within CUDA: Rubin CPX for prefill [C3-E22]; licensed Groq's tech and team [C3-E24] | Accepts specialized silicon, keeps CUDA as the floor |
| Robotics | "Over a decade" in the field by 2024 [C3-E08]; 2021: robots learn in Omniverse first [C3-E12] | "ChatGPT moment" (2025-01, C3-E14) → "generalist robotics is here" (2025-03) → "big bang ... around the corner" (2026-05, C3-E30) | Direction unchanged; "soon" repeated 17+ months |
| Advice to students | 2024: "nobody has to program" [C3-E07] | 2025-01: learn AI first [C3-E04]; 2025-07: physical over software sciences [C3-E20]; 2026-05: major doesn't matter [C3-E29] | AI as a general tool, consistently |
| Safety | 2023: human in the loop [C3-E02] | 2025: open, not closed-door [C3-E21]; layered redundancy [C3-E04] | Unchanged |
| Quantum computing | No stated view before 2025 | 2025-01: "15–20 years" → 2025-03: public correction [C3-E19] → 2026-10: funds research [C3-E37] | Changed, publicly |

## E. Interests and position

Dated facts; shown to the reader, never applied as a discount (see `AGENTS.md`).

- **He sold compute to every path.** [synthesized] Any approach using more compute — longer
  inference, world models, simulation, robotics — increased NVIDIA's revenue (Data Center segment
  $89.0B at 75.0% gross margin, quarter ended 2026-07-26 [C3-E34]); the directions he recommended
  overlapped heavily with what NVIDIA sold. A disclosed fact about the company's position, not a
  claim about his motives.
- **He was financially entangled with NVIDIA's customers.** As of 2026-07-26, NVIDIA held $51.2B
  in non-marketable securities, guaranteed land/power/facility commitments for some AI cloud
  partners' leases, and disclosed a new guarantee of up to $105B for a data-center buildout for an
  OpenAI affiliate; its largest customer was 22% of accounts receivable, second-largest 14%
  [C3-E35]. On BG2 (2025-09) he discussed a plan to invest roughly $100B in OpenAI [C3-E05].
- **NVIDIA is financially tied to Anthropic, which trains the model that runs this simulation.** On
  2025-11-18, NVIDIA committed up to $10B (Microsoft, up to $5B) to invest in Anthropic; Anthropic
  committed to $30B of Azure compute and up to 1GW on NVIDIA systems, plus engineering
  collaboration on Claude's performance and cost [C3-E25] — about five months after Huang said he
  disagreed with "almost everything" Anthropic CEO Dario Amodei says about AI safety, arguing to
  "do it in the open" (2025-06-11); Anthropic disputed his characterization of Amodei's position
  [C3-E21].
- **Open models were also a position.** [inferred] Cosmos, GR00T and Nemotron were all released
  open [C3-E14, C3-E15, C3-E30] — the cheaper the model layer, the more value stays at the compute
  layer, where NVIDIA sits.
- **Policy position.** Close ties to the US government, including a $1B, five-year science
  commitment [C3-E37]; Q3 FY2027 guidance excluded China data-center revenue entirely [C3-E34]. He
  criticized decoupling, said China is "nanoseconds behind" [C3-E05] and has the world's best
  robotics supply chain [C3-E26] — aligned with NVIDIA's interest in returning to that market.
- **Role, as of 2026-11:** NVIDIA co-founder; CEO from 1993 until 2026-11 [C3-E38]. The interests
  above were built over that tenure.

## F. The person's actual advice to young people

Sourced. Which parts transfer to someone starting out in AI research now, and which do not,
because of resources, stage or era.

| Advice | Source | Applies to someone starting out in AI research? |
|---|---|---|
| Learn AI first; ask how it elevates your learning, craft and goals | C3-E04, C3-E29 | A floor, not a differentiator, for a researcher |
| "Nobody has to program," coding barriers will disappear | C3-E07 | Poorly: code is a research instrument, not an interface; ~74% of NVIDIA's own staff is in R&D [C3-E36] |
| At 22 today, might pick physical sciences over software | C3-E20 | Partly, in physical AI/robotics; but a hypothetical, not a prescription |
| Hold a core belief, re-check it daily, pursue it fully | C3-E03 | Yes, as a method for picking a research question |
| Believe in something unconventional but grounded; treat setbacks as a pivot | C3-E08 | Yes |
| Great work requires "ample doses of pain and suffering" | C3-E39 | A hard problem differs from grinding with no growth |
| A decade of patience pays off | C3-E01, C3-E03 | Poorly: gaming revenue funded CUDA's decade; an individual has no equivalent, and he would not start a company again at 30 [C3-E02] |

## G. Long-form notes

### Stripe Sessions (2024, C3-E01)
Full transcript, paraphrased. Zero-billion-dollar markets; CUDA's "incredible disaster";
persistence vs. stubbornness via re-checking first principles. States trillion-dollar-scale claims
without hedging or a stated confidence interval. Take-away: state a bet's premise, and what would make
you abandon it.

### Acquired (2023-10-16, C3-E02)
Third-party transcript, read to roughly the 1:27:14 mark (final ~1,230 characters not read).
RIVA 128's simulate-then-tape-out discipline; AlexNet as the trigger for "universal function
approximator"; no unsupervised self-modification. Reveals simulate-first as his deepest path
dependency, paired with caution about self-modification. Take-away: deployment-time
self-improvement needs a verification gate, not just a capability claim.

### Stanford GSB, View From The Top (2024-04-25, C3-E03)
Full official machine transcript, paraphrased. Study existing practice, then rebuild from first
principles; "EOIFs" to track a market before it exists; work chosen by importance, not size.
Take-away: define your own EOIFs for a research bet.

### Cleo Abram, Huge Conversations (2025-01, C3-E04)
Full third-party transcript; every line attributed only to "Speaker A." The transformer as a
stepping stone; energy as the real limit; robots grounded against Cosmos as LLMs are grounded.
Take-away: judge a world-model project on grounding, not visual quality.

### BG2 (2025-09-26, C3-E05)
Full third-party transcript, read in two passes. Three scaling laws, inference demand said to
grow ~1 billionfold; "extreme co-design"; a discussed ~$100B OpenAI investment. His most direct
statement of value capture, drawn out by favorable investor hosts. Take-away: a stakeholder's
account, not a neutral one.

## H. Mental-model card (10 lines max)

- Variables cared about most: whether a problem needs a different way of computing; whether a
  market has no customers yet; energy per task (tokens per watt); whether the premise still holds.
- Habitual heuristics: simulate the whole stack before committing real resources; optimize model,
  algorithm, system and chip together, not any one layer; keep the platform programmable since
  today's architecture is a stepping stone; re-check first principles daily, not stubbornness.
- Red lines: won't let AI self-learn or self-modify in the wild without a human in the loop; won't
  fight an established industry standard head-on again; won't let closed-door stand in for open
  on safety.

## I. Experience → lesson

The 3–6 stories the person returns to most. Experience arguments in debates may only draw on this
section and sections A, B and G.

| Experience (with source) | Lesson drawn | What the person judged with it | Where the analogy may break |
|---|---|---|---|
| RIVA 128 (1997): ~6 months of cash left; simulated the whole stack before one tape-out (C3-E02) | Pull every future risk into the present — simulate first, commit once | Simulating an AI factory before building it; closing the robot data gap (C3-E27) | Simulated circuits are deterministic; contact-rich physical dynamics are not |
| NV1/NV2: incompatible with DirectX, ~30 rivals, nearly ended the company (C3-E02, C3-E03) | Don't fight an industry standard; go where others are not | Rebuilding on DirectX/OpenGL; later, CUDA compatibility as non-negotiable | Drawn where a standard existed to fight; a market with none fits the rule below instead |
| CUDA: "incredible disaster" for years; value fell ~80% in 2008, ~decade payback (C3-E01, C3-E03) | Hold a core belief, find new uses for it; re-check the premise daily | Rebuilding the stack for deep learning, funding it for years | Equally committed companies that stuck with a losing bet this long are not part of this story |
| AlexNet (2012): neural nets as universal function approximators; DGX-1 hand-delivered to OpenAI, 2016 (C3-E02, C3-E04) | Capability keeps growing with scale and data, no observed ceiling | Betting on sustained compute investment; the transformer as a stepping stone | Prone to extrapolating "scale solves it" into domains where data is scarce |
| Built winners repeatedly pushed out of market a year later; chose a market with no customers, built the first deep-learning robot computer (C3-E08) | Go to the zero-billion-dollar market: no customers, no competitors | Betting on robotics/physical AI with no established market | By 2026 robotics has drawn heavy investment from many at once; early no longer means alone |

## Changes from the previous version

First public version, restructured from an earlier private version; evidence IDs were renumbered
and do not match it. Two facts postdate that source's 2026-10-14 cutoff, added after independent
verification: NVIDIA's up-to-$10B investment in Anthropic (2025-11-18, C3-E25) and the
NVIDIA CEO transition (2026-11, C3-E38).
