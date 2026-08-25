---
title: agent-bom v0.102.0
url: https://kitploit.com/en/posts/github-msaad00-agent-bom-v01020
source: Kitploit
date: 2026-08-24
fetch_date: 2026-08-25T02:59:06.777637
---

# agent-bom v0.102.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/13617/63f5d9fca72080ad3d4e288f4fb99db514c8f2bd8412915e4556b822fbe8fe57.png)

New releaseAug 24, 2026

# agent-bom v0.102.0

Open security scanner and self-hosted control plane for AI, MCP, and cloud. One evidence model — run scans in your environment, centralize findings, govern in your VPC.

Share

![agent-bom](https://raw.githubusercontent.com/msaad00/agent-bom/main/docs/images/logo-light.svg)

[![Build](https://img.shields.io/github/actions/workflow/status/msaad00/agent-bom/ci.yml?branch=main&style=flat&label=Build)](https://github.com/msaad00/agent-bom/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/agent-bom?style=flat&label=PyPI&cacheSeconds=60)](https://pypi.org/project/agent-bom/)
[![Python 3.11 through 3.14](https://img.shields.io/badge/Python-3.11%E2%80%933.14-blue?style=flat)](https://pypi.org/project/agent-bom/)
[![Docker pulls](https://img.shields.io/docker/pulls/agentbom/agent-bom?style=flat&label=Docker%20pulls)](https://hub.docker.com/r/agentbom/agent-bom)
[![Apache-2.0 license](https://img.shields.io/badge/License-Apache%202.0-blue?style=flat)](LICENSE)
[![OpenSSF Scorecard](https://img.shields.io/ossf-scorecard/github.com/msaad00/agent-bom?style=flat&label=OpenSSF%20scorecard)](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)
[![Glama MCP server](https://img.shields.io/badge/MCP-Glama-7c3aed?style=flat)](https://glama.ai/mcp/servers/msaad00/agent-bom)
[![Smithery MCP server](https://img.shields.io/badge/MCP-Smithery-1f6feb?style=flat)](https://smithery.ai/servers/agent-bom/agent-bom)

**Open security scanner and self-hosted control plane for AI, MCP, and cloud infrastructure.**

**15** package ecosystems · **16** compliance surfaces · **77** MCP tools · no account required
[**Quick start**](#quick-start) ·
[Live demo](https://agent-bom-demo-82102570041.us-central1.run.app) ·
[Docs](https://msaad00.github.io/agent-bom/)

## What it is

`agent-bom` scans repositories, images, and cloud accounts, then correlates what
it finds into one Finding + UnifiedGraph model — powering CLI and CI artifacts,
fleet and browser investigations, compliance evidence, and runtime policy. Run
the scanner without an account, or deploy the control plane inside your own
cloud, VPC, cluster, database, identity, and audit boundary.

Graph provenance stays explicit: collected, inferred, static, and runtime
relationships remain distinct, and unavailable evidence is never upgraded to
observed.

**Control-plane architecture**

![Sources, evidence engine, control plane, API, MCP, and operator surfaces in the self-hosted agent-bom architecture](https://raw.githubusercontent.com/msaad00/agent-bom/main/docs/images/architecture-light.svg)

## Who it is for

![Developer, AppSec, platform, GRC, and AI or MCP owner workflows on the shared evidence model](https://raw.githubusercontent.com/msaad00/agent-bom/main/docs/images/persona-value-light.svg)

| Role | Start here | Primary outcome |
| --- | --- | --- |
| Developers | `agent-bom scan .` | Find and explain issues before code leaves the workstation |
| AppSec | `agent-bom scan . -f sarif -o findings.sarif` | Triage reachable findings and enforce CI gates |
| Security engineers | `pip install 'agent-bom[ui]' && agent-bom serve` | Investigate exposure paths, identities, and evidence provenance |
| Platform / SRE | `agent-bom connect aws` | Centralize estate inventory, jobs, and runtime controls |
| GRC / audit | `agent-bom report compliance-narrative scan.json` | Review control mappings and export evidence with explicit gaps |
| Leadership / CISO | `pip install 'agent-bom[ui]' && agent-bom serve` | Review posture, coverage, material risk, and change over time |
| AI / MCP owners | `pip install 'agent-bom[mcp-server]' && agent-bom mcp server` | Inventory tools and apply allow, warn, or block decisions |

AppSec and GRC remain separate workflows: findings and reachability are not
presented as audit certification. See [product boundaries](https://github.com/msaad00/agent-bom/blob/HEAD/docs/PRODUCT_BOUNDARIES.md).

**Product gallery**

The gallery uses deterministic sample data, visibly labeled in the UI. It is
product-state proof, not customer or advisory evidence.

| Overview | Findings |
| --- | --- |
| ![Overview with posture, finding, coverage, and operations summaries](https://assets.kitploit.com/production/public/readmes/13617/8c841fb2362e5e23e5a40779e356b521a7446c2cf199fad9c342bf8e1baf2e29.png) | ![Findings queue with severity, evidence, and next actions](https://assets.kitploit.com/production/public/readmes/13617/8deae0138554b37da694443126013a1909c9797670dec5cb85f96ea6c2e81bf7.png) |

| Investigation | Remediation |
| --- | --- |
| ![Path-first investigation with provenance-aware synthetic graph evidence](https://assets.kitploit.com/production/public/readmes/13617/768f1ba51cf1134b8683e9c00394f32b0620e83fb07e852a91168f6b1d2630f6.png) | ![Compact prioritized remediation workflow](https://assets.kitploit.com/production/public/readmes/13617/c040bd512a8967d9576245bf716cbcbc72d1617b8f42092be131457ffadaf175.png) |

| Cloud and environment lineage | Agent mesh |
| --- | --- |
| ![Scoped environment lineage with interactive graph controls](https://assets.kitploit.com/production/public/readmes/13617/66eac91bfc59e20f1cc5f5ed95651b5ad4d85fd556c7ba2fa9b05489ed361a12.png) | ![Agent and MCP server relationships with labeled edges](https://assets.kitploit.com/production/public/readmes/13617/511a6a5a2a47e6c42dd491c99400e7f12e501a0b033adec00f98036b928fec5d.png) |

[Capture protocol](https://github.com/msaad00/agent-bom/blob/HEAD/docs/CAPTURE.md)

## Quick start

Run against the repository in your current directory:

root@kitploit:~

```
pip install agent-bom
agent-bom scan .
```

The console shows inventory, findings, and reachable impact. Save an artifact
with `agent-bom scan . -f sarif -o findings.sarif`, or follow the
[first-run guide](https://github.com/msaad00/agent-bom/blob/HEAD/docs/FIRST_RUN.md) for exit codes, formats, and CI use.

**Try without a repository**

Use the curated, explicitly synthetic sample when you only want to inspect the
output shape:

root@kitploit:~

```
agent-bom scan --demo --offline
```

The sample intentionally contains blocking findings, so exit status `1` is
expected.

![Synthetic agent-bom console scan showing inventory, findings, and remediation](https://assets.kitploit.com/production/public/readmes/13617/651dfd4ce15f25d02b775b9489b2be7349ba80ef3942add6b0868316cef1715b.gif)

## Self-host

Start the loopback control plane:

root@kitploit:~

```
pip install 'agent-bom[ui]'
agent-bom serve
```

For a shared deployment, use the documented Docker or Helm path and configure
real identity, TLS, PostgreSQL, encryption, and audit keys before exposing it.

| Target | Start here |
| --- | --- |
| Docker Compose | [Platform compose](https://github.com/msaad00/agent-bom/blob/HEAD/deploy/docker-compose.platform.yml) — PostgreSQL, split secrets, migration job |
| Docker Compose (evaluation) | [Pilot compose](https://github.com/msaad00/agent-bom/blob/HEAD/deploy/docker-compose.pilot.yml) — loopback only, SQLite, no auth |
| Helm / Kubernetes | `helm install agent-bom oci://ghcr.io/msaad00/charts/agent-bom --version 0.99.0` |
| EKS | [Terraform module](https://github.com/msaad00/agent-bom/blob/HEAD/deploy/terraform/platform-eks) |
| Snowflake SPCS / Native App | `scripts/deploy/install.sh snowflake-native` · [install guide](https://github.com/msaad00/agent-bom/blob/HEAD/docs/snowflake-native-app/INSTALL.md) |
| Air-gapped | [Image bundle guide](https://github.com/msaad00/agent-bo...