# pi-clarity

A [pi](https://github.com/earendil-works/pi) extension that adds a "Clear mode" communication instruction to the system prompt: lead with the answer, be concise, separate facts from assumptions.

Clear mode is on by default for every session. A `CLEAR` badge shows in the footer while it is active.

## Install

Copy or symlink `clarity.ts` into `~/.pi/agent/extensions/`:

```sh
ln -s "$PWD/clarity.ts" ~/.pi/agent/extensions/clarity.ts
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
