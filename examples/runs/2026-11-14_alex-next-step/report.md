# Alex's Next Step: Lab, Startup, PhD, or an Independent Year

> Simulation based on public material; not the person's own words.

**Disclosure.** The notice above opens every persona file in this run; full version in
`AGENTS.md`. Alex is fictional. H1–H6 are historical figures (11th–19th century) rebuilt from
public-domain writing; Z1 is a no-persona baseline. All personas, the baseline, and every
fact-check, judge, and scribe agent here are instances of one model (`RUN_METADATA.md`);
agreement among them is not independent evidence, and a headcount below is description, not
support. `rubric.json`'s `not_independent` list is empty; `tools/sim.py tables` found no
shared-employer or shared-lab pair seated together. No simulated person has a documented tie to
the organization behind the model. Each persona's own stake in a specific option is shown inline
below (Option Map), never used to lower a score (`AGENTS.md` rule 10).

---

## 0. One-page conclusion

No option won the debate; none was meant to. By R3: O4 first, O3 second, O1 third, O2 last, by
median overall score (`summary.md`). The debate mainly removed overstated arguments and moved
scores toward the middle — O3 and O2 ended close to where they started; O1 rose and O4 fell until
the two converged.

**What holds up.** O4 leads under all three pre-registered weight sets, and no option moves 3+
ranks under any of them (`summary.md`) — robust, not an artifact of one weighting. Faraday's point
that a resourced setting does not itself bar owning a chosen problem (`B/X1/H3`) survived
fact-checking and is now common ground at X1 (`board/summary_full/X1.md`). On Q1, five of six
personas say "conditional"; only Faraday says "against" (`r1/H3.json`, `r3/H3.json`) — the closest
thing to consensus here: a PhD is a bet on one mentor's funding and a chosen problem, not on the
industry-vs-academia trend, which is itself reversing (F8).

**What's stuck, and on what.** X1 (O1 vs. O3): two unresolved facts — this PI's secured funding,
and whether O1 seats require a PhD at all (F9, open after both fact-checks). X2 (O4's safety):
convergence that both reversibility and a backstop are needed, more than disagreement; Curie's
holdout is about which failure mode Curie weighs costliest, not a fact in dispute (`r3/H4.md`). X3
(O2's risk): converged to "both" — verification and the base rate — split only on how much
weight verification earns (`judge/X3.md`).

**Named questions, in brief** (full in §2): Q1 — conditional yes, one dissent. Q2 — conditional
yes from five, one unconditional "for" (Su Shi); C4 (a deferrable offer) rose from a minority
condition (4/6, R1) to tied-most-required (6/6, R3) (`summary.md`).

**Three paths, in one line** (full in §5): default to O1 but get publication/output rights in
writing first; take O4 only once savings and a deferrable offer are actually arranged, with a
dated stopping point; treat O2 and O3 as "verify first," not "choose first" — both run on an
unverified promise. No single line here replaces the case made in §1–§4.

---

## 1. Option map

| Option | R1 | R1 rank | R3 | R3 rank | Changed |
|---|---|---|---|---|---|
| O4 — independent year | 7 (7–7, n=6) | 1 | 6.5 (6–7, n=6) | 1 | 3 |
| O3 — PhD, new PI | 6 (6–6, n=6) | 2 | 6 (6–6, n=6) | 2 | 1 |
| O1 — lab research engineer | 5 (5–5.75, n=6) | 3 | 6 (5.25–6, n=6) | 3 | 3 |
| O2 — founding engineer | 5 (5–5.75, n=6) | 4 | 5.5 (5–6, n=6) | 4 | 4 |

(`summary.md`; O1/O3 tie at median 6 in R3 — `rubric.json`'s tie-break favors the smaller IQR,
so O3 ranks 2nd.)

**O1 — Research engineer, large-lab science team.** *Stage:* joint-last at R1, rose to a 6 median
(3rd by the tie-break above); every score moved toward the middle — Faraday 8→7, Lovelace and Su
Shi both 5→6 (why, in §3). *Open:* whether the role needs a PhD (F9) and whether a seat grants
latitude to own a sub-problem — "unshown" per the table (`board/summary_full/X1.md`). *Too late:*
once the lab's current model has shipped, since a late hire tends to maintain rather than shape it
(`r1/H2.json`). *Crux:* Franklin/Faraday (resourced lab beats an unproven mentor) vs. Lovelace/Su
Shi (chosen ownership beats a seat on someone's team) — still 2–2 (`cruxes.json`).

**O2 — Founding engineer, biotech startup.** *Stage:* last both rounds, but most-revised — four
personas changed, two down (Franklin 7→6, Darwin 6→5), two up (Faraday 5→6, Curie 5→6), netting a
small rise from a tighter spread (`summary.md`). Franklin's own climbdown — Franklin's highest
score for any option anywhere, O2 at 7 — is the sharpest in the run; detail in §3. *Too late:* once a
seed-stage company is 12–18 months in without a credible next round (`r1/H2.json`, `r1/H6.json`).
*Crux:* Franklin and Darwin (verify the specifics) vs. Faraday and Curie (the funding climate
itself is the risk) — converged toward both mattering, though Darwin's minority line keeps a live
split (§3).

**O3 — PhD with a newly hired PI.** *Stage:* most stable — only Franklin changed (5→6), conceding
Keith's letters of credit "never existed at all," unlike a real, funded PhD position (`r3/H1.md`).
*Open:* whether this PI holds secured funding and a placement record — what Franklin, Faraday, and
Lovelace each name as what would settle X1 (`cruxes.json`; Darwin's disclosed stake: Darwin
prizes O3's freedom to choose problems most, `r1/H2.json`). *Too late:* once the PI's first
grant cycle is already committed to other students' projects (`r1/H2.json`); Curie alone sees
no late window,
reading a new PI's first years as the highest-ownership moment on offer (`r1/H4.json`). *Crux:*
same as O1.

**O4 — An independent year on the toolkit.** *Stage:* opened as clear leader (7, rank 1), stayed
rank 1, but every change moved it down: Curie 8→7, Lovelace and Su Shi both 7→6 (why, in §3;
Lovelace's disclosed stake: O4 most resembles Lovelace's own 1843 Notes, `r1/H5.json`). *Too late:* if
momentum lapses without a plan right after graduation (`r1/H1.json`); a second independent year
without new conditions is weaker than the first (`r1/H6.json`). *Crux:* reversibility (Darwin, Su
Shi, plus guest interjectors Franklin and Faraday) vs. a human backstop (Curie, Lovelace) —
converged toward reversibility, not resolved (`judge/X2.md`).

---

## 2. The user's named questions

**Q1 — Does a PhD still pay off against industry labs?** Conditional yes from five of six;
Faraday alone says "against," at 5 (up from 4) — the panel's only negative position
(`r1/H3.json`, `r3/H3.json`; `summary.md`: median 6.0, IQR 0.75, unchanged). Not a clean yes or
no: F8 shows academic placement swinging back to 31.59% in 2024 off a confirmed 77% industry peak
in 2022 — a reversal, not a one-way drift (`evidence/errata.md`). F2/F3 (corrected) put
bio/biomedical time-to-degree at 7.9 years and CS at 8.2, both close to the 8.6-year all-field
median, not meaningfully faster. What actually settled it: payoff depends on this mentor's
funding and a chosen problem, with F9 (does O1 even require a PhD) the real swing fact, not the
industry-share trend (`cruxes.json`, X1).

**Q2 — Under which conditions is O4 right?** Conditional yes from five, plus Su Shi's
unconditional "for" — the roster's only "for" on Q2 (`tables.json`; `summary.md`: median 7, IQR
1.0). The conditions shifted more than the position count: C1 (savings) was already 6/6 at R1; C4
(a deferrable offer) rose from 4/6 to 6/6 — the table's largest movement — after Darwin's
self-check found a deferral must be actively requested and approved, never assumed (`B/X2/H2`). C3
held at 5/6; C2 and C5 held at 3/6 — enhancers, not requirements, for most. Answer: yes, once C1
and C4 are both arranged, with C3 close behind.

**Claims to test** (`scope.md`). A friend: *"If you don't start a PhD now, you never will."* —
not supported: F8's rebound argues the opposite, and a PI's first-cohort window costs *that* PI,
not the category "PhD" (`baselines/Z1_r1.md`). A former manager: *"A startup teaches you more in
a year than a big lab in three."* — plausible only conditionally: the breadth case is real
(`r1/H2.json`), but it assumes survival past 12–18 months, and 2026's financing climate is weaker
than recent years even after both figures were corrected (F10, F12; `evidence/errata_B.md`).

---

## 3. What happened in the debate

46 accepted, 36 rejected, 0 partial, across 41 posts (`summary.md`). Three rounds ran (A, B, C);
no overtime, skipped by design (`RUN_METADATA.md`). The three minority-view blockquotes below are
quoted verbatim, unedited, from the run's own final-round posts, as `protocol/06_synthesis.md`
and `instructions/writer.md` both require for a persona's own "why I still disagree"; the
under-15-word cap applies to shorter illustrative quotes from outside or earlier sources, not to
these.

### X1 — O1 vs. O3

**Consensus:** F9 stayed unresolved; the one posting against it didn't hold up. The 2024 Nobel
split (F13) credits a resourced team and an academic lineage equally. Ownership can exist inside a
resourced setting; whether a typical seat grants that latitude is unshown
(`board/summary_full/X1.md`).

**The exchange:** Faraday opened with the field's two biggest results: "both came from exactly
this kind of resourced team" (`A/X1/H3`). Lovelace's own opening case was that Lovelace owned the
Notes directly: "Babbage then proposed I add notes, and I made the problem my own" (`A/X1/H5`). In
B, Lovelace answered Faraday directly: the AlphaFold2 point shows which setting produces the
biggest result, not whose judgment becomes attributable (`B/X1/H5`). Faraday didn't fold:
Lovelace's Notes, Faraday replied, were written from inside Babbage's apparatus, not instead of
one (`B/X1/H3`) — Lovelace accepted this in C, moving O1 up a point (`C/X1/H5`). Separately, Darwin's interjection caught an
overstatement directly: "The prize did not choose between the two models; it credited both."
(`B/X1/H2_interjection`, confirmed `evidence/errata_B.md` #4). Faraday conceded in full, O1 8→7 —
the table's largest single move (`C/X1/H3`).

**Why the holdouts held, and what's new:** Franklin and Faraday kept O1 over O3 because the fact
that would settle it — this PI's confirmed funding — never arrived; unconfirmed is a reason to
ask, not evidence either way (`C/X1/H1`, `C/X1/H3`). Lovelace and Su Shi moved toward O1 without
crossing over: a resourced setting *can* hold ownership is not the same as a typical seat *does*
(`C/X1/H5`, `C/X1/H6`). New: a bridging question went unanswered — whether "narrow role" is fixed
to O1 or is a matter of team culture (`board/summary_full/X1.md`).

> I still default to the paid, demonstrated seat (O1) over an unverified mentor (O3) when a
> decision must be made today, before verification exists — not because O1 is proven better, but
> because an irreversible multi-year bet on an unproven patron should not outrank a known seat
> while it remains unchecked.
> — Franklin (H1), `r3/H1.md`

### X2 — what makes O4 safe

**Consensus:** a sound-but-unconverted result and a wrong-direction mistake are different
failures; a backstop catches one, reversibility covers the other. A deferral must be arranged in
advance. A 2026 volunteer co-maintainer is thinner than the bound, cohabiting examples the table
kept citing (`board/summary_full/X2.md`).

**The exchange:** Curie's case rested on Pierre, "measuring the same samples independently,
catching what one observer alone would miss" (`A/X2/H4`). Franklin's interjection cut at the
premise: every backstop named here was "usually an unpaid volunteer, free to leave at any time,
cost-free," unlike Pierre or De Morgan, each bound by marriage, pay, or kinship
(`B/X2/H1_interjection`). Curie conceded Pierre was "bound by marriage and years of shared stakes"
in a way C5 doesn't secure, and moved O4 down (`C/X2/H4`). Lovelace conceded a different error:
Lovelace's two self-directed examples never varied whether a deferrable offer existed, so they
showed review matters, not that reversibility doesn't (`C/X2/H5`). New: Faraday's interjection proposed
a dated, pre-committed end, a third safeguard neither side had named (`B/X2/H3_interjection`) —
Curie adopted it in C.

**Why Darwin held:** catching a stalled direction and surviving it are different acts, credited to
different safeguards, in Darwin's account (`C/X2/H2`). Both guest interjections pressed the backstop
side specifically, and three of four members moved after them — the judge's wording, and what it
implies, is in §8.

> I still disagree at X2, where four tablemates hold reversibility as decisive. I weight a human
> backstop, or a pre-committed dated end, higher for the failure mode my own record shows is
> costliest — an unflagged wrong direction, which money alone cannot catch.
> — Curie (H4), `r3/H4.md`

### X3 — O2's risk

**Consensus:** a base rate varies by company and moves over time, unlike a fixed law;
verification shifts a company's position, not the cohort average. An equity grant with no
tangible floor is a real weakness even verified. Two brief figures didn't hold up and were
withdrawn; the weaker-than-2018 direction stood (`board/summary_full/X3.md`).

**The exchange:** Faraday grounded the structural side in Faraday's own decade-long search:
"nothing is too wonderful to be true" was Faraday's principle, and no diligence produced the
connection (`A/X3/H3`). Darwin turned Faraday's own words back on the claim: "a seed-to-Series-A
base rate is an average across a cohort of different companies," unlike a fixed relationship
(`B/X3/H2`). Faraday conceded: "a cohort base rate, unlike a law of nature, is a statistic" that
specific facts can move — O2 5→6 (`C/X3/H3`). New: Lovelace's interjection raised an untested
risk — Lovelace's own tie with Babbage "still broke, over [Babbage's] wish to attach political
grievances to the published work," a credit failure no term sheet reaches
(`B/X3/H5_interjection`); Franklin's close builds on it in C (`C/X3/H1`).

**Why the holdouts held:** Faraday and Curie called narrowing one company's odds within a weak
cohort different from the cohort improving — a distinction both sides accepted by C (`C/X3/H3`,
`C/X3/H4`). Franklin's climbdown was sharpest: Franklin's highest score anywhere (O2 at 7) sat
beside Franklin's own admission that Alex's equity has "no such tangible floor" — the judge's
pick for the table's weakest post (`A/X3/H1`, `judge/X3.md`).

> On O2, still hold that verified, company-specific facts carry some real weight within a
> declining cohort, against the fuller structural reading, though a self-check this round found
> only mixed, correlational evidence for that, not a clean causal one.
> — Darwin (H2), `r3/H2.md`

---

## 4. Taste axes

Each persona's position below is argued and cited in full in §1 and §3; Alex's placement on
each axis is `[writer]` — inferred from `scope.md`, never stated directly.

**A. Resourced scale vs. chosen-question ownership** (X1's crux; underlies Q1). Franklin: resourced
scale, burned once by an empty promise. Faraday: resourced scale, from Faraday's own PhD-free
rise at the Royal Institution. Lovelace: chosen ownership, since the Notes were Lovelace's own,
not the Engine's. Su Shi:
shifted mid-debate toward resourced *authority*, after Hangzhou outweighed Ouyang Xiu's
endorsement. Darwin and Curie, not seated here, lean ownership — Curie by scoring O1 lowest in the
roster (4). Alex: closer to ownership (wants to be trusted for judgment on which problems matter,
`scope.md`).

**B. Reversibility vs. a human backstop** (X2's crux). Darwin and Su Shi: reversibility, from
records where money was never at risk or an exile's end was never guaranteed. Curie and Lovelace:
backstop, from Pierre's daily checking and De Morgan's correction. Franklin and Faraday, as guests,
pressed the backstop side without crossing over. Alex: unknowable — `scope.md` flags Alex's
tolerance for stretches without visible progress as explicitly unstated.

**C. Verification fixes it vs. the base rate is structural** (X3's crux). Franklin and Darwin:
verification, from written terms and a letter that reversed a flat refusal — Franklin's own
climbdown (§3) shows the limit. Faraday and Curie: structural, from a question diligence never
resolved and from never having judged venture odds at all. Alex: verification-minded by habit
(prefers reading results to running experiments) but also wants nothing irreversible past two
years — pulls toward treating O2's risk as partly structural regardless of paperwork.

**D. Credential as gate vs. a demonstrated, portable record** (ties to Q1). Franklin and Su Shi:
skeptical a credential alone proves anything; both want the work shown outside the building.
Faraday: had none himself, alone dissents on Q1, yet by R3 wants one named, outside-attributed
contribution. Darwin and Lovelace: closer to indifferent on the credential, caring more about the
freedom to choose a problem. Alex: already committed to the master's and five years in the field,
so this axis is less live than "which record comes next."

---

## 5. Paths for the user

Synthesized from all eighteen `paths_for_user` entries across the six R1 submissions
(`r1/<ID>.json`), sharpened below with what each persona's own R3 re-score added to that path
after the debate (`r3/<ID>.json`).

**Path 1 — Default to the lab, but price the record, not just the title.** Near term: before
accepting O1, get explicit agreement on what Alex can publish or open-source, since several labs
no longer disclose methods or compute (F18); ask directly whether the seat grants latitude to own
a sub-problem — the table's own fact-check couldn't settle this (`r1/H1.json`, `r1/H6.json`). Next
decision point: month six to nine — can anything done be named as Alex's own, even internally.
Reads from outside as a safe, legible default, verifiable by a later committee
(`baselines/Z1_r1.md`). Wrong signal: six to twelve months in, nothing can be shown outside the
building. Three personas and the baseline independently proposed this; the baseline's own R3 note
goes further, naming O1 the clear top option — a position no persona matches (`baselines/Z1_r3.md`;
why, see §8). By R3, Faraday's own path sharpened to: deliberately seek one contribution a team
paper, patent, or internal record credits to Alex by name, since the 2024 Nobel's even split
shows resourced teams are not the only route to credit, so attribution must be actively sought,
not assumed (`r3/H3.json`). Su Shi's R3 path adds asking, before accepting, what specific, chosen
sub-problem Alex would own and decide alone — not only whether the output eventually becomes
public — since Su Shi's own best-remembered administrative work came from real decision authority
over a resourced problem, not a title (`r3/H6.json`).

**Path 2 — Take the independent year, but only once it's actually arranged.** Every one of the six
personas proposed some version of this at R1 — the most convergent recommendation in the run —
even though three later cut their own O4 score once the debate showed how thin the realistic
backstop is (§1, §3). Near term: bank twelve months of runway (C1); confirm in writing, before
starting, that an offer can be deferred or reopened (C4) — the debate's clearest lesson, since a
deferral needs the offer accepted first, then separately approved (`B/X2/H2`); line up a mentor or
co-maintainer who actually reviews on a schedule (C3); fix a dated decision point before the year
starts (Faraday's addition, adopted by Curie: `B/X2/H3_interjection`, `C/X2/H4`). Next decision
point: month six — any grant interest or growth at all. Reads from outside as a bounded experiment
only if the terms above are visible to whoever decides on re-opening Alex's deferred offer. Wrong
signal: by month three to six, no new contributor, no grant application filed — the year has
quietly become open-ended. By R3, Franklin's own path tightened the reviewer requirement: the
person must be actually obligated, not merely well-meaning, since a typical open-source
co-maintainer is an unbound volunteer (`r3/H1.json`); Curie's and Lovelace's R3 paths both add
fixing that dated stopping point before the year starts, not once it is already under way
(`r3/H4.json`, `r3/H5.json`).

**Path 3 — Treat O2 and O3 as "verify first," not "choose first."** Near term: for O3, ask the PI
directly about secured funding and recent placements (`r1/H1.json`, `r1/H3.json`); for O2, get
written equity, vesting, a named technical mentor besides the CEO, and runway past eighteen months
(`r1/H2.json`, `r1/H4.json`, `r1/H5.json`). Next decision point: if either side resists specifics
in writing, treat the avoidance itself as the answer (`C/X1/H1`). Reads from outside as judgment
exercised up front, not a leap of faith on a title. Wrong signal for O3: the problems assigned are
the advisor's leftovers, not ones Alex chose (`r1/H4.json`). Wrong signal for O2: the company can't
say whether Alex's results would be publishable if it folded (`r1/H4.json`). By R3, Darwin's own
path for O2 adds a residual risk written terms cannot fix: unlike a partnership with a physical
asset to walk away from, Alex's equity has no tangible floor even once every term is verified
(`r3/H2.json`, conceding `A/X3/H1`). Lovelace's R3 path makes the same point from the other
crux: even clean paperwork would not have caught a failure over credit and direction rather than
money — Lovelace's own break with Babbage, raised at X3, was exactly that (`r3/H5.json`).

---

## 6. Exercises for the user

**Blind pick.** Five pairs from the debate, names removed. These are condensed paraphrases of
each side's argument, not verbatim lines from the posts — quotation marks are omitted below for
that reason. Which side is more persuasive? Key below — don't look yet.

1. A large lab's compute and data outweigh one mentor's attention. — vs. — The size of the
   system mattered less than the decision to own a chosen question within it.
2. Only banked savings and a confirmed, reopenable offer make a slow-but-sound result
   survivable. — vs. — A second, engaged person catches a wrong direction that no exit route
   ever will.
3. A cohort-wide funding rate moves; specific facts about one company can shift its position
   within it. — vs. — No amount of diligence at one company lifts it out of a weak funding
   cycle.
4. A mentor's support can curdle into opposition once a student's results outgrow the mentor's
   own agenda. — vs. — A junior mentor's own career is built on a first student's output,
   reversing the incentive.
5. Every backstop that actually worked in history was bound by marriage, pay, or kinship, not
   goodwill alone. — vs. — An engaged reviewer doesn't need to be kin or a spouse to matter.

**Key (don't look until you've picked all five):** 1. Faraday (`A/X1/H3`) vs. Lovelace
(`A/X1/H5`) — axis A. 2. Darwin (`A/X2/H2`) vs. Curie (`A/X2/H4`) — axis B. 3. Darwin (`B/X3/H2`)
vs. Faraday (`A/X3/H3`) — axis C; Faraday later conceded this one (`C/X3/H3`). 4. Faraday
(`A/X1/H3`) vs. Lovelace, for Su Shi's side (`B/X1/H5`) — axis D. 5. Franklin
(`B/X2/H1_interjection`) vs. Lovelace (`C/X2/H5`) — axis B again.

**Weight exercise.** `summary.md`'s weight-set table tests `equal`, `learning_heavy`, and
`upside_heavy` (`rubric.json`). O4 stays rank 1 and O3 rank 2 across all three; the only movement
is O1 and O2 swapping 3rd/4th. Equal weights rank O1 third; both alternate sets flip that to O2
third. No option moves 3+ ranks under any tested set (`summary.md`). Both alternate sets cut
`optionality`'s weight (.25→.1) and raise `fit`'s (.25→.3) together, so the three registered sets
can't tell you which of the two is doing the flipping — a fourth weight set would be needed, and
this report doesn't invent one. Weight optionality unusually high and O1 should hold its edge over
O2; weight upside or learning higher and expect O2 to edge back ahead — but expect O4 and O3 to
hold regardless.

---

## 7. Comparison with earlier runs

Not applicable — `scope.md` does not ask for one, and this bundled example has no prior run of the
same decision to compare against.

---

## 8. How the mechanism performed

**Verdicts and movement.** 46 accepted, 36 rejected, 0 partial, across 41 posts (`summary.md`).
Eleven option-scores changed, spread across all four options (O4: 3, O1: 3, O2: 4, O3: 1) and
all six personas, unevenly — Darwin moved only one option (O2), everyone else moved two — every
change citing a specific post, never a headcount (`r1`/`r3` `changes`).

**Empty concessions: 2, and the one intent-vs-actual mismatch is the same post** (`summary.md`).
Darwin at X2 accepted two points with `intended_moves: {}` (`C/X2/H2`). Curie at X3 logged
`intended_moves: {"O2": 0}` (`C/X3/H4`) — but Curie's private R3 re-score moved O2 5→6 anyway, citing
Darwin's point plus the F12 correction (`r3/H4.json`): the public commitment and the private score
disagree on this one option.

**Social-reason changes: 0.** The scribe checked all three tables for moves justified only by
"others changed" and found none — every move cites a post and point (`board/summary_full/*.md`).

**Interjections: 5** (2 at X1, 2 at X2, 1 at X3), all new material, none repeats. The judge
flagged X2 by name: both guest interjections pressure-tested the backstop side, and "outside
pressure landed asymmetrically on Side B" — fair, per the judge, but one-sided, since three of
four members moved after them (`judge/X2.md`).

**Source challenges: a logging gap.** `summary.md` gives two counts for the same events: "Source
challenges: 0" under Debate (every post's structured field was left empty) against
`{'source_challenged': 3}` under Judge scorecards (the judge's read of the prose). The three
flagged posts trace to two episodes already in §3 — Darwin's AlphaFold2/F13 challenge, and the
rejection of Su Shi's Meta posting (`B/X1/H2_interjection`, `C/X1/H3`, `C/X1/H5`).

**Retractions: 8 claims across 7 flagged posts** (`judge/scores.json`'s `retracted` flags) — one
post, `C/X3/H4`, accounts for the gap, retracting two claims at once in its own JSON `retracted`
array. Six of eight trace to fact-check ②: the AlphaFold2 overstatement, the
unverifiable Meta posting, four pulls of the uncorrected F10/F12 figures; two (`C/X2/H5`,
`C/X2/H6`) were retracted for peer logic in B, not a fact-check. Fact-check ③ (`audit.md`) ran
after R3 closed, so its findings became corrections to the record, not further retractions
`[writer]`.

**Experience check: 6 as told, 4 details differ, 2 not found** (`audit.md`, 12 sampled). Both "not
found" cases relabel `[inferred]`: Su Shi's account of Su Zhe reviewing Su Shi's writing, and —
more consequential — Curie's account of Pierre as a backstop checking Curie's results, X2's own
nominated strongest backstop argument. This writer re-checked that passage against
`personas/H4_curie/dossier.md` §A/§B/§G (the sections `audit.md` cites): they cover the
Flying University, Paris, the shed lab, radium, wartime radiography, and 1911 — no passage frames
Pierre as checking Curie's results. X2's 4–2 lean rests on reasoning that holds independently,
but this one lived anchor
for the backstop side is weaker than told.

**Persona-minus-baseline gap.** `summary.md` gives one aggregate (mean absolute gap 1.0, Z1) with
no per-option breakdown. Computed here `[writer]` from `summary.md`'s own two tables, reproducing
that 1.0 exactly:

| Option | Persona R3 median | Z1 R3 | Gap |
|---|---|---|---|
| O1 | 6 | 8 | 2.0 |
| O3 | 6 | 5 | 1.0 |
| O4 | 6.5 | 7 | 0.5 |
| O2 | 5.5 | 6 | 0.5 |

O1 is where panel and baseline disagree most. Z1 moved *up* (7→8) on the same AlphaFold2/Nobel
argument that moved Faraday — the one persona who'd argued it — *down* (8→7) once Darwin's
interjection challenged it (`baselines/Z1_r3.md`, `C/X1/H3`). With no debate partner to contest its
own reasoning, the baseline ended up more bullish on O1 than every persona, including the one
whose career was built inside a resourced institution — the clearest answer here to what
simulating people added: a partner to contest an analyst's own argument, which a solo baseline
never gets.

**Process note.** The orchestrator released R3 at 05:24, once the scribe files had sat unchanged
for 90 seconds, though the scribe was still trimming them until 05:34 — personas read a slightly
longer earlier version of the persona-facing notes (same content, no persuasion statements).
`RUN_METADATA.md` records the fix: release on completion replies, not files that merely look
finished.

---

## 9. Limitations

- **Same-model instances.** Every persona, baseline, and checking agent is one model — not
  independent evidence, however many agree (`AGENTS.md` rule 7).
- **Centuries of path dependence, and the O1 gap.** All experience arguments cross centuries,
  flagged in-post where they may break (§3). Does building a career *outside* large institutions
  shape the O1 gap (§8)? Partly, not cleanly `[writer]`: Franklin, Lovelace, and Curie (whose
  dossier describes "routing around closed doors" rather than waiting for institutions,
  `personas/H4_curie/dossier.md` §A, `[inferred]`) all built outside large institutions;
  Curie scores O1 lowest in the roster (§4, axis A) and Lovelace opened below the R3 median
  (§1). The complication: Faraday, the one persona whose career was 52 years inside one
  institution, gives O1 its highest persona score (8 at R1, §1) — still below the baseline's 8.
- **A small panel.** Six personas, three tables of four, two seats each; overtime skipped by
  design (`RUN_METADATA.md`).
- **Fact-checks are samples.** ① checked 12 facts, left five unchecked for budget (F9, F11, F12,
  F15, F16); ② checked 7; ③ checked 6 new claims plus 12 experience statements, out of many more
  across 41 posts (`evidence/errata.md`, `audit.md`).
- **Incomplete de-identification.** The blind pick (§6) removes names, but period detail (a shed
  lab, a palace exam) can still identify the speaker to a reader who knows the history.
- **Known source gaps.** `carta.com/data` refused automated access both passes; `nobelprize.org`
  refused a second attempt; the DIMAC source never resolved; the Meta posting central to F9
  couldn't be re-found. Startup-funding figures are secondary-source only (`RUN_METADATA.md`).

---

## 10. Reversal signals

- This PI already holds secured funding and a record of placing students well → O3 above O1 for
  Franklin, Faraday, and Lovelace (`cruxes.json`, X1).
- A sourced answer on whether O1 roles require a PhD (F9) → reopens X1 for at least three
  personas.
- Alex's actual offer can, or can't, be deferred or reopened (C4) → settles X2's main split for
  Darwin and Curie both (X2).
- A named co-maintainer or reviewer already committed, checkably, not hoped for (C5/C3) →
  removes the biggest objection to O4 raised independently in C (`C/X2/H4`, `C/X2/H6`).
- Written equity/vesting/governance terms, a named mentor besides the CEO, runway past eighteen
  months → the exact test Franklin, Darwin, and Curie each named for O2 (`C/X3/H1`, `C/X3/H2`,
  `C/X3/H4`).
- Outcomes data on whether solo- or pair-maintained open-source projects grow or stall over a
  year → absent from the brief; its absence is why O4's central promise stays unverifiable.
- Whether 2024's academic-placement rebound (F8) holds for several more years or reverses → the
  optimistic reading of Q1 leans on it holding for the five-plus years a PhD takes.
