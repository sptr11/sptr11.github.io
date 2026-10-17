---
title: "Pluck: Forms Your Users' AI Can Fill"
date: 2026-10-17
draft: true
summary: "People tell their AI assistants their budgets, deadlines, and plans. Then a form asks them to type it all again. Pluck lets the assistant fill it in."
tags: ["product", "ai", "side-project"]
---

Anyone who uses an AI assistant has told it a great deal. It knows their budget, their deadlines, and the project they want help with. Yet when a vendor sends them an intake form, they open a browser and type the same facts in by hand.

[Pluck](https://pluck.one) is a form builder designed around that waste. A Pluck form can be filled in by a person, by the person's assistant, or by both working together.

## How it works

Each form has one web address. Open it in a browser and you see an ordinary form. Ask the same address for JSON, as an agent does, and you get the form as structured data: the fields, their types, the rules, and where to submit.

No plugin or software kit is needed. A recipient pastes the link into Claude or ChatGPT. The assistant reads the fields, fills in what it knows, asks about the rest, and returns the answers for the person to check. A form that takes three minutes to type takes seconds to review.

Creators work the same way. They describe the form to their own agent, which builds it through Pluck's API and returns a link. Later the agent can read the submissions and summarize them.

## Follow-up questions

Pre-filling is the obvious feature. The more useful one is the follow-up question, which Pluck calls a probe.

A creator can attach probes to any field. If someone answers "What blocked you this week?" with one word, the form asks "How many days did that cost you?" People see the probe appear as they type. Agents see it in the JSON and answer it in their draft. Most forms collect thin answers because nothing on the page asks for more. Probes do.

## What went wrong

Pluck was built in the wrong order, and the order cost more than any single bug.

A polished design system broke the live form renderer. Forty pages describing use cases were written before probes existed, and all had to be redone once they did. An admin dashboard was built when the product had four users. Worst of all, the core loop was broken for weeks: agents were showing people empty forms. Users reported it in week three. A simple end-to-end test would have caught it in week one.

Then the hosting provider's free database plan expired, and the production database was deleted. There was no warning and no backup. The site's health check reported "ok" throughout, because the code that tested the database connection ignored its own errors. Fixing that took one line. Not having it cost every form and every response.

Those lessons became a starter kit, [seriousvibes]({{< ref "seriousvibes" >}}), which is the subject of the next post.

Pluck is live at [pluck.one](https://pluck.one).
