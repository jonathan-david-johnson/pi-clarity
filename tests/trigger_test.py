#!/usr/bin/env python3
"""Trigger test: does the agent load documentation-style and the right module?

Runs each prompt through `pi -p --mode json --no-session`, then inspects the
tool calls. A case passes when the skill and every expected module were read,
and (for negative cases) nothing from the skill was read.

Usage:
  tests/trigger_test.py [--model PATTERN] [--runs N] [--only SUBSTR] [--jobs N] [--thinking LEVEL]
"""
import argparse, json, os, re, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor

SKILL = "documentation-style/SKILL.md"
REF = re.compile(r"documentation-style/references/([\w-]+)\.md")

# (id, prompt, expected modules; empty set = skill must NOT load)
CASES = [
    ("commit", "Write a git commit message for this change: I renamed getUser to fetchUser across the repo because it makes a network call.", {"dev-artifacts"}),
    ("pr", "Write a pull request description for a change that adds retry with exponential backoff to our HTTP client. It fixes issue #412 where transient 503s failed whole batch jobs.", {"dev-artifacts"}),
    ("readme", "Write a README for a small CLI called `tidy` that deletes empty directories under a path. Output the README only.", {"dev-artifacts"}),
    ("changelog", "Write the changelog entry for v2.0.0: we removed the deprecated `--legacy` flag, added `--json` output, and fixed a crash on empty input.", {"dev-artifacts"}),
    ("docstring", "Write JSDoc comments for this function: function getBird(id, includeRetired = false) { /* returns a Bird or throws NotFoundError */ }", {"code-and-comments"}),
    ("code-prose", "Write a short reference paragraph describing what the API_TIMEOUT environment variable does, how config.yaml overrides it, and how the client.connect method uses it.", {"code-and-comments"}),
    ("procedure", "Write step-by-step instructions for installing and configuring Postgres 16 on Ubuntu for a first-time user.", {"procedures"}),
    ("review", "Review this doc for quality: 'Please note that it is simple to deploy. Just run the script here and the thing will be handled.'", {"review"}),
    # Negative controls: the skill should not load.
    ("neg-concept", "In two sentences, what is a mutex?", set()),
    ("neg-code", "Write a Python function that returns the nth Fibonacci number. Code only.", set()),
]


def run_case(args, case):
    cid, prompt, expected = case
    with tempfile.TemporaryDirectory() as cwd:
        cmd = ["pi", "-p", "--mode", "json", "--no-session", "--thinking", args.thinking]
        if args.model:
            cmd += ["--model", args.model]
        cmd.append(prompt)
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    skill, mods, calls = False, set(), []
    for line in p.stdout.splitlines():
        try:
            e = json.loads(line)
        except ValueError:
            continue
        if e.get("type") != "agent_end":
            continue
        for m in e.get("messages", []):
            if m.get("role") != "assistant" or not isinstance(m.get("content"), list):
                continue
            for b in m["content"]:
                if b.get("type") != "toolCall":
                    continue
                blob = json.dumps(b.get("arguments", {}))
                calls.append(b.get("name"))
                if SKILL in blob:
                    skill = True
                mods.update(REF.findall(blob))
    if expected:
        ok = skill and expected <= mods
    else:
        ok = not skill and not mods
    return cid, ok, skill, mods, expected, p.returncode


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model")
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--only")
    ap.add_argument("--thinking", default="off")
    ap.add_argument("--jobs", type=int, default=4)
    a = ap.parse_args()
    cases = [c for c in CASES if not a.only or a.only in c[0]] * a.runs
    with ThreadPoolExecutor(a.jobs) as ex:
        results = list(ex.map(lambda c: run_case(a, c), cases))
    fails = 0
    for cid, ok, skill, mods, expected, rc in results:
        fails += not ok
        print(f"{'PASS' if ok else 'FAIL'}  {cid:12} skill={skill!s:5} read={sorted(mods)} expected={sorted(expected)}" + (f" exit={rc}" if rc else ""))
    print(f"\n{len(results) - fails}/{len(results)} passed")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
