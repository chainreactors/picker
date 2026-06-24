---
title: Fortibleed: Anatomy of the FortiBleed campaign based on the server that the attackers themselves left exposed.
url: https://zenox.ai/en/fortibleed-anatomy-of-the-fortibleed-campaign-based-on-the-server-that-the-attackers-themselves-left-exposed/
source: Over Security
date: 2026-06-23
fetch_date: 2026-06-24T06:06:02.548624
---

# Fortibleed: Anatomy of the FortiBleed campaign based on the server that the attackers themselves left exposed.

![Page Loader Image](http://zenox.ai/wp-content/uploads/2024/11/cropped-Asset-23@3x-e1730486489136.png)

* Platform
  + [Vydar Intelligence](https://zenox.ai/en/vydar-platform/)
  + [Tellyu GenAI](https://zenox.ai/en/products/tellyu-genai/)
* Products
  + [Brand Intelligence](https://zenox.ai/en/products/vydar-brand-intelligence/)
  + [Identity Intelligence](https://zenox.ai/en/products/vydar-identity-intelligence/)
  + [Investigation Intelligence](https://zenox.ai/en/products/vydar-investigation-intelligence/)
* Services
  + [Takedown](https://zenox.ai/en/services/takedown/)
  + [Managed Services](https://zenox.ai/en/services/managed-services/)
  + [Cyber Investigations](https://zenox.ai/en/services/cyber-investigation/)
* Company
  + [About Us](https://zenox.ai/en/about/)
  + [ZenoX In The News](https://zenox.ai/en/zenox-in-the-news/)
* [Blog](https://zenox.ai/en/blog/)
* [Resources](https://zenox.ai/en/resources/)
* [Partners](https://zenox.ai/en/partners/)
* [Contacts](https://zenox.ai/en/contacts/)
* [![](data:image/png;base64...)English](#pll_switcher)

Contacts

+55 11 3382-7396

contact@zenox.ai

Call us: +55 11 3382-7396

Email: contact@zenox.ai

Has your company had data leaked? [Discover for free](https://discover.zenox.ai/en/threat-landscape-report)!

[![](https://zenox.ai/wp-content/plugins/polylang-pro/vendor/wpsyntex/polylang/flags/br.png)](https://zenox.ai/pt/)[![](https://zenox.ai/wp-content/plugins/polylang-pro/vendor/wpsyntex/polylang/flags/es.png)](https://zenox.ai/es/)

[![ZenoX – Artificial Intelligence for Cyber Security](http://zenox.ai/wp-content/uploads/2024/11/Asset-23@3x-e1730484963801.png)](https://zenox.ai/en/)

[![ZenoX – Artificial Intelligence for Cyber Security](http://zenox.ai/wp-content/uploads/2024/11/Asset-23@3x-e1730484963801.png)](https://zenox.ai/en/)

* Platform
  + [Vydar Intelligence](https://zenox.ai/en/vydar-platform/)
  + [Tellyu GenAI](https://zenox.ai/en/products/tellyu-genai/)
* Products
  + [Brand Intelligence](https://zenox.ai/en/products/vydar-brand-intelligence/)
  + [Identity Intelligence](https://zenox.ai/en/products/vydar-identity-intelligence/)
  + [Investigation Intelligence](https://zenox.ai/en/products/vydar-investigation-intelligence/)
* Services
  + [Takedown](https://zenox.ai/en/services/takedown/)
  + [Managed Services](https://zenox.ai/en/services/managed-services/)
  + [Cyber Investigations](https://zenox.ai/en/services/cyber-investigation/)
* Company
  + [About Us](https://zenox.ai/en/about/)
  + [ZenoX In The News](https://zenox.ai/en/zenox-in-the-news/)
* [Blog](https://zenox.ai/en/blog/)
* [Resources](https://zenox.ai/en/resources/)
* [Partners](https://zenox.ai/en/partners/)
* [Contacts](https://zenox.ai/en/contacts/)
* [![](data:image/png;base64...)English](#pll_switcher)

![fortibleed](https://zenox.ai/wp-content/uploads/2026/06/fortibleed-1080x638.png "fortibleed")

[June 20, 2026](https://zenox.ai/en/2026/06/20/)

[Emerging Threats](https://zenox.ai/en/category/emerging-threats/)[Research](https://zenox.ai/en/category/research/)[Threat Hunting](https://zenox.ai/en/category/threat-hunting/)

### Fortibleed: Anatomy of the FortiBleed campaign based on the server that the attackers themselves left exposed.

## Executive Summary:

In June 19 2026 we received access to the contents of an internet-exposed directory, left open by the operators themselves of a campaign the press named **FortiBleed**. It was not a victim leak. It was the **attacker command post**: roughly 318 files containing the tooling, scripts, target lists, operational logs, and stolen data of a global-scale credential theft operation against Fortinet FortiGate firewalls.

Throughout this analysis, what emerged was not a group of “hackers” in the classic sense, but rather something closer to an **industrial assembly line**. The operation has four chained stages (mass scanning and traffic capture, credential extraction, offline hash cracking, and movement inside Active Directory), a multi-operator team model with supervision, elastic cracking capacity rented on demand, and, surprisingly, **an autonomous AI-powered pentest agent** built into the arsenal.

This report reconstructs that operation from the evidence we analyzed file by file. The public figures of the campaign (approximately 73,932 firewalls across 194 countries, around 21,632 domains, close to half of all Fortinet devices exposed to the internet) gain, with possession of the server, the how: how the data was captured, how it was cleaned, **how** targets were prioritized by revenue, and how firewall access was converted into domain compromise.

![](https://zenox.ai/wp-content/uploads/2026/06/Design-sem-nome-3-724x1024.png)

## 1. How we got here

**1.1 The discovery of the open directory**

The FortiBleed campaign became public on **June 17, 2026****,** after researcher Volodymyr “Bob” Diachenko located an internet-accessible server tied to the attacking group. Researcher Kevin Beaumont personally validated credentials from the set across multiple organizations and confirmed they were real and active. The detail that makes this case rare is simple: the group **left its own working directory exposed**, with tooling, connection strings, scripts, and data, all accessible without authentication.

It was this set of files that we received for analysis. From here on, we describe what we found upon opening them, in the order in which the findings began to make sense.

**1.2 What we received**

The material is a snapshot of the operational server. The files carry a copy date of June 7, 2026, but the internal timestamps (logs, builds, captures) concentrate the activity between **May 19 and June 7, 2026**. The content is distributed across five layers, which became the roadmap of our investigation:

* 1.Cracking orchestration (Telegram bot, Hashtopolis, hashcat, GPUs).
* 2.FortiGate credential collection and sniffing (web automation, session capture, traffic harvester).
* 3.Data pipeline (cleaning, deduplication, honeypot removal, OSINT and revenue enrichment).
* 4.Post-exploitation and lateral movement (impacket over LDAP, SMB and Kerberos, password spraying, Active Directory auditing).
* 5.Infrastructure (Kali VMs on KVM, multi-operator SSH mesh, a custom web panel, and an offensive AI agent).

**1.3 Scope, objectives and responsible handling**

Our objective is defensive: to understand the tradecraft, extract actionable indicators, and enable victim notification. For that reason, throughout this report, **passwords and individual identifiers have been redacted or aggregated.** The indicators we publish in full are attacker-side (command and control IPs, tokens, vouchers, keys, planted accounts), because they serve the defense.

## 2. What FortiBleed is

**2.1 The public picture**

FortiBleed is a massive credential-compromise campaign against Fortinet FortiGate devices, that is, the firewalls and SSL-VPN concentrators of those organizations. The figures released by the press are striking: approximately 73,932 unique firewall URLs across 194 countries, around 21,632 affected domains, and something close to **half of all Fortinet devices exposed to the internet.**

The volume of activity is also impressive: roughly 1.16 billion credential attempts against **320,777 FortiGate targets**, plus 2.1 billion brute-force attempts against **163,650 Microsoft SQL Server** hosts, which shows the operation went well beyond Fortinet.

Despite the name evoking “Heartbleed,” FortiBleed is not a memory bug nor an isolated vulnerability. It is a credential harvesting operation combined with offline cracking at industrial scale. The press links the context to CVE-2026-24858 (a FortiCloud SAML SSO authentication bypass, with CVSS up to 9.8, disclosed by Fortinet on January 27, 2026), but there is no confirmation that all the collection came from that flaw. What amplified the campaign was the storage of credentials with weak hashing schemes (SHA-256 with salt) in older configurat...