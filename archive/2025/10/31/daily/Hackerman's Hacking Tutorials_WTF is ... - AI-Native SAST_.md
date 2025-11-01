---
title: WTF is ... - AI-Native SAST?
url: https://parsiya.net/blog/wtf-is-ai-native-sast/
source: Hackerman's Hacking Tutorials
date: 2025-10-31
fetch_date: 2025-11-01T03:11:39.957225
---

# WTF is ... - AI-Native SAST?

# [Hackerman's Hacking Tutorials](https://parsiya.net/)

## The knowledge of anything, since all things have causes, is not acquired or complete unless it is known by its causes. - Avicenna

Navigate…» About Me!» Cheat Sheet» My Clone» Source Repo» Manual Work is a Bug» The Other Guy from Wham!

* [About Me!](https://parsiya.net/about/ "About Me!")
* [Cheat Sheet](https://parsiya.net/cheatsheet/ "Cheat Sheet")
* [My Clone](https://parsiya.io/ "My Clone")
* [Source Repo](https://github.com/parsiya/parsiya.net "Source Repo")
* [Manual Work is a Bug](https://queue.acm.org/detail.cfm?id=3197520 "Manual Work is a Bug")
* [The Other Guy from Wham!](https://www.google.com/search?q=andrew+ridgeley "The Other Guy from Wham!")

Oct 31, 2025
- 17 minute read - [AI](https://parsiya.net/categories/ai/) [Static Analysis](https://parsiya.net/categories/static-analysis/)

# WTF is ... - AI-Native SAST?

* [The Promise (Or the Premise)](#the-promise-or-the-premise)
* [Why You Should Try SAST+AI!](#why-you-should-try-sastai)
  + [Complementing Traditional SAST](#complementing-traditional-sast)
* [What Hurdles Await You!](#what-hurdles-await-you)
  + [Cost](#cost)
  + [Context Rot](#context-rot)
  + [Non-Determinism](#non-determinism)
* [A Blueprint for SecurityTooling+AI?!](#a-blueprint-for-securitytoolingai)
  + [Ingredients](#ingredients)
  + [Input](#input)
    - [RAG](#rag)
* [How Many Ways Can You Do SAST+AI Anyway?](#how-many-ways-can-you-do-sastai-anyway)
  + [Prompt + Code](#prompt--code)
    - [Analyzing Pull Requests with AI](#analyzing-pull-requests-with-ai)
    - [AI as Classifier/Triager](#ai-as-classifiertriager)
  + [Prompt + Agent](#prompt--agent)
  + [Tailored Prompt + SAST Result](#tailored-prompt--sast-result)
  + [Agent + Code Graph + SAST MCP](#agent--code-graph--sast-mcp)
    - [How ZeroPath Works](#how-zeropath-works)
    - [MCPs](#mcps)
    - [Embedding Models](#embedding-models)
* [What Did We Learn Here Today?](#what-did-we-learn-here-today)

Ladies and gentlemen, my name is Parsia and I'm here to ask and answer one
simple question: WTF is AI-Native SAST? (RIP TotalBiscuit).

Spoiler: It's SAST+AI. But that doesn't make it useless. Quite the opposite,
I'll make the case for passing all your code to AI while tokens are cheap. Don't
believe the marketing, though. Current LLMs need serious hand-holding to go
beyond surface-level bug discovery, and that hand-holding comes from static
analysis.

Disclaimers: Not related to or endorsed by past, present, or future employers.

# The Promise (Or the Premise)

You've seen it, read it. The world has changed forever. Those other SAST tools
are bad; our AI-Native tool can replace all your tools and engineers. "Are we
gonna lose our jobs?" I yelled as I jumped like a maniac into the XBOW huddle at
DEF CON.

I get lots of marketing emails like this. First, I have no purchase authority,
besties. Second, "Gentlemen, you can't fight in here! This is LinkedIn!" Tag
your competition on Twitter and insult them directly instead of my inbox.

A few weeks ago I read this excellent blog,
[Hacking with AI SASTs: An overview of 'AI Security Engineers'/'LLM Security Scanners' for Penetration Testers and Security Teams](https://joshua.hu/llm-engineer-review-sast-security-ai-tools-pentesters)
(Joshua, could I possibly interest you in shorter titles?). It's a hands-on
comparison of multiple SAST+AI tools and a great primer on getting started in
this space.

Instead of passing that blog to an LLM and asking it to rewrite it in my style
like the norm these days, I want to explain what *I* would do to create a new
static analysis tool in "the age of AI." But first, you need to sit through some
of my rants. Because if you cannot handle my rants, you do not deserve my
thought leadership (lol).

# Why You Should Try SAST+AI!

If you know me, you know I love static analysis. For employment reasons, I'm
obligated to say I also love AI and dream of adding Copilot to Windows
Calculator. I've been disappointed in the SAST+AI space. I don't mean the people
"with AI in their Twitter bio" (grifters gonna grift), but actual static
analysis companies are doing, well, not much?!

We need progress in this space while VCs throw money at AI. In my opinion, if
you are interested in static analysis you should experiment with AI because:

1. The Price is Right! Tokens are heavily subsidized right now.
2. This might be your only chance to run AI tools on all your code.
3. We need AI to review all this AI-generated code.
4. AI can catch bug classes that are hard to detect with traditional SAST.

The hype is useful. Convince your employer to let you review all your code with
AI. You won't get this chance again. Run it before they start caring about costs
(not legal advice).

![Boss can AI review all of our code?](06.webp "Boss can AI review all of our code?")
Boss can AI review all of our code?

Companies claim X% of their code is AI-generated. There's a tsunami of
AI-generated code. Our only chance to secure it is more AI!

![The only thing that can stop bad AI-generated code is good AI-generated code](01.png "The only thing that can stop bad AI-generated code is good AI-generated code")
The only thing that can stop bad AI-generated code is good AI-generated code

Image credit: By Unknown author - Chrysopoea of Cleopatra (Codex Marcianus graecus 299 fol. 188v), [Public Domain from wikimedia](https://commons.wikimedia.org/w/index.php?curid=36915535)

## Complementing Traditional SAST

Traditional static analysis has been historically bad at catching some bug
classes like authorization and business logic issues. AI is promising here.
Sometimes AI can understand the code's intent. In other words, you explain what
the code needs to do and ask AI "chat, is this true?"

In other words, I do not believe current AI-native SAST products are a direct
replacement. Here's another simple question: are you catching all I catch with
Semgrep, CodeQL, and more? I have hand-crafted artisanal Semgrep rules (lol) and
a treasure trove of CodeQL queries at my disposal. I am not being adversarial;
it's completely OK to create a product to fill those gaps instead of doing
everything.

# What Hurdles Await You!

I've hyped AI up like a prompt engineering course hawker, now listen to my AI
H8R side.

## Cost

Tokens are cheap, but not that cheap. Human-generated code still dwarfs
AI-generated code. "There's a lot of software out there, Parsia! More
repositories than stars in the sky!"

![Paraphrasing princess Kahm from Outlanders](03.webp "Paraphrasing princess Kahm from Outlanders")
Paraphrasing princess Kahm from Outlanders

Recently, I read [Secret Detection Tools Comparison](https://github.com/FuzzingLabs/fuzzforge_ai/blob/master/backend/benchmarks/by_category/secret_detection/results/comparison_report.md) by FuzzingLabs. While
I'm impressed by LLMs, look at the run times. GPT-5 mini took more than 10
minutes to find 32 secrets! This is not "web scale" (lol). While AI processed
one log file, 10 more were added to the backlog.

## Context Rot

Models advertise longer context windows and users think it's a good thing,
right? Wrong. Initial tokens are more important. You can feel this in
conversations. The AI forgets older prompts and data.

![Older tokens, saluting goodbye!](04.webp "Older tokens, saluting goodbye!")
Older tokens, saluting goodbye!

Image credit: My Hero Academia manga, chapter 333.

I read two studies recently that deal with this phenomenon. Even when the model
advertises a large context window, you need to get things done within the first
few 10K tokens. So while we can fit entire projects or modules into a context
window, the model won't actually understand all of them.

1. [Evaluating Long Context (Reasoning) Ability](https://nrehiew.github.io/blog/long_context/)
   1. "What do 1M and 500K context windows have in common? They are both actually 64K." lol.
2. [Context Rot: How Increasing Input Tokens Impacts LLM Performance](https://research.trychrom...