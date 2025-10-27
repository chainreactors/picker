---
title: 12 Months of Fighting Cybercrime & Defending Enterprises | SentinelLabs 2022 Review
url: https://buaq.net/go-141592.html
source: unSafe.sh - 不安全
date: 2022-12-28
fetch_date: 2025-10-04T02:34:46.884352
---

# 12 Months of Fighting Cybercrime & Defending Enterprises | SentinelLabs 2022 Review

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

![](https://8aqnet.cdn.bcebos.com/0a30fae3332acf4dffcfed850f800ffc.jpg)

12 Months of Fighting Cybercrime & Defending Enterprises | SentinelLabs 2022 Review

2022 has been another eventful year for the SentinelLabs research team, with events in Ukraine domi
*2022-12-27 19:24:55
Author: [www.sentinelone.com(查看原文)](/jump-141592.htm)
阅读量:27
收藏*

---

2022 has been another eventful year for the SentinelLabs research team, with [events in Ukraine](https://s1.ai/hermetic) dominating and directing a large portion of our research output. We also hosted the first ever [LABScon](https://www.labscon.io), bringing together top tier researchers and thought leaders from across the industry, and found time to investigate a number of [supply chain attacks](https://www.sentinelone.com/labs/pypi-phishing-campaign-juiceledger-threat-actor-pivots-from-fake-apps-to-supply-chain-attacks/), [adversaries](https://www.sentinelone.com/labs/the-mystery-of-metador-an-unattributed-threat-hiding-in-telcos-isps-and-universities/), [macOS](https://www.sentinelone.com/labs/use-of-obfuscated-beacons-in-pymafka-supply-chain-attack-signals-a-new-trend-in-macos-attack-ttps/), [Linux](https://s1.ai/crate) and [Windows](https://www.sentinelone.com/labs/who-needs-macros-threat-actors-pivot-to-abusing-explorer-and-other-lolbins-via-windows-shortcuts/) malware, and [exploitable vulnerabilities](https://s1.ai/azure-iot).

We’ve seen a [shift in ransomware TTPs](https://www.sentinelone.com/blog/ransoms-without-ransomware-data-corruption-and-other-new-tactics-in-cyber-extortion/) with increasing use of [hybrid and partial encryption](https://www.sentinelone.com/labs/crimeware-trends-ransomware-developers-turn-to-intermittent-encryption-to-evade-detection/) and a greater focus from threat actors on stealing data for ransom as well as – and sometimes instead of – using file lockers.

All our research and threat intelligence posts can be found on the [SentinelLabs home page](https://labs.sentinelone.com/), but for a quick recap of the year’s main highlights, take a scroll through the 2022 timeline below.

![12 Months of Fighting Cybercrime & Defending Enterprises SentinelLabs 2022 Review](https://www.sentinelone.com/wp-content/uploads/2022/12/12-Months-of-Fighting-Cybercrime-Defending-Enterprises-SentinelLabs-2022-Review.jpg)

## January

In January, we identified new variants of the PowGoop malware belonging to Iranian-linked threat actor [MuddyWater](https://www.sentinelone.com/labs/wading-through-muddy-waters-recent-activity-of-an-iranian-state-sponsored-threat-actor/). We described how this adversary used tunneling tools and likely exploited CVE-2020-0688 on Exchange servers to compromise governmental organizations in the Middle East. Like many other Iranian threat actors, the group displays less sophistication and technological complexity compared to other state-sponsored APT groups but continues to be successful through its use of publicly available offensive security tools and exploitation of unpatched vulnerabilities.

[![Wading Through Muddy Waters | Recent Activity of an Iranian State-Sponsored Threat Actor](https://www.sentinelone.com/wp-content/uploads/2022/01/Wading-Through-Muddy-Waters-Recent-Activity-of-an-Iranian-State-Sponsored-Threat-Actor-5.jpg)](https://www.sentinelone.com/labs/wading-through-muddy-waters-recent-activity-of-an-iranian-state-sponsored-threat-actor/)

January also saw SentinelLabs post research on threat hunting for [macOS adware infections](https://www.sentinelone.com/labs/a-threat-hunters-guide-to-the-macs-most-prevalent-adware-infections-2022/), recent [hacktivist campaigns](https://www.sentinelone.com/labs/hacktivism-and-state-sponsored-knock-offs-attributing-deceptive-hack-and-leak-operations/), and analyses of [BlackCat ransomware](https://www.sentinelone.com/labs/blackcat-ransomware-highly-configurable-rust-driven-raas-on-the-prowl-for-victims/), and CVE-2021-45608 – a [flaw in NetUSB](https://www.sentinelone.com/labs/cve-2021-45608-netusb-rce-flaw-in-millions-of-end-user-routers/) affecting millions of routers.

## February

The Russian invasion of Ukraine in February 2022 was an event that had, and continues to have, a global impact. It was widely expected that the Russian campaign would be swift and decisive, and accompanied by an equally destructive cyber warfare campaign. Those expectations turned out to be far from correct. While the resolve of the Ukrainians took both the Russians and many observers by surprise, the cyber campaigns associated with the war also had an unexpected dimension. In February, the first of these was a new destructive wiper that SentinelLabs dubbed [Hermetic Wiper](https://s1.ai/hermetic), a signed driver targeting Windows devices in Ukrainian organizations.

[![](https://www.sentinelone.com/wp-content/uploads/2022/02/Hermetic-Wiper-Ukraine-is-Under-Attack-3.jpg)](https://s1.ai/hermetic)

This month, SentinelLabs also exposed a decade-old state-sponsored adversary named [ModifiedElephant](https://www.sentinelone.com/labs/modifiedelephant-apt-and-a-decade-of-fabricating-evidence/) targeting human rights activists, lawyers, academics and others involved in civilian dissent in India. The objective of ModifiedElephant is long-term surveillance that at times concludes with the delivery of ‘evidence’—files that incriminate the target in specific crimes—prior to conveniently coordinated arrests.

SentinelLabs also reported on an Iranian threat actor, [TunnelVision](https://www.sentinelone.com/labs/log4j2-in-the-wild-iranian-aligned-threat-actor-tunnelvision-actively-exploiting-vmware-horizon/), exploiting the Log4j2 and other vulnerabilities against Middle East and US targets.

## March

As the war in Ukraine gathered pace, so did the cyber attacks: WhisperKill, WhisperGate, HermeticWiper, IsaacWiper, CaddyWiper, and DoubleZero were all reported on across the industry, but [AcidRain](https://www.sentinelone.com/labs/acidrain-a-modem-wiper-rains-down-on-europe/) saw a new development. An attempt to take out Ukrainian military command-and-control capabilities by hindering satellite connectivity spilled over to affect German infrastructure with remote monitoring and control of almost 6000 Enercon wind turbines disrupted by an attack on Viatsat modems.

[![](https://www.sentinelone.com/wp-content/uploads/2022/03/AcidRain-A-Modem-Wiper-Rains-Down-on-Europe-1.jpg)](https://www.sentinelone.com/labs/acidrain-a-modem-wiper-rains-down-on-europe/)

It turns out it hasn’t only been the Russians targeting Ukraine, either. In March, SentinelLabs reported on a Chinese threat actor [Scarab APT](https://www.sentinelone.com/labs/chinese-threat-actor-scarab-targeting-ukraine/) attempting to infect organizations in Ukraine with HeaderTip malware. Meanwhile, multiple critical severity flaws in [Microsoft Azure’s Defender for IoT](https://www.sentinelone.com/labs/pwning-microsoft-azure-defender-for-iot-multiple-flaws-allow-remote-code-execution-for-all/) were disclosed by SentinelLabs that could allow unauthenticated attackers to remotely compromise devices.

## April

In April, SentinelLabs’ focus turned to crimeware with research on LockBit 3.0 discovering that threat actors were [sideloading](https://www.sentinelone.com/labs/lockbit-ransomware-side-loads-cobalt-strike-beacon-with-legitimate-vmware-utility/) Cobalt Strike beacons via a signed VMware xfer logs command line utility. We subsequently discovered this technique was connected with an affiliate Microsoft tracks as DEV-0401, a threat actor that had not previously been known to use LockBit.

[![](https://www.sentinelone.com/wp-content/uploads/2022/...