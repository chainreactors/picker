---
title: vigolium v0.4.3
url: https://kitploit.com/en/posts/github-vigolium-vigolium-v043
source: Kitploit
date: 2026-08-20
fetch_date: 2026-08-21T03:03:36.382954
---

# vigolium v0.4.3

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/7564/53e0fa8b4720097b76733b441faff865416650f04b180be06ade468314dc2936.png)

New releaseAug 20, 2026

# vigolium v0.4.3

Vigolium - High-fidelity vulnerability scanner fusing agentic AI with native speed, modularity, and precision

Share

![Vigolium](https://assets.kitploit.com/production/public/readmes/7564/13fa005338f3e4aba3cc042d3ee7c70e3f2ffa4fe782c1ba6253896aa6f4eb52.jpg)

**Vigolium - High-fidelity vulnerability scanner fusing agentic AI with native speed, modularity, and precision**

[![](https://img.shields.io/badge/Vigolium-Cloud-0078D4?style=flat&logo=google-cloud&logoColor=ffb86c&labelColor=black&color=black)](https://console.vigolium.com/)
[![](https://img.shields.io/badge/Documentation-0078D4?style=flat&logo=GitBook&logoColor=8be9fd&labelColor=black&color=black)](https://docs.vigolium.com/)
[![](https://img.shields.io/badge/Vigolium-0078D4?style=flat&logo=X&logoColor=f8f8f2&labelColor=black&color=black)](https://twitter.com/Vigolium)
[![](https://img.shields.io/badge/Discord%20Server-0078D4?style=flat&logo=Discord&logoColor=bd93f9&labelColor=black&color=black)](https://discord.gg/aHFypbAu6Y)
[![](https://custom-icon-badges.demolab.com/badge/LinkedIn-black?logo=linkedin-white&logoColor=39ff14)](https://www.linkedin.com/company/vigolium)
[![](https://img.shields.io/npm/v/@vigolium/vigolium.svg?style=flat&logo=npm&logoColor=50fa7b&labelColor=black&color=black)](https://www.linkedin.com/company/vigolium)

---

Vigolium provides two complementary scanning modes:

* **Native Scan** (`vigolium scan`): **Fast, powerful, and flexible.** Deterministic, multi-phase scanning with 317 modules across content discovery, browser/SPA spidering, and active/passive audit, covering injection, access control, file/path, API/protocol, framework-specific, cloud/infra, and out-of-band (OAST) vulnerability classes.
* **Agentic Scan** (`vigolium agent`): **Thoroughly audits your codebase.** AI-driven scanning that autonomously plans attacks, selects modules, generates custom extensions, and triages results, combining [deep source-code audit](https://github.com/vigolium/vigolium-audit) with autonomous and targeted vulnerability scanning.

## Installation

### Quick Install (Recommended)

root@kitploit:~

```
curl -fsSL https://vigolium.com/install.sh | bash
```

### [npm](https://www.npmjs.com/package/%40vigolium/vigolium)

root@kitploit:~

```
npm install -g @vigolium/vigolium
```

Other method like Docker or Build from source

### Docker

root@kitploit:~

```
docker pull j3ssie/vigolium:latest
docker run --rm j3ssie/vigolium:latest scan -h
```

### Build from Source

root@kitploit:~

```
git clone https://github.com/vigolium/vigolium.git
cd vigolium
make build         # build and install to $GOPATH/bin
```

Requires **Go 1.26+** and **bun 1.3.11+**. See [HACKING.md](https://github.com/vigolium/vigolium/blob/HEAD/HACKING.md#build-and-run) for prerequisites and build details.

| UI Dashboard | Traffic Dashboard |
| --- | --- |
| ![Dashboard 1](https://raw.githubusercontent.com/vigolium/docs/main/images/vigolium-main-workbench.png?raw=true) | ![Dashboard 2](https://raw.githubusercontent.com/vigolium/docs/main/images/vigolium-ui-dashboard-2.png?raw=true) |

| Static Reports | Static Reports |
| --- | --- |
| ![Static Report 1](https://raw.githubusercontent.com/vigolium/docs/main/images/vigolium-static-report-1.png?raw=true) | ![Static Report 2](https://raw.githubusercontent.com/vigolium/docs/main/images/vigolium-static-report-2.png?raw=true) |

| Native scan | Agentic Scan |
| --- | --- |
| ![Native scan](https://raw.githubusercontent.com/vigolium/docs/main/images/vigolium-cli-native-scan.png?raw=true) | ![Agentic Scan](https://raw.githubusercontent.com/vigolium/docs/main/images/vigolium-cli-agent-audit-1.png?raw=true) |

## Key Features

### Native Scan

* **323 scanner modules**: 207 active (fuzzing) + 116 passive (pattern matching), covering OWASP Top 10 and beyond
* **Out-of-band testing (OAST)**: blind XSS/SSRF/command injection via interactsh callbacks with automatic payload correlation
* **Value-aware mutation**: classifies parameters by semantic type (integer, UUID, JWT, email) and mutates per intent
* **Multi-phase pipeline**: external harvesting, content discovery (Deparos), browser/SPA spidering (Spitolas), and audit, controlled by strategy presets and scanning profiles
* **Flexible inputs**: URLs, OpenAPI/Swagger, Postman, Burp Suite, cURL, Nuclei JSONL
* **Multi-session authentication**: inline sessions, session files, or full auth configs with login flows, token extraction, and IDOR/BOLA testing
* **JavaScript extensions**: custom modules and hooks via embedded JS engine with session-aware HTTP APIs
* **Scalable & reportable**: concurrent worker pool with per-host rate limiting, hybrid in-memory/disk/Redis queue, and self-contained HTML reports

### Agentic Scan

* **In-process olium runtime**: every agent mode runs on the native Go `pkg/olium` engine: turn-based loop, built-in tool registry, skills support, and pluggable provider drivers (no subprocess SDK pools)
* **Autopilot**: agent autonomously discovers endpoints, runs scans, and triages findings, with optional multi-specialist pipeline and session resume
* **Swarm**: master agent selects modules, generates custom JS attack extensions, runs code audit + SAST, executes scans, and triages results; targeted or full-scope (`--discover`), with `--diff`/`--last-commits` for change-focused runs
* **Source-audit drivers**: `audit`, `piolium`, and the unified `audit` dispatcher run foreground source-code audits sharing one finding schema and DB tagging
* **Query mode**: single-shot prompts for code review, endpoint discovery, and secret detection
* **Pluggable providers**: `openai-compatible` (default), `openai-codex-oauth`, `openai-api-key`, `openai-responses`, `anthropic-api-key`, `anthropic-oauth`, `anthropic-cli`, `anthropic-compatible`, `anthropic-vertex`, `google-vertex`. Same modes exposed over the REST API with SSE streaming and an OpenAI-compatible chat endpoint

## Quick Start: Native Scan

root@kitploit:~

```
# Scan a single target (default: balanced strategy)
vigolium scan -t https://example.com

# Scan with a strategy preset
vigolium scan -t https://example.com --strategy deep

# Scan specific modules only
vigolium scan -t https://example.com -m xss-reflected,sqli-error

# Scan from an OpenAPI spec
vigolium scan -T openapi.yaml -I openapi

# Pipe URLs from stdin
cat urls.txt | vigolium scan

# Run a single phase directly
vigolium run discovery -t https://example.com

# Generate an HTML report
vigolium scan -t https://example.com --only discovery --format html -o report.html
```

See the [architecture overview](https://docs.vigolium.com/architecture/overview) for the full pipeline and the [strategies guide](https://docs.vigolium.com/native-scan/strategies) for strategies, profiles, and pace configuration. For a quick command reference, see [docs.vigolium.com/getting-started/cheat-sheet](https://docs.vigolium.com/getting-started/cheat-sheet).

## Server Mode

root@kitploit:~

```
# Start API server with authentication
vigolium server -k my-secret-key

# Enable transparent HTTP proxy for traffic recording
vigolium server -k my-key --ingest-proxy-port 9003

# Auto-scan ingested traffic
vigolium server -k my-key --scan-on-receive
```

root@kitploit:~

```
# Ingest traffic to a running server
cat urls.txt | vigolium ingest -s http://localhost:9002

# Ingest an OpenAPI spec
vigolium ingest -s http://localhost:9002 -i api.yaml -I openapi
```

See [running the server](https://docs.vigolium.com/server-mode...