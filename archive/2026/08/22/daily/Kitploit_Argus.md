---
title: Argus
url: https://kitploit.com/en/tools/github/dozermx/argus
source: Kitploit
date: 2026-08-22
fetch_date: 2026-08-23T02:57:27.559515
---

# Argus

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

Argus — Multi-phase reconnaissance and attack-surface scanner that maps domains, IPs, ASNs, cloud assets, and CVEs into a knowledge graph with CVSS scoring and compliance mapping. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/dozermx/argus

![](https://assets.kitploit.com/production/public/tools/50608/56f09fb994e748610c8136022231b2ed6ad71fb557e7406a3d19e03453913e72-display-v1.webp)

[Reconnaissance](/en/categories/reconnaissance)[Port Scanning](/en/categories/port-scanning)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Web Application Exploitation](/en/categories/web-application-exploitation)[Information Gathering](/en/categories/information-gathering)[Web Security](/en/categories/web-security)[Fuzzing](/en/categories/fuzzing)[Network Security](/en/categories/network-security)[Penetration Testing](/en/categories/penetration-testing)[Threat Intelligence](/en/categories/threat-intelligence)[Subdomain Enumeration](/en/categories/subdomain-enumeration)[API Security](/en/categories/api-security)

55 months ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

![GitHub](/providers/github.png)dozermx/argus

# Argus

Multi-phase reconnaissance and attack-surface scanner that maps domains, IPs, ASNs, cloud assets, and CVEs into a knowledge graph with CVSS scoring and compliance mapping.

[View Repository](https://github.com/dozermx/argus)

![Argus](https://assets.kitploit.com/production/public/readmes/50608/66a533b6b46e3ea36354e5e584f7ddba6120ad22a3e4b15fe93ad74a8bcc57e5/e38ca77376dcf5be392f930aa9a641b1bc418621e87c1209ded615641b3a96b6-display-v1.webp)

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-AGPL--v3-red?style=flat-square&logo=gnu&logoColor=white)](LICENSE)
[![Version](https://img.shields.io/badge/Version-3.5-blueviolet?style=flat-square)](https://github.com/DozerMx/Argus/releases)
[![Phases](https://img.shields.io/badge/Scan%20Phases-43-darkred?style=flat-square)](https://github.com/DozerMx/Argus)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Termux-222?style=flat-square&logo=linux&logoColor=white)](https://github.com/DozerMx/Argus)
[![Async](https://img.shields.io/badge/Async-aiohttp-009688?style=flat-square)](https://github.com/aio-libs/aiohttp)
[![Graph](https://img.shields.io/badge/Knowledge%20Graph-NetworkX-orange?style=flat-square)](https://networkx.org)
[![No API Keys](https://img.shields.io/badge/API%20Keys-None%20Required-brightgreen?style=flat-square&logo=checkmarx&logoColor=white)](https://github.com/DozerMx/Argus)
[![Web UI](https://img.shields.io/badge/Web%20UI-FastAPI-05998b?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Last Commit](https://img.shields.io/github/last-commit/DozerMx/Argus?style=flat-square&color=555)](https://github.com/DozerMx/Argus/commits/main)
[![Stars](https://img.shields.io/github/stars/DozerMx/Argus?style=flat-square&color=gold)](https://github.com/DozerMx/Argus/stargazers)
[![Repo Size](https://img.shields.io/github/repo-size/DozerMx/Argus?style=flat-square&color=informational)](https://github.com/DozerMx/Argus)

# Argus

**Security Intelligence Framework**

Argus is a multi-phase security reconnaissance and analysis framework built for professional penetration testing and attack surface assessment. It runs fully autonomous — no API keys required, no external services, no accounts. A single command produces a complete picture of an organization's external exposure.

---

## Architecture

root@kitploit:~

```
argus/
├── sources/          Certificate Transparency, passive DNS, brute force
├── correlators/      DNS resolution, CDN bypass, port scanning
├── intelligence/     43 analysis modules
│   ├── Core          TLS, HTTP, email, content discovery, JS secrets
│   ├── Graph         Attack paths, compliance, CVE, anomaly detection
│   ├── Advanced      SSRF chains, OAuth/GraphQL/WebSocket, BGP, stealth
│   └── Intelligence  Deep CVE, API enumeration, cloud storage, threat intel
├── ontology/         Knowledge graph (NetworkX), entity model, pivot engine
├── output/           HTML report, executive report, CSV, JSON, terminal
└── web/              FastAPI real-time dashboard with WebSocket
```

The engine builds a **Knowledge Graph** of all discovered entities — domains, IPs, certificates, organizations, technologies, open ports — and the relationships between them. Every finding is an anomaly attached to a graph node with a CVSS 3.1 score, attack path linkage, and compliance mapping.

---

## 43 Phases

---

## Installation

**Requirements:** Python 3.9+, Linux/macOS/Termux

root@kitploit:~

```
git clone https://github.com/DozerMx/Argus
cd Argus
pip install -r requirements.txt
```

**Web UI (optional):**

root@kitploit:~

```
pip install fastapi uvicorn websockets
```

---

## Usage

root@kitploit:~

```
python argus.py -d TARGET [OPTIONS]
```

### Basic scans

root@kitploit:~

```
# CT log collection + DNS resolution + anomaly detection
python argus.py -d target.com

# Full 43-phase scan
python argus.py -d target.com --full

# Full scan with executive report
python argus.py -d target.com --full --output executive

# Full scan with authentication and fuzzing
python argus.py -d target.com --full --fuzz --auth

# Scan with known credentials
python argus.py -d target.com --full --auth --user admin --password admin123
```

### Targeted modules

root@kitploit:~

```
# Subdomain brute force + AXFR
python argus.py -d target.com --brute --axfr

# Deep infrastructure: ASN + CDN bypass + ports
python argus.py -d target.com --deep --cdn-bypass --ports

# Stealth scan (paranoid jitter profile)
python argus.py -d target.com --full --stealth-profile paranoid

# Through Tor
python argus.py -d target.com --full --proxy socks5://127.0.0.1:9050
```

### Bulk and continuous

root@kitploit:~

```
# Bulk scan from file
python argus.py -f targets.txt --full --output json

# Continuous monitoring with Slack alerts
python argus.py -d target.com --daemon --webhook https://hooks.slack.com/...

# Web UI dashboard
python argus.py --serve --ui-port 8080
```

---

## Options

root@kitploit:~

```
Target:
  -d DOMAIN             Single target domain
  -f FILE               File with one domain per line

Scan Modules:
  --full                Enable all modules
  --deep                ASN, cloud detection, Wayback, reverse IP
  --brute               Subdomain brute force + permutations
  --axfr                DNS zone transfer
  --cdn-bypass          CDN/WAF origin IP discovery
  --ports               TCP port scan + banner grab (178 ports)
  --jarm                JARM TLS fingerprinting
  --fuzz                Parameter fuzzing (SQLi, XSS, SSRF, IDOR, traversal)
  --auth                Authentication analysis
  --user USER           Username for authenticated scanning
  --password PASS       Password for authenticated scanning

Output:
  --output FORMAT       terminal...