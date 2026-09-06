---
title: ephemora-cell
url: https://kitploit.com/en/tools/github/michaels1011/ephemora-cell
source: Kitploit
date: 2026-09-05
fetch_date: 2026-09-06T06:39:12.898433
---

# ephemora-cell

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

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/michaels1011/ephemora-cell

![](https://assets.kitploit.com/production/public/tools/54135/fa2e7346a82237afd5a91984aa180fbca9181ad28e7709dd85942fe0e1f5d37c-display-v1.webp)

[Container Security](/en/categories/container-security)[Dynamic Analysis (Sandboxing)](/en/categories/dynamic-analysis-sandboxing)[Security Virtualization](/en/categories/security-virtualization)[Cloud Security](/en/categories/cloud-security)[DevSecOps](/en/categories/devsecops)[API Security](/en/categories/api-security)[AI Security](/en/categories/ai-security)

![GitHub](/providers/github.png)michaels1011/ephemora-cell

# ephemora-cell

Capability-based WASM runtime for executing untrusted AI-generated code with enforced CPU, memory, time, I/O, and filesystem limits. Provides sub-millisecond warm execution, signed execution records, and an MCP server for integration.

[View Repository](https://github.com/michaels1011/ephemora-cell)

11272 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

[Website](https://pypi.org/project/ephemora-cell/)

# Ephemora Cell

### The execution layer for untrusted AI-generated code.

Fast, capability-based WASM execution with explicit CPU, memory, time, I/O, and filesystem limits — **sub-millisecond warm execution with signed execution records.**

Built for **AI agents, MCP tools, plugins, code interpreters, and other untrusted workloads.**

[![PyPI](https://img.shields.io/pypi/v/ephemora-cell)](https://pypi.org/project/ephemora-cell/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache--2.0-green)](https://opensource.org/licenses/Apache-2.0)
[![Status](https://img.shields.io/badge/status-beta-yellow)](https://github.com/MichaelS1011/ephemora-cell)

![AI Agent → Ephemora Cell enforcement stack → bounded result](https://raw.githubusercontent.com/michaels1011/ephemora-cell/main/assets/hero-light.svg)

## The problem

AI agents increasingly need to write and execute code, call tools, and run plugins. The question that decides whether that is safe:

**How do you let an agent execute untrusted code without giving that code access to your host, your credentials, your network, or unlimited compute?**

root@kitploit:~

```
AI Agent ──▶ Tool / MCP ──▶ Ephemora Cell ──▶ WASM ──▶ bounded result
```

**Ephemora Cell** is a small, capability-based WASM execution runtime for exactly that job: an execution primitive — not an agent framework — that sits underneath your existing agent stack, MCP server, plugin system, or application.

## Quick Start

root@kitploit:~

```
pip install ephemora-cell

# Run your first isolated module (grab the repo's examples, or bring any .wasm):
git clone https://github.com/MichaelS1011/ephemora-cell.git
ephemora-cell run ephemora-cell/examples/hello.wasm
```

root@kitploit:~

```
Hello from Ephemora Cell!
```

root@kitploit:~

```
from ephemora_cell import run_wasm

result = run_wasm("my_module.wasm")
print(result.stdout)          # captured output (10 KB cap)
print(result.status.name)     # SUCCESS
print(result.elapsed_ms)      # wall time
print(result.fuel_consumed)   # compute actually used
```

![Ephemora Cell demo — install, run, JSON report, attack blocked](https://assets.kitploit.com/production/public/readmes/54135/fa2e7346a82237afd5a91984aa180fbca9181ad28e7709dd85942fe0e1f5d37c/d6863d35eeac09392c47869a2401705ca6aaf50d7ccf842879d3096ae242616d-display-v1.webp)

*Real CLI session: install, first run, machine-readable `--json` report with the security baseline, and an attack module (`exploit.wasm`) blocked at the WASI import layer. Verify every frame: the commands run as shown from a clone.*

![Same attack, different boundary — 8 attack primitives allowed in a stock Docker container, all 8 blocked by Ephemora Cell](https://assets.kitploit.com/production/public/readmes/54135/e46a87166a24b584abf7c2a7339e032e1a95df3744e74c0a3dfce6ef1e900322/888cbb7cb17352ec3463a4d0437a1b652e8d790b088aa7cdd783eaa212969472-display-v1.webp)

*Same eight attack primitives, measured live in one run (2026-09-02): a stock `python:3.12-slim` container lets every one through (0/8 blocked), the Ephemora Cell boundary blocks all eight (8/8). Reproduce both columns:*

root@kitploit:~

```
python3 assets/demo_attack_probe.py    # left column  -> 0/8 blocked (stock Docker)
python  benchmarks/verify_8_vectors.py # right column -> 8/8 blocked (Ephemora Cell)
```

## Why this matters

Agent-generated code is different from application code: it can be buggy, computationally unbounded, unexpectedly expensive — or hostile. The runtime must **enforce** boundaries, not document them. Every Cell run does:

* **Enforced, not promised** — fuel metering (CPU), memory caps, epoch-based wall-clock timeouts, output caps and I/O budgets are enforced per execution; the effective posture is attested in a signed execution record.
* **Measured isolation advantage** — of the attack vectors that succeed against a stock Docker container (shell, fork, socket, host filesystem, symlink escape, …), all 8 are blocked here (live-verified, script in the repo).
* **Sub-millisecond warm execution** — 0.16 ms guest / 0.46 ms end-to-end (pooled, measured) makes sandboxing every call affordable instead of exceptional.

## What is enforced

Every execution runs under explicit limits — no opt-in security:

Additional controls: **I/O budgets** (`io_cpu_seconds=2.0` / `io_budget_bytes=64 MiB` — walls for host work, not just guest compute), **dual-ABI** (WASI Preview1 + WASI 0.2 components, opt-in), **memory64 opt-in**, **GC-heap declared cap** (recorded in the security baseline; fuel remains the effective bound), **named state** (64 entries · 256 KiB · 1 MiB per session), and an **egress sidecar** reference mediator (allowlist-validated host-side API calls — [docs/egress\_patterns.md](https://github.com/michaels1011/ephemora-cell/blob/main/docs/egress_patterns.md)).

## Security

The guest receives only the capabilities explicitly made available to it. Live verification of eight attack classes ([`benchmarks/verify_8_vectors.py`](https://github.com/michaels1011/ephemora-cell/blob/main/benchmarks/verify_8_vectors.py)):

**Result: 8/8 attack vectors blocked (live-verified); Docker baselines are measured live per run — never hardcoded.**

This is an execution boundary, not a claim that guest software is trustworthy. Cell does not evaluate whether a module is malicious or correct — a guest can still misbehave *within* the budgets it was given. Execution paths differ materially: the default runs the guest inside your process; `run_isolated()` adds OS-level walls (rlimits, disk quota, I/O CPU watchdog, hard kill).

Full details: [SECURITY.md](https://github.com/michaels1011/ephemora-cell/blob/main/SECURITY.md) (policy, execution-path control matrix, known limitations) · [docs/threat-model.md](https://github.com/michaels1011/ephemora-cell/blob/main/docs/threat-model.md) (adversary model, trust boun...