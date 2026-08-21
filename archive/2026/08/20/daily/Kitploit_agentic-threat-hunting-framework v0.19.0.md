---
title: agentic-threat-hunting-framework v0.19.0
url: https://kitploit.com/en/posts/github-nebulock-inc-agentic-threat-hunting-framework-v0190
source: Kitploit
date: 2026-08-20
fetch_date: 2026-08-21T03:03:30.661429
---

# agentic-threat-hunting-framework v0.19.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/10009/e74ce4b3550bef5466ffeb85581e60b7591edbf5874505e3dff4fe701399a690.png)

New releaseAug 20, 2026

# agentic-threat-hunting-framework v0.19.0

ATHF is a framework for agentic threat hunting - building systems that can remember, learn, and act with increasing autonomy.

Share

# Agentic Threat Hunting Framework (ATHF)

![ATHF Logo](https://assets.kitploit.com/production/public/readmes/10009/e74ce4b3550bef5466ffeb85581e60b7591edbf5874505e3dff4fe701399a690.png)

[![PyPI version](https://img.shields.io/pypi/v/agentic-threat-hunting-framework)](https://pypi.org/project/agentic-threat-hunting-framework/)
[![PyPI downloads](https://img.shields.io/pypi/dm/agentic-threat-hunting-framework)](https://pypi.org/project/agentic-threat-hunting-framework/)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Nebulock-Inc/agentic-threat-hunting-framework/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Nebulock-Inc/agentic-threat-hunting-framework?style=social)](https://github.com/Nebulock-Inc/agentic-threat-hunting-framework/stargazers)

**[Quick Start](#-quick-start)** • **[Installation](#installation)** • **[Documentation](#documentation)** • **[Examples](https://github.com/Nebulock-Inc/agentic-threat-hunting-framework/blob/main/SHOWCASE.md)**

*Give your threat hunting program memory and agency.*

The **Agentic Threat Hunting Framework (ATHF)** is the memory and automation layer for your threat hunting program. It gives your hunts structure, persistence, and context - making every past investigation accessible to both humans and AI.

ATHF works with any hunting methodology (PEAK, TaHiTI, or your own process). It's not a replacement; it's the layer that makes your existing process AI-ready.

## What is ATHF?

ATHF provides structure and persistence for threat hunting programs. It's a markdown-based framework that:

* Documents hunts using the LOCK pattern (Learn → Observe → Check → Keep)
* Maintains a searchable repository of past investigations
* Enables AI assistants to reference your environment and previous work
* Works with any SIEM/EDR platform
* **NEW:** Includes AI-powered research and hypothesis generation agents (v0.3.0+)

## The Problem

Most threat hunting programs lose valuable context once a hunt ends. Notes live in Slack or tickets, queries are written once and forgotten, and lessons learned exist only in analysts' heads.

Even AI tools start from zero every time without access to your environment, your data, or your past hunts.

ATHF changes that by giving your hunts structure, persistence, and context.

**Read more:** [docs/why-athf.md](https://github.com/Nebulock-Inc/agentic-threat-hunting-framework/blob/main/docs/why-athf.md)

## The LOCK Pattern

Every threat hunt follows the same basic loop: **Learn → Observe → Check → Keep**.

![The LOCK Pattern](https://assets.kitploit.com/production/public/readmes/10009/b68ee8add5d757c974e4956704c657077c2d553924dc4043b8f2113134141c2c.png)

* **Learn:** Gather context from threat intel, alerts, or anomalies
* **Observe:** Form a hypothesis about adversary behavior
* **Check:** Test hypotheses with targeted queries
* **Keep:** Record findings and lessons learned

**Why LOCK?** It's small enough to use and strict enough for agents to interpret. By capturing every hunt in this format, ATHF makes it possible for AI assistants to recall prior work and suggest refined queries based on past results.

**Read more:** [docs/lock-pattern.md](https://github.com/Nebulock-Inc/agentic-threat-hunting-framework/blob/main/docs/lock-pattern.md)

## The Five Levels of Agentic Hunting

ATHF defines a simple maturity model. Each level builds on the previous one.

**Most teams will live at Levels 1–2. Everything beyond that is optional maturity.**

![The Five Levels](https://assets.kitploit.com/production/public/readmes/10009/8ed29527e992b3cefadbd910ee166f767d084b288552e6ef0e130686c308fe00.png)

| Level | Capability | What You Get |
| --- | --- | --- |
| **0** | Ad-hoc | Hunts exist in Slack, tickets, or analyst notes |
| **1** | Documented | Persistent hunt records using LOCK |
| **2** | Searchable | AI reads and recalls your hunts |
| **3** | Generative | AI executes queries via MCP tools, conducts research |
| **4** | Agentic | Autonomous agents monitor and act, generate hypotheses |

**Level 1:** Operational within a day
**Level 2:** Operational within a week
**Level 3:** 2-4 weeks (optional)
**Level 4:** 1-3 months (optional)

**Read more:** [docs/maturity-model.md](https://github.com/Nebulock-Inc/agentic-threat-hunting-framework/blob/main/docs/maturity-model.md)

## 🚀 Quick Start

### Option 1: Install from PyPI (Recommended)

root@kitploit:~

```
# Install ATHF
pip install agentic-threat-hunting-framework

# Initialize your hunt program
athf init

# NEW: Conduct research before hunting (5-skill methodology)
athf research new --topic "LSASS dumping" --technique T1003.001

# Create your first hunt (link to research)
athf hunt new --technique T1003.001 --title "LSASS Credential Dumping" --research R-0001
```

### Option 2: Install from Source (Development)

root@kitploit:~

```
# Clone and install from source
git clone https://github.com/Nebulock-Inc/agentic-threat-hunting-framework
cd agentic-threat-hunting-framework
pip install -e .

# Initialize and start hunting
athf init
athf hunt new --technique T1003.001
```

### Option 3: Pure Markdown (No Installation)

root@kitploit:~

```
# Clone the repository
git clone https://github.com/Nebulock-Inc/agentic-threat-hunting-framework
cd agentic-threat-hunting-framework

# Copy a template and start documenting
mkdir -p hunts
cp athf/data/templates/HUNT_LOCK.md hunts/H-0001.md

# Customize AGENTS.md with your environment
# Add your SIEM, EDR, and data sources
```

**Choose your AI assistant:** Claude Code, GitHub Copilot, or Cursor - any tool that can read your repository files.

**Full guide:** [docs/getting-started.md](https://github.com/Nebulock-Inc/agentic-threat-hunting-framework/blob/main/docs/getting-started.md)

## 🔧 CLI Commands

ATHF includes a full-featured CLI for managing your hunts. Here's a quick reference:

### Initialize Workspace

root@kitploit:~

```
athf init                           # Interactive setup
athf init --non-interactive         # Use defaults
```

### Research & Hypothesis Generation (NEW in v0.3.0)

root@kitploit:~

```
# Conduct thorough pre-hunt research (15-20 min)
athf research new --topic "LSASS dumping" --technique T1003.001

# Quick research for urgent hunts (5 min)
athf research new --topic "Pass-the-Hash" --depth basic

# Generate AI-powered hypothesis from threat intel
athf agent run hypothesis-generator --threat-intel "APT29 targeting SaaS"

# List research and agents
athf research list
athf agent list
```

### Create Hunts

root@kitploit:~

```
athf hunt new                       # Interactive mode
athf hunt new \
  --technique T1003.001 \
  --title "LSASS Dumping Detection" \
  --platform windows \
  --research R-0001                 # Link to research document
```

### List & Search

root@kitploit:~

```
athf hunt list                      # Show all hunts
athf hunt list --status completed   # Filter by status
athf hunt list --directory test     # Filter by environment (test/production)
athf hunt list --output json        # JSON output
athf hunt search "kerberoasting"    # Full-text search
athf hunt search "credential" --directory production  # Search with directory filter
athf r...