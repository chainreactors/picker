---
title: Critical Apache Log4j2 flaw still threatens global finance
url: https://buaq.net/go-242660.html
source: unSafe.sh - 不安全
date: 2024-06-02
fetch_date: 2025-10-06T16:55:10.543705
---

# Critical Apache Log4j2 flaw still threatens global finance

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

![](https://8aqnet.cdn.bcebos.com/c5332c0ace2640a5a49f41874518d390.jpg)

Critical Apache Log4j2 flaw still threatens global finance

Critical Apache Log4j2 flaw still threatens global financeThe vulnerability CVE-2021-44832 is
*2024-6-1 23:44:6
Author: [securityaffairs.com(查看原文)](/jump-242660.htm)
阅读量:15
收藏*

---

## Critical Apache Log4j2 flaw still threatens global finance

![](https://i0.wp.com/securityaffairs.com/wp-content/uploads/2014/05/russia-and-ukraine.jpg?fit=620%2C388&ssl=1)

## The vulnerability [CVE-2021-44832](https://securityaffairs.com/126135/hacking/new-apache-log4j-cve-2021-44832.html) is Apache Log4j2 library is still a serious problem for multiple industries, expert warns it threatens global Finance.

The independent cyber threat intelligence analyst [Anis Haboubi](https://x.com/HaboubiAnis) warns of a severe logging configuration flaw that could dramatically impact the financial industry.

> 🚨 Critical Vulnerability Threatens Global Finance 🚨
>
> — Anis Haboubi |₿| (@HaboubiAnis) [May 31, 2024](https://twitter.com/HaboubiAnis/status/1796675660259205367?ref_src=twsrc%5Etfw)

The vulnerability is [CVE-2021-44832](https://securityaffairs.com/126135/hacking/new-apache-log4j-cve-2021-44832.html) and impacts Apache Log4j2, a remote attacker can exploit this vulnerability to execute malicious code on affected systems. The flaw received a CVSS score of 6.6 and impacts all log4j versions from 2.0-alpha7 to 2.17.0. Versions 2.3.2 and 2.12.4. are not impacted.

*“Apache Log4j2 versions 2.0-beta7 through 2.17.0 (excluding security fix releases 2.3.2 and 2.12.4) are vulnerable to a remote code execution (RCE) attack where an attacker with permission to modify the logging configuration file can construct a malicious configuration using a JDBC Appender with a data source referencing a JNDI URI which can execute remote code. This issue is fixed by limiting JNDI data source names to the java protocol in Log4j2 versions 2.17.1, 2.12.4, and 2.3.2.” [reads the advisory](https://nvd.nist.gov/vuln/detail/CVE-2021-44832).*

The vulnerability was discovered by Checkmarx security researcher Yaniv Nizry who reported it to Apache on December 27, 2020. The Apache Software Foundation released Log4j 2.17.1 version to address the flaw a couple of days later.

The recent breaches at [Sisense](https://securityaffairs.com/161728/data-breach/sisense-suffers-a-cyber-attack.html) and [Snowflake](https://www.sisense.com/data-connectors/snowflake/), both ISO/IEC 27001 certified companies, highlight a critical vulnerability that still threatens the entire finance industry. Despite adhering to stringent security standards, the flaws in their infrastructure have exposed sensitive financial data to unauthorized access, potentially leading to catastrophic consequences, [Haboubi](https://x.com/HaboubiAnis) told SecurityAffairs.

Why does this old flaw still threaten the Finance industry?

The critical flaw in logging configurations allows attackers with write access to exploit a JDBC Appender with a JNDI URI, enabling remote code execution. This can lead to complete system compromise, allowing attackers to execute malicious code remotely and gain unauthorized access to sensitive financial data. Sisense and Snowflake are trusted by top international financial groups.

“These companies rely on their services for critical operations, including data analytics and cloud storage. A breach in these systems can disrupt financial activities on a global scale, causing significant financial and reputational damage.” said [Haboubi](https://x.com/HaboubiAnis).

“The breaches have resulted in the exfiltration of several terabytes of customer data, including access tokens, email account passwords, and SSL certificates. This data can be exploited by attackers to gain further access to financial systems and conduct fraudulent activities. Interconnected Financial Systems: The financial industry is highly interconnected. A vulnerability in one system can lead to a domino effect, compromising other systems and services. The potential for widespread disruption makes this flaw particularly dangerous.”

The breaches have raised questions about whether Sisense and Snowflake were doing enough to protect sensitive data. The stolen data, which was apparently not encrypted while at rest, underscores the need for more robust security measures.

In conclusion, the flaws in the infrastructure of Sisense and Snowflake, combined with their extensive use in the finance sector, pose a significant threat. Immediate action is required to mitigate these vulnerabilities and protect the integrity of financial operations globally. Enhanced security measures, such as the integration of PEM key-based authentication, are crucial to prevent future breaches and ensure the safety of sensitive financial data.

> 🧵4/4
> It's crucial to update your logging configurations and implement robust SSH security measures immediately. Ensure all access points are secure to protect against potential exploits. Stay vigilant and secure! [pic.twitter.com/yn6QLUL4zW](https://t.co/yn6QLUL4zW)
>
> — Anis Haboubi |₿| (@HaboubiAnis) [May 31, 2024](https://twitter.com/HaboubiAnis/status/1796675677778768252?ref_src=twsrc%5Etfw)

“It’s quite impressive. I believe the attackers breached the systems several months, or perhaps even years, ago. They likely waited for the right moment to exfiltrate the data, and Sisense only recently discovered the breach. One of the biggest issues for me is that Sisense allowed “Connecting to a Private Network with an SSH Tunnel” without a PEM key. This is what they discreetly fixed in the commit I shared with you. The attackers clearly exploited the Log4j vulnerability from the outset to gain privileged access to critical infrastructures. They then hid for months to see if they could maintain persistence” concludes the expert. “even today 30% of log4J installations are vulnerable to log4hell”

Follow me on Twitter: [**@securityaffairs**](https://twitter.com/securityaffairs) and [**Facebook**](https://www.facebook.com/sec.affairs) and [Mastodon](https://infosec.exchange/%40securityaffairs)

[**Pierluigi Paganini**](http://www.linkedin.com/pub/pierluigi-paganini/b/742/559)

**(**[**SecurityAffairs**](http://securityaffairs.co/wordpress/)**–** **hacking, Log4j2)**

---

文章来源: https://securityaffairs.com/163984/hacking/critical-apache-log4j2-flaw-still-threatens-global-finance.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)