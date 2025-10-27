---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 34
url: https://buaq.net/go-175409.html
source: unSafe.sh - 不安全
date: 2023-08-26
fetch_date: 2025-10-04T11:59:30.084699
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 34

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

![](https://8aqnet.cdn.bcebos.com/7b884fe2a76c94546bdde3ea20bd56c4.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 34

The Good | Lapsus$ Teen Members Found Responsible for High-Profile Cyber Crime SpreeThis week, a L
*2023-8-25 21:0:26
Author: [www.sentinelone.com(查看原文)](/jump-175409.htm)
阅读量:11
收藏*

---

## The Good | Lapsus$ Teen Members Found Responsible for High-Profile Cyber Crime Spree

This week, a London jury found 18 year-old Arion Kurtaj of Oxford, UK to be [responsible](https://www.bbc.co.uk/news/technology-66549159) for a series of cyberattacks against [major firms](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-12-3/), including Uber, Nvidia, and Rockstar Games. Additional charges include computer intrusion, fraud, and the demand for millions of US dollars in ransom backed by the threat of leaking sensitive information.

Kurtaj holds several online aliases, including *teapotuberhacker*, *White*, and *Breachbase* and is estimated to have made over 300 [BTC](https://www.sentinelone.com/blog/malware-analyst-guide-bitcoin/) from various illicit activities. Much of these ill-gotten profits, however, were reportedly lost to rival hackers and gambling. Alongside Kurtaj, a second teenager has been convicted for their association with Lapsus$ and breaching several companies.

![](https://www.sentinelone.com/wp-content/uploads/2023/08/23-08-24-23-37-44-200_deco-scaled.jpg)

Described by the court as a loose and unorganized collective of young “digital bandits”, Lapsus$ is thought to have members operating within the UK and possibly Brazil. Over the years, the group has targeted multiple high-profile organizations such as Microsoft, Okta, Cisco, T-Mobile, and Samsung. Since their emergence in December of 2021, members have been observed attacking [government](https://www.sentinelone.com/blog/why-governments-and-agencies-are-targeted-by-cyber-attacks-a-deep-dive-into-the-motives/), technology, telecom, media, retail, and [healthcare](https://www.sentinelone.com/blog/healthcare-cybersecurity-how-to-strengthen-defenses-against-cyber-attacks/) sectors for both [notoriety and financial gain](https://www.sentinelone.com/blog/ransoms-without-ransomware-data-corruption-and-other-new-tactics-in-cyber-extortion/).

According to reports, Kurtaj and the unnamed 17 year-old first met online and committed cyber trespassing, sneaking into cellphone network operator servers. This soon escalated to ransoms and the use of swiped data to break into several cryptocurrency wallets. Prosecutors have noted the groups’ juvenile desire to defy and taunt victims, often leaving offensive messages after infiltrating systems. Kurtaj, who is autistic and deemed not fit to stand trial, did not appear in court to give evidence. Jurors were asked to determine whether the teen committed the alleged acts rather than to determine if he did so with criminal intent. These cases have simultaneously highlighted the vulnerability of teenage hackers and the need to enhance cyber defenses across the web.

## The Bad | macOS Malware “XLoader” Returns Disguised As Productivity App

A new variant of the macOS malware known as “[XLoader](https://www.sentinelone.com/blog/detecting-xloader-a-macos-malware-as-a-service-info-stealer-and-keylogger/)” has been discovered, now masquerading as an office productivity app called “OfficeNote”. In [findings](https://www.sentinelone.com/blog/xloaders-latest-trick-new-macos-variant-disguised-as-signed-officenote-app/) published this week, SentinelOne found that this version of XLoader is hidden within an Apple disk image named OfficeNote.dmg and signed with the developer signature “MAIT JAKHU (54YDV8NU9C).” Initially identified in 2020, XLoader functions as an information stealer and keylogger, operating under the Malware-as-a-Service (MaaS) model and succeeding the infamous [Formbook malware](https://www.sentinelone.com/blog/formbook-yet-another-stealer-malware/).

XLoader was first seen targeting macOS in 2021, when it was distributed by attackers as a Java program. The new XLoader variant uses the C and Objective C programming languages to avoid the limitations caused by the requirement for Java Runtime Environment, which isn’t installed by default on Mac devices. SentinelOne noted several instances of this artifact on VirusTotal throughout July 2023, suggesting a widespread campaign.

![XLoader submissions to VirusTotal July 2023](https://www.sentinelone.com/wp-content/uploads/2023/08/XLoader_2023_2.jpg)

XLoader submissions to VirusTotal July 2023

The malware pretends to be an office application named OfficeNote but in reality, installs a [Launch Agent](https://www.sentinelone.com/wp-content/uploads/2021/10/SentinelOne_macOS_Threat_Hunting_and_Incident_Response_A_Complete_Guide_update.pdf) in the background for persistent execution. Once active, XLoader captures clipboard data and information stored in directories linked to popular web browsers that could be exploited or sold to other threat actors. To evade analysis, XLoader employs evasion techniques against both manual and automated analysis. It also incorporates sleep commands to delay execution in an attempt to avoid detection.

SentinelOne concluded that XLoader remains a threat to macOS users and businesses, emphasizing the need for continued vigilance against such cyber threats. Customers of SentinelOne are automatically protected from this new variant of XLoader.

## The Ugly | US & UK Critical Infrastructure Targeted By Lazarus Group’s New RAT

DPRK-backed [Lazarus Group](https://www.sentinelone.com/blog/lazarus-operation-interception-targets-macos-users-dreaming-of-jobs-in-crypto/) has exploited a patched critical security vulnerability in [Zoho ManageEngine ServiceDesk Plus](https://www.sentinelone.com/blog/enterprise-security-essentials-top-12-most-routinely-exploited-vulnerabilities/) with the purpose of distributing a remote access trojan (RAT) named QuiteRAT. The targets of these attacks include internet backbone infrastructure and healthcare organizations in Europe and the US, according to [reports](https://blog.talosintelligence.com/lazarus-quiterat/) by security researchers this week. Additionally, in-depth analysis of the group’s attack infrastructure uncovered a new threat called [CollectionRAT](https://blog.talosintelligence.com/lazarus-collectionrat/).

QuiteRAT, a successor to MagicRAT and TigerRAT, exhibits similar capabilities but with a significantly smaller file size. The malware is built on the Qt framework, which adds complexity to its code and makes analysis more challenging for cyber defenders. The attacks, observed in early 2023, involved exploiting [CVE-2022-47966](https://nvd.nist.gov/vuln/detail/cve-2022-47966), a vulnerability that emerged just five days before the first attack in a proof-of-concept (PoC) to deploy QuiteRAT from a malicious URL. Unlike MagicRAT, QuiteRAT lacks a built-in persistence mechanism and requires the server to issue commands for ongoing activity on compromised hosts.

The [Lazarus Group](https://www.sentinelone.com/blog/smoothoperator-ongoing-campaign-trojanizes-3cx-software-in-software-supply-chain-attack/) is also observed incorporating [open-source](https://www.sentinelone.com/blog/open-source-security/) tools and frameworks for initial access in their attacks as opposed to using them solely post-compromise. The reports indicate the use of the open-source DeimosC2 framework and CollectionRAT for various malicious activities, such as gathering metadata, executing commands, managing files, and delivering payloads.

![](https://www.sentinelon...