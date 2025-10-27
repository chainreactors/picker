---
title: Manic Menagerie 2.0: The Evolution of a Highly Motivated Threat Actor
url: https://buaq.net/go-170747.html
source: unSafe.sh - 不安全
date: 2023-06-29
fetch_date: 2025-10-04T11:46:38.590865
---

# Manic Menagerie 2.0: The Evolution of a Highly Motivated Threat Actor

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

![](https://8aqnet.cdn.bcebos.com/963c132bfa2ac180a18a58ef7e84aa63.jpg)

Manic Menagerie 2.0: The Evolution of a Highly Motivated Threat Actor

Executive SummaryUnit 42 res
*2023-6-28 21:0:31
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-170747.htm)
阅读量:38
收藏*

---

![A pictorial representation of a threat actor implementing cryptojacking in a campaign like Manic Menagerie 2.0](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/06/Cryptojacking-r3d3.png)

## **Executive Summary**

Unit 42 researchers discovered an active campaign that targeted several web hosting and IT providers in the United States and European Union from late 2020 to late 2022. Unit 42 [tracks the activity](https://unit42.paloaltonetworks.com/from-activity-to-formal-naming/) associated with this campaign as CL-CRI-0021 and believes it stems from the same threat actor responsible for the previous campaign known as [Manic Menagerie](https://www.cyber.gov.au/sites/default/files/2023-03/report_manic_menagerie.pdf).

The threat actor deployed coin miners on hijacked machines to abuse the compromised servers’ resources. They have further deepened their foothold in victims’ environments by mass deployment of web shells, which granted them sustained access, as well as access to internal resources of the compromised websites.

In doing so, the attackers could potentially have turned the hijacked legitimate websites – hosted by the targeted web hosting and IT providers – into command and control (C2) servers at scale, affecting thousands of web pages. The threat actor could thus run their C2 activity from legitimate websites that have good reputations, and which are not necessarily flagged by security solutions as malicious. This could have a tremendous impact on the abused legitimate websites, which would in that circumstance be made to unknowingly host malicious content and harbor criminal activity. Such criminal activity could inflict legal and/or reputational damages upon the owners of the websites or the web hosting companies.

While operating in the victims’ networks, the attackers attempted multiple techniques to evade the detection of various monitoring tools as well as active commercial cybersecurity products. They also kept executing payloads, redeploying and rerunning tools that were previously blocked, or using other similar tools. Attackers tried to stay under the radar by avoiding known malware, introducing custom tools and relying on publicly available legitimate tools.

Based on the tactics, techniques and procedures (TTPs) that we observed in this attack, the threat actor whose previous campaign was dubbed [Manic Menagerie](https://www.cyber.gov.au/sites/default/files/2023-03/report_manic_menagerie.pdf) carried out this more recently observed campaign, which we therefore call Manic Menagerie 2.0.

This threat actor was reported as active from at least 2018, targeting web hosting companies in Australia, by the [Australian Cyber Security Center](https://www.cyber.gov.au/). The name is most likely a reference to their noisy activity, plus the large number of attacked web hosting companies and different tools used by the attacker.

Palo Alto Networks customers receive protections from the threats mentioned in this article through the following products and services:

* [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and [XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM) with Local Analysis, Behavioral Threat Protection, the Cryptominers module and Analytics
* [Cloud-Delivered Security Services](https://www.paloaltonetworks.com/network-security/security-subscriptions) including [Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering/administration), [DNS Security](https://docs.paloaltonetworks.com/dns-security) and [WildFire](https://docs.paloaltonetworks.com/wildfire)
* [Managed Detection and Response](https://www.paloaltonetworks.com/cortex/managed-detection-and-response) services
* [Next-Generation Firewall](https://docs.paloaltonetworks.com/ngfw) with a Threat Prevention security subscription
* [WildFire](https://docs.paloaltonetworks.com/wildfire) cloud-delivered malware analysis service

| **Related Unit 42 Topics** | [**Cryptominers**](https://unit42.paloaltonetworks.com/tag/cryptominers/), **[Web shells](https://unit42.paloaltonetworks.com/tag/webshell/)** |
| --- | --- |

## **Table of Contents**

[Initial Access and Persistence](#post-128904-_mkf6s0gx8fix)

## **Initial Access and Persistence**

The initial foothold in the Manic Menagerie 2.0 campaign was first observed in late 2020, targeting companies in the United States and European Union. In this campaign, the threat actors gained access to target machines by exploiting vulnerable web applications and IIS servers, and deploying different web shells on these infected servers.

Deploying web shells on an active web server allows the threat actor to hijack legitimate websites. The web shells are placed on these hosted websites in the following folders on the compromised server: C:\*[hosted websites on the server path]*\wwwroot\example.com\webshell.aspx)

These actions also allow public access from outside the victim’s network in the future. This effectively allows these websites to be turned into future C2 servers for the attacker.

We also observed the same web shell, xn.aspx, mentioned in the [Australian Cyber Security Center’s (ACSC) report](https://www.cyber.gov.au/sites/default/files/2023-03/report_manic_menagerie.pdf) about the original Manic Menagerie operation targeting web host companies in Australia.

After deploying web shells in Manic Menagerie 2.0, the threat actor initiated the deployment of coin miners. This was likely done to abuse the compromised servers' powerful computing resources for the threat actor’s financial gain through coin mining.

During 2021-2022, upon the public disclosure of multiple Microsoft Exchange Server vulnerabilities, the threat actor attempted to exploit the following vulnerabilities in some targets:

* [CVE-2021-26855](https://nvd.nist.gov/vuln/detail/CVE-2021-26855), [CVE-2022-41040](https://nvd.nist.gov/vuln/detail/CVE-2022-41040): (ProxyNotShell) Exchange Server SSRF vulnerabilities
* [CVE-2021-34473](https://nvd.nist.gov/vuln/detail/cve-2021-34473): (One of the ProxyShell vulnerabilities) Exchange Server remote code execution vulnerability
* [CVE-2021-33766](https://nvd.nist.gov/vuln/detail/CVE-2021-33766): (ProxyToken) Allows an attacker to modify the configuration of mailboxes of arbitrary users

Therefore, in addition to vulnerabilities in the [IIS servers](https://blog.viettelcybersecurity.com/deep-understand-aspx-file-handling-and-some-related-attack-vector/) as well as [vulnerable web applications](https://attack.mitre.org/techniques/T1190/) in the environment, the previously mentioned vulnerabilities provided the threat actor another penetration and persistence vector. [Morphisec](https://blog.morphisec.com/proxyshellminer-campaign) recently researched a campaign where attackers used Exchange Server vulnerabilities (collectively known as ProxyShell) to drop cryptominers.

## Reconnaissance and Privilege Escalation

From late 2020, threat actors involved in the Manic Menagerie 2.0 campaign began periodically trying to execute local privilege escalation proof-of-concept (PoC) tools (detailed below) to add their own users to the Administrators group in IIS servers, to further promote their interests. When one tool failed, they would try another tool with similar functionality.

Attackers employed a runas.exe .NET wrapper called RunasCs. This publicly available to...