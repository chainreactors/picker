---
title: ThreatLens
url: https://kitploit.com/en/tools/github/abdaullahag/threatlens
source: Kitploit
date: 2026-09-11
fetch_date: 2026-09-12T06:48:02.347760
---

# ThreatLens

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

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/abdaullahag/threatlens

![](https://assets.kitploit.com/production/public/tools/54773/3266cee3883fc8fffb8592ec82f7451aac31050570c88ab283501b942e17365c-display-v1.webp)

[Defensive Tools](/en/categories/defensive-tools)[Indicator of Compromise (IOC) Management](/en/categories/ioc-management)[OSINT (Open Source Intelligence)](/en/categories/osint)[Threat Feeds & Aggregators](/en/categories/threat-feeds-aggregators)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Scripting & Automation](/en/categories/scripting-automation)[Information Gathering](/en/categories/information-gathering)[Threat Intelligence](/en/categories/threat-intelligence)[Incident Response](/en/categories/incident-response)[Log Analysis](/en/categories/log-analysis)

![GitHub](/providers/github.png)abdaullahag/threatlens

81241 day ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

# ThreatLens

Python CLI tool for rapid IOC analysis (IPs, Domains, CVEs) using 6 free Threat Intel APIs. Outputs: Color-coded Excel, JSON, CSV. Uses: VT, Shodan, AbuseIPDB.

[View Repository](https://github.com/abdaullahag/threatlens)

Share

![ThreatLens — Multi-Source Threat Intelligence CLI](https://raw.githubusercontent.com/abdaullahag/threatlens/main/screenshots/banner.svg)

[![Awesome](https://awesome.re/badge.svg)](https://github.com/jivoi/awesome-osint)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![License: PolyForm Noncommercial](https://img.shields.io/badge/license-PolyForm%20Noncommercial-lightgrey.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-60%20passed-brightgreen.svg)](tests/)
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF.svg)](.github/workflows/security.yml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#-contributing)
![Maintained](https://img.shields.io/badge/maintained-yes-success.svg)

**Investigate IPs, domains, hashes, and CVEs across 6 free threat intel APIs — without switching between browser tabs.**

[**Quick Start**](#-quick-start) ·
[**Usage**](#-usage) ·
[**Architecture**](#️-architecture) ·
[**API Keys**](#-api-keys) ·
[**Screenshots**](#-screenshots) ·
[**Contributing**](#-contributing)

🚀 Proudly featured in the official **[Awesome OSINT](https://github.com/jivoi/awesome-osint)** repository.

---

## 📖 Overview

**ThreatLens** is a single command-line tool that unifies threat intelligence lookups across the most trusted free OSINT sources. Instead of pasting an IP into five different websites, ThreatLens queries them all in parallel, normalizes the results, and gives you a clear verdict — in the terminal, or in a polished, color-coded Excel/JSON/CSV report.

Built for SOC analysts, incident responders, threat hunters, and anyone who wants fast, reliable IOC enrichment without leaving the shell.

|  |  |
| --- | --- |
| **Why ThreatLens**   * One command instead of five browser tabs * Auto-extracts IOCs straight out of raw logs * A single failing/rate-limited API never blocks the rest * Works entirely on free API tiers * Local SQLite cache — repeated lookups are instant * Request budget cap prevents runaway API spend | **Not for**   * Real-time/streaming detection pipelines * Paid/enterprise-only intel feeds * Replacing a full SIEM or SOAR platform |

---

## ✨ Features

| Feature | Details |
| --- | --- |
| 🎯 **IOC Types** | IP, Domain, URL, File Hash (MD5 / SHA1 / SHA256), CVE |
| 🔌 **Integrated APIs** | AbuseIPDB, VirusTotal, AlienVault OTX, Shodan, URLScan.io, NVD |
| 📄 **Log Parsing** | Automatically extracts every IOC type from any log or text file |
| 📊 **Reports** | Excel (color-coded), JSON, CSV |
| 💾 **Local Cache** | SQLite cache with configurable TTL — skip re-querying known IOCs |
| 🛡️ **Security** | Redirect blocking, host allow-listing, API-key redaction in logs, spreadsheet-formula neutralisation |
| 🔒 **Lockfile** | `requirements.lock` with SHA-256 hashes for reproducible installs |
| 💻 **CLI Experience** | Rich progress bars, colored tables, and a clean verdict summary |
| 🧩 **Architecture** | Modular enrichers, typed models, strict separation of concerns |
| ✅ **Tested** | 60 unit & integration tests with `pytest`; CI via GitHub Actions |
| ⚡ **Resilient** | One failing API never blocks the others — errors are isolated and logged |

---

## 🚀 Quick Start

root@kitploit:~

```
# 1. Clone & install
git clone https://github.com/AbdaullahAG/threatlens.git
cd threatlens
pip install -r requirements.txt

# 2. Configure your API keys
cp config/keys.env.example config/keys.env
# → edit config/keys.env and fill in your keys

# 3. Run your first scan
python main.py -i 45.33.32.156
```

> 💡 **NVD (CVE lookups) works out of the box with no API key.** Every other API offers a free tier that takes under 2 minutes to sign up for — see [API Keys](#-api-keys) below.

### Reproducible install (with locked dependencies)

root@kitploit:~

```
pip install --require-hashes -r requirements.lock
```

---

## 🧰 Usage

|  |  |
| --- | --- |
| root@kitploit:~   ``` # Investigate a single IP python main.py -i 45.33.32.156 ``` | Basic single-IOC lookup |
| root@kitploit:~   ``` # Investigate multiple IOC types at once python main.py -i 45.33.32.156 -d malware.example.com \   -s d41d8cd98f00b204e9800998ecf8427e -c CVE-2021-44228 ``` | Mix and match IOC types in one run |
| root@kitploit:~   ``` # Parse a log file — all IOCs auto-extracted python main.py --file /var/log/apache2/access.log ``` | Bulk investigate straight from raw logs |
| root@kitploit:~   ``` # Output JSON instead of Excel python main.py -i 8.8.8.8 --format json ``` | Machine-readable output for pipelines |
| root@kitploit:~   ``` # Use only specific APIs python main.py -i 8.8.8.8 --apis abuseipdb virustotal ``` | Restrict enrichment to selected sources |
| root@kitploit:~   ``` # Generate every report format at once python main.py --file access.log --format all ``` | Excel + JSON + CSV in a single run |
| root@kitploit:~   ``` # Lookup a CVE — no API key needed python main.py -c CVE-2021-44228 --apis nvd --format json ``` | CVE enrichment via NIST NVD (free, no key) |
| root@kitploit:~   ``` # Verbose / debug mode python main.py -i 8.8.8.8 -v ``` | Full request/response logging for troubleshooting |

**See all CLI flags**

| Flag | Description |
| --- | --- |
| `-i, --ip` | IP address(es) to investigate |
| `-d, --domain` | Domain(s) to investigate |
| `-s, --hash` | File hash(es) — MD5 / SHA1 / SHA256 |
| `-c, --cve` | CVE ID(s), e.g. `CVE-2021-44228` |
| `--file` | Path to a log/text file to auto-extract IOCs from |
| `--apis` | Restrict enrichment to a specific set of APIs |
| `--format` | Output format: `excel` (default) | `json` | `csv` | `all` |
| `--output` | Directory to save reports (default: `./output`) |
| `--no-report` | Print results to terminal only, skip saving a file |
| `--cache-path` | SQLite path for local cache (default: `.threatlens/investigations.db`) |
| `--cache-ttl` | Cache lifetime i...