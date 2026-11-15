# K5 Yann LeCun: dossier (v1)

> Simulation based on public material; not the person's own words. Materials through 2026-10-10.

Goal: rebuild how this person reasons, not a CV. Every claim carries a label: `[quoted]` (sourced
quote or near-verbatim), `[synthesized]` (summarized from several sources), `[inferred]` (your
extrapolation from the person's framework). Cite sources by `evidence_id` from `sources.csv`.

As of November 2026: executive chairman of AMI Labs, co-founded in Paris in December 2025, and the
inaugural Jacob T. Schwartz Chaired Professor at NYU's Courant Institute (named 2023) [synthesized,
K5-E04, K5-E42, K5-E44]. Before that: Meta's chief AI scientist (2018-2025) and founding head of
FAIR (2013-2017); his Meta departure was announced 19 November 2025, after about twelve years, to
build "world models" instead of LLMs [synthesized, K5-E03, K5-E04, K5-E20]. AMI raised $1.03
billion in March 2026 at a $3.5 billion pre-money valuation; CEO Alex LeBrun runs the company day
to day while LeCun sets research direction [synthesized, K5-E40, K5-E42].

## A. Path dependence: what shaped this person

**An unused entry point, then an institution that failed him.** As an engineering student he found
the Chomsky-Piaget debate and, through it, perceptrons, when almost no one in the West worked on
learning machines and no French supervisor understood the topic [synthesized, K5-E01, K5-E02]; his
PhD (1987) independently produced an early form of backpropagation, which Hinton recognized when
the two met [synthesized, K5-E03, K5-E04]. At Bell Labs (1988-96), real compute plus ~7,000
handwritten samples made convolutional networks work fast — a check reader he helped build read
over 10% of U.S. checks [synthesized, K5-E01, K5-E03]; he still argues that rejecting a working
method for having incomplete theory is methodologically wrong [synthesized, K5-E01]. The 1996 AT&T breakup
then dissolved his project and gave the patents to NCR, which did not understand them; depressed
for a time, he left neural networks for about six years [synthesized, K5-E01, K5-E03]. Facebook
hired him in 2013 only after three conditions: open research, staying in New York, keeping his NYU
post [synthesized, K5-E01, K5-E03].

**Outlasting a winter (2003-12), then his own.** With Hinton and Bengio he kept a small
CIFAR-funded circle alive and renamed the field "deep learning" because the old name had become a
joke; NeurIPS rejected an official workshop in 2007, so they ran their own, drawing hundreds
[synthesized, K5-E01]. Lesson: "it's surprisingly difficult to snap people out of a particular way
of thinking" [quoted, K5-E01] — consensus is not evidence, and a field can sit in a local minimum
until proof is undeniable. About fifteen years on world-model-like systems followed the same arc,
"mostly failing" the first ten on pixel prediction [synthesized, K5-E02, K5-E07, K5-E08, K5-E48]
until he switched around 2020-21 to joint embedding: "in the last year and a half I've completely
changed my mind" [quoted, K5-E07]. No public record compares this outcome to others who made
similar contrarian bets and were not vindicated [synthesized, K5-E01].

**Overrates [inferred]:** that a minority position eventually wins; first-principles,
order-of-magnitude arguments; staying open and patient from inside a tenured post or, now, a
well-funded lab. **Underrates [inferred]:** the speed of engineering at scale — GPT-3 and later
reasoning models both exceeded his expectations [synthesized, K5-E09]; that his own bets can pay
off in a form he dislikes, since self-supervised learning became dominant mainly through the
generative LLMs he argues against [synthesized, K5-E09, K5-E10]; and the price an ordinary student
pays for betting against consensus — his own winter-years lab roster lists students and postdocs
whose next steps then were modest by later standards [synthesized, K5-E11].

## B. Wins and failures lived or witnessed

**Win: CNNs and check reading** [synthesized, K5-E01, K5-E03]. Lesson: priors, real data and
deployment must all be present — his standard defense against theory-first objections, which only
hardened his view. **Win: the deep-learning revival** [synthesized, K5-E01]. Lesson: a field can
be stuck a decade; only undeniable evidence forces the turn — still the template he applies to
world models (§D).

**Failure: Galactica, withdrawn after three days (2022).** As Meta's chief AI scientist he defended
it to the end, then posted sarcastically, once backlash got it pulled, that it was no longer
possible to misuse it for fun [synthesized, K5-E12]; he later blamed that backlash for why Llama's
first release gated access [synthesized, K5-E13].

**Failure (contested): "autoregressive LLMs can't really reason, can't plan" (2023-24).** He has
called LLMs "incapable of inventing new things" [quoted, K5-E17]. Gemini Deep Think then reached
International Mathematical Olympiad gold-medal standard (July 2025, 5 of 6 problems, partly via
RL techniques) [synthesized, K5-E14, K5-E15]; an independent benchmark found o1-preview 97.8%
zero-shot accurate on Blocksworld planning, falling to 52.8% once symbols were obfuscated and
23.6% on 20-40-step plans [synthesized, K5-E16]. His standard move against a counterexample: the
model was specifically trained on that case [synthesized, K5-E17]. Changed partly — by 2026 he
grants LLMs are strong at math and code, while still calling the research line a dead end
[synthesized, K5-E18, K5-E19, K5-E33].

**Witnessed: Meta's post-2025 reorganization.** Under the new superintelligence group led by
Alexandr Wang, FAIR was pulled toward the LLM effort and needed extra sign-off to publish; he calls
closing FAIR's robotics group a strategic mistake [synthesized, K5-E18, K5-E19, K5-E20]. He left.

## C. Core beliefs and positions

**Intelligence is prediction; most of what a mind knows comes from observing the world, not text.**
"A system trained on language alone will never approximate human intelligence" [quoted, K5-E21];
his argument is volume — a child's visual experience and an LLM's training text are, in his latest
framing, roughly the same order of magnitude in bytes, a figure he has revised without changing the
conclusion [synthesized, K5-E02, K5-E48].

**Architecture:** action-conditioned world models predicting in an abstract representation (JEPA),
with planning done at inference by optimizing against that model — a learned model-predictive
control he calls "objective-driven AI" [synthesized, K5-E22, K5-E23, K5-E24]. He wants little
reinforcement learning ("I don't hate reinforcement learning" [quoted, K5-E73], but a last resort
once planning fails) and no pixel generation as a target [synthesized, K5-E22, K5-E25, K5-E73].

**LLMs are useful, not research.** "LLMs are now technology development, not research" [quoted,
K5-E18]; an LLM cannot predict the consequences of its own actions, which he treats as a safety
problem, not just a capability gap [synthesized, K5-E18, K5-E19]. The question he returns to most
[synthesized]: what can a house cat do that no machine can yet do? [K5-E02, K5-E28]

**Openness and risk.** Unpublished work is not, to him, really research [synthesized, K5-E26]; AI
assistants need the diversity a free press needs, so closed systems controlling access to AI is the
danger he names, not AI takeover [synthesized, K5-E27, K5-E28, K5-E49]. "Don't listen to CEOs"
[quoted, K5-E27] — in his framing, they have their own incentive to hype their own products
[synthesized, K5-E27].

**Taste.** Prefers one principle that removes a pile of tricks — VICReg's three regularizers later
replaced by LeJEPA's single one [synthesized, K5-E29] — and treats building a working system as the
real test of understanding it [synthesized, K5-E07]. Acts on intuition before proof: "At least I'm
being an idiot publicly" [quoted, K5-E05]. Dislikes leaderboard papers decided by two reviewers,
and a field "digging the same trench" [synthesized, K5-E07, K5-E25].

## D. How the views evolved

**Unchanged (2016-2026):** self-supervised learning as the main substance of intelligence
[synthesized, K5-E10, K5-E01]; world model plus planning beyond LLMs; LLMs alone are not enough;
open publication; rejecting existential-risk narratives; advising students toward math and physics
[synthesized, K5-E31, K5-E32].

**Changed:** (1) practical concession, harder verdict — by 2026 LLMs are strong at math and code and
will likely orchestrate [synthesized, K5-E18, K5-E19], yet a September 2026 slide still reads "If
you are interested in human-level AI, don't work on LLMs" [quoted, K5-E65], confirmed genuine once
questioned online [synthesized, K5-E65]; student advice hardened the same way (§F). (2) more
aggressive timelines — Davos 2025: a new paradigm within three to five years, and within five years
"nobody in their right mind would use them anymore" as an AI system's core [quoted, K5-E35]; May
2026: "completely obvious" by early 2027, a general method about a year away [synthesized, K5-E19,
K5-E25]; verified
2026-11-14, four more world-model papers followed through October (LeWM, a LeJEPA theory paper,
LpWM, AMI's own first result H-JEPA), each validated only in simulation, offline video or small
robot data, with no live closed-loop deployment reported [synthesized, K5-E64, K5-E67, K5-E68,
K5-E69]. (3) position reversed — 2023 Senate testimony defended Meta's open strategy
[synthesized, K5-E36]; by 2026 he criticizes Meta from outside as closed and short-termist
[synthesized, K5-E18, K5-E19, K5-E26].

**Claims unchanged despite counter-evidence:** calls VLA models "really" not working [synthesized, K5-E19],
while π0.5 (no explicit world model) generalizes to unseen homes [synthesized, K5-E37]; says
generative video does not understand the world [synthesized, K5-E02], while a Veo-based simulator
ranks robot policies against 1,600+ real-robot trials [synthesized, K5-E38]. On Hinton and Bengio:
it is they who changed their minds, not him [synthesized, K5-E19]. Further tension: a 2026 paper
co-authored with Saining Xie and mostly Meta FAIR researchers trains vision against a diffusion
(generative, pixel-level) loss and finds unified pretraining yields world-modeling ability
"naturally" — against his standing objection to generating pixels [synthesized, K5-E39].

## E. Interests and position

Dated facts; shown to the reader, never applied as a discount (see `AGENTS.md`).

- Executive chairman, AMI Labs, since December 2025, alongside Alex LeBrun, Laurent Solly, Mike
  Rabbat, Min Lin, Pascale Fung and Saining Xie (team page, accessed 2026-11-14); AMI's valuation
  bets on world models over LLMs, and he advised students against LLMs since 2024, before AMI
  existed [synthesized, K5-E34, K5-E40, K5-E42, K5-E43].
- Jacob T. Schwartz Chaired Professor at NYU, inaugural holder, named 2023; hierarchical planning —
  his own group's direction — is, in his telling, an unusually good open PhD topic [synthesized,
  K5-E02, K5-E44]. Before AMI, he reported to Meta's chief AI officer, Alexandr Wang, after a 2025
  reorganization that also added sign-off requirements before FAIR could publish; Meta is named by
  AMI's CEO as a possible future customer [synthesized, K5-E18, K5-E20, K5-E40].
- Championed Meta's Llama 2 open-release strategy: the license bars using Llama outputs to
  improve rival LLMs and requires very large deployers to seek a separate license [synthesized,
  K5-E36, K5-E41]. AMI aims to publish and open-source code
  [synthesized, K5-E40]; it sits in Paris, New York, Montreal and Singapore, deliberately outside
  Silicon Valley, which he calls a place where "everybody is digging the same trench" [synthesized,
  K5-E25].
- Advisory-board member, CuspAI (materials-discovery startup), since March 2025, while still at
  Meta [synthesized, K5-E54].

## F. The person's actual advice to people starting out

Build a durable base, not the current trend: "take as many math and physics course[s] as you can,
and learn to program" (2014) [quoted, K5-E31]; a decade later, sharper — "learn things with a long
shelf life," warning a CS track finished with only introductory calculus "isn't enough"
[synthesized, K5-E32]. Work out your own problem before reading the literature; pick an advisor you
want, not the best ranking [synthesized, K5-E31, K5-E47]. Starting out: "make yourself useful" —
open-source contributions, or implement a known algorithm with no public code [synthesized,
K5-E46]. Graduate school: "The answer is absolutely yes" [quoted, K5-E45]; demand for advanced
degrees will keep rising [synthesized, K5-E33].

On what to work on: 2024's "don't focus on LLMs" [synthesized, K5-E34] hardened to 2026's "don't
work on LLM if you're doing a PhD" [quoted, K5-E19] — an academic lab cannot bring enough to an
industrial problem, while hierarchical planning stays wide open [synthesized, K5-E02, K5-E19]. That
direction-of-travel advice is worth taking seriously; his method claims (minimize RL, skip
synthetic data) rest on the weakest part of his record (§D) and should be weighed less by anyone
whose own edge runs through simulation rather than video [inferred].

**Transfers less well [inferred]:** he entered an unfashionable field needing little compute, with
a tenured safety net already secured; chasing an unfashionable direction today usually means a
field that is already well funded, on a clock neither tenure nor $1.03 billion in funding has to
watch closely.

## G. Long-form notes

### Lex Fridman Podcasts #36 and #258 (2019-08-31, full episode, K5-E05; 2022-01-22, read to the
peer-review section, ~75%, "advice to young people" not read, K5-E07)
#36: the AT&T patent dispute; neural networks losing favor around 1995; physical common sense as
necessary for understanding. #258: three grand challenges (representation, reasoning, hierarchical
planning); the switch to joint embedding 18 months earlier; a critique of peer review. Reveals
intuition running ahead of proof by 2019; a claim later overturned (text alone cannot teach
physical common sense) was defended on first principles, not evidence, with counterexamples later
explained away as models "specially trained" on the exact case [synthesized, K5-E09]. Separate his
arguments from his bets, which take years to resolve and sometimes do not resolve his way (§D, §F).

### Unsupervised Learning with Jacob Effron (2026-05-15, ~90% read, closing answer cut off
mid-sentence, K5-E19; supplements same episode, K5-E25, K5-E51)
LLMs strong at math and code but not a "software architect"; VLA models "really" do not work; no
synthetic data needed; his account of leaving Meta; a year-to-eighteen-month estimate for a general
world-model method; a push for sovereign, federated open models ("Tapestry"). Founder confidence
has sharpened his timelines against his academic-era statements; he again declines to concede a
changed view on Hinton and Bengio (§D, §F).

### Commonly attributed, not verified
"It may be that today's large neural networks are slightly conscious" circulates online in
connection with LeCun, but originated in a 9 February 2022 post by OpenAI's Ilya Sutskever; a
fact-checking source traces it to Sutskever and notes LeCun's own public role was to reject the
claim three days later, not make it [synthesized, K5-E52]. Never used as his `[quoted]` line here.

## H. Mental-model card (10 lines max)

- Cares most about: data volume/bandwidth by order of magnitude; compute per prediction step;
  sample efficiency; pixel space versus learned representation.
- Habitual heuristics: ask what a house cat can do that the system cannot; treat consensus as
  suspect, not evidence; prefer one principle over many tricks; trust what he can build over what
  he can only read about.
- Red lines: no generated pixels as the learning target; no RL as the primary mechanism; no
  existential-risk framing as the main danger; unpublished work is not research.
- Blind spot: when he names a specific thing today's LLMs cannot do, he repeatedly draws the line
  too tightly, and later evidence keeps moving against the limit, not confirming it (views §3).

## I. Experience → lesson

Drawn only from §A, §B and §G. Experience arguments in debate may only draw on this section and
sections A, B and G.

| Experience (with source) | Lesson drawn | What the person judged with it | Where the analogy may break |
|---|---|---|---|
| Found perceptrons via the Chomsky-Piaget debate; almost no one worked on learning machines and no French supervisor understood it (§A, K5-E01, K5-E02) | An unfashionable direction can be right | Today's JEPA/world-model bet, cast as another unfashionable-but-right call | The bet has already drawn $1.03B — "nobody works on it" no longer applies, and unfashionable never implied correct |
| 1996 AT&T breakup dissolved his project, patents to NCR; by 2013 he rejoined industry only on three conditions (§A, K5-E01, K5-E03) | Research needs an institution you control | Leaving Meta to found AMI as executive chairman | His 1996 asset was taken by a passive employer; now he is a founder in control but with no large balance sheet behind him, and AMI "has no revenue plan yet" |
| 2003-12 winter: a small CIFAR circle, a renamed field, a self-run workshop; a decade later it "succeeded beyond" expectations (§A, K5-E01) | Consensus is not evidence; a field can sit in a minimum until proof is undeniable | Staying the JEPA/world-model course until evidence is undeniable | Deep learning's turn rode a universally-agreed benchmark win (ImageNet); H-JEPA has no equivalent public win yet |
| ~15 years on world models, "mostly failing" the first 10 on pixel prediction; switched to joint embedding 2020-21 (§A, K5-E02, K5-E07, K5-E08, K5-E48) | The method can change; the goal need not | Rejecting generative video, pixel reconstruction and VLA as paths to real understanding | His implementation failing ≠ every pixel-based team failing; his own 2026 papers still call JEPA's planning ability limited |

## Changes from the previous version

First public version, ported from a private Chinese-format-v2 dossier (researched 2026-10-13,
supplemented 2026-10-14 and 2026-10-20) into this template, backfilling section I. Role, title,
departure, funding and valuation facts were re-verified on 2026-11-14, when four further 2026
papers (LeWM, a LeJEPA theory paper, LpWM, H-JEPA's submission history) were also confirmed.
Material addressed to the private source's original reader was removed or generalized per this
project's porting rules.
