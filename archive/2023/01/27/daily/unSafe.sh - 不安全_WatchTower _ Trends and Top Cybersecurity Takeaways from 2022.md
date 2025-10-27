---
title: WatchTower | Trends and Top Cybersecurity Takeaways from 2022
url: https://buaq.net/go-146772.html
source: unSafe.sh - 不安全
date: 2023-01-27
fetch_date: 2025-10-04T04:56:36.263187
---

# WatchTower | Trends and Top Cybersecurity Takeaways from 2022

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

![](https://8aqnet.cdn.bcebos.com/987f990f77362b0af465b7695ee053fe.jpg)

WatchTower | Trends and Top Cybersecurity Takeaways from 2022

read file error: read notes: is a directory
*2023-1-26 22:0:15
Author: [www.sentinelone.com(查看原文)](/jump-146772.htm)
阅读量:20
收藏*

---

Gathering information about cyber attacks is only half of the battle – the other half lies in curating the raw data into original insights about major vulnerabilities, cybercrime toolkits, and ransomware groups.

In this blog post, SentinelOne’s [WatchTower](https://www.sentinelone.com/global-services/watchtower/) team reflects on a year’s worth of threats observed and investigated across every geography and industry our partners operate in. Based on telemetry from tens of millions of endpoints protected by [Singularity XDR](https://www.sentinelone.com/platform) platform, here’s a review of the top cyber attack trends from 2022 and their significance in the fluctuating threat landscape.

![](https://www.sentinelone.com/wp-content/uploads/2023/01/WatchTower-Trends-and-Top-Cybersecurity-Takeaways-from-2022.jpg)

## Trends In the Landscape | 2022 Top Cybersecurity Takeaways

Findings from 2022 show the top ransomware variants, initial infection vectors, and emerging malware that organizations from all sectors contended with.

### Ransomware Findings

Over the course of last year, ransomware showed no signs of slowing down. Faced with federal level sanctions, the act of rebranding is now a widespread strategy ransomware groups use to obfuscate their identities and sidestep crackdowns. Several new ransomware groups emerged in 2022 and existing ones rebranded before showing their faces in the threat landscape once more.

* [Quantum](https://www.youtube.com/watch?v=gn1Xyc4RpjM) ransomware operation became Dagon Locker
* Notorious cybergang [Conti](https://www.youtube.com/watch?v=xt1yk3npOHE) siphoned their brand into smaller groups including [Hive](https://www.youtube.com/watch?v=b4ZHK3Ehigs), [BlackCat](https://www.youtube.com/watch?v=zjc0s9AB1Zo), and [HelloKitty](https://www.youtube.com/watch?v=xd5bbMY91FE)
* DarkSide transitioned into [BlackMatter](https://www.youtube.com/watch?v=aDtoxdLhTTk), followed by further splinters including [AlphV](https://www.sentinelone.com/labs/crimeware-trends-ransomware-developers-turn-to-intermittent-encryption-to-evade-detection/).
* [DoppelPaymer](https://www.youtube.com/watch?v=lw3CjPQ4nNA) rebranded into Grief
* [Rook](https://www.youtube.com/watch?v=J5ywO1jzkk4) ransomware transitioned into [Pandora](https://www.youtube.com/watch?v=E1kxhUtd3qo)

Ransomware authors have also widely adopted both Rust and Golang in their efforts to evade detection. BlackCat, Hive and a host of other ransomware families made the switch. taking advantage of their fast file encryption capabilities and wide-ranging cryptographic libraries.

### Growing Infection Vectors

2022 saw a steep increase in [supply chain attacks](https://www.sentinelone.com/blog/defending-the-enterprise-against-digital-supply-chain-risk-in-2022/), [SEO poisoning/malvertising](https://www.sentinelone.com/blog/breaking-down-the-seo-poisoning-attack-how-attackers-are-hijacking-search-results/), and cracked software. The growing theme in attacks from last year saw threat actors steering towards the path of least resistance for greater rewards.

Through software supply chain attacks, actors exploit weaknesses in a vendor’s development cycle to inject malicious code into a certified application. While many organizations have worked to monitor and detect such threats since the attack on [SolarWinds in 2020](https://www.sentinelone.com/blog/fireeye-breached-taking-action-and-staying-protected/), threat actors are still leveraging open-source modules for initial intrusion. Identity management giant, Okta for example, found themselves the target of a [supply chain attack](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-36-4/) last year when its 2FA provider, Twilio, was breached.

[SEO poisoning](https://www.sentinelone.com/blog/breaking-down-the-seo-poisoning-attack-how-attackers-are-hijacking-search-results/) has also risen to the top as a way for threat actors to take advantage of existing infrastructure for malicious purposes. By poisoning the mechanisms that influence search engine optimization (SEO), attackers have been able to quickly lure and infect unsuspecting users with commodity malware. Cracked software follows the same theme, banking on victims to download unlocked, illegal software which is embedded with dangerous malware.

### Malware Innovations

Attackers were observed attempting to neutralize and sidestep endpoint detection and response (EDR) tools over the past year, using bypass techniques and known vulnerabilities. In February 2022, the FBI and United States Secret Service (USSS) released a joint cybersecurity [advisory](https://www.ic3.gov/Media/News/2022/220211.pdf) warning against BlackByte ransomware group known for using a “Bring Your Own Driver” technique to circumvent various EDR products available on the market today.

A table of ransomware groups that created modules attempting to kill EDR solutions in 2022 is provided below. SentinelOne offers robust anti-tamper capabilities to protect against these attacks.

![ransomware edr bypass](https://www.sentinelone.com/wp-content/uploads/2023/01/WatchTower_2022_5.jpg)

The threat intelligence community observed new wiper malware samples and ransomware strains circulating in Ukrainian organizations. The malware was distributed  with the goal of rendering their computer systems inoperable. [HermeticWiper and PartyTicket ransomware](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack/) were among the novel threats that prefaced the unprovoked Russian invasion of Ukraine that have since evolved to produce several new malware variants. SolarMarker infostealer, [Bumblebee](https://www.sentinelone.com/blog/microsoft-active-directory-as-a-prime-target-for-ransomware-operators/) downloader, and the [Raspberry Robin](https://www.sentinelone.com/labs/who-needs-macros-threat-actors-pivot-to-abusing-explorer-and-other-lolbins-via-windows-shortcuts/) worm (*aka* QNAP worm, or LNK worm) also emerged as popular tools for cyberattackers in 2022.

## 2022 Most Used Commodity Tooling & Techniques

Attackers will always look for opportunities to do less work for more damage. They don’t always use sophisticated and customized malware and often rely on the same public tools used by network administrators and security professionals.

The most notable commodity tooling observed in 2022 by threat tactic are as follows:

* Reconnaissance – Ipconfig, Net.exe, Netstat, Nslookup, arp.exe, [WMI](https://www.sentinelone.com/labs/labscon-replay-blasting-event-driven-cornucopia-wmi-based-user-space-attacks-blind-siems-and-edrs/), [Impacket](https://www.sentinelone.com/labs/moshen-dragons-triad-and-error-approach-abusing-security-software-to-sideload-plugx-and-shadowpad/), [Cobalt Strike](https://www.sentinelone.com/cybersecurity-101/what-is-cobalt-strike/), Whoami, ADFind, ADRecon.py, Advanced Port Scanner, IP Scanner, PingCastle, Powerview, and Winrm
* Credential Theft – [Mimikatz](https://www.sentinelone.com/cybersecurity-101/mimikatz/), Meterpreter, Cobalt Strike, [BloodHound](https://www.sentinelone.com/blog/deep-dive-exploring-an-ntlm-brute-force-attack-with-bloodhound/), SharpHound, ProcDump, Process Hacker, ninjacopy, NirSoft, Lazagne, and PassView
* Lateral Movement – Psexec, PDQ Install, Winrm, SMB, WMI, RDP, SSH
* Remote Access – TeamViewer, AnyDesk, Splashto...