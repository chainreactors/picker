---
title: FSB’s matryoshka #2/3 – Gamaredon’s gifts that keeps unpacking – GammaLoad
url: https://blog.sekoia.io/fsbs-matryoshka-2-3-gamaredons-gifts-that-keeps-unpacking-gammaload/
source: Over Security
date: 2026-06-03
fetch_date: 2026-06-04T06:32:00.434979
---

# FSB’s matryoshka #2/3 – Gamaredon’s gifts that keeps unpacking – GammaLoad

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

[![logo sekoia.io blog light](data:image/svg+xml...)![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

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

# FSB’s matryoshka #2/3 – Gamaredon’s gifts that keeps unpacking – GammaLoad

[![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/01/TDR-badge.png)](#molongui-disabled-link)

[Amaury G. and Sekoia TDR](#molongui-disabled-link)
June 3 2026

0

11 minutes reading

This investigation is published in three parts. Follow the links below to navigate through our findings:

* [FSB’s matryoshka #1/3](https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/) – **GammaPhish** and **GammaWorm**
* [FSB’s matryoshka #2/3](https://blog.sekoia.io/fsbs-matryoshka-2-3-gamaredons-gifts-that-keeps-unpacking-gammaload/) – **GammaLoad**
* [FSB’s matryoshka #3/3](https://blog.sekoia.io/fsbs-matryoshka-3-3-gamaredons-gifts-that-keeps-unpacking-gammasteel/) – **GammaSteel**

## Key Takeaways

* **Gamaredon** is a **cyberespionage group specialized in long-term and persistent intrusion operations** targeting Ukraine. Officially operated by **Russia’s FSB**, the group is focusing government, military, and critical infrastructure networks, and is still actively operating at the time of this publication.
* **This report analyses over a decade of malware families** and establishes a unified naming taxonomy to cut through the fragmented nomenclature.
* **The infection chain is designed to be invisible:** by hiding inside legitimate Windows features and abusing trusted platforms like Telegram, Cloudflare, and standard cloud storage, Gamaredon leaves almost no trace on infected machines.
* **Once inside a network, malware spreads physically**, infecting USB drives to jump across air-gapped systems and steals documents whether they are stored, being transferred, or actively edited in real time.
* **Every step of the infection chain doubles as a backdoor**, giving operators the ability to push new commands, update configurations, or deploy additional payloads, ensuring permanent access to compromised hosts.
* **Sekoia’s TDR team tracked and reconstructed this entire infection chain** to anticipate the threat, protect our worldwide clients, and contribute to countering operations that directly target the sovereignty of democratic states.

## Table of contents

* [Key Takeaways](#h-key-takeaways)
* [Introduction](#h-introduction)
* [Infection chain](#h-infection-chain)
  + [GammaLoad : loaders loading loaders](#h-gammaload-loaders-loading-loaders)
* [Conclusion](#h-conclusion)
* [IOCs](#h-iocs)
  + [Payloads](#h-payloads)
  + [DDR](#h-ddr)
  + [C2](#h-c2)

## Introduction

The Sekoia.io **Threat Detection & Research** (TDR) team continuously monitors **Gamaredon** (aka UAC-0010, Armagedon), an **FSB operated Russian intrusion-set historically targeting Ukrainian governmental and critical infrastructure**. In our last report [FSB’s matryoshka #1/3](https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/), we detailed the early stages of their January 2026 infection chain, focusing specifically on their initial access and propagation mechanisms.

Tracking Gamaredon’s ongoing campaigns presents **significant challenges** due to the rapid development cycle and the cybersecurity industry’s fragmented naming conventions. Over the past decade, their espionage arsenal has heavily evolved, shifting from the **Pteranodon** framework to highly modular, standalone payloads tracked under various names. To cut through this complexity and bring clarity to their current capabilities, **Sekoia.io aligns with CERT-UA’s taxonomy**, grouping the malware by its primary function:

* **GammaPhish** (initial access)
* **GammaLoad** (intermediary loaders)
* **GammaWorm** (worm)
* **GammaSteel** (stealer)
* **GammaWipe** (wiper)

*Note: We use the term loader when the execution chain remains entirely in-memory without writing files to disk, whereas dropper refers to stages where a file is written to the file system.*

Building upon our initial publication, and thanks to over 70 artifacts retrieved by a trusted partner alongside our own live interactions with Gamaredon’s C2 staging infrastructure, we are continuing our series documenting Gamaredon 2026 arsenal. This second report focuses exclusively on **GammaLoad**, providing a technical analysis of the intermediary components used by Gamaredon to stage and deploy their final payload, **GammaSteel**, that will be analysed in the next report.

## Infection chain

### GammaLoad : loaders loading loaders

In this section, we will examine **GammaLoad**, a collection of VBScripts designed to ensure continuous access and deploy payloads over time by leveraging **Dead Drop Resolvers** (DDR).

It stores and updates its active C2 configuration within the Windows registry (`HKCU\Console`, the same location used by **GammaWorm**). This registry caching mechanism ensures that whenever GammaLoad is triggered again, it can resume communications using the most recent valid infrastructure.

By combining artifacts from a compromised host with live network replay, we successfully triggered the execution flow, which consists of three distinct stages:

* **First Stage (loader):** fingerprints the host and uses a failover mechanism to find an active C2. It prioritizes cached URLs in the registry before falling back to legitimate DDR services (Telegraph, Telegram, Check-Host) to fetch and execute the next stage.
* **Second Stage (dropper):** Unlike the first stage, this script fetches the next payload and writes it to an Alternate Data Stream (ADS) within `%TEMP%`. It then establishes persistence by creating a scheduled task to execute this ADS before terminating.
* **Third Stage (PowerShell loader):** Executed regularly by the scheduled task, this obfuscated loader spawns a hidden PowerShell process. It fetches, XOR-decry...