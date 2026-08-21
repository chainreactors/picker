---
title: BloodBash
url: https://kitploit.com/en/tools/github/squidsec/bloodbash
source: Kitploit
date: 2026-08-20
fetch_date: 2026-08-21T03:03:16.926083
---

# BloodBash

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

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/squidsec/bloodbash

![](https://assets.kitploit.com/production/public/tools/50513/e6dab1b1c42dfd6243f237c0530af72e21c23c2411545bcdfafd592a06156c77.png)

[Privilege Escalation](/en/categories/privilege-escalation)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Lateral Movement](/en/categories/lateral-movement)[Configuration Auditing](/en/categories/configuration-auditing)[Information Gathering](/en/categories/information-gathering)[Penetration Testing](/en/categories/penetration-testing)[Cloud Security](/en/categories/cloud-security)[Identity & Access Management (IAM)](/en/categories/identity-access-management)[Red Teaming](/en/categories/red-teaming)

![GitHub](/providers/github.png)squidsec/bloodbash

# BloodBash

Offline AD/Entra attack-path analyzer for SharpHound/AzureHound JSON. Surfaces prioritized privilege escalation, credential, and misconfiguration findings without BloodHound or Neo4j.

40649271 day ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

[View Repository](https://github.com/squidsec/bloodbash)

# BloodBash

[![SquidSec logo](https://assets.kitploit.com/production/public/readmes/50513/e6dab1b1c42dfd6243f237c0530af72e21c23c2411545bcdfafd592a06156c77.png)](https://squidoffense.com/)

**A SquidSec Open Source Project**
[SquidOffense.com](https://squidoffense.com/) ·
[GitHub](https://github.com/DotNetRussell/BloodBash)

[![Run Unit Tests](https://github.com/DotNetRussell/BloodBash/actions/workflows/run-tests.yml/badge.svg)](https://github.com/DotNetRussell/BloodBash/actions/workflows/run-tests.yml)
[![Build and Release Binaries](https://github.com/DotNetRussell/BloodBash/actions/workflows/release-binaries.yml/badge.svg)](https://github.com/DotNetRussell/BloodBash/actions/workflows/release-binaries.yml)
[![Latest release](https://img.shields.io/github/v/release/DotNetRussell/BloodBash?label=latest%20build)](https://github.com/DotNetRussell/BloodBash/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**BloodBash** is an open source offline SharpHound **and** AzureHound JSON analyzer, created and managed by **[SquidSec](https://squidoffense.com/)**. It builds a graph, surfaces AD/Entra attack paths and misconfigs, and prints prioritized findings. No Neo4j or BloodHound UI required.

Merges to `main` automatically build **Linux** and **Windows** binaries and publish a GitHub Release (tag `v1.4.2-build.N`).

---

## About SquidSec

BloodBash is built and maintained by **[SquidSec](https://squidoffense.com/)** for the security community - red teamers, pentesters, and defenders who need fast offline AD/Entra analysis without standing up BloodHound infrastructure.

* **Website:** <https://squidoffense.com/>
* **Project:** <https://github.com/DotNetRussell/BloodBash>

---

## Download (no Python required)

Standalone **SquidSec** BloodBash executables - no Python, pip, or venv needed:

| Platform | Latest download |
| --- | --- |
| **Linux x64** | [bloodbash-linux-x64](https://github.com/DotNetRussell/BloodBash/releases/latest/download/bloodbash-linux-x64) |
| **Windows x64** | [bloodbash-windows-x64.exe](https://github.com/DotNetRussell/BloodBash/releases/latest/download/bloodbash-windows-x64.exe) |

* **All releases & version tags:** <https://github.com/DotNetRussell/BloodBash/releases>
* **Latest release page:** <https://github.com/DotNetRussell/BloodBash/releases/latest>

root@kitploit:~

```
# Linux
curl -sL -o bloodbash \
  https://github.com/DotNetRussell/BloodBash/releases/latest/download/bloodbash-linux-x64
chmod +x bloodbash
./bloodbash /path/to/json --all
```

root@kitploit:~

```
# Windows (PowerShell)
Invoke-WebRequest -Uri "https://github.com/DotNetRussell/BloodBash/releases/latest/download/bloodbash-windows-x64.exe" `
  -OutFile bloodbash.exe
.\bloodbash.exe C:\path\to\json --all
```

## Install (Python / source)

root@kitploit:~

```
pipx install git+https://github.com/DotNetRussell/BloodBash
```

Or from a clone:

root@kitploit:~

```
git clone https://github.com/DotNetRussell/BloodBash.git
cd BloodBash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

Dependencies: `networkx`, `rich`, `tqdm`, `pyyaml`.

## Quick start

**Start with these 3** (point at a SharpHound/AzureHound directory or `.zip`):

root@kitploit:~

```
# 1) Day-0 triage - default when you pass only the data path
bloodbash /path/to/json
# same as:
bloodbash /path/to/json --quick-wins

# 2) Just owned a user - outbound compromise dossier
bloodbash ./sharpout --from-user alice --from-user-export

# 3) Full attack analysis (large env: --fast auto on big graphs)
bloodbash /path/to/json --all --fast
# inventory ladders still opt-in:
bloodbash /path/to/json --all --inventory
```

From a source checkout, `python3 BloodBash.py` is equivalent to `bloodbash`.

root@kitploit:~

```
# Binary / pipx
./bloodbash /path/to/json
bloodbash /path/to/json --from-user alice --from-user-export

# Multi-collection merge (low-priv + DA zip, multi-domain forest)
bloodbash ./lowpriv.zip --merge ./da.zip ./child-domain.zip --all --fast
```

Bare directory (no check flags) runs **quick-wins** triage. Use `--all` for full attack-path analysis (not inventory), or `--wizard` for an interactive picker.

Under `--all` and `--quick-wins`, empty detector sections are suppressed so the console stays readable. Selective flags still print green "none found" lines for the checks you asked for.

Sample data: `SampleSharphoundADData/` and `SampleAzurehoundData/`.

root@kitploit:~

```
bloodbash --help            # start-here + cheat sheet
bloodbash --help-advanced   # full flag tables + all examples
```

More recipes: [docs/cookbook.md](https://github.com/squidsec/bloodbash/blob/HEAD/docs/cookbook.md).

## What it finds

Findings are scored and summarized in a **Prioritized Findings** table (high-volume hygiene categories collapse; use `--all-findings` for the full collapsed list). Abuse panels suggest tools/commands per category.

This is an **offline heuristic analyzer** from SquidSec, not a full BloodHound CE replacement. Prefer validating against BloodHound CE on the same zip for path parity.

---

## Example commands

Replace `./sharpout` with your SharpHound/AzureHound directory or zip. Source checkout: use `python3 BloodBash.py` instead of `bloodbash`.

### Basics

root@kitploit:~

```
# Help (tables + examples)
bloodbash --help
bloodbash --help-advanced

# Default = quick wins (high-signal day-0 triage)
bloodbash ./sharpout
bloodbash ./sharpout --quick-wins
bloodbash ./sharpout --quick-wins --domain CORP.LOCAL
bloodbash ./2024-collection.zip --quick-wins

# Interactive picker
bloodbash ./sharpout --wizard

# Full attack analysis (--all auto --fast on large graphs; inventory is separate)
bloodbash ./sharpout --all
bloodbash ./sharpout --all --fast
bloodbash ./2024-collection.zip --all
bloodbash ./sharpout --all --inventory

# Merge multiple collections into one graph
bloodbash ./lowpriv.zip --m...