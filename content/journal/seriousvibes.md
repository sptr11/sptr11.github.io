---
title: "seriousvibes: A Starter That Tells Your Coding Agent the Rules"
date: 2026-10-17
draft: true
summary: "A coding agent copies whatever is nearby. So the cheapest way to get good code out of one is to make sure the nearby code is already right."
tags: ["engineering", "ai", "side-project"]
---

A coding agent can write 10,000 lines in an afternoon. The trouble is what's in them. Copy that overclaims, a schema you'll rewrite next month, a query that forgot which tenant it belongs to, colors hardcoded into 40 components. It looks like a product. It costs more to fix than to rebuild.

I learned this building [Pluck]({{< ref "pluck" >}}). [seriousvibes](https://sptr11.github.io/seriousvibes/) is what I took away from it, packaged as a starter repo.

## Agents copy what's nearby

The observation behind it is simple. An agent writing a new route looks at the routes that already exist and does what they do. If the existing code scopes every query to a workspace, the new code will too. If there's a hex value in a component, there will soon be 20.

So seriousvibes ships a working app (auth, workspaces, API keys, a settings page, tests) where every line already follows the rules. Alongside it is an `AGENTS.md` that states those rules in plain language. Codex, Cursor, and Copilot read that file automatically. Claude Code reads `CLAUDE.md`, which imports it. The agent gets the rules in writing and correct examples to copy.

## The rules

Most of them came from a specific Pluck bug.

Every authenticated query filters on `workspace_id`, and every route needs a test where a user from another workspace asks for something and gets a 404. Pluck shipped a slug lookup without that filter. The tests passed because the test database only had one workspace. A leak between tenants is the one bug you can't take back, so the cross-workspace test is mandatory.

Tests come first, and they're fast. Vitest calls routes in-process with Hono's `app.request()` against a mocked database, so the whole suite runs in under a second. An agent will actually run a test suite that fast.

Colors, radius, shadows, and motion live in CSS variables with semantic names like `--color-accent`. A rebrand is a one-file change, and the agent never sees a raw hex value worth imitating. A copy guide does the same job for words: banned terms, error message patterns, and examples in your own product's vocabulary.

The `/health` route only answers when both the web and API processes are up. That one is from the night Pluck's database disappeared while its health check reported fine.

The last rule is about scope. Build only what the prompt asks for, and if you finish early, write tests. Agents are generous with features nobody requested.

## Sequence beats quality

The broader lesson from Pluck was that each piece I built was decent and the order was expensive. Content written before the differentiator exists has to be rewritten. UI built before the design tokens has to be retrofitted. Tenancy added after launch means touching every route.

seriousvibes encodes the cheap order. It also leaves things out on purpose: no marketing pages, no billing, no admin dashboard. Add them once you have users who need them.

The stack is Next.js 15, Hono, and Postgres with raw SQL and no ORM. Auth is about 260 lines of `bcryptjs` and `jose` that you own. It's MIT licensed, and you can start a project with `npx degit sptr11/seriousvibes myapp`.

The code is on GitHub at [github.com/sptr11/seriousvibes](https://github.com/sptr11/seriousvibes). If your agent ships a bug these rules should have caught, open an issue there.
