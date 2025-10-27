---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 44
url: https://buaq.net/go-133143.html
source: unSafe.sh - 不安全
date: 2022-10-29
fetch_date: 2025-10-03T21:11:23.121148
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 44

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

![](https://8aqnet.cdn.bcebos.com/465dc9c76c8eccbd4733def49b5ea83b.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 44

The GoodThis week, U.S. law enforcement charged a Ukrainian national for his alleged participation
*2022-10-28 21:0:5
Author: [www.sentinelone.com(查看原文)](/jump-133143.htm)
阅读量:23
收藏*

---

## The Good

This week, U.S. law enforcement [charged](https://www.justice.gov/usao-wdtx/pr/newly-unsealed-indictment-charges-ukrainian-national-international-cybercrime-operation) a Ukrainian national for his alleged participation in an international cybercrime operation known as Raccoon Infostealer. Authorities say the MaaS (Malware-as-a-Service) infostealer has infected millions of computers worldwide.

Mark Sokolovsky, 26, is currently being held in the Netherlands and is awaiting extradition to the U.S. Sokolovsky was arrested by Dutch police after fleeing Ukraine in March, [reportedly](https://thehackernews.com/2022/10/us-charges-ukrainian-hacker-over-role.html) in a Porsche Cayenne.

![raccoon stealer](https://899029.smushcdn.com/2131410/wp-content/uploads/2022/10/raccoon-stealer.jpg?lossy=0&strip=1&webp=0)

Raccoon Stealer is advertised in [cybercrime market places](https://www.sentinelone.com/blog/more-evil-markets-how-its-never-been-easier-to-buy-initial-access-to-compromised-networks/) and offers its services to other criminals for a subscription of $200 per month. The MaaS allows users access to the malware, which they subsequently deploy on victims’ computers via cracked software and [email phishing](https://www.sentinelone.com/cybersecurity-101/phishing-scams/) infection vectors.

After Sokolovksy’s arrest, authorities were able to temporarily take down the infrastructure supporting Raccoon Stealer and identified over 50 million unique credentials including bank accounts, cryptocurrency addresses, credit card numbers and other forms of identification stolen by the operators, many of which belong to U.S. citizens. The FBI has set up a [website](https://raccoon.ic3.gov/home) for any individuals wishing to check if their email address appears in the cache of stolen data.

If found guilty, Sokolovsky, who allegedly used various online nicknames including Photix, raccoonstealer and black21jack77777, faces a maximum penalty of 20 years in prison for wire fraud and money laundering.

Unfortunately, despite Sokolovsky’s arrest and the subsequent dismantling of Raccoon Stealer infrastructure, other members of the gang remain undeterred and have since stood up a new version of the infostealer, continuing to promote it in underground cybercrime forums. The FBI, the Department of Army Criminal Investigation Division (Army CID) and other law enforcement agencies continue to investigate the case.

## The Bad

Vice Society, a threat actor group which has been [disproportionately targeting](https://www.sentinelone.com/blog/cyber-risks-in-the-education-sector-why-cybersecurity-needs-to-be-top-of-the-class/) the U.S. education sector, continues to be a mounting concern as the threat actor adopts [multiple extortion techniques](https://www.sentinelone.com/blog/ransoms-without-ransomware-data-corruption-and-other-new-tactics-in-cyber-extortion/).

A [report](https://www.microsoft.com/en-us/security/blog/2022/10/25/dev-0832-vice-society-opportunistic-ransomware-campaigns-impacting-us-education-sector/) this week details the TTPs used by this threat actor as it continues its campaigns against school and colleges. The group variously deploys [BlackCat](https://www.sentinelone.com/labs/blackcat-ransomware-highly-configurable-rust-driven-raas-on-the-prowl-for-victims/), [HelloKitty](https://www.sentinelone.com/labs/hellokitty-ransomware-lacks-stealth-but-still-strikes-home/), QuantumLocker and custom versions of Zeppelin ransomware. In some intrusions, Vice Society demands a ransom without deploying ransomware, instead threatening victims with exposure of the leaked data.

![vice society ransomware](https://899029.smushcdn.com/2131410/wp-content/uploads/2022/10/vice-society-ransomware.jpg?lossy=0&strip=1&webp=0)

As described in a recent report authored by SentinelLabs researchers, data extortion has now evolved into a [spectrum of TTPs](https://www.sentinelone.com/blog/ransoms-without-ransomware-data-corruption-and-other-new-tactics-in-cyber-extortion/); Vice Society is just the latest example of a threat actor occupying a fluid position across that spectrum, adapting their approach according to the target.

The researchers note how Vice Society switches between deploying RaaS payloads such as BlackCat to “wholly-owned malware” like Zeppelin and even their own custom variants in different intrusions. In one intrusion, the operators exfiltrated hundreds of gigabytes of data by staging a [malicious PowerShell script](https://www.sentinelone.com/blog/windows-powershell-malicious/) on a network share.

The threat actors abuse registry commands to disable [Windows Defender](https://www.sentinelone.com/blog/living-off-windows-defender-lockbit-ransomware-sideloads-cobalt-strike-through-microsoft-security-tool/) and often prefer `comsvcs.dll` and MiniDump over [Mimikatz](https://www.sentinelone.com/cybersecurity-101/mimikatz/) for credential dumping. Vice Society has also been observed exploiting [PrintNightmare](https://www.sentinelone.com/blog/printnightmare-latest-patch-almost-puts-microsoft-vulnerability-to-bed/) to elevate privileges in a domain.

Security teams working in the education sector are urged to review Vice Society TTPs as well as bolster their cyber defenses more generally by deploying [a robust EDR](https://www.sentinelone.com/platform/highereducation/), reviewing [regularly exploited vulnerabilities](https://www.sentinelone.com/blog/enterprise-security-essentials-top-15-most-routinely-exploited-vulnerabilities-2022/), and using [device discovery](https://assets.sentinelone.com/iotranger/sentinel-one-ranger-) to find unmanaged devices on the network.

## The Ugly

This week, [hacktivists](https://www.sentinelone.com/cybersecurity-101/hacktivism/) have been busy causing disruption, dismay and offense in two unrelated intrusions. On Thursday, the New York Post reported that it had been the victim of a hack which took over its website and Twitter account. The attackers used their unauthorized access to post offensive content relating to various U.S. politicians, including President Biden and New York Rep. Alexandria Ocasio-Cortez.

> The New York Post has been hacked. We are currently investigating the cause.
>
> — New York Post (@nypost) [October 27, 2022](https://twitter.com/nypost/status/1585629621521100801?ref_src=twsrc%5Etfw)

Details of the attack so far remain sparse, but it’s not the first time New York Post’s owner, News Corp, has been targeted. A [breach](https://www.reuters.com/business/media-telecom/news-corp-says-one-its-network-systems-targeted-by-cyberattack-2022-02-04/) in January 2022 was speculatively attributed to a Chinese-linked APT, though it remains unclear at this time whether the cases are connected.

The Iranian Atomic Energy Organization (AEOI) is also investigating [a breach](https://www.bleepingcomputer.com/news/security/iran-s-atomic-energy-agency-confirms-hack-after-stolen-data-leaked-online/) apparently in support of the recent nationwide protests following the death of [Mehsa Amini](https://www.theguardian.com/world/2022/oct/27/this-generation-is-really-brave-iranians-on-the-protests-over-mahsa-aminis-death) in police custody. A hacktivist group calling itself ‘Black Reward’ has leaked 85000 sensitive email messages stolen from servers belonging to one of the...