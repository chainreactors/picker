---
title: Kimsuky Evolves Reconnaissance Capabilities in New Global Campaign
url: https://buaq.net/go-161695.html
source: unSafe.sh - 不安全
date: 2023-05-05
fetch_date: 2025-10-04T11:36:58.442351
---

# Kimsuky Evolves Reconnaissance Capabilities in New Global Campaign

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

![](https://8aqnet.cdn.bcebos.com/0c4b9b5cb76433062e285412f978838c.jpg)

Kimsuky Evolves Reconnaissance Capabilities in New Global Campaign

By Tom Hegel and Aleksandar MilenkoskiExecutive SummarySentinelLabs has observed ongoing attacks
*2023-5-4 21:55:19
Author: [www.sentinelone.com(查看原文)](/jump-161695.htm)
阅读量:88
收藏*

---

**By Tom Hegel and Aleksandar Milenkoski**

## Executive Summary

* SentinelLabs has observed ongoing attacks from Kimsuky, a North Korean state-sponsored APT that has a long history of targeting organizations across Asia, North America, and Europe.
* Ongoing campaigns use a new malware component we call ReconShark, which is actively delivered to specifically targeted individuals through spear-phishing emails, OneDrive links leading to document downloads, and the execution of malicious macros.
* ReconShark functions as a reconnaissance tool with unique execution instructions and server communication methods. Recent activity has been linked to a wider set of activity we confidently attribute to North Korea.

## Background

Kimsuky is a North Korean advanced persistent threat (APT) group with a long history of targeted attacks across the world. Current understanding of the group indicates they are primarily assigned to intelligence collection and espionage operations in support of the North Korean government since at least 2012. In 2018 the group was observed deploying [a malware family dubbed BabyShark](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/), and our latest observations indicate the group has evolved the malware with an expanded reconnaissance capability – we refer to this BabyShark component as ReconShark.

## Targeted Organizations

Historically, Kimsuky targets have been located across countries in North America, Asia, and Europe. In the groups latest campaigns, they continue their global targeting themed around various ongoing geopolitical topics. For example, the latest Kimsuky campaigns have focused on nuclear agendas between China and North Korea, relevant to the ongoing war between Russia and Ukraine.

In a recent campaign Kimsuky targeted the staff of [Korea Risk Group](https://www.korearisk.com/) (KRG), the information and analysis firm specializing in matters directly and indirectly impacting the Democratic People’s Republic of Korea (DPRK). We applaud KRG’s willingness to publicly share our analysis of attacks against them so the wider cybersecurity community can use this intelligence for expanded understanding of the Kimsuky threat actor and their own hunting and detection efforts. Our assessment is that the same campaign has been used to continue targeting other organizations and individuals in at least the United States, Europe, and Asia, including think tanks, research universities, and government entities.

## Initial Access Targeting

For the deployment of ReconShark, Kimsuky continues to make use of specially crafted phishing emails. Notably, the spear-phishing emails are made with a level of design quality tuned for specific individuals, increasing the likelihood of opening by the target. This includes proper formatting, grammar, and visual clues, appearing legitimate to unsuspecting users. Notably, the targeted emails, which contain links to download malicious documents, and the malicious documents themselves, abuse the names of real individuals whose expertise is relevant to the lure subject such as Political Scientists.

In the malicious emails, Kimsuky entices the target to open a link to download a password-protected document. Most recently, they made use of Microsoft OneDrive to host the malicious document for download. For example, as used against KRG, the lure email contained the OneDrive shared file link:

```
1drv[.]ms/u/s!AvPucizxIXoqedcUKN647svN3QM?e=K6N1gT
```

The file downloaded is a password protected `.doc` file named “Research Proposal-Haowen Song.doc” (SHA1: `86a025e282495584eabece67e4e2a43dca28e505`) which contains a malicious macro (SHA1: `c8f54cb73c240a1904030eb36bb2baa7db6aeb01`)

![Malicious Document, themed to DPRK / China](https://www.sentinelone.com/wp-content/uploads/2023/05/Kimsuky_reconshark_5.jpg)

## ReconShark: A New BabyShark Reconnaissance Variant

The lure documents Kimsuky distributes contain Microsoft Office macros that activate on document close. Based on overlaps in file naming conventions, used malware staging techniques, and code format, we assess that the macros implement a newer variant of a reconnaissance capability of the Kimsuky’s BabyShark malware [seen](https://web.archive.org/web/20221201031619/https%3A//mp.weixin.qq.com/s/OaECtSaeClPzFHslN_WamA) targeting entities in the Korean peninsula towards the end of 2022. We refer to this BabyShark component as ReconShark.

The ability of ReconShark to exfiltrate valuable information, such as deployed detection mechanisms and hardware information, indicates that ReconShark is part of a Kimsuky-orchestrated reconnaissance operation that enables subsequent precision attacks, possibly involving malware specifically tailored to evade defenses and exploit platform weaknesses.

### Information Exfiltration

The main responsibility of ReconShark is to exfiltrate information about the infected platform, such as running processes, information about the battery connected to the system, and deployed endpoint threat detection mechanisms.

Similar to previous BabyShark variants, ReconShark relies on Windows Management Instrumentation (WMI) to query process and battery information.

![ReconShark queries process and battery information](https://www.sentinelone.com/wp-content/uploads/2023/05/Kimsuky_reconshark_3.jpg)

ReconShark queries process and battery information

ReconShark checks for the presence of a broad set of processes associated with detection mechanisms, such as `ntrtscan.exe` (Trend Micro OfficeScan), `mbam.exe` (Malwarebytes Anti-Malware), `NortonSecurity.exe` (Norton Security), and `avpui.exe` (Kaspersky Internet Security).

![Enumeration of deployed detection mechanisms](https://www.sentinelone.com/wp-content/uploads/2023/05/Kimsuky_reconshark_9_2.jpg)

Enumeration of deployed detection mechanisms

In contrast to previous BabyShark variants, ReconShark exfiltrates information without first storing it on the filesystem – the malware stores the information it collects in string variables and then uploads them to the C2 server by issuing HTTP POST requests.

![ReconShark exfiltrates information](https://www.sentinelone.com/wp-content/uploads/2023/05/Kimsuky_reconshark_8.jpg)

ReconShark exfiltrates information

### Payload Deployment

In addition to exfiltrating information, ReconShark deploys further payloads in a multi-stage manner that are implemented as scripts (VBS, HTA, and Windows Batch), macro-enabled Microsoft Office templates, or Windows DLL files. ReconShark decides what payloads to deploy depending on what detection mechanism processes run on infected machines.

Some ReconShark strings are encrypted using a relatively simple cipher to evade static detection mechanisms. These strings are typically commands or scripts for downloading and/or executing payloads.

![A decrypted command](https://www.sentinelone.com/wp-content/uploads/2023/05/Kimsuky_reconshark_2.jpg)

A decrypted command

ReconShark deploys and executes payloads in different ways. For example, the malware can directly download a payload from the C2 server using the `curl` utility, but also use Windows Shortcut (LNK files) or Office templates for that purpose.

ReconShark edits Windows Shortcuts (LNK files) to the `msedge.exe` (Microsoft Ed...