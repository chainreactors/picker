---
title: monitor v0.39.0
url: https://kitploit.com/en/posts/github-betterdb-inc-monitor-v0390
source: Kitploit
date: 2026-08-21
fetch_date: 2026-08-22T02:51:05.819661
---

# monitor v0.39.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/13512/75122df1ace1587725ca99201e27939b093cbf184aa3beb5ce8b083df649f245.png)

New releaseAug 21, 2026

# monitor v0.39.0

Real-time monitoring and slowlog analysis for Valkey and Redis databases with anomaly detection, ACL auditing, and Prometheus metrics export.

Share

# BetterDB Monitor

[![Docker Pulls](https://img.shields.io/docker/pulls/betterdb/monitor)](https://hub.docker.com/r/betterdb/monitor)
[![Docker Image Version](https://img.shields.io/docker/v/betterdb/monitor?sort=semver&label=docker)](https://hub.docker.com/r/betterdb/monitor/tags)
[![npm](https://img.shields.io/npm/v/@betterdb/monitor?label=npm)](https://www.npmjs.com/package/%40betterdb/monitor)
[![npm downloads](https://img.shields.io/npm/dm/@betterdb/monitor)](https://www.npmjs.com/package/%40betterdb/monitor)
[![API Tests](https://github.com/betterdb-inc/monitor/actions/workflows/api-tests.yml/badge.svg)](https://github.com/betterdb-inc/monitor/actions/workflows/api-tests.yml)
[![License](https://img.shields.io/badge/license-MIT%20+%20Commercial-blue)](LICENSE)
[![Valkey](https://img.shields.io/badge/Valkey-8.x%20native-6a5acd)](https://valkey.io)
[![Redis](https://img.shields.io/badge/Redis-6+%20compatible-d82c20)](https://redis.io)

**The monitoring layer that Valkey deserves.**

BetterDB persists what Valkey throws away - slowlogs, command patterns, client activity, anomaly signals - so you can debug what happened at 3am, not just what's happening now. Built for Valkey 8.x with native support for COMMANDLOG, CLUSTER SLOT-STATS, and per-thread I/O metrics. Redis 6+ compatible for everything else.

[Website](https://betterdb.com) | [Docker Hub](https://hub.docker.com/r/betterdb/monitor) | [npm](https://www.npmjs.com/package/%40betterdb/monitor) | [Documentation](https://docs.betterdb.com) | [Blog](https://betterdb.com/blog)

BetterDB is built by [BetterDB Inc.](https://betterdb.com), a public benefit company operating under the [OCV Open Charter](https://github.com/OpenCoreVentures/ocv-public-benefit-company).

![BetterDB Monitor - Key Analytics with per-type key size distribution histograms](https://assets.kitploit.com/production/public/readmes/13512/f78a0e3d9383f43dc78d6abfa8d2a5b7b55f786ec368452b1927ef7e76571ec9.png)

## Quick Start (Docker)

root@kitploit:~

```
docker run -d --name betterdb -p 3001:3001 betterdb/monitor:latest
```

Point your browser to `http://localhost:3001`. To monitor a specific instance:

root@kitploit:~

```
docker run -d \
  --name betterdb \
  -p 3001:3001 \
  -e DB_HOST=your-valkey-host \
  -e DB_PORT=6379 \
  -e DB_PASSWORD=your-password \
  betterdb/monitor:latest
```

Two image variants are published, both multi-arch (`linux/amd64`, `linux/arm64`):

| Tag | What it is |
| --- | --- |
| `latest`, `X.Y.Z-no-ai` | Default image - every monitoring feature included, without the dependencies for the experimental local-LLM AI Helper |
| `X.Y.Z` | Adds the experimental AI Helper (bring your own Ollama; disabled by default via `AI_ENABLED`) |

See [Docker Production Deployment](#docker-production-deployment) for persistent storage, custom ports, licensing, and air-gapped setups.

## Quick Start (CLI)

Run BetterDB Monitor without Docker:

root@kitploit:~

```
npx @betterdb/monitor
```

On first run, an interactive setup wizard guides you through database connection, storage backend (SQLite, PostgreSQL, or in-memory), and server settings. Configuration is saved to `~/.betterdb/config.json`.

root@kitploit:~

```
npm install -g @betterdb/monitor   # global install
betterdb --setup                   # re-run setup wizard
betterdb --port 8080               # override server port
betterdb --db-host 1.2.3.4         # override database host
betterdb --help                    # all options
```

Requires Node.js >= 20.0.0 and a Valkey or Redis instance to monitor. For SQLite storage, also `npm install -g better-sqlite3`.

## What You Get

### See everything, keep everything

* **Historical analytics** - query slowlogs, command patterns, client activity, and latency across any time range. The data that used to disappear after a log rotation.
* **COMMANDLOG support** - Valkey 8.1+ exclusive. Large requests and large replies, not just the slow ones.
* **MONITOR capture sessions** - record real traffic on demand: live tail, filter, replay, export to JSON/CSV, and cross-reference against connection history.
* **Hot key tracking** - top keys by access frequency with rank movement over time. Key Analytics (Pro, free in early access) adds type, TTL, and size distributions from live sampling.
* **Cluster visibility** - topology graphs, SLOT-STATS heatmaps, per-slot CPU and key distribution.
* **CPU & I/O thread metrics** - per-thread visibility that no Redis tool can provide.
* **Client analytics** - see exactly which service is responsible for what, attributed by client name and pattern.
* **ACL audit trail** - track who accessed what, persisted for compliance and post-incident debugging.

### Understand and act

* **Anomaly detection** (Pro, free in early access) - automatic baseline learning with correlated events and plain-English diagnoses. 20+ detectors, no manual thresholds.
* **Capacity forecasting** - projected time-to-ceiling for memory, ops/sec, CPU, and fragmentation.
* **Webhooks** - HMAC-signed alert deliveries with retries and a full delivery log.
* **Live migration** - move between Redis and Valkey with a three-phase analysis, execution, and validation workflow.

### Built for the AI era

* **Vector search observability** - FT.SEARCH ops/sec and latency with per-index health for [valkey-search](https://github.com/valkey-io/valkey-search) and RediSearch. See [docs/vector-ai](https://github.com/betterdb-inc/monitor/blob/HEAD/docs/vector-ai/README.md).
* **Inference latency** - p50/p95/p99 per index, with SLA breach alerts (Pro, free in early access).
* **Semantic cache intelligence** (Pro, free in early access) - hit-rate health, similarity-threshold recommendations, and an approve/reject proposal workflow. Agent memory observability included.
* **AI traces** - OTLP span waterfalls from your AI application, correlated with the live Valkey state underneath each request.

### Plugs into everything

* **MCP server** - 60 tools for Claude Code, Cursor, or any MCP client via [`@betterdb/mcp`](https://github.com/betterdb-inc/monitor/blob/HEAD/packages/mcp).
* **Prometheus endpoint** - 100+ `betterdb_*` metrics. See [docs/prometheus-metrics.md](https://github.com/betterdb-inc/monitor/blob/HEAD/docs/prometheus-metrics.md).
* **OpenTelemetry** - mirror metrics and events to any OTLP backend.
* **REST API** - everything in the UI is an API call, documented via OpenAPI.

## Access Your Data Your Way

| Interface | Details |
| --- | --- |
| Web UI | `http://localhost:3001` |
| MCP server | `npx @betterdb/mcp` (stdio) - create a token under Settings → MCP Tokens |
| Prometheus | `http://localhost:3001/api/prometheus/metrics` |
| REST API (OpenAPI) | `http://localhost:3001/docs` |
| Health check | `http://localhost:3001/api/health` |

> **Note**: In production builds (Docker, CLI) API routes are served under the `/api` prefix. In local development (`pnpm dev`) there is no prefix - e.g. `http://localhost:3001/health`.

## Supported Databases

| Database | Minimum Version | Supported Features |
| --- | --- | --- |
| **Valkey** | 8.0+ | All features including COMMANDLOG (8.1+) and CLUSTER SLOT-STATS |
| **Redis** | 6+ | All features except the Valkey-exclusive COMMANDLOG and CLUSTER SLOT-STATS |

The backend uses a unified adapter over the wire-compatible `iovalkey` client and ...