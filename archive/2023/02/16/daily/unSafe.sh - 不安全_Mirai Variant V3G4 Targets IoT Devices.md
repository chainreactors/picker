---
title: Mirai Variant V3G4 Targets IoT Devices
url: https://buaq.net/go-149546.html
source: unSafe.sh - 不安全
date: 2023-02-16
fetch_date: 2025-10-04T06:44:51.033629
---

# Mirai Variant V3G4 Targets IoT Devices

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

![](https://8aqnet.cdn.bcebos.com/44fd35a94efa5b63183da2bd2d558a09.jpg)

Mirai Variant V3G4 Targets IoT Devices

This post is also available i
*2023-2-15 22:0:28
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-149546.htm)
阅读量:67
收藏*

---

![A pictorial representation of the Mirai Variant V3G4](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/02/Unit42-blog-2by1-characters-r4d1-2020_New-mirai-variant-v3.png)

This post is also available in:
[日本語 (Japanese)](https://unit42.paloaltonetworks.jp/mirai-variant-v3g4/)

## Content Warning

We are providing a content warning because the following contains usage of a racial slur by a threat actor, which is not condoned in any instance by Unit 42. Unit 42 has partially redacted the racial slur to provide researchers with the ability to identify it and check IoCs as needed.

## Executive Summary

From July to December 2022, Unit 42 researchers observed a Mirai variant called V3G4, which was leveraging several vulnerabilities to spread itself. The vulnerabilities exploited include the following:

* [CVE-2012-4869](https://nvd.nist.gov/vuln/detail/CVE-2012-4869): FreePBX Elastix Remote Command Execution Vulnerability
* [Gitorious Remote Command Execution Vulnerability](https://www.exploit-db.com/exploits/18393)
* [CVE-2014-9727](https://nvd.nist.gov/vuln/detail/CVE-2014-9727): FRITZ!Box Webcam Remote Command Execution Vulnerability
* [Mitel AWC Remote Command Execution Vulnerability](https://www.exploit-db.com/exploits/15807)
* [CVE-2017-5173](https://nvd.nist.gov/vuln/detail/CVE-2017-5173): Geutebruck IP Cameras Remote Command Execution Vulnerability
* [CVE-2019-15107](https://nvd.nist.gov/vuln/detail/cve-2019-15107): Webmin Command Injection Vulnerability
* [Spree Commerce Arbitrary Command Execution Vulnerability](https://web.archive.org/web/20110726024546/http%3A//www.spreecommerce.com/blog/2011/04/19/security-fixes/)
* [FLIR Thermal Camera Remote Command Execution Vulnerability](https://www.exploit-db.com/exploits/42788)
* [CVE-2020-8515:](https://nvd.nist.gov/vuln/detail/CVE-2020-8515) DrayTek Vigor Remote Command Execution Vulnerability
* [CVE-2020-15415](https://nvd.nist.gov/vuln/detail/CVE-2020-15415): DrayTek Vigor Remote Command Injection Vulnerability
* [CVE-2022-36267](https://nvd.nist.gov/vuln/detail/CVE-2022-36267): Airspan AirSpot Remote Command Execution Vulnerability
* [CVE-2022-26134](https://nvd.nist.gov/vuln/detail/CVE-2022-26134): Atlassian Confluence Remote Code Execution Vulnerability
* [CVE-2022-4257](https://nvd.nist.gov/vuln/detail/CVE-2022-4257): C-Data Web Management System Command Injection Vulnerability

Once the vulnerable devices are compromised, they will be fully controlled by attackers and become a part of the botnet. The threat actor has the capability to utilize those devices to conduct further attacks, such as distributed denial-of-service (DDoS) attacks. The exploit attempts captured by Unit 42 researchers leverage the aforementioned vulnerabilities to spread V3G4, which targets exposed servers and networking devices running Linux.

Palo Alto Networks [Next-Generation Firewall](https://www.paloaltonetworks.com/network-security/next-generation-firewall) customers receive protections through [cloud-delivered security services](https://www.paloaltonetworks.com/network-security/security-subscriptions) such as [IoT Security](https://www.paloaltonetworks.com/network-security/smart-devices-smarter-iot-security?utm_source=google-jg-amer-cdss&utm_medium=paid_search&utm_term=palo%20alto%20networks%20iot%20security&utm_campaign=google-cdss-iot_security-amer-ca-awareness-en&utm_content=gs-19633824690-151442986731-646705931499&sfdcid=7014u000001hHCRAA2&gclid=EAIaIQobChMI1Lm26OmS_QIVQUNyCh1G3gKWEAAYASAAEgJ3KvD_BwE), [Advanced Threat Prevention](https://www.paloaltonetworks.com/network-security/advanced-threat-prevention), [WildFire](https://www.paloaltonetworks.com/network-security/advanced-wildfire), and [Advanced URL Filtering](https://www.paloaltonetworks.com/network-security/advanced-url-filtering), which can help detect and block the exploit traffic and malware.

## Table of Contents

[Content Warning](#post-126924-_ruyyl6wo0i0m)

## Campaign Overview

Since July 2022, Unit 42 researchers have observed three campaigns utilizing the Mirai V3G4 variant. Based on our analysis, we believe the campaigns were operated by the same threat actor for the following reasons:

* The hardcoded command and control (C2) domains among these three campaigns contain the same string (8xl9)
* The malware shell script downloaders are almost identical between the three campaigns
* The botnet client samples use the same XOR decryption key
* The botnet client samples use the same “stop list” (a list of target processes that the botnet client searches for and terminates)
* The botnet client samples use almost identical functions

The threat actor exploited 13 vulnerabilities that could lead to remote code execution. Upon successful exploitation, the wget and curl utilities are automatically executed to download Mirai client samples from malware infrastructure and then execute the downloaded bot clients.

The utilized vulnerabilities are listed in Figure 1 below, and the detailed vulnerability information is listed in the [Appendix](#post-126924-_ajb20h1i7fau) section.

![Image 1 is a timeline overview of the V3G4 campaign. For each of the three campaigns it lists the callback IP, the botnet C2, the month and year, and the exploited vulnerabilities. The campaigns were in July, September, and December of 2022. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/02/word-image-126924-1.png)

Figure 1. V3G4 Campaign Overview.

## V3G4 Malware Analysis

Based on behavior and patterns Unit 42 researchers observed during analysis of the downloaded botnet client samples, we believe that the botnet sample is a variant of the Mirai botnet.

Upon execution, the botnet client prints xXxSlicexXxxVEGA. to the console. The malware also contains a function that makes sure only one instance of this malware is executing on the infected device. If a botnet process already exists, the botnet client will simply print a string from the console and exit, as depicted in Figure 2.

![Image 2 is a screenshot of the botnet printing a string from the console. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/02/word-image-126924-2.png)

Figure 2. V3G4 ensures single instance execution.

The botnet client also contains a list of process names, and it tries to terminate those processes by checking the running process names on the infected host. The process names in that list belong to other botnet malware families and other Mirai variants. The full stop list is shown in Figure 3.

![Image 3 is a screenshot of the full stop list of V3G4. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/02/word-image-126924-3.png)

Figure 3. V3G4’s stop list.

The V3G4 variant tries to connect to its hardcoded C2. This activity is shown in Figure 4.

![Image 4 is a screenshot of many lines of code where the V3G4 variant is trying to connect to the hardcoded C2.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/02/word-image-126924-4.png)

Figure 4. V3G4 malware C2 domain.

Most Mirai variants use the same key for string encryption. However, this V3G4 variant uses different XOR encryption keys for different scenarios.

### **Botnet Client Execution-Related String Decryption**

For strings related to botnet client execution, this V3G4 variant will first initialize an encrypted string table. It will then retrieve the encrypted string through an index (show...