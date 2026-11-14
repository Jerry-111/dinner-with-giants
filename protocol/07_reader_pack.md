# Reader pack

A one-page version of the report for the user to read. The full report
(`protocol/06_synthesis.md`) is the archive; this is the summary a person will actually read end
to end.

## Before you write it

- **Ask the user first:** which conclusions should go into the reader pack, how they'll use it,
  how long it should be. Most of the full report should stay in the run folder — not everything
  belongs in a one-page summary.
- Write the Markdown in the run folder first (as `reader/page.md`); only then publish it
  somewhere else, if the user wants that.

## Destination

Markdown, in the run folder, by default. That alone satisfies this step. Publishing it somewhere
else is optional and is a separate decision the user makes — **ask before publishing anywhere**,
every time, even to a destination used before. If the destination has its own publishing quirks
(for example, a workspace tool reached through an MCP server), check whether `docs/integrations/`
has notes for it before you start.

## Structure: one page

- **One flat page.** Don't split it into child pages or a database. Once it's compressed to one
  page, splitting it only adds navigation, not clarity.
- **Top to bottom:** a short notice block (simulation disclosure, material cutoff date, a link to
  the full record) → the one-line conclusion → domain analysis → paths for the user → per-option
  detail → stage of the field → personas → the user's own named questions, answered → where this
  could be wrong.
- **Use formatting to carry structure**, not more text: callout boxes, tables, short labels or
  tags, columns where the destination supports them.
- **Summary on the surface, detail collapsed.** Each option, each persona, each named question
  gets one row or one line; detail goes in a collapsible block or a link to the file in the full
  record.
- **Reversal signals and other agent-facing detail** go in a collapsed block at the bottom — the
  user doesn't need to read them, a future agent does.

## Writing each section

- Lead with the conclusion, in the first sentence. Then: why, what it means for the user, ways of
  engaging that are already too late, what's worth doing, reversal signals.
- Keep only the numbers and sources that matter; link out to the file in the full record for
  detail instead of inlining it.
- Avoid both failure modes: dumping everything in, and compressing until there's nothing left to
  act on.

## The user's own notes space

If the user keeps a running space for their own thinking (a decision journal, a planning log) and
the reader pack is going next to it, that space is theirs. Don't re-categorize it, don't impose a
new structure on it, don't delete anything in it — follow whatever organizing principle it already
uses (for example, entries ordered by when they happened, not by when they were written up).
