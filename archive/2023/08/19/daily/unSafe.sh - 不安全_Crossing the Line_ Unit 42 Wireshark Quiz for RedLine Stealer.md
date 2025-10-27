---
title: Crossing the Line: Unit 42 Wireshark Quiz for RedLine Stealer
url: https://buaq.net/go-174793.html
source: unSafe.sh - 不安全
date: 2023-08-19
fetch_date: 2025-10-04T11:59:20.949642
---

# Crossing the Line: Unit 42 Wireshark Quiz for RedLine Stealer

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

![](https://8aqnet.cdn.bcebos.com/ddcb12877136d62baece1b38d436dc57.jpg)

Crossing the Line: Unit 42 Wireshark Quiz for RedLine Stealer

This post is also available i
*2023-8-18 21:0:25
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-174793.htm)
阅读量:36
收藏*

---

![A pictorial representation of Wireshark traffic including RedLine Stealer.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/08/Unit42-packet-analyzer-23-illustration_Orange-wo-logo.png)

This post is also available in:
[日本語 (Japanese)](https://unit42.paloaltonetworks.jp/unit-42-wireshark-%E3%82%AF%E3%82%A4%E3%82%BA-2023%E5%B9%B48%E6%9C%88-%E5%95%8F%E9%A1%8C%E7%B7%A8-%E2%88%92-redline-stealer/)

## Executive Summary

RedLine Stealer is information-stealing malware that harvests login credentials and other sensitive data from a victim's Windows host. This Wireshark quiz uses a packet capture (pcap) that “crosses a line” separating normal traffic from malicious activity. The malicious activity in this pcap is a RedLine Stealer infection from July 2023. Our pcap provides experience analyzing RedLine traffic, and we can determine what specific data was stolen from an infected Windows computer.

Anyone can participate in this quiz. To get the most benefit, participants should be familiar with Wireshark. This quiz also requires a basic understanding of IPv4 traffic. To help people gain this knowledge, we have [a series of Wireshark tutorials](https://unit42.paloaltonetworks.com/wireshark-workshop-videos/) available.

Palo Alto Networks customers receive protection from RedLine Stealer and other malware through [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and our [Next-Generation Firewall (NGFW)](https://docs.paloaltonetworks.com/ngfw) with [Cloud-Delivered Security Services (CDSS)](https://docs.paloaltonetworks.com/cdss) that includes [WildFire](https://docs.paloaltonetworks.com/wildfire) and [Advanced Threat Prevention](https://docs.paloaltonetworks.com/advanced-threat-prevention/administration).

| **Related Unit 42 Topics** | [**pcap**](https://unit42.paloaltonetworks.com/tag/pcap/)**,** [**RedLine**](https://unit42.paloaltonetworks.com/tag/redline/)**,** [**RedLine Stealer**](https://unit42.paloaltonetworks.com/tag/redline-stealer/)**,** [**Wireshark**](https://unit42.paloaltonetworks.com/tag/wireshark/)**,** [**Wireshark Tutorial**](https://unit42.paloaltonetworks.com/tag/wireshark-tutorial/) |
| --- | --- |

## Table of Contents

[Scenario](#post-129632-_wven14kmgum2)

## Scenario

Traffic for this quiz occurred in an Active Directory (AD) environment during July 2023. Details of the local area network (LAN) environment for the pcap follow.

### **Local Area Network (LAN) Details**

* LAN segment range: 10.7.10[.]0/24 (10.7.10[.]1 through 10.7.10[.]255)
* Domain: coolweathercoat[.]com
* Domain controller IP address: 10.7.10[.]9
* Domain controller hostname: WIN-S3WT6LGQFVX
* LAN segment gateway: 10.7.10[.]1
* LAN segment broadcast address: 10.7.10[.]255

### **Quiz Questions**

* What is the date and time in UTC the infection started?
* What is the IP address of the infected Windows client?
* What is the MAC address of the infected Windows client?
* What is the hostname of the infected Windows client?
* What is the user account name from the infected Windows host?
* What type of information did this RedLine Stealer try to steal?

## Requirements

Participants should use Wireshark to review the pcap. We encourage people to customize their Wireshark column display before reviewing the traffic. While you should personalize Wireshark according to your specific needs, we recommend starting with changes demonstrated in our [Unit 42 series of tutorials and videos](https://unit42.paloaltonetworks.com/wireshark-workshop-videos/).

Participants should use the [latest version of Wireshark](https://www.wireshark.org/download.html) if possible, due to its feature updates and bug fixes over previous versions. We do not recommend outdated Wireshark versions like 1.x and 2.x for these quizzes.

Infection traffic often contains malware or malicious code targeting Microsoft Windows. Because of this, we recommend using Wireshark in a non-Windows environment to review the pcap for this quiz. Operating systems like BSD, Linux or macOS provide an ideal environment for Wireshark when reviewing traffic from Windows-based malware like RedLine Stealer.

## Accessing the Pcap

The pcap for this quiz is located in our [GitHub repository](https://github.com/pan-unit42/Wireshark-quizzes/) as shown in Figure 1. Download the ZIP archive named 2023-07-Unit42-Wireshark-quiz.pcap.zip as shown in Figure 2. Use *infected* as the password to unlock the ZIP archive as shown in Figure 3.

![Image 1 is a screenshot of the GitHub repository for the Unit 42 Wireshark quizzes. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/08/word-image-129632-1.jpeg)

Figure 1. Our GitHub repository for Unit 42 Wireshark quizzes.

![Image 2 is a screenshot of how to download the zip file of material for the quiz. After clicking the “View raw” link on the GitHub page, this will prompt a download of the zip archive. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/08/word-image-129632-2.jpeg)

Figure 2. After selecting the pcap, download it from the GitHub repository.

![Image 3 is a screenshot of how to extract the zip file contents from the zip. From the downloads window, the user can select “Extract Here” and enter the password into the “Password required” window. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/08/word-image-129632-3.jpeg)

Figure 3. Extracting the pcap from the downloaded ZIP archive.

## Conclusion

RedLine Stealer is one of many information stealers within our current threat landscape. This Wireshark quiz can help participants better understand network traffic associated with a RedLine Stealer infection.

The answers to the Unit 42 Wireshark quiz for RedLine Stealer will be published in a separate post.

Palo Alto Networks customers receive protection from RedLine Stealer and other malware through [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and our [NGFW](https://docs.paloaltonetworks.com/ngfw) with [CDSS](https://docs.paloaltonetworks.com/cdss) that includes [WildFire](https://docs.paloaltonetworks.com/wildfire) and [Advanced Threat Prevention](https://docs.paloaltonetworks.com/advanced-threat-prevention/administration).

If you think you might have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

* North America Toll-Free: 866.486.4842 (866.4.UNIT42)
* EMEA: +31.20.299.3130
* APAC: +65.6983.8730
* Japan: +81.50.1790.0200

Palo Alto Networks has shared these findings, including file samples and indicators of compromise, with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://www.cyberthreatalliance.org).

## Additional Resources

* [Wireshark Tutorial: Wireshark Workshop Videos Now Available](https://unit42.paloaltonetworks.com/wireshark-workshop-videos/) – Unit 42, Palo Alto Networks
* [Unit 42 Wireshark Quiz, January 2023](https://unit42.paloaltonetworks.com/january-wireshark-quiz/) – Unit 42, Palo Alto Networks
* [Answers to January 2023 Unit 42 Wireshark Quiz](https://unit42.paloaltonetworks.com/january-wireshark-quiz-answers/) – Unit 42, Palo Alto Networks
* [Unit 42 Wireshark Quiz, February 20...