# Persona library

> Every persona here is a simulation based on public material, not the person's own words. None
> of the people simulated has reviewed or endorsed their persona. See
> [RESPONSIBLE_USE.md](../RESPONSIBLE_USE.md).

26 personas: 20 living public figures in AI research, technology and investing, built
from their own interviews, talks, essays, papers and filings; and 6 historical figures,
built from their own public-domain writings. Each folder follows `templates/persona/`:

- `dossier.md`: sections A–I (path dependence, wins and failures, core beliefs, how the views
  evolved, interests, advice to young people, long-form notes with the range actually read, a
  mental-model card, and experience → lesson);
- `views.md`: domain views and a dated prediction record with outcomes;
- `card.yaml`: the machine-readable card the protocol reads;
- `sources.csv`: every source, with dates and limitations.

Use them in `/consult`, `/review` or `/deliberate` by name or ID. Build your own with
`/new-persona`; your own personas belong in `workspace/personas/`, which git ignores.

## Living public figures

### Capital and value

| ID | Persona | Lens | Materials through | Sources |
|---|---|---|---|---|
| [C1](C1_mauboussin/) | Michael Mauboussin | Not a technology specialist: asks first what the base rate is for a claim like this, who captures the value once competition arrives, and what the price already assumes. | 2026-09-22 | 22 |
| [C2](C2_gurley/) | Bill Gurley | Asks first whether revenue is real and who keeps the value, then whether a product changes behavior and creates new demand; reads technology waves through markets and policy. | 2026-06-04 | 37 |
| [K1](K1_khosla/) | Vinod Khosla | Starts from what technology makes possible and what becomes nearly free, and picks problems by the size of the outcome if they work; uses experts to check a founder's naivete, not to dominate decisions. | 2026-09-29 | 39 |
| [K6](K6_collison/) | Patrick Collison | Founder-and-funder lens: asks first who defines 'good' in a setting, then looks at output per person, per dollar and per experiment rather than total input or the technology itself. | 2026-10-21 | 50 |

### Platforms and cost

| ID | Persona | Lens | Materials through | Sources |
|---|---|---|---|---|
| [C3](C3_huang/) | Jensen Huang | Asks whether a problem is even possible without a different way of computing, then tracks it in energy and systems terms -- tokens per watt, joules per task -- rather than by field or architecture label. | 2026-11-12 | 39 |
| [K2](K2_dean/) | Jeff Dean | A systems engineer's lens: ask first what the dominant cost is and which quantity could change 100x, estimate the order of magnitude, then measure; the faster the experiment loop turns, the faster progress comes. | 2026-11-05 | 36 |

### Scale and verification

| ID | Persona | Lens | Materials through | Sources |
|---|---|---|---|---|
| [C4](C4_amodei/) | Dario Amodei | Treats intelligence as a scalable empirical phenomenon — asks first whether compute, data, and training time explain a gain, not whether a clever trick does — while running a company that has bet on that exact curve. | 2026-10-30 | 44 |
| [K4](K4_karpathy/) | Andrej Karpathy | Tests any technical or career question with three questions — can you build it from scratch, can you verify it, is there a data loop — and reasons on a decade timescale, unmoved by demos or benchmark scores. | 2026-10-12 | 35 |

### Experience and world models

| ID | Persona | Lens | Materials through | Sources |
|---|---|---|---|---|
| [C5](C5_levine/) | Sergey Levine | Capability gains are an information problem: new information about the world has to come from real interaction, and simulation, human video and generated trajectories reuse existing information rather than add new. | 2026-10-13 | 42 |
| [C6](C6_hassabis/) | Demis Hassabis | Judges whether a problem can be handed to AI with a three-part test -- a huge search space, a clear objective function, and data or an accurate, efficient simulator; core judgment is that generating candidates is getting cheap while credible evaluation is getting scarce. | 2026-09-29 | 25 |
| [K3](K3_sutton/) | Rich Sutton | Asks whether an agent keeps learning from its own experience, gets a right-or-wrong signal from consequences, and scales with compute rather than human-supplied knowledge. | 2026-10-06 | 40 |
| [K5](K5_lecun/) | Yann LeCun | Asks whether a result bears on what a house cat already does — predicting the physical world and planning against that prediction — and treats consensus itself as suspect until the counter-evidence is undeniable. | 2026-10-10 | 73 |

### Academia and evaluation

| ID | Persona | Lens | Materials through | Sources |
|---|---|---|---|---|
| [M1](M1_liang/) | Percy Liang | Asks first whether a claim about an AI system can be checked: what a benchmark measures, whether data, code and process can be inspected, and whether the result can be reproduced. | 2026-11-05 | 36 |
| [M3](M3_neubig/) | Graham Neubig | Asks first whether a score is reproducible and free of training-data leakage, and whether an architecture will be flattened by the next model release, before asking how clever the system is. | 2026-02-24 | 23 |

### Agents

| ID | Persona | Lens | Materials through | Sources |
|---|---|---|---|---|
| [M2](M2_yao/) | Shunyu Yao | Asks whether an evaluation tests a real capability or only a harder version of a solved task, and expects scaled language pre-training plus RL and reasoning-as-action to absorb incremental methods. | 2026-11-06 | 28 |

### Multimodal and generative

| ID | Persona | Lens | Materials through | Sources |
|---|---|---|---|---|
| [M4](M4_xie/) | Saining Xie | Visual or world representation quality, not model scale or whether an architecture is unified, limits understanding, generation and spatial reasoning; test that with small, controlled diagnostics. | 2026-03-16 | 28 |
| [M5](M5_kaiminghe/) | Kaiming He | Takes a widely held pipeline assumption, removes or replaces it, and re-measures on one clean metric at a scale one lab can run; asks whether the result holds on what was not seen, whether it scales with compute, and which hand-crafted stage is left. | 2026-10-01 | 40 |
| [M8](M8_zhujun/) | Jun Zhu | Restates a new method in probabilistic terms (a distribution with uncertainty, or a deterministic mapping?) and asks whether understanding, prediction and action form one closed loop. | 2026-10-08 | 29 |

### Spatial intelligence and robotics

| ID | Persona | Lens | Materials through | Sources |
|---|---|---|---|---|
| [M6](M6_feifeili/) | Fei-Fei Li | Asks, for any research question, whether it defines a new resource/benchmark/environment or just scores someone else's already-defined pipeline; attributes paradigm shifts to getting the resource/benchmark/environment right rather than to one clever algorithm. | 2026-09-28 | 22 |
| [M7](M7_tedrake/) | Russ Tedrake | Asks what known structure can be used first, lets learning fill what models cannot, wants capability claims tested by designs that could show them wrong, and since 2026 asks what share of a market a design covers. | 2026-08-03 | 26 |


## Historical figures

| ID | Persona | Lens | Materials through | Sources |
|---|---|---|---|---|
| [H1](H1_franklin/) | Benjamin Franklin | Tests a claim, including his own, by whether it is useful to someone else and checkable by direct experience. | 1790-03-23 | 22 |
| [H2](H2_darwin/) | Charles Darwin | Treats a claim as provisional until it survives both a specific test and years of independently gathered facts. | 1876-01-01 | 29 |
| [H3](H3_faraday/) | Michael Faraday | Tests one falsifiable guess at a time with his own hands, logged and numbered, before he lets himself believe it; refuses office or pay that would cost him the time to do that. | 1864-12-24 | 16 |
| [H4](H4_curie/) | Marie Curie | Trusts a patient, independently-checked measurement over theory or reputation, and treats scarce money and equipment as routine, not as a reason to wait. | 1923-01-01 | 24 |
| [H5](H5_lovelace/) | Ada Lovelace | Judges a mechanism, a proof or a partnership by what its defined rules could reach beyond the one case she was shown, not by the use it was first built for. | 1843-08-01 | 22 |
| [H6](H6_su_shi/) | Su Shi (苏轼) | Treats a stripped rank as a change of scenery, not a verdict: farm, build, teach, and keep writing wherever that posting lands. | 1101-01-01 | 13 |

## What to look at

- **Range actually read.** Every long text in dossier §G records whether it was read in full, in
  part, or only as a summary. Sources that refused automated access are recorded as
  inaccessible, not worked around.
- **Commonly attributed, not verified.** Each dossier lists famous lines that circulate under
  the person's name but could not be found in a primary source. None is used as `[quoted]`.
- **Track records are dated predictions, not verdicts.** `views.md` §3 lists public predictions
  with dates, outcomes and sources; the card's `trust` field only counts them.
- **Interests are dated facts.** Roles, companies and deals carry a source and an "as of" date.
  They are shown to the reader and never applied as a discount.
- **Not independent.** Personas that share an organization or a long collaboration list each
  other in `not_independent_of`; the aggregation reports them.
- **Thin materials.** Each card's `thin_materials` says where the sources ran thin.

## Limits

- A persona is a reconstruction by one model from the sources listed, as of a date. It can be
  wrong about the person. Claude is trained by Anthropic; where a simulated person works there,
  the card says so.
- Living people change their minds. Check `materials_latest_date` before relying on a persona
  for a time-sensitive question, and refresh it with `/new-persona`.
- If you are one of the people simulated here and want your persona changed or removed, open an
  issue with the Content concern template or report privately through the Security tab. We
  remove it; no reason needed.
