---
title: Watcher v3.5.3
url: https://kitploit.com/en/posts/github-thalesgroup-cert-watcher-v353
source: Kitploit
date: 2026-09-08
fetch_date: 2026-09-09T06:55:05.671730
---

# Watcher v3.5.3

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/6816/14a2ee423b04f57aa0fdb3211cb1bfeb9122f89e0154923a327da2b4befa2d7a.png)

New releaseSep 8, 2026

# Watcher v3.5.3

AI-powered threat intelligence platform for automated CVE/ransomware monitoring, domain surveillance, data leak detection, and incident response with MISP/TheHive integration.

Share

![Watcher Logo](https://assets.kitploit.com/production/public/readmes/6816/e4e489f04c6ba2eb88f27dbbcd3924b06658a7fe314c331215fbe7d20d160654.png)

**AI-Powered Automated Cybersecurity Threat Detection Platform**

[![Install](https://img.shields.io/badge/Install-Guide-informational?style=for-the-badge&logo=docker)](https://thalesgroup-cert.github.io/Watcher/README.html)
[![Documentation](https://img.shields.io/badge/Documentation-Read-informational?style=for-the-badge&logo=readthedocs)](https://thalesgroup-cert.github.io/Watcher/)
[![Stars](https://img.shields.io/github/stars/thalesgroup-cert/Watcher?style=for-the-badge&logo=github)](https://github.com/thalesgroup-cert/Watcher)
[![Closed Issues](https://img.shields.io/github/issues-closed-raw/thalesgroup-cert/Watcher?style=for-the-badge&logo=github)](https://github.com/thalesgroup-cert/Watcher/issues?q=is%3Aissue+is%3Aclosed)
[![License](https://img.shields.io/github/license/thalesgroup-cert/Watcher?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](https://github.com/thalesgroup-cert/watcher/blob/master/LICENSE)
[![Docker Pulls](https://img.shields.io/docker/pulls/felix83000/watcher?style=for-the-badge&logo=docker)](https://hub.docker.com/r/felix83000/watcher/tags)

[![thalesgroup-cert/Watcher | Trendshift](https://trendshift.io/api/badge/repositories/15680)](https://trendshift.io/repositories/15680?utm_source=repository-badge&utm_medium=badge&utm_campaign=badge-repository-15680)
[![thalesgroup-cert/Watcher | Trendshift](https://trendshift.io/api/badge/trendshift/repositories/15680/daily?language=JavaScript)](https://trendshift.io/repositories/15680?utm_source=trendshift-badge&utm_medium=badge&utm_campaign=badge-trendshift-15680)

Watcher is a Django & React JS platform designed to discover and monitor emerging cybersecurity threats with **AI-powered threat intelligence analysis**. It can be deployed on webservers or quickly run via Docker.

## Watcher Capabilities

Watcher empowers your security operations with comprehensive threat detection and monitoring:

* **AI-Driven Threat Intelligence** - Transform raw threat data into actionable intelligence with automated weekly digests of top-5 trending cybersecurity topics, real-time breaking news alerts when threats emerge, on-demand summaries for any security keyword including related CVE and threat actor details.
* **CVE & Ransomware Intelligence** - Continuously fetch, correlate, and surface external threat data: CVEs from [cve.circl.lu](https://cve.circl.lu), ransomware victims and groups from [ransomware.live](https://ransomware.live) and [ransomlook.io](https://ransomlook.io). Define keyword-based Watch Rules to get alerted when specific threats match your organisation's context.
* **Emerging Threat Detection** - Monitor cybersecurity trends via RSS feeds from CERT-FR ([www.cert.ssi.gouv.fr](http://www.cert.ssi.gouv.fr)), CERT-EU ([www.cert.europa.eu](http://www.cert.europa.eu)), US-CERT ([www.us-cert.gov](http://www.us-cert.gov)), Australian Cyber Security Centre ([www.cyber.gov.au](http://www.cyber.gov.au)), and more. Track new vulnerabilities, malware campaigns, and threat advisories as they appear.
* **Legitimate Domain Management** - Centralized approved domains with expiry, repurchase status, registrar info, and contacts. Easily convert monitored malicious domains into legitimate ones. Automated UDRP case tracking.
* **Information Leak Monitoring** - Detect sensitive data exposure across the webs including Pastebin, StackOverflow, GitHub, GitLab, Bitbucket, APKMirror, npm registries, and other platforms. Catch leaked credentials, API keys, and confidential information early.
* **Malicious Domain Surveillance** - Monitor malicious domains for changes in IP addresses, mail/MX records, and web content. Use [TLSH](https://github.com/trendmicro/tlsh) fuzzy hashing to detect modifications. Automatic RDAP/WHOIS checks with registrar and expiry alerts.
* **Suspicious Domain Detection** - Identify potentially malicious domains targeting your organisation via:

  + **Domain Generation Algorithm Detection** using [dnstwist](https://github.com/elceef/dnstwist) to find typosquatting, homograph attacks, and similar domain variants
  + **Certificate Transparency Monitoring** via [certstream](https://github.com/CaliDog/certstream-python) to catch newly registered suspicious domains in real-time

## Additional Features

Extend Watcher's capabilities with powerful integrations and management tools:

* **TheHive Full Synchronization** - Integration with [TheHive](https://thehive-project.org/) featuring automated alert creation, smart case management, IOC enrichment, and ready-to-use Cortex Analyzers & Responders. Detailed configuration are provided in the documentation [here.](https://thalesgroup-cert.github.io/Watcher/README.html#thehive-export)
* **MISP Integration** - Seamlessly export Indicators of Compromise (IOCs) to [MISP](https://www.misp-project.org/) with smart UUID tracking, automatic object creation, and manual attribute updates for collaborative threat intelligence sharing
* **SSO / OpenID Connect** - Federated login via any OIDC provider (Keycloak, Azure AD, etc.) with PKCE and Knox token issuance. Configurable per-instance via `.env`
* **Flexible Authentication** - Support for LDAP, local, and SSO/OIDC authentication systems
* **Connectors Dashboard** - A superuser-only `/connectors` page to view, edit, and test every external integration (SMTP, Slack, Citadel, TheHive, MISP, CyberWatch feeds, and more) from one place, with encrypted credential storage and per-connector health checks.
* **Smart Notifications** - Receive email, Slack, or Citadel alerts for critical findings and threshold violations across all modules including CyberWatch and UDRP decisions
* **Interactive API Documentation** - Auto-generated Swagger UI at `/api/docs/` and OpenAPI 3 schema at `/api/schema/` powered by drf-spectacular
* **Ticketing System Integration** - Automatically feed your ticketing system with security findings
* **Comprehensive Admin Interface** - Manage all aspects of Watcher through Django's powerful admin panel
* **Advanced Access Control** - Granular user permissions and group management for team collaboration
* **Modern UI Experience** - A modern interface with customizable themes, resizable dashboard panels, advanced filtering with saved filter sets, and persistent user preferences

## Involved dependencies

Watcher leverages open source tools and libraries:

* [**Hugging Face Transformers**](https://huggingface.co/docs/transformers) - AI/ML framework powering threat intelligence summarization and entity extraction
* [**google/flan-t5-base**](https://huggingface.co/google/flan-t5-base) - Text-to-text generation model for AI-powered threat summaries
* [**dslim/bert-base-NER**](https://huggingface.co/dslim/bert-base-NER) - Named Entity Recognition for automatic IOC extraction
* [**certstream**](https://github.com/CaliDog/certstream-python) - Certificate Transparency monitoring
* [**dnstwist**](https://github.com/elceef/dnstwist) - Domain name permutation engine
* [**SearxNG**](https://github.com/searxng/searxng) - Privacy-respecting metasearch engine
* [**PyMISP**](https://github.com/MISP/PyMISP) - MISP threat intelligence platform integration
* [**TL...