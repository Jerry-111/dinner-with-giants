# CLAUDE.md

Rules are in `AGENTS.md` — read it first. This file is Claude-Code-specific.

- **Persona agents are real sub-agents.** Launch them with the Agent tool, concurrently. Never
  simulate several personas by role-playing them in one context and then describe them as
  independent — they aren't, and the run record would be misstating it. Each prompt states exactly
  which files the agent may read, where it writes, and the expected length and format.
- **Debate rounds are released whole.** Send the next round's instructions only when every post
  of the current round is in, so nobody writes after reading a same-round post. "In" means the
  agent has replied that it is done — not that its files have stopped changing for a while. An
  agent may still be revising (for example, trimming to a size limit) after a quiet minute.
- **In light mode, critiques and replies run in two synchronized waves.** Launch every persona's critique
  concurrently; only once all of them are in, launch every reply concurrently. A serial run
  (critique, reply, critique, reply, one pair at a time) can let one side's reply go out before
  the other side's critique has even arrived, so it never gets answered. Don't let that happen.
- **Fact-checks and final reviews use fresh agents.** They should not have read the persona files
  or the debate — that is what makes the check independent. Don't reuse a persona agent for this,
  and don't hand the new agent the debate transcript "for context."
- **Long files stay on disk.** Reports, digests, and aggregates get written to a file; the chat
  only states the conclusion and the path.
- **Concurrency.** Keep simultaneous sub-agents at 7 or fewer. Ramp up in steps (3, then 6, then
  7) rather than launching a full roster at once. On an HTTP 429, back off about 3 minutes before
  resuming, then continue the ramp.
- **Per-persona scratch folders.** Give the orchestrator its own subfolder and each persona a
  subfolder keyed by its ID; tell every agent not to read or list outside its own folder. A shared
  scratch directory lets agents overwrite or read each other's drafts mid-round.
- **Resume, don't restart.** Continuing a persona agent with SendMessage for its next round keeps
  its gathered material and its voice; a fresh agent re-reads everything and tends to drift from
  the persona.
- **Project skills** live in `.claude/skills/`, maintained separately from this protocol.
