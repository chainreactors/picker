---
title: Unit 42 Wireshark Quiz, January 2023
url: https://buaq.net/go-146351.html
source: unSafe.sh - 不安全
date: 2023-01-21
fetch_date: 2025-10-04T04:27:13.849137
---

# Unit 42 Wireshark Quiz, January 2023

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

![](https://8aqnet.cdn.bcebos.com/a88846b638ed32486db8a5b891416f95.jpg)

Unit 42 Wireshark Quiz, January 2023

This post is also available i
*2023-1-20 22:0:39
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-146351.htm)
阅读量:46
收藏*

---

![The text Wireshark Quiz in orange set across a screenshot of the Wireshark program.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/01/image2-1.jpg)

This post is also available in:
[日本語 (Japanese)](https://unit42.paloaltonetworks.jp/january-wireshark-quiz/)

## Executive Summary

Welcome to the January 2023 Unit 42 Wireshark quiz. This blog presents a packet capture (pcap) of malicious activity and asks questions based on information derived from the network traffic. A separate Unit 42 blog post will present the answers with detailed explanations.

These quizzes are designed for security professionals who investigate suspicious network activity, but anyone can participate. To get the most benefit, readers should understand basic network traffic concepts and be somewhat familiar with [Wireshark](https://www.wireshark.org/).

The material provides experience reviewing real-world traffic from a live environment.

| **Related Unit 42 Topics** | [**AgentTesla**](https://unit42.paloaltonetworks.com/category/AgentTesla/)**,** [**OriginLogger**](https://unit42.paloaltonetworks.com/category/OriginLogger/)**,** [**pcap**](https://unit42.paloaltonetworks.com/category/pcap/)**,** [**Wireshark**](https://unit42.paloaltonetworks.com/category/Wireshark/)**,** [**Wireshark Tutorial**](https://unit42.paloaltonetworks.com/category/wireshark-tutorial/) |
| --- | --- |

## Table of Contents

[Background](#post-126652-_wven14kmgum2)

## Background

Earlier this month, Palo Alto Networks Unit 42 tweeted about Agent Tesla-style activity from a possible OriginLogger infection that was found Thursday, Jan. 5, 2023. [The original tweet](https://twitter.com/Unit42_Intel/status/1611379660029366273) contains our initial analysis. You can also find further information on the [associated malware binary](https://forensicitguy.github.io/net-downloader-originlogger/).

![Image 1 is a flow chart showing the Agent Tesla variant infection, starting with malspam. It shows the circuitous route the loader.exe takes depending on the victim’s actions. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/01/word-image-126652-2.jpeg)

Figure 1. Flow chart for the Agent Tesla variant infection.

For this month’s exercise, we generated a pcap of network traffic from this malware sample. Post-infection activity contains unencrypted SMTP traffic with data stolen from the infected computer.

## Requirements

Our analysis requires [Wireshark](https://www.wireshark.org/), a well-known tool used to review pcaps. However, its default settings are not optimized for web-based malware traffic. Therefore, we encourage people to customize Wireshark after installing it. To help, Unit 42 has published [a series of tutorials and videos](https://unit42.paloaltonetworks.com/wireshark-workshop-videos/) that include customizing Wireshark.

We recommend using the latest 3.x version of Wireshark, since it has more features, capabilities and bug fixes over previous Wireshark versions.

Furthermore, we recommend using a non-Windows environment like BSD, Linux or macOS to analyze malicious traffic. The pcap for this quiz contains HTTP traffic of an obfuscated binary. If decoded, this binary becomes a malicious DLL file, as previously noted in the [indicators for this infection posted on Github](https://github.com/pan-unit42/tweets/blob/master/2023-01-05-IOCs-from-Agent-Tesla-variant-infection.txt). The decoded malware presents a risk of infection when using a Windows computer.

## Quiz Material

To obtain the pcap for this month’s quiz, visit our [Github repository](https://github.com/pan-unit42/Wireshark-quizzes/blob/main/2023-01-Unit42-Wireshark-quiz.pcap.zip). Download the ZIP archive and extract the pcap as shown below in Figures 2 and 3. Use ***infected*** as the password to unlock the ZIP archive.

![Figure 2. Download the ZIP archive containing the pcap from our Github repository.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/01/word-image-126652-3.jpeg)

Figure 2. Download the ZIP archive containing the pcap from our Github repository.

![Image 3 is a screenshot of two windows showing the Wireshark-quizzes Github, demonstrating how to extract the zip archive containing pcap. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/01/word-image-126652-4.jpeg)

Figure 3. Extract the pcap file from the password-protected ZIP archive.

## Quiz Questions

When did this activity first occur? Format your answer as Universal Coordinated Time (UTC). When sharing threat intelligence, UTC ensures recipients understand the exact time regardless of time zone.

Can you identify the infected host? For a Windows computer, the basic identifiers are the following:

* Victim’s IP address
* Victim’s MAC address
* Victim’s Windows host name
* Victim’s WIndows user account name

This month, our infected host is a stand-alone Windows client. In addition to Windows system traffic, the pcap also contains unencrypted SMTP traffic generated by the malware. This traffic contains additional information, so we can determine all four of the above identifiers.

The SMTP traffic includes various login credentials from the infected host. Of note, this traffic does ***not*** contain legitimate credentials. We populated the host with fake login data before we ran the malware. Despite the fake data, this traffic provides a better understanding of data stolen by Agent Tesla variants like OriginLogger.

Review the pcap and answer the following questions for this month’s Unit 42 Wireshark quiz:

* When did the malicious traffic start in UTC?
* What is the victim’s IP address?
* What is the victim’s MAC address?
* What is the victim’s Windows host name?
* What is the victim’s Windows user account name?
* How much RAM does the victim’s host have?
* What type of CPU is used by the victim’s host?
* What is the public IP address of the victim’s host?
* What type of account login data was stolen by the malware?

## Conclusion

Palo Alto Networks encourages members of the security community to develop their skills, so we can all better protect our digital way of life. This month’s Wireshark quiz can help participants accomplish that goal.

The answers to this month’s Unit 42 Wireshark quiz will be published in a separate blog post on Monday, Jan. 23.

Palo Alto Networks customers receive protections from Agent Tesla variants like OriginLogger through [Cortex XDR](https://www.paloaltonetworks.com/cortex/cortex-xdr) and our [Next-Generation Firewall](https://www.paloaltonetworks.com/network-security/next-generation-firewall) with [cloud-delivered security services](https://www.paloaltonetworks.com/network-security/security-subscriptions) including [WildFire](https://www.paloaltonetworks.com/network-security/wildfire) and [Advanced Threat Prevention](https://www.paloaltonetworks.com/network-security/advanced-threat-prevention).

If you think you may have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

* North America Toll-Free: 866.486.4842 (866.4.UNIT42)
* EMEA: +31.20.299.3130
* APAC: +65.6983.8730
* Japan: +81.50.1790.0200

## Additional Resources

[Wireshark Tutorial: Wireshark Workshop Videos Now Available](https://unit42.paloaltonetworks.com/wireshark-workshop-videos/) – Unit 42, Palo Alto Networks

#### Get updates from Pa...