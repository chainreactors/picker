---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 4
url: https://buaq.net/go-146858.html
source: unSafe.sh - 不安全
date: 2023-01-28
fetch_date: 2025-10-04T05:03:00.902757
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 4

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

![](https://8aqnet.cdn.bcebos.com/e99919a971e96d5c29931028da5f55a4.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 4

The GoodThe tables have turned for Hive ransomware group. This week, FBI and international partner
*2023-1-27 22:0:0
Author: [www.sentinelone.com(查看原文)](/jump-146858.htm)
阅读量:21
收藏*

---

## The Good

The tables have turned for [Hive](https://www.sentinelone.com/blog/hive-ransomware-deploys-novel-ipfuscation-technique/) ransomware group. This week, FBI and international partners shared news of their successful sting operation; a “hack of the hackers” resulting in the seizure of two of the group’s servers and one virtual private server. The FBI also revealed that it was able to burrow deep into the group’s infrastructure and gather intelligence prior to dismantling the operation.![](https://www.sentinelone.com/wp-content/uploads/2023/01/hive.png)

Hive is among the world’s most prolific ransomware networks, which has long beleaguered critical infrastructures such as governments and [hospitals](https://www.sentinelone.com/labs/hive-attacks-analysis-of-the-human-operated-ransomware-targeting-healthcare/). Initially spotted in July 2021 during the height of the COVID-19 pandemic, the syndicate is known for its Ransomware-as-a-Service (RaaS) model. Hive ransomware group has extorted more than $100 million from 1500 organizations across at least 80 countries.

According to the [DOJ](https://www.justice.gov/opa/pr/us-department-justice-disrupts-hive-ransomware-variant), the month-long operation came to a head in July of last year when the FBI quietly accessed Hive’s control panel and obtained the software keys shared with the syndicate’s partners used to perform double extortion attacks. While no arrests have been made yet, officials announced that they were building a map of associated administrators, software, and affiliates based on the seized servers. Officials have been helping recent victims regain access to their networks, saving almost 300 organizations over $130 million in what would have been ransom payments.

The dismantling of Hive is one of the first big crackdowns of 2023; a concerted effort across various law enforcement groups in the effort to slow the ransomware epidemic. While the ransomware economy continues to be a lucrative one for attackers, these sting operations are hitting them where it hurts most – their earnings. Officials are now [offering](https://twitter.com/RFJ_USA/status/1618658902626779136) rewards for information linking Hive to foreign governments.

## The Bad

Alleged Chinese-speaking threat actors are upping their evasion game through a little-known open source SparkRAT and Golang malware. In an [analysis](https://www.sentinelone.com/labs/dragonspark-attacks-evade-detection-with-sparkrat-and-golang-source-code-interpretation/) by SentinelLabs this week, a recent cluster of attacks dubbed DragonSpark has been observed employing uncommon tactics to sidestep security layers. DragonSpark attacks have so far victimized organizations in China, Taiwan, Hong Kong, and Singapore.

Initial access involves the compromise of vulnerable, internet-exposed web servers and MySQL servers to drop a ‘[China Chopper](https://www.cyber.nj.gov/threat-center/threat-profiles/trojan-variants/china-chopper)’ web shell. After gaining that foothold, DragonSpark attacks use lateral movement techniques paired with privilege escalation and malware deployment to root deeper into a victim’s environment.

Once lateral spread is underway, actors use a cross-platform remote access trojan called SparkRAT to conduct a host of malicious activities such as manipulating system files, stealing information, and running additional PowerShell commands. SparkRAT is based in Golang and can run on Windows, macOS, and Linux. Other malicious tools observed in DragonSpark attacks have all been open sourced tools such as [SharpToken](https://github.com/BeichenDream/SharpToken), [BadPotato](https://github.com/BeichenDream/BadPotato), and [GotoHTTP](https://gotohttp.com/).

![](https://www.sentinelone.com/wp-content/uploads/2023/01/SaprkRAT_9.jpeg)

The Golang malware ‘m6699.exe’ executes code from embedded Go scripts in the malware binaries – a technique for hindering static analysis and evading detection. The malware then opens a reverse shell allowing the threat actors to begin remote code execution (RCE).

SentinelLabs analysts hypothesize that multi-platform, feature-rich tools like SparkRAT will continue to appear in future attacks by attackers known to favor open source software in their campaigns.

## The Ugly

A new [warning](https://www.cisa.gov/uscert/ncas/alerts/aa23-025a) from CISA, the NSA, and Multi-State Information Sharing & Analysis Center (MS-ISAC) dropped this week detailing attacks against multiple federal civilian executive branch (FCEB) agencies through the use of legitimate remote monitoring and management (RMM) software.

Malicious activity against many FCEB networks was executed through callback phishing campaigns. Threat actors sent spoofed help desk emails to federal staffers’ personal and government email addresses. Emails were found to contain a link to a first-stage domain and encouraged targeted users to call the attackers who then posed as help desk technicians.

After the ‘technicians’ convinced the caller to visit the domains, malware would be downloaded automatically, connecting the target to a second-stage domain with downloads for AnyDesk and ScreenConnect – popular RMM tools used by remote workers globally – after which the attacker had full access to the victim’s device.

Weaponizing legitimate remote software continues to be attractive to threat actors as an effective means of establishing local user access – all without needing any admin permissions. The joint warning released this week highlights the increased spike in [social engineering](https://www.sentinelone.com/blog/the-dangers-of-social-engineering-how-to-protect-your-organization/) and [phishing attacks](https://www.sentinelone.com/cybersecurity-101/spear-phishing/) combined with the use of legitimate software for access.

![](https://www.sentinelone.com/wp-content/uploads/2023/01/23-01-26-23-17-02-329_deco-scaled.jpg)

This follows on from a [recent case](https://www.sentinelone.com/blog/gotta-catch-em-all-understanding-the-netsupport-rat-campaigns-hiding-behind-pokemon-lures/) in which attackers hosted an online Pokémon-based NFT game, luring fans of the franchise to download remote access trojans (RATs) on the site. Efforts like this are considered ‘quick wins’ for threat actors as they get the access they want without spending time or resources on developing bespoke attacks. CISA’s official warning includes a [list](https://www.cisa.gov/uscert/ncas/alerts/aa23-025a#:~:text=Paypal%20domains.-,Mitigations,-The%20authoring%20organizations) of preventative measures organizations can take to avoid social engineering attacks and reduce the risk of RMM software misuse.

文章来源: https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-4-4/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)