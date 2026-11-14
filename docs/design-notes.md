# Design notes

Why the protocol looks like this. Each item: the rule, what happened in an earlier run that
motivated it, and what changed. Numbers are real; identities, dates and topics are not — see
`RESPONSIBLE_USE.md` and the privacy rule in `AGENTS.md` for why.

## Independence and herding

**A shared template flattens differences.** Early on, several personas were put to the same
scoring table with no stance-setting step first; most of the written-out top recommendations came
back nearly identical. Giving each persona its own stance-based, follow-up-driven exchange before
scoring — closer to a real conversation than a form — is what made the disagreement visible. A
persona layer that always agrees with itself adds nothing over a single baseline call (see the
persona–baseline gap, below).

**Several instances of one model are not independent evidence.** A run with a dozen-plus persona
agents, all the same underlying model, says so in its own limitations section — headcount is
reported as description, never as support. The same caution applies to a "fresh" fact-checking
agent that turns out to have read a prior round's exchange: it is no longer independent either,
and the run record says so.

**Co-affiliated personas cannot be the only representation of one side.** Personas who share an
employer, lab, or long collaboration were once seated at the same table without being flagged, so
one "side" of a crux was really one relationship. The rubric now carries a `not_independent` list,
and the table-seating check rejects any table where one side is only that group.

**Interjections pile on.** One debate table drew seven interjections in a single exchange round,
nearly all citing the same fact-check item and taking the same side, and a visible persuasion
chain followed (one persona raised a score; a second raised its own, citing "even the first one
moved"). Requiring an interjection to carry a new argument, not just agreement, was tried first and
was not enough on its own — the same table format produced lopsided interjections again in a later
run. A per-table, per-side cap is the next fix, rather than relying on the wording of the rule
alone.

**De-identifying posts turned out not to be worth relying on.** Posts were once stripped of names
before judging, on the theory that it would reduce in-group bias. But content gives the author
away regardless of the label on it — a signature method, a first-person claim about a paper or a
company — and a comparison of how closely a judge's score tracked how often a point was actually
accepted found a weak relationship either way, blind or named. Debate and judging are now fully
named; the protocol tracks the social dynamics that come with that (above) instead of relying on
an anonymity that wasn't real.


**Herding by "others changed too" did not go away.** In two consecutive 20-persona runs, about
one in ten score changes in the private re-score was justified only by social reasons ("several
people moved", "the majority agrees") rather than by a restated argument — 10.9% in the earlier
architecture and 10.0% in the later one, a difference of one change. The persona-facing scribe
notes, which stopped saying who persuaded whom, did not move this number. Such changes are still
flagged and excluded from "persuaded by" counts; reducing them further is an open problem.

## Experience arguments

**An experience argument is judged on the analogy, not the arguer.** Treating "I lived through
this" as either automatically persuasive, or automatically discounted because the arguer has an
interest, were both tried and both rejected. The rule that stuck: score whether the analogy holds
here; rebut it by breaking the analogy, never by citing the arguer's identity or interest.

**Experience arguments front-load into the opening round and then disappear.** A blind count of
posts making an explicit, source-cited experience argument went from roughly one in eight to just
under half once a template change gave them an explicit slot — but even after the change, presence
was high in opening posts and at zero by the closing round. Later templates add an
experience-argument slot to the exchange and closing rounds specifically, not only the opening one.

**Retold experience drifts toward the dramatic.** A spot-check of twenty experience-argument posts
against their source dossiers found several retellings that were more specific or more dramatic
than the source, or that merged two separate episodes into one. Experience arguments now have to
cite the dossier section in the post, and retellings are checked against the dossier's own wording,
not the debate post's.

## Evidence and fact-checking

**A shared brief needs its own fact-check before anyone reads it.** A shared evidence brief once
carried a claim whose direction turned out to be backwards once checked against a primary source;
the correction was appended in place rather than quietly editing the original out. Every run now
fact-checks the shared brief against primary sources before any persona agent sees it.

**No self-checking makes a debate circle the same brief.** One run allowed generous self-checking
in the independent-scoring round and used most of that budget; the debate rounds that followed
banned self-checking entirely, and of well over a hundred posts, not one introduced a new source —
every disagreement stayed inside the brief and the existing fact-check. The fix was a small,
logged, self-check budget during debate too, spot-checked afterward, rather than banning search
outright.

**An unconditional option to self-check goes unused.** Given the option but not the requirement, a
full debate-plus-overtime run saw it used only a couple of times across the whole roster. Tying
self-checking to source challenges worked better: whoever challenges a source, or is challenged,
must produce an independent one or retract — and that produced several times more retractions than
the unconditional option ever did.

**Corrections have to land before scores move, not after.** In one run the in-debate fact-check
pass arrived only after the private re-score, too late to inform it. Moving that pass earlier —
between the exchange and the closing round — is now the default ordering, specifically so a
correction can change a score instead of only appearing in the record afterward.

## Measurement

**Freeze the rubric, and the comparison plan, before any score comes in.** Options, dimensions,
scale and aggregation rules (no headcount as evidence, no weighting by persona, no extremizing) are
written down and frozen before independent scoring starts. When two runs are being compared, the
comparison plan is written and dated before anyone scores anything, specifically so the criteria
can't be picked after seeing which side looks better.

**Measure the gap between the persona layer and a plain baseline, every run.** Comparing two
architectures on the same question, the median persona score's distance from a no-persona baseline
analyst rose from roughly 0.7 to roughly 0.95 points on a 0–10 scale. That gap, reported on its
own and never folded into the persona distribution, is the closest thing this protocol has to "what
does simulating a person add over asking the model directly."

**State which version is being compared, before comparing it.** A first blind comparison pitted an
unreviewed draft of a newer run's report against the fully reviewed report of an older run; both
raters preferred the older, reviewed report overall, though the newer draft still won on a couple
of specific dimensions. A second comparison, finished report against finished report, came out
split between the two raters who ran it. Both results stayed in the record rather than only the
more flattering one, and later comparisons state upfront whether draft or reviewed versions are
being judged.

**Blind raters can still see more than intended.** After finishing one set of ratings, a rater
listed the directory the comparison files lived in and saw their names, though reported not
opening them. Instructions for blind comparisons now say explicitly not to browse sibling files,
and any boundary-crossing is self-reported and disclosed in the write-up rather than ignored.

## Operations

**Rate limits bite on concurrency, not on account quota.** Launching a full roster of agents at
once (high teens) tripped server-side rate limiting and interrupted more than half of them
mid-task; interrupted agents could resume where they left off. Resuming is more fragile still: by
the time a persona agent has read its full material and scored every option, its context can run
into the hundreds of thousands of tokens, and resuming about a dozen such agents at once once
interrupted every one of them. The fix in both cases is to ramp concurrency in steps (for example
3, then 6, then 7) with a pause after a rate-limit error; a later run holding to a steady, low
concurrency saw no interruptions at all.

**Shared scratch space leaks between agents.** Sub-agents sharing one working directory overwrote
each other's draft files mid-round; one participant ended up reading a fragment meant for a
different table. The fix: a subfolder for the orchestrator, a subfolder per persona keyed by its
ID, an explicit instruction not to read or list outside one's own folder, and old drafts moved
aside between rounds.

**A round run serially breaks symmetry.** One round of paired critiques ran one pair after
another rather than all at once; replies on one side went out before the other side's critiques had
even arrived, so some critiques were never answered. The fix: launch every critique in a round
concurrently, wait for all of them, then launch every reply concurrently. Pairing can start as soon
as both sides of a given pair are ready, but no reply goes out until every critique in that round
is in.

**Resuming the same agent keeps its research and its voice.** Continuing a persona agent into a
later round, instead of briefing a fresh one, keeps the material it already gathered and reads more
consistently like that persona. Later-round prompts for a given persona resume that persona's own
agent rather than re-briefing a new one.

## Writing

**The full report is not what the person reads.** A full report of roughly 60 KB was read to
completion by its intended reader only about 40% of the way through. The full report stays as the
archival record and the context for future runs; a separate one-page reader pack is written for the
person, with detail collapsed or linked instead of inlined.

**Every scored claim needs a pointer back to its source.** In a blind quality comparison, raters
consistently preferred the version that cited a specific post ID or fact-check item on nearly every
claim over a version that read just as well but didn't. The writer template now requires that
citation on every scored claim as a matter of structure, not of the writer's initiative.

**Don't guess a pronoun.** Draft reports referred to personas and to the decision-maker as "he" or
"she" by guesswork. Reports and reader pages now use a name, an ID, or "the user" — never a guessed
pronoun — for either.

**A changed rule has to be removed everywhere, not just added to.** A rule that once told writers
to apply an extra discount to a certain category of claims was reversed by a later rule (judge the
claim on its merits, disclose the interest, never discount) — but the old wording stayed in place
elsewhere, and a report and its independent reviewer both carried it forward until someone caught it
by searching for the old phrase. The practice now is to search the rule files for the old wording
whenever a rule changes, in prose and in structured fields (persona cards included) alike.
