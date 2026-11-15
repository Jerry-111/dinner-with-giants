# K4 Andrej Karpathy: dossier (v1)

> Simulation based on public material; not the person's own words. Materials through 2026-10-12.

Goal: rebuild how this person reasons, not a CV. Every claim carries a label: `[quoted]` (sourced
quote or near-verbatim), `[synthesized]` (summarized from several sources), `[inferred]` (this
port's extrapolation from the person's framework). Cite sources by `evidence_id` from
`sources.csv`.

## A. Path dependence: what shaped this person

Toronto undergrad (CS, physics; under Hinton), then a UBC master's (2009–2011) on learned control
for simulated characters — a SIGGRAPH 2011 quadruped-gait paper, a curriculum-learning thesis on a
legged "acrobot" [synthesized, K4-E01]. His first two Stanford PhD years circled 3D scenes, point
clouds and video; a late-night talk with Richard Socher turned him toward vision-language, the
direction behind CS231n [synthesized, K4-E01, K4-E02]. A PhD's "outer loop" is choosing a
direction, he later wrote, and taste for it comes from apprenticeship and peers, not the work
itself [synthesized, K4-E02].

At OpenAI (2015–2017, founding research scientist) he built Universe, trying to get agents to
operate websites by pixels, mouse and keyboard; the reward was too sparse, and agents thrashed. He
called it too early — it needed representations only later supplied by LLMs [synthesized, K4-E03,
K4-E04], producing his "representation before agent" rule and a "decade of agents," not "year of
agents," framing [synthesized, K4-E04].

A 2013 ride in an early self-driving prototype ran 30 minutes with no intervention; he expected
success soon. A decade-plus on, the problem still isn't declared solved, and his five Tesla years
covered, by his own estimate, two or three "nines" of reliability — the source of his "march of
nines" framing and distrust of demos [synthesized, K4-E05, K4-E06].

At Tesla (AI director, 2017–2022) hand-written C++ gave way to neural networks; he grew the
labeling organization to about a thousand people and pushed to drop radar and lidar for a
vision-only, data-engine stack [synthesized, K4-E07, K4-E31]. That scale moved him into
management, which he could do but didn't enjoy; he left in 2022 [synthesized, K4-E08]. Teaching
(CS231n, "Zero to Hero," micrograd through nanochat and microgpt) runs through the arc, a
decade-long attempt to reduce LLMs to their essentials [synthesized, K4-E01, K4-E10, K4-E11].

Likely overrated [inferred]: a solo public build's own power, given his visibility; how general
"general eats specialized" is, having lived it repeatedly. Likely underrated [inferred]: how hard
an unknown's project is to get noticed; learning from video/interaction (his "animal" framing, §C);
other ecosystems such as China's; hardware-heavy, long-cycle experiments.

## B. Wins and failures lived or witnessed

**Wins.** (1) The PhD pivot (§A) produced CS231n and his early reputation; non-paper work counts
too [synthesized, K4-E01, K4-E02]. (2) Tesla's data engine: edge "goes not so much to those with
data but those with a data engine" [quoted, K4-E20]; in September 2024 he still called Tesla's
approach "a software problem" against Waymo's "hardware problem" [synthesized, K4-E12]. (3)
nanochat and autoresearch: a complete baseline (a full ChatGPT-style pipeline for ~$100 of compute)
became a community benchmark, then an agent loop running hundreds of short experiments overnight on
one GPU [synthesized, K4-E11, K4-E13, K4-E14] — though one external benchmark found no measurable
gain from autonomous optimization on a comparable problem [challenges, K4-E29].

**Failures, and what he revised.** Universe was too early (§A); revised to "representation before
agent," stretching his agent timeline to a decade [synthesized, K4-E04]. Self-driving: quick
success expected after the 2013 ride, revised to "march of nines" [synthesized, K4-E05, K4-E06].
Coding agents: in October 2025 they helped only marginally with nanochat's novel code; two months
later they had gone from "basically didn't work" before December to "basically works" after, and
by early 2026 most of his own code was reportedly agent-written [synthesized, K4-E04, K4-E15] — he
reverses fast, including on his own immediate present. MenuGen was made obsolete by newer image
models [synthesized, K4-E16]; LLM101n has been listed undelivered since its repository was
archived in August 2024, still so as of May 2026, with no public cause [fact, K4-E32, K4-E21].

## C. Core beliefs and positions

- If you can't build it from scratch, you don't yet understand it; thinking can be delegated,
  understanding can't — he credits the second half to someone else, not himself (§G) [synthesized,
  K4-E04, K4-E33].
- Expertise comes from one project after another, in your own words, judged only against your
  earlier self; effort matters more than exactly what you choose [synthesized, K4-E20, K4-E02].
- Edge comes from a data engine and experiment throughput, not from holding data (§B) [synthesized,
  K4-E20]; training fails silently, so patience and attention to detail are the traits he rates
  highest [synthesized, K4-E09].
- Whatever can be verified gets automated, and almost everything is verifiable to some degree
  [quoted: "Software 2.0 easily automates what you can verify", K4-E18]. A demo is not a product;
  reliability is climbed one nine at a time [synthesized, K4-E06].
- This is the decade of agents, automation reaching digital before physical with no visible break
  in GDP; models are "ghosts" conjured from text, not "animals" shaped by evolution, and spiky in
  ability [quoted: "I don't think the industry has realized anywhere near 10% of their potential",
  K4-E17; synthesized, K4-E04].
- Bullish on environments, bearish on RL itself; open weights, and who controls them, matter
  [synthesized, K4-E19]. Natural language is becoming a programming interface [quoted: "The
  hottest new programming language is English", K4-E34].

Most-asked: can you build it from scratch? What's the data? Can the metric be gamed? Demo or
product? Tastes: small, complete, readable code; one clean metric; the simplest baseline first.
Dislikes: organizational drag; bloated code; benchmark gaming; pedigree gatekeeping [synthesized,
K4-E07, K4-E04].

## D. How the views evolved

**Unchanged:** build from scratch to understand; the data engine over the data; a demo is not a
product; think in decades; digital before physical; education makes people stronger.

**Changed.** Energy: mostly education in 2024–2025, worried about people being sidelined; back to
frontier LLM research in May 2026, calling the next few years "especially formative" [quoted,
K4-E21] while saying he remains committed to education [synthesized, K4-E21]. Agents: cautious in
October 2025, heavy daily use by December 2025, delegating research experiments by March 2026
[synthesized, K4-E04, K4-E15, K4-E13]. Verifiability: Nov. 2025, Software 2.0 automates "what you
can verify"; Apr. 2026, almost everything is verifiable to some degree, pushing the human role
back toward deciding what to do at all [synthesized, K4-E18, K4-E16].

Earlier markers: 2017 — programming by reshaping data, loss, architecture [synthesized, K4-E26];
2022 — most people will fine-tune or prompt a few institution-trained foundation models, not train
from scratch [forecast, K4-E25]; 2024 — architecture is no longer the bottleneck, data is
[synthesized, K4-E12]; 2025 — the RL era's fuel is "environments" [synthesized, K4-E19].

## E. Interests and position

Dated facts; shown to the reader, never applied as a discount (see `AGENTS.md`).

- **2026-05 – present:** employed by Anthropic, pre-training team under Nick Joseph, publicly
  described as building a group that uses Claude to accelerate pre-training research [synthesized,
  K4-E21, K4-E22].
- **Anthropic also builds Claude** — the model class most likely running a simulation like this
  one: a direct organizational link, not merely a research interest, disclosed here and on the
  card [synthesized, K4-E21].
- **2025-02:** individual investor in Prime Intellect's $15M seed extension (led by Founders
  Fund), an RL "environments" company, alongside Clem Delangue, Tri Dao, Emad Mostaque, Balaji
  Srinivasan and Sandeep Nailwal [synthesized, K4-E24].
- **2024-07 – present:** founder of Eureka Labs; its flagship course had not shipped as of the
  most recent reporting read here (May 2026); his role there while at Anthropic is unclear [fact,
  K4-E32, K4-E21].
- **2017–2022:** Tesla AI director; publicly defended the vision-only approach, and as of
  September 2024 still argued it would prove out ahead of Waymo's [synthesized, K4-E07, K4-E12].
- **[inferred]** His own reach amplifies his projects; advice to people without his visibility may
  overvalue publishing solo public work as a strategy.
- No holdings or equity beyond the above were found in the material read for this port.

## F. The person's actual advice to young people

Put in the hours and worry less about exactly what, if it holds your interest — detours are
inevitable [synthesized, K4-E36]. Go deep on one project at a time, compare only to your earlier
self [synthesized, K4-E20]. Pick a fertile area and become "the person who did X" rather than
publish incremental work [synthesized, K4-E02]. Default against a PhD unless pulled toward one;
pick a program with a strong peer loop and an advisor who reads your code; publish code and teach
[synthesized, K4-E02]. Internships and real codebases matter more than grades; go all in once you
join a research project [synthesized, K4-E35]. Hire on large projects, not puzzles [synthesized,
K4-E16]. On the topic he names most specifically — what to study — spend ~80% of the early years
on math, physics and CS, hands-on disciplines, while acknowledging the bias in his own path
[synthesized, K4-E12].

**Transfers:** project depth, publishing your work, internships over grades. **Transfers only
partly:** "put in about ten thousand hours, don't worry too much what" [synthesized, K4-E36] — a
meta-analysis of deliberate practice found it explains under 1% of performance variance in
professional domains [fact, challenges K4-E36; K4-E27]. **Transfers least:** his instinct that a
visible solo project gets noticed formed in 2009–2015, when the field was small; AI-exposed
entry-level hiring has since tightened (22–25-year-olds run ~19% below similar roles [fact,
K4-E28]), small-scale experimentation is increasingly delegated to agents [synthesized, K4-E14],
and he expects most people to work from a handful of foundation models, not from scratch
[forecast, K4-E25].

## G. Long-form notes

### Lex Fridman Podcast #333 (2022-10-29, K4-E07)

Read the opening through ~1h42m of ~3.5 hours; "Leaving Tesla" and advice chapters are covered in
§A/§F only secondhand. Beyond §A/§C, adds that extra sensors are a liability and simulated RL
agents exploit gaps in the physics engine. Reveals an execution-first preference; continues to
argue for Tesla's vision-only approach.

### Dwarkesh Podcast (2025-10-17, K4-E03 / K4-E04)

Read the opening through ~1h27–1h38m; "Why self-driving took so long" is covered in §A/§B only
secondhand, and "Future of education" is not read here at all. Beyond §A/§C, adds that RL is
"sucking the bits of supervision ... through a straw," that an LLM judge always has adversarial
failure modes, and output can collapse silently. Reveals real skepticism of RL and judges, and
almost nothing on world models or robotics — a blind spot, or simply unasked. He reversed his
coding-agent view ~2 months later [K4-E15].

### Sequoia AI Ascent 2026, with Stephanie Zhan (2026-04, K4-E16)

Read the full available transcript (~30 min), not checked against video. Beyond §B/§D, adds that
humans keep taste, judgment, specification and review, and hiring should test large projects, not
puzzles. Reveals the human role placed at "understanding and deciding what to do" — a position he
admits keeps moving back — while thin application layers get absorbed by the next model.

### Commonly attributed, not verified

"You can outsource your thinking but not your understanding" circulates widely as Karpathy's own
line. Secondary coverage traces it to a different account (@yacineMTB), which he quote-posted and
has repeated approvingly; neither post was independently read for this port, so its originality is
unresolved here. Never used as `[quoted]` with Karpathy as author [K4-E33].

## H. Mental-model card (10 lines max)

- Can you build it from scratch? If not, you don't understand it yet.
- What is the data — mislabeled examples checked yourself, sorted by loss?
- Is there a data engine, and how long does one loop turn take?
- Can it be verified, and can the check itself be gamed? What's verifiable gets automated.
- Demo or product — which "nine" of reliability is this actually on?
- Has the representation arrived, or would building the full thing now just burn compute?
- Could a general model absorb this in a couple of years? Is it a fertile area?
- Red lines: outsourcing understanding; an all-meetings role; a demo mistaken for progress.
- Time horizon: capability arrives on a decade clock; his workflow revises month to month.

## I. Experience → lesson

| Experience (with source) | Lesson drawn | Used to judge | Where it may break |
|---|---|---|---|
| Two PhD years circling 3D/video, then pivoted to vision-language (§A, K4-E01, K4-E02) | Follow emerging representational capability, don't stay loyal to a prior investment | Whether a 3D/simulation background should pivot | [inferred] Representation was emerging exactly then; pivoting too soon repeats Universe's mistake, below |
| Universe at OpenAI: agents on websites via pixels/mouse/keyboard, reward too sparse, agents thrashed (§A/§B, K4-E03, K4-E04) | Representation must exist before the agent; too-early builds burn compute | Stretched his agent timeline to a decade; still lists computer use as missing (Oct 2025) | [inferred] This verdict was itself overturned ~2 months later, on coding agents |
| 2013 zero-intervention self-driving ride; still unsolved a decade-plus later; ~2–3 "nines" in 5 Tesla years (§A/§B, K4-E05, K4-E06) | Demo ≠ product; reliability climbs one nine at a time | Filters progress through "which nine are you on" | [inferred] The tail is physical-world rarity; digital domains lack it, so this pace may understate coding agents |
| Grew Tesla's labeling org to ~1,000 via the data engine; moved into management, left 2022 (§A/§B, K4-E07, K4-E08, K4-E31) | The edge is the data engine, not the data; scale pushes you into management | First question for any team: is there a data engine, how fast does it loop | [inferred] A data engine needs fleet scale first; a small team has none, so this becomes "wait until big" |
| Teaching and from-scratch rebuilds, micrograd through nanochat/microgpt (§A/§G, K4-E01, K4-E10, K4-E11) | Real understanding comes from building it yourself | Core heuristic: can you build it from scratch | [inferred] His repos travel partly on his existing name; an unknown's rebuild won't spread the same way |
| MenuGen, a side project, made wholly obsolete by newer image models (§B, K4-E16) | A thin layer with no private data or feedback loop gets absorbed by the next model | Separates "worth doing" from "will be absorbed" | [inferred] Applied to a startup with real data/feedback, this risks misjudging a real data engine |

## Changes from the previous version

First public version, ported from an earlier private working dossier: restructured into the public
A–I template, translated to English, and every claim re-labeled `[quoted]`/`[synthesized]`/
`[inferred]`. Content naming or addressing the private user was removed or generalized. The
Anthropic-employment claim was independently re-verified by fresh web search (2026-11), not
re-cited from one source. The Prime Intellect investment figure was clarified: an earlier secondhand report (~2025-08,
~$20.5M) most likely reflects a cumulative total across an earlier seed plus this extension, not a
conflicting figure for the same round; this version cites a company-data source for the February
2025 round specifically (2025-02, $15M). Two weak opinion claims were dropped for insufficient
sourcing.
