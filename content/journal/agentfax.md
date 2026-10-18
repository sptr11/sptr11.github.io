---
title: "AgentFax: Send Your Agent's Work to Someone Outside the Chat"
date: 2026-10-17
draft: true
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

## Why a fax

The fax got one thing right. A document arrives, a person reads it, and an answer goes back. AgentFax keeps that.

Existing agent standards solve a different problem. MCP connects an agent to tools, and A2A connects one agent to another. Both assume software on both ends. AgentFax connects two people, whatever assistants they happen to use. The recipient needs nothing but a link, and there are no accounts.

## Try it

Start a fax server on your own machine with a public link:

```bash
npx agentfax serve --tunnel
```

AgentFax is free and open source. The [specification](https://github.com/sptr11/agentfax/blob/main/SPEC.md) takes about five minutes to read, so anyone can build a compatible server. The code is on GitHub at [github.com/sptr11/agentfax](https://github.com/sptr11/agentfax).
