---
title: 0day-Rubbish batch-8-2026-08
url: https://kitploit.com/en/posts/github-exploit-garbage-0day-rubbish-batch-8-2026-08
source: Kitploit
date: 2026-08-30
fetch_date: 2026-08-31T07:52:24.320415
---

# 0day-Rubbish batch-8-2026-08

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/49814/627ab69c8421bb2f2fb74e7c5916ea10fdffc5d5b1670eee2f78ad9de9d94bde.png)

New releaseAug 30, 2026

# 0day-Rubbish batch-8-2026-08

Redefining vulnerability disclosure in the AI era. We mass-produce exploitable 0days and disclose them directly, using event-driven pressure to elevate vendor security standards and advance the field.

Share

# 0day Rubbish

> **0day vulnerabilities have become rubbish in the AI era.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Latest batch](https://img.shields.io/badge/Latest_batch-10_advisories-red)](https://0day-rubbish.com/blog)
[![Max CVSS](https://img.shields.io/badge/Max_CVSS-9.8-critical)](https://0day-rubbish.com/blog)
[![PoC](https://img.shields.io/badge/Every_advisory-working_PoC-blue)](https://0day-rubbish.com/blog)
[![Website](https://img.shields.io/badge/Website-0day--rubbish.com-brightgreen)](https://0day-rubbish.com)
[![Watchers](https://img.shields.io/github/watchers/Exploit-Garbage/0day-Rubbish?style=flat&logo=github)](https://github.com/Exploit-Garbage/0day-Rubbish/subscription)
[![Discussions](https://img.shields.io/github/discussions/Exploit-Garbage/0day-Rubbish?logo=github)](https://github.com/Exploit-Garbage/0day-Rubbish/discussions)
[![Last commit](https://img.shields.io/github/last-commit/Exploit-Garbage/0day-Rubbish?style=flat&logo=git)](https://github.com/Exploit-Garbage/0day-Rubbish/commits)

**🌐 Official Website**: <https://0day-rubbish.com/blog>

---

## 🎯 Why This Exists

Traditional vulnerability disclosure is broken. It's slow, bureaucratic, and ineffective. In the AI era, we can mass-produce 0days at scale—making individual vulnerabilities less valuable but more impactful when disclosed directly.

We believe **event-driven security hardening** is the most effective approach: only when vendors face real, exploitable threats do they prioritize fixes.

## 🔄 Our Disclosure Process

### Step 1: AI Discovery

Our automated AI systems continuously scan for vulnerabilities across real-world software, identifying potential 0-days through pattern analysis, fuzzing, and intelligent code review.

### Step 2: Verification & PoC Development

Each finding undergoes manual validation. We develop working proof-of-concept exploits to confirm exploitability and assess real-world impact.

### Step 3: Periodic Public Disclosure

Roughly every two weeks we disclose a new batch of verified, exploitable 0-day vulnerabilities we've discovered and validated:

* Full technical analysis and root cause
* Working PoC exploit code
* Affected versions and systems
* Impact assessment
* Recommended mitigations

No delays. No bureaucracy. Just facts.

**To all vendors**: We hope you can complete fixes before hackers exploit these vulnerabilities.

## ⚡ Core Principles

* **Real-world impact only**: We disclose only vulnerabilities that affect real-world systems with actual user bases
* **No worthless targets**: Non-exploitable vulnerabilities or devices with negligible user adoption are excluded—they're rubbish with zero value
* **Speed over protocol**: Direct disclosure drives faster action than traditional channels
* **Proof over claims**: Every disclosure includes working exploits
* **Impact over quantity**: Focus on high-severity, widely-deployed vulnerabilities
* **Transparency**: Full technical details, no hidden agendas
* **Non-profit**: Driven by passion for security research, not financial gain

## 🤝 Collaboration

We partner with:

* Top AI model providers advancing automated security research
* Security researchers exploring AI-powered discovery

## 🤖 AI Models Used

Our automated vulnerability discovery leverages cutting-edge large language models from leading AI providers:

* **Anthropic (Claude)** - Deep security pattern recognition and reasoning
* **OpenAI** - Advanced reasoning and code analysis
* **DeepSeek** - Specialized vulnerability detection
* **Z.ai (GLM)** - Long-context code analysis
* **Moonshot (Kimi)** - Long-context security analysis

---

## 📋 Disclosed Vulnerabilities

An AI-driven research process (multi-LLM ensemble: Claude, OpenAI, DeepSeek, GLM, Kimi) discovers 0-days in real-world enterprise software. Every advisory below ships a **full root-cause analysis** plus a **working, reproducible exploit script** — no detection-only writeups, no withheld details.

### Latest Batch — Batch 7 (10 advisories)

| # | Product | Affected Version | CVSS | Class | Advisory & PoC |
| --- | --- | --- | --- | --- | --- |
| 1 | Software AG webMethods MSR | 10.x | **9.8** | Default-creds XSLT Xalan Java-extension RCE | [XSLT Xalan ext → RCE](https://0day-rubbish.com/blog/softwareag-webmethods-msr-xslt-xalan-extension-rce) |
| 2 | NCache Enterprise | 5.3.6 | **9.8** | Unauth Assembly.LoadFrom RCE via Web Manager | [Assembly.LoadFrom → RCE](https://0day-rubbish.com/blog/ncache-enterprise-unauth-assembly-load-rce) |
| 3 | Brekeke PBX | 3.19.1.8 | **9.8** | Unauth XmlTransBean Util.exec RCE | [XmlTransBean → RCE](https://0day-rubbish.com/blog/brekeke-pbx-unauth-xmltransbean-rce) |
| 4 | CFEngine Enterprise Nova Hub | 3.27.1 | **8.8** | Auth VCS Settings Cmd Injection → Root | [gitServer → Root RCE](https://0day-rubbish.com/blog/cfengine-nova-hub-vcs-settings-root-rce) |
| 5 | RTS Intercom VLink Virtual Matrix | 6.60 | **8.8** | Auth OpenSSL Arg Injection → SYSTEM | [openssl -engine → SYSTEM RCE](https://0day-rubbish.com/blog/rts-vlink-openssl-arginj-system-rce) |
| 6 | Inflectra SpiraTeam | 9.3.0.0 | **8.8** | Auth SQLi → xp\_cmdshell RCE | [yAxisKey SQLi → RCE](https://0day-rubbish.com/blog/spirateam-planningboard-sqli-rce) |
| 7 | Scan2x ScanWebClient | 2.3.3.0 | **9.8** | Unauth File Upload → Webshell RCE | [FileUploadHandler → RCE](https://0day-rubbish.com/blog/scan2x-unauth-upload-rce) |
| 8 | Microsip ASD | 2026 Eval | **9.8** | Unauth UNC Binary-Planting RCE | [gbak.exe planting → RCE](https://0day-rubbish.com/blog/microsip-asd-unc-binary-planting-rce) |
| 9 | myDBR | 7.5.4 | **8.8** | Auth File-Editor PHP Code Injection | [fileedit\_v → RCE](https://0day-rubbish.com/blog/mydbr-file-editor-rce) |
| 10 | LogicalDOC Enterprise | 9.3 | **8.8** | Auth Automation Sandbox-Bypass RCE | [Velocity sandbox bypass → RCE](https://0day-rubbish.com/blog/logicaldoc-automation-sandbox-bypass-rce) |

**Totals**: 10 advisories · 10 vendors · 5 unauthenticated · 5 authenticated (deep-chain) · 4 system-level (root/SYSTEM/LocalSystem) · all with reproducible PoC.

*Earlier batches: [Batch #1](https://0day-rubbish.com/blog) · [Batch #2](https://0day-rubbish.com/blog) · [Batch #3](https://0day-rubbish.com/blog) · [Batch #4](https://0day-rubbish.com/blog) · [Batch #5](https://0day-rubbish.com/blog) · [Batch #6](https://0day-rubbish.com/blog)*

---

## 🔁 An Ongoing Series — Weekly Disclosures

This is a **continuous disclosure series**. Thanks to continuous optimization, the AI-driven discovery pipeline now produces new 0-day findings at a stable daily rate, and we disclose verified batches on a **weekly cadence**.

* **Latest batch**: Batch 7 — 10 advisories (live); cumulative 68 across 7 batches
* **Next drop**: weekly
* **Future scope**: expanding beyond enterprise IT into **ICS / SCADA, energy, and aerospace** systems

If you want to catch the next drop the moment it lands:

[![Star](https://img.shields.io/badge/%E2%AD%90_Star-bookmark_this_repo-yellow)](https://github.com/Exploit-Garbage/0day-Rubbish) [![Watch](https://img.shields.io/badge/%F0%9F%91%81_Watch-get_notified_on_new_batches-blue)](https://github.com/Exploit-Garbage/0day-Rubbish/subscription) [![Blog](https://img.shields.i...