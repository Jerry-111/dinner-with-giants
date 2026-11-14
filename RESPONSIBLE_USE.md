# Responsible use

This framework simulates how a person reasons, rebuilt from public material. A simulation is never
the person. This page says what the project ships, what you may do with it, and what you should not.

## What this repository ships

- The protocol, templates, schemas and tooling.
- An example persona pack built from **historical figures whose own writings are in the public
  domain**, and fictional examples. **No personas of living people are shipped or accepted into
  this repository.**
- An example run about a fictional user.

## Rules that every run follows

These are enforced by the templates and checked by `tools/sim.py lint` where a machine can check them.

1. **Every persona output says it is a simulation.** English: "Simulation based on public
   material; not the person's own words." Chinese: "基于公开材料的模拟，不是本人言论。"
2. **Every claim is labeled** `[quoted]`, `[synthesized]` or `[inferred]`. The persona's views,
   the agent's extrapolation and technical evidence are kept apart.
3. **Quotes are real and short.** Only text the agent actually read; English quotes under 15
   words; at most one quote per source; the range actually read is recorded.
4. **No invented conflicts.** Where the person has said nothing in public, the persona says "no
   judgment" or labels the view `[inferred]`.
5. **No working around access controls.** If a site refuses access, the source is recorded as
   inaccessible.
6. **Interests are disclosed as dated facts** and never used to attack or to discount an argument.
7. **No confessions in the first person.** A persona never writes "I admit my judgment is shaped
   by my stake in …" or any other first-person statement about its own motives or biases. That is
   the agent's inference, and in the first person it reads like something the person said.
   Interests appear only as third-person, dated facts (the card's `interest_line`); any judgment
   about motives is written in the third person and labeled `[inferred]`.

## If you simulate living public figures

You can build personas of public figures from their public interviews, talks and writing, for your
own use. You are responsible for what you do with them.

- **Keep them in `workspace/`.** That folder is git-ignored. Publishing a living person's persona,
  or a run that contains one, is your decision and your responsibility under the platform's rules
  and the law where you live (publicity rights, defamation, data protection).
- **Never present simulated output as something the person said or believes.** No fabricated
  quotes, screenshots, posts, letters or "interviews". Do not strip the simulation notice.
- **No endorsements, no persuasion campaigns.** Do not use simulations to make a person appear to
  endorse a product, a candidate, a cause or an investment.
- **No harassment or impersonation.** Do not use personas to target, mock, deceive or contact
  anyone, or to stand in for a person in a conversation with third parties.
- **Track records describe public predictions, with sources.** They are not judgments of a
  person's character.
- **Disclose model-vendor links.** If the model running the simulation is made by an organization
  that employs or is closely linked to a simulated person, say so in the run's limitations.

## Private individuals

Do not build personas of private individuals (friends, colleagues, family, mentors) without their
explicit permission. When a user wants to test something a friend said, record it as a "claim to
test" attributed to "a friend", not as a persona.

## Not professional advice

Runs produce structured arguments and disagreements, not advice. They do not replace a qualified
professional for legal, medical, financial, immigration or employment decisions. Several instances
of one model are not independent experts, whatever names they carry.

## Concerns and takedown

If you believe something in this repository misrepresents a person, contains personal data, or
infringes a right, open an issue with the **Content concern** template, or report it privately
through the repository's Security tab ("Report a vulnerability") if it involves personal data.
Content under a good-faith concern is removed first and discussed after.
