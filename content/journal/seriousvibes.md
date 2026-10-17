---
title: "seriousvibes: A Starter Kit That Teaches Coding Agents the Rules"
date: 2026-10-17
draft: true
summary: "Coding agents imitate the code around them. seriousvibes makes sure that code is right from the first commit."
tags: ["engineering", "ai", "side-project"]
---

A coding agent can write 10,000 lines of code in an afternoon. Much of it will need rewriting. The copy overclaims, the database schema changes next month, colors are hardcoded into dozens of components, and a query forgets which customer's data it is reading. The result looks like a product but costs more to fix than to rebuild.

[seriousvibes](https://sptr11.github.io/seriousvibes/) is a starter kit meant to prevent that. It grew out of the mistakes made building [Pluck]({{< ref "pluck" >}}).

## The idea

Agents imitate. When an agent writes a new feature, it looks at the existing code and follows its patterns. If existing queries are scoped to a single customer, new ones will be too. If one component contains a hardcoded color, others soon will.

So seriousvibes ships a small working app, with sign-in, team workspaces, API keys, a settings page, and tests, in which every line already follows the rules. A file called `AGENTS.md` states those rules in plain English. Codex, Cursor, and Copilot read it automatically, and Claude Code reads it through `CLAUDE.md`. The agent gets both instructions and examples.

## The rules

Most rules trace back to a specific bug.

Every query that touches customer data must filter by workspace, and every route needs a test in which a user from another workspace is refused. Pluck once shipped a lookup without that filter. Its tests passed because the test database held only one workspace. Leaking one customer's data to another is the bug that cannot be undone, so the test is compulsory.

Tests come first and run quickly. The whole suite finishes in under a second, which means an agent will actually run it.

Colors, spacing, and fonts are defined once, under names such as `--color-accent`, so a redesign means editing one file. A copy guide does the same for words. It lists banned phrases and gives examples of error messages written in the product's own vocabulary.

The health check reports success only when both the website and the API are running. That rule dates from the night Pluck's database vanished while its health check said all was well.

The last rule is about restraint. The agent should build only what it was asked to build, and spend any spare time writing tests.

## Order matters

The broader lesson from Pluck was that sequence matters more than polish. Marketing written before the product's main feature exists has to be rewritten. Screens built before the design system have to be redone. Support for multiple customers added after launch means changing every route.

seriousvibes builds in a cheaper order and leaves out what can wait: marketing pages, billing, and admin dashboards. Those should come once there are users who need them.

It uses Next.js, Hono, and Postgres, with plain SQL and about 260 lines of sign-in code you own outright. It is free under the MIT license. Start a project with `npx degit sptr11/seriousvibes myapp`.

The code is on GitHub at [github.com/sptr11/seriousvibes](https://github.com/sptr11/seriousvibes). If your agent ships a bug these rules should have caught, open an issue there.
