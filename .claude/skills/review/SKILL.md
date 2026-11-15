---
name: review
description: Put a draft (research proposal, paper, pitch, product spec, essay, plan) in front of a panel of 3–5 personas with different lenses — independent critiques, a cross-check wave, then a ranked fix list. Use when the user wants feedback on an artifact rather than a choice between options, e.g. "review my pitch with Gurley, Huang and Collison" or "tear this proposal apart".
---

# Review

Follow `protocol/09_review.md`. Rules are in `AGENTS.md`; read its hard rules first. Claude
Code specifics are in `CLAUDE.md`.

1. Get the artifact (a path or pasted text) and its goal: who reads it, what it should make them
   do, what the user does not want changed. Create
   `workspace/runs/<YYYY-MM-DD>_review_<slug>/`, write `brief.md`, copy the artifact to
   `artifact.md`.
2. Pick 3–5 personas with different lenses from `personas/` (the bundled library) or
   `workspace/personas/` (the user's own). If the user named them, use those. Tell the user the
   panel in one line each: who, and what that lens is likely to catch.
3. **Wave 1.** One real sub-agent per persona, launched together. Each reads only its persona
   folder, `brief.md` and `artifact.md`, and writes `critiques/<ID>.md` from
   `templates/run/review.md`.
4. **Wave 2.** Only after every critique is in, continue each persona agent (SendMessage) with
   the other critiques; each writes `cross/<ID>.md` from `templates/run/review_cross.md`.
5. A fresh editor agent, which has not read the persona folders, writes `summary.md` from
   `templates/run/review_summary.md`.
6. Reply with the top three fixes, the contested calls and the path. Long files stay on disk.

Every persona file starts with the simulation notice. Personas propose fixes; they never rewrite
the user's artifact.
