---
title: openshield
url: https://kitploit.com/en/tools/github/owasp/openshield
source: Kitploit
date: 2026-09-10
fetch_date: 2026-09-11T06:51:43.926030
---

# openshield

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

openshield — Open source CSPM for Azure - scan for misconfigurations and quantum-unsafe cryptography, map findings to CIS/NIST/ISO27001/SOC2, and fix them with one command | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/owasp/openshield

![](https://assets.kitploit.com/production/public/tools/54559/9e42a5fb3059862e052762a64393836472ceeee320e03010b830eec31c172cf5-display-v1.webp)

[Vulnerability Scanners](/en/categories/vulnerability-scanners)[Configuration Auditing](/en/categories/configuration-auditing)[Cryptography](/en/categories/cryptography)[Cloud Security](/en/categories/cloud-security)[DevSecOps](/en/categories/devsecops)[Threat Intelligence](/en/categories/threat-intelligence)[Misconfiguration](/en/categories/misconfiguration)

![GitHub](/providers/github.png)owasp/openshield

# openshield

Open source CSPM for Azure - scan for misconfigurations and quantum-unsafe cryptography, map findings to CIS/NIST/ISO27001/SOC2, and fix them with one command

[View Repository](https://github.com/owasp/openshield)

5668392 days ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

![OpenShield](https://assets.kitploit.com/production/public/readmes/54559/9e42a5fb3059862e052762a64393836472ceeee320e03010b830eec31c172cf5/8aa00e26f28507bfec2150f0b41e2297a5174f24a2683f736a4759f42c4db979-display-v1.webp)

**Open source Cloud Security Posture Management (CSPM) for Azure** detect misconfigurations, map them to CIS / NIST / ISO 27001 / SOC 2, remediate with one command, and identify cryptographic assets requiring quantum-safe migration.

[**Website**](https://openshield-org.github.io/openshield/) · [**Documentation**](https://github.com/owasp/openshield/blob/dev/docs) · [**Roadmap**](https://github.com/owasp/openshield/blob/dev/ROADMAP.md) · [**Changelog**](https://github.com/owasp/openshield/blob/dev/CHANGELOG.md) · [**Security Policy**](https://github.com/owasp/openshield/blob/dev/.github/SECURITY.md) · [**Discord**](https://discord.gg/openshield)

[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/13618/badge)](https://www.bestpractices.dev/projects/13618)
[![OpenShield CI](https://github.com/openshield-org/openshield/actions/workflows/ci.yml/badge.svg)](https://github.com/openshield-org/openshield/actions/workflows/ci.yml)
[![CodeQL](https://github.com/openshield-org/openshield/actions/workflows/codeql.yml/badge.svg)](https://github.com/openshield-org/openshield/actions/workflows/codeql.yml)
[![Deploy](https://github.com/openshield-org/openshield/actions/workflows/deploy.yml/badge.svg?branch=dev)](https://github.com/openshield-org/openshield/actions/workflows/deploy.yml)

[![OWASP](https://img.shields.io/badge/OWASP-listing%20review-orange.svg)](https://owasp.org)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![GitHub Repo stars](https://img.shields.io/github/stars/openshield-org/openshield?style=flat-square)](https://github.com/openshield-org/openshield/stargazers)
[![GitHub contributors](https://img.shields.io/github/contributors/openshield-org/openshield?style=flat-square)](https://github.com/openshield-org/openshield/graphs/contributors)
[![GitHub last commit](https://img.shields.io/github/last-commit/openshield-org/openshield?style=flat-square)](https://github.com/openshield-org/openshield/commits/main)
[![GitHub issues](https://img.shields.io/github/issues/openshield-org/openshield?style=flat-square)](https://github.com/openshield-org/openshield/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289da)](https://discord.gg/openshield)

Release artifacts include SHA-256 checksums, an SBOM, and identity-bound
provenance attestations. See [release verification](https://github.com/owasp/openshield/blob/dev/docs/release-verification.md).

---

## The Problem

Enterprise cloud security tools like **Wiz**, **Prisma Cloud**, and **Microsoft Defender for Cloud** cost **$50,000–$500,000/year**.

Startups, SMEs, universities, and student teams are left with **zero visibility** into their Azure security posture. A misconfigured storage blob, an overprivileged service principal, or an open NSG rule can sit undetected for months.

**OpenShield changes that.**

## Why Post-Quantum Cryptography Matters Now

Adversaries are collecting encrypted Azure traffic today to decrypt it when quantum computers become available. This is called a Harvest Now Decrypt Later attack and it is happening right now.

OpenShield scans Azure for classical cryptographic assets that need migration before it is too late:

* TLS configurations using RSA or ECDH key exchange on App Services
* Key Vault keys using RSA or ECC algorithms vulnerable to Shor's algorithm
* Certificates using classical signature algorithms

Findings map to NIST FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), and FIPS 205 (SLH-DSA) and feed directly into post-quantum migration planning.

---

## What OpenShield Does

| Feature | Description |
| --- | --- |
| **Misconfiguration Scanner** | Runs 95 Azure security rules across storage, network, identity, database, compute, Key Vault, AKS, post-quantum cryptography, backup, serverless, private endpoint, and supply chain posture |
| **Compliance Mapper** | Maps findings to CIS Benchmarks, NIST CSF, ISO 27001, and SOC 2 framework JSON files |
| **Scan History API** | Stores scans and findings in PostgreSQL and exposes findings, score, scan history, compliance posture, drift, and resource inventory over REST |
| **Remediation Playbooks** | Every rule ships with a matching Azure CLI remediation script (95 playbooks) |
| **Security Dashboard** | Full React dashboard deployed on Vercel - live monitoring, findings, compliance, drift, prioritization, and AI-layer views |
| **Project Website** | Documentation and reference site at [openshield-org.github.io/openshield](https://openshield-org.github.io/openshield/) - blog, rules gallery, architecture, evidence guides, roadmap, and releases |
| **Sentinel Integration** | Normalises findings and pushes them into Microsoft Sentinel via a Log Analytics custom table and KQL analytics rules |

---

## Security Assurance

OpenShield has achieved the **OpenSSF Best Practices Passing Badge**, completing 100% of the applicable Passing-level criteria across project governance, change control, reporting, quality, security, and code analysis.

[![OpenSSF Best Practices Passing Badge](https://raw.githubusercontent.com/owasp/openshield/dev/docs/assets/openssf-best-practices.svg)](https://www.bestpractices.dev/projects/13618)

**OpenSSF Best Practices - Passing**

The project's OpenSSF status is publicly verifiable through the official OpenSSF Best Practices project record. OpenShield continues to strengthen its engineering, security assurance, and open source governance practices as it progr...