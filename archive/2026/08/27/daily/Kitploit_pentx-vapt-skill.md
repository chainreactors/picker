---
title: pentx-vapt-skill
url: https://kitploit.com/en/tools/github/yashas-13/pentx-vapt-skill
source: Kitploit
date: 2026-08-27
fetch_date: 2026-08-28T13:36:44.743280
---

# pentx-vapt-skill

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

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/yashas-13/pentx-vapt-skill

![](https://assets.kitploit.com/production/public/tools/53184/f7a7f4d1d94b4de3bbb7339ceea4d0d0783825d81f368204654ed9ae249398f5-display-v1.webp)

[Reconnaissance](/en/categories/reconnaissance)[Vulnerability Scanners](/en/categories/vulnerability-scanners)[Port Scanning](/en/categories/port-scanning)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Exploitation](/en/categories/exploitation)[Information Gathering](/en/categories/information-gathering)[Web Security](/en/categories/web-security)[Penetration Testing](/en/categories/penetration-testing)[Subdomain Enumeration](/en/categories/subdomain-enumeration)

![GitHub](/providers/github.png)yashas-13/pentx-vapt-skill

# pentx-vapt-skill

Open-source AI-powered 5-phase VAPT pentest agent — recon/scan/vuln/exploit/report with PoC

[View Repository](https://github.com/yashas-13/pentx-vapt-skill)

382 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# Pentx — AI-Powered 5-Phase VAPT Agent

**Pentx** is an open-source, AI-powered **Vulnerability Assessment & Penetration Testing** agent that automates the full 5-phase pentest lifecycle with detailed Proof-of-Concept (PoC) for every finding.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue?logo=python)](https://python.org)
![VAPT](https://img.shields.io/badge/phase-5%20full%20lifecycle-orange)

---

## 🎯 Key Features

| Feature | Pentx |
| --- | --- |

|  |  |
| --- | --- |
| **Full 5-phase coverage** | Recon → Scan → Vuln Assessment → Exploitation → Reporting |
| **Mandatory PoC** | Every Confirmed finding stores raw HTTP request/response |
| **Cross-validation** | Findings marked `Confirmed` only when ≥2 tools agree or manual PoC succeeds |
| **Multi-tool accuracy** | nmap, nuclei, httpx, sqlmap, ffuf, nikto, amass, subfinder |
| **Python fallbacks** | Built-in port scanner, dir brute, PoC capture if tools unavailable |
| **Safety-first** | Read-only by default (`--no-exploit`), no destructive payloads |
| **Flexible output** | HTML + Markdown reports, JSON findings, raw PoC artifacts |

---

## 📦 Installation

### Prerequisites

root@kitploit:~

```
# Core tools (any subset works — Pentx adapts)
sudo apt install nmap nuclei httpx sqlmap ffuf nikto amass subfinder
# or on Termux:
pkg install nmap nuclei httpx sqlmap ffuf nikto amass subfinder

# Python dependencies
pip3 install requests beautifulsoup4
```

### From this repository

root@kitploit:~

```
git clone https://github.com/yashas-13/pentx-vapt-skill.git
cd pentx-vapt-skill
```

---

## 🚀 Quick Start

root@kitploit:~

```
# 1. Check which tools are available
python3 scripts/pentx.py --check

# 2. Run a full 5-phase VAPT (read-only, safe)
python3 scripts/pentx.py https://target.example.com ./output --no-exploit

# 3. Full assessment (requires authorization — read Phase 1 prompts)
python3 scripts/pentx.py https://target.example.com ./output

# 4. Run a specific phase only
python3 scripts/pentx.py https://target.example.com ./output --phase 3

# 5. Regenerate report from existing findings
python3 scripts/pentx.py ./output --phase 5
```

### CLI Options

| Flag | Description |
| --- | --- |
| `--check` | Check tool availability and exit |
| `--phase N` | Run only phase N (1-5) |
| `--no-exploit` | Skip Phase 4 (Exploitation) — safe default |
| `--threads N` | Concurrency for scanning (default 5) |
| `--rate-limit N` | Requests per second cap (default 10) |
| `--scope` | Path to JSON file with authorized target list |

---

## 🔧 The 5 Phases

### Phase 1 — Reconnaissance

* Subdomain enumeration (`amass`, `subfinder`)
* Live host probing (`httpx`)
* Tech stack detection
* Quick vulnerability template scan (`nuclei`)
* **Output:** `live.json`, `subdomains.txt`, `assets.txt`

### Phase 2 — Deep Scanning

* Full port scan + service detection (`nmap -sV -sC`)
* NSE vulnerability scripts (`nmap --script vuln`)
* Directory/file fuzzing (`ffuf`)
* Web server misconfiguration scan (`nikto`)
* **Output:** `nmap_full.json`, `ffuf_dirs.json`, `nikto.json`

### Phase 3 — Vulnerability Assessment

* SQL injection detection (`sqlmap`)
* Security header analysis (CSP, HSTS, X-Frame-Options, etc.)
* TLS/SSL weakness detection
* Info disclosure (server version, debug pages, S3 buckets)
* Exposed secrets extraction from JS bundles
* **Output:** `findings.jsonl` (one JSON per finding)

### Phase 4 — Exploitation & Proof-of-Concept

* Safe validation of each finding
* Manual HTTP PoC construction for every finding
* Raw request/response capture
* Severity rating + CVSS scoring
* **Output:** `exploits.jsonl`, `poc-full/*.txt`

### Phase 5 — Reporting

* HTML report with severity tables and PoC details
* Markdown report for documentation
* Executive summary
* Merged findings JSON for integration
* **Output:** `report.html`, `report.md`, `exec-summary.md`, `findings-merged.json`

---

## 📊 Output Structure

root@kitploit:~

```
output/
├── phase1-recon/
│   ├── assets.txt        → All discovered assets
│   ├── live.json         → Live hosts (httpx)
│   └── subdomains.txt    → Subdomain enumeration
├── phase2-scan/
│   ├── nmap_full.json    → Full nmap results
│   ├── ffuf_dirs.json    → Directory fuzzing
│   └── nikto.json        → Nikto findings
├── phase3-vuln/
│   └── findings.jsonl    → Vuln findings (JSONL)
├── phase4-exploit/
│   └── exploits.jsonl    → Confirmed exploits + PoCs
├── report.html           → Full HTML report
├── report.md             → Full Markdown report
├── exec-summary.md       → Executive summary
├── findings-merged.json  → All findings merged
└── poc-full/
    └── poc-*.txt         → Raw PoC artifacts (*.txt)
```

---

## 🔍 Tool Stack

| Tool | Phase | Capability |
| --- | --- | --- |
| `nmap` | 2 | Port/service/vuln + NSE scripts |
| `nuclei` | 1, 3 | 3000+ vulnerability templates |
| `httpx` | 1, 2 | Live probing, tech detection |
| `sqlmap` | 3, 4 | SQLi detection + exploitation |
| `ffuf` | 2 | Directory/file fuzzing |
| `nikto` | 2 | Web server misconfigs |
| `amass` | 1 | Subdomain enumeration |
| `subfinder` | 1 | Subdomain enumeration |

---

## 🛡️ Safety Rules

1. **Authorization required** — Prompts for written scope before Phase 1
2. **Read-only by default** — `--no-exploit` skips Phase 4 entirely
3. **No destructive payloads** — sqlmap uses `--batch --level=2 --risk=1`
4. **Rate limiting** — All fuzzing respects configurable rate limits
5. **Cross-validation** — `Confirmed` only when ≥2 tools agree or PoC succeeds; otherwise `Potential`

> ⚠️ **Only use on systems you own or have explicit written authorization to test.**

---

## 🏗️ Architecture

root@kitploit:~

```
pentx-vapt-skill/
├── SKILL.md                        # pi-agent skill spec
├── README.md                       # This file
├── LICENSE                         # MIT
├── CONTRIBUTING.md                 # Contribution guide
├── assets/
│   └── report_template.md          # Report template
...