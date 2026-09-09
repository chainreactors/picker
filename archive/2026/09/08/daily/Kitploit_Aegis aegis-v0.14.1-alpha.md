---
title: Aegis aegis-v0.14.1-alpha
url: https://kitploit.com/en/posts/github-antropos17-aegis-aegis-v0141-alpha
source: Kitploit
date: 2026-09-08
fetch_date: 2026-09-09T06:54:50.457912
---

# Aegis aegis-v0.14.1-alpha

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/11867/a09521f6803576be415a2b40c76c6c9e8c7c6abe29564a07fd3ee0519d0df482.png)

New releaseSep 8, 2026

# Aegis aegis-v0.14.1-alpha

OS-level monitor for AI agents: observes processes, file access, and network activity on the local machine and attributes each event to an agent instance.

Share

# AEGIS

**Independent, OS-level observability for AI coding agents**

*Watches what AI agents actually do on your machine — processes, files, network — from outside the agents, no hooks required.*

**AEGIS is an independent, OS-level observer for AI agents.** It watches agent processes, file access, and network activity regardless of how the agent was launched or whether it cooperates with monitoring — and it ties every observation to a specific agent *instance*, with the evidence for that attribution stated on the record. Built on a CommonJS JavaScript monitoring engine, with TypeScript in the renderer and the shared types. **Open-source, local, no telemetry** — everything stays on your machine.

[![Release](https://img.shields.io/github/v/release/antropos17/Aegis?include_prereleases&style=flat-square&label=Release)](https://github.com/antropos17/Aegis/releases/latest)
![CI](https://img.shields.io/github/actions/workflow/status/antropos17/Aegis/ci.yml?style=flat-square&label=CI)
[![Monitor-first](https://img.shields.io/badge/Mode-monitor--first-8a2be2?style=flat-square)](#monitor-first)
![MIT License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows%20%C2%B7%20macOS/Linux%20experimental-lightgrey?style=flat-square)

![AEGIS Demo](https://github.com/antropos17/Aegis/releases/download/aegis-v0.10.0-alpha/demo.gif)
Demo recorded at v0.10.0-alpha; some labels have been renamed since.

[Download](#download) ·
[Report Bug](https://github.com/antropos17/Aegis/issues/new?template=01-bug-report.yml) ·
[Feature Request](https://github.com/antropos17/Aegis/issues/new?template=02-feature-request.yml) ·
[Contributing](https://github.com/antropos17/aegis/blob/master/CONTRIBUTING.md)

---

## What AEGIS observes

| Layer | How |
| --- | --- |
| **Processes** | 110 agents (262 process-name signatures), parent-chain resolution, IDE host detection, WSL and IDE-extension discovery |
| **Files** | chokidar watch on sensitive directories (`.ssh`, `.aws`, `.gnupg`, `.env*`, cloud configs) and the registered config paths of known agents; open-handle and Restart-Manager read detection on Windows |
| **Network** | Outbound TCP per agent process, forward-confirmed reverse DNS, and a verdict per endpoint — `allowlisted`, `unknown`, or `flagged`; an unidentified endpoint is never displayed as safe |
| **Behavior** | 73 detection rules across 8 categories (YAML, hot-reloaded), rolling 10-session baselines, anomaly scoring over four axes (network / filesystem / process / baseline) |
| **Local LLMs** | Runtime probes for Ollama and LM Studio, including loaded models; other runtimes such as vLLM and llama.cpp are detected by process signature |

The counted facts above are not hand-maintained: `npm run counts:check` re-derives every documented counter from the tree on each CI run and fails the build when a number in the docs drifts from reality.

## The evidence graph

What separates AEGIS from a process viewer is not the sensors — it is that every event is attached to an agent **instance**, with evidence you can audit:

* **Instance identity.** An agent is keyed as `pid` + OS birth time (`instanceId`), so a recycled PID is a new instance, not a continuation of the old one's history. Identity caching is gated by a witness, and CI runs an injection proof (`npm run verify:gate`, 4 mutants) that goes red if an identity could ever be served from a stale cache.
* **Attribution with stated evidence.** Every audit record carries `pid`, `instanceId`, and an `attribution` object with one of three statuses — confirmed, inferred, or unattributed — backed by a closed registry of evidence codes. When AEGIS does not know which agent touched a file, it says *unattributed*; it never invents an owner.
* **Tamper-evident log.** Audit events are hash-chained JSONL (Event Schema v1) with daily rotation, 30-day retention, and explicit loss markers when the write buffer overflows.
* **Measured, not asserted.** The identity mechanism is benchmarked in-repo: provider birth-time parity was exact for every comparable process in both recorded runs (542/542 and 419/419), and the process-snapshot sidecar costs ~10 ms per scan where the fallback provider costs hundreds to thousands. Per-run tables, environments, and the stated gaps are in [docs/bench/](https://github.com/antropos17/aegis/blob/master/docs/bench).

Evidence: [`src/main/process-identity.js`](https://github.com/antropos17/aegis/blob/master/src/main/process-identity.js) · [`src/main/attribution.js`](https://github.com/antropos17/aegis/blob/master/src/main/attribution.js) · [correctness audit](https://github.com/antropos17/aegis/blob/master/docs/current-state/CORRECTNESS-AUDIT.md) · [bench 2026-08-12](https://github.com/antropos17/aegis/blob/master/docs/bench/generation-v2-2026-08-12.md) · [bench 2026-08-13](https://github.com/antropos17/aegis/blob/master/docs/bench/generation-v2-2026-08-13.md)

## Monitor-first

> **AEGIS is a camera, not a guard.** It **observes and logs** — it does **not** block agents at the OS level today. There are no kernel hooks and no automatic enforcement. Process control (kill / suspend / resume) is **manual and user-invoked** only. Active blocking is on the [roadmap](#roadmap), not in the current release. Use AEGIS for visibility, auditing, and anomaly detection — pair it with sandboxing when you need enforcement.

## How AEGIS differs from in-agent oversight

Most AI-agent oversight tools instrument the agent itself — a Claude Code plugin, an IDE extension, an SDK wrapper. That placement has a structural blind spot: an agent only shows up if it (or its user) installed the hook. A raw `python autogpt.py`, an unwrapped binary, or a tool that simply does not cooperate is invisible to in-agent instrumentation.

AEGIS sits at the OS layer instead: it watches process, file, and network activity from outside the agents, so what it sees does not depend on the agent's cooperation — only on AEGIS's own coverage (see [known limits](#known-limits)). It is not the only tool observing agents locally — [AgentSight](https://github.com/eunomia-bpf/agentsight), for example, observes from the eBPF layer on Linux — and hook-based tools are complementary rather than competing: hooks see intent (prompts, tool calls) inside the agents that opted in, while AEGIS sees effects (processes, files, connections) for whatever runs on the machine, linked to agent instances without requiring cooperation.

## Known limits

A monitor you cannot calibrate is a monitor you cannot trust, so the limits are stated here rather than discovered later. The re-verified findings behind this list, each with an OPEN/CLOSED status, live in the [correctness audit](https://github.com/antropos17/aegis/blob/master/docs/current-state/CORRECTNESS-AUDIT.md); the short version:

* **Coverage is signature- and heuristic-based.** Detection starts from 110 agents (262 process-name signatures) plus heuristics (WSL, IDE extensions, local LLM probes). An agent binary that matches none of these is not detected.
* **Polling has a blind spot.** A process born and dead between scan ticks (~10 s) is never observed; the bench pages state this explicitly. Per-event capture via ETW is on the [roadmap](#roadmap), with a static recon ...