---
title: Ransom Cartel Ransomware: A Possible Connection With REvil
url: https://buaq.net/go-130907.html
source: unSafe.sh - 不安全
date: 2022-10-15
fetch_date: 2025-10-03T19:54:59.215674
---

# Ransom Cartel Ransomware: A Possible Connection With REvil

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

![](https://8aqnet.cdn.bcebos.com/5d4d0e02299300ff9289d6683ba0d847.jpg)

Ransom Cartel Ransomware: A Possible Connection With REvil

Executive SummaryRansom Cart
*2022-10-14 21:0:26
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-130907.htm)
阅读量:39
收藏*

---

![Ransomware conceptual image, covering threat actors such as Ransom Cartel](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/Unit42-ransomware-21-illustration_yellow.png)

## Executive Summary

Ransom Cartel is ransomware as a service (RaaS) that surfaced in mid-December 2021. This ransomware performs [double extortion](https://www.paloaltonetworks.com/blog/2022/03/ransomware-trends-demands-dark-web-leak-sites/) attacks and exhibits several similarities and technical overlaps with REvil ransomware. REvil ransomware disappeared just a couple of months before Ransom Cartel surfaced and just one month after 14 of its alleged members were [arrested in Russia](https://www.washingtonpost.com/world/2022/01/14/russia-hacker-revil/). When Ransom Cartel first appeared, it was unclear whether it was a rebrand of REvil or an unrelated threat actor who reused or mimicked REvil ransomware code.

In this report, we will provide our analysis of Ransom Cartel ransomware, as well as our assessment of the possible connections between REvil and Ransom Cartel ransomware.

Palo Alto Networks customers receive help with the detection and prevention of Ransom Cartel ransomware through the following products and services: [Cortex XDR](https://www.paloaltonetworks.com/cortex/cortex-xdr) and [Next-Generation Firewalls](https://www.paloaltonetworks.com/network-security/next-generation-firewall) (including [cloud-delivered security services](https://www.paloaltonetworks.com/network-security/security-subscriptions) such as [WildFire)](https://www.paloaltonetworks.com/network-security/next-generation-firewall).

If you think a cyber incident may have impacted you, the [Unit 42 Incident Response team](https://www.paloaltonetworks.com/unit42/respond/incident-response) is available 24/7/365. You can also take preventative steps by requesting any of our [cyber risk management services](https://www.paloaltonetworks.com/unit42/assess).

Indicators of compromise and Ransom Cartel-associated tactics, techniques and procedures (TTPs) can be found in the [Ransom Cartel ATOM](https://unit42.paloaltonetworks.com/atoms/ransom-cartel/).

## Table of Contents

[History of REvil Disappearance and Possible Connection With Ransom Cartel](#post-125298-_77hssf93mxs)

## History of REvil Disappearance and Possible Connection With Ransom Cartel

In October 2021, REvil operators went quiet. REvil’s dark web leak site and the chat feature used for communication between the threat actors and their targets became unreachable. Around mid-April 2022, the REvil blog (“Happy Blog”) [became active again](https://unit42.paloaltonetworks.com/revil-threat-actors/) and began redirecting visitors to a new name-and-shame blog for an operation identified as Ransom Cartel.

At the start of the redirect, no breached organizations were listed on the site. Over time, the threat actors began adding records that had appeared on “Happy Blog,” mostly from late April to October 2021. They also included the old file-sharing links previously used by REvil as proof of compromise.

The newly established blog operated by Ransom Cartel listed Tox Chat ID for communication with the ransomware operator. The blog hinted at Ransom Cartel’s connection to REvil with the claim that the newer group offered “the same, yet improved software” (referring to a new Ransom Cartel variant).

To read more about REvil and its disappearance and possible return, please refer to our blog, [Understanding REvil](https://unit42.paloaltonetworks.com/revil-threat-actors/).

## Ransom Cartel Overview

Ransom Cartel was first observed in mid-December 2021, and it first posted the names of organizations it claimed to have breached around late April 2022. Since then, Unit 42 has observed the group claiming to have breached additional organizations in the U.S. and France, including in the following industries: Education, Manufacturing, and Utilities and Energy. Unit 42 incident responders have also assisted clients with response efforts in several Ransom Cartel cases.

Like many other ransomware gangs, Ransom Cartel leverages double extortion techniques. Unit 42 has observed the group taking an aggressive approach, threatening not only to publish stolen data to their leak site, but also to send it to the victim’s partners, competitors and the news in an effort to inflict reputational damage.

Ransom Cartel typically gains initial access to an environment via compromised credentials, which is one of the most common vectors for initial access for ransomware operators. This includes access credentials for external remote services, remote desktop protocol (RDP), secure shell protocol (SSH) and virtual private networks (VPNs). These credentials are widely available in the cyber underground and offer threat actors a reliable means to gain access to victims' corporate networks.

These credentials can also be obtained through the work of ransomware operators themselves or by purchasing them from an initial access broker.

Initial access brokers are actors who offer to sell compromised network access. Their motivation is not to carry out cyberattacks themselves but rather to sell the access to other threat actors. Due to the profitability of ransomware, these brokers likely have working relationships with RaaS groups based on the amount they are willing to pay.

Unit 42 has seen evidence that Ransom Cartel has relied on this type of service to gain initial access for ransomware deployment.

Unit 42 has also observed Ransom Cartel encrypting both Windows and Linux VMWare ESXi servers in attacks on corporate networks.

### Tactics, Techniques and Procedures Observed During Ransom Cartel Attacks

Unit 42 observed a Ransom Cartel threat actor using a tool called [DonPAPI](https://github.com/login-securite/DonPAPI), which has not been observed in past incidents. This tool can locate and retrieve Windows Data Protection API (DPAPI) protected credentials, which is known as DPAPI dumping.

DonPAPI is used to search machines for certain files known to be DPAPI blobs, including Wi-Fi keys, RDP passwords, credentials saved in web browsers, etc. To avoid the risk of detection by antivirus (AVs) or endpoint detection and response (EDR), the tool downloads the files and decrypts them locally. To compromise Linux ESXi devices, Ransom Cartel uses DonPAPI to harvest credentials stored in web browsers used to authenticate to the vCenter web interface.

We also observed the threat actor using additional tools, including LaZagne to recover credentials stored locally and Mimikatz to steal credentials from host memory.

In order to establish persistent access to Linux ESXi devices, the threat actor enables SSH after authenticating to vCenter. The threat actor will create new accounts and sets the account’s user identifier (UID) to zero. For Unix/Linux users, a UID=0 is root. This means any security checks are bypassed.

The threat actor was observed downloading and using a cracked version of a legitimate tool called PDQ Inventory, which is a legitimate system management solution that IT administrators use to scan their network and collect hardware, software and Windows configuration data. Ransom Cartel used this as a remote access tool to establish an interactive command and control channel and to scan the compromised network.

Once a VMware ESXi server is compromised, the th...