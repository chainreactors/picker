---
title: Network Security Trends: May-July 2022
url: https://buaq.net/go-135940.html
source: unSafe.sh - 不安全
date: 2022-11-17
fetch_date: 2025-10-03T22:58:13.005302
---

# Network Security Trends: May-July 2022

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

![](https://8aqnet.cdn.bcebos.com/f8afb491213235f1e7090a33a7b190cc.jpg)

Network Security Trends: May-July 2022

Executive SummaryRecent May-
*2022-11-16 22:0:59
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-135940.htm)
阅读量:113
收藏*

---

![Network security trends conceptual image](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/11/Trends-r3d2.png)

## **Executive Summary**

Recent May-July 2022 observations of network security trends and exploits used in the wild reveal that attackers have been making use of newly published remote code execution vulnerabilities in Atlassian Confluence, SolarView Compact and a WordPress plugin. Attackers have also been taking advantage of embedded malicious functionality in a WordPress plugin by the name of "School Management Pro," and an authentication bypass in F5 BIG-IP.

In our observations of network security trends, Unit 42 researchers have pinpointed several attacks based on proof-of-concept (PoC) availability and impact. We have detailed below which of these we believe should be on the defender’s radar.

Other insights that could assist defenders include the following:

* Rankings of the most commonly used attack techniques and the types of vulnerabilities that attackers have recently favored. For example, among 5,976 newly published vulnerabilities, a large portion (almost 11.6%) involves cross-site-scripting.
* Lists of major vulnerabilities identified by evaluating more than 340 million attack sessions including remote code execution, directory traversal and information disclosure.
* Insight into how these vulnerabilities are exploited in the wild based on real-world data collected from our Next-Generation Firewalls.
* Summaries of key trends from May-July 2022.
* Analysis of the most recently published vulnerabilities, including the severity and attack origin distribution.
* Classification of these vulnerabilities to provide a clear view of the prevalence of the different types, such as cross-site scripting or denial-of-service.
* Lists of the most commonly exploited vulnerabilities attackers are using, as well as the severity, category and origin of each attack.

Palo Alto Networks customers receive protections from the vulnerabilities discussed here through the Next-Generation Firewall and Cloud-Delivered Security Services, including Threat Prevention, WildFire, Advanced URL Filtering and Cortex XDR.

|  |  |
| --- | --- |
| CVEs Discussed | [CVE-2022-1388](https://nvd.nist.gov/vuln/detail/CVE-2022-1388), [CVE-2022-26134](https://nvd.nist.gov/vuln/detail/cve-2022-26134), [CVE-2022-2488](https://nvd.nist.gov/vuln/detail/CVE-2022-2488), [CVE-2022-26138](https://nvd.nist.gov/vuln/detail/cve-2022-26138), [CVE-2022-29303](https://nvd.nist.gov/vuln/detail/CVE-2022-29303), [CVE-2022-31446](https://nvd.nist.gov/vuln/detail/CVE-2022-31446), [CVE-2022-1119](https://nvd.nist.gov/vuln/detail/CVE-2022-1119), [CVE-2022-1609](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1609), [CVE-2021-26085](https://nvd.nist.gov/vuln/detail/CVE-2021-26085), [CVE-2021-25003](https://nvd.nist.gov/vuln/detail/CVE-2021-25003), [CVE-2021-35064](https://nvd.nist.gov/vuln/detail/CVE-2021-35064) |
| Types of Attacks and Vulnerabilities Covered | Cross-site scripting, denial of service, information disclosure, buffer overflow, privilege escalation, memory corruption, code execution, SQL injection, out-of-bounds read, cross-site request forgery, directory traversal, command injection, improper authentication, security feature bypass |
| Related Unit 42 Topics | [Network Security Trends](https://unit42.paloaltonetworks.com/tag/network-security-trends/), [exploits in the wild](https://unit42.paloaltonetworks.com/tag/exploit-in-the-wild/), [attack analysis](https://unit42.paloaltonetworks.com/tag/attack-analysis/) |

## **Table of Contents**

* [Analysis of Published Vulnerabilities, May-July 2022](#post-125749-_d4fxv97n1oql)
  + [How Severe Are the Latest Vulnerabilities?](#post-125749-_mtjquq2rgybs)
  + [Vulnerability Category Distribution](#post-125749-_trkp8qrw7rlk)
* [Network Security Trends: Analysis of Exploits in the Wild, May-July 2022](#post-125749-_vfmgbhbd90aq)
  + [Data Collection](#post-125749-_e0n4tu7kdfmt)
  + [How Severe Were the Attacks Exploited in the Wild?](#post-125749-_n2ws7k1wokpi)
  + [When Did the Network Attacks Occur?](#post-125749-_4hsvkgja7tuf)
* [Exploits in the Wild, May-July 2022: A Detailed View of Network Security Trends](#post-125749-_j5lptm394qwj)
  + [Attack Category Distribution](#post-125749-_j39clpv4lyb5)
  + [Where Did the Attacks Originate?](#post-125749-_hc12hvlkgejs)
* [Conclusion](#post-125749-_vtiimj7cgrr)
* [Additional Resources](#post-125749-_i35zice6o0zd)

## Analysis of Published Vulnerabilities, May-July 2022

From May-July 2022, a total of 5,976 new Common Vulnerabilities and Exposures (CVE) numbers were registered. To better understand the potential impact these newly published vulnerabilities could have on network security, we provide our observations based on the severity, availability of working proof-of-concept (PoC) code, and vulnerability categories.

### **How Severe Are the Latest Vulnerabilities?**

To estimate the potential impact of vulnerabilities, we consider their severity and examine any reliable PoCs available that attackers could easily launch. Some of the public sources we use to find PoCs are Exploit-DB, GitHub and Metasploit. Distribution of the 5,976 CVEs that have an assigned severity score of medium or higher can be seen in the following table:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Severity** | **Count** | **Ratio** | **PoC Availability** | **Change** |
| Critical | **1133** | **19.0%** | **5.5%** | **-2.3%** |
| High | **2399** | **40.1%** | **3.8%** | **-1.0%** |
| Medium | **2444** | **40.9%** | **3.4%** | **-0.2%** |

*Table 1. Severity distribution for CVEs registered May-July 2022,* *including only those rated medium-critical****.***

![Medium severity: 40.9%, high severity: 40.1%, critical severity: 19.0%](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/11/word-image-33.png)

Figure 1. Severity distribution for CVEs registered May-July 2022, including only those rated medium-critical.

Our classification of vulnerabilities is based on CVSS v3 scores. Many conditions must be met to rate a vulnerability as critical, so there are very few at this level. One of the common factors for rating a vulnerability at this level is having a working PoC available. To be considered critical, vulnerabilities generally have low attack complexity, and it is often easy to create a PoC to exploit them.

In the period discussed, the critical-severity ratios increased while high-severity and medium-severity PoC ratios decreased slightly.

### **Vulnerability Category Distribution**

It is crucial to understand each type of vulnerability and its consequences. Out of the newly published CVEs that were analyzed, 23.5% are classified as local vulnerabilities, requiring prior access to compromised systems, while the remaining 76.5% are remote vulnerabilities, which can be exploited over a network. This means that most newly published vulnerabilities introduce potential opportunities for threat actors to attack vulnerable organizations from anywhere in the world.

In Figure 2, the most common vulnerability types are ranked by how prevalent they were among the most recent set of published vulnerabilities.

![Red = critical, yellow = high, blue = medium. In order from most to least prevalent vulnerability category: cross-site scripting, SQL injection, information disclosure, privilege escalat...