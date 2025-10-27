---
title: Answers to Unit 42 Wireshark Quiz, January 2023
url: https://buaq.net/go-146546.html
source: unSafe.sh - 不安全
date: 2023-01-24
fetch_date: 2025-10-04T04:36:58.237281
---

# Answers to Unit 42 Wireshark Quiz, January 2023

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

![](https://8aqnet.cdn.bcebos.com/f29daf1f5cf3e68e86df56a7e9215d56.jpg)

Answers to Unit 42 Wireshark Quiz, January 2023

This post is also available i
*2023-1-23 22:0:56
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-146546.htm)
阅读量:35
收藏*

---

![The text Wireshark Quiz in orange set across a screenshot of the Wireshark program.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/01/image2-1.jpg)

This post is also available in:
[日本語 (Japanese)](https://unit42.paloaltonetworks.jp/january-wireshark-quiz-answers/)

## Executive Summary

This blog presents the answers for our [January 2023 Unit 42 Wireshark quiz](https://unit42.paloaltonetworks.com/january-wireshark-quiz/). The information is ideal for security professionals who investigate suspicious network activity, but everyone is welcome to review. To get the most benefit, readers should understand basic network traffic concepts and be familiar with [Wireshark](https://www.wireshark.org/).

If you’d like to view the version without answers, [please see the standalone quiz post](https://unit42.paloaltonetworks.com/january-wireshark-quiz/).

| **Related Unit 42 Topics** | [**AgentTesla**](https://unit42.paloaltonetworks.com/category/AgentTesla/)**,** [**OriginLogger**](https://unit42.paloaltonetworks.com/category/OriginLogger/)**,** [**pcap**](https://unit42.paloaltonetworks.com/category/pcap/)**,** [**Wireshark**](https://unit42.paloaltonetworks.com/category/Wireshark/)**,** [**Wireshark Tutorial**](https://unit42.paloaltonetworks.com/category/wireshark-tutorial/) |
| --- | --- |

## Table of Contents

[Background, Requirements and Quiz Material](#post-126670-_aerxd2yulm78)

## Background, Requirements and Quiz Material

This quiz is based on a Palo Alto Networks Unit 42 tweet about [Agent Tesla-style activity from a possible OriginLogger infection](https://twitter.com/Unit42_Intel/status/1611379660029366273) that was found Thursday, Jan. 5, 2023. Figure 1 provides a chain of events from the infection.

![Image 1 is a flow chart showing the Agent Tesla variant infection, starting with malspam. It shows the circuitous route the loader.exe takes depending on the victim’s actions. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/01/word-image-126670-2.jpeg)

Figure 1. Flow chart for the Agent Tesla variant infection.

Our investigation for this month’s quiz requires [Wireshark](https://www.wireshark.org/). This blog utilizes a recent version of Wireshark, and we recommend Wireshark version 3.x. We also use the [Thunderbird email client](https://www.thunderbird.net/) to review an email extracted from the packet capture (pcap).

Participants should have some basic knowledge of network traffic fundamentals. We also recommend readers customize their Wireshark display to better analyze web traffic. [A list of tutorials and videos is available](https://unit42.paloaltonetworks.com/wireshark-workshop-videos/). As always, we recommend using Wireshark in a non-Windows environment like BSD, Linux or macOS when analyzing malicious Windows-based traffic.

To obtain the pcap, [visit our Github repository](https://github.com/pan-unit42/Wireshark-quizzes/blob/main/2023-01-Unit42-Wireshark-quiz.pcap.zip). Download the ZIP archive and extract the pcap. Use ***infected*** as the password to unlock the ZIP archive.

## Quiz Questions

The Unit 42 Wireshark quiz for January 2023 has the following questions:

* When did the malicious traffic start in UTC?
* What is the victim’s IP address?
* What is the victim’s MAC address?
* What is the victim’s Windows host name?
* What is the victim’s Windows user account name?
* How much RAM does the victim’s host have?
* What type of CPU is used by the victim’s host?
* What is the public IP address of the victim’s host?
* What type of account login data was stolen by the malware?

## Quiz Answers

The answers for our January 2023 Unit 42 Wireshark quiz are:

* The malicious traffic started 2023-01-05 at 22:51 UTC
* Victim’s IP address: 192.168.1[.]27
* Victim’s MAC address: bc:ea:fa:22:74:fb
* Victim’s Windows host name: DESKTOP-WIN11PC
* Victim’s Windows user account name: windows11user
* Amount of victim’s RAM on victim’s host: 32 MB
* Victim’s CPU: Intel(R) Core(TM) i5-13600K
* Victim’s public IP address: 173.66.46[.]112
* Type of stolen account data: email and web accounts

## Pcap Analysis

Our analysis assumes you have customized Wireshark [according to our tutorials or workshop videos](https://unit42.paloaltonetworks.com/wireshark-workshop-videos/).

Analyzing the pcap requires a basic knowledge of network traffic. You should understand that a router acts as a gateway between public-facing IP addresses and hosts within an internal network.

Participants should recognize internal, non-routable IPv4 addresses. We commonly find one of three classes for non-routable internal IPv4 addresses behind an internet router:

* Class A: 10.0.0[.]0/8 (10.0.0[.]0 through 10.255.255[.]255)
* Class B: 172.16.0[.]0/12 (172.16.0[.]0 through 172.31.255[.]255)
* Class C: 192.168.0[.]0/16 (192.168.0[.]0 through 192.168.255[.]255)

In most pcaps, the victim’s IP address is from the internal network. For this month’s pcap, our victim is using a Class C non-routable IP address in the 192.168.0[.]0/16 range.

How do we find the victim’s IP address? Use the basic web filter provided in our Wireshark tutorials, or type the following in your Wireshark filter bar:

http.request or tls.handshake.type eq 1

In the frame details panel for any frame listed in the column display, the source IP address should be 192.168.1[.]27. The frame details also provide a MAC address that corresponds to 192.168.1[.]27 as shown below in Figure 2.

![Image 2 is a screenshot of the Wireshark program. Highlighted in boxes and with arrows are the victim’s IP address and MAC address in the program.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/01/word-image-126670-3.jpeg)

Figure 2. Finding the victim’s IP address and MAC address in Wireshark.

In some pcap files, NBNS or SMB traffic provides a victim’s Windows host name. Use the following filter in Wireshark:

nbns or smb or smb2

The default host name for a Windows 10 and Windows 11 computer is a 15 character string. The name starts with DESKTOP- and is followed by an alpha-numeric string of seven additional ASCII characters. In Figure 3, we find DESKTOP-WIN11PC in the frame details from one of the frames in the column display.

![Image 4 is a screenshot of the Wireshark program. This shows the SMB traffic from the cpap. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/01/word-image-126670-4.jpeg)

Figure 3. Finding the victim’s Windows host name in Wireshark.

Please note that threat actors often abuse legitimate products and operating system features for malicious purposes. This does not necessarily imply a flaw or malicious quality to the legitimate software being abused.

The remaining information for this quiz is from stolen data in the unencrypted SMTP traffic. Type smtp in your Wireshark filter. The results reveal several frames as shown below in Figure 4.

![Image 4 is a screenshot of the Wireshark program. This shows the SMTP traffic from the cpap. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/01/word-image-126670-5.jpeg)

Figure 4. Finding SMTP traffic from the pcap in Wireshark.

These frames represent a single TCP stream of traffic. Follow the TCP stream to review the associated email as shown in Figures 5 and 6.

![Image 5 is a screenshot of the Wireshark program. Arrows highlight menu windows that show how to follow a single TCP stream.](https://un...