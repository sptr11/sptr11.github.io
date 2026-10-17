---
title: "AgentFax: The Fax Machine, Rebuilt for Agents"
date: 2026-10-17
draft: true
summary: "Your agent finished the work. Now it has to reach someone who isn't in your chat. AgentFax turns the result into a link that people and their agents can both read."
tags: ["ai", "open-source", "side-project"]
---

Your agent just finished something. A report, a proposal, a set of questions for a vendor. Now it has to reach a person who isn't in your chat, doesn't use your tools, and may have an agent of their own.

[AgentFax](https://github.com/sptr11/agentfax) turns that work into a link. The person opens a clean page. Their agent can open the same link and know exactly what it's looking at. If the page asks something, their agent drafts the answers and the person sends them back with one click.

## Why a fax

Faxes got one thing right. A document arrives, a person reads it, and an answer goes back. Everything else about them was terrible, so that's the only part I kept.

MCP connects an agent to tools. A2A connects an agent to another agent. Both are software talking to software, with servers on each end. AgentFax connects two people through whatever assistants they happen to use. The other side needs a link and nothing else.

## A reply is a link

The design question I spent the most time on was how an agent sends an answer back without being able to send anything.

Every fax page ends with a short section headed "For AI assistants." It lists the questions and gives the agent a reply template: the fax's own URL, with answers in the fragment after the `#`. The agent fills it in and hands the link to its person. They open it, see every answer pre-filled, and click Send.

Browsers don't send the fragment to the server. So nothing leaves until a person clicks, and an agent can draft every answer without being able to submit any of them. Many faxes have no questions at all. Those are a page to read, with an optional "Got it" button that works like the confirmation slip on an old fax.

## Tested against real assistants

The text of that agent section is fixed by the spec, byte for byte, because I tested assistants against exactly that wording. The testing turned up details that matter. Reply links under about 1,700 characters survived every assistant I tried. Gemini opens a link it composed as a Google search, so every fax also has a plain reply box as a fallback.

Sender content is a trust problem too. It renders in a sandbox with no network access, so it can display anything and transmit nothing. Sender text is also scrubbed of the phrases that would let it close the content block early and write a fake agent section underneath.

## Try it

AgentFax is a small open spec ("one page, two rules, six routes") and an MIT-licensed reference server on npm. Run `npx agentfax serve --tunnel` to get a public fax server on your machine. Then `npx agentfax send report.html --to priya --ask "Approve the Q3 numbers?"` gives you one link to send Priya and a private inbox link for yourself. There are no accounts. The link is the permission, and each recipient gets their own, so you know who replied.

[The spec](https://github.com/sptr11/agentfax/blob/main/SPEC.md) takes about five minutes to read.

The code is on GitHub at [github.com/sptr11/agentfax](https://github.com/sptr11/agentfax). Issues on the spec are welcome.
