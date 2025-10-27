---
title: Spike in LokiBot Activity During Final Week of 2022
url: https://buaq.net/go-151897.html
source: unSafe.sh - 不安全
date: 2023-03-04
fetch_date: 2025-10-04T08:37:16.040606
---

# Spike in LokiBot Activity During Final Week of 2022

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/d74c95cb263f58967c5e4233b07a653b.jpg)

Spike in LokiBot Activity During Final Week of 2022

Executive SummaryUnit 42 res
*2023-3-3 22:0:16
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-151897.htm)
阅读量:43
收藏*

---

![A pictorial representation of malicious email like LokiBot where a stylized bug pops out of an envelope](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/03/Malicious-email-r3d2.png)

## Executive Summary

Unit 42 researchers have uncovered a malware distribution campaign that is delivering the LokiBot information stealer via business email compromise (BEC) phishing emails. This malware is designed to steal sensitive information from victims' systems, such as passwords and banking information, as well as other sensitive data.

In this blog, we will explain how attackers used an innocent-looking email to lure victims into opening an attachment. The attachment contained a LokiBot information stealer.

We will provide technical details on how the LokiBot sample uses obfuscation and a persistence mechanism to avoid detection. We will also describe the command and control (C2) channel communication. Finally, we will list the various applications from which the malware steals data.

The [Appendix](#post-127127-_ivlsyj521a6a) of this blog will provide an in-depth description of each data byte in the HTTP based C2 communication, detailing the specific purpose of each byte. It will also provide a breakdown of how the data byte is structured.

Palo Alto Networks customers receive protections from and mitigations for LokiBot information stealer C2 communication in the following ways:

* [Next-Generation Firewalls](https://www.paloaltonetworks.com/network-security/next-generation-firewall) with a [Threat Prevention](https://www.paloaltonetworks.com/products/secure-the-network/subscriptions/threat-prevention) subscription can identify and block LokiBot malware with TID 85304 and 21630.
* [Next-Generation Firewalls](https://www.paloaltonetworks.com/network-security/next-generation-firewall) with an [Advanced Threat Prevention](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/threat-prevention/about-threat-prevention/advanced-threat-prevention) subscription can identify and block the variations of LokiBot communication using a machine learning solution.
* [WildFire](https://www.paloaltonetworks.com/products/secure-the-network/wildfire) and [Cortex XDR](https://www.paloaltonetworks.com/cortex/cortex-xdr) can identify and block the attachment file described in the blog.

| **Related Unit 42 Topics** | [**LokiBot**](https://unit42.paloaltonetworks.com/tag/lokibot/) |
| --- | --- |

## Table of Contents

[Introduction](#post-127127-_qiwqxzjk24f9)

## Introduction

LokiBot (often referred to as Loki-bot or Loki PWS) is notorious information-stealing malware. It collects sensitive data from web browsers, email clients, FTP servers and crypto wallets. This threat then uploads this information to an attacker-controlled machine via HTTP POST.

The malware can also create a backdoor on the infected machine, enabling an attacker to install further malicious software. First identified in 2015, LokiBot has since been used in multiple security breaches. Furthermore, the malware is constantly evolving, making it difficult to contain and protect against.

During the winter holiday season of 2022, Unit 42 researchers noticed that our machine learning-based C2 detection solution identified a particular HTTP payload as malicious. After analyzing its traffic patterns, we identified that it belonged to a LokiBot infection.

After investigating the attack vector delivering this malware and further network traffic activity, we found the original email that included a ZIP file attached, which contained an ISO file. The ISO file had the final payload.

We have found that this attempt to deliver the LokiBot malware has strong ties to a BEC campaign. BEC entails gaining unauthorized access to email leading to financial fraud, and it is one of the most prevalent and costly forms of cyberattacks today.

Signs of BEC include fraudulent wire transfer requests, as well as spam or phishing emails sent from a customer’s corporate domain. Victims might also notice missing or deleted emails due to unauthorized access to email systems.

![Image 1 is a screenshot of a malspam email that delivers a LokiBot sample. Identifying information is redacted, and the language in the email is Turkish. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/03/word-image-127127-1-1.png)

Figure 1. Malspam delivers a LokiBot sample.

When collecting data, we also analyzed additional threat intel data sources such as [ThreatFox](https://threatfox.abuse.ch/browse/tag/LokiBot/). We noticed that LokiBot activity had a relatively small amount of indicators of compromise (IoCs) when we first detected this sample. However, during the end of 2022, the number of occurrences peaked in the last three days of December.

Threat actors [often increase their attack efforts](https://www.cisa.gov/uscert/ncas/alerts/aa21-243a) during U.S. or other targeted nations' holidays. During this time, cyberattacks are often more effective as security and other personnel take this time off.

Figure 2 shows LokiBot activity from ThreatFox.

![Image 2 is a graph using data from ThreatFox measuring the spike in December 2022 of LokiBot activity. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/03/word-image-127127-2-1.png)

Figure 2. ThreatFox LokiBot monitoring. Data source: [ThreatFox](https://threatfox.abuse.ch/browse/tag/LokiBot/).

## LokiBot Malware Analysis

### First Stage

The ISO file format is typically used to package the contents of an optical disc. In this instance, it is used to deliver the LokiBot malware. By using this file format, the attackers are trying to bypass malspam detection technologies that usually focus on detecting file types more commonly used in malware infection chains (e.g., EXE and DLL files, MS Office files).

ISO files are also attractive to attackers because, while specific software was required to open them in the past, Windows includes an ISO file opener that mounts and opens the file with a simple double-click. To the victim, the opening process simply looks like a regular directory.

### Loader

Opening the ISO file gives us access to a PE EXE file that is actually a loader. This file is an obfuscated .NET file using [process hollowing](https://unit42.paloaltonetworks.com/banking-trojan-techniques/), which is a code injection technique in which an attacker removes legitimate code from an executable and replaces it with malicious code.

In this case, process hollowing was used to inject a malicious PE file into the legitimate process called aspnet\_compiler.exe. Figure 3 shows some IoCs in the memory of the infected process. Dumping the PE from the process memory gives us access to the final LokiBot payload.

![Image 3 is a screenshot of aspnet_compiler.exe showing the IoCs in the memory of the infected process in the “Results” window.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/03/word-image-127127-3-1.png)

Figure 3. The infected process that contains IoCs.

### Final Payload

#### Obfuscation

This LokiBot sample only uses one code obfuscation technique: API hashing. Malware authors use this technique to retrieve export functions from loaded libraries using a computed hash.

Replicating the hashing function implementation allows us to retrieve the corresponding APIs in the appropriate library. Figure 4 shows a Python implementation of the API hashing...