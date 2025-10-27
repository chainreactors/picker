---
title: Network Security Trends: November 2022-January 2023
url: https://buaq.net/go-161392.html
source: unSafe.sh - 不安全
date: 2023-05-03
fetch_date: 2025-10-04T11:38:45.700557
---

# Network Security Trends: November 2022-January 2023

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

![](https://8aqnet.cdn.bcebos.com/78df19c81e0edaedf39282fad1925c0d.jpg)

Network Security Trends: November 2022-January 2023

Executive SummaryRecent obse
*2023-5-2 21:0:3
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-161392.htm)
阅读量:40
收藏*

---

![A pictorial representation of security vulnerability trending from November 2022 to January 2023](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/05/Trends-r3d2.png)

## Executive Summary

Recent observations of exploits used in the wild November 2022-January 2023 reveal that attackers have been using newly published remote code execution vulnerabilities in the following three products:

* Roxy-WI, a web interface for managing and monitoring RoxyDNS
* CWP, a free web hosting control panel (aka Control Web Panel or CentOS Web Panel)
* Cacti, an open-source network monitoring and graphing tool used to track the performance of various network devices, servers and applications

Additionally, attackers have also been taking advantage of a traversal and information disclosure vulnerability in ThoughtWorks GoCD to read sensitive files stored on servers.

In our observations of network security trends, Unit 42 researchers have pinpointed several attacks based on proof-of-concept (PoC) availability and impact. We have detailed below which of these we believe should be on the defender’s radar.

Other insights that could assist defenders include the following:

* Rankings of the most commonly used attack techniques and the types of vulnerabilities that attackers have recently favored. For example, among 6,169 newly published vulnerabilities, a large portion (almost 11%) involves cross-site scripting.
* Lists of major vulnerabilities identified by evaluating more than 276 million attack sessions including code execution, traversal and information disclosure.
* Insight into how these vulnerabilities are exploited in the wild based on real-world data collected from our Next-Generation Firewalls.
* Summaries of key trends from November 2022-January 2023.
* Analysis of the most recently published vulnerabilities, including the severity and attack origin distribution.
* Classification of these vulnerabilities to provide a clear view of the prevalence of the different types, such as cross-site scripting or denial-of-service.
* Lists of the most commonly exploited vulnerabilities attackers are using, as well as the severity, category and origin of each attack.

Palo Alto Networks customers receive protections from the vulnerabilities discussed here through the Next-Generation Firewall, Cloud-Delivered Security Services and Prisma Cloud WAAS, including Threat Prevention, WildFire, Advanced URL Filtering and Cortex XDR.

|  |  |
| --- | --- |
| CVEs Discussed | **[CVE-2022-27924,](https://nvd.nist.gov/vuln/detail/CVE-2022-27924) [CVE-2022-31137,](https://nvd.nist.gov/vuln/detail/CVE-2022-31137) [CVE-2022-44877,](https://nvd.nist.gov/vuln/detail/CVE-2022-44877) [CVE-2022-46169,](https://nvd.nist.gov/vuln/detail/CVE-2022-46169) [CVE-2022-41852,](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41852) [CVE-2021-43287,](https://nvd.nist.gov/vuln/detail/CVE-2021-43287) [CVE-2021-31602,](https://nvd.nist.gov/vuln/detail/CVE-2021-31602) [CVE-2021-22005,](https://nvd.nist.gov/vuln/detail/CVE-2021-22005) [CVE-2021-33035,](https://nvd.nist.gov/vuln/detail/CVE-2021-33035) [CVE-2022-30136.](https://nvd.nist.gov/vuln/detail/CVE-2022-30136) [CVE-2022-1118](https://nvd.nist.gov/vuln/detail/CVE-2022-1118)** |
| Types of Attacks and Vulnerabilities Covered | Cross-site scripting, information disclosure, buffer overflow, code execution, SQL injection, traversal, command injection, improper authentication, security feature bypass |
| Related Unit 42 Topics | **[Network Security Trends](https://unit42.paloaltonetworks.com/tag/network-security-trends/), [exploits in the wild](https://unit42.paloaltonetworks.com/tag/exploit-in-the-wild/), [attack analysis](https://unit42.paloaltonetworks.com/tag/attack-analysis/)** |

## Table of Contents

[Analysis of Published Vulnerabilities, November 2022-January 2023](#post-127995-_d4fxv97n1oql)

## Analysis of Published Vulnerabilities, November 2022-January 2023

From November 2022-January 2023, a total of 6,169 new Common Vulnerabilities and Exposures (CVE) numbers were registered. To better understand the potential impact these newly published vulnerabilities could have on network security, we provide our observations based on the severity, availability of working proof-of-concept (PoC) code, and vulnerability categories.

### How Severe Are the Latest Vulnerabilities?

To estimate the potential impact of vulnerabilities, we consider their severity and examine any reliable PoCs available that attackers could easily launch. Some of the public sources we use to find PoCs are Exploit-DB, GitHub and Metasploit. Distribution of the CVEs that have an assigned severity score of Medium or higher can be seen in the following table:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Severity** | **Count** | **Ratio** | **Ratio Change From Last Quarter %** | **PoC Availability** | **Change in PoC Availability** |
| **Critical** | 1,100 | 17.8% | -1.1% | 3% | +0.1% |
| **High** | 2,339 | 37.9% | -4.2% | 3.1% | +0.9% |
| **Medium** | 2,730 | 44.3% | +5.3% | 2.2% | -0.1% |

*Table 1. Severity distribution for CVEs registered November 2022-January 2023,* *including only those rated Medium-Critical**.*

![Image 1 is a pie chart measuring the distribution of critical, high, and medium CVEs registered through August and September of 2022. The largest percent is “high” at 37.9%.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/05/chart.png)

Figure 1. Severity distribution for CVEs registered November 2022-January 2023, including only those rated Medium-Critical.

Our classification of vulnerabilities is based on CVSS v3 scores. Many conditions must be met to rate a vulnerability as Critical, so there are very few at this level. One of the common factors for rating a vulnerability at this level is having a working PoC available. To be considered Critical, vulnerabilities generally have low attack complexity, and it is often easy to create a PoC to exploit them.

### Vulnerability Category Distribution

It is crucial to understand each type of vulnerability and its consequences. Out of the newly published CVEs that were analyzed, 22.6% are classified as local vulnerabilities, requiring prior access to compromised systems, while the remaining 77.4% are remote vulnerabilities, which can be exploited over a network. This means that most newly published vulnerabilities introduce potential opportunities for threat actors to attack vulnerable organizations from anywhere in the world.

In Figure 2, the most common vulnerability types are ranked by how prevalent they were among the most recent set of published vulnerabilities.

![Image 2 is a stacked bar chart showing the vulnerability category distribution for CVEs registered through November 2022 to January 2023. Medium has the largest portion in yellow for cross-site scripting. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/05/chart-1.png)

Figure 2. Vulnerability category distribution for CVEs registered November 2022-January 2023.

Cross-site scripting remains the most reported vulnerability from November 2022-January 2023. We also saw that the prevalence of cross-site scripting vulnerabilities increased during this time, and the majority of the vulnerabilities in this category are ranked Medium. Code execution and information disclosure vulnerabilities decreased. Most o...