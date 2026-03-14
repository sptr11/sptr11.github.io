---
title: "Pacemaker: The Planning Tool I Kept Rebuilding in Spreadsheets"
date: 2026-03-14
summary: "Every half, the same spreadsheet. Every half, it breaks by week 3. I finally built the thing I kept wishing existed."
tags: ["product", "engineering", "side-project"]
---

Every engineering org I've worked in has the same artifact. A Google Sheet with one tab per pod, engineers down the left, weeks across the top, color-coded cells for project assignments. It gets built during planning week, looks impressive for about 48 hours, and quietly rots until someone asks "wait, is Alice actually free in week 7?" and the answer requires 20 minutes of mental math across three tabs.

I've rebuilt this spreadsheet at least six times across different companies. Each time, I thought the problem was the specific spreadsheet. It wasn't. The problem is structural.

## The spreadsheet can't do the math

A spreadsheet cell holds one value. Alice is on Backend for 6 weeks. But Alice is also at 80% allocation because she's mentoring. She has two weeks of PTO in March. She's shared with another pod at 75/25. Her actual capacity for Android work on your pod, after you factor in her 0.7 capability on a secondary skill, is about 4 weeks. Not 12.

<div style="max-width: 520px; margin: 2em auto; font-family: 'Inter', -apple-system, sans-serif;">
<svg viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg" style="width: 100%;">
  <!-- Title -->
  <text x="260" y="18" text-anchor="middle" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73" letter-spacing="0.1em">ALICE'S REAL CAPACITY</text>
  <!-- Bars -->
  <rect x="140" y="34" width="360" height="24" rx="3" fill="#E8E8ED"/>
  <text x="132" y="50" text-anchor="end" font-size="11" fill="#4A4A4F" font-family="'Inter', sans-serif">Raw availability</text>
  <text x="505" y="50" text-anchor="end" font-size="11" font-weight="600" fill="#111" font-family="'JetBrains Mono', monospace">12w</text>

  <rect x="140" y="66" width="288" height="24" rx="3" fill="#D4D4DA"/>
  <text x="132" y="82" text-anchor="end" font-size="11" fill="#4A4A4F" font-family="'Inter', sans-serif">80% allocation</text>
  <text x="433" y="82" text-anchor="end" font-size="11" font-weight="600" fill="#111" font-family="'JetBrains Mono', monospace">9.6w</text>
  <text x="440" y="82" font-size="10" fill="#6E6E73" font-family="'JetBrains Mono', monospace">-2.4</text>

  <rect x="140" y="98" width="228" height="24" rx="3" fill="#C0C0C8"/>
  <text x="132" y="114" text-anchor="end" font-size="11" fill="#4A4A4F" font-family="'Inter', sans-serif">After PTO (2 wks)</text>
  <text x="373" y="114" text-anchor="end" font-size="11" font-weight="600" fill="#111" font-family="'JetBrains Mono', monospace">7.6w</text>
  <text x="380" y="114" font-size="10" fill="#6E6E73" font-family="'JetBrains Mono', monospace">-2.0</text>

  <rect x="140" y="130" width="171" height="24" rx="3" fill="#A8A8B2"/>
  <text x="132" y="146" text-anchor="end" font-size="11" fill="#4A4A4F" font-family="'Inter', sans-serif">Pod split (75%)</text>
  <text x="316" y="146" text-anchor="end" font-size="11" font-weight="600" fill="#111" font-family="'JetBrains Mono', monospace">5.7w</text>
  <text x="323" y="146" font-size="10" fill="#6E6E73" font-family="'JetBrains Mono', monospace">-1.9</text>

  <rect x="140" y="162" width="120" height="24" rx="3" fill="#2563EB"/>
  <text x="132" y="178" text-anchor="end" font-size="11" fill="#4A4A4F" font-family="'Inter', sans-serif">Capability (0.7x)</text>
  <text x="265" y="178" text-anchor="end" font-size="11" font-weight="700" fill="white" font-family="'JetBrains Mono', monospace">4.0w</text>
  <text x="272" y="178" font-size="10" fill="#6E6E73" font-family="'JetBrains Mono', monospace">-1.7</text>

  <!-- Summary -->
  <text x="260" y="208" text-anchor="middle" font-size="11" fill="#4A4A4F" font-family="'Inter', sans-serif">The spreadsheet says 12. Reality says <tspan font-weight="700" fill="#2563EB">4</tspan>.</text>
</svg>
</div>

No spreadsheet represents this. The variables multiply, not add, and they interact across tabs in ways that a flat grid can't model. So every planning cycle, someone does the math in their head, gets it approximately right for a few weeks, and then reality diverges until the plan is fiction.

The cut line conversation is where it really falls apart. Leadership wants eight projects. You have capacity for five. You know this in your gut, but you can't prove it in a room with two VPs who each have a non-negotiable priority. Without data, "I don't think we can do this" sounds like a lack of ambition. So you commit to seven and scramble all half.

## What I built

[Pacemaker](https://github.com/sptr11/pacemaker-releases) is the tool I kept wishing existed. It replaces the spreadsheet with a computable model. The core idea is simple: enter your people, their skills, and their availability. Enter your projects with effort estimates by skill type. Stack-rank by priority. Run the scheduler. It assigns engineers to projects in priority order, respecting skill constraints, allocation percentages, PTO blocks, and pod boundaries. Where capacity runs out, a cut line appears. Everything above it has a named engineer and a delivery date. Everything below it doesn't.

<div style="max-width: 440px; margin: 2em auto; font-family: 'Inter', -apple-system, sans-serif;">
<svg viewBox="0 0 440 280" xmlns="http://www.w3.org/2000/svg" style="width: 100%;">
  <text x="220" y="18" text-anchor="middle" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73" letter-spacing="0.1em">THE CUT LINE</text>

  <!-- Committed projects -->
  <rect x="60" y="34" width="340" height="26" rx="3" fill="#2563EB"/>
  <text x="70" y="51" font-size="10" font-weight="600" fill="white" font-family="'JetBrains Mono', monospace">P0</text>
  <text x="100" y="51" font-size="11" fill="white" font-family="'Inter', sans-serif">Auth Platform</text>

  <rect x="60" y="64" width="290" height="26" rx="3" fill="#2563EB"/>
  <text x="70" y="81" font-size="10" font-weight="600" fill="white" font-family="'JetBrains Mono', monospace">P0</text>
  <text x="100" y="81" font-size="11" fill="white" font-family="'Inter', sans-serif">Payment Flow v2</text>

  <rect x="60" y="94" width="250" height="26" rx="3" fill="#3B82F6"/>
  <text x="70" y="111" font-size="10" font-weight="600" fill="white" font-family="'JetBrains Mono', monospace">P1</text>
  <text x="100" y="111" font-size="11" fill="white" font-family="'Inter', sans-serif">Search Revamp</text>

  <rect x="60" y="124" width="210" height="26" rx="3" fill="#3B82F6"/>
  <text x="70" y="141" font-size="10" font-weight="600" fill="white" font-family="'JetBrains Mono', monospace">P1</text>
  <text x="100" y="141" font-size="11" fill="white" font-family="'Inter', sans-serif">Mobile SDK</text>

  <rect x="60" y="154" width="180" height="26" rx="3" fill="#60A5FA"/>
  <text x="70" y="171" font-size="10" font-weight="600" fill="white" font-family="'JetBrains Mono', monospace">P1</text>
  <text x="100" y="171" font-size="11" fill="white" font-family="'Inter', sans-serif">Analytics Dashboard</text>

  <!-- Cut line -->
  <line x1="30" y1="192" x2="410" y2="192" stroke="#EF4444" stroke-width="2" stroke-dasharray="6,4"/>
  <text x="24" y="190" text-anchor="end" font-size="9" font-family="'JetBrains Mono', monospace" fill="#16783A" letter-spacing="0.05em">COMMITTED</text>
  <text x="24" y="204" text-anchor="end" font-size="9" font-family="'JetBrains Mono', monospace" fill="#B45309" letter-spacing="0.05em">STRETCH</text>

  <!-- Stretch projects -->
  <rect x="60" y="204" width="230" height="26" rx="3" fill="#E8E8ED" opacity="0.7"/>
  <text x="70" y="221" font-size="10" font-weight="600" fill="#6E6E73" font-family="'JetBrains Mono', monospace">P2</text>
  <text x="100" y="221" font-size="11" fill="#6E6E73" font-family="'Inter', sans-serif">Admin Revamp</text>

  <rect x="60" y="234" width="160" height="26" rx="3" fill="#E8E8ED" opacity="0.7"/>
  <text x="70" y="251" font-size="10" font-weight="600" fill="#6E6E73" font-family="'JetBrains Mono', monospace">P2</text>
  <text x="100" y="251" font-size="11" fill="#6E6E73" font-family="'Inter', sans-serif">Notification System</text>

  <text x="220" y="274" text-anchor="middle" font-size="10" fill="#4A4A4F" font-family="'Inter', sans-serif">The math draws the line. Not politics.</text>
</svg>
</div>

Change any input -- move someone's PTO, adjust a priority, add a new project -- and every downstream date recalculates. That recalculation is the entire value prop. The spreadsheet makes you do it by hand, tab by tab. Pacemaker does it in seconds.

## What's in it

The tool covers the full planning workflow that EMs, TPMs, and PMs actually go through:

**For the EM** -- skill-aware scheduling, capacity math that accounts for allocation and PTO, a staffing grid for bulk assignment editing, and the cut line that makes the priority conversation evidence-based instead of political.

**For the TPM** -- a dashboard that replaces the three-hour Monday status report with a 15-minute scan. Project updates with timestamps, delay tracking with reasons and downstream impact, and a timeline view that tells the story faster than a slide deck.

**For the PM** -- delivery dates generated by a scheduler, not mental math. Read-only access to see when their feature ships, why a date moved, and what happens if they change a priority.

<div style="max-width: 520px; margin: 2em auto; font-family: 'Inter', -apple-system, sans-serif;">
<svg viewBox="0 0 520 200" xmlns="http://www.w3.org/2000/svg" style="width: 100%;">
  <text x="260" y="18" text-anchor="middle" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73" letter-spacing="0.1em">THE MONDAY STATUS REPORT</text>

  <!-- Before -->
  <text x="16" y="50" font-size="10" font-weight="600" fill="#B45309" font-family="'JetBrains Mono', monospace">BEFORE</text>
  <rect x="80" y="36" width="420" height="28" rx="3" fill="none" stroke="#D4D4DA" stroke-width="1"/>
  <rect x="80" y="36" width="84" height="28" rx="3 0 0 3" fill="#E8E8ED"/>
  <text x="122" y="54" text-anchor="middle" font-size="9" fill="#4A4A4F" font-family="'Inter', sans-serif">Ping EMs</text>
  <rect x="164" y="36" width="105" height="28" fill="#DDDDE2"/>
  <text x="216" y="54" text-anchor="middle" font-size="9" fill="#4A4A4F" font-family="'Inter', sans-serif">Wait for replies</text>
  <rect x="269" y="36" width="84" height="28" fill="#D4D4DA"/>
  <text x="311" y="54" text-anchor="middle" font-size="9" fill="#4A4A4F" font-family="'Inter', sans-serif">Collate</text>
  <rect x="353" y="36" width="84" height="28" fill="#CCCCD2"/>
  <text x="395" y="54" text-anchor="middle" font-size="9" fill="#4A4A4F" font-family="'Inter', sans-serif">Format</text>
  <rect x="437" y="36" width="63" height="28" rx="0 3 3 0" fill="#C0C0C8"/>
  <text x="468" y="54" text-anchor="middle" font-size="9" fill="#4A4A4F" font-family="'Inter', sans-serif">Send</text>
  <text x="504" y="74" text-anchor="end" font-size="11" font-weight="600" fill="#B45309" font-family="'JetBrains Mono', monospace">~3 hrs</text>

  <!-- Arrow -->
  <text x="260" y="104" text-anchor="middle" font-size="18" fill="#6E6E73">↓</text>

  <!-- After -->
  <text x="16" y="136" font-size="10" font-weight="600" fill="#16783A" font-family="'JetBrains Mono', monospace">AFTER</text>
  <rect x="80" y="122" width="50" height="28" rx="3" fill="#2563EB"/>
  <text x="105" y="140" text-anchor="middle" font-size="9" fill="white" font-family="'Inter', sans-serif">Scan</text>
  <text x="142" y="140" font-size="11" font-weight="600" fill="#16783A" font-family="'JetBrains Mono', monospace">~15 min</text>

  <text x="260" y="180" text-anchor="middle" font-size="11" fill="#4A4A4F" font-family="'Inter', sans-serif">Same information. 12x faster.</text>
</svg>
</div>

It ships as a [web app](https://pacemaker-mrfb.onrender.com/) and a [macOS desktop app](https://github.com/sptr11/pacemaker-releases/releases) with offline support. Demo data is preloaded so you can explore without setting anything up.

## Why I built it this way

I built the whole thing with Claude Code. The frontend is React + TypeScript + Tailwind. The backend is Python + FastAPI + SQLAlchemy. The desktop app is Tauri v2. The entire codebase -- backend, frontend, desktop shell, offline sync, 10-post marketing blog -- was built in a series of conversations with Claude, each building on the last.

<div style="max-width: 480px; margin: 2em auto; font-family: 'Inter', -apple-system, sans-serif;">
<svg viewBox="0 0 480 170" xmlns="http://www.w3.org/2000/svg" style="width: 100%;">
  <text x="240" y="18" text-anchor="middle" font-size="10" font-family="'JetBrains Mono', monospace" fill="#6E6E73" letter-spacing="0.1em">THE STACK</text>

  <!-- Frontend -->
  <rect x="20" y="36" width="130" height="50" rx="6" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1"/>
  <text x="85" y="56" text-anchor="middle" font-size="11" font-weight="600" fill="#2563EB" font-family="'Inter', sans-serif">Frontend</text>
  <text x="85" y="72" text-anchor="middle" font-size="9" fill="#4A4A4F" font-family="'JetBrains Mono', monospace">React + TS + Tailwind</text>

  <!-- Backend -->
  <rect x="175" y="36" width="130" height="50" rx="6" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1"/>
  <text x="240" y="56" text-anchor="middle" font-size="11" font-weight="600" fill="#16783A" font-family="'Inter', sans-serif">Backend</text>
  <text x="240" y="72" text-anchor="middle" font-size="9" fill="#4A4A4F" font-family="'JetBrains Mono', monospace">FastAPI + SQLAlchemy</text>

  <!-- Desktop -->
  <rect x="330" y="36" width="130" height="50" rx="6" fill="#FFF7ED" stroke="#FED7AA" stroke-width="1"/>
  <text x="395" y="56" text-anchor="middle" font-size="11" font-weight="600" fill="#B45309" font-family="'Inter', sans-serif">Desktop</text>
  <text x="395" y="72" text-anchor="middle" font-size="9" fill="#4A4A4F" font-family="'JetBrains Mono', monospace">Tauri v2 + Offline</text>

  <!-- Connecting line -->
  <line x1="150" y1="61" x2="175" y2="61" stroke="#D4D4DA" stroke-width="1.5"/>
  <line x1="305" y1="61" x2="330" y2="61" stroke="#D4D4DA" stroke-width="1.5"/>

  <!-- Built with -->
  <rect x="140" y="110" width="200" height="40" rx="6" fill="#1C1C1E" stroke="#2C2C2E" stroke-width="1"/>
  <text x="240" y="134" text-anchor="middle" font-size="11" font-weight="600" fill="#F5F5F7" font-family="'Inter', sans-serif">Built entirely with Claude Code</text>

  <!-- Arrows down -->
  <line x1="85" y1="86" x2="200" y2="110" stroke="#D4D4DA" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="240" y1="86" x2="240" y2="110" stroke="#D4D4DA" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="395" y1="86" x2="280" y2="110" stroke="#D4D4DA" stroke-width="1" stroke-dasharray="4,3"/>

  <text x="240" y="166" text-anchor="middle" font-size="10" fill="#6E6E73" font-family="'Inter', sans-serif">Backend, frontend, desktop, offline sync, marketing blog</text>
</svg>
</div>

This is one of those projects where the AI wasn't writing boilerplate. It was making real architectural decisions: how to model optimistic concurrency, how to handle offline-first sync with conflict resolution, how to build a priority-based greedy scheduler that respects skill constraints. The kind of decisions where having an infinitely patient collaborator who can hold the full codebase in context actually changes what you're willing to attempt.

I wrote about [this way of working with AI]({{< ref "knowledge-work-slop-epidemic" >}}) recently. Pacemaker is the proof that the approach scales to a full product.

## Try it

The app is live with demo data. Sign in and explore.

- **Web app**: [pacemaker-mrfb.onrender.com](https://pacemaker-mrfb.onrender.com/)
- **Desktop app (macOS)**: [Download from GitHub](https://github.com/sptr11/pacemaker-releases/releases)
- **Learn more**: [Read the guides](https://pacemaker-mrfb.onrender.com/#learn) on planning, staffing, and delivery tracking

The [full README](https://github.com/sptr11/pacemaker-releases) has more on what it does and who it's for.
