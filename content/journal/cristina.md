---
title: "Cristina: A Wiki for the Pages Your Agents Make"
date: 2026-10-17
draft: true
summary: "AI assistants now produce polished web pages: reports, prototypes, and dashboards. Most end up stranded in a chat window. Cristina gives them a link."
tags: ["product", "ai", "side-project"]
---

Ask an AI assistant for a planning summary or a sales review and it will often produce a polished web page, complete with charts. Then the page sits in a chat window or a downloads folder. Sharing it means a screenshot, a PDF that loses the interactive parts, or a document that strips the formatting.

[Cristina](https://cristina.cc) is a team wiki for these pages. You post the HTML, get a link, and share it.

## How it works

There are three ways in. You can paste the page, upload a file, or have an agent send it through the API. You land on the finished page with its link in the address bar. Colleagues open the link, comment, and see new pages in a shared feed.

Agents that use MCP, a common standard for connecting AI tools, can save pages directly through a small add-on called `cristina-mcp`. Pages are sorted into color-coded folders. Anything left unsorted goes to an "Unclassified" folder rather than getting lost.

## The security problem

Every page is arbitrary code, often including scripts, and it is displayed inside an app where colleagues are signed in. A malicious page could try to read their login cookies.

Cristina runs each page in a sandbox that permits scripts and nothing else. Charts and prototypes work, but the page cannot reach the surrounding app. One setting, `allow-same-origin`, would quietly undo that protection. It is a tempting fix when a page misbehaves, so the project's instructions to coding agents forbid it in bold.

Comments can be pinned to a particular chart or paragraph, and the pin stays with that element as the page scrolls.

## Sharing

The harder problem was sharing. A link pasted into Slack has to work for whoever clicks it.

Each link carries the team's name, as in `cristina.cc/finch-labs/a/q3-planning`. A colleague who is signed in goes straight to the page. One who is not sees a sign-in screen bearing the team's name, then returns to the page. Someone with a company email address joins the team automatically, and anyone else is turned away. If a team renames itself, old links keep working.

Cristina was built on [seriousvibes]({{< ref "seriousvibes" >}}). It was the first project to start with those rules rather than learn them the hard way. It is in early preview with a waitlist, and the first 25 pages are free.

Cristina is live at [cristina.cc](https://cristina.cc).
