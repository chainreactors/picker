---
title: Ransomware-driven data exfiltration: techniques and implications
url: https://blog.sekoia.io/ransomware-driven-data-exfiltration-techniques-and-implications/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-28
fetch_date: 2025-10-06T19:31:49.747082
---

# Ransomware-driven data exfiltration: techniques and implications

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

# Ransomware-driven data exfiltration: techniques and implications

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Livia Tibirna, Caroline Lewis and Sekoia TDR](#molongui-disabled-link)
November 27 2024

0

3 minutes reading

[Download the full report](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/11/Ransomware-driven-data-exfiltration-techniques-and-implications.pdf)

## Introduction

This report focuses on the **exfiltration techniques** leveraged by **ransomware and extortion groups** in lucrative campaigns. It aims to provide a comprehensive analysis of the techniques and tools used during the exfiltration phase and the **impact** **on affected organisations**. It also includes observations relating to the collection tactic, which we consider essential for a comprehensive understanding of exfiltration campaigns.

First, we will explore the **progressive adoption** of the exfiltration technique by ransomware and extortion groups and the **motivations** behind their campaigns. Second, we will analyse the different **categories of targeted data** during the exfiltration phase.

Next, we will focus on the **tools leveraged by lucrative intrusion sets** to gather valuable data from a victim’s environment. Finally, we will provide insights into **detecting different tools** and techniques associated with data exfiltration.

While this report focuses on opportunistic, ransomware-driven intrusion sets and campaigns, it is worth noting that a wide range of distinct financially motivated intrusion sets employ exfiltration tactics. This includes operators of infostealers, remote access trojans (RATs), spyware, credit card skimmers, backdoors, and other types of malicious software. Moreover, state-sponsored actors also largely leverage the exfiltration tactic in information-gathering campaigns. While we may reference these categories of actors in our analysis, they are not the primary focus of our study.

Our research involved both open-source reporting and in-house investigations.

## Executive summary

* **Data exfiltration** became a **critical element** in ransomware campaigns, in line with the widespread adoption of the double extortion technique between 2019 and 2024.

* Attackers **leverage stolen data** to maximise **financial and reputational impact** through public exposure on dedicated leak sites, while also potentially selling the data to other threat actors or using it for additional extortion and subsequent attacks.

* These motivations, along with factors like reduced effort and the circumvention of encryption-related challenges, led some ransomware groups to **focus partially or exclusively on data exfiltration** for extortion, without encrypting files.

* Besides lucrative ransomware and extortion groups, exfiltration is also **leveraged by state-sponsored intrusion sets** during ransomware operations, likely to misdirect attribution, conduct covert intelligence gathering campaigns, and generate revenue.

* Over the past five years, ransomware operators increasingly refined their extortion techniques to **maximise leverage for double extortion**. They adopted a more strategic approach by **pre-qualifying and triaging collected data**. This involves **targeted searches** aimed at extracting high-value, sensitive files, such as financial information, personal and medical records, classified documents, IT-related and network data and other highly sensitive information.

* Ransomware groups use a combination of **custom and publicly available tools** to facilitate data exfiltration. This is according to their specific features and their intended use in exfiltration campaigns: **enumeration**, **compression, uploading**, etc.

* Advanced intrusion sets increasingly develop and use **custom exfiltration tools** to enhance efficiency, precision, and stealth. Ransomware operators occasionally leverage **commodity malware**, including infostealers and Malware-as-a-Service (MaaS) tools, to streamline the data exfiltration processes. However, their use remains limited compared to publicly available alternatives.

* **Legitimate and publicly available tools** are widely leveraged to facilitate stealthy and cost-effective data exfiltration while blending in with legitimate activities to evade detection.

* To mitigate the impact of data theft and ransomware deployment, companies should prioritise **early detection** of data exfiltration attempts through a **multimethod strategy**, including monitoring suspicious behaviour, file access patterns, and the use of known exfiltration tools, while focusing on critical files and directories to detect potential data movement.

![Tools most used by main ransomware operations to facilitate exfiltration in lucrative campaings, from 2022 to November 2024, based on open-source reporting.](data:image/svg+xml...)![Tools most used by main ransomware operations to facilitate exfiltration in lucrative campaings, from 2022 to November 2024, based on open-source reporting.](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/11/FIgure-4.-Tools-used-by-main-ransomware-operations-to-facilitate-exfiltration-799x1024.png)

[Download the full report](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/11/Ransomware-driven-data-exfiltration-techniques-and-implications.pdf)

**Thank you for reading this blog post. Please don’t hesitate to provide your feedback on our publications by [clicking here](https://framaforms.org/sekoiaio-blogposts-feedback-1721899427). You can also contact us at tdr[at]sekoia.io for further discussions.**

* [Sekoia.io mid-2023 Ransomware Threat Landscape](https://blog.sekoia.io/sekoia-io-mid-2023-ransomware-threat-landscape/)
* [Sekoia.io Mid-2022 Ransomware Threat Landscape](https://blog.sekoia.io/sekoia-io-mid-2022-ra...