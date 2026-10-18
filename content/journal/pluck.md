---
title: "Pluck: Forms That AI Assistants Can Fill In"
date: 2026-10-17
draft: false
summary: "Online forms are invisible to AI assistants, so people retype answers their assistant already knows. Pluck serves every form in a format agents can read and submit."
tags: ["product", "ai", "side-project"]
---

Online forms were designed for a person typing into a browser. That made sense until recently. Now many people have an AI assistant that already knows the answers: their company's details, their budget, their deadlines, the project they need help with.

But hand that assistant a Typeform or Google Forms link and it usually can't do anything with it. These forms are built in JavaScript, and the tools assistants use to read web pages generally don't run JavaScript. The assistant sees an empty page. So the person reads the questions and types out, by hand, facts their assistant could have supplied in seconds.

I built [Pluck](https://pluck.one) to fix that. It's a form builder where every form can be read and filled in by an AI assistant as easily as by a person.

## How it works

Each Pluck form has one link. Open it in a browser and you get a normal form. Request the same link as JSON, which is what an agent does, and you get the form as structured data: each field, its type, whether it's required, and where to submit the answers.

<div style="max-width: 520px; margin: 2em auto; font-family: 'Inter', -apple-system, sans-serif;">
<svg viewBox="0 0 520 250" xmlns="http://www.w3.org/2000/svg" style="width: 100%;" role="img" aria-label="One Pluck link. Opened in a browser it shows a form; requested as JSON it returns the fields, types and submit address.">
  <defs><marker id="pk-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#A8A8B2"/></marker></defs>
  <text x="260" y="18" text-anchor="middle" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73" letter-spacing="0.1em">ONE LINK, TWO READERS</text>
  <rect x="170" y="30" width="180" height="30" rx="3" fill="#2563EB"/>
  <text x="260" y="49" text-anchor="middle" font-size="11" font-weight="600" fill="#fff" font-family="'JetBrains Mono', monospace">pluck.one/f/project</text>
  <path d="M220,60 C220,85 130,80 130,104" fill="none" stroke="#A8A8B2" stroke-width="1.5" marker-end="url(#pk-a)"/>
  <path d="M300,60 C300,85 390,80 390,104" fill="none" stroke="#A8A8B2" stroke-width="1.5" marker-end="url(#pk-a)"/>
  <text x="130" y="100" text-anchor="end" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73" dx="-12">a person</text>
  <text x="390" y="100" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73" dx="12">an assistant</text>
  <!-- browser card -->
  <rect x="30" y="110" width="200" height="125" rx="4" fill="#F5F5F7" stroke="#D4D4DA"/>
  <text x="46" y="134" font-size="11" font-weight="600" fill="#111">Project requirements</text>
  <text x="46" y="154" font-size="10" fill="#4A4A4F">Budget</text>
  <rect x="46" y="159" width="168" height="18" rx="2" fill="#fff" stroke="#D4D4DA"/>
  <text x="52" y="172" font-size="10" fill="#6E6E73">$10k–$50k  ▾</text>
  <text x="46" y="192" font-size="10" fill="#4A4A4F">Start date</text>
  <rect x="46" y="197" width="168" height="18" rx="2" fill="#fff" stroke="#D4D4DA"/>
  <rect x="160" y="219" width="54" height="11" rx="2" fill="#2563EB"/>
  <!-- json card -->
  <rect x="290" y="110" width="200" height="125" rx="4" fill="#1C1C1E"/>
  <g font-size="10" font-family="'JetBrains Mono', monospace" fill="#E8E8ED">
    <text x="304" y="132">{ "fields": [</text>
    <text x="316" y="148">{ "name": "budget",</text>
    <text x="328" y="162">"type": "select" },</text>
    <text x="316" y="178">{ "name": "start_date",</text>
    <text x="328" y="192">"type": "date" } ],</text>
    <text x="316" y="210" fill="#8AB4FF">"submit": "/api/..."</text>
    <text x="304" y="226">}</text>
  </g>
</svg>
</div>

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

<div style="max-width: 520px; margin: 2em auto; font-family: 'Inter', -apple-system, sans-serif;">
<svg viewBox="0 0 520 130" xmlns="http://www.w3.org/2000/svg" style="width: 100%;" role="img" aria-label="A short answer, meetings, triggers the follow-up question: how many days did that cost you?">
  <defs><marker id="pk-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#2563EB"/></marker></defs>
  <text x="260" y="18" text-anchor="middle" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73" letter-spacing="0.1em">A THIN ANSWER GETS A FOLLOW-UP</text>
  <text x="20" y="50" font-size="11" fill="#4A4A4F">What blocked you this week?</text>
  <rect x="20" y="58" width="200" height="30" rx="3" fill="#fff" stroke="#D4D4DA"/>
  <text x="32" y="78" font-size="12" fill="#111">meetings</text>
  <text x="20" y="108" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73">one word: too short</text>
  <path d="M228,73 L292,73" stroke="#2563EB" stroke-width="1.5" marker-end="url(#pk-b)"/>
  <text x="260" y="66" text-anchor="middle" font-size="10" font-family="'JetBrains Mono', monospace" fill="#2563EB">probe</text>
  <rect x="300" y="50" width="200" height="46" rx="3" fill="#EEF3FE" stroke="#2563EB"/>
  <text x="312" y="70" font-size="11" font-weight="600" fill="#111">How many days did</text>
  <text x="312" y="86" font-size="11" font-weight="600" fill="#111">that cost you?</text>
  <text x="300" y="114" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73">shown to people and agents alike</text>
</svg>
</div>

## Try it

Pluck is live at [pluck.one](https://pluck.one). Sign up, and the dashboard gives you an API key and setup instructions to paste into your agent.
