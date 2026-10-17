---
title: "seriousvibes: A Starter Kit for Building Apps With Coding Agents"
date: 2026-10-17
draft: true
summary: "Coding agents copy the patterns in your codebase. An empty project gives them nothing to copy, so each feature gets built a different way. seriousvibes starts them with the right patterns."
tags: ["engineering", "ai", "side-project"]
---

Coding agents are fast at producing an app and bad at keeping it consistent. Ask one for ten features and you get ten slightly different ways of doing things. One route checks permissions and the next doesn't. One page uses the brand color and the next hardcodes a hex value. By the second month, changing anything means changing it in ten places.

The reason is that agents learn from the code around them. When an agent adds a feature, it looks at what's already in the project and does something similar. In a fresh project there's nothing to look at, so it improvises, and it improvises differently each time.

[seriousvibes](https://sptr11.github.io/seriousvibes/) is a starter kit that gives the agent something good to copy from the first prompt.

## What's in it

It's a small, working web app: sign-in, team workspaces, API keys, a settings page, and a test suite. Every part of it follows the same handful of rules, so whatever the agent builds next follows them too.

The rules are also written down, in a file called `AGENTS.md`. Codex, Cursor, and Copilot read that file automatically, and Claude Code picks it up through `CLAUDE.md`. The agent gets the rules in writing and working examples of each.

## The rules

Each team's data stays separate. Every database query filters by workspace, and every feature needs a test proving that a user from another team can't see its data. This is the bug that's easiest to write and hardest to apologize for.

Tests come first, and they're fast. The whole suite runs in under a second, which is fast enough that an agent will actually run it after every change.

Colors, spacing, and fonts are defined in one file. Components refer to names like `--color-accent`, never to raw values, so a redesign is a one-file change. A copy guide does the same for wording, with examples of error messages and buttons written properly.

Scope is limited. The agent builds only what it was asked to build. If it finishes early, it writes tests instead of adding features.

## Try it

seriousvibes uses Next.js, Hono, and Postgres, with plain SQL and no ORM. It's free under the MIT license. To start a project:

```bash
npx degit sptr11/seriousvibes myapp
```

The README walks through renaming it and making the rules your own. The code is on GitHub at [github.com/sptr11/seriousvibes](https://github.com/sptr11/seriousvibes). If your agent ships a bug these rules should have caught, open an issue there.
