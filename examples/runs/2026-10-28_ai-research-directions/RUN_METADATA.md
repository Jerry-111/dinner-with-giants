# RUN_METADATA: 2026-10-28_ai-research-directions

| Item | Content |
|---|---|
| Run | `2026-10-28_ai-research-directions`: a real run, adapted for publication on 2026-11-14 |
| Question | 16 AI research directions (D01–D16) scored on impact, bottleneck, academic edge and timing; Q1 levers, Q2 academic foundation models, Q5 late entry, Q6 taste |
| User | One private user. Their background, their four candidate topics, two questions about their own path and one rubric dimension about their career are removed (see [README.md](README.md)) |
| Personas | 20 public figures in AI research, technology and investing (`scope.md`); two no-persona baselines, Z1 and Z2 |
| Materials through | 2026-10-28 |
| Environment | Claude Code. All persona agents were started fresh for this run and continued round to round with SendMessage; fresh agents for the evidence brief, follow-up evidence, crux map, scribe notes, judges and fact-checks |
| Language | Run in Chinese; translated into English for publication |
| Main outputs here | `reader/page.md`, `report.md`, `summary.md`, `board/`, `judge/`, `r1/`, `r3/`, `evidence/`, `audit.md` |

## Timeline (PT, 2026-10-28)

| Time | Event |
|---|---|
| 14:00–14:20 | `rubric.json` (pairwise comparisons and Q2 conditions), `scope.md` and round instructions written; an evidence agent condensed the shared brief, `evidence/brief.md` (18.6 KB in the original) |
| 14:15–15:00 | R0: 20 fresh persona agents write their cards and fill dossier §I, extracting only from their existing folders |
| 14:29–15:33 | R1: 20 personas and baselines Z1, Z2 score independently |
| 15:33–16:14 | A crux agent that had read no persona material groups the disagreements into seven cruxes and seats seven tables, two per persona |
| 16:20–16:36 | A opening: 40 posts, 38 of them citing an experience from the persona's dossier. A follow-up evidence agent answers five open questions raised in the openings → `evidence/followups.md` |
| 16:38–16:57 | B exchange: 40 posts and 6 interjections; verdicts 88 accept, 71 reject; 6 source challenges |
| 16:57–17:42 | Fact-check ② (fresh agent): 14 claims, 8 confirmed, 6 partly confirmed; 4 corrections → `evidence/errata_B.md`, delivered before round C |
| 17:42–about 18:15 | C closing: 40 posts; 13 retractions |
| 17:59–about 18:45 | Five scribes write two versions of the notes for seven tables. The persona-facing version (`board/summary/`) never says who persuaded whom |
| about 18:15–18:55 | Overtime: one pair per table, two rounds, both sides writing at once; 28 posts |
| about 18:45–19:05 | Scribes add the overtime; judges J1 (X1–X4) and J2 (X5–X7), seeing names, score 154 posts against a scorecard |
| about 19:05–19:55 | R3: private re-score by the 20 personas and Z1, Z2 |
| about 19:45–20:15 | Fact-check ③: 11 claims, 9 confirmed, 2 partly confirmed. Experience check of 20 arguments against the dossiers: 16 as told, 4 with details changed, 0 not found → `audit.md` |
| about 19:55 | Aggregation → `summary.json`, `summary.md` (recomputed for this public version; see below) |
| 20:10–22:00 | The original report, its review and a reader page were written for the original user. They are not included |

## Adaptation for publication (2026-11-14)

- **Removed:** the user's background section in `scope.md`; the user's candidate topics T1–T4
  with every score, comparison and argument about them; Q3 (two acquaintances' claims about
  academia and industry) and Q4 (the user's own paths); the `career_capital` dimension and the
  weight set built for the user; every sentence that applied an argument to the user; persona
  sentences that confessed their own interests in the first person. Counts per file are in
  [README.md](README.md).
- **Reworded:** judge and scribe notes that described a persona's character now describe the
  post ("the post conceded"), with the substance unchanged.
- **Translated:** from Chinese, by sub-agents, one per debate table and one per group of score
  files, each checked for leftover Chinese text and private markers; JSON keys and numbers
  checked against the originals by script.
- **Recomputed:** `summary.md` and `summary.json` with this repository's `tools/sim.py
  aggregate` over the cleaned files, so the ranking no longer includes the removed topics. No
  score was changed.
- **Written new, from the public files only:** `report.md`, `reader/page.md` and `review.md`,
  by fresh agents that did not see the original report.
- **Not included:** the R1 and R3 prose write-ups (the JSON files carry the scores, reasons and
  changes), the original round instructions, the original report and reader page, the
  orchestrator's design notes, and a blind comparison against the previous protocol version.

## Independence and limitations

- **One model.** Personas, baselines, evidence, crux, scribe, judge and fact-check agents are all
  instances of one model. Headcount is not independent evidence. Claude is trained by Anthropic;
  Dario Amodei is Anthropic's CEO, and Andrej Karpathy joined its pre-training team in 2026-05.
- **K3 read design files at R0.** The persona agent reported having read the orchestrator's
  design notes, the scope and the user's topic list. It was not restarted; later instructions
  forbade it, and the protocol comparison ran a sensitivity analysis without K3.
- **A script showed old lines.** At R0, K2 ran a scan that printed a few stance lines from a
  previous run's posts. The script now scans cards only by default.
- **Shared scratch directory.** Until about 16:50 all sub-agents shared one scratch folder that
  still held drafts from a previous run. In round B, M4 reported that another agent overwrote
  its temporary file once and that it saw a fragment of table X3 (not its own table; it reports
  not using it). From round C, each agent had its own subfolder; K5 and K2 still wrote to the
  root a few times. This is why `CLAUDE.md` now requires per-persona scratch folders.
- **Directory listings.** Simultaneous posting relied on instructions. K3 (rounds A and B), K6,
  M2 and M4 (round A) listed `board/` and saw file names only; C3 listed the round-B folder in
  round C to find interjections.
- **A rule was added mid-round.** At the start of round B, interjections did not require the
  closing JSON block; it was required from the eleventh post on, and C3, M7 and K3 added the
  `responses` to their interjections in round C.
- **Format slips.** Two round-C verdicts used the retired "partial"; K3's and C4's round-C posts
  ran over the length limit.
- **Self-reported change values.** In M6's R3 `changes`, the `from` values for D07 and D08 were
  its round-C intended values, not its R1 scores; it took back its round-C concession in R3, so
  the net change from R1 is 0 for both. The aggregation uses actual scores and is unaffected.
- **Few self-checks.** R1: 3; debate: 2; overtime: 0; R3: 1. Personas relied mainly on the
  shared brief and their own dossiers.
- **Experience details drift.** Of 20 experience arguments checked in fact-check ③, 4 differed
  from the dossiers in detail: K4's posts told two stories (a friction exploit in a Tesla
  simulator, and an "intent gap" found during the Universe project) more specifically than the
  dossier does; M6 merged two separate self-assessments into one sentence; C5's QT-Opt numbers
  were mis-joined when the scribe compressed the notes (the original post was correct).
- **Overtime pairs were chosen by the orchestrator** from the scribe's "remaining disagreements"
  and "strong arguments nobody answered", not at random.
- **Table sides did not always match posts.** At X4, M2 and M3 were seated on the "bet heavily"
  side; their posts were closer to the middle, and the scribes followed the posts.
- **Limited fact-check coverage.** Fact-check ② covered 14 claims, fact-check ③ 11 claims and 20
  experience arguments; the rest were not independently checked.
