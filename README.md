# pi-clarity

A [pi](https://github.com/earendil-works/pi) extension that adds a "Clear mode" communication instruction to the system prompt: lead with the answer, be concise, separate facts from assumptions.

Clear mode is on by default for every session. A `CLEAR` badge shows in the footer while it is active.

## How it works

Guidance loads in tiers so the always-on cost stays small.

1. **Core (always on).** `clarity.ts` appends a short block to the system prompt. It ends by pointing at the `documentation-style` skill.
2. **Skill.** `skills/documentation-style/SKILL.md` holds the default writing standard. The agent loads it when writing documentation or developer-facing text.
3. **Reference modules.** `skills/documentation-style/references/` holds detail. The skill tells the agent which single module to read:
   - `procedures.md`: steps a reader performs.
   - `reference-docs.md`: reference pages, commands, APIs.
   - `tone-and-language.md`: rewrites and tone.
   - `dev-artifacts.md`: commit messages, PR descriptions, READMEs, changelogs.
   - `code-and-comments.md`: code in prose, code samples, API doc comments.
   - `review.md`: final quality check.

Parts of the reference modules are adapted from the [Google developer documentation style guide](https://developers.google.com/style) (CC BY 4.0) and Google's [eng-practices](https://google.github.io/eng-practices/) guide. Each module notes what is Google-derived and what is a local standard.

## Install

Symlink the extension and the skill:

```sh
ln -s "$PWD/clarity.ts" ~/.pi/agent/extensions/clarity.ts
ln -s "$PWD/skills/documentation-style" ~/.pi/agent/skills/documentation-style
```

Restart pi.

## Usage

| Command | Effect |
| --- | --- |
| `/clarity` | Toggle |
| `/clarity on` / `off` | Set explicitly |
| `/clarity status` | Show current state |

State is stored per session. `/claity` is an alias for the common typo.

## Customize

Edit `CLARITY_INSTRUCTION` in `clarity.ts`.
