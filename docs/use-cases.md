# What you can use it for

The idea underneath every mode: a great person's advice is the residue of a particular path:
the bets they lived through, the failures that marked them, the question they always ask first.
That bias is not noise to average away. It is the reason to ask them. Each recipe below seats a
room of such biases around one problem and keeps them apart long enough to disagree.

All persona outputs are simulations based on public material, not the people's words.

| You want to… | Mode | Time |
|---|---|---|
| [Hear what a few people would ask you first](#1-ask-the-room) | `/consult` | minutes |
| [Get a draft torn apart before its real audience sees it](#2-review-a-draft) | `/review` | 10–30 min |
| [Find out how a plan fails, in advance](#3-pre-mortem) | `/review` | 10–30 min |
| [Rehearse a pitch or an interview](#4-rehearse-a-pitch) | `/review`, then `/consult` | 20–40 min |
| [Choose between real options](#5-decide-between-options) | `/deliberate` | 1–6 hours |
| [Map a contested field](#6-map-a-contested-field) | `/deliberate` | 2–6 hours |
| [Get argued out of a belief](#7-red-team-a-belief) | `/consult` | minutes |
| [Brainstorm from different paths](#8-brainstorm-from-different-paths) | `/consult` | minutes |
| [Keep a standing board that knows you](#9-keep-a-standing-board) | all modes, over months | ongoing |

## 1. Ask the room

Before a hard conversation, a meeting or a decision you have not framed yet.

```
/consult What would Karpathy, LeCun and Fei-Fei Li ask me first about building a robotics
startup on top of video world models?
```

Each persona answers alone, in one screen: the questions it would ask back, its judgment with
labels, where it would push back on you, and its interests as dated facts. A panel ends with
where they disagree and what evidence would settle it.

## 2. Review a draft

A research proposal, a paper, a pitch, a product spec, an essay, a plan.

```
/review drafts/proposal.md — a two-page proposal for an academic world-model project; the
audience is a funding committee. Panel: Sutton, Hassabis, Liang, Tedrake.
```

Wave 1: every persona critiques alone (three problems at most, each tied to the experience
behind it, each with a fix). Wave 2: each persona marks the others' problems agree or disagree,
with an argument. A fresh editor compiles a fix list ordered by severity and by how well each
argument survived, not by headcount, plus the contested calls you have to make yourself.

Pick the panel for difference. For a pitch: capital (Gurley, Khosla), platform and cost (Huang),
operating (Collison). For research: scale (Amodei, Karpathy), lived experiments (Sutton,
Levine), evaluation (Liang, Neubig).

## 3. Pre-mortem

Ask the room to assume the plan already failed.

```
/review plans/2027.md — assume it is 2028 and this plan failed. Each persona: the most likely
cause, from your own experience, and the earliest signal we would have seen.
```

Personas with different paths see different failure modes: a capital lens sees the financing
cliff, an experiment lens sees the evaluation that never got built.

## 4. Rehearse a pitch

Run `/review` on the deck's text with investor and operator personas, then:

```
/consult Gurley, Khosla and Collison: the five hardest questions you would ask in the meeting,
hardest first.
```

## 5. Decide between options

The full protocol: a pre-registered rubric, independent scores, debate tables around the cruxes,
timed fact-checks, judges, private re-scores, and a report that keeps the disagreements intact.

```
/deliberate
```

The skill asks for the decision, the options, the personas and the budget first. Start with a
panel of 3–6 personas. Example: [`examples/runs/2026-11-14_alex-next-step/`](../examples/runs/2026-11-14_alex-next-step/).

## 6. Map a contested field

Make the options the field's directions and the rubric dimensions field-level (impact,
bottleneck, where academia has an edge, timing). The debate tables then form around the field's
real cruxes.

Example: [`examples/runs/2026-10-28_ai-research-directions/`](../examples/runs/2026-10-28_ai-research-directions/)
— 20 personas, 16 AI research directions, seven tables (does RLVR teach new reasoning? are world
models ahead of their evidence? can simulation replace real robot data?).

## 7. Red-team a belief

```
/consult I believe evaluation is the best bet for an academic lab in the next five years. Pick
the three personas most likely to disagree and have each argue me out of it.
```

## 8. Brainstorm from different paths

```
/consult If you were starting in AI research today with a small GPU budget, which three
projects would you start? Each persona: the experience that makes you pick them.
```

Ideas come back already tagged with the path that produced them, which tells you what each idea
assumes.

## 9. Keep a standing board

A famous mentor gives you five minutes. A standing board gets your whole context and keeps it.

1. Copy the templates once: `mkdir -p workspace/context && cp templates/context/*.md workspace/context/`.
   Fill in `user_profile.md` and `preferences.md` with only what you are willing to share.
2. Keep `workspace/` wherever your notes live: inside your Obsidian vault, synced from Notion,
   or as its own private git repository. Never push it anywhere public.
3. Ask the same panel at each turning point: before a job decision, after a project ships,
   when a plan stalls. Every consult, review and run reads your context first.
4. Close the loop in `calibration_log.md`: what the room advised, what you did, how it turned
   out. The next run reads it, so advice that kept missing gets questioned instead of repeated.

## Build your own room

`/new-persona` builds a persona from public sources: dossier, domain views with a dated
prediction record, card and sources table. Your own personas, context and runs stay in
`workspace/`, which git ignores. Follow [`RESPONSIBLE_USE.md`](../RESPONSIBLE_USE.md).
