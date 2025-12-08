---
title: I Built Two Claude Code Features a Week Before Anthropic Released Them
url: https://danielmiessler.com/blog/i-built-two-claude-code-features-before-anthropic-released-them?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2025-12-07
fetch_date: 2025-12-08T03:21:34.504930
---

# I Built Two Claude Code Features a Week Before Anthropic Released Them

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# I Built Two Claude Code Features a Week Before Anthropic Released Them

I'm not looking for a job on the Claude Code team, but if I were, this would be the blog post I'd use

December 7, 2025

[#ai](/archives/?tag=ai) [#engineering](/archives/?tag=engineering) [#claude](/archives/?tag=claude)

[![Two Claude Code Features I Built Before Anthropic](/images/blog/claude-code-features-before-anthropic/header-combined.png)](/images/blog/claude-code-features-before-anthropic/header-combined.png)

I'm not the type who brags, but I have to brag about this.

I guess it's not really bragging. It's more like validation.

Anyway.

I'm basically in love with Claude Code for multiple reasons, I have been for months. You know that by now. I've built a whole [open source project](https://github.com/danielmiessler/PAI) around it and have constructed my entire AI ecosystem on top of it.

And now this thing has happened twice:

**Twice I've built a complete, full-featured system into Kai (my personal AI infrastructure), and then less than a week later, Anthropic actually released the same functionality into Claude Code itself.**

## The Two Features [​](#the-two-features)

---

## Feature 1: Universal File-based Context (UFC) [​](#feature-1-universal-file-based-context-ufc)

Before Claude Code existed, I was already building what I called the **Universal File-based Context** system. Basically just using the file system to manage AI context and history.

[![UFC System Architecture](/images/blog/claude-code-features-before-anthropic/ufc-system.png)](/images/blog/claude-code-features-before-anthropic/ufc-system.png)

### The Problem [​](#the-problem)

Every AI conversation was ephemeral. Context disappeared between sessions. I'd have the same conversations over and over because the AI had no memory of what we'd built together.

### What I Built [​](#what-i-built)

Universal file system-based context. It had three parts:

1. **`~/.claude/context/`** - The brain. System prompt, user preferences, active project state
2. **`~/.claude/prompts/`** - Task-specific prompts that load based on what I'm doing
3. **`~/.claude/history/`** - Automatic capture of sessions, learnings, research, and decisions

Hooks would automatically inject the right context at session start and capture the good stuff at session end.

### What Anthropic Later Released [​](#what-anthropic-later-released)

On October 16, 2025, Anthropic released [Agent Skills](https://claude.com/blog/skills)—a complete system for extending Claude with modular capability packages. But it wasn't just "here's a folder structure." They built a sophisticated architecture:

**Progressive Disclosure (3 Levels):**

* **Level 1 - Metadata:** Skill name and description pre-loaded in the system prompt, so Claude knows what's available without loading everything
* **Level 2 - Core Instructions:** The full `SKILL.md` file loads only when Claude determines the skill applies to the current task
* **Level 3+ - Nested Resources:** Additional files load dynamically only as needed—making context effectively unbounded

**Dynamic Loading:** Rather than loading all skill content upfront, Claude uses filesystem tools to request specific files by name. This is exactly the "just-in-time context" pattern I'd been building with hooks—load context when relevant, not all at once.

**Code Execution Integration:** Skills can bundle scripts (Python, Bash) that Claude executes as tools. Their engineering blog describes this as providing "deterministic reliability that only code can provide" for operations better suited to code than token generation.

The parallels to what I built:

* My `~/.claude/prompts/` task-specific loading → Their progressive disclosure
* My hooks injecting context at session start → Their dynamic loading system
* My `~/.claude/context/` directory → Their `SKILL.md` architecture

I spent all this time building something I thought would be useful. Then about a week later, turns out they'd been working on the same thing and released a better, more native version of it. Made me so happy.

---

## Feature 2: Dynamic Skill Loading [​](#feature-2-dynamic-skill-loading)

Then just a few days ago, Anthropic released a blog called [Advanced Tool Use](https://www.anthropic.com/engineering/advanced-tool-use).

[![Context-Aware Routing System](/images/blog/claude-code-features-before-anthropic/architecture.png)](/images/blog/claude-code-features-before-anthropic/architecture.png)

I had *just* built something similar and taken it out of production because I thought it was overkill.

### What I Built [​](#what-i-built-1)

I built a **persistent state management system** that maintained a state file updated after every action. The architecture worked like this:

1. **State File:** A dedicated file tracked the current session context—what we were working on, what the goal was, what had been accomplished
2. **Haiku Summarization:** After each action, Haiku (fast and cheap) would quickly summarize the session state, so the system always had a compressed understanding of "what are we doing right now"
3. **User Prompt Submit Hook:** On every user message, the hook would check the state file to understand the current context—so I could say "push this" and it would know exactly what "this" meant
4. **No Full Session Reads:** Because Haiku maintained the summary, the system never had to re-read the entire conversation history to understand context

The whole point was to keep Claude locked in on exactly what we were doing. Later in a Claude Code session—especially after multiple compactions—even Claude can start to lose the plot. This system was designed to be an external memory that never forgot the task purpose.

I ended up only using it for a couple of days and then swapping it out because I thought it was excessive scaffolding—too heavy for the benefit. I figured a better model or better native scaffolding would eventually solve the problem without all that machinery.

### What Anthropic Published [​](#what-anthropic-published)

Then they published [this engineering blog](https://www.anthropic.com/engineering/advanced-tool-use) on Advanced Tool Use. The key pattern they describe is the **Tool Search Tool**—a meta-tool that lets Claude discover capabilities on-demand instead of loading everything upfront.

The specific technique: Tools are marked with `defer_loading: true` to make them discoverable on-demand. Claude initially sees only the Tool Search Tool itself plus a few high-priority tools. Everything else gets loaded only when needed.

I ran my upgrade skill against this blog and it said, "Hey, you should implement this pattern." So I did—creating extremely abridged versions of skills at startup that save context, then dynamically loading full skill content only when Claude determines it's relevant. You can see the architecture in the diagram above.

The results from their testing:

> "Instead of loading all tool definitions upfront, the Tool Search Tool discovers tools on-demand. Claude only sees the tools it actually needs for the current task."

And the token savings?

> "This represents an **85% reduction in token usage** while maintaining access to your full tool library."

They also found that Opus 4.5's accuracy improved from 79.5% to 88.1% with this pattern—fewer tokens meant less confusion, not less capability.

---

## What This All Means [​](#what-this-all-means)

So basically in both cases I had an idea that I thought would be super useful for Claude Code, and I implemented it. Then a couple of days later—or in the case of UFC about a week later—it turns out the Claude Code team was building this the whole time and they release a better version.

On one hand you'...