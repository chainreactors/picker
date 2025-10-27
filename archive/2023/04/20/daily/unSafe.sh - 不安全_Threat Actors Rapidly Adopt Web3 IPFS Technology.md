---
title: Threat Actors Rapidly Adopt Web3 IPFS Technology
url: https://buaq.net/go-159482.html
source: unSafe.sh - 不安全
date: 2023-04-20
fetch_date: 2025-10-04T11:32:42.352403
---

# Threat Actors Rapidly Adopt Web3 IPFS Technology

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

![](https://8aqnet.cdn.bcebos.com/c7c491f2265184b0ad5d8f555a0458d4.jpg)

Threat Actors Rapidly Adopt Web3 IPFS Technology

This post is also available i
*2023-4-19 21:0:55
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-159482.htm)
阅读量:40
收藏*

---

![A pictorial representation of InterPlanetary File System being used as a malicious vehicle](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/04/Unit42-red-team-23-illustration_Yellow-wo-logo.png)

This post is also available in:
[日本語 (Japanese)](https://unit42.paloaltonetworks.jp/ipfs-used-maliciously/)

## Executive Summary

During 2022, analysts from Unit 42 observed the rampant adoption of the InterPlanetary File System (aka IPFS) being used as a vehicle for malicious intent. IPFS is a Web3 technology that decentralizes and distributes the storage of files and other data into a peer-to-peer network.

Like any technology, IPFS can be abused by malicious threat actors. However, because the hosted content on IPFS is decentralized and distributed, there are challenges in locating and removing malicious content from the ecosystem, making it akin to bullet-proof hosting.

From the **last quarter of 2021 through the end of the last quarter of 2022**, Palo Alto Networks detected an 893% increase in IPFS-related traffic. Our calculations also show that VirusTotal reported over 27,000% increase during the same period.

This increase in IPFS-related traffic is rife with notable increases in malicious activity, as can be expected. Analysts from Unit 42 observed numerous threat campaigns in 2022 that covered the gamut of phishing, credential theft, malicious payload distribution and general adoption by threat actors.

Some of the key takeaways from our analysis include the following:

* There was a significant jump in IPFS-related traffic at the beginning of 2022. Palo Alto Networks detected a **178% increase** in IPFS-related traffic from the **last quarter of 2021 to the first quarter of 2022**, while **VirusTotal reported more than 6,500% increase** during that same reporting period.
* We have identified threat actors discussing the adoption of the technology on forums in the dark web as well as threat actors selling services hosted on IPFS.
* We have seen several types of cyberthreats using IPFS, including phishing, credential theft, command and control (C2) communications, and malicious payload distribution.

Palo Alto Networks customers receive protections from the malware families discussed as well as their malicious components in the following ways:

* [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR)
* The [Next-Generation Firewall](https://docs.paloaltonetworks.com/ngfw) with [Cloud-Delivered Security Services](https://docs.paloaltonetworks.com/cdss) including [WildFire](https://docs.paloaltonetworks.com/wildfire) and [Advanced Threat Prevention](https://docs.paloaltonetworks.com/advanced-threat-prevention/administration).
* [Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering/administration) and [DNS Security](https://docs.paloaltonetworks.com/dns-security) can analyze and block malicious IPFS domains, including malware and phishing hosting URLs, and C2 domains.

| **Related Unit 42 Topics** | [**Phishing**](https://unit42.paloaltonetworks.com/tag/phishing/), **[Malware](https://unit42.paloaltonetworks.com/category/malware-2/)** |
| --- | --- |

## Table of Contents

[What Are Web3 and IPFS?](#post-127743-_wven14kmgum2)

## What Are Web3 and IPFS?

Before we delve into our observations around threat actor behavior associated with IPFS, it is important to have a general understanding of Web3 and also IPFS. IPFS is one of the technologies that supports Web3 infrastructures.

Web3 – or the third iteration of the web – is a new version of the internet that prioritizes decentralization using blockchain technology and tokens. With Web3, users can safeguard their data against censorship and manipulation without the need for a central authority.

This decentralization allows individuals to have ownership and control over their own content, which can be posted without fear of governments or tech companies removing it. However, cybercriminals can also exploit these same benefits to further their malicious activities.

IPFS is a distributed file sharing system that was released in 2015. It is open source and uses a peer-to-peer (P2P) hypermedia protocol, making the internet faster, safer and more open.

Unlike the traditional web, IPFS is content-oriented and searches for content identifiers in the form of hashes through a decentralized network, rather than specific locations. Content on IPFS can be accessed by establishing your own node on the IPFS network or using IPFS gateways, which are third-party web-based interfaces between the web and the IPFS network. These gateways allow users to view and pull content through HTTP requests, but they cannot alter or add to the content.

More information about Web3 and IPFS can be found at the following sites:

* [Web3](https://en.wikipedia.org/wiki/Web3)
* [IPFS](https://github.com/ipfs/ipfs)

## Increase in Overall Traffic

Despite its relative obscurity, we observed a notable increase in IPFS traffic across Palo Alto Networks starting the first quarter of 2022, as seen in Figure 1. In the first quarter of 2022, our products detected a 178% increase in IPFS traffic as compared to what we logged at the end of the last quarter of 2021.

This traffic continued to increase following this initial observation:

* An increase of 85% in the second quarter
* A 62% increase in the third quarter
* A 19% increase in the last quarter of 2022

This equated to an overall increase of 893%.

![Image 1 is a graph of Palo Alto Networks’ observed IPFS traffic. It shows an increase of almost 900% between quarter four of 2021 to quarter four of 2022.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/04/chart.png)

Figure 1. Palo Alto Networks IPFS traffic.

We had also identified that IPFS-related traffic saw a similar increase on VirusTotal for the first quarter of 2022, with an increase of 6,503% when compared to the last quarter of 2021.

Similar to what was seen across Palo Alto Networks, VirusTotal continued to see the following increases quarter over quarter (as shown in Figure 2):

* A 68% increase in the second quarter
* A 69% increase in the third quarter
* A 48% increase in the last quarter of 2022

![Image 2 is a graph showing the increase of VirusTotal IPFS submissions from quarter four of 2021 to quarter four of 2022. There is a large increase over time from 149 to almost 41,500.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/04/chart-1.png)

Figure 2. VirusTotal IPFS submissions.

As shown in the observed traffic for IPFS represented in Figures 1 and 2, this increase can be directly attributed to the adoption of IPFS as a technology. Unfortunately, with the adoption of any new technology, there are always people who aim to use it with malicious intent. The notable increase in IPFS traffic we observed in Palo Alto Networks and VirusTotal submissions also includes substantial increases in malicious activity using IPFS.

Analysts from Unit 42 have observed adoption of IPFS for the following types of malicious activities over the past year:

* Adoption by threat actors
* Utilization for phishing and account credential theft
* Utilization by several malware intrusion sets for malicious payload distribution
* C2 communication

## Observations of Threat Actors Adopting IPFS

Unit 42 researchers have observed threat actors discussing their use of IPFS, or their c...