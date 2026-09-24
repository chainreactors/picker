---
title: PikaBot: a Guide to its Deep Secrets and Operations
url: https://www.sekoia.com/blog/pikabot-a-guide-to-its-deep-secrets-and-operations
source: Over Security
date: 2026-09-23
fetch_date: 2026-09-24T07:08:02.206282
---

# PikaBot: a Guide to its Deep Secrets and Operations

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

* Solutions
* Platform
* Partners
* Company
* Resources

[en](/blog/pikabot-a-guide-to-its-deep-secrets-and-operations)

[fr](/fr)

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

[en](/blog/pikabot-a-guide-to-its-deep-secrets-and-operations)

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

PikaBot: a Guide to its Deep Secrets and Operations

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

[Phishing](/category/phishing)

By

[Pierre LE BOURHIS](/authors/pierre-le-bourhis)

By

[Quentin Bourgue](/authors/quentin-bourgue)

By

[TDR Team](/authors/threat-detection-research-team)

June 3, 2024

# PikaBot: a Guide to its Deep Secrets and Operations

This blog post provides an in-depth analysis of PikaBot, focusing on its anti-analysis techniques implemented in the different malware stages.

![Illustration of a yellow robotic creature, pikabot, plugging cables into a server rack](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a6b3f14008e16ede337a036_blog-pikabot-a-guide-to-its-deep-secrets-and-operations-img-cover.webp)

## Key takeaways

Sekoia TDR analyses PikaBot's anti-analysis techniques across its stages and tracks the loader's command-and-control infrastructure.

* PikaBot is a malware loader used by Initial Access Brokers since February 2023 to gain a foothold and drop payloads like Cobalt Strike.
* Successful PikaBot compromises have reportedly led to Black Basta ransomware deployment, making it a serious threat.
* The loader uses a multi-stage design with anti-analysis techniques including junk code, RC4-encrypted stages and SysWhispers2 direct syscalls.
* Sekoia collected more than 360 unique C2 IP addresses between February 2023 and May 2024, tracked via TLS certificates and configs.
* Infrastructure activity aligns closely with TA577's campaigns, which Sekoia assesses as PikaBot's primary and possibly exclusive user.

*Between 27 and 29 May 2024, international law enforcement agencies and partners conducted the* [*Operation Endgame*](https://www.europol.europa.eu/media-press/newsroom/news/largest-ever-operation-against-botnets-hits-dropper-malware-ecosystem) *to disrupt criminal services, notably through taking down key botnet infrastructures, including those of IcedID, SystemBC, PikaBot, SmokeLoader and BumbleBee.*

*The Sekoia TDR team supported the French law enforcement agencies by providing valuable cyber threat intelligence, in particular on PikaBot.*

## Introduction

**PikaBot** is a malware loader, widely distributed since February 2023, that is used by **Initial Access Brokers** (IABs) to establish an initial foothold within a victim’s networks and to distribute additional payloads such as Cobalt Strike and Meterpreter. Furthermore, several sources reported that successful PikaBot compromises led to the deployment of the **Black Basta ransomware**[1](https://www.trendmicro.com/en_us/research/24/a/a-look-into-pikabot-spam-wave-campaign.html)[2](https://www.microsoft.com/en-us/security/blog/2023/12/28/financially-motivated-threat-actors-misusing-app-installer/).

Technical analysis shared in open source revealed close ties between PikaBot and other infamous malware families, suggesting possible affiliation between their developers and operators. Specifically, **PikaBot** shares code similarities with **Matanbuchus** regarding traffic and string encryption, while its TLS certificate pattern for Command & Control (C2) infrastructure is similar to the Qakbot one.

Since its emergence in early 2023, PikaBot appears to be in active development, with a new major version released in February 2024. The malware employs advanced anti-analysis techniques to evade detection and harden analysis, including system checks, indirect syscalls, encryption of next-stage and strings, and dynamic API resolution. The Sekoia Threat Detection & Research (TDR) team also identified multiple changes in the PikaBot C2 infrastructure throughout 2023.

This article provides an in-depth analysis of PikaBot, focusing on its anti-analysis techniques implemented in the different malware stages. Additionally, this report shares technical details on PikaBot C2 infrastructure.

## Context

### Emergence of PikaBot

In February 2023, PikaBot was first observed being distributed through a thread-hijacking phishing campaign by the IAB group TA577[3](https://twitter.com/Unit42_Intel/status/1623349272061136900). The infection chain involved a OneNote file attached to a thread-hijacked email, which ran a CMD script to download and execute a PikaBot ...