---
title: Network Security Trends: August-October 2022
url: https://buaq.net/go-145276.html
source: unSafe.sh - 不安全
date: 2023-01-13
fetch_date: 2025-10-04T03:43:16.598562
---

# Network Security Trends: August-October 2022

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

![](https://8aqnet.cdn.bcebos.com/7ead7489f84442c93ddb6d162b2bedcc.jpg)

Network Security Trends: August-October 2022

Executive SummaryRecent Augu
*2023-1-12 22:0:2
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-145276.htm)
阅读量:59
收藏*

---

![A pictorial representation of a security vulnerability. It shows a checkmark on a shield within a crystal ball.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/01/Trends-r3d2.png)

## **Executive Summary**

Recent August-October 2022 observations of exploits used in the wild reveal that threat actors have been leveraging significant numbers of attacks against the Realtek Jungle SDK remote code execution vulnerability (CVE-2021-35394). They have also been making use of a newly published arbitrary file download vulnerability in BackupBuddy and taking advantage of a command injection vulnerability in Bitbucket.

In our observations of network security trends, Unit 42 researchers have pinpointed several attacks based on proof-of-concept (PoC) availability and impact. We have detailed below which of these we believe should be on a defender’s radar.

Other insights that could assist defenders include the following:

* Rankings of the most commonly used attack techniques and the types of vulnerabilities that attackers have recently favored. For example, among 5,190 newly published vulnerabilities, a large portion (almost 9.8%) involves cross-site scripting.
* Lists of major vulnerabilities identified by evaluating more than 232 million attack sessions including remote code execution.
* Insight into how these vulnerabilities are exploited in the wild based on real-world data collected from our Next-Generation Firewalls.
* Summaries of key trends from August-October 2022.
* Analysis of the most recently published vulnerabilities, including the severity and attack origin distribution.
* Classification of these vulnerabilities to provide a clear view of the prevalence of the different types, such as cross-site scripting or SQL injection.
* Lists of the most commonly exploited vulnerabilities attackers are using, as well as the severity, category and origin of each attack.

Palo Alto Networks customers receive protections from the vulnerabilities discussed here through the Next-Generation Firewall and associated Cloud-Delivered Security Services including Threat Prevention, WildFire and Advanced URL Filtering. Protections are also available from Prisma Cloud’s Web Application and API Security (WAAS) and Cortex XDR.

|  |  |
| --- | --- |
| CVEs Discussed | [CVE-2022-27925](https://nvd.nist.gov/vuln/detail/CVE-2022-27925), [CVE-2022-26352](https://nvd.nist.gov/vuln/detail/CVE-2022-26352), [CVE-2022-31474](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31474), [CVE-2022-36804](https://nvd.nist.gov/vuln/detail/CVE-2022-36804), [CVE-2022-31499](https://nvd.nist.gov/vuln/detail/CVE-2022-31499), [CVE-2022-35914](https://nvd.nist.gov/vuln/detail/CVE-2022-35914), [CVE-2022-2486](https://nvd.nist.gov/vuln/detail/CVE-2022-2486), [CVE-2022-40684](https://nvd.nist.gov/vuln/detail/CVE-2022-40684), [CVE-2022-42889](https://nvd.nist.gov/vuln/detail/CVE-2022-42889), [CVE-2021-34429](https://nvd.nist.gov/vuln/detail/CVE-2021-34429) |
| Types of Attacks and Vulnerabilities Covered | Cross-site scripting, denial of service, information disclosure, buffer overflow, privilege escalation, memory corruption, code execution, SQL injection, out-of-bounds read, traversal, command injection, improper authentication, arbitrary file download, security feature bypass |
| Related Unit 42 Topics | [Network Security Trends](https://unit42.paloaltonetworks.com/tag/network-security-trends/), [exploits in the wild](https://unit42.paloaltonetworks.com/tag/exploit-in-the-wild/), [attack analysis](https://unit42.paloaltonetworks.com/tag/attack-analysis/) |

## **Table of Contents**

[Analysis of Published Vulnerabilities, August-October 2022](#post-126464-_d4fxv97n1oql)

#### Table of Contents: Figures and Tables

[Table 1. Severity distribution for CVEs registered August-October 2022, including only those rated medium to critical.](#post-126517-_981odf6lefey)
[Figure 1. Severity distribution for CVEs registered August-October 2022, including only those rated medium to critical.](#post-126517-_k85hynuqidhr)
[Figure 2. Vulnerability category distribution for CVEs registered August-October 2022.](#post-126517-_c2z899rg00v0)
[Figure 3. Vulnerability category distribution compared with the previous quarter.](#post-126517-_4pltsplfd6d1)
[Figure 4. Attack severity distribution, August-October 2022, including only medium-critical vulnerabilities.](#post-126517-_b61l5o3r88ec)
[Figure 5. Vulnerability severity distribution compared with the previous quarter.](#post-126517-_s47f29ynancp)
[Figure 6. Proportion of attacking CVE-2021-35394. Numbers are rounded to the nearest million.](#post-126517-_skd7hpb2pjhi)
[Figure 7. Severity of exploits in the wild measured weekly from August-October 2022.](#post-126517-_hcrsbpc3e3r0)
[Figure 8. Observed attacks broken down by the year in which the exploited CVE was disclosed, measured weekly from August-October 2022.](#post-126517-_3i00vomx4ywi)
[Figure 9. Zimbra remote code execution.](#post-126517-_lohgtlkb54q3)
[Figure 10. dotCMS remote code execution.](#post-126517-_1urpoorfxlgf)
[Figure 11. BackupBuddy arbitrary file download.](#post-126517-_pfa37hd9m3xz)
[Figure 12. Bitbucket command Injection.](#post-126517-_azhxkpyyav72)
[Figure 13. Nortek Linear eMerge E3-Series command injection.](#post-126517-_km03vsj2pevf)
[Figure 14. GLPI command injection.](#post-126517-_tp7k9ewcauy4)
[Figure 15. WAVLINK command injection.](#post-126517-_g4x0gsw77i9f)
[Figure 16. Fortinet FortiOS authentication bypass.](#post-126517-_9leamqx2qa7h)
[Figure 17. Apache Commons Text code execution.](#post-126517-_nfwkodjt6f6p)
[Figure 18. Jetty bypass.](#post-126517-_50xoi3acpq42)
[Figure 19. Attack category and severity, August-October 2022.](#post-126517-_prz63cr2twhn)
[Figure 20. Locations ranked in terms of how frequently they were the origin of observed attacks from August-October 2022.](#post-126517-_h1xg8n45c2oz)
[Figure 21. Attack originate distribution compared to the previous quarter.](#post-126517-_fmszo2q2uo1c)
[Figure 22. Attack geolocation distribution from August-October 2022.](#post-126517-_g8m0dmhlzllr)

## **Analysis of Published Vulnerabilities, August-October 2022**

From August-October 2022, a total of 5,190 new Common Vulnerabilities and Exposures (CVE) numbers were registered. To better understand the potential impact these newly published vulnerabilities could have on network security, we provide our observations based on the severity, availability of working proof-of-concept (PoC) code, and vulnerability categories.

### **How Severe Are the Latest Vulnerabilities?**

To estimate the potential impact of vulnerabilities, we consider their severity and examine any reliable PoCs available that attackers could easily launch. Some of the public sources we use to find PoCs are Exploit-DB, GitHub and Metasploit. Distribution of the 5,190 CVEs that have an assigned severity score of medium or higher can be seen in the following table:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Severity** | **Count** | **Ratio** | **Ratio Change From Last Quarter %** | **PoC Availability** | **Change in PoC Availability** |
| **Critical** | 980 | 18.9% | -0.1% | 2.9% | -2.6% |
| **High** | 2184 | 42.1% | +2.0% | 2.2% | -1.6% |
| **Medium** | 2026 | 39.0% | -1.9% | 2.3% | -1.1% |

*Table 1. Severity distribution for CVEs registered August-October 2022, including only...