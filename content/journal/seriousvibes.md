---
title: "seriousvibes: A Starter Kit for Building Apps With Coding Agents"
date: 2026-10-17
draft: false
summary: "Coding agents copy the patterns in your codebase. An empty project gives them nothing to copy, so each feature gets built a different way. seriousvibes starts them with the right patterns."
tags: ["engineering", "ai", "side-project"]
---

Coding agents are fast at producing an app and bad at keeping it consistent. Ask one for ten features and you get ten slightly different ways of doing things. One route checks permissions and the next doesn't. One page uses the brand color and the next hardcodes a hex value. By the second month, changing anything means changing it in ten places.

The reason is that agents learn from the code around them. When an agent adds a feature, it looks at what's already in the project and does something similar. In a fresh project there's nothing to look at, so it improvises, and it improvises differently each time.

<div style="max-width: 520px; margin: 2em auto; font-family: 'Inter', -apple-system, sans-serif;">
<svg viewBox="0 0 520 190" xmlns="http://www.w3.org/2000/svg" style="width: 100%;" role="img" aria-label="Left: an empty project, where ten features come out ten different ways. Right: a starter with patterns, where ten features come out the same way.">
  <text x="135" y="22" text-anchor="middle" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73" letter-spacing="0.1em">EMPTY PROJECT</text>
  <text x="385" y="22" text-anchor="middle" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73" letter-spacing="0.1em">PATTERNS TO COPY</text>
  <rect x="40" y="40" width="32" height="32" rx="3" fill="#2563EB"/>
  <rect x="82" y="40" width="32" height="32" rx="16" fill="#3B82F6"/>
  <rect x="124" y="40" width="32" height="32" rx="0" fill="none" stroke="#2563EB" stroke-width="2"/>
  <rect x="166" y="40" width="32" height="32" rx="3" fill="#A8A8B2"/>
  <rect x="208" y="40" width="32" height="32" rx="8" fill="#60A5FA" transform="rotate(10 224 56)"/>
  <rect x="40" y="82" width="32" height="32" rx="3" fill="none" stroke="#6E6E73" stroke-dasharray="4 3" stroke-width="2"/>
  <rect x="82" y="82" width="32" height="32" rx="0" fill="#1D4ED8"/>
  <rect x="124" y="82" width="32" height="32" rx="3" fill="#D4D4DA"/>
  <rect x="166" y="82" width="32" height="32" rx="16" fill="none" stroke="#3B82F6" stroke-width="3"/>
  <rect x="208" y="82" width="32" height="32" rx="5" fill="#93C5FD"/>
  <rect x="290" y="40" width="32" height="32" rx="3" fill="#2563EB"/>
  <rect x="332" y="40" width="32" height="32" rx="3" fill="#2563EB"/>
  <rect x="374" y="40" width="32" height="32" rx="3" fill="#2563EB"/>
  <rect x="416" y="40" width="32" height="32" rx="3" fill="#2563EB"/>
  <rect x="458" y="40" width="32" height="32" rx="3" fill="#2563EB"/>
  <rect x="290" y="82" width="32" height="32" rx="3" fill="#2563EB"/>
  <rect x="332" y="82" width="32" height="32" rx="3" fill="#2563EB"/>
  <rect x="374" y="82" width="32" height="32" rx="3" fill="#2563EB"/>
  <rect x="416" y="82" width="32" height="32" rx="3" fill="#2563EB"/>
  <rect x="458" y="82" width="32" height="32" rx="3" fill="#2563EB"/>
  <line x1="260" y1="36" x2="260" y2="150" stroke="#E8E8ED" stroke-width="1.5"/>
  <text x="135" y="146" text-anchor="middle" font-size="11" fill="#4A4A4F">10 features, 10 ways</text>
  <text x="385" y="146" text-anchor="middle" font-size="11" fill="#4A4A4F">10 features, 1 way</text>
  <text x="135" y="170" text-anchor="middle" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73">the agent improvises</text>
  <text x="385" y="170" text-anchor="middle" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73">the agent copies</text>
</svg>
</div>

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
