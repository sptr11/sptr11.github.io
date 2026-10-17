---
title: "Cristina: A Shared Home for the Web Pages Your AI Makes"
date: 2026-10-17
draft: true
summary: "AI assistants now produce reports, dashboards, and prototypes as web pages. There's no good place to put them where a team can see them. Cristina is that place."
tags: ["product", "ai", "side-project"]
---

AI assistants have quietly become very good at making web pages. Ask Claude to analyze a spreadsheet or sketch a feature and you often get back a polished HTML page with charts, tables, and working buttons.

Sharing that page with your team is surprisingly hard. Send the file and it lands in someone's downloads folder. Paste it into a doc or a wiki and the charts and scripts are stripped out. Take a screenshot and nobody can click anything. The best work your assistant produced ends up in one person's chat history.

I built [Cristina](https://cristina.cc) to give those pages a home. It's a wiki for HTML: you post a page, get a permanent link, and your team can open it, comment on it, and find it later.

## How it works

You can paste the HTML, upload a file, or have your agent post it directly:

```bash
curl -X POST https://cristina.cc/api/artifacts \
  -H "Authorization: Bearer <api-key>" \
  -H "Content-Type: application/json" \
  -d '{"title": "Q3 planning", "html": "<html>...</html>"}'
```

You get back a link. Teammates who open it see the page exactly as the assistant made it, scripts and all. New pages show up in a shared feed and can be sorted into folders. Teammates can pin comments to a specific chart or paragraph.

If your assistant supports MCP, an add-on called `cristina-mcp` lets it save pages to the wiki without you copying anything.

## Running untrusted pages safely

A wiki that runs arbitrary scripts is a security risk. A page could try to read the cookies of whoever opens it and take over their account.

Cristina displays each page in a sandboxed frame that lets scripts run but cuts them off from everything else. Charts animate and buttons work, but the page can't see the app around it, the viewer's login, or their stored data.

## Links that work for the whole team

A link is only useful if it works for whoever clicks it. Each Cristina link includes the team's name, like `cristina.cc/finch-labs/a/q3-planning`. A teammate who's signed in goes straight to the page. One who isn't gets a sign-in screen for that team and then lands on the page. Colleagues with the same company email domain can join automatically.

## Try it

Cristina is live at [cristina.cc](https://cristina.cc). It's in early preview with a waitlist, and the first 25 pages are free.
