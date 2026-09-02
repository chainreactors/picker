---
title: vet v1.19.0
url: https://kitploit.com/en/posts/github-safedep-vet-v1190
source: Kitploit
date: 2026-09-01
fetch_date: 2026-09-02T06:40:07.758218
---

# vet v1.19.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/9305/c62dfd90aec2dcdc14e1f7254235a639d6cebc3f563c349537760dc6e697eace.png)

New releaseSep 1, 2026

# vet v1.19.0

Protect against malicious open source packages 🤖

Share

[![SafeDep VET - Real-time malicious package detection & software supply chain security](https://raw.githubusercontent.com/safedep/vet/HEAD/docs/assets/vet-banner-light.svg)](https://safedep.io)

[**Quick Start**](#quick-start) •
[**Documentation**](https://docs.safedep.io/) •
[**Community**](#community--support)

[![Go Report Card](https://goreportcard.com/badge/github.com/safedep/vet)](https://goreportcard.com/report/github.com/safedep/vet)
[![License](https://img.shields.io/github/license/safedep/vet)](https://github.com/safedep/vet/blob/main/LICENSE)
[![Release](https://img.shields.io/github/v/release/safedep/vet)](https://github.com/safedep/vet/releases)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/safedep/vet/badge)](https://api.securityscorecards.dev/projects/github.com/safedep/vet)
[![SLSA 3](https://slsa.dev/images/gh-badge-level3.svg)](https://slsa.dev)
[![CodeQL](https://github.com/safedep/vet/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/safedep/vet/actions/workflows/codeql.yml)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/safedep/vet)

---

> [!NOTE]
> `vet` supports special mode for Agent Skills.
> Run `vet scan --agent-skill <owner/repo>` to scan an Agent Skill hosted in a GitHub repository.

## Why vet?

> **70-90% of modern software is open source code** — how do you know it's safe?

Traditional SCA tools drown you in CVE noise. **vet** takes a different approach:

* **Shadow AI discovery** — Discover AI tool usage signals across various tools and configurations
* **Catch malware before it ships** — Zero-day detection through static and dynamic behavioral analysis (requires SafeDep Cloud access)
* **Cut through vulnerability noise** — Analyzes actual code usage to surface only the risks that matter
* **Enforce policy as code** — Express security, license, and quality requirements as [CEL](https://cel.dev/) expressions
* **CI/CD integration** — Zero-config security guardrails in CI/CD

Free for open source. Hosted SaaS available at [SafeDep](https://safedep.io).

## Quick Start

**Install in seconds:**

root@kitploit:~

```
# macOS & Linux
brew install safedep/tap/vet

# Using npm
npm install -g @safedep/vet
```

or download a [pre-built binary](https://github.com/safedep/vet/releases)

**Get started immediately:**

root@kitploit:~

```
# Scan for malware in your dependencies
vet scan -D . --malware-query

# Fail CI on critical vulnerabilities
vet scan -D . --filter 'vulns.critical.exists(p, true)' --filter-fail
```

## Architecture

`vet` follows a pipeline architecture: **readers** ingest package manifests from diverse sources (directories, repositories, container images, SBOMs), **enrichers** augment each package with vulnerability, malware, and scorecard data from SafeDep Cloud, the **CEL policy engine** evaluates security policies against enriched data, and **reporters** produce actionable output in formats like SARIF, JSON, and Markdown.

View architecture diagram

root@kitploit:~

```
graph TB
    subgraph "OSS Ecosystem"
        R1[npm Registry]
        R2[PyPI Registry]
        R3[Maven Central]
        R4[Other Registries]
    end

    subgraph "SafeDep Cloud"
        M[Continuous Monitoring]
        A[Real-time Code Analysis<br/>Malware Detection]
        T[Threat Intelligence DB<br/>Vulnerabilities • Malware • Scorecard]
    end

    subgraph "vet CLI"
        S[Source Repository<br/>Scanner]
        P[CEL Policy Engine]
        O[Reports & Actions<br/>SARIF/JSON/CSV]
    end

    R1 -->|New Packages| M
    R2 -->|New Packages| M
    R3 -->|New Packages| M
    R4 -->|New Packages| M
    M -->|Behavioral Analysis| A
    A -->|Malware Signals| T

    S -->|Query Package Info| T
    T -->|Security Intelligence| S
    S -->|Analysis Results| P
    P -->|Policy Decisions| O

    style M fill:#7CB9E8,stroke:#5A8DB8,color:#1a1a1a
    style A fill:#E8A87C,stroke:#B88A5A,color:#1a1a1a
    style T fill:#7CB9E8,stroke:#5A8DB8,color:#1a1a1a
    style S fill:#90C695,stroke:#6B9870,color:#1a1a1a
    style P fill:#E8C47C,stroke:#B89B5A,color:#1a1a1a
    style O fill:#B8A3D4,stroke:#9478AA,color:#1a1a1a
```

## Key Features

### **Malicious Package Detection**

Real-time protection against malicious packages powered by [SafeDep Cloud](https://docs.safedep.io/cloud/malware-analysis).
Free for open source projects. Detects zero-day malware through active code analysis.

### **Vulnerability Analysis**

Unlike dependency scanners that flood you with noise, `vet` analyzes your **actual code usage** to prioritize real risks.
See [dependency usage evidence](https://docs.safedep.io/vet/guides/dependency-usage-identification) for details.

### **Policy as Code**

Define security policies using CEL expressions to enforce context specific requirements:

root@kitploit:~

```
# Block packages with critical CVEs
vet scan --filter 'vulns.critical.exists(p, true)' --filter-fail

# Enforce license compliance
vet scan --filter 'licenses.contains_license("GPL-3.0")' --filter-fail

# Require minimum OpenSSF Scorecard scores
vet scan --filter 'scorecard.scores.Maintained < 5' --filter-fail
```

### **Multi-Ecosystem Support**

Package managers: **npm**, **PyPI**, **Maven**, **Go**, **Ruby**, **Rust**, **PHP**
Container images: **Docker**, **OCI**
SBOM formats: **CycloneDX**, **SPDX**
Source repositories: **GitHub**, **GitLab**

## Malicious Package Detection

**Real-time protection against malicious packages** by querying SafeDep's threat intelligence
database, continuously populated through static and dynamic behavioral analysis.

### Quick Setup

root@kitploit:~

```
# Query known malicious packages (no API key needed)
vet scan -D . --malware-query
```

> [!NOTE]
> The `--malware` flag is deprecated. Active (on-demand) scanning has been retired in favour of
> querying SafeDep's threat intelligence database. `--malware` now behaves identically to
> `--malware-query` and is retained for backward compatibility.

**Example detections:**

* [MAL-2025-3541: express-cookie-parser](https://safedep.io/malicious-npm-package-express-cookie-parser/)
* [MAL-2025-4339: eslint-config-airbnb-compat](https://safedep.io/digging-into-dynamic-malware-analysis-signals/)
* [MAL-2025-4029: ts-runtime-compat-check](https://safedep.io/digging-into-dynamic-malware-analysis-signals/)

**Key security features:**

* Real-time lookups against SafeDep's known malicious packages database
* Behavioral analysis using static and dynamic analysis (performed continuously in SafeDep Cloud)
* Human-in-the-loop triaging for high-impact findings
* Public [analysis log](https://vetpkg.dev/mal) for transparency

### Advanced Usage

root@kitploit:~

```
# Specialized scans
vet scan --vsx --malware-query                  # VS Code extensions
vet scan -D .github/workflows --malware-query   # GitHub Actions
vet scan --image nats:2.10 --malware-query      # Container images
```

> [!NOTE]
> The `vet inspect malware` command (on-demand analysis of a single package) is deprecated and
> will be removed in a future release. Use `vet scan --malware-query` to check packages against
> SafeDep's known malicious packages database.

## Production Ready Integrations

### GitHub Actions

Zero-config security guardrails in CI/CD:

root@kitploit:~

```
- uses: safedep/vet-action@v1
  with:
    policy: ".github/vet/policy.yml"
```

See [vet-action](https://github.com/saf...