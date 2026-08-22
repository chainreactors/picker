---
title: claude-bug-bounty v6.0.0
url: https://kitploit.com/en/posts/github-shuvonsec-claude-bug-bounty-v600
source: Kitploit
date: 2026-08-21
fetch_date: 2026-08-22T02:50:55.017109
---

# claude-bug-bounty v6.0.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/65/8c9b8d571325539775f92d58d2a095c0fbb5cc7c272b28b4edb291b886d9d60b.png)

New releaseAug 21, 2026

# claude-bug-bounty v6.0.0

AI-powered bug bounty hunting from your terminal - recon, 20 vuln classes, autonomous hunting, and report generation. All inside Claude Code.

Share

![BugHunter](https://raw.githubusercontent.com/shuvonsec/claude-bug-bounty/HEAD/logo.png)

# BugHunter

**AI-powered bug bounty hunting — recon to report, in your terminal.**

[Free Setup](#standalone-mode--no-subscription-required)
·
[Quick Start](#quick-start)
·
[Commands](#commands)
·
[What It Finds](#what-it-finds)
·
[Install](#installation)
·
[FAQ](FAQ.md)

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://github.com/shuvonsec/claude-bug-bounty/blob/main/LICENSE)
![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB.svg?style=flat-square&logo=python&logoColor=white)
![Free Standalone Mode](https://img.shields.io/badge/Standalone-Free-brightgreen.svg?style=flat-square)
[![Claude Code Plugin](https://img.shields.io/badge/Claude_Code-Plugin-D97706.svg?style=flat-square)](https://claude.ai/claude-code)
[![Tests](https://img.shields.io/github/actions/workflow/status/shuvonsec/claude-bug-bounty/tests.yml?branch=main&style=flat-square&label=tests)](https://github.com/shuvonsec/claude-bug-bounty/actions/workflows/tests.yml)
[![GitHub Stars](https://img.shields.io/github/stars/shuvonsec/claude-bug-bounty?style=flat-square&color=yellow)](https://github.com/shuvonsec/claude-bug-bounty/stargazers)
[![Powered by AwareXone.com](https://img.shields.io/badge/Powered_by-AwareXone.com-7F55FF.svg?style=flat-square)](https://awarexone.com)

[![shuvonsec%2Fclaude-bug-bounty | Trendshift](https://trendshift.io/api/badge/repositories/23808)](https://trendshift.io/repositories/23808?utm_source=repository-badge&utm_medium=badge&utm_campaign=badge-repository-23808)
![BUGHUNTER — Bug Bounty Automation Pipeline](https://assets.kitploit.com/production/public/readmes/65/8b735147a39d67f81ef8827d6dc67efdc24467056cfb5b6f6f5fd02b03dd8b37/953331149f16c4b1e7705fd51f139284db8133ed5cd694b3a3bc05c4a2c7f511-display-v1.webp)

[![AwareXone](https://assets.kitploit.com/production/public/readmes/65/29e21784cbe8b37142a688801ddd02d4084136effa303a59c67cdd8621e4ac2a/b44baafd696ad5280f1c515671c279895b049b007d04ef2400f00b7eaef441fc-display-v1.webp)](https://awarexone.com)

**Powered by [AwareXone.com](https://awarexone.com)** — Your AI Agent Against Scams & Fraud

> ### 💜 Open for Sponsorship
>
> **BugHunter is open for sponsorship.** Your support funds new features and keeps the free standalone mode running for everyone. Sponsors get a logo and link right here in the README, plus a credit in every release.
>
> **Want to sponsor?** Reach out at **[AwareXone.com](https://awarexone.com)** or email **[[email protected]](/cdn-cgi/l/email-protection#4c3f24393a23223f292f0c2b212d2520622f2321)**.

---

## What Is This?

A professional bug bounty hunting toolkit that works **with or without a Claude subscription**. Give it a target — it handles recon, tests for vulnerabilities, validates findings through a strict gate, and writes submission-ready reports for HackerOne, Bugcrowd, Intigriti, and Immunefi.

**It remembers everything.** Patterns found on one target inform the next. Sessions pick up where they left off.

Works as a [Claude Code](https://claude.ai/claude-code) plugin **or** as a fully standalone CLI (`bughunter`) powered by free AI providers.

---

## Standalone Mode — No Subscription Required

**You no longer need Claude Code, Claude Pro, or any paid AI subscription.**

Install once, use the `bughunter` command from any terminal on your machine:

root@kitploit:~

```
git clone https://github.com/shuvonsec/claude-bug-bounty.git
cd claude-bug-bounty
./install.sh --agent standalone
```

Rerun the same command after pulling updates. The installer detects and
refreshes the active managed `bughunter` command, including older installations
under `/usr/local/bin` or `~/.local/bin`, while preserving your saved provider
configuration in `~/.bughunter/config.json`.

To uninstall the standalone command while keeping its configuration:

root@kitploit:~

```
./uninstall.sh --agent standalone
```

Use `--purge-config` to also delete `~/.bughunter/config.json`. The uninstaller
also supports `claude`, `opencode`, `pi`, `codex`, `agents`, and `all` targets.

root@kitploit:~

```
bughunter help               # show every command
bughunter setup              # choose your AI provider (Ollama is free + offline)
bughunter recon target.com   # map the attack surface
bughunter hunt  target.com   # hunt for vulnerabilities
bughunter validate "finding" # 7-Question Gate on your finding
bughunter report             # write a submission-ready report
bughunter chat               # interactive AI hunting shell
bughunter providers          # list all available AI providers
bughunter models             # list models and show the selected one
bughunter status             # check which provider is active
bughunter h target.com       # short alias for hunt
bughunter r target.com       # short alias for recon
bughunter v "finding"        # short alias for validate
```

### Free AI Providers (auto-detected, free-first priority)

| Provider | Cost | Privacy | Speed | Get Started |
| --- | --- | --- | --- | --- |
| **Ollama** | 100% free · runs locally | Full — stays on your machine | Fast | `ollama pull qwen2.5:14b` |
| **Groq** | Free tier available | Cloud | Very fast | [console.groq.com](https://console.groq.com) → get API key |
| **DeepSeek** | Very cheap (v4-flash / v4-pro) | Cloud | Fast | [platform.deepseek.com](https://platform.deepseek.com) |
| Claude API | Paid | Cloud | Fast | [console.anthropic.com](https://console.anthropic.com) |
| OpenAI | Paid | Cloud | Fast | [platform.openai.com](https://platform.openai.com) |
| **Grok (xAI)** | Paid | Cloud | Fast | [console.x.ai](https://console.x.ai) → `grok-4.5` |
| **OpenRouter** | Subscription / pay-as-you-go | Cloud | Fast | [openrouter.ai/keys](https://openrouter.ai/keys) → get API key |
| **OrcaRouter** | Subscription / pay-as-you-go | Cloud | Fast | [orcarouter.ai](https://www.orcarouter.ai) → get API key |

BugHunter auto-detects providers in this order: **Ollama → Groq → DeepSeek → … → OrcaRouter → OpenRouter → Claude → OpenAI**

Switch providers or choose an installed Ollama model anytime: `bughunter setup`.
The setup can also be fully non-interactive:

root@kitploit:~

```
bughunter setup --provider ollama --model qwen2.5:14b
```

For a one-off override, put the option before the command:

root@kitploit:~

```
bughunter --provider ollama --model qwen3:14b hunt target.com
```

### Zero-cost fully offline setup

root@kitploit:~

```
# 1. Install Ollama (runs AI locally, no internet needed after download)
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull qwen2.5:14b          # ~9 GB, one-time download

# 2. Install BugHunter
git clone https://github.com/shuvonsec/claude-bug-bounty.git
cd claude-bug-bounty
./install.sh --agent standalone   # creates system-wide 'bughunter' command

# 3. Hunt
bughunter setup       # choose Ollama, then choose one of its installed models
bughunter recon target.com
```

### Groq setup (free cloud, fastest option)

root@kitploit:~

```
export GROQ_API_KEY="your-key-here"     # free at console.groq.com
./install.sh --agent standalone
bughunter setup       # choose Groq
bughunter hunt target.com
```

---

## Quick Start

**Option A — standalone (no subscription, works for everyone)**

root@kitploit:~

```
git ...