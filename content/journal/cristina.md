---
title: "Cristina: A Shared Home for the Web Pages Your AI Makes"
date: 2026-10-17
draft: true
summary: "AI assistants now produce reports, dashboards, and prototypes as web pages. There's no good place to put them where a team can see them. Cristina is that place."
tags: ["product", "ai", "side-project"]
---

AI assistants have quietly become very good at making web pages. Ask Claude to analyze a spreadsheet or sketch a feature and you often get back a polished HTML page with charts, tables, and working buttons.

Sharing that page with your team is surprisingly hard. Send the file and it lands in someone's downloads folder. Paste it into a doc or a wiki and the charts and scripts are stripped out. Take a screenshot and nobody can click anything. The best work your assistant produced ends up in one person's chat history.

<div style="max-width: 520px; margin: 2em auto; font-family: 'Inter', -apple-system, sans-serif;">
<svg viewBox="0 0 520 190" xmlns="http://www.w3.org/2000/svg" style="width: 100%;" role="img" aria-label="Ways to share an AI-made page. Sending the file keeps it working but gives no shared link. Pasting into a doc gives a link the team can find but strips scripts. A screenshot does none of the three. Cristina does all three.">
  <text x="260" y="18" text-anchor="middle" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73" letter-spacing="0.1em">SHARING A PAGE YOUR AI MADE</text>
  <text x="255" y="46" text-anchor="middle" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73">Works as made</text>
  <text x="355" y="46" text-anchor="middle" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73">One link</text>
  <text x="455" y="46" text-anchor="middle" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73">Team finds it later</text>
  <text x="24" y="78" font-size="11" fill="#4A4A4F">Send the file</text>
  <circle cx="255" cy="74" r="8" fill="#2563EB"/><path d="M251,74 L254,77 L259,71" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="350" y1="74" x2="360" y2="74" stroke="#C0C0C8" stroke-width="2" stroke-linecap="round"/>
  <line x1="450" y1="74" x2="460" y2="74" stroke="#C0C0C8" stroke-width="2" stroke-linecap="round"/>
  <text x="24" y="112" font-size="11" fill="#4A4A4F">Paste into a doc</text>
  <line x1="250" y1="108" x2="260" y2="108" stroke="#C0C0C8" stroke-width="2" stroke-linecap="round"/>
  <circle cx="355" cy="108" r="8" fill="#2563EB"/><path d="M351,108 L354,111 L359,105" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="455" cy="108" r="8" fill="#2563EB"/><path d="M451,108 L454,111 L459,105" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="24" y="146" font-size="11" fill="#4A4A4F">Screenshot</text>
  <line x1="250" y1="142" x2="260" y2="142" stroke="#C0C0C8" stroke-width="2" stroke-linecap="round"/>
  <line x1="350" y1="142" x2="360" y2="142" stroke="#C0C0C8" stroke-width="2" stroke-linecap="round"/>
  <line x1="450" y1="142" x2="460" y2="142" stroke="#C0C0C8" stroke-width="2" stroke-linecap="round"/>
  <rect x="12" y="160" width="496" height="32" rx="3" fill="#EEF3FE"/>
  <text x="24" y="180" font-size="11" font-weight="600" fill="#111">Cristina</text>
  <circle cx="255" cy="176" r="8" fill="#2563EB"/><path d="M251,176 L254,179 L259,173" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="355" cy="176" r="8" fill="#2563EB"/><path d="M351,176 L354,179 L359,173" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="455" cy="176" r="8" fill="#2563EB"/><path d="M451,176 L454,179 L459,173" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
</div>

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

<div style="max-width: 520px; margin: 2em auto; font-family: 'Inter', -apple-system, sans-serif;">
<svg viewBox="0 0 520 200" xmlns="http://www.w3.org/2000/svg" style="width: 100%;" role="img" aria-label="The posted page runs inside a sandboxed frame. Its scripts run, but it can't reach the app around it, the viewer's login, or their stored data.">
  <text x="260" y="18" text-anchor="middle" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73" letter-spacing="0.1em">SCRIPTS RUN. THEY JUST CAN'T LEAVE.</text>
  <rect x="20" y="40" width="210" height="140" rx="4" fill="#fff" stroke="#2563EB" stroke-width="1.5" stroke-dasharray="6 4"/>
  <text x="34" y="60" font-size="10" font-family="'JetBrains Mono', monospace" fill="#2563EB">sandboxed frame</text>
  <text x="34" y="82" font-size="11" font-weight="600" fill="#111">Q3 planning</text>
  <rect x="34"  y="132" width="22" height="30" fill="#D4D4DA"/>
  <rect x="62"  y="116" width="22" height="46" fill="#A8A8B2"/>
  <rect x="90"  y="100" width="22" height="62" fill="#2563EB"/>
  <rect x="118" y="122" width="22" height="40" fill="#C0C0C8"/>
  <rect x="160" y="146" width="56" height="16" rx="2" fill="#2563EB"/>
  <text x="188" y="157" text-anchor="middle" font-size="9" fill="#fff">Filter</text>
  <line x1="340" y1="38" x2="340" y2="182" stroke="#2563EB" stroke-width="3"/>
  <line x1="232" y1="62" x2="318" y2="62" stroke="#A8A8B2" stroke-width="1.5" stroke-dasharray="4 3"/><text x="326" y="66" font-size="13" font-weight="700" fill="#2563EB">×</text><rect x="350" y="47" width="150" height="30" rx="3" fill="#F5F5F7" stroke="#D4D4DA"/><text x="362" y="66" font-size="11" fill="#4A4A4F">The app around it</text>
  <line x1="232" y1="110" x2="318" y2="110" stroke="#A8A8B2" stroke-width="1.5" stroke-dasharray="4 3"/><text x="326" y="114" font-size="13" font-weight="700" fill="#2563EB">×</text><rect x="350" y="95" width="150" height="30" rx="3" fill="#F5F5F7" stroke="#D4D4DA"/><text x="362" y="114" font-size="11" fill="#4A4A4F">Viewer's login</text>
  <line x1="232" y1="158" x2="318" y2="158" stroke="#A8A8B2" stroke-width="1.5" stroke-dasharray="4 3"/><text x="326" y="162" font-size="13" font-weight="700" fill="#2563EB">×</text><rect x="350" y="143" width="150" height="30" rx="3" fill="#F5F5F7" stroke="#D4D4DA"/><text x="362" y="162" font-size="11" fill="#4A4A4F">Stored data</text>
</svg>
</div>

## Links that work for the whole team

A link is only useful if it works for whoever clicks it. Each Cristina link includes the team's name, like `cristina.cc/finch-labs/a/q3-planning`. A teammate who's signed in goes straight to the page. One who isn't gets a sign-in screen for that team and then lands on the page. Colleagues with the same company email domain can join automatically.

## Try it

Cristina is live at [cristina.cc](https://cristina.cc). It's in early preview with a waitlist, and the first 25 pages are free.
