---
title: "Pluck: Forms That AI Assistants Can Fill In"
date: 2026-10-17
draft: true
summary: "Online forms are invisible to AI assistants, so people retype answers their assistant already knows. Pluck serves every form in a format agents can read and submit."
tags: ["product", "ai", "side-project"]
---

Online forms were designed for a person typing into a browser. That made sense until recently. Now many people have an AI assistant that already knows the answers: their company's details, their budget, their deadlines, the project they need help with.

But hand that assistant a Typeform or Google Forms link and it usually can't do anything with it. These forms are built in JavaScript, and the tools assistants use to read web pages generally don't run JavaScript. The assistant sees an empty page. So the person reads the questions and types out, by hand, facts their assistant could have supplied in seconds.

I built [Pluck](https://pluck.one) to fix that. It's a form builder where every form can be read and filled in by an AI assistant as easily as by a person.

## How it works

Each Pluck form has one link. Open it in a browser and you get a normal form. Request the same link as JSON, which is what an agent does, and you get the form as structured data: each field, its type, whether it's required, and where to submit the answers.

That means nothing needs installing on either side. The recipient pastes the link into Claude or ChatGPT. The assistant reads the questions, fills in what it knows, asks about what it doesn't, and submits.

Creating a form works the same way. You tell your own agent what you want to ask. It calls Pluck's API and hands you back a link. When responses come in, your agent can read them through the same API and summarize them.

```bash
curl -X POST https://pluck.one/api/forms \
  -H "Authorization: Bearer pk_your_key" \
  -H "Content-Type: application/json" \
  -d '{"title": "Project requirements", "fields": [
        {"name": "budget", "type": "select", "options": ["<$10k", "$10k-$50k", "$50k+"]},
        {"name": "start_date", "type": "date"}
      ]}'
```

## Follow-up questions

Making forms readable by agents fixes the retyping. It doesn't fix the other problem with forms, which is that the answers are thin. Ask "What blocked you this week?" and many people write "meetings".

So Pluck lets you attach follow-up questions, which it calls probes, to any field. If the answer is short, the form asks the follow-up: "How many days did that cost you?" A person sees it appear as they type. An assistant sees it in the JSON and answers it in its draft. You write the follow-ups once, and every respondent gets them.

## Try it

Pluck is live at [pluck.one](https://pluck.one). Sign up, and the dashboard gives you an API key and setup instructions to paste into your agent.
