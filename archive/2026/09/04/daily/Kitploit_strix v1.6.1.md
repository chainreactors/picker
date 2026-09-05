---
title: strix v1.6.1
url: https://kitploit.com/en/posts/github-usestrix-strix-v161
source: Kitploit
date: 2026-09-04
fetch_date: 2026-09-05T06:28:31.328782
---

# strix v1.6.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/2/d047c43ce0248573d8e04dcff4ba48d57413c614d6c0feb9c13b0d20a7f9efc4.png)

New releaseSep 4, 2026

# strix v1.6.1

Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.

Share

[![Strix Banner](https://raw.githubusercontent.com/usestrix/.github/main/imgs/cover.png)](https://strix.ai/)

# Strix

### The open-source AI pentesting tool. Autonomous AI hackers that find and fix your app’s vulnerabilities.

[![Docs](https://img.shields.io/badge/Docs-docs.strix.ai-2b9246?style=for-the-badge&logo=gitbook&logoColor=white)](https://docs.strix.ai)
[![Website](https://img.shields.io/badge/Website-strix.ai-f0f0f0?style=for-the-badge&logoColor=000000)](https://strix.ai)
[![](https://dcbadge.limes.pink/api/server/strix-ai)](https://discord.gg/strix-ai)

[![Strix Cloud](https://img.shields.io/badge/Strix%20Cloud-app.strix.ai-2b9246?style=for-the-badge&logoColor=white)](https://app.strix.ai?utm_source=github&utm_medium=readme&utm_content=badge_cloud)
[![Try Strix Enterprise](https://img.shields.io/badge/Try%20Strix%20Enterprise-555555?style=for-the-badge&logoColor=white)](https://strix.ai/demo?utm_source=github&utm_medium=readme&utm_content=badge_demo)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/usestrix/strix)
[![GitHub Stars](https://img.shields.io/github/stars/usestrix/strix?style=flat-square)](https://github.com/usestrix/strix)
[![License](https://img.shields.io/badge/License-Apache%202.0-3b82f6?style=flat-square)](https://github.com/usestrix/strix/blob/main/LICENSE)
[![PyPI Version](https://img.shields.io/pypi/v/strix-agent?style=flat-square)](https://pypi.org/project/strix-agent/)

[![Join Discord](https://raw.githubusercontent.com/usestrix/.github/main/imgs/Discord.png)](https://discord.gg/strix-ai)
[![Follow on X](https://raw.githubusercontent.com/usestrix/.github/main/imgs/X.png)](https://x.com/strix_ai)

[![usestrix%2Fstrix | Trendshift](https://trendshift.io/api/badge/trendshift/repositories/15362/weekly)](https://trendshift.io/repositories/15362?utm_source=trendshift-badge&utm_medium=badge&utm_campaign=badge-trendshift-15362)
[![usestrix/strix | Trendshift](https://trendshift.io/api/badge/repositories/15362)](https://trendshift.io/repositories/15362)

> [!TIP]
> **New!** Strix integrates seamlessly with GitHub Actions and CI/CD pipelines. Automatically scan for vulnerabilities on every pull request and block insecure code before it reaches production - [Get started with no setup required](https://app.strix.ai?utm_source=github&utm_medium=readme&utm_content=tip_ci).

---

## Strix Overview

Strix are autonomous AI penetration testing agents that act just like real hackers - they run your code dynamically, find vulnerabilities, and validate them through actual proofs-of-concept. Built for developers and security teams who need fast, accurate security testing without the overhead of manual pentesting or the false positives of static analysis tools.

**Key Capabilities:**

* **Full pentesting toolkit** - reconnaissance, exploitation, and validation out of the box
* **Multi-agent orchestration** - teams of AI pentesters that collaborate and scale
* **Real exploit validation** - working PoCs, not false positives like legacy vulnerability scanners
* **Developer‑first CLI** - actionable findings with remediation guidance
* **Auto‑fix & reporting** - generate patches and compliance-ready pentest reports

[![Strix Demo](https://raw.githubusercontent.com/usestrix/strix/HEAD/.github/screenshot.png)](https://strix.ai)

## Use Cases

* **Application Security Testing** - Detect and validate critical vulnerabilities in your applications
* **Rapid Penetration Testing** - Get penetration tests done in hours, not weeks, with compliance reports
* **Bug Bounty Automation** - Automate bug bounty research and generate PoCs for faster reporting
* **CI/CD Integration** - Run tests in CI/CD to block vulnerabilities before reaching production

## 🚀 Quick Start

**Prerequisites:**

* Docker (running)
* An LLM API key from any [supported provider](https://docs.strix.ai/llm-providers/overview) (OpenAI, Anthropic, Google, etc.)

### Installation & First Scan

root@kitploit:~

```
# Install Strix
curl -sSL https://strix.ai/install | bash

# Configure your AI provider
export STRIX_LLM="openrouter/z-ai/glm-5.3"
export LLM_API_KEY="your-api-key"

# Run your first security assessment
strix --target ./app-directory
```

> [!NOTE]
> First run automatically pulls the sandbox Docker image. Results are saved to `strix_runs/<run-name>`

---

## Ways to Run Strix

* **Open Source** - free, runs locally with Docker and your own LLM key. [Quick Start](https://docs.strix.ai/quickstart)
* **Strix Cloud** - no setup, validated findings, one-click autofix, and PR reviews. [Run a pentest →](https://app.strix.ai?intent=pentest&utm_source=github&utm_medium=readme&utm_content=table_cloud)
* **Enterprise** - SSO, compliance-ready reports, VPC or self-hosted deployment. [Try Strix Enterprise →](https://strix.ai/demo?utm_source=github&utm_medium=readme&utm_content=table_demo)

---

## ☁️ Strix Cloud

Try the Strix full-stack penetration testing platform at **[app.strix.ai](https://app.strix.ai?utm_source=github&utm_medium=readme&utm_content=cloud_heading)** - sign up for free, connect your repos and domains, and launch a pentest in minutes.

* **Validated findings with PoCs** - every vulnerability includes a working proof-of-concept exploit and reproduction steps
* **One-click autofix** - AI-generated security patches as ready-to-merge pull requests
* **Continuous pentesting** - always-on vulnerability scanning that keeps pace with your deployments
* **DevSecOps integrations** - GitHub, GitLab, Bitbucket, Slack, Jira, Linear, and CI/CD pipelines
* **Continuous learning** - AI that builds on past findings, adapts to your codebase, and reduces false positives over time

[**Run a pentest →**](https://app.strix.ai?intent=pentest&utm_source=github&utm_medium=readme&utm_content=cloud_cta)

## 🏢 Enterprise

Get the same Strix experience with enterprise-grade controls: SSO (SAML/OIDC), custom compliance-ready penetration testing reports (SOC 2, ISO 27001, PCI DSS), dedicated support and SLA, custom deployment options (VPC or self-hosted), BYOK model support, and tailored AI pentesting agents optimized for your environment.

[**Try Strix Enterprise →**](https://strix.ai/demo?utm_source=github&utm_medium=readme&utm_content=enterprise_cta)

---

## 🤖 Use Strix from Your Coding Agent

Strix is agent-ready. Give Claude Code, Cursor, Codex, or any [SKILL.md-compatible](https://agentskills.io) agent the ability to run pentests, fix findings, and set up CI scanning:

root@kitploit:~

```
npx skills add usestrix/strix
```

This installs nine skills for running pentests, fixing findings, and CI scanning, against code, web apps, APIs, and the OWASP Top 10. Agents can use the local CLI or the managed cloud with the same engine.

See [`AGENTS.md`](https://github.com/usestrix/strix/blob/main/AGENTS.md) for the quick reference, [docs.strix.ai/llms.txt](https://docs.strix.ai/llms.txt) for the CLI, and [docs.app.strix.ai](https://docs.app.strix.ai) for the API.

---

## ✨ Features

### Agentic Pentesting Tools

Strix agents come equipped with a comprehensive offensive security toolkit - the same tools used by professional penetration testers and ethical hackers:

* **HTTP Interception Proxy** - Full request/response manipulation and analysis with Caido
* **Browser Exploitation** - Automated browser for testing XSS, CSRF, clickjacking, and auth bypass flows
* **Shell & Command Executi...