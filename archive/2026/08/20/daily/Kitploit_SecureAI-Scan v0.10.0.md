---
title: SecureAI-Scan v0.10.0
url: https://kitploit.com/en/posts/github-akanthed-secureai-scan-v0100
source: Kitploit
date: 2026-08-20
fetch_date: 2026-08-21T03:03:24.139126
---

# SecureAI-Scan v0.10.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/7064/a207bc9facd660bd5c48dd6f284b225c53f66e9d1de47876aac27472d0f83c87.png)

New releaseAug 20, 2026

# SecureAI-Scan v0.10.0

SecureAI-Scan is a CLI tool that scans TypeScript and JavaScript codebases for security issues specific to AI-powered apps — prompt injection, MCP tool abuse, RAG data poisoning, agent trust violations, and more.

Share

# SecureAI-Scan

[![npm version](https://img.shields.io/npm/v/secureai-scan)](https://www.npmjs.com/package/secureai-scan)
[![npm downloads](https://img.shields.io/npm/dm/secureai-scan)](https://www.npmjs.com/package/secureai-scan)
[![CI](https://github.com/akanthed/SecureAI-Scan/actions/workflows/ci.yml/badge.svg)](https://github.com/akanthed/SecureAI-Scan/actions/workflows/ci.yml)
[![CodeQL](https://github.com/akanthed/SecureAI-Scan/actions/workflows/codeql.yml/badge.svg)](https://github.com/akanthed/SecureAI-Scan/actions/workflows/codeql.yml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/akanthed/SecureAI-Scan/badge)](https://scorecard.dev/viewer/?uri=github.com/akanthed/SecureAI-Scan)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Node](https://img.shields.io/badge/node-%3E=22.12-brightgreen)](https://nodejs.org)
[![OWASP](https://img.shields.io/badge/OWASP-LLM%20%C2%B7%20ASI%20%C2%B7%20MCP%20Top%2010-000000)](#rules)

**The AI security scanner that proves its findings.**

SecureAI-Scan finds LLM, MCP, Agent Skill, and RAG vulnerabilities in **TypeScript, JavaScript, and Python** — and shows you the evidence: the exact source → flow → sink path for every dataflow finding, resolved through real imports, not keyword matching.

It provides launch-week support for the official [OWASP Top 10 for LLM Applications 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/), alongside the [Top 10 for Agentic Applications (2026)](https://genai.owasp.org/) and the [MCP Top 10](https://owasp.org/www-project-mcp-top-10/). Every threat model distinguishes static coverage from runtime concerns.

## Get started in 30 seconds

root@kitploit:~

```
npx --yes [email protected] scan .
```

No account, cloud upload, Python interpreter, or configuration required. TypeScript, JavaScript, Python, MCP configs, and Agent Skill bundles are detected automatically.

**Measured `0.9.0` release candidate:** 136/136 tests · 88.08% statement coverage · 12,676 files across 9 public repositories · 0 new default-tier fingerprints against the reviewed baseline. [Evidence](https://github.com/akanthed/secureai-scan/blob/HEAD/docs/benchmarks/v0.9.0.json) · [methodology and limits](https://github.com/akanthed/secureai-scan/blob/HEAD/docs/ReleaseAssurance.md)

root@kitploit:~

```
  ▌ HIGH  AI001  Prompt injection via user input
    PROVEN  LLM01:2026 Prompt Injection

    source src/chat.ts:8   request data `req.body.input`
    flow   src/chat.ts:13  passed as `systemPrompt`
    sink   src/chat.ts:10  openai.chat.completions.create — system role (OpenAI)

    fix    Keep system prompts static; pass user input as a user-role message.
```

**Is this for you?** SecureAI-Scan is scoped deliberately to LLM, MCP, and RAG/agent risks — prompt injection, tool poisoning, unsafe output handling, vector-store access control, agent-skill poisoning. It is not a general SAST or secrets scanner, and doesn't try to be one; a known-malicious package with no LLM-shaped payload (e.g. a hardcoded exfiltration address in an email API call) is caught by the offline advisory list (`DEP003`), not a pattern rule. If your codebase talks to an LLM, an MCP server, a vector store, or ships Agent Skills, this is built for you.

## Contents

* [Why this scanner is different](#why-this-scanner-is-different)
* [How it compares](#how-it-compares)
* [Get started in 30 seconds](#get-started-in-30-seconds)
* [See it work](#see-it-work)
* [Commands](#commands)
* [GitHub Action](#github-action)
* [Rules](#rules)
* [Architecture](#architecture)
* [MCP server (use it from Claude)](#mcp-server-use-it-from-claude)
* [Claude Skill](#claude-skill)
* [Trust and release assurance](#trust-and-release-assurance)
* [The precision contract](#the-precision-contract)
* [Testing & benchmarking](#testing--benchmarking)
* [Roadmap](#roadmap)
* [Contributing](#contributing)

## Why this scanner is different

* **Evidence tiers, not noise.** Every finding is `proven` (traced dataflow or parsed config fact), `likely` (resolved sink, one heuristic hop), or `heuristic`. **A default scan shows only proven + likely.** Heuristics are opt-in via `--paranoid`.
* **Import-resolved detection.** A call is only an "LLM call" if it resolves to a real SDK import (`openai`, `@anthropic-ai/sdk`, `ai`, `@google/genai`, LangChain, Bedrock, …). Your Google Maps client will never be flagged as an LLM again.
* **Precision-gated, and benchmarked against real repos.** The test suite asserts every vulnerable fixture fires *and* every safe fixture stays clean — a false positive on the safe corpus fails the build. Beyond that, `npm run regression` scans real public repos (OpenAI/Anthropic/Vercel AI SDKs, official MCP servers, LlamaIndex) against a committed, hand-reviewed baseline and **fails on any new `proven`/`likely` finding**. See [Testing & benchmarking](#testing--benchmarking) for the actual before/after numbers, or [What we found scanning real repos](https://github.com/akanthed/secureai-scan/blob/HEAD/docs/RealWorldFindings.md) for the story behind them — a 6/6 catch rate on a labeled malicious-skill corpus, and why we're *not* calling llama\_index "vulnerable" over an honest library-level finding.
* **SARIF for GitHub code scanning.** `--output report.sarif` puts findings inline on pull requests and in the Security tab.
* **AI-BOM.** `secureai-scan bom .` builds a syntax-derived inventory of SDKs, model IDs, vector stores, agent frameworks, and MCP servers, mapped to OWASP LLM Top 10 / EU AI Act documentation needs.
* **MCP config scanning.** Parses `.mcp.json`, `claude_desktop_config.json`, `.cursor/mcp.json`: unpinned `npx -y` servers, inline secrets, plaintext HTTP transports.
* **MCP tool-poisoning detection.** Catches the pattern behind the WhatsApp MCP rug-pull and postmark-mcp backdoor — invisible Unicode, agent-directed injection phrases, and cross-tool shadowing in tool names/descriptions, statically, before you ever run the server.
* **MCP command-injection detection.** Flags MCP stdio transport `command`/`args` built from request data — the pattern behind the 2026 MCP STDIO RCE disclosure.
* **Agent Skill poisoning detection.** The same invisible-Unicode, injection-phrase, and shadowing checks applied to `SKILL.md` files — Agent Skills load into context wholesale, so a poisoned skill is a poisoned tool description by another name.
* **Evasion-resistant skill scanning.** Skill bundles are scanned as *directories*, not just their `SKILL.md`, and every content check runs against deobfuscated variants of the text. This targets the published techniques — homoglyphs, zero-width splitting, payloads staged in `.git/` or `build/`, exfiltration hidden in a `*.test.ts` file — that bypassed **>90% of the nine scanners** surveyed in *Cloak and Detonate* (arXiv:2607.02357). See [Evasion resistance](#evasion-resistance).
* **Known-vulnerable and known-malicious package advisories, version-aware.** Checks every dependency and every MCP-launched package against a bundled advisory snapshot — a hand-curated list of documented in-the-wild backdoors, plus HIGH/CRITICAL OSV advisories for an LLM/MCP/RAG package watchlist, regenerated by [`scripts/sync-advisories.js`](https:...