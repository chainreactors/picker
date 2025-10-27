---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 26
url: https://buaq.net/go-170918.html
source: unSafe.sh - 不安全
date: 2023-07-01
fetch_date: 2025-10-04T11:51:02.564684
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 26

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

![](https://8aqnet.cdn.bcebos.com/728b580d3287e773bfde4885eec2157b.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 26

The Good | Authorities Sentence 2020 Twitter Hacker For SIM Swap & Crypto Theft SchemesJoseph Jame
*2023-6-30 21:0:9
Author: [www.sentinelone.com(查看原文)](/jump-170918.htm)
阅读量:22
收藏*

---

## The Good | Authorities Sentence 2020 Twitter Hacker For SIM Swap & Crypto Theft Schemes

Joseph James O’Connor (*aka* PlugWalkJoe) was sentenced this week to five years in prison for various cybercrimes including his role in the [2020 Twitter Hack](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-29-2/). O’Connor is charged with stealing cryptocurrency, money laundering, cyberstalking, and unauthorized access to Twitter, TikTok, and Snapchat accounts. Further, he is ordered to return the $749,000 stolen from a New York-based cryptocurrency firm.

[![](https://www.sentinelone.com/wp-content/uploads/2023/06/josephjamesoconnor_arrest.jpg)](https://www.sentinelone.com/?attachment_id=82194)

Source: Reuters

According to the [DoJ](https://www.justice.gov/usao-sdny/pr/uk-citizen-sentenced-five-years-prison-cybercrime-offenses), O’Connor and his co-conspirators conducted a mass SIM swap attack in 2019 to steal from a targeted cryptocurrency firm. In SIM swap attacks, a threat actor gains control of a victim’s mobile phone number by linking it to an SIM card controlled by the actors. The victim’s calls and messages are then routed to the actor-controlled device and used to access accounts registered with the victim’s number. Using this technique, O’Connor and his associates successfully targeted three of the cryptocurrency firm’s executives and obtained access to the company’s internal accounts and system.

In the 2020 Twitter Hack, O’Connor and his associates again used SIM swaps, along with social engineering tactics, to gain access to Twitter’s back-end tools and transfer control of high-profile accounts to various unauthorized users. While some accounts were [hijacked](https://www.sentinelone.com/cybersecurity-101/the-ultimate-guide-to-preventing-account-takeover-attacks/) by the actors themselves, O’Connor sold the access rights of several well-known accounts. Using similar techniques, O’Connor also hijacked TikTok and Snapchat accounts to participate in online extortion, harassment, and cyber stalking.

These attacks on social media platforms underscore the impact that cyber attacks have on everyday users. As the rate of digital identity theft skyrockets and threat actors continue to eye up popular apps and services, implementing strong [identity-based controls](https://www.sentinelone.com/cybersecurity-101/identity-security-what-it-is-why-its-so-important/) remains a high-priority task for organizations in all industries.

## The Bad | New Infostealer Malware Dubbed “ThirdEye” Targets Windows Devices

A newly discovered Windows-based infostealer dubbed “ThirdEye” has been spotted in the wild, harvesting sensitive data from infected hosts. Security researchers this week [reported](https://www.fortinet.com/blog/threat-research/new-fast-developing-thirdeye-infostealer-pries-open-system-information) on an executable masquerading as a PDF file which hosts the info-stealing malware. While the arrival vector for the malware isn’t yet known, researchers believe it is used in [phishing](https://www.sentinelone.com/cybersecurity-101/phishing-scams/) campaigns.

[![](https://www.sentinelone.com/wp-content/uploads/2023/06/arunas-naujokas-YTahzF760ds-unsplash-scaled.jpg)](https://www.sentinelone.com/?attachment_id=82193)

Based on an earlier version of ThirdEye that was [uploaded](https://www.virustotal.com/gui/file/610aff11acce8398f2b35e3742cb46c6a168a781c23a816de2aca471492161b2) to VirusTotal in early April, the infostealer is evolving and now shows capabilities of gathering system metadata such as BIOS release dates and vendors, total and free disk space on C: drives, volume information, and registered usernames. Details collected are then transmitted to a command-and-control (C2) server.

Though the malware is not considered technically sophisticated, researchers warn that its purpose-built design allows malicious users to gather critical information for use in future attacks. In the case of ThirdEye, the information stolen could be used by attackers as a way of narrowing down potential targets and planning unique campaigns.

There are no current indications that ThirdEye has been used in the wild. However, given the fact that the infostealer artifacts were uploaded to VirusTotal from Russia, researchers speculate that any malicious activity leveraging the malware is likely being aimed at Russian-speaking organizations. ThirdEye is the latest to make an appearance following a marked [surge](https://www.secureworks.com/research/the-growing-threat-from-infostealers) of infostealer malware being sold on Russian [darknets](https://www.sentinelone.com/cybersecurity-101/what-is-the-dark-web/).

As more infostealers become readily available, enabling cybercriminals to launch their ransomware campaigns, organizations should invest in machine learning algorithms and analytics to identify patterns indicating suspicious activity in real-time.

## The Ugly | Emerging 8Base Ransomware Group Responsible For Uptick In Ransomware Attacks

First appearing in March, the emerging [ransomware](https://www.sentinelone.com/cybersecurity-101/ransomware/) group called 8Base has accelerated its activity over the past two months, targeting small to medium-sized businesses worldwide in double extortion “name and shame” attacks. According to security analysts, ransomware attacks have [spiked](https://www.sdxcentral.com/articles/ransomware-victims-spike-24-in-may-as-new-threat-actor-8base-discovered/2023/06/) in May and June so far, up respectively 24% from this April and 56% compared to the same period last year. 8Base claims a significant role in this surge, responsible for more than 15% of all ransomware victims recorded last month.

In [double extortion attacks](https://www.sentinelone.com/blog/ransoms-without-ransomware-data-corruption-and-other-new-tactics-in-cyber-extortion/), threat actors exfiltrate and encrypt all of a victim’s sensitive data, giving them extra leverage when demanding ransom payments. Actors then threaten to release or sell the data onto the dark web unless payment is made.

Like many other groups in the threat landscape though, 8Base accepts ransom payments in [Bitcoin](https://www.sentinelone.com/blog/malware-analyst-guide-bitcoin/) only and claims on its leak site to be “honest and simple [pentesters](https://www.sentinelone.com/cybersecurity-101/penetration-testing/)”. The group employs multiple streams of communication, including an active [Twitter](https://www.sdxcentral.com/articles/ransomware-victims-spike-24-in-may-as-new-threat-actor-8base-discovered/2023/06/) profile and several encrypted [Telegram](https://t.me/eightbase) channels. Latest [findings](https://blogs.vmware.com/security/2023/06/8base-ransomware-a-heavy-hitting-player.html) on the group note that 8Base has compromised businesses across a large span of industries but has not shown allegiance to any one particular methodology or source of motivation.

> 8base ransomware group has exploded in victim postings. Their output rivals the big 3.
>
> Prediction: in the coming months they will become a big player in the ransomware scene.
>
> — vx-underground (@vxunderground) [June 29, 2023](https://twitter.com/vxunderground/status/1674348915242532865?ref_src=twsrc%5Etfw)

Based on the speed and effec...