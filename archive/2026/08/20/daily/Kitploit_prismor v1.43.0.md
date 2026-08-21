---
title: prismor v1.43.0
url: https://kitploit.com/en/posts/github-prismorsec-prismor-v1430
source: Kitploit
date: 2026-08-20
fetch_date: 2026-08-21T03:03:28.834330
---

# prismor v1.43.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/13903/0e84c7211b3275de581182b7f69c44d8224142323b43220dd1234eee17616757.png)

New releaseAug 20, 2026

# prismor v1.43.0

Self-hosted runtime control plane for AI agents. Observe or HITL approve or Block rogue tool calls before it executes: secret leaks, prompt injection, supply chain etc in a local dashboard. Agent agnostic (Claude,codex etc.)

Share

# Prismor

[![PyPI](https://img.shields.io/pypi/v/prismor)](https://pypi.org/project/prismor/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://github.com/PrismorSec/prismor/blob/main/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/PrismorSec/prismor)
[![X](https://img.shields.io/badge/@prismor__dev-black?logo=x&logoColor=white)](https://x.com/prismor_dev)
[![DeepWiki](https://img.shields.io/badge/DeepWiki-prismor-blue?logo=bookstack&logoColor=white)](https://deepwiki.com/PrismorSec/prismor)
[![Discord](https://img.shields.io/badge/Discord-join-5865F2?logo=discord&logoColor=white)](https://discord.gg/FH2PRX754c)

### Runtime security hooks for Claude Code, Codex, and other AI coding agents.

Prismor can also be used in observe mode to see agent session activity and dangerous actions in a local self-serve dashboard

### [**Website**](https://prismor.dev) • [**Onboard with Skill**](SKILL.md)

[![Claude Code](https://d205xtizsu1yjh.cloudfront.net/icons/coding-agents/claude-code.svg "Claude Code")](https://github.com/anthropics/claude-code)
[![Codex CLI](https://d205xtizsu1yjh.cloudfront.net/icons/coding-agents/codex.svg "Codex CLI")](https://github.com/openai/codex)
[![Gemini CLI](https://d205xtizsu1yjh.cloudfront.net/icons/coding-agents/gemini-cli.svg "Gemini CLI")](https://github.com/google-gemini/gemini-cli)
![Cursor](https://d205xtizsu1yjh.cloudfront.net/icons/coding-agents/cursor.svg "Cursor")
![GitHub Copilot](https://d205xtizsu1yjh.cloudfront.net/icons/coding-agents/github-copilot.svg "GitHub Copilot")
![OpenCode](https://d205xtizsu1yjh.cloudfront.net/icons/coding-agents/opencode.svg "OpenCode")
![Pi Agent](https://d205xtizsu1yjh.cloudfront.net/icons/coding-agents/pi-agent.svg "Pi Agent")
![Kiro](https://d205xtizsu1yjh.cloudfront.net/icons/coding-agents/kiro.svg "Kiro")
![Kimi Code](https://d205xtizsu1yjh.cloudfront.net/icons/coding-agents/kimi-code.svg "Kimi Code")
![Trae / Trae CN](https://d205xtizsu1yjh.cloudfront.net/icons/coding-agents/trae.svg "Trae / Trae CN")
![Google Antigravity](https://d205xtizsu1yjh.cloudfront.net/icons/coding-agents/google-antigravity.svg "Google Antigravity")

Plus Grok Build, Crush, OpenHands, Qwen Code, Continue CLI, Goose, Hermes, OpenClaw, Devin CLI, Factory Droid, Aider, and more — see <AGENT_INTEGRATIONS.md> for the full coverage matrix

---

![Prismor demo](https://assets.kitploit.com/production/public/readmes/13903/a5ce575cfad36bacc81b2d679bc6898adc5e99c526eceb4961b1a1c921745659.gif)

---

## The Problem

AI coding agents execute shell commands, read and write files, access credentials, and call external APIs. They do this autonomously, often across many steps, with limited checkpoints.

This creates risks that traditional security tooling isn't designed for:

* **Prompt injection** - malicious content in a file, issue, or web page can redirect the agent mid-task
* **Unintended destructive actions** - an agent misinterprets an instruction and runs something irreversible
* **Secret exfiltration** - an agent reads `.env` or credential files as part of a debugging task and sends the content outbound
* **Privilege escalation** - an agent modifies sudoers, CI pipelines, or file permissions to resolve a permission error
* **Dependency manipulation** - an agent installs or rewrites a package at the direction of injected input
* **Supply chain risk** - an agent installs a vulnerable or 0-day package while optimizing for code velocity

Standard OS-level and endpoint security tools monitor the kernel and filesystem. By the time they see an action, the agent has already decided to take it. The gap is at the agent layer for avoiding the attack

---

## Quick Start (30s)

root@kitploit:~

```
pip install prismor
prismor setup
```

For the Skill, curl, and git-clone alternatives, plus PEP 668 systems and secret-cloaking setup, see the[full installation guide](https://github.com/prismorsec/prismor/blob/HEAD/docs/installation.md).

---

## Capabilities

![Prismor Architecture](https://assets.kitploit.com/production/public/readmes/13903/0e84c7211b3275de581182b7f69c44d8224142323b43220dd1234eee17616757.png)

* 🛡️[Prismor](https://github.com/prismorsec/prismor/blob/HEAD/docs/prismor-runtime.md) covers the policy engine, session logs, security audit, and CLI reference
* 📦 [Supply Chain](https://github.com/prismorsec/prismor/blob/HEAD/docs/supply-chain.md) covers install-time enforcement, IOC matching, and risk scoring
* 🛜 [Network Isolation](https://github.com/prismorsec/prismor/blob/HEAD/docs/network-isolation.md) covers policy-driven egress control, raw IP detection, and tunnel blocking
* 🔍 [Skill Scanner](https://github.com/prismorsec/prismor/blob/HEAD/docs/skill-scanner.md) covers MCP server and skill risk scanning across supported agents
* 🚦 [MCP Guardrails](https://github.com/prismorsec/prismor/blob/HEAD/docs/prismor-runtime.md#custom-guardrails-for-mcp-tools) let you block a specific MCP server or tool, or require human approval before the agent calls it, with a policy rule you write yourself
* 🛰️ [MCP Gateway](https://github.com/prismorsec/prismor/blob/HEAD/docs/mcp-gateway.md) is a single MCP connector that fronts every other MCP server you use — each `tools/call` is policy-evaluated before it forwards and each response is injection-scanned before the model sees it, so a poisoned tool result never becomes context. `prismor mcp-gateway install` moves an existing `.mcp.json` behind it
* 🏷️ [Tool Tags](https://github.com/prismorsec/prismor/blob/HEAD/docs/tool-tags.md) classify tools by capability (read, write, network, exec) so a rule can say "nothing that reads private data may also reach the network" instead of naming every tool one by one — MCP tools self-declare via `_meta`, and `prismor tags` lists, tests, and lints the rule expressions
* 🔐 [Sweep and Cloak](https://github.com/prismorsec/prismor/blob/HEAD/docs/sweep-and-cloak.md) covers secret prevention at tool boundaries, practical setup, best practices, threat model, and cleanup for leaked secrets
* 🦞 [OpenClaw Integration](https://github.com/prismorsec/prismor/blob/HEAD/docs/openclaw.md) covers runtime hooks, prompt-injection scanning, and project or user-scope setup for OpenClaw
* 🤖 [Hermes Agent Cloaking](https://github.com/prismorsec/prismor/blob/HEAD/docs/hermes.md) covers Hermes-specific secret cloaking with pip entry-point auto-discovery, filesystem install, and pre\_gateway\_dispatch paste guard
* 🧠 [Semantic Guard](https://github.com/prismorsec/prismor/blob/HEAD/docs/semantic-guard.md): opt-in hybrid layer that adds an LLM-assisted intent check for paraphrased prompt-injection attempts the regex rules cannot catch
* 🪤 [Canary](https://github.com/prismorsec/prismor/blob/HEAD/docs/canary.md) plants honeytoken credential files that trip a CRITICAL finding the moment an agent reads them, catching recon behavior
* 🪪 [IAM](https://github.com/prismorsec/prismor/blob/HEAD/docs/iam.md) gives each agent a named identity and least-privilege permission profile when several agents share a workspace
* 🧩 [Framework Agents](https://github.com/prismorsec/prismor/blob/HEAD/docs/frameworks-overview.md) guards production agents (OpenAI Agents SDK, L...