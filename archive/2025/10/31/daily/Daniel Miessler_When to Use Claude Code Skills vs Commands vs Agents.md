---
title: When to Use Claude Code Skills vs Commands vs Agents
url: https://danielmiessler.com/blog/when-to-use-skills-vs-commands-vs-agents?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2025-10-31
fetch_date: 2025-11-01T03:13:04.638772
---

# When to Use Claude Code Skills vs Commands vs Agents

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[speaking](/speaking/)[about](/about/)

# When to Use Claude Code Skills vs Commands vs Agents

How I restructured my Claude Code-based Personal AI Infrastructure around the Skill -> Commands —> Agents structure

October 31, 2025

[#ai](/archives/?tag=ai) [#productivity](/archives/?tag=productivity) [#tutorial](/archives/?tag=tutorial) [#technology](/archives/?tag=technology)

[![Three-tier hierarchy diagram showing Skills as containers, Workflows nested inside, and Agents as parallel workers](/images/skills-commands-agents-hierarchy.png)](/images/skills-commands-agents-hierarchy.png)

When [Anthropic released Skills](https://simonwillison.net/2025/Oct/16/claude-skills/) in October 2025, I faced a confusing problem: Skills, Commands, and Agents are all essentially the same thing—markdown files containing prompts. Structurally identical. So which do you use, and when?

## The Problem: Three Identical Primitives [​](#the-problem-three-identical-primitives)

Here's what makes Claude Code's architecture confusing:

**They're all just markdown files with prompts:**

* Skills? Markdown files in `~/.claude/skills/`
* Commands? Markdown files (used to be in `~/.claude/commands/`)
* Agents? Markdown files in `~/.claude/agents/`

Same structure. Same format. Same basic idea: give Claude instructions.

So when you want to add a "write blog post" capability, which primitive do you use?

* Make it a skill?
* Make it a command?
* Make it an agent?
* All three somehow?

I had all three problems at once:

**1. No clear decision framework.** Should blog writing be a skill or a command? I had both. They duplicated each other. Neither was authoritative.

**2. Scattered functionality.** Blog commands lived in a global directory, divorced from blog-specific context like formatting rules and voice guidelines.

**3. Unclear nesting.** If skills can contain other files, should commands live inside skills? Should agents call skills? Should skills call agents? What calls what?

The result: I never knew where new capabilities should go, I had duplication everywhere, and my system was impossible to extend consistently.

## The Solution: A Clear Decision Framework [​](#the-solution-a-clear-decision-framework)

Since all three primitives are structurally identical, the answer isn't about syntax—it's about **purpose and nesting**. Here's the framework I landed on:

**Skills = Domain containers** (blogging, research, security) **Commands = Tasks/Commands within domains** (nested inside skills under workflows/ directory) **Agents = Standalone parallel workers** (can execute skills and their commands)

This solves the nesting problem: agents aren't nested in skills, but they CAN execute them. Skills contain commands (in workflows/ subdirectories). Commands don't contain anything—they're the leaf nodes.

Here's how it works in practice:

Here's what the overall structure looks like:

```
~/.claude/
├── skills/                    # Domain containers
│   ├── blogging/
│   │   ├── SKILL.md          # Main prompt file with routing logic
│   │   ├── workflows/        # Commands live here (nested, not global)
│   │   │   ├── write.md      # Command: write blog post
│   │   │   ├── publish.md    # Command: publish blog post
│   │   │   └── rewrite.md    # Command: rewrite blog post
│   │   └── context/          # Supporting prompt files by topic
│   │       ├── formatting.md # Frontmatter and structure
│   │       └── examples.md   # Sample blog posts
│   ├── research/
│   │   ├── SKILL.md          # Main prompt file
│   │   ├── workflows/        # Commands for research
│   │   │   └── conduct.md    # Command: conduct research
│   │   └── context/          # Supporting prompts
│   │       ├── sources.md    # Preferred research sources
│   │       └── methodology.md
│   ├── images/
│   │   ├── SKILL.md          # Main prompt file
│   │   ├── workflows/        # Commands for images
│   │   │   └── generate.md   # Command: generate image
│   │   └── context/          # Supporting prompts
│   │       ├── styles.md     # Image style guidelines
│   │       └── prompts.md    # Prompt templates
│   └── system/
│       ├── SKILL.md          # System-level operations
│       └── workflows/        # System commands
│           ├── update-kai-repo.md
│           ├── check-sensitive.md
│           └── observability.md
├── agents/                    # Parallel workers
│   ├── engineer.md
│   ├── architect.md
│   ├── pentester.md
│   ├── researcher.md
│   └── intern.md
└── history/                   # Logging output
    ├── sessions/
    ├── research/
    └── learnings/
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41

### Tier 1: Skills (Domain Containers) [​](#tier-1-skills-domain-containers)

**When to use:** You're organizing a domain of related capabilities (blogging, research, security, etc.)

Skills are self-contained modules where everything for a specific domain lives together:

```
~/.claude/skills/blogging/
├── SKILL.md              # Routing logic and domain knowledge
├── workflows/            # Commands live here (still commands, just nested)
│   ├── write.md          # Command: write blog post
│   ├── publish.md        # Command: publish blog post
│   └── rewrite.md        # Command: rewrite blog post
└── context/              # Supporting prompts and references
    ├── voice.md
    └── formatting.md
```

1
2
3
4
5
6
7
8
9

When you say "write a blog post," the blogging skill loads, analyzes your intent, and routes internally to `workflows/write.md`.

**Key insight:** Skills are just markdown files that can reference OTHER markdown files in their directory. That's it.

### Tier 2: Commands (Nested Tasks) [​](#tier-2-commands-nested-tasks)

**When to use:** You have a specific task within a domain (write, publish, research, etc.)

Commands are task-specific prompt files that live INSIDE their parent skill under the `workflows/` directory. They're still commands—they just have a new home.

For example, `skills/blogging/workflows/write.md` is a command (markdown file with instructions for writing blog posts)—same structure as before, just nested inside the blogging skill instead of floating globally.

**Key insight:** Commands didn't go away. They just moved from `~/.claude/commands/` to `~/.claude/skills/{domain}/workflows/` where they belong with their related context.

### Tier 3: Agents (Parallel Workers) [​](#tier-3-agents-parallel-workers)

**When to use:** You need concurrent execution of multiple tasks

Agents are standalone markdown files in `~/.claude/agents/` that execute work in parallel. The key difference: agents can invoke skills and their commands.

Example workflow:

1. You ask to research a topic
2. The research skill launches 3 intern agents in parallel
3. Each intern executes the research skill's commands on different sources
4. All report back simultaneously

**Key insight:** Agents aren't nested in skills—they're standalone entities that can EXECUTE skills and commands as parallel workers.

## The Implementation [​](#the-implementation)

I restructured the entire PAI system around this hierarchy. Here's what changed:

**Before:**

```
~/.claude/
├── commands/
│   ├── write-blog.md          # 721 lines, divorced from blogging context
│   ├── publish-blog.md        # 471 lines, divorced from blogging context
│   ├── conduct-research.md    # Separated from research skill
│   ├── get-ai-news.md         # Duplicate of skill version
│   └── update-kai-repo.md     # System-level, no clear home
└── skills/
    ├── blogging/
    │   └── SKILL.md           # 48KB monolith doing everything
    ├── research/
    │   └── SKILL.md
    └── get-ai-news/
        └── SKILL.md           # Duplicate functionality
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14

**Afte...