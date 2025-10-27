---
title: Answers to Unit 42 Wireshark Quiz, February 2023
url: https://buaq.net/go-151251.html
source: unSafe.sh - 不安全
date: 2023-02-28
fetch_date: 2025-10-04T08:13:46.896562
---

# Answers to Unit 42 Wireshark Quiz, February 2023

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

![](https://8aqnet.cdn.bcebos.com/bec2f88aa2ed2f34b25d4e9d677c4636.jpg)

Answers to Unit 42 Wireshark Quiz, February 2023

Executive SummaryThis blog p
*2023-2-27 22:0:23
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-151251.htm)
阅读量:37
收藏*

---

![A pictorial representation of packet capture. It also includes the Unit 42 and Palo Alto Networks logos.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/02/Unit42-packet-analyzer-23-illustration_Yellow.png)

## Executive Summary

This blog presents the answers for our [February 2023 Unit 42 Wireshark quiz](https://unit42.paloaltonetworks.com/feb-wireshark-quiz/). The information is ideal for security professionals who investigate suspicious network activity in an Active Directory (AD) environment, but everyone is welcome to review. To get the most benefit, readers should understand basic network traffic concepts and be familiar with [Wireshark](https://www.wireshark.org/).

If you’d like to view the version without answers, please see [the standalone quiz post](https://unit42.paloaltonetworks.com/feb-wireshark-quiz/).

## Table of Contents

[Scenario, Requirements and Quiz Material](#post-127019-_ob2qe7xczcog)

## Scenario, Requirements and Quiz Material

The pcap for this month’s Wireshark quiz is from an AD environment, and it contains real-world traffic from a simulated enterprise setting. Details of the local area network (LAN) from the pcap follow.

* LAN segment range: 10.0.0[.]0/24 (10.0.0[.]0 through 10.0.0[.]255)
* Domain: work4us[.]org
* Domain Controller IP address: 10.0.0[.]6
* Domain Controller host name: WORK4US-DC
* LAN segment gateway: 10.0.0[.]1
* Land segment broadcast address: 10.0.0[.]255

Our investigation for this month’s quiz requires [Wireshark](https://www.wireshark.org/). This blog utilizes a recent version of Wireshark, and we recommend at least version 3.x.

Participants should have some basic knowledge of network traffic fundamentals. We also recommend readers customize their Wireshark display to better analyze web traffic. [A list of tutorials and videos is available](https://unit42.paloaltonetworks.com/wireshark-workshop-videos/). As always, we recommend using Wireshark in a non-Windows environment like BSD, Linux or macOS when analyzing malicious Windows-based traffic.

To obtain the pcap, [visit our GitHub repository](https://github.com/pan-unit42/Wireshark-quizzes/blob/main/2023-02-Unit42-Wireshark-quiz.pcap.zip). Download the ZIP archive and extract the pcap. Use *infected* as the password to unlock the ZIP archive.

## Quiz Questions

This month’s Wireshark quiz asks participants to write an incident report on the activity, as described in [the February 2023 standalone quiz post](https://unit42.paloaltonetworks.com/feb-wireshark-quiz/). The incident report should consist of three sections:

* **Executive Summary:** State in simple, direct terms what happened (when, who and what).
* **Victim Details:** Victim’s IP address, MAC address, Windows hostname and Windows user account name.
* **Indicators of Compromise (IoCs):** IP addresses, ports, domains and URLs associated with the infection. SHA256 hashes if any files from the infection can be extracted from the pcap.

## Quiz Answers

The incident report should look similar to the following write-up.

Executive Summary:

On 2023-02-03 at 17:04 UTC, a Windows computer used by Damon Bauer was infected with Qakbot (Qbot) malware. The Qakbot infection may have spread to the domain controller.

Victim Details:

* IP address: 10.0.0[.]149
* MAC address: 00:21:5d:9e:42:fb
* Host name: DESKTOP-E7FHJS4
* Windows user account: damon.bauer

IoCs:

Malicious network traffic

* Port 80 - hxxp://128.254.207[.]55/86607.dat
* 102.156.32[.]143:443 - HTTPS/SSL/TLS traffic
* 208.187.122[.]74:443 - HTTPS/SSL/TLS traffic
* 5.75.205[.]43:443 - HTTPS/SSL/TLS traffic
* 23.111.114[.]52:65400 - TCP traffic
* 78.31.67[.]7:443 - TCP traffic for VNC activity
* Various IP addresses over TCP ports 25 and 465 - SMTP traffic to servers on various email domains
* ARP scanning from the infected Windows host
* File transfer over SMB between the infected Windows host and the domain controller

Malware:

* SHA256 hash: 713207d9d9875ec88d2f3a53377bf8c2d620147a4199eb183c13a7e957056432
* File size: 1,761,280 bytes
* File location: hxxp://128.254.207[.]55/86607.dat
* File description: Malicious 32-bit DLL for Qakbot
* Run method: rundll32.exe *[filename]*,Wind
* Sample available at [MalwareBazaar](https://bazaar.abuse.ch/sample/713207d9d9875ec88d2f3a53377bf8c2d620147a4199eb183c13a7e957056432/).

## Pcap Analysis: Victim Details

Our analysis assumes you have customized Wireshark [according to our tutorials or workshop videos](https://unit42.paloaltonetworks.com/wireshark-workshop-videos/).

First, determine the victim’s details.

The common internal, non-routable IP address from this pcap is 10.0.0[.]149. To find it, use the basic web filter provided in our Wireshark tutorials, or type the following in your Wireshark filter bar:

(http.request or tls.handshake.type eq 1) and !(ssdp)

The results in the column display should show the source IP address as 10.0.0[.]149. The frame details section provides a corresponding MAC address of 00:21:5d:9e:42:fb as shown in Figure 1.

![Image 1 is a screenshot of Wireshark that highlights the source IP column (Src), the source MAC address when filtering the web traffic. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/02/word-image-127019-2.jpeg)

Figure 1. Filtering on web traffic to find the victim’s IP and MAC address.

Network Basic Input/Output System (NetBIOS) Name Service (NBNS) traffic or Server Message Block (SMB) traffic may also provide a victim’s Windows host name. Use the following filter in Wireshark:

nbns or smb or smb2

The default host name for a Windows 10 or Windows 11 computer is a 15-character string. The name starts with DESKTOP- and is followed by an alphanumeric string of seven additional ASCII characters. We find DESKTOP-E7FHJS4 in the column display and frame details as shown in Figure 2.

![Image 2 is a screenshot of Wireshark showing how to find the Windows host name in the traffic, highlighted with arrows. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/02/word-image-127019-3.jpeg)

Figure 2. Finding a Windows host name in NBNS or SMB traffic.

Kerberos authentication traffic generated when a user logs in may provide a Windows user account name in the pcap. Filter on kerberos.CNameString and scroll to the end of the results in your column display. Select one of the last few frames in the column display. Go to the frame details section and expand the Kerberos line. Keep expanding values until you find the CNameString that has a value of damon.bauer, as shown in Figure 3.

![Image 3 is a screenshot of Wireshark highlighting the CNameString column, showing how to find the victim’s Window user account name in the Kerberos traffic.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/02/word-image-127019-4.jpeg)

Figure 3. Finding the victim’s Windows user account name in Kerberos traffic.

As stated in our [tutorial on identifying hosts and users](https://unit42.paloaltonetworks.com/using-wireshark-identifying-hosts-and-users/), you can select the CNameString value and apply it as a column in your Wireshark display. The result is a CNameString column as shown above in Figure 3.

## Pcap Analysis: Identifying the Malware

After gathering the victim’s details, determine when the malicious traffic started. First, check unencrypted HTTP traffic for any unusual URLs. Modify our basic web filter by removing tls...