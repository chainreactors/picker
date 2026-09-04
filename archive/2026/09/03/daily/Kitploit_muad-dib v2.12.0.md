---
title: muad-dib v2.12.0
url: https://kitploit.com/en/posts/github-dnszlsk-muad-dib-v2120
source: Kitploit
date: 2026-09-03
fetch_date: 2026-09-04T06:42:38.478027
---

# muad-dib v2.12.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/10373/11262ac16c0c966925063196945bbca4ac7540a310c5b2a4c792f36bb0de1b58.png)

New releaseSep 3, 2026

# muad-dib v2.12.0

Real-time npm/PyPI supply-chain threat detection. Behavioral chain analysis, AST scanning, IOC feeds, and compound scoring engine.

Share

![MUAD'DIB Logo](https://assets.kitploit.com/production/public/readmes/10373/84132538a800a2879cff088259fe9e98e975a3fe37f8462fe731d6a06f82314a.png)

[![npm version](https://img.shields.io/npm/v/muaddib-scanner)](https://www.npmjs.com/package/muaddib-scanner)
[![CI](https://github.com/DNSZLSK/muad-dib/actions/workflows/scan.yml/badge.svg)](https://github.com/DNSZLSK/muad-dib/actions/workflows/scan.yml)
[![Coverage](https://codecov.io/gh/DNSZLSK/muad-dib/branch/master/graph/badge.svg)](https://codecov.io/gh/DNSZLSK/muad-dib)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/DNSZLSK/muad-dib/badge)](https://scorecard.dev/viewer/?uri=github.com/DNSZLSK/muad-dib)
![License](https://img.shields.io/badge/license-AGPL--3.0--only-blue)
![Node](https://img.shields.io/badge/node-%3E=18-brightgreen)
![IOCs](https://img.shields.io/badge/IOCs-225,000+-red)

[Installation](#installation) |
[Usage](#usage) |
[Features](#features) |
[VS Code](#vs-code) |
[CI/CD](#cicd)

[Version francaise](https://github.com/dnszlsk/muad-dib/blob/master/docs/README.fr.md)

---

## Why MUAD'DIB?

npm and PyPI supply-chain attacks are exploding. Shai-Hulud compromised 25K+ repos in 2025. Existing tools detect threats but don't help you respond.

MUAD'DIB combines **22 parallel scanners** (278 detection rules), a **deobfuscation engine**, **inter-module dataflow analysis**, **compound scoring** (21 compound rules), and a gVisor/Docker sandbox to detect known threats and suspicious behavioral patterns in npm and PyPI packages. An XGBoost classifier exists in the codebase but is **currently inactive** (see [Evaluation](#evaluation)).

---

## Positioning

MUAD'DIB is a free, open, and fully auditable supply-chain scanner for npm and PyPI. It detects **known** threats (225,000+ IOCs), install-time RCE, credential-then-exfiltration flows, obfuscated payloads, and other suspicious behavioral patterns — locally, with no telemetry.

It is licensed under the **AGPL-3.0**; a **commercial license** is available for organizations that need to embed it in a proprietary product or run it as a closed hosted service (see [License](#license)).

It deliberately does not try to do everything — see [Scope](#scope) for exactly what it catches and what it does not.

---

## Scope

**Detects** (npm & PyPI): known-malicious packages (name + SHA256 IOC match), typosquats, install-time RCE (lifecycle `preinstall`/`postinstall`, `curl | sh`, Python import-time, `binding.gyp`), credential read then network exfiltration (intra- and cross-file), obfuscated / high-entropy / stub-loader payloads, binary droppers (`chmod +x` + exec/spawn), and anti-analysis evasion markers.

**Out of scope**: browser-only attacks (DOM/`window`, no Node.js API), the *contents* of native binaries / WASM (no binary analysis), zero-day unknown packages (the IOC feed is reactive), and non-npm/PyPI ecosystems (RubyGems, Maven, Go). Determined anti-sandbox fingerprinting and multi-stage remote payloads are known false-negative risks. Full detail: [Threat Model](https://github.com/dnszlsk/muad-dib/blob/master/docs/threat-model.md).

**No telemetry.** Your code and scan results never leave your machine — MUAD'DIB only *downloads* threat-intel feeds (`muaddib update`) and, for scoring, reads public npm registry metadata. Webhook alerts are opt-in.

---

## Installation

### npm (recommended)

root@kitploit:~

```
npm install -g muaddib-scanner
```

### From source

root@kitploit:~

```
git clone https://github.com/DNSZLSK/muad-dib
cd muad-dib
npm install
npm link
```

---

## Usage

### Basic scan

root@kitploit:~

```
muaddib scan .
muaddib scan /path/to/project
```

Scans both npm (package.json, node\_modules) and Python (requirements.txt, setup.py, pyproject.toml) dependencies.

### Interactive mode

root@kitploit:~

```
muaddib
```

### Safe install

root@kitploit:~

```
muaddib install <package>
muaddib install lodash axios --save-dev
muaddib install suspicious-pkg --force    # Force install despite threats
```

Scans packages for threats BEFORE installing. Blocks known malicious packages.

### Risk score

Each scan displays a 0-100 risk score:

root@kitploit:~

```
[SCORE] 58/100 [***********---------] HIGH
```

### Explain mode

root@kitploit:~

```
muaddib scan . --explain
```

Shows rule ID, MITRE ATT&CK technique, references, and response playbook for each detection.

### Export

root@kitploit:~

```
muaddib scan . --json > results.json     # JSON
muaddib scan . --html report.html        # HTML
muaddib scan . --sarif results.sarif     # SARIF (GitHub Security)
```

### Severity threshold

root@kitploit:~

```
muaddib scan . --fail-on critical  # Fail only on CRITICAL
muaddib scan . --fail-on high      # Fail on HIGH and CRITICAL (default)
```

### Paranoid mode

root@kitploit:~

```
muaddib scan . --paranoid
```

Ultra-strict detection with lower tolerance. Detects any network access, subprocess execution, dynamic code evaluation, and sensitive file access.

### Webhook alerts

root@kitploit:~

```
muaddib scan . --webhook "https://discord.com/api/webhooks/..."
```

Strict filtering (v2.1.2): alerts only for IOC matches, sandbox-confirmed threats, or canary token exfiltration. Priority triage (v2.10.21): P1 (red, IOC/sandbox/canary), P2 (orange, high-score/compounds), P3 (yellow, rest).

### Behavioral anomaly detection (v2.0)

root@kitploit:~

```
muaddib scan . --temporal-full     # All 4 temporal features
muaddib scan . --temporal          # Sudden lifecycle script detection
muaddib scan . --temporal-ast      # AST diff between versions
muaddib scan . --temporal-publish  # Publish frequency anomaly
muaddib scan . --temporal-maintainer # Maintainer change detection
```

Detects supply-chain attacks **before** they appear in IOC databases by analyzing changes between package versions. See [Evaluation Methodology](https://github.com/dnszlsk/muad-dib/blob/master/docs/EVALUATION_METHODOLOGY.md) for details.

### Docker sandbox

root@kitploit:~

```
muaddib sandbox <package-name>
muaddib sandbox <package-name> --strict
```

Dynamic analysis in an isolated Docker container: strace, tcpdump, filesystem diff, canary tokens, CI-aware environment, and monkey-patching preload for time-bomb detection (multi-run at [0h, 72h, 7d] offsets).

### Other commands

root@kitploit:~

```
muaddib watch .                    # Real-time monitoring
muaddib daemon                     # Daemon mode (auto-scan npm install)
muaddib update                     # Update IOCs (fast, ~5s)
muaddib scrape                     # Full IOC refresh (~5min)
muaddib diff HEAD~1                # Compare threats with previous commit
muaddib init-hooks                 # Pre-commit hooks (husky/pre-commit/git)
muaddib scan . --breakdown         # Explainable score decomposition
muaddib replay                     # Ground truth validation (90/94 TPR@3, v2.11.48)
```

---

## Features

### 22 parallel scanners

| Scanner | Detection |
| --- | --- |
| AST Parse (acorn) | eval, Function, credential theft, binary droppers, prototype hooks |
| Pattern Matching | Shell commands, reverse shells, dead man's switch |
| Dataflow Analysis | Credential read + network send (intra-file and cross-file) |
| Obfuscation Detection | JS obfuscation patterns (skip .min.js) |
| Deobfuscation Pre-processing | String concat, charcode,...