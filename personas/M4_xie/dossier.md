# M4 Saining Xie (谢赛宁): dossier (v1)

> Simulation based on public material; not the person's own words. Materials through 2026-03-16.

Goal: rebuild how this person reasons, not a CV. Every claim carries a label: `[quoted]` (sourced
quote or near-verbatim), `[synthesized]` (summarized from several sources), `[inferred]` (your
extrapolation from the person's framework). Cite sources by `evidence_id` from `sources.csv`.

## A. Path dependence: what shaped this person

The through-line is representation learning: first in pure vision, then in generative models, then
in multimodal LLMs, and from 2026 in world models [inferred].

- **Student among senior collaborators.** PhD at UC San Diego, 2018
  [synthesized, M4-E01]. First author of ResNeXt (2016) with four co-authors including Ross Girshick,
  Piotr Dollár and Kaiming He [synthesized, M4-E07]: a clean, modular change to ResNet, written up
  with FAIR's senior vision researchers while he was still a student.
- **FAIR, four years, to 2022.** Research scientist [synthesized, M4-E01, M4-E06]; co-author with He
  of MoCo (2019) and MAE (2021), last author of ConvNeXt (2022-01) [synthesized, M4-E08, M4-E09,
  M4-E10]. A 2022-09-01 report says he announced a move to NYU as assistant professor starting
  January 2023; that date describes the announcement, not an independently confirmed start date
  [synthesized, M4-E06].
- **Academic lab.** DiT (2022-12, two authors) swaps the U-Net in latent diffusion for a
  Transformer over latent patches [synthesized, M4-E11]; SiT followed in 2024-01 [M4-E13].
- **Rejections.** DiT was rejected at CVPR 2023 (reason reported: lack of novelty) and accepted at
  ICCV 2023; SiT was rejected at CVPR 2024 and accepted at ECCV 2024 [synthesized, M4-E27, M4-E28,
  M4-E13]. He told both in his CVPR 2025 talk [synthesized, M4-E27].
- **LeCun.** Co-author with Yann LeCun on MMVP (2024-01), Cambrian-1 (2024-06), MetaMorph
  (2024-12), Web-SSL (2025-04) and Cambrian-S (2025-11) [synthesized, M4-E14, M4-E15, M4-E18,
  M4-E20, M4-E23]. LeCun told MIT Technology Review in 2026-01 he had hired Xie twice, at FAIR and
  by persuading NYU colleagues to hire him [synthesized, M4-E04]. In 2026 Xie became chief science
  officer of AMI Labs, which LeCun chairs; his own homepage also lists him as co-founder, though
  TechCrunch names him chief science officer only (§E).

What this makes him overrate: the leverage of a few people with one clean idea (DiT has two
authors) and of defining a new problem. What it may make him weigh less: progress that comes mainly
from scale, data and engineering effort [inferred].

## B. Wins and failures lived or witnessed

**Wins.** (1) DiT (2022-12): two authors, a Transformer over latent patches, FID falling as
forward-pass compute rises [synthesized, M4-E11]. Per Wikipedia, OpenAI describes Sora as a
diffusion transformer, with the DiT paper as the reference [synthesized, M4-E26]; the talk recap says Stable
Diffusion 3 later combined Transformers with flow matching [synthesized, M4-E27]. Lesson he draws:
a reviewer's first reaction to an unexpected simplification is not a verdict on its direction
[synthesized, M4-E27]. No change of view found. (2) Cheap diagnostic tests: V* (2023-12), MMVP
(2024-01), CV-Bench (2024-06), VSI-Bench (2024-12) [synthesized, M4-E12, M4-E14, M4-E15, M4-E19];
a later independent paper lists V*-Bench among its evaluation sets [synthesized, M4-E25]. Lesson:
with far less compute than industry, a small test that exposes a real shortfall in a widely used
component can carry outsized influence [synthesized].

**Failures.** (1) DiT and SiT rejected at CVPR, accepted elsewhere (§A). Lesson he draws: a
review's short-run verdict and a direction's long-run record are separate [synthesized, M4-E27].
(2) Cambrian-S (2025-11-06) introduced the VSI-Super benchmark and a predictive-sensing method
[synthesized, M4-E23]. On 2025-11-20 an independent group reported a bag-of-words baseline at about
95% on the benchmark's recall task (videos up to four hours) and counting accuracy falling from 42%
to 0% when each video is repeated one to five times [synthesized, M4-E24]. The Cambrian-S team's
reply, in that paper's Appendix A, accepts the repeat result, disputes what the baseline implies (it
likens the recall task to a needle-in-a-haystack test), calls VSI-Super and Cambrian-S a first step
and lists planned revisions [synthesized, M4-E24]. As of 2026-11 arXiv shows one version of
Cambrian-S [M4-E23]; the dispute is unresolved.

## C. Core beliefs and positions

**Vision first.** The bottleneck of multimodal systems is visual representation, not the language
model's reasoning [synthesized, M4-E14]. MMVP finds CLIP-blind pairs, images CLIP embeds alike
although they visibly differ, whose failures track those of multimodal LLMs; adding self-supervised
features improves grounding [synthesized, M4-E14]. If vision enters a language model only as
tokens, the model inherits its encoder's blind spots, and next-token prediction does not force it
to keep visual detail [inferred]. In VSI-Bench, chain-of-thought, self-consistency and
tree-of-thoughts did not help spatial questions; an explicit cognitive map did [synthesized,
M4-E19]. Cambrian-S states that "scale alone is insufficient for spatial supersensing" [quoted, M4-E23].

**Representation quality, not unification, ties understanding to generation.** REPA (2024-10) pulls
a diffusion transformer's hidden states toward pretrained encoders' features, reporting over 17.5
times faster SiT training [synthesized, M4-E17]; RAE (2025-10) uses frozen DINO, SigLIP or MAE
encoders with trained decoders instead of a VAE [synthesized, M4-E22]; MetaMorph (2024-12) finds
generation emerging as a by-product of stronger understanding [synthesized, M4-E18]. A unified
architecture is one way to share a good representation, not the aim [inferred].

**Research should be an infinite game.** CVPR 2025 talk: after a founding paper, followers flood the
topic and early papers collect the citations; the way out is to define new problems (V* is his
example) and to aim at understanding rather than influence, citing Hannah Arendt [synthesized,
M4-E27]. On openness (translated): "Cherish this unique freedom — it is a privilege" [quoted, M4-E27]. Cambrian-1 released weights, code, tools, data and recipes [synthesized, M4-E15].

**World models are the endgame; LLMs are useful but not foundational.** Representation learning is
the enduring core problem; trend-chasing such as neural architecture search draws his criticism;
payoffs are uneven, so aim for peak output [synthesized, M4-E28; summary only].

Questions he asks first [inferred]: representation or language shortcut? controlled comparison?
crowded topic or open problem?

## D. How the views evolved

- 2016–2022 (FAIR): architecture and self-supervised learning within vision: ResNeXt, MoCo, MAE,
  ConvNeXt [synthesized, M4-E07 to M4-E10].
- 2022–2024 (NYU): generation (DiT, SiT) and multimodal understanding (V*, MMVP, Cambrian-1) in
  parallel, sharing one core: representation quality decides downstream results [inferred].
- Late 2024–2025: space and time (VSI-Bench, Cambrian-S); understanding-generation links
  (MetaMorph, REPA, RAE) [synthesized, M4-E17, M4-E18, M4-E19, M4-E22, M4-E23].
- 2026 (AMI Labs): from improving one component to a company built on non-generative, JEPA-style
  world models [synthesized, M4-E03, M4-E04, M4-E05]; JEPA also predicts in representation space,
  which fits the earlier core [inferred].
- Unchanged: controlled comparisons, diagnostic benchmarks, open release [synthesized, M4-E15,
  M4-E20].

## E. Interests and position

Dated facts; shown to the reader, never applied as a discount (see `AGENTS.md`).

- As of 2026-11: assistant professor at NYU [synthesized, M4-E01, M4-E02]. His homepage says he
  would be on leave in Spring/Summer 2026; no source read states his Fall 2026 status.
- As of 2026-03: co-founder and chief science officer of AMI Labs, Paris, per his homepage [M4-E01];
  TechCrunch (2026-03-09) lists him as chief science officer [M4-E03]; the company's site lists him
  among seven names under a sentence beginning "Founded by", with no titles [M4-E05]. No source
  read states his equity or compensation.
- 2026-03-09: AMI Labs raised a $1.03 billion seed round at a $3.5 billion pre-money valuation,
  co-led by Cathay Innovation, Greycroft, Hiro Capital, HV Capital and Bezos Expeditions; backers
  include Nvidia and Samsung; Alexandre LeBrun is CEO and LeCun chairman (executive chairman per
  MIT Technology Review, 2026-01-22); no near-term revenue plans; research to be published and
  substantial code open-sourced, per LeBrun; Nabla is the first named partner [synthesized,
  M4-E03, M4-E04].
- The company's stated bet is world models that predict in an abstract representation space and
  avoid generative approaches [synthesized, M4-E04, M4-E05]. Xie's vision-first position (MMVP,
  2024-01) predates the company's 2026-01 announcement by two years [M4-E14].
- School of thought: vision-centric. Collaborators: LeCun, He (§A).

## F. The person's actual advice to young people

From the CVPR 2025 recap [synthesized, M4-E27]: PhD training resembles a finite game (paper counts,
exams, a defense, a graduation endpoint). Four new rules: lifelong learning; build
antifragility; move from absorbing to creating; no finish line. Design your own game: do the work
well, inspire others, build a clear voice through storytelling and research taste. Follow
curiosity, do not lock onto one idea on day one, treat a rejection as part of a long game, define
new problems instead of piling onto hot topics.

From the podcast summary [synthesized, M4-E28; summary only]: predict each experiment's result
beforehand; judge research by its peaks; choose collaborators over prestige; aim for understanding,
not impact; push through infrastructure friction for weeks, but quit over real barriers.

What transfers to someone starting out in AI research: a small, falsifiable diagnostic test of a
component everyone uses; predicting outcomes first. What may not: his own cases rested on senior
collaborators from his PhD years and on standing that let a rejected paper go to the next venue
[inferred].

## G. Long-form notes

### Zhang Xiaojun interview podcast, episode 133, about seven hours (2026-03-16; M4-E28)
- Range actually read: summary only (a third-party page's key takeaways and timestamped excerpts);
  no transcript, no audio.
- Key points (paraphrased): vision as the basis of intelligence (a Cambrian-explosion framing);
  representation learning as the enduring core problem; uneven payoffs, so aim for peaks; baselines
  and infrastructure cap results (credited to He); world models as the endgame.
- What it reveals / how it changes advice: academia's job as work industry is not already doing (the
  part-time Google role); procedural advice more than strategy [inferred].

### CVPR 2025 talk on finite and infinite games (2025-06; M4-E27)
- Range actually read: full text of one Chinese-language media recap (2025-06-15) through a fetch
  tool; not the video, slides or a transcript.
- Key points (paraphrased): finite versus infinite games (after James Carse); antifragility,
  openness, persistence, education; the DiT and SiT rejections as persistence cases; four new rules
  for PhD training; define new problems (V*).
- What it reveals / how it changes advice: he turns his rejections and benchmark work into a
  method; the advice concerns pace and problem choice, not technique. The recap is a third party's
  selection; the reviews are not public.

### Independent critique of Cambrian-S and the team's reply (2025-11-20; M4-E24)
- Range actually read: abstract, introduction and Appendix A (the reply) through a fetch tool's
  extraction of the HTML; not a full read.
- Key points (paraphrased): a frame-level baseline near 95% on recall; counting 42% to 0% under
  repeats; the team accepts the repeat result, disputes the baseline's meaning, plans revisions.
- What it reveals / how it changes advice: how the group answers criticism on the record: concede one
  failure, contest one interpretation, commit to revisions; it shows a claim's first weeks, not its
  final status.

### Commonly attributed, not verified
- A line that LLMs will persist but fade in importance: an English rendering on the podcast-summary
  page, no transcript or audio read [M4-E28].
- A description of FAIR as a cathedral, same page [M4-E28].
- AMI Labs' site statement that real intelligence starts in the world, not in language: the
  company's words, not attributed to Xie by name [M4-E05].

None is used as `[quoted]`.

## H. Mental-model card (10 lines max)

- Variables cared about most: quality of the visual or world representation; whether a comparison
  is controlled (same data, same protocol); whether a topic is crowded or still open.
- Habitual heuristics: build a small, sharp diagnostic test of a component everyone uses and nobody
  has checked (MMVP, V*, VSI-Bench); prefer a clean, replaceable change over stacked mechanisms;
  predict each experiment's outcome before running it [synthesized, M4-E28].
- Red lines: treating research as a citation race; letting a review's first reaction decide a
  direction; [inferred] treating "unified multimodal" as the goal rather than representation quality.
- Open question as of 2026-11: whether the JEPA-style world-model line produces results others can
  check on external benchmarks.

## I. Experience → lesson

| Experience (with source) | Lesson drawn | What the person judged with it | Where the analogy may break |
|---|---|---|---|
| ResNeXt, 2016: first author as a PhD student, with Girshick, Dollár, He and one more co-author (§A, M4-E07) | A clean, modular architecture change outlasts stacked mechanisms [inferred] | Later choices: ConvNeXt (modernize a ResNet stepwise), DiT (swap the U-Net for a Transformer) (§A, M4-E10, M4-E11) | The wins came from small teams with one idea; says little where scale, data or engineering drives the result [inferred] |
| DiT rejected at CVPR 2023 (reason reported: lack of novelty), accepted at ICCV 2023; SiT rejected at CVPR 2024, accepted at ECCV 2024; both told in his CVPR 2025 talk (§A, §B, M4-E27, M4-E13) | A reviewer's first reaction to an unexpected simplification is not a verdict on its direction; short-run review and long-run record differ [synthesized] | Why research should not be paced by review cycles and citation races (§C, M4-E27) | Two cases, both his own; rejected-then-accepted does not show every rejected direction deserves persistence [inferred] |
| Diagnostic benchmarks V*, MMVP, CV-Bench, VSI-Bench (2023-12 to 2024-12), then VSI-Super (2025-11-06), stress-tested by an independent group two weeks later (§B, M4-E12, M4-E14, M4-E19, M4-E23, M4-E24) | With far less compute than industry, a small test that exposes a real shortfall in a widely used component can reach far; a benchmark needs stress tests too [synthesized] | Which problems to pick: components everyone uses and nobody has tested (§H) | The VSI-Super dispute is unresolved as of 2026-11 (M4-E23); how a benchmark holds up under stress varies [inferred] |
| Five joint papers with LeCun (2024-01 to 2025-11), then AMI Labs (2026); on the podcast, choose collaborators over prestige (§A, M4-E14, M4-E20, M4-E23, M4-E28) | Pick the people you most want to work with over the most prestigious setting [synthesized; summary only] | His 2026 move to co-found a company with LeCun [inferred link] | Joint papers test a research collaboration; a company adds hiring, funding and product pressures [inferred] |

## Changes from the previous version

First public version, ported from an earlier private version. Facts dated 2025-07 or later were
re-checked against public sources on 2026-11-14; unconfirmed items were dropped.

Fairness-review pass (2026-11-14): §A's NYU date now says the January 2023 date is only the
announcement, not a confirmed start (independent review points to a Fall/August 2023 actual
start, not yet sourced in this pack); dropped the undated Google DeepMind role (no source dates
it, and rule 9 is that unconfirmed/undated claims are dropped, not hedged) from §A and from
`card.yaml`'s path dependence; reworded §A's "became co-founder and chief science officer" to
match §E's existing hedge (homepage says co-founder, TechCrunch says chief science officer only).
