---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 18
url: https://buaq.net/go-161890.html
source: unSafe.sh - 不安全
date: 2023-05-06
fetch_date: 2025-10-04T11:38:33.743804
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 18

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

![](https://8aqnet.cdn.bcebos.com/8d0d7473f2ca7a624236919a599f95fb.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 18

International Seizure | Police Shutdown 9 Cryptocurrency Laundering ExchangesA multi-level collabo
*2023-5-5 21:0:13
Author: [www.sentinelone.com(查看原文)](/jump-161890.htm)
阅读量:28
收藏*

---

## International Seizure | Police Shutdown 9 Cryptocurrency Laundering Exchanges

A multi-level collaboration between the FBI, DoJ, and Ukrainian Cyber and National Police this week culminated in the seizure of nine [cryptocurrency](https://www.sentinelone.com/blog/lazarus-operation-interception-targets-macos-users-dreaming-of-jobs-in-crypto/) laundering websites. According to authorities, the sites were used mainly by cybercriminals and ransomware groups for money laundering and crypto exchange services. The joint takedown also includes all servers related to the sites.

> Last week, the FBI and international partners disrupted nine virtual currency exchange services which facilitated money laundering and allowed users to avoid law enforcement detection. [#CyberIsATeamSport](https://twitter.com/hashtag/CyberIsATeamSport?src=hash&ref_src=twsrc%5Etfw) <https://t.co/GqtlzI7g2b> [pic.twitter.com/sCllgynKnZ](https://t.co/sCllgynKnZ)
>
> — FBI (@FBI) [May 2, 2023](https://twitter.com/FBI/status/1653192182336036865?ref_src=twsrc%5Etfw)

In their [press release](https://www.justice.gov/usao-edmi/pr/fbi-disrupts-virtual-currency-exchanges-used-facilitate-criminal-activity), the FBI listed the domains `24xbtc.com`, `100btc.pro`, `pridechange.com`, `101crypta.com`, `uxbtc.com`, `trust-exchange.org`, `bitcoin24.exchange`, `paybtc.pro`, and `owl.gold`; all of which violated virtual currency codes of conduct to create haven for criminal activities and support the greater cybercrime ecosystem. These sites had boasted lax or no Know Your Customer (KYC) and Anti-Money Laundering (AML) measures and many also advertised forums dedicated to discussing [criminal activity](https://www.sentinelone.com/cybersecurity-101/what-is-crypto-malware/).

Illicit websites such as these nine allow users to convert [stolen](https://www.sentinelone.com/blog/is-cryptojacking-going-out-of-fashion-or-making-a-comeback/) cryptocurrency into coins that are harder to trace, blurring the money trail and enabling criminals to anonymously launder their wares under the radar. Reports noted that most of the sites provided live support and instructions in both English and Russian to service a wider range of customers.

Crackdowns like this one have become a primary goal across global law enforcement groups as they race to disrupt hackers’ financial infrastructures and stop the use of stolen goods that further fund malicious activity. Confiscated sites allow authorities to identify associated criminals, possibly leading to more arrests in the future or valuable intel on threat actors’ operational trends.

## Kimsuky APT | New Recon Tool Expands Cyber Attacks On Global Organizations

In a new [report](https://www.sentinelone.com/labs/kimsuky-evolves-reconnaissance-capabilities-in-new-global-campaign/) published by SentinelLabs this week, researchers revealed that a North Korean-backed APT known as “Kimsuky” has been deploying a previously unseen spy tool in active threat campaigns against Asian, North American, and European organizations. Since 2012, activity from the threat group has indicated their focus on collecting intel through [cyber espionage](https://www.sentinelone.com/labs/winter-vivern-uncovering-a-wave-of-global-espionage/) for the North Korean government.

Previous campaigns by Kimsuky often featured the deployment of a malware family called [BabyShark](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/). The new report by SentinelLabs highlights an expansion in the groups’ arsenal – the use of an evolved version of BabyShark that includes a reconnaissance capability. Dubbed ‘ReconShark’, this [reconnaissance](https://www.sentinelone.com/cybersecurity-101/lateral-movement/) tool has been observed using unique execution instructions and server communication methods.

ReconShark is deployed through [spear phishing](https://www.sentinelone.com/cybersecurity-101/spear-phishing/) emails; ones crafted to specifically target an individual directly. To increase the likelihood of success, the emails are seen to be properly formatted, branded, and abuse the names of real people associated with the email’s fake content. Kimsuky emails include links to download a lure document containing macros that activate the malware on close. Once activated, ReconShark exfiltrates running processes, battery information, and any endpoint threat detection solutions deployed on the infected platform. Additionally, the malware deploys more payloads through scripts, macro-enabled MS Office templates, or as Windows DLL files.

[![Malicious Document, themed to DPRK / China](https://www.sentinelone.com/wp-content/uploads/2023/05/Kimsuky_reconshark_5.jpg)](https://www.sentinelone.com/labs/kimsuky-evolves-reconnaissance-capabilities-in-new-global-campaign/kimsuky_reconshark_5/)

Malicious Document, themed to DPRK / China

North Korean state-sponsored APTs continue to [evolve](https://www.cisa.gov/northkorea) their tools, tactics, and techniques to more effectively target their victims. As we see more cases of advanced [social engineering](https://www.sentinelone.com/blog/the-dangers-of-social-engineering-how-to-protect-your-organization/) and sophisticated [malware](https://www.sentinelone.com/cybersecurity-101/what-is-malware-everything-you-need-to-know/) attacks, organizations in all sectors should continue to take preventative measures against identity based threats, implement multi-factor authentication, and train users on the signs of phishing.

## macOS Threats | Infostealer Sold on Telegram Eyes Up YouTube Campaign

Further research into [Atomic Stealer](https://www.sentinelone.com/blog/atomic-stealer-threat-actor-spawns-second-variant-of-macos-malware-sold-on-telegram/) this week revealed the threat actor behind the version being sold on Telegram has developed a second version that appears to be a trojan game installer looking to lure victims through YouTube.

As advertised in a Telegram channel, Atomic Stealer promises cybercriminals a full-fledged infostealer capable of grabbing keychain passwords, browser data, and [session cookies](https://www.sentinelone.com/blog/session-cookies-keychains-ssh-keys-and-more-7-kinds-of-data-malware-steals-from-macos-users/). The malware is also known to steal crypto wallets, targeting numerous popular cryptocurrency extensions to nab credentials. The going price is $1000 per month and includes a ready-for-use web interface for threat campaign management.

A second version of the malware was [discovered this week](https://www.sentinelone.com/blog/atomic-stealer-threat-actor-spawns-second-variant-of-macos-malware-sold-on-telegram/) that appears to be associated with a YouTube channel advertising “Crypto ALMV”, supposedly a game offering with crypto wallet integration that promises “secure cryptocurrency wallet in metaverse”.

![](https://www.sentinelone.com/wp-content/uploads/2023/05/atomic_stealer_10.jpg)

Distributed as a stand-alone executable called ‘Game Installer’, the malicious binary contains functions to steal passwords, wallets and browser secrets. Tellingly, the author left strings such as “ATOMIC STEALER” embedded in the binary. Given that the Telegram variant reached out to a URL of `amos-malware[.]ru/sendlogillegal`, it’s clear the author isn’t expectin...