---
title: FSB’s matryoshka #1/3 – Gamaredon’s gifts that keeps unpacking – GammaPhish and GammaWorm
url: https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/
source: Over Security
date: 2026-06-01
fetch_date: 2026-06-02T06:33:06.962321
---

# FSB’s matryoshka #1/3 – Gamaredon’s gifts that keeps unpacking – GammaPhish and GammaWorm

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

# FSB’s matryoshka #1/3 – Gamaredon’s gifts that keeps unpacking – GammaPhish and GammaWorm

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/01/TDR-badge.png)](#molongui-disabled-link)

[Amaury G. and Sekoia TDR](#molongui-disabled-link)
June 1 2026

0

29 minutes reading

This investigation is published in three parts. Follow the links below to navigate through our findings:

* [FSB’s matryoshka #1/3](https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/) – **GammaPhish** and **GammaWorm**
* (*coming soon*) [FSB’s matr](https://blog.sekoia.io/fsbs-matryoshka-2-3-gamaredons-gifts-that-keeps-unpacking-gammaload/%E2%86%97)[y](https://blog.sekoia.io/fsbs-matryoshka-2-3-gamaredons-gifts-that-keeps-unpacking-gammaload/)[oshka #2/3](https://blog.sekoia.io/fsbs-matryoshka-2-3-gamaredons-gifts-that-keeps-unpacking-gammaload/%E2%86%97) – **GammaLoad**
* (*coming soon*) [FSB’s matryoshka #3/3](https://blog.sekoia.io/fsbs-matryoshka-3-3-gamaredons-gifts-that-keeps-unpacking-gammasteel/) – **GammaSteel**

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
* [Context](#h-context)
  + [Gamaredon](#h-gamaredon)
  + [Malware family](#h-malware-family)
* [Infection chain](#h-infection-chain)
  + [Overview](#h-overview)
  + [GammaPhish](#h-gammaphish)
  + [GammaWorm](#h-gammaworm)
* [Conclusion](#h-conclusion)
* [Detection and hunting opportunities](#h-detection-and-hunting-opportunities)
* [IOCs](#h-iocs)
  + [GammaPhish](#h-gammaphish-0)
  + [GammaWorm](#h-gammaworm-0)

## Introduction

**Sekoia.io’s Threat Detection & Research** (TDR) team closely monitors the activities of Russian Advanced Persistent Threats (APT). In late December 2025, we deployed an opportunistic YARA rule designed to uncover novel initial access vectors. By January 2026, **this rule had generated a dozen hits**, prompting an in-depth investigation. While we successfully identified the **early stages of a Gamaredon infection chain**, unknown restrictions prevented us from fully detonating the sequence to observe the final payloads.

To overcome this, we collaborated with a trusted partner who provided over 70 artifacts retrieved directly from compromised hosts. These artifacts not only corroborated the initial attack stages we observed in December but also contained several distinct malware families historically attributed to Gamaredon: a **worm, loaders and a stealer**, widely tracked by the community as Pteranodon, GammaLoad, and GammaSteel.

While the TDR team has previously modeled multiple Gamaredon campaigns for Sekoia CTI, **tracking this specific intrusion-set consistently presents significant challenges**. Their execution flows are notoriously lengthy and complex. Furthermore, the fragmented naming conventions across the cybersecurity industry, combined with Gamaredon’s rapid iteration of its malware, create technical confusion and obscure the threat’s operational comprehension.

To cut through this complexity and provide clarity on Gamaredon’s current capabilities, we decided to **thoroughly document their January 2026 infection chain**, compare the different malware versions, and **align the naming conventions of the malware** based on our own findings. By combining our initial findings with the partner-provided artifacts, we reconstructed an important part of Gamaredon’s long-term campaign, which is still ongoing at the time of writing. In addition, understanding some stages allowed us to replay live network requests to Gamaredon’s Command and Control (C2) servers. This live interaction successfully tricked the staging infrastructure into **delivering the most recent versions of the loaders and the final stealer**.

TDR team is releasing a series of reports dedicated to dissecting Gamaredon’s latest espionage arsenal. This series aims to **comprehensively document the full execution chain and the novel methodologies deployed by the group in 2026**, contrasting our findings with existing open-source intelligence.

Specifically, this first report focuses on the initial access stage and the worm.

## Context

### Gamaredon

This long-term campaign is attributed to **Gamaredon** (aka ACTINUM, Armageddon, UAC-0010, BlueAlpha), a Russian state-sponsored intrusion-set [officially linked by national agencies, such as the Security Service of Ukraine (SSU)](https://ssu.gov.ua/en/novyny/sbu-vstanovyla-khakeriv-fsb-yaki-zdiisnyly-ponad-5-tys-kiberatak-na-derz...