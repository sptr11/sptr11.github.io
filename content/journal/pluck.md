---
title: "Pluck: Forms Your Users' AI Can Fill"
date: 2026-10-17
draft: true
summary: "Your users have already told their AI their budget, their timeline, and what they need built. Then you send them a form and make them type it all again."
tags: ["product", "ai", "side-project"]
---

Your users have already told their AI almost everything you're about to ask them. Their budget, their timeline, the project they need help with, the dates they're free. Then you send a Typeform link, and they open a browser and type it all out by hand.

That gap is what [Pluck](https://pluck.one) is built around. It's a form builder for a world where the person filling in the form usually has an assistant open in another tab.

## One URL, two readers

Every Pluck form lives at a single URL. A browser that opens it gets a normal HTML form. An agent that asks for JSON gets the same form as structured data: field names, types, rules, and the endpoint to submit to.

That's the whole integration. There's no SDK and no plugin. A recipient pastes the link into Claude or ChatGPT, the agent reads the fields, fills in what it already knows, asks for what it doesn't, and hands the answers back. A form that takes three minutes to type takes a few seconds to review.

The creator side works the same way. You tell your own agent what you need, it calls the Pluck API with an API key, and you get back a link. Your agent can read submissions through the same API later and summarize them.

## Probes

Pre-filling turned out to be the less interesting half. The feature that changed what the product is for is probes.

A probe is a follow-up question attached to a field. When someone gives a one-word answer to "What blocked you this week?", the form asks "How many days did that block you?" You write the probes once, when you create the form. A person sees them appear as they type. An agent sees them in the JSON and covers them in its draft.

That turns a form into something closer to an interview. Most forms collect thin answers because nothing on the page pushes back. Probes push back, politely, for every respondent.

## What I'd do differently

I built Pluck in the wrong order, and the order cost more than any single bug.

I shipped a polished design system, then found it broke the live form renderer. I wrote 40 use-case pages before probes existed, and every one of them had to be rewritten once they did. I built usage tracking and a tabbed admin dashboard when the product had four users. The worst one: early users told me agents were showing them empty forms. The core loop was broken, and I found out in week three when I could have found out in week one.

Then Render's free Postgres tier expired and deleted the production database. No warning, no export. The health check kept reporting "ok" the whole time because the startup database check swallowed its own error. The fix was one line. Learning that I needed it cost every form and submission in the system.

Each of those mistakes went into a starter I now use for every new project. That's the next post.
