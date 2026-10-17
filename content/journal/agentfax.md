---
title: "AgentFax: The Fax Machine, Rebuilt for Agents"
date: 2026-10-17
draft: true
summary: "An AI agent finishes a report, but the person who needs it is outside the conversation. AgentFax turns the report into a link that both people and their assistants can read."
tags: ["ai", "open-source", "side-project"]
---

An AI agent finishes a report, a proposal, or a list of questions for a supplier. The person who needs it is not in the conversation, does not use the same tools, and may have an assistant of their own.

[AgentFax](https://github.com/sptr11/agentfax) turns the work into a link. The recipient opens a clean page. Their assistant can open the same link and understand it. If the page asks questions, the assistant drafts the answers and the person sends them with one click.

## Why a fax

The fax machine got one thing right: a document arrives, a person reads it, and an answer goes back. AgentFax keeps that and drops the rest.

Existing standards for AI agents solve different problems. MCP connects an agent to tools, and A2A connects one agent to another. Both need software on each end. AgentFax connects two people, whatever assistants they use. The recipient needs only a link.

## Replies are links

The central design problem was letting an assistant write a reply without letting it send one.

Every fax page ends with a short section addressed to AI assistants. It lists the questions and gives a template for the reply: the fax's own web address, with the answers added after a `#`. The assistant fills in the template and gives the link to its user. The user opens it, finds the answers already filled in, and clicks Send.

Browsers never send the part after the `#` to the server. So nothing leaves until a person clicks. The assistant can draft every answer but cannot submit any of them.

Many faxes ask nothing. They are simply pages to read, with an optional "Got it" button that works like the old confirmation slip.

## Testing with real assistants

The wording of the section for assistants is fixed by the specification, word for word, because it was tested against real assistants. The tests turned up practical limits. Reply links shorter than about 1,700 characters worked in every assistant tried. Gemini opens links it writes as a Google search, so every fax also has a plain reply box.

The sender is not fully trusted either. Their content runs in a sandbox that cannot reach the network, so it can display anything but send nothing. Phrases that could be used to fake the assistant section are rewritten before display.

## Trying it

AgentFax is a short open specification and a free server, published on npm. Run `npx agentfax serve --tunnel` to start a fax server on your own machine. Then `npx agentfax send report.html --to priya --ask "Approve the Q3 numbers?"` gives you one link to send to Priya and a private inbox link for yourself. There are no accounts. Each recipient gets a separate link, so you know who replied.

[The specification](https://github.com/sptr11/agentfax/blob/main/SPEC.md) takes about five minutes to read. The code is on GitHub at [github.com/sptr11/agentfax](https://github.com/sptr11/agentfax), and comments on the spec are welcome there.
