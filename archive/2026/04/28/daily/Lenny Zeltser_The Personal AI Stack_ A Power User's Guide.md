---
title: The Personal AI Stack: A Power User's Guide
url: https://zeltser.com/personal-ai-stack
source: Lenny Zeltser
date: 2026-04-28
fetch_date: 2026-04-29T05:13:07.132817
---

# The Personal AI Stack: A Power User's Guide

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

×

# The Personal AI Stack: A Power User's Guide

An AI tool like Claude Code gives you solid general-purpose capabilities out of the box. To make it truly indispensable, add the layers that teach it who you are, how you work, and what you do.

![The Personal AI Stack: A Power User's Guide - illustration](/assets/personal-ai-stack.DewOhs6n_ZChPKY.webp)

The Personal AI Stack is my seven-layer model for shaping a capable AI tool such as Claude Code around your projects, tools, and knowledge. I’ll walk through each layer, so you can choose which ones to add to your own setup.

| Layer | Name | Examples |
| --- | --- | --- |
| 7 | [Work](#layer-7-work) | Your Projects |
| 6 | [Connectors](#layer-6-connectors) | MCP Servers, CLIs |
| 5 | [Tech Stack](#layer-5-tech-stack) | Files, AI-Friendly Services |
| 4 | [Hardening](#layer-4-hardening) | Security Tweaks |
| 3 | [Personalization](#layer-3-personalization) | PAI Customizations |
| 2 | [Scaffolding](#layer-2-scaffolding) | PAI, Skills |
| 1 | [Harness](#layer-1-harness) | Claude Code, Ghostty, Maestro |

The examples center on Claude Code, but you can adjust the stack to your own preferences.

I’ve been using the Personal AI Stack to expand and deepen my work. For example, it helped me ship a [new version of REMnux](/remnux-v8-release) with its [MCP server](/ai-malware-analysis-remnux) and profile the [RSAC Innovation Sandbox finalists](/media/rsac-2026-sandbox). And my [endpoint security startup guide](/endpoint-security-startup-questions) and [security product creation framework](/security-product-creation-framework) would’ve taken many more hours of browsing and note-taking without it.

## Layer 1: Harness (Claude Code, Ghostty, Maestro)

The harness is the client AI software you use to interact with an LLM. Claude Code will be the tool I use as the basis for my examples. Other popular options include [Codex](https://github.com/openai/codex), [Gemini CLI](https://github.com/google-gemini/gemini-cli), and [OpenCode](https://opencode.ai). Sometimes such tools are called AI agents or AI orchestrators; the terminology is ambiguous and overlapping.

You install the harness on your workstation and give it access to your local tools and files. That makes it much more capable than AI providers’ web-based chat interfaces.

Sign up for a [Claude subscription](https://www.anthropic.com/pricing), then install Claude Code. It’s a command-line tool, and this is the approach I recommend for technologists. If you don’t like using a terminal, you can download the [Claude desktop app](https://claude.ai/download). Click its `</>` icon to use its built-in (but slightly hidden) Claude Code app.

If you’ll be using the command-line version of Claude Code on macOS or Linux, install [Ghostty](https://ghostty.org). It’s a better choice than the native terminal apps. You don’t need it if you’ll use Claude Code solely in the Claude desktop app.

If you find yourself running several Claude Code sessions at once, [Maestro](https://runmaestro.ai) will launch and manage multiple Claude Code instances side by side. Think of it as a supercharged alternative to running them in Ghostty or the Claude desktop app.

> By the way, don’t get hung up on the word “code” in the name Claude Code. It’s useful for any scenario where you want a customizable harness for Anthropic’s AI models.

## Layer 2: Scaffolding (PAI, Skills)

Daniel Miessler’s [PAI project](https://ourpai.ai/) amplifies Claude Code, making it smarter and attuned to your specific needs. Daniel describes PAI as a “context-based life operating system.”

As Anthropic improves Claude Code, it absorbs some of the capabilities PAI currently offers. Daniel keeps advancing PAI, staying a step ahead of what’s possible with Claude Code alone. For example, PAI gives Claude Code an adaptive approach to solving problems that Daniel calls [The Algorithm](https://github.com/danielmiessler/TheAlgorithm), a method he designed to “hill-climb toward the ideal state using testable criteria.”

PAI includes [Skills](https://agentskills.io/what-are-skills) that extend Claude Code’s capabilities. For instance, [the Council Skill](https://x.com/DanielMiessler/status/2033288165184962971) pressure-tests your document, code, or idea from multiple perspectives. To do this, the Skill creates different personas with expertise relevant to your task, gathers their critique and ideas, and has them debate each other before unifying their perspectives.

When you run the [PAI installer](https://ourpai.ai/#install), it’ll ask you some questions about yourself. Don’t worry if you aren’t sure about the answers. It’ll be easy to adjust them later. For example, the installer asks you for an [ElevenLabs](https://elevenlabs.io) API key, which PAI can use to speak with you; if you don’t need that feature, don’t bother with the key.

Beyond PAI, Skills offer additional ways of expanding the capabilities of Claude Code. For example, Anthropic publishes [its official Skills](https://github.com/anthropics/skills), which include the ability to work with PDF and Microsoft Office files. Add them through Claude Code’s `/plugin` command.

> Treat Skills like you’d treat any third-party software that might turn out to be malware. Only install Skills from trusted authors and sources.

## Layer 3: Personalization (PAI Customizations)

PAI is meant to be an extension of you, which means it needs to know about your goals, tools, likes, and dislikes. This can feel personal, and that’s the intent. It’s what will allow Claude Code to become *your* Claude Code, so it can code, research, and write the way that works best for you.

PAI refers to its understanding of who you are as a “Telos,” which it captures in a series of markdown-formatted files. You can edit them yourself, but it’s easier to let Claude Code do that. Here’s a sample prompt you can give Claude Code for this. Replace [FILES] with paths to your resume, papers, notes, apps you’ve built, anything that captures how you think and work.

```
Help me set up my personal TELOS without overwhelming me. Use the Telos Skill. Start by reviewing these files for baseline context: [FILES]. Review silently, then interview me for 20-30 minutes, one question at a time, to populate only four files: MISSION.md (2-3 things my life is actually about), BELIEFS.md (5-7 specific beliefs, not platitudes), BOOKS.md (5-10 books that shaped my thinking, and why), and WRONG.md (3-5 things I used to believe but don't, and what updated me). Let the baseline guide what to ask, skip, and probe deeper. If I answer generically, push me for the specific story or stake behind it. Keep entries honest, not aspirational.
```

You can return to Claude Code later to work through the remaining Telos files. If you’re unsure what a file is for or how to approach it, ask it. You can also revisit your earlier Telos answers when life gives you something specific to record, such as a job role that changed, a goal that shifted, or a book that affected how you think.

Some of the Skills that come with PAI require API keys. For example, the Media Skill uses image-generation APIs to create illustrations and visuals. The Scraping Skill uses services such as [Apify](https://apify.com/) to access web content that would otherwise be hard to retrieve.

You can ask Claude Code to walk you through the process of setting up these keys based on your plans. Use a prompt like this:

```
Which PAI Skills need API keys? For each, explain what the Skill does, which API it uses, the approximate cost, whether there's a free tier, and why someone like me might or might not want it.
```

## Layer 4: Hardening (Security Tweaks)

By default, Claude Code asks for approval before running most tools. PAI pre-approves most shell commands, file reads, and MCP tool calls, so you aren’t interrupted during normal work. It still requires confirmatio...