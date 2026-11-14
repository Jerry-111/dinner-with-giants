# Publishing a reader pack to Notion

Optional. The reader pack (`protocol/07_reader_pack.md`) is destination-agnostic — Markdown in
the run folder by default. These notes are for the case where you also publish it to Notion,
through a Notion MCP server. Nothing here is required to run the protocol.

## Before you touch a page

- **Ask the user first.** Which conclusions go to Notion, how they'll use it, how long it should
  be. Not everything in the full report belongs in Notion — most of it should stay in Git.
- **Fetch the current content before editing.** The user may be editing the same page (for
  example, a space they keep for their own notes) while you work. Fetch, then edit against what's
  actually there, not against what you last saw.
- **Write the Markdown locally first**, in the run's reader-pack file, then upload it. Don't
  compose the page inside the Notion call itself.

## Replacing a page's content

- A replace-content call that doesn't carry forward the tags for every child page and database
  already under that page will delete or detach them. If the tool refuses the call for this
  reason, add the missing tags and retry. Only pass whatever flag allows deletion once the user
  has explicitly agreed to lose those child pages — never as a default.
- Long pages: write the first section with the replace call, then append the rest section by
  section (split on `## ` headings) with an insert-content call per section. A single call with
  the whole page is more likely to hit size or formatting limits, and harder to recover from.

## Moving child pages

Moving several child pages in one call can reorder them unpredictably. Move one at a time: remove
its tag from the old location, add it at the new location, in a single update call — then fetch
and verify before moving the next one.

## Notion-flavored Markdown drifts

The Markdown dialect a Notion MCP server accepts changes over time (toggle syntax,
colored-paragraph syntax, what counts as a comment). Re-read the current spec before a session
that uploads to Notion; don't rely on what worked last time. Specific traps seen in practice:

- A generic collapsible-block syntax may be stored as plain text instead of rendering as a toggle;
  the dialect usually wants the toggle's own tag, with a heading on the first line, a blank line,
  then the body.
- A colored paragraph usually needs its own inline tag around the paragraph, not a Markdown
  extension syntax.
- HTML comments are often not supported at all.
- Bold text that ends right at CJK punctuation with no space, immediately followed by more CJK
  text, can render with the literal asterisks showing instead of bold. An explicit bold tag avoids
  it in that position.
- Upload the first section, fetch it back, and check it rendered the way you intended before
  uploading the rest — a formatting mistake is cheaper to catch in one section than in ten.

## Keeping track of page and database IDs

Publishing to Notion means tracking the IDs of the pages and databases you created or are
updating. Keep that map in your own workspace (for example, a short file under `workspace/`), not
in a shared or public repository — it is specific to one person's Notion workspace and is useless,
or confusing, to anyone else.

## The user's own space

If the reader pack is going next to a space the user already keeps for their own notes (a running
journal, a decision log), that space is theirs: don't reorganize it, re-categorize it, or delete
anything in it. Add the new page the way the user's existing pages are already organized (for
example, newest at the bottom, dated headings) rather than imposing a new structure on it.
