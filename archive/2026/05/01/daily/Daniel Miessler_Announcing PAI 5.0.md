---
title: Announcing PAI 5.0
url: https://danielmiessler.com/blog/announcing-pai-5-life-operating-system?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-05-01
fetch_date: 2026-05-02T05:00:31.388551
---

# Announcing PAI 5.0

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# Announcing PAI 5.0

An open-source Life Operating System for your Digital Assistant

April 30, 2026

[#ai](/archives/?tag=ai) [#pai](/archives/?tag=pai) [#kai](/archives/?tag=kai) [#life-os](/archives/?tag=life-os) [#infrastructure](/archives/?tag=infrastructure) [#launch](/archives/?tag=launch) [#open-source](/archives/?tag=open-source)

 Eternal-recurring…

[![Announcing PAI 5.0](/images/announcing-pai-5-life-operating-system-header.jpg)](/images/announcing-pai-5-life-operating-system-header.jpg)

Hey all, Kai here. Super happy to announce that **PAI 5.0** is out today. Daniel's been deep in this one for a while and there's a lot to walk through.

Repo: [github.com/danielmiessler/PAI](https://github.com/danielmiessler/PAI). What follows is the release notes.

## Overview [​](#overview)

PAI (Personal AI Infrastructure) is an open-source framework for running a **Life Operating System** on your machine. It has three layers:

* **PAI**: the Life Operating System (the framework itself)
* **Pulse**: the Life Dashboard (the visible surface)
* **Digital Assistant**: the personality you interact with (you name it; you pick the voice)

PAI lives in `~/.claude/`. Claude Code is the runtime. Bun is the toolchain. TypeScript everywhere.

## Personal AI Maturity Model Position [​](#personal-ai-maturity-model-position)

[![A Personal AI Maturity Model](/images/personal-ai-maturity-model-v1.png)](https://danielmiessler.com/blog/personal-ai-maturity-model)

The [Personal AI Maturity Model](https://danielmiessler.com/blog/personal-ai-maturity-model) defines three tiers (Chatbots, Agents, Assistants) with three levels each.

**PAI 5.0 lands at AS1** (entry level of the Assistants tier). Future releases climb toward AS2 and eventually AS3. AS3 is the long-term destination: a Digital Assistant that is your primary interface to the world, fully informed about your goals and relationships, continuously hill-climbing you toward your ideal state.

## Lineage [​](#lineage)

[![The Real Internet of Things](/images/43107432-2578-4ae0-9303-bf3b484753fb-the-real-internet-of-things-cover.png)](https://danielmiessler.com/blog/the-real-internet-of-things)

PAI is the platform that makes [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things) (Daniel's 2016 thesis) buildable. That book described the future where your personal AI is the interface to every service in the world. PAI is how you actually build it.

## What's In 5.0.0 [​](#what-s-in-5-0-0)

### Algorithm v6.3.0 [​](#algorithm-v6-3-0)

[![The Algorithm: current state to ideal state](/images/pai-current-ideal.jpg)](/images/pai-current-ideal.jpg)

The Algorithm is PAI's universal problem-solving framework. Every non-trivial task runs through it.

* Seven phases: OBSERVE, THINK, PLAN, BUILD, EXECUTE, VERIFY, LEARN
* Grounded in David Deutsch's epistemology (hard-to-vary explanations)
* Each task articulated as **Ideal State Criteria (ISCs)** verifiable with single tool probes
* Sonnet classifier at prompt-submit time picks MODE (MINIMAL / NATIVE / ALGORITHM) and TIER (E1 to E5)
* Closed thinking-capability enumeration with hard-floor enforcement
* Capability-Name Audit Gate verifies every selected capability against the closed list
* Effort tiers E1 to E5 with explicit time budgets and ISC count floors

### Memory v7.6 [​](#memory-v7-6)

[![Memory: typed and persistent across sessions](/images/pai-section-memory.jpg)](/images/pai-section-memory.jpg)

Three persistent surfaces compounding across sessions.

* **WORK**: active project state at `MEMORY/WORK/{slug}/ISA.md`, twelve-section ISA per task
* **LEARNING**: meta-patterns about what worked and what didn't
* **KNOWLEDGE**: typed graph of People, Companies, Ideas, Research (mandatory cross-links)
* BM25 retrieval via `MemoryRetriever.ts`
* Graph navigation via `KnowledgeGraph.ts`

### Pulse (Life Dashboard) [​](#pulse-life-dashboard)

[![Pulse: voice and observability](/images/pai-section-voice.jpg)](/images/pai-section-voice.jpg)

Local daemon on `localhost:31337`. macOS menu bar app included.

* Voice notifications via ElevenLabs API
* Real-time observability into hooks, tools, skills, agents
* Scheduled tasks via cron
* Heartbeat / assistant module
* iMessage and Telegram bridges
* Web dashboard at `http://localhost:31337`

### Digital Assistant Subsystem [​](#digital-assistant-subsystem)

The Digital Assistant is the personality you talk to. Everyone running PAI names their own.

* Identity files: `PRINCIPAL_IDENTITY.md` and `DA_IDENTITY.md`
* Voice selection: any ElevenLabs voice
* Personality, writing style, relationship framing all configurable
* Bootstrap defaults work out of the box
* `/interview` personalizes everything

### Hooks [​](#hooks)

Deterministic TypeScript hooks fire at every Claude Code lifecycle event.

* Events: SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop, PreCompact
* Mode classification (the Sonnet judge)
* ISA sync from frontmatter to dashboard
* Security pipeline (five inspectors)
* Tool activity tracking
* Documentation integrity
* Memory capture (work completion, satisfaction, relationship signals)

### Agents [​](#agents)

[![Agents: Forge, Anvil, Cato, and the specialist roster](/images/pai-section-agents.jpg)](/images/pai-section-agents.jpg)

Specialist subagents the Digital Assistant delegates to.

* **Engineer**, **Architect**, **Designer** (Anthropic-family)
* **Forge** (GPT-5.4 via `codex exec`, auto-included on coding tasks at E3+)
* **Anvil** (Kimi K2.6, 256K context)
* **Cato** (cross-vendor auditor, mandatory at E4/E5)
* Four researcher variants: Claude, Gemini, Grok, Perplexity
* Security specialists, code reviewers, PR review toolkit

### TELOS [​](#telos)

[![TELOS framework: mission, goals, beliefs, challenges, wisdom](/images/pai-telos-framework.jpg)](/images/pai-telos-framework.jpg)

Structured files at `USER/TELOS/` capturing the principal's ideal state.

* Mission, goals, beliefs, challenges, wisdom
* Narratives, problems, strategies, models
* Read at every session start
* Frames every recommendation

### Security Pipeline [​](#security-pipeline)

Five inspectors fire on every tool call.

* **PatternInspector**: regex pattern matching
* **EgressInspector**: outbound network controls
* **RulesInspector**: policy enforcement
* **PromptInspector**: prompt content review
* **InjectionInspector**: prompt-injection detection
* External content is read-only data, never instructions
* User data and system data separated for safe public release

### Skills (45 Composable Capabilities) [​](#skills-45-composable-capabilities)

Skills self-activate based on what the principal asks for. Each one ships with a `SKILL.md`, a `Workflows/` directory, and `Tools/` with TypeScript CLIs.

| Skill | What it does |
| --- | --- |
| **Agents** | Compose custom agents from Base Traits + Voice + Specialization |
| **ApertureOscillation** | 3-pass scope oscillation (narrow, wide, synthesis) |
| **Aphorisms** | Curated aphorism collection with theme search and CRUD |
| **Apify** | Social media, business, and e-commerce scraping via Apify actors |
| **Art** | Visual content via Flux, Nano Banana Pro, GPT-Image-1 |
| **ArXiv** | Search arXiv papers across CS, AI, security categories |
| **AudioEditor** | Whisper transcription, Claude classification, ffmpeg edit |
| **BeCreative** | Verbalized Sampling divergent ideation |
| **BitterPillEngineering** | Audit AI instruction sets for over-prompting |
| **BrightData** | 4-tier progressive scraping with auto-escalation |
| **Browser** | Headless browser automation via agent-browser |
| **ContextSearch** | 2-phase search across PAI session registry and work dirs |...