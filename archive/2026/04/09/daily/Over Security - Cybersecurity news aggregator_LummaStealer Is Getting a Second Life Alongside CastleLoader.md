---
title: LummaStealer Is Getting a Second Life Alongside CastleLoader
url: https://www.bitdefender.com/en-us/blog/labs/lummastealer-second-life-castleloader
source: Over Security - Cybersecurity news aggregator
date: 2026-04-09
fetch_date: 2026-04-10T04:46:56.634100
---

# LummaStealer Is Getting a Second Life Alongside CastleLoader

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Anti-Malware Research](/en-us/blog/labs/tag/antimalware-research "Anti-Malware Research")

18 min read

# LummaStealer Is Getting a Second Life Alongside CastleLoader

[![Bogdan Ionut Lazar](https://blogapp.bitdefender.com/labs/content/images/size/w100/2026/02/bilazar.jpeg "Bogdan Ionut Lazar")](/en-us/blog/labs/author/bogdan-ionut-lazar "Bogdan Ionut Lazar")[![Manuel Dragomir](https://blogapp.bitdefender.com/labs/content/images/size/w100/2026/02/madragomir.jpeg "Manuel Dragomir")](/en-us/blog/labs/author/manuel "Manuel Dragomir")[![Janos Gergo SZELES](https://blogapp.bitdefender.com/labs/content/images/size/w100/2020/11/jszeles.png "Janos Gergo SZELES")](/en-us/blog/labs/author/jszeles "Janos Gergo SZELES")

[Bogdan Ionut Lazar](/en-us/blog/labs/author/bogdan-ionut-lazar "Bogdan Ionut Lazar")[Manuel Dragomir](/en-us/blog/labs/author/manuel "Manuel Dragomir")[Janos Gergo SZELES](/en-us/blog/labs/author/jszeles "Janos Gergo SZELES")

February 11, 2026

  ![LummaStealer Is Getting a Second Life Alongside CastleLoader](https://blogapp.bitdefender.com/labs/content/images/size/w600/2026/02/lumma_castleloader.png "LummaStealer Is Getting a Second Life Alongside CastleLoader")

Bitdefender researchers have discovered a surge in LummaStealer activity, showing how one of the world's most prolific information-stealing malware operations managed to survive despite being almost brought down by law enforcement less than a year ago.

LummaStealer is a highly scalable information-stealing threat with a long history, having operated under a malware-as-a-service model since it appeared on the scene in late 2022.

The threat quickly evolved into one of the most widely deployed infostealers worldwide, supported by a large affiliate ecosystem and a constantly adapting delivery infrastructure.

Despite significant [law-enforcement disruption efforts](https://www.bitdefender.com/en-gb/blog/hotforsecurity/microsoft-takedown-lumma-stealer) in 2025, LummaStealer operations continued, demonstrating resilience by rapidly migrating to new hosting providers and adapting alternative loaders and delivery techniques.

Our analysis shows that LummaStealer infections are primarily driven by social engineering rather than by the exploitation of technical vulnerabilities.

Malware campaigns consistently rely on users unwittingly running infected files, using simple lures such as fake cracked software, fake games or [media downloads](https://www.bitdefender.com/en-us/blog/hotforsecurity/fake-mission-impossible-lumma-stealer-torrent), and abuse of trusted platforms.

Recent campaigns increasingly employ fake CAPTCHA ("[ClickFix](https://www.bitdefender.com/en-us/blog/businessinsights/how-clickfix-cyberattack-technique-works)") techniques, converting normal users' web interactions into direct command execution on victim systems.

At the core of many of these campaigns is CastleLoader, which plays a central role in helping LummaStealer spread through delivery chains. Its modular, in-memory execution model, extensive obfuscation, and flexible command-and-control communication make it well-suited to malware distribution of this scale.

We found some infrastructure overlap between CastleLoader and LummaStealer, which further suggests that both developer teams are coordinating on it or at least share service providers.

## Key Findings

* LummaStealer is back at scale, despite a major 2025 law-enforcement takedown that disrupted thousands of its command-and-control domains. The operation has rapidly rebuilt its infrastructure and continues to spread worldwide.
* Most infections start with social engineering, not hacking. Victims are tricked into running the malware themselves through fake cracked software, fake game or movie downloads, and deceptive "human verification" pages.
* Fake CAPTCHA ("ClickFix") attacks are becoming a preferred entry point, turning routine web interactions into manual command execution by the victim.
* CastleLoader has become a central delivery mechanism, using in-memory execution, heavy obfuscation, and flexible payload deployment to evade detection and distribute LummaStealer.
* A DNS artefact exposes CastleLoader activity. The loader deliberately triggers failed DNS lookups to nonexistent domains, creating a detectable pattern that can be used to identify related campaigns.
* Infrastructure overlap links CastleLoader and LummaStealer operations, suggesting shared services or coordination within a broader malware-as-a-service ecosystem.
* The privacy impact is severe and long-lasting. Stolen credentials, active sessions, personal documents and cryptocurrency data enable account takeovers, financial fraud, identity theft and extortion.

## Introduction

LummaStealer emerged on [Russian-language forums in late 2022](https://deepstrike.io/blog/infostealer-malware-credential-theft-2025), and evolved into one of the most prolific infostealers by the mid-2020s. It targets Windows systems and can harvest a wide range of sensitive data, including browser credentials, session cookies, cryptocurrency wallets and even two-factor authentication (2FA) tokens.

Under its MaaS model, Lumma's developers lease the malware to an extensive network of cybercriminal affiliates across the world. This has resulted in hundreds of thousands of infections across multiple industries, positioning Lumma as a significant enabler of secondary crimes such as account takeovers and fraudulent financial activity.

In May 2025, [Lumma's infrastructure was disrupted](https://www.bitdefender.com/en-gb/blog/hotforsecurity/microsoft-takedown-lumma-stealer) during a law-enforcement takedown that neutralized more than 2,300 command-and-control domains. However, the operation wasn't fully dismantled. Instead, the threat actors behind Lumma [migrated to bulletproof hosting providers](https://www.trendmicro.com/en_us/research/25/g/lumma-stealer-returns.html) that are less cooperative with law enforcement.

Recently, we have observed a considerable increase in LummaStealer activity in our insights. Loaders are typically delivered through evolving social-engineering lures, ranging from fake [CAPTCHA](https://blog.qualys.com/vulnerabilities-threat-research/2024/10/20/unmasking-lumma-stealer-analyzing-deceptive-tactics-with-fake-captcha) [challenges](https://mandarnaik016.in/blog/2024-10-05-malware-analysis-lumma-stealer/) to bogus update notifications on Steam pages and game development websites. The loaders themselves change frequently; we've seen LummaStealer using Rugmi, [DonutLoader](https://k3rn3lc4llz.medium.com/donutloader-uncovered-the-stealthy-malware-hiding-in-plain-sight-2775c955fd40), and, more recently, **CastleLoader** for initial execution.

By itself, CastleLoader is a sophisticated loader that executes in stages, entirely in memory, obfuscates its code, dynamically resolves APIs, and communicates with a large C2 infrastructure using stealth techniques. Its flexible, modular design allows threat actors to plug in various payloads while remaining relatively [hidden](https://blackpointcyber.com/blog/python-driven-castleloader-analysis/) in victim [systems](https://www.ibm.com/think/x-force/dissecting-castlebot-maas-operation).

Previous research has identified an overlap between the infrastructure used in Lumma Stealer and CastleLoader campaigns. Recorded Future's Insikt Group, which monitors the threat actor known as GrayBravo, the developer behind CastleLoader, [observed that multiple domains](https://www.recordedfuture.com/research/graybravos-castleloader-activity-clusters-target-multiple-industries) within the CastleLoader...