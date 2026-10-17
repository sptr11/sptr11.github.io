---
title: "Cristina: A Wiki for the HTML Your Agents Make"
date: 2026-10-17
draft: true
summary: "Agents are good at producing HTML. Reports, prototypes, dashboards. Then the file sits in a chat window or a Downloads folder and nobody on the team ever sees it."
tags: ["product", "ai", "side-project"]
---

Agents have become very good at producing HTML. Ask Claude for a planning brainstorm or a metrics review and you often get a polished page with charts. Then it sits in a chat window or a Downloads folder. To share it, you screenshot it, or export a PDF that loses the interactivity, or paste it into a doc that strips it.

[Cristina](https://cristina.cc) gives those pages a permanent home. Post HTML, get a URL, share it with your team.

## One request, one link

The loop is three steps. Paste HTML from your assistant, upload a file, or have your agent POST it to `/api/artifacts` with an API key. You land on the rendered page, and the link is already in the address bar. Teammates open it, leave comments, and see new artifacts in their feed.

For agents that speak MCP, there's a small server, `cristina-mcp`, so Claude can save an artifact without anyone copying a file anywhere. Pages go into color-coded folders. Anything you don't file lands in an Unclassified folder so it doesn't disappear.

## Untrusted HTML, rendered safely

The interesting engineering problem is that every artifact is arbitrary HTML, often with scripts, and you're rendering it inside an app where your teammates are signed in.

Each artifact runs in an iframe with `sandbox="allow-scripts"` and nothing else. Scripts run, so charts and interactive prototypes work. The page can't read the parent's cookies, DOM, or storage. The tempting one-word fix for a misbehaving artifact is to add `allow-same-origin`, and that one word would defeat the sandbox entirely. The project instructions say so in bold, because a coding agent will reach for it.

Comments sit on top of all that. You can pin a comment to a specific element inside the artifact, and the pin follows the content as you scroll rather than staying fixed to the viewport.

## Links that know which team they belong to

Sharing turned out to be the harder product problem. A link pasted into Slack has to work for whoever clicks it.

Shared links carry the team's handle: `cristina.cc/finch-labs/a/q3-planning-brainstorm`. A teammate who's signed in lands straight on the artifact, in that team's context. A teammate who isn't sees a sign-in page branded with the team's name, then goes back to the artifact afterward. Someone with a matching work email domain joins automatically. Everyone else gets a clear "not accessible" page. Owners can rename a handle, and the old one keeps resolving so links already in Slack and email don't break.

Cristina was bootstrapped from [seriousvibes]({{< ref "seriousvibes" >}}), and it's the first project that started with those rules instead of discovering them. It's in early preview with a waitlist, and the first 25 artifacts are free.
