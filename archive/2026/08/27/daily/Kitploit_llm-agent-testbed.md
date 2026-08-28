---
title: llm-agent-testbed
url: https://kitploit.com/en/tools/github/pie-script/llm-agent-testbed
source: Kitploit
date: 2026-08-27
fetch_date: 2026-08-28T13:36:33.662143
---

# llm-agent-testbed

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/pie-script/llm-agent-testbed

![](https://assets.kitploit.com/production/public/tools/53358/f5cbf25830657c83010fd2395b76fa034d62004301f0257afc9924355f04729c-display-v1.webp)

[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Penetration Testing](/en/categories/penetration-testing)[Learning & Education](/en/categories/education)[Red Teaming](/en/categories/red-teaming)[API Security](/en/categories/api-security)[AI Security](/en/categories/ai-security)[Labs & Practice](/en/categories/labs-practice)

![GitHub](/providers/github.png)pie-script/llm-agent-testbed

# llm-agent-testbed

An empirical security testbed evaluating prompt injection, confused-deputy vulnerabilities, and tool-calling defenses in LLM agents.

[View Repository](https://github.com/pie-script/llm-agent-testbed)

91251 day ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# 🛡️ LLM Agent Security Testbed

### *Empirical Vulnerability & Defense Harness for Tool-Calling LLM Agents*

[![Python Version](https://img.shields.io/badge/python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Google GenAI](https://img.shields.io/badge/Google%20GenAI-Gemini%203.6%20Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Package Manager](https://img.shields.io/badge/uv-Fast%20Packaging-DE5FE9?style=for-the-badge&logo=astral&logoColor=white)](https://astral.sh/uv)
[![Security Focus](https://img.shields.io/badge/OWASP-Agentic%20Security-E0234E?style=for-the-badge&logo=owasp&logoColor=white)](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)

**A disciplined security testbed testing whether tool-equipped LLM agents can be manipulated into unauthorized data exfiltration via prompt injection, role-claim social engineering, and confused-deputy attacks.**

[Core Architecture](#-core-architecture) •
[Attack Taxonomy](#-attack-taxonomy) •
[Naive vs Hardened](#-the-two-tool-paradigms) •
[Quickstart](#-quickstart) •
[Roadmap](#-phase-progress)

---

## 🎯 Executive Overview

Modern LLM-powered agents execute privileged actions: querying internal databases, reading file systems, and interacting with backend APIs. Every action is a boundary where an attacker’s prompt can trigger unauthorized execution.

> ⚠️ **Key Architectural Takeaway:**
> **The vulnerability rarely lives inside the LLM weights alone.** It thrives in the trust boundary between the model's intent request and the application backend executing it without validation.

Much like **SQL Injection** stemmed from unparameterized string concatenation rather than the database engine itself, **LLM Confused-Deputy Flaws** occur when application code blindly trusts an agent's tool arguments.

---

## 🏛️ Core Architecture

![Architecture Overview](https://raw.githubusercontent.com/pie-script/llm-agent-testbed/HEAD/diagrams/01-architecture-overview.svg)

root@kitploit:~

```
flowchart TD
    subgraph Adversary["Adversarial Inputs"]
        A1["Direct Override Prompt"]
        A2["Role Authority Claim"]
        A3["Indirect Data Injection"]
        A4["Boundary Bypass Hinting"]
    end

    subgraph AgenticLoop["LLM Agent Runtime (Gemini 3.6 Flash)"]
        LLM["Agent Reasoning Core"]
        FC["Tool Call Declaration: get_user(username)"]
    end

    subgraph DefenseLayer["Evaluation Defense Layers"]
        direction TB
        subgraph Naive["Naive Backend (Insecure)"]
            N1["Zero Validation"]
            N2["Returns ALL fields (inc. Password)"]
            N3["Ignores restricted=True"]
        end

        subgraph Hardened["Hardened Backend (Secure)"]
            H1["Access Control Enforcement"]
            H2["Refuses restricted=True rows"]
            H3["Password Field Stripped by Design"]
        end
    end

    subgraph Evaluation["Inspection & Grading Engine"]
        G1["Tool Output Interception"]
        G2["Target Secret Inspection ('s3cr3t-fake-admin-pw')"]
        G3["Verdict: LEAKED | BLOCKED | UNCLEAR"]
    end

    Adversary --> LLM
    LLM --> FC
    FC -.->|Test Run A| Naive
    FC -.->|Test Run B| Hardened
    Naive --> G1
    Hardened --> G1
    G1 --> G2 --> G3
```

---

## ⚔️ The Two Tool Paradigms

![Naive vs Hardened Flow](https://raw.githubusercontent.com/pie-script/llm-agent-testbed/HEAD/diagrams/02-naive-vs-hardened-flow.svg)

Both tools expose an **identical function signature** to the LLM agent (`get_user(username: str)`). The model cannot determine which tool version it is interacting with.

---

## 🗃️ Attack Taxonomy & Test Suite

The testbed exercises 5 key vulnerability categories defined in attacks.py:

---

## 🔬 Mock Backend & Planted Injection Setup

The environment is backed by pure, deterministic Python dataclasses in `testbed/fake_data.py`:

> 💡 **Why Alice's bio is poisoned:** This models a realistic indirect prompt injection scenario where an attacker doesn't need elevated privileges. They only need to control data a tool retrieves (e.g. public profile bio), waiting for an agent to read it during a routine lookup.

---

## ⚖️ Ground-Truth Inspection & The `"UNCLEAR"` Verdict

Grading free-text LLM responses is fundamentally non-deterministic. A model might hedge, partially disclose information, or decline to call a tool entirely.

Distinguishing **`UNCLEAR`** from **`BLOCKED`** is crucial: it prevents falsely claiming that a tool backend is secure when the attack simply failed to reach the tool layer.

---

## 📊 Data Model & Directory Layout

root@kitploit:~

```
llm-agent-testbed/
├── testbed/
│   ├── __init__.py               # Package initializer
│   ├── attacks.py                # Structured attack checklist (5 categories)
│   ├── display.py                # Formatted terminal display & verdict styling
│   ├── fake_data.py              # Mock backend storage & seeded injection payloads
│   ├── models.py                 # Pure dataclass shapes: FakeUser, AttackAttempt, AttackResult
│   ├── runner.py                 # Multi-turn attack execution engine & grading logic
│   ├── tools_hardened.py         # Hardened implementation with boundary defenses
│   └── tools_naive.py            # Baseline unvalidated lookup implementation
├── diagrams/
│   ├── 01-architecture-overview.svg
│   ├── 02-naive-vs-hardened-flow.svg
│   ├── 03-attack1-direct-override.svg
│   ├── 04-attack2-role-authority.svg
│   ├── 05-attack3-indirect-injection.svg
│   ├── 06-attack4-boundary-bypass.svg
│   ├── 07-attack5-chained-request.svg
│   ├── 08-summary-table.svg
│   └── 09-summary-chart.png
├── .env                          # Local API keys (ignored by git)
├── .gitignore                    # Standard exclusion rules
├── BUILD-JOURNAL.md              # Engineering decision log & architectural evolution
├── LICENSE                       # MIT License
├── NOTES.md                      # Project notes & phase progress tracker...