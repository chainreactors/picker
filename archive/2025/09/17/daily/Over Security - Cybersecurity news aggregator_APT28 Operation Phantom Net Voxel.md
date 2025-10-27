---
title: APT28 Operation Phantom Net Voxel
url: https://blog.sekoia.io/apt28-operation-phantom-net-voxel/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-17
fetch_date: 2025-10-02T20:15:42.189029
---

# APT28 Operation Phantom Net Voxel

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# APT28 Operation Phantom Net Voxel

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/01/TDR-badge.png)](#molongui-disabled-link)

[Amaury G., Charles M. and Sekoia TDR](#molongui-disabled-link)
September 16 2025

0

41 minutes reading

**This post was originally distributed as a private FLINT report to our customers on 12 August 2025.**

#### Table of contents

* [Introduction](#h-introduction)
* [Infection chain overview](#h-infection-chain-overview)
* [Technical analysis](#h-technical-analysis)
  + [Lure documents analysis](#h-lure-documents-analysis)
  + [Infection – VBA Analysis](#h-infection-vba-analysis)
  + [Second stage DLL and steganography](#h-second-stage-dll-and-steganography)
  + [Shellcode](#h-shellcode)
  + [Covenant & Koofr interactions](#h-covenant-amp-koofr-interactions)
  + [BeardShell](#h-beardshell)
  + [SlimAgent](#h-slimagent)
* [Conclusion](#h-conclusion)
* [IOCs and Technical Details](#h-iocs-and-technical-details)
  + [Weaponized Office documents](#h-weaponized-office-documents)
  + [Public cloud infrastructure](#h-public-cloud-infrastructure)
  + [Hashes](#h-hashes)
  + [YARA](#h-yara)
  + [Python scripts](#h-python-scripts)

## Introduction

**Sekoia.io’s Threat Detection and Response** (TDR) team closely monitors APT28 as one of its highest-priority threat actors. In early 2025 a trusted partner provided **two previously unseen malware** **samples attributed to APT28**. These samples did not correspond to any publicly documented infection chain at the time, so we began to take a closer look. A few months later, on 21 June 2025,  [CERT-UA published a report](https://cert.gov.ua/article/6284080) on the BeardShell and Covenant framework, attributing them to APT28. By analysing the samples, we established that the partner’s samples and those described by CERT-UA were identical. By correlating CERT-UA’s findings with our own, **we uncovered additional weaponized Office documents** and subtle techniques that have not yet been documented publicly.

Known by no fewer than 28 aliases – among them Sofacy, Fancy Bear, BlueDelta, Forest Blizzard and TAG-110 – **APT28** is identified by intelligence services as operated by Russia’s General Staff Main Intelligence Directorate (GRU), specifically the 85th Main Special Service Centre (GTsSS) of Military Unit 26165.

Throughout 2025, this intrusion set has drawn attention across the cybersecurity community by being the subject of multiple reports including a [joint advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a) of 21 international partners or a report of the [French ANSSI](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2025-CTI-007.pdf). In January 2025, we shared our findings on the **Double-Tap campaign,** a Russia-nexus APT operation potentially linked to APT28 that [targeted diplomatic channels in Central Asia and Kazakhstan for cyber espionage](https://blog.sekoia.io/double-tap-campaign-russia-nexus-apt-possibly-related-to-apt28-conducts-cyber-espionage-on-central-asia-and-kazakhstan-diplomatic-relations/). This campaign remains active and has shifted its operations to targets in Tajikistan, [as noted by Recorded Future](https://go.recordedfuture.com/hubfs/reports/cta-2025-0522.pdf) in May 2025, although a conclusive attribution between UAC-0063 and APT28 has yet to be established.

**This report presents our current insights and serves to complement CERT-UA’s analysis of the new techniques deployed by APT28 in this new campaign based on our own investigation.**

## Infection chain overview

Combining CERT-UA’s findings with our own analysis, the following figure presents an overview of the infection chain.

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/09/Group-626267.png)

*Figure 1 – Overall infection chain*

As documented by CERT-UA, the infection chain begins with the Office document being delivered via a private Signal chat.

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/09/signao-cert-ua-1.png)

*Figure 2 – Preview of Signal conversation (source: CERT-UA)*

These exchanges exemplify a spearphishing campaign in which a user, posing as a colleague or superior, urges the recipient to open and complete the malicious Office document. By invoking compensation decisions and threatening legal action, the sender creates a false sense of urgency, manipulating the target with references to penalties and prompts to liaise with higher-level management for further details.

The document retrieved by the victim embeds multiple malicious macros: a primary routine plus several auxiliary methods that together implement a user-level COM hijack to load a malicious DLL. Once loaded this DLL extracts a shellcode from a valid PNG file, `windows.png`, which loads a .NET assembly executable. This new executable corresponds to the `GruntHTTPStager` component of the **Covenant framework**. Its primary function is to establish an API-driven channel to the Koofr cloud infrastructure and await some additional payloads.

According to CERT-UA, this first first part of the infection chain leads to the download of two files, `sample-03.wav` and `PlaySndSrv.dll`. We were unable to retrieve these samples and therefore could not analyse them. `PlaySndSrv.dll` is reported to decrypt and extract a second-stage payload from `sample-03.wav`, named **BeardShell**. This C++ malware uses the icedrive cloud-storage service as its command and control channel to receive and execute PowerShell commands.

In the following section of this report, we will **analyze in detail the various stages of the infection chain**. We will also describe SlimAgent, a spyware that CERT-UA observed on the same infected server as BeardShell even if they cannot confirm a direct link between it and this infection chain. The only part ...