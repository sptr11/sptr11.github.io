---
title: "Knowledge Work Has a Slop Problem. Developers Solved It Years Ago."
date: 2026-03-09
summary: "The market analysis could describe any market. The strategy could belong to any company. The PRD passes a casual read and collapses under the first real question. What can we learn from how developers work with AI?"
tags: ["ai", "product-management", "engineering"]
---

Knowledge work is facing a [slop epidemic](https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity). The market analysis could describe any market. The strategy could belong to any company. The PRD passes a casual read and collapses under the first real question.

Developers on the other hand -- at least those writing production-grade code, not the vibe coders -- have converged on a way of working with AI that reliably produces high-quality output. What can we learn from it, and why does the gap exist in the first place?

## The output is structurally different

A PRD, for example, and the code that implements it are both artefacts that require sustained thinking. But they inhabit entirely different quality regimes.

A passable PRD could always be assembled on instincts, intuition and vibe. The quality bar is informal, unevenly enforced, and largely a function of the individual PM's own rigor.

Production grade code has no equivalent tolerance. It has architectural design docs and test-driven development. Multiple people review it line by line. It either compiles or it doesn't. There is a structural accountability that exists independent of any individual developer's standards.

![Code vs Knowledge Work](/images/code-vs-knowledge-work.png)

## The workflow, and work-tool, is different

Developers operate inside IDEs -- constrained, focused, purpose-built for deep work. PMs work between meetings and Slack pings. Deep work hours are a luxury.

AI tooling for each type of work evolved along these existing grooves.

[Boris Tane, writing about his Claude Code workflow](https://boristane.com/blog/how-i-use-claude-code/), described spending the bulk of his time curating context and planning before any generation begins -- a pattern I have seen independently in every strong engineer I have observed. Context is curated upfront. Work is broken into chunks. Collaborators are invited into specific chunks. Progress is versioned. This is why agentic coding workflows and sub-agents emerged the way they did: to support a process that was *already* structured.

Knowledge work never developed its own equivalent of Git -- no versioning culture, no expectation that work-in-progress gets reviewed at intermediate stages. The infrastructure of accountability never existed, formally at least. As a result, the dominant AI knowledge work model became chat-interact: state what you need, the AI guesses, you correct via another prompt.

> Claude Co-work is an exception but it was built because PMs and other non-engineers began adopting Claude Code and working like developers.

## Knowledge-work done like structured coding

If the structural differences above are the diagnosis, the treatment is a deliberate workflow that borrows the practices developers already use -- adapted for knowledge work. Here is how it can work in practice:

![The Engineering Mindset for Knowledge Work](/images/engineering-mindset-knowledge-work.png)

The core idea is a reallocation of effort. Most knowledge workers spend a thin sliver of time on context, a large block wrestling with the AI, and then a rushed pass fixing the output. The engineering-influenced workflow inverts this.

**Phase 1: Don't skip the grunt work**

Context is messy by design. You can easily gather transcripts, Slack threads, and research notes, but separating high-signal from low-signal information needs careful pruning. You have to extract the relevant bits into structured context files, and review the result as a critical artifact.

The act of consolidating disparate inputs forces you to synthesize, identify gaps, and form a point of view. This is grunt work. And there is no alternative, yet.

**Phases 2 & 3: The generate-review cycle**

Assume that AI never produces final output. Everything it generates needs a genuine critical read.

Developers have always had the pull request: a structural reduction of slop baked into the culture. A fresh pair of eyes. The social contract that someone else reads your work before it ships. Most PM workflows have no equivalent but you can impose that discipline yourself. Hunt for slop and edit it.

---

AI is a tool at the end of the day and what it produces is a reflection of your personal quality bar. Good output producers are producing stunningly better output. Average workers are producing shockingly average slop. And that distinction is becoming more and more visible.
