# Developer artifacts

Use this module for commit messages, pull request descriptions, READMEs, changelogs, and release notes.

If the project has its own convention (for example Conventional Commits, a PR template, or a CHANGELOG format), follow it. Apply the rules below only where the project is silent.

## Commit messages and pull request descriptions

A description is a permanent record. A future reader will find it by search, often without remembering the details. It must say what changed and why.

- Write the first line as a short, specific summary of what the change does. It must stand alone in a history list.
- Write the first line as a complete sentence in the imperative: "Delete the unused RPC", not "Deleting the unused RPC" or "Deleted".
- Leave a blank line after the first line.
- Use the body for the reason, not a restatement of the diff. Cover the problem, why this approach, known shortcomings, and decisions the code does not show.
- Include supporting facts: bug or issue numbers, benchmark results, and links to design documents.
- Do not depend on an external link alone. It may become inaccessible. State enough context in the description.
- Give small changes a little context too.
- The body does not need to be imperative.

Reject summaries that name no subject or action: "Fix bug", "Fix build", "Add patch", "Phase 1", "Moving code from A to B".

For a pull request, restate the same two facts (what and why). Add how to verify the change when a reviewer needs it.

## README

- Open with what the project is and who it is for, in one or two sentences.
- Put the fastest path to a working result next: install, then a minimal usage example.
- Follow `references/procedures.md` for install and setup steps.
- Follow `references/reference-docs.md` for command, option, and configuration listings.
- Put requirements and supported platforms before the steps that depend on them.
- Link to deeper documentation instead of duplicating it.
- State the license.

## Changelogs and release notes

- Group entries by reader impact: breaking changes first, then features, fixes, and deprecations.
- Describe the effect on the user, not the internal change.
- For a deprecation, name the replacement and what to change.
- Name the version and date unambiguously.

## Provenance

The commit and pull request rules come from Google's "Writing good CL descriptions" in the eng-practices guide. The README and changelog rules are local standards, not taken from the Google developer documentation style guide.
