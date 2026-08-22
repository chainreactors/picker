---
title: Krawl v2.3.0
url: https://kitploit.com/en/posts/github-blessedrebus-krawl-v230
source: Kitploit
date: 2026-08-21
fetch_date: 2026-08-22T02:50:54.219903
---

# Krawl v2.3.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/12879/30a42393851ed51015609282643749e98372b0ac6eee207eb779f8ea070c7f63.png)

New releaseAug 21, 2026

# Krawl v2.3.0

Krawl is a customizable, lightweight, cloud-native web deception server and anti-crawler that creates fake web applications with low-hanging vulnerabilities using realistic, randomly generated decoy data and AI-generated HTML templates.

Share

# Krawl

### ![](https://raw.githubusercontent.com/blessedrebus/krawl/HEAD/img/krawl-svg.svg)

A modern, customizable web honeypot server designed to detect and track malicious activity from attackers and web crawlers through deceptive web pages, fake credentials, and canary tokens.

[![License](https://img.shields.io/github/license/blessedrebus/krawl)](https://github.com/blessedrebus/krawl/blob/main/LICENSE)
[![Release](https://img.shields.io/github/v/release/blessedrebus/krawl)](https://github.com/blessedrebus/krawl/releases)

[![GitHub Container Registry](https://img.shields.io/badge/ghcr.io-krawl-blue)](https://ghcr.io/blessedrebus/krawl)
[![Kubernetes](https://img.shields.io/badge/kubernetes-ready-326CE5?logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![Helm Chart](https://img.shields.io/badge/helm-chart-0F1689?logo=helm&logoColor=white)](https://github.com/BlessedRebuS/Krawl/pkgs/container/krawl-chart)

## Table of Contents

* [Demo](#demo)
* [What is Krawl?](#what-is-krawl)
* [Krawl Dashboard](#krawl-dashboard)
* [Deployment Modes](#deployment-modes)
* [Krawl Banlist](#krawl-banlist)
* [Quickstart](#quickstart)
  + [Docker Run](#docker-run)
  + [Docker Compose](#docker-compose)
  + [Kubernetes](#kubernetes)
  + [Uvicorn (Python)](#uvicorn-python)
* [Configuration](#configuration)
  + [config.yaml](#configuration-via-configyaml)
  + [Environment Variables](#configuration-via-environmental-variables)
* [Ban Malicious IPs](#use-krawl-to-ban-malicious-ips)
* [IP Reputation](#ip-reputation)
* [Running Behind a Reverse Proxy or CDN](#running-behind-a-reverse-proxy-or-cdn)
* [Metrics & Monitoring](#metrics--monitoring)
* [Additional Documentation](#additional-documentation)
* [Deception using AI](#ai-generated-deception-pages)
* [Contributing](#contributing)

## Demo

Tip: crawl the `robots.txt` paths for additional fun

### Krawl URL: <http://demo.krawlme.com>

### View the dashboard <http://demo.krawlme.com/das_dashboard>

## What is Krawl?

**Krawl** is a cloud‑native deception server designed to detect, delay, and analyze malicious attackers, web crawlers and automated scanners.

It creates realistic fake web applications filled with low‑hanging fruit such as admin panels, configuration files, and exposed fake credentials to attract and identify suspicious activity.

![dashboard](https://assets.kitploit.com/production/public/readmes/12879/a01b9a420bd9f26c6837b29c55c0c4f7c415cf155d5b640ecf614cfed4097997.png)

By wasting attacker resources, Krawl helps clearly distinguish malicious behavior from legitimate crawlers.

It features:

* **[AI Generated Deception Pages](https://github.com/blessedrebus/krawl/blob/HEAD/docs/ai_generation.md)**: **Let attackers help generate your fake vulnerable attack surface**
* **Spider Trap Pages**: Infinite random links to waste crawler resources based on the [spidertrap project](https://github.com/adhdproject/spidertrap)
* **Fake Login Pages**: WordPress, phpMyAdmin, admin panels
* **Honeypot Paths**: Advertised in robots.txt to catch scanners
* **Fake Credentials**: Realistic-looking usernames, passwords, API keys
* **[Canary Token](https://github.com/blessedrebus/krawl/blob/HEAD/docs/canary-token.md) Integration**: External alert triggering
* **Random server headers**: Confuse attacks based on server header and version
* **Real-time Dashboard**: Monitor suspicious activity
* **Customizable Wordlists**: Easy JSON-based configuration
* **Random Error Injection**: Mimic real server behavior

You can easily expose Krawl alongside your other services to shield them from web crawlers and malicious users using a reverse proxy. For more details, see the [Reverse Proxy documentation](https://github.com/blessedrebus/krawl/blob/HEAD/docs/reverse-proxy.md).

![use case](https://assets.kitploit.com/production/public/readmes/12879/60f7ddddd201d89a440fbd2b0b3ac08a1d19b9b9a87dc956a02a06c608f1a73d.png)

## Krawl Dashboard

Krawl provides a comprehensive dashboard, accessible at a **random secret path** generated at startup or at a **custom path** configured via `KRAWL_DASHBOARD_SECRET_PATH`. This keeps the dashboard hidden from attackers scanning your honeypot.

The dashboard is organized in six tabs:

* **Overview**: high-level view of attack activity: an interactive map of IP origins, recent suspicious requests, and top IPs, User-Agents, and paths.

![geoip](https://assets.kitploit.com/production/public/readmes/12879/391bf8fda76ed917c8731427a914f2279d9e0cc8bc69034797c355944972f085.png)

* **Attacks**: detailed breakdown of captured credentials, honeypot triggers, and detected attack types (SQLi, XSS, path traversal, etc.) with charts and tables.

![attack_types](https://assets.kitploit.com/production/public/readmes/12879/30a42393851ed51015609282643749e98372b0ac6eee207eb779f8ea070c7f63.png)

* **IP Insight**: in-depth forensic view of a selected IP: geolocation, ISP/ASN info, reputation flags, behavioral timeline, attack type distribution, and full access history.

![ipinsight](https://assets.kitploit.com/production/public/readmes/12879/93a6ddb8e4b69769fadbba30869373248d0f14c2c7c14d008f0143f3e24c5728.png)

Additionally, after authenticating with the dashboard password, two protected tabs become available:

* **Tracked IPs**: maintain a watchlist of IP addresses you want to monitor over time.
* **IP Banlist**: manage IP bans, view detected attackers, and export the banlist in raw or IPTables format.
* **Deception**: manage AI generated pages, export them or import new ones.

For more details, see the [Dashboard documentation](https://github.com/blessedrebus/krawl/blob/HEAD/docs/dashboard.md).

## Deployment Modes

Krawl supports two deployment modes, controlled by the `mode` setting in `config.yaml` or the `KRAWL_MODE` environment variable.

|  | Standalone | Scalable |
| --- | --- | --- |
| **Database** | SQLite (WAL mode) | PostgreSQL |
| **Cache** | In-memory Python dict | Redis (multi-tier TTL) |
| **Replicas** | 1 (single instance) | 1+ (horizontal scaling) |
| **External deps** | None | PostgreSQL + Redis |
| **Best for** | Dev, homelabs, <500k requests | Production, HA, >500k requests |

**Standalone**: ideal for development environments or homelabs with low request counts. Zero additional configuration needed, just run Krawl and it works.

* Single container deployment with no external dependencies
* Lower RAM and resource usage

**Scalable**: designed for production environments or high-traffic honeypots. The Helm chart defaults to this mode.

* Faster, more responsive dashboard thanks to Redis multi-tier caching
* Lower disk I/O with Redis acting as a hot-path cache in front of PostgreSQL
* Horizontal scaling increase the number of Krawl replicas behind a load balancer

For detailed configuration, Docker Compose examples, Kubernetes/Helm setup, and step-by-step migration instructions, see the [Deployment Modes documentation](https://github.com/blessedrebus/krawl/blob/HEAD/docs/deployment-modes.md).

## Krawl Banlist

Krawl maintains a regularly updated [`banlist.txt`](https://github.com/blessedrebus/krawl/blob/HEAD/banlist.txt) of IP addresses from **attackers that triggered its honeypot traps**. The banlist is published weekly and available for download, hel...