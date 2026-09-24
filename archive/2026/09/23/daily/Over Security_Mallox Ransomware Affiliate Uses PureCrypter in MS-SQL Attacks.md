---
title: Mallox Ransomware Affiliate Uses PureCrypter in MS-SQL Attacks
url: https://www.sekoia.com/blog/mallox-ransomware-affiliate-leverages-purecrypter-in-microsoft-sql-exploitation-campaigns
source: Over Security
date: 2026-09-23
fetch_date: 2026-09-24T07:08:01.201262
---

# Mallox Ransomware Affiliate Uses PureCrypter in MS-SQL Attacks

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

* Solutions
* Platform
* Partners
* Company
* Resources

[en](/blog/mallox-ransomware-affiliate-leverages-purecrypter-in-microsoft-sql-exploitation-campaigns)

[fr](/fr)

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

[en](/blog/mallox-ransomware-affiliate-leverages-purecrypter-in-microsoft-sql-exploitation-campaigns)

[fr](/fr)

Solutions

Tailored cybersecurity built for your specific challenges and industry

By Use Case

[SIEM replacement](/solutions/siem-replacement)[Stack integration](/solutions/cybersecurity-stack-integration)[Continuous threat detection](/solutions/real-time-threat-detection)[Automated incident response](/solutions/automated-incident-response)[Alert fatigue relief](/solutions/reduce-alert-fatigue)

By Vertical

[Healthcare](/solutions/healthcare)[Technology](/solutions/technology)[Energy & Utilities](/solutions/energy-utilities)[Government](/solutions/government)[Manufacturing](/solutions/manufacturing)[MSSP](/solutions/mssp)

Platform

Give your analysts their time back

UNIFIED Platform

[Autonomous SOC Platform](/platform)[Cyber Threat Intelligence](/platform/intelligence)

PLATFORM IntegrationS

[Integrations catalog](/integrations)

Products

[Sekoia Defend

SIEM](/platform/defend)[Sekoia Intelligence

CTI](/platform/intelligence)[Sekoia Reveal

CAASM](/platform/reveal)[Sekoia Elevate

AI SOC agents](/platform/elevate)

See Sekoia in action

Curious about what our platform can do? Take a self-guided tour and explore the features that security teams rely on.

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)

Partners

Join a powerful ecosystem of cyber experts, continuous training, and shared success

Partners

[Our business partners](/our-business-partners)[Why become a partner?](/why-become-a-business-partner)[Partner portal](https://sekoia.introw.io/)

Services

[Training courses](/training-courses)[Sekoia university](https://training.sekoia.com/account/login/)

Join our business partner ecosystem

Grow your business alongside Sekoia. Join a thriving network of partners and unlock new revenue opportunities in cybersecurity.

[Become a partner](/become-a-partner)

Why Sekoia?

Our story, our world-class team, and our latest updates

About us

[About Sekoia](/about)[About TDR team](/about-threat-detection-research-team)[Customer reviews](/our-customers)[Join us](/join-us)

Newsroom

[Newsroom](/newsroom)[Brand kit](https://share.sekoia.com/s/MH3CJ6Q8o5BC6Q6)

Resources

Deepen your cyber knowledge with expert insights, reports, and real-world case studies

Blog

[Blog](/blog)

glossary

[Cyberglossary](/glossary)

Resource center

[Case studies](/resources-category/case-studies)[Solution briefs](/resources-category/solution-briefs)[Webinars](/resources-category/webinars)[Reports](/resources-category/reports)

[View all](/resources)

Stay ahead of cyber threats

Get the latest insights on threat intelligence, SOC best practices and Sekoia product updates delivered straight to your inbox.

[Subscribe](https://go.sekoia.com/Preference-center-EN.html)

[Home](/)[Blog](/blog)

Mallox affiliate leverages PureCrypter in MS-SQL exploitation campaigns

All categories & topics

[Threat Research & Intelligence](/category/threat-research-intelligence)

[Detection Engineering](/category/detection-engineering)

[SOC Insights & Other News](/category/soc-insights-other-news)

[Product News](/category/product-news)

[TDR Team](/category/tdr)

[AI](/category/ai-security)

[Cloud](/category/cloud-security)

[Integrations](/category/integrations)

[Compliance](/category/compliance)

[APT](/category/apt)

[Cybercrime](/category/cybercrime)

[Phishing](/category/phishing)

[Ransomware](/category/ransomware)

Share

Copied !

[Threat Research & Intelligence](/category/threat-research-intelligence)

[TDR Team](/category/tdr)

[Cybercrime](/category/cybercrime)

[Ransomware](/category/ransomware)

By

[TDR Team](/authors/threat-detection-research-team)

By

[Jérémy SCION](/authors/jeremy-scion)

By

[Livia TIBIRNA](/authors/livia-tibirna)

By

[Pierre LE BOURHIS](/authors/pierre-le-bourhis)

May 13, 2024

# Mallox affiliate leverages PureCrypter in MS-SQL exploitation campaigns

Learn about the techniques used by the Mallox ransomware affiliate to compromise an MS-SQL server. Dive into our detailed technical analysis.

![Central microchip with a glowing green padlock icon on a dark circuit board.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aad4efb7b411a234fcf9b5e_blog-mallox-affiliate-img-cover.webp)

## Key takeaways

Sekoia TDR analyses how a Mallox affiliate exploits MS-SQL servers with PureCrypter, and profiles the ransomware's operators and infrastructure.

* Sekoia TDR observed an MS-SQL honeypot compromised by brute force within an hour, then used to deploy Mallox ransomware via PureCrypter.
* Attackers abused MS-SQL features like xp\_cmdshell, CLR assemblies and OLE Automation to run commands and drop payloads.
* PureCrypter is a Malware-as-a-Service loader that hides the Mallox payload in fake multimedia files and evades analysis and Defender.
* Mallox is a RaaS active since 2021, using double and sometimes triple extortion and sparing Russian-speaking regions.
* Sekoia identified affiliates such as Maestro, vampire and hiervos, distinguishing those hitting single servers from those compromising whole networks.

*This report was originally published for our customers on 2 May 2024.*

As part of our critical vulnerabilities monitoring routine, Sekoia’s Threat & Detection Research (TDR) team deploys and supervises honeypots in different locations around the world to identify potential exploitations.

## Introduction

Recently, our team observed an incident involving our MS-SQL (Microsoft SQL) honeypot. It was targeted by an intrusion set **leveraging brute-force tactics,** aiming to deploy the **Mallox** ransomware via **PureCrypter** through several MS-SQL exploitation techniques.

Our investigation of Mallox samples led us to identify two affiliates with distinct modus operandi. The first focuses on exploiting vulnerable assets, while the second aims at broader compromises of information systems on a larger scale.

This blogpost report aims at presenting a comprehensive technical analysis of the techniques used to compromise the MS-SQL server we deployed. Additionally, it delves into the behaviour observed, with a focus on Mallox ransomware and its affiliates. Finally, we offer insights into detection opportunities to mitigate such threats in the future.

## Infection flow

Our MS-SQL honeypot was deployed online on 15 April 2024 8am UTC and monitored throughout the following week. It exposes the MS-SQL port, the authentication is configured as mixed and the *sa* (SQL Administrator) account is associated with a weak password.

### Initial access

The initial access occurred through a brute-force attack targeting the MS-SQL server. As illustrated in the graph below, the attacker primarily targeted the “**sa**” account. The account was compromised at 8.50 am, less than an hour after it went online. We observed approximately 320 attempts per minute during this timeframe.

![A breakdown of the accounts targeted by bruteforce.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5c1a49553afbaf44c08_6a92a2bf8d1115926b203604_6a2a7d6d3ac1f0766e40e04d.webp)

A breakdown of the accounts targeted by bruteforce.

*Figure 1. A breakdown of the accounts targeted by bruteforce*.

All of the attacking IPs addresses belong to AS208091, which is owned by the hosting provider XHost Internet Solution. Despite a successful compromise of the account, the attacker persisted to brute-force throughout the entire observation window.

### Exploitation

The first attempt of exploitation was observed on 15 April 2024, at 2.17 p.m, several hours after the account was compromised. All of the exploitati...