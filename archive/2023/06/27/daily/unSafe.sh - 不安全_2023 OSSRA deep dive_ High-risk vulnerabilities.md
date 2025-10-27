---
title: 2023 OSSRA deep dive: High-risk vulnerabilities
url: https://buaq.net/go-170431.html
source: unSafe.sh - 不安全
date: 2023-06-27
fetch_date: 2025-10-04T11:44:40.294664
---

# 2023 OSSRA deep dive: High-risk vulnerabilities

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

![](https://8aqnet.cdn.bcebos.com/5c9f8eed93aec91f65964ecddf96bf71.jpg)

2023 OSSRA deep dive: High-risk vulnerabilities

The 2023 OSSRA report indicates that organizations are failing to patch high-risk vulnerabilities;
*2023-6-26 23:44:12
Author: [www.synopsys.com(查看原文)](/jump-170431.htm)
阅读量:14
收藏*

---

*The 2023 OSSRA report indicates that organizations are failing to patch high-risk vulnerabilities; our vulnerability deep-dive shows how to evaluate your own risk.*

![](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2023/06/NewsCredBanner_19x5TSK8803.png)

According to [the 2023 “Open Source Security and Risk Analysis” (OSSRA) report](https://www.synopsys.com/software-integrity/resources/analyst-reports/open-source-security-risk-analysis.html), 96% of commercial code contains open source material. In fact, 76% of the code that [Black Duck® Audit Services](https://www.synopsys.com/software-integrity/open-source-software-audit.html) scanned in 2022 *was* open source. Eighty-four percent of the scanned codebases contained at least one known open source vulnerability, and nearly half—48%—of the codebases contained high-risk vulnerabilities.

## What is a high-risk vulnerability?

Software vulnerabilities are categorized into risk levels based on the potential impact of exploitation (taking advantage of a vulnerability to cause unintended or unanticipated behavior). The Common Vulnerability Scoring System (CVSS), an industry standard for ranking the characteristics and severity of software vulnerabilities, uses a score ranging from 0 to 10. The current specification for CVSS is [version 3.1](https://www.first.org/cvss/). Actual vulnerability risk levels may vary dependent on how your organization ranks risk, but in CVSS rankings risk levels range are

* Low (0.1 to 3.9): These vulnerabilities have a small potential for harm and are unlikely to cause significant damage if exploited.
* Medium (4.0 to 6.9): These vulnerabilities may not pose an immediate or severe threat but do have the potential for harm. An attacker might exploit a medium-risk vulnerability to gain unauthorized access to a system or to compromise sensitive information.
* High (7.0 to 8.9): These vulnerabilities have significant potential for harm if exploited and can lead to severe consequences, such as significant data loss or downtime. Immediate attention and mitigation are recommended for high-risk vulnerabilities.
* Critical (9.0 to 10.0): These vulnerabilities are usually easy for an attacker to exploit and may result in unauthorized access, data breaches, and system compromise or disruption. As with high-risk vulnerabilities, immediate attention and mitigation are advised. The major difference between critical and high-risk vulnerabilities is that exploitation of a critical-risk vulnerability usually results in root-level compromise of servers or infrastructure devices.

###### Some examples of high-risk open source vulnerabilities include

* Heartbleed (CVE-2014-0160), a critical vulnerability in the OpenSSL cryptographic software library, allowed attackers to exploit a flaw in the TLS heartbeat extension, potentially exposing sensitive information such as usernames, passwords, and private keys. Heartbleed was publicly disclosed in April 2014, with a fixed version of OpenSSL released the same day.
* Shellshock (CVE-2014-6271), a vulnerability found in the popular Bash shell command-line interface in UNIX-based systems, enabled attackers to execute arbitrary commands on vulnerable systems, potentially leading to unauthorized access or control. The vulnerability lasted 30 years before being discovered.
* Apache Struts Remote Code Execution (CVE-2017-5638) affected Apache Struts, a popular open source framework used for building Java web applications. It allowed remote attackers to execute arbitrary code by sending specially crafted requests, potentially leading to unauthorized access or control of the affected server. An exploit of CVE-2017-5638 caused Equifax’s high-profile, high-impact data breach, which occurred between May and July 2017 and compromised the private records of 147.9 million American, 15.2 million British, and 19,000 Canadian citizens. It’s one of the largest cybercrimes related to identity theft to date.
* Drupalgeddon (CVE-2018-7600), a critical vulnerability in the Drupal open source content management system, allowed attackers to execute arbitrary code without authentication, potentially leading to unauthorized access, data breaches, or full compromise of the affected Drupal-based websites. Although a patch was issued shortly after disclosure, attackers were still exploiting the vulnerability nearly two years later.

Open source projects typically have active security communities and mechanisms for reporting and addressing vulnerabilities, but it’s crucial to stay informed about known vulnerabilities and apply the necessary patches or updates as they become available. Unlike most commercial code, open source uses a “pull” model when it comes to patches and updates, meaning that developers and end users have the responsibility to download and install the latest version of those components themselves.

## The 2023 OSSRA shows organizations aren’t fixing high-risk vulnerabilities

This year, the 2023 OSSRA took a five-year look back at the data used for the report with the goal of identifying notable trends, some of which were surprising. Since 2019, for example, the number of high-risk vulnerabilities jumped as much as 557% in the retail and eCommerce sector. Likewise, the aerospace, aviation, automotive, transportation, and logistics sector saw a massive 232% increase in high-risk vulnerabilities.

Since 2019, 100% of the codebases from the Internet of Things (IoT) sector contained some amount of open source. The total amount of open source in each codebase has also increased over the years, up 35% since 2019, with 89% of the total code being open source code.

The IoT is an ideal representation of the benefits of open source; IoT organizations (for example, the smart devices offered by Ring, Amazon, and Nest) are under extreme pressure to produce new software, fast. In a fast-paced industry with strong competition, open source helps organizations remain quick on their feet—without it, they couldn’t keep up with the breakneck pace that software development demands.

The downside is the risk of introducing vulnerabilities. The IoT vertical has seen a 130% increase in high-risk vulnerabilities since 2019, and this year, 53% of its audited applications contained high-risk vulnerabilities (one of the higher percentages in OSSRA’s findings). This is particularly concerning when you think about the ubiquity of IoT devices and how so many aspects of our lives are connected to these devices. IoT devices power our lights on automated schedules, meaning they contain data about when we are home and when we are out. We use cameras that contain images of the inside of our homes, smart locks on our front doors, and baby monitors to watch over our children.

[See the full 2023 OSSRA](https://www.synopsys.com/software-integrity/resources/analyst-reports/open-source-security-risk-analysis.html) report for more details on open source trends from the past five years.

## Set vulnerability patching priorities

There is a myth that the proverbial developer can fix each and every vulnerability, but that’s just not possible if the management team hasn’t prioritized resolution. To work effectively, patch priorities should align with the business importance of the asset being patched, the criticality of the asset, a...