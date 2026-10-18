---
title: "Agents Can Work Across Companies. Nobody Can Prove What Was Approved."
date: 2026-10-18
draft: false
summary: "Inside a company, agents now get logins, tool access, and approval steps. Between companies, the work still runs through people, one side writes all the rules, and outside of payments there's no record of who approved what."
tags: ["ai", "agents", "research"]
---

More of my work now starts as a draft from an agent. A status update for a client. A reply to a supplier. A list of questions for a new vendor. More of what I receive gets read first by the other person's agent, which summarizes it, answers what it can, and flags the rest for them.

So on each end of a lot of business communication there is now a pair: a person and their agent. I wanted to know how that actually works today, so I spent a few weeks going through the protocols, the deployments, the standards drafts, and the research. The full report is [How humans and agents talk](/humans-and-agents/). This post covers how I'd frame the problem and what I think is missing.

## Two halves

The useful split is inside a company versus across companies.

Inside one company, the hard questions mostly have answers. Everyone signs in through the same identity provider, works under the same policies, and answers to the same legal entity. Agents now get identities and owners the way employees do, through products like [Okta's Agent SSO](https://www.okta.com/en-gb/newsroom/press-releases/okta-brings-first-class-identity-to-ai-agents-with-agent-sso/) and Microsoft's Agent 365. MCP connects them to the company's tools, and a person approves anything that leaves the building or moves money. The main gap inside is agents the company can't see: workers at more than 90% of companies use personal AI tools for work, while only 40% of companies pay for an official subscription, according to [MIT's NANDA project](https://virtualizationreview.com/articles/2025/08/19/mit-report-finds-most-ai-business-investments-fail-reveals-genai-divide.aspx).

Across companies, none of that holds. There's no shared login, no shared policy, and at most a contract between the two sides. Every question gets harder. Who is this? May they see this? Can they commit their company? And when something goes wrong, whose record wins?

## What actually happens across companies

I catalogued 25 public deployments where agent work crosses a company line. Only two put an AI agent on both sides: a data-sharing pilot between [Tyson Foods and Gordon Food Service](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade), and a [2023 contract-negotiation demo](https://www.cnbc.com/2023/11/07/ai-negotiates-legal-contract-without-humans-involved-for-first-time.html). Neither commits anyone to anything.

Everything with real volume falls into three patterns. One company's agent deals with another company's people, as when Walmart's negotiation agent bargains with supplier reps, or a freight broker's agent books carriers by email and phone. An agent pays a posted price, mostly developer tools paying per API call. Or agents draft and people send. That last one is plausibly the biggest of the three, and nobody measures it.

The protocol built for agent-to-agent work, A2A, has more than 150 supporting organizations and no named deployment between two companies. The plumbing exists. The traffic is going through people.

## One side writes the rules

Every autonomous exchange I found runs inside limits that one party set alone. Walmart sets the ceiling, and the supplier's rep accepts or declines. [project44's freight agent](https://www.ajot.com/news/project44-launches-ai-freight-procurement-agent) renews contracts "within approved limits" and sends anything new to a person. Chain's booking agent takes a start, target, and maximum rate from the broker's system and escalates when a carrier asks for more.

So approval has moved from each message to the envelope as a whole, which is what makes these agents fast. But only the buyer wrote the envelope. None of the 25 deployments has two companies' agents comparing their limits with each other. That's fine while the other side is a person. It breaks the moment both sides send agents.

## What's missing

The transport is settled. MCP and A2A both sit in the Linux Foundation's [Agentic AI Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation), and identity is converging on a couple of IETF drafts. What's missing is everything about approval between companies that have never set up trust with each other. Six pieces, specifically.

### A signed approval for anything that isn't a payment

Card payments already solved this for agents. In Mastercard's [Verifiable Intent](https://verifiableintent.dev/spec/credential-format), a bank binds the person to a key, the person signs a mandate with limits, and the agent signs the final action, so a merchant that has never met the person can check the whole chain. Nothing like it exists for a purchase order, a contract term, a credit, or a data release. The structure would carry over. What's missing is the issuer: the role a bank plays in payments has no counterpart in a company's identity provider.

### A way for one company to vouch for its employee to another

Today your agent can reach a vendor's app through your company's identity provider, but only because you already have an account there. The IETF drafts that could express "Company A's agent, acting for Priya, may do X at Company B" all require B to know Priya already. [Microsoft](https://learn.microsoft.com/en-us/entra/agent-id/agent-identities) says its agent identities "can't access resources or APIs in other tenants," and [NIST](https://www.nccoe.nist.gov/sites/default/files/2026-02/accelerating-the-adoption-of-software-and-ai-agent-identity-and-authorization-concept-paper.pdf) left outside agents out of its first project.

### A way to compare limits before negotiating

Two agents bargaining for two companies need to disclose what each may agree to, and check the other's, before trading anything. Without that step, the research isn't encouraging. In Microsoft's [Magentic Marketplace](https://arxiv.org/html/2510.25779v1), every model tested took the first acceptable offer 60% to 100% of the time.

### A way to take an approval back

The delegations an agent holds while its person is away can last up to 30 days in Verifiable Intent, and no specification I reviewed can revoke one early. Everything else relies on tokens that expire in minutes.

### Proof of which company sent a message

Email has DKIM, so a receiver can check the sending domain. A message delivered as a link proves which server hosted it, not which company wrote it. The pieces for a fix exist in A2A's signed cards and Web Bot Auth's key directories. Nobody has applied them to a message a person sends.

### An approval step the agent can't write

The Send button is the right control. Security researchers call the dangerous setup the [lethal trifecta](https://simonwillison.net/2025/Jul/06/supabase-mcp-lethal-trifecta/): an agent that reads untrusted input, can reach private data, and can send. But [people approve 93% of permission prompts](https://anthropic.com/engineering/claude-code-auto-mode). An approval screen only protects anyone if it shows the raw outbound fields and the agent had no hand in drawing it.

## Where it will probably come from

Probably from a big buyer. The last time companies wired their machines together, Walmart told its suppliers in 2002 to move to Internet EDI within a year, before the protocol was even a finished standard. The hubs setting the limits for agents today, in retail procurement and freight tendering, are in the same position.

A mandate buys compliance, though, not real use. The record has to be worth something to the supplier too. Payments show how that works: a mandate is the evidence a merchant uses in a chargeback.

The timing is also odd. Email got its trust layer decades after the transport. Agents are getting pieces of theirs early and out of order. Network edges like Cloudflare already enforce agent verification before the IETF has finished the standard, and acquirers have paid or agreed to pay about $41B for identity and security companies on the strength of agent identity, before any vendor reports real agent revenue. The groups most likely to standardize the missing layer, FIDO's new Agentic Authentication working group and the IETF's AIMS profile, convened only this year. They're what I'll be watching.

## Read the report

The full report is at [How humans and agents talk](/humans-and-agents/). It covers each work pattern inside and across companies, the protocols, the history from EDI to email to 1990s agent research, who's competing for which layer, and 221 sources. It's also listed under [research](/research/).
