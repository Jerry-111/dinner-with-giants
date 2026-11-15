# Responsible use

This framework simulates how a person reasons, rebuilt from public material. A simulation is never
the person. This page says what the project ships, the rules every persona and run follows, and
what you should not do with them.

## What this repository ships

- The protocol, templates, schemas and tooling.
- A persona library (`personas/`):
  - **20 living public figures** in AI research, technology and investing, built from their own
    public interviews, talks, essays, papers and filings;
  - **6 historical figures**, built from their own public-domain writings.
- Two example runs: one adapted from a real run about AI research directions, with its user's
  personal details removed; one about a fictional user.

**None of the people simulated here has reviewed, endorsed or contributed to their persona, and
none is affiliated with this project.** The personas are reconstructions by a language model, as
of a stated date, from the sources listed in each folder.

## Who can be a persona in this repository

- **Public figures with a substantial public record of their own views**: books, essays, long
  interviews, talks, papers. A persona is simulated only within that record: on the person's
  field, work and public positions.
- **Historical figures** with their own writings or a solid archival record.
- **Archetypes and fictional characters**, clearly labeled.
- **Never** private individuals (friends, colleagues, family, mentors, students), minors, or
  people known mainly for their private lives.

## Rules that every persona and run follows

These are enforced by the templates and checked by `tools/sim.py lint` where a machine can check them.

1. **Every persona output says it is a simulation.** English: "Simulation based on public
   material; not the person's own words." Chinese runs: "基于公开材料的模拟，不是本人言论。"
2. **Every claim is labeled** `[quoted]`, `[synthesized]` or `[inferred]`. The persona's views,
   the agent's extrapolation and technical evidence are kept apart.
3. **Quotes are real and short.** Only text the agent actually read; English quotes under 15
   words; at most one quote per source; the range actually read is recorded. Famous lines that
   no primary source confirms are listed as "commonly attributed, not verified" and never quoted.
4. **No invented positions.** Where the person has said nothing in public, the persona says "no
   judgment" or labels the view `[inferred]`.
5. **No working around access controls.** If a site refuses access, the source is recorded as
   inaccessible.
6. **Interests are disclosed as dated facts** and never used to attack or to discount an argument.
7. **No confessions in the first person.** A persona never writes "I admit my judgment is shaped
   by my stake in …" or any other first-person statement about its own motives. That is the
   agent's inference, and in the first person it reads like something the person said.
8. **No judgments of character.** Persona files, judges and reports evaluate arguments and
   dated predictions, never a person's honesty, motives or character. A track record lists
   public predictions with dates, outcomes and sources; it is not a verdict on the person.
9. **Dated, sourced facts about people.** Roles, companies, departures and deals carry a source
   and an "as of" date. Unconfirmed claims are dropped, not hedged.
10. **No commentary on a person's own news.** A persona of a living person does not discuss its
    own recent news, legal matters or governance matters, and is not asked to. Interest lines show
    only the dated facts that bear on the question at hand.
11. **Model-vendor links are disclosed.** Claude is trained by Anthropic. Where a simulated
    person leads or works at the company that makes the model running the simulation, the
    persona card and the run's limitations say so.

## What not to do with it

- **Never present simulated output as something the person said or believes.** No fabricated
  quotes, screenshots, posts, letters or "interviews". Do not strip the simulation notice when you
  share an output.
- **No endorsements, no persuasion campaigns.** Do not use simulations to make a person appear to
  endorse a product, a candidate, a cause or an investment.
- **No harassment or impersonation.** Do not use personas to target, mock, deceive or contact
  anyone, or to stand in for a person in a conversation with third parties.
- **Your own private people stay private.** Do not build personas of private individuals without
  their explicit permission. To test something a friend said, record it as a "claim to test"
  attributed to "a friend", not as a persona. Your own context, personas and runs belong in
  `workspace/`, which git ignores.

## Not professional advice

Runs produce structured arguments and disagreements, not advice. They do not replace a qualified
professional for legal, medical, financial, immigration or employment decisions. Several instances
of one model are not independent experts, whatever names they carry.

## Concerns and takedown

- **If you are a person simulated here**, or act for one, and want your persona changed or
  removed: open an issue with the **Content concern** template, or report it privately through
  the repository's Security tab ("Report a vulnerability"). We remove it; no reason needed.
- If you believe something here misrepresents a person, contains personal data, or infringes a
  right, use the same routes. Content under a good-faith concern is removed first and discussed
  after.
