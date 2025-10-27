---
title: A three beats waltz: The ecosystem behind Chinese state-sponsored cyber threats
url: https://blog.sekoia.io/a-three-beats-waltz-the-ecosystem-behind-chinese-state-sponsored-cyber-threats/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-14
fetch_date: 2025-10-06T19:28:24.914846
---

# A three beats waltz: The ecosystem behind Chinese state-sponsored cyber threats

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

# A three beats waltz: The ecosystem behind Chinese state-sponsored cyber threats

[![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/04/TDR-badge.png)](#molongui-disabled-link)

[Sekoia TDR and Coline Chavane](#molongui-disabled-link)
November 13 2024

0

2 minutes reading

[Download the full report](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/11/A-three-beat-waltz-The-ecosystem-behind-Chinese-state-sponsored-cyber-threats.pdf)

## Executive Summary

* The **People’s Liberation Army** (PLA), the **Ministry of State Security** (MSS) and the **Ministry of Public Security** (MPS) are the three main **state actors** conducting state-sponsored offensive cyber operations for the interests of the Chinese Communist Party (CCP).

* From 2021 onward, Sekoia observed that operations attributed to China were **mostly linked to the Ministry of State Security (MSS)** rather than the People’s Liberation Army (PLA). Still, since the 2015 PLA reform, malicious cyber activity attributed to MSS-sponsored entities **increased**, while activity attributed to the PLA **depleted**.

* **Provincial departments** of the MSS and the MPS enjoy a **large degree of autonomy** to conduct cyber operations and **rely on private companies** to outsource offensive capacities.

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/11/Short-CCH-_-Schema-organisation-cyber-CN.svg)

* In addition to state actors, **civilian actors also took part historically** in state-sponsored operations. This is the case of the **first communities of patriotic hackers**, which conducted hacktivist campaigns in reaction to geopolitical events, and were progressively integrated into state-sponsored operations.

* The role of patriotic hackers in Chinese cyber offensive capacities is highlighted by their participation in the **development of malicious payloads** used by China-nexus APTS, such as **PlugX and ShadowPad**. This proximity was encouraged by the policies of Xi Jinping, who made **Military-Civil Fusion (MCF) a national strategy** in 2015.

* The CCP policy regarding activities of patriotic hackers changed after 2002, leading patriotic hackers to **stop hacktivism and professionalise**. Today, many of these individuals work for private companies and maintain parallel activities like cybercrime.

* Recent leaks from the Chinese IT company I-SOON revealed important details about the **current hack-for-hire ecosystem** in China. State actors subcontract cyber offensive services at the provincial and the city levels.

* State actors **increasingly outsource** cyber offensive capabilities to private entities, a trend fueled by ministries like the **MSS collecting vulnerabilities** from researchers and companies. These vulnerabilities are then **weaponized** and used as exploits in state-sponsored operations.

* The companies providing cyber offensive capacities to state actors are historical tech giants, but also **smaller companies offering niche digital services**, like I-SOON. China-nexus APTs are likely to be a **mix of private and state actors cooperating** to conduct operations, rather than strictly being associated with single units.

## Introduction

Recent reports about the People’s Republic of China (PRC) cyber capabilities highlighted its important arsenal mobilising **institutional** and **military** actors, as well as **private companies** providing hack-for-hire services for governmental operations. These findings pointed out the complexity of attributing attack campaigns to specific clusters of malicious activity and tracing back Chinese state-sponsored units throughout the time.

This report aims at presenting the **Chinese offensive cyber ecosystem**, its key actors, their role and their relationships, based on Sekoia’s analysis of the latest cyber campaigns attributed to China, open source reports, and interviews conducted with prominent researchers on the topic. Thanks to **Ivan Kwiatkowski, Dakota Cary and Eugenio Benincasa** for their time and insights into this subject.

*Cut-off date for this paper is 12 November 2024.*

[Download the full report](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/11/A-three-beat-waltz-The-ecosystem-behind-Chinese-state-sponsored-cyber-threats.pdf)

Share

[China](https://blog.sekoia.io/tag/china/)
[CTI](https://blog.sekoia.io/tag/cti/)
[State-sponsored](https://blog.sekoia.io/tag/state-sponsored/)
[Strategic](https://blog.sekoia.io/tag/strategic/)

Share this post:

### What's next

## [Helldown Ransomware: an overview of this emerging threat](https://blog.sekoia.io/helldown-ransomware-an-overview-of-this-emerging-threat/)

This blogpost provide a comprehensive Analysis of Helldown: Tactics, Techniques, and Procedures (TTPs).

[![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/07/TDR-badge2.png)](#molongui-disabled-link)

[Jeremy Scion and Sekoia TDR](#molongui-disabled-link)

## [Ransomware-driven data exfiltration: techniques and implications](https://blog.sekoia.io/ransomware-driven-data-exfiltration-techniques-and-implications/)

Introduction This report focuses on the exfiltration techniques leveraged by ransomware and extortion groups in lucrative campaigns. It aims...

[![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Livia Tibirna, Caroline Lewis and Sekoia TDR](#molongui-disabled-link)

## [Implementing blocklists in the Sekoia SOC platform](https://blog.sekoia.io/blocklist-in-sekoia/)

On a calm Friday afternoon, rumors of a new active threat starts hitting the various social network websites. Your...

[![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.r...