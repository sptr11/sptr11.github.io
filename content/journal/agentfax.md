---
title: "AgentFax: Send Your Agent's Work to Someone Outside the Chat"
date: 2026-10-17
draft: false
summary: "When your AI agent produces something another person needs to read or answer, there's no clean way to get it to them. AgentFax turns it into a link that both they and their assistant can use."
tags: ["ai", "open-source", "side-project"]
---

My AI agent often finishes work that someone else needs. A report for a client. A proposal that needs a yes or no. A list of questions for a supplier.

Getting it to that person is clumsy. I can paste it into an email, where the formatting breaks and the replies come back as loose paragraphs I have to match to questions. I can share a doc, which they have to read and answer by hand. And if they have an AI assistant of their own, which they increasingly do, it usually can't help, because it can't reliably read whatever I sent.

[AgentFax](https://github.com/sptr11/agentfax) is my answer. It turns your agent's work into a link. The recipient opens a clean page. Their assistant can open the same link and understand it. If the page asks questions, their assistant drafts the answers, and they send them back with one click.

## How it works

You send a page with one command:

```bash
npx agentfax send report.html --to priya --ask "Approve the Q3 numbers?"
# → https://fax.example.com/f/k3J9xQ   send this to Priya
# → https://fax.example.com/i/Zp81wL   your inbox
```

Priya opens her link and reads the report. If she wants help, she pastes the link into whatever assistant she uses. At the bottom of every page is a short section written for AI assistants. It explains the questions and gives a template for the reply.

The reply is itself a link: the same address, with the answers added after a `#`. Her assistant fills in the template and hands her the link. She opens it, sees the answers already filled in, and clicks Send.

That design has a useful property. Browsers never send the part of a link after the `#` to the server, so nothing leaves until Priya clicks. Her assistant can draft every answer, but only she can send them.

<div style="max-width: 520px; margin: 2em auto; font-family: 'Inter', -apple-system, sans-serif;">
<svg viewBox="0 0 520 280" xmlns="http://www.w3.org/2000/svg" style="width: 100%;" role="img" aria-label="You send a page and get two links. Priya opens hers, her assistant reads the same link and drafts answers into a reply link after the hash. Nothing reaches the server until Priya clicks Send, then the answers land in your inbox.">
  <defs><marker id="af-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#A8A8B2"/></marker></defs><defs><marker id="af-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#2563EB"/></marker></defs>
  <g font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73" letter-spacing="0.1em">
    <text x="112" y="24">YOU</text>
    <text x="112" y="114">FAX SERVER</text>
    <text x="112" y="204">PRIYA + HER ASSISTANT</text>
  </g>
  <line x1="10" y1="96" x2="510" y2="96" stroke="#E8E8ED"/>
  <line x1="10" y1="186" x2="510" y2="186" stroke="#E8E8ED"/>
  <rect x="10" y="32" width="92" height="40" rx="3" fill="#F5F5F7" stroke="#D4D4DA"/><text x="56" y="49" text-anchor="middle" font-size="10" font-weight="600" fill="#111">agentfax send</text><text x="56" y="63" text-anchor="middle" font-size="9" fill="#6E6E73">report.html</text>
  <rect x="10" y="122" width="92" height="40" rx="3" fill="#F5F5F7" stroke="#D4D4DA"/><text x="56" y="139" text-anchor="middle" font-size="10" font-weight="600" fill="#111">stores the page</text><text x="56" y="153" text-anchor="middle" font-size="9" fill="#6E6E73">returns two links</text>
  <rect x="112" y="212" width="92" height="40" rx="3" fill="#F5F5F7" stroke="#D4D4DA"/><text x="158" y="229" text-anchor="middle" font-size="10" font-weight="600" fill="#111">opens /f/k3J9xQ</text><text x="158" y="243" text-anchor="middle" font-size="9" fill="#6E6E73">reads the report</text>
  <rect x="214" y="212" width="92" height="40" rx="3" fill="#F5F5F7" stroke="#D4D4DA"/><text x="260" y="229" text-anchor="middle" font-size="10" font-weight="600" fill="#111">her assistant</text><text x="260" y="243" text-anchor="middle" font-size="9" fill="#6E6E73">drafts answers</text>
  <rect x="316" y="212" width="92" height="40" rx="3" fill="#F5F5F7" stroke="#D4D4DA"/><text x="362" y="229" text-anchor="middle" font-size="10" font-weight="600" fill="#111">opens reply link</text><text x="362" y="243" text-anchor="middle" font-size="9" fill="#6E6E73">#answers prefilled</text>
  <rect x="418" y="212" width="92" height="40" rx="3" fill="#2563EB" stroke="#2563EB"/><text x="464" y="236" text-anchor="middle" font-size="10" font-weight="600" fill="#fff">clicks Send</text>
  <rect x="418" y="122" width="92" height="40" rx="3" fill="#F5F5F7" stroke="#D4D4DA"/><text x="464" y="146" text-anchor="middle" font-size="10" font-weight="600" fill="#111">records reply</text>
  <rect x="418" y="32" width="92" height="40" rx="3" fill="#2563EB" stroke="#2563EB"/><text x="464" y="49" text-anchor="middle" font-size="10" font-weight="600" fill="#fff">your inbox</text><text x="464" y="63" text-anchor="middle" font-size="9" fill="#DCE6FD">/i/Zp81wL</text>
  <path d="M56,72 L56,120" fill="none" stroke="#A8A8B2" stroke-width="1.5" marker-end="url(#af-a)"/>
  <path d="M56,162 L56,232 L110,232" fill="none" stroke="#A8A8B2" stroke-width="1.5" marker-end="url(#af-a)"/>
  <path d="M204,232 L212,232" fill="none" stroke="#A8A8B2" stroke-width="1.5" marker-end="url(#af-a)"/>
  <path d="M306,232 L314,232" fill="none" stroke="#A8A8B2" stroke-width="1.5" marker-end="url(#af-a)"/>
  <path d="M408,232 L416,232" fill="none" stroke="#2563EB" stroke-width="1.5" marker-end="url(#af-b)"/>
  <path d="M464,212 L464,164" fill="none" stroke="#2563EB" stroke-width="1.5" marker-end="url(#af-b)"/>
  <path d="M464,122 L464,74" fill="none" stroke="#2563EB" stroke-width="1.5" marker-end="url(#af-b)"/>
  <text x="311" y="138" text-anchor="middle" font-size="10" font-family="'JetBrains Mono', monospace" fill="#2563EB">everything after # stays</text>
  <text x="311" y="152" text-anchor="middle" font-size="10" font-family="'JetBrains Mono', monospace" fill="#2563EB">in her browser until Send</text>
</svg>
</div>

## A person and an agent, on both ends

The way we write and read has changed. More of what I send starts as a draft from my agent. More of what I receive gets read first by the recipient's assistant, which summarizes it, answers what it can, and flags the rest for them. On each end of most exchanges now sits a pair: a person and their agent.

No protocol was built for that pair. Email and shared docs assume a person on each end, so the agent has to scrape text written for human eyes. MCP connects an agent to tools, and A2A connects one agent to another, so the person drops out. Each one serves half of the pair.

<div style="max-width: 520px; margin: 2em auto; font-family: 'Inter', -apple-system, sans-serif;">
<svg viewBox="0 0 520 230" xmlns="http://www.w3.org/2000/svg" style="width: 100%;" role="img" aria-label="Who each protocol connects. Email and docs connect two people, so agents have to scrape them. MCP connects an agent to tools and A2A connects two agents, with no person in the loop. AgentFax connects a person and their agent to another person and their agent.">
  <text x="260" y="18" text-anchor="middle" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73" letter-spacing="0.1em">WHO EACH PROTOCOL CONNECTS</text>
  <circle cx="60" cy="56" r="8" fill="#4A4A4F"/>
  <line x1="86" y1="56" x2="164" y2="56" stroke="#C0C0C8" stroke-width="1.5"/>
  <circle cx="190" cy="56" r="8" fill="#4A4A4F"/>
  <text x="236" y="60" font-size="11" font-weight="600" fill="#111">Email, docs</text>
  <text x="330" y="60" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73">the agent has to scrape it</text>
  <rect x="52" y="88" width="16" height="16" rx="3" fill="#2563EB"/>
  <line x1="86" y1="96" x2="164" y2="96" stroke="#C0C0C8" stroke-width="1.5"/>
  <rect x="182" y="88" width="16" height="16" rx="1" fill="none" stroke="#6E6E73" stroke-width="1.5"/>
  <text x="236" y="100" font-size="11" font-weight="600" fill="#111">MCP</text>
  <text x="330" y="100" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73">no person in the loop</text>
  <rect x="52" y="128" width="16" height="16" rx="3" fill="#2563EB"/>
  <line x1="86" y1="136" x2="164" y2="136" stroke="#C0C0C8" stroke-width="1.5"/>
  <rect x="182" y="128" width="16" height="16" rx="3" fill="#2563EB"/>
  <text x="236" y="140" font-size="11" font-weight="600" fill="#111">A2A</text>
  <text x="330" y="140" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73">no person in the loop</text>
  <rect x="12" y="158" width="496" height="36" rx="3" fill="#EEF3FE"/>
  <circle cx="50" cy="176" r="8" fill="#4A4A4F"/><rect x="62" y="168" width="16" height="16" rx="3" fill="#2563EB"/>
  <line x1="86" y1="176" x2="164" y2="176" stroke="#2563EB" stroke-width="1.5"/>
  <circle cx="180" cy="176" r="8" fill="#4A4A4F"/><rect x="192" y="168" width="16" height="16" rx="3" fill="#2563EB"/>
  <text x="236" y="180" font-size="11" font-weight="600" fill="#111">AgentFax</text>
  <text x="330" y="180" font-size="10" font-family="'JetBrains Mono', monospace" fill="#2563EB">built for the pair</text>
  <circle cx="150" cy="214" r="8" fill="#4A4A4F"/><text x="162" y="218" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73">person</text>
  <rect x="232" y="206" width="16" height="16" rx="3" fill="#2563EB"/><text x="252" y="218" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73">agent</text>
  <rect x="316" y="206" width="16" height="16" rx="1" fill="none" stroke="#6E6E73" stroke-width="1.5"/><text x="336" y="218" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73">tool</text>
</svg>
</div>

AgentFax is built for both halves. Every page carries a part for the person and a part for their assistant. The assistant does the reading and drafting. The person keeps the decision, because nothing goes back until they click Send.

## Why a fax

The fax got one thing right. A document arrives, a person reads it, and an answer goes back. AgentFax keeps that, whatever assistants the two people happen to use. The recipient needs nothing but a link, and there are no accounts.

## Try it

Start a fax server on your own machine with a public link:

```bash
npx agentfax serve --tunnel
```

AgentFax is free and open source. The [specification](https://github.com/sptr11/agentfax/blob/main/SPEC.md) takes about five minutes to read, so anyone can build a compatible server. The code is on GitHub at [github.com/sptr11/agentfax](https://github.com/sptr11/agentfax).
