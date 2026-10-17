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

## Why a fax

The fax got one thing right. A document arrives, a person reads it, and an answer goes back. AgentFax keeps that.

Existing agent standards solve a different problem. MCP connects an agent to tools, and A2A connects one agent to another. Both assume software on both ends. AgentFax connects two people, whatever assistants they happen to use. The recipient needs nothing but a link, and there are no accounts.

## Try it

Start a fax server on your own machine with a public link:

```bash
npx agentfax serve --tunnel
```

AgentFax is free and open source. The [specification](https://github.com/sptr11/agentfax/blob/main/SPEC.md) takes about five minutes to read, so anyone can build a compatible server. The code is on GitHub at [github.com/sptr11/agentfax](https://github.com/sptr11/agentfax).
