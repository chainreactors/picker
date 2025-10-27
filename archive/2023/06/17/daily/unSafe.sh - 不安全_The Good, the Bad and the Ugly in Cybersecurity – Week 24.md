---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 24
url: https://buaq.net/go-169083.html
source: unSafe.sh - 不安全
date: 2023-06-17
fetch_date: 2025-10-04T11:46:48.283565
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 24

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

![](https://8aqnet.cdn.bcebos.com/f6ee1afc62f7d6cb4b0ae50dfe61eee5.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 24

The Good | Bulletproof Hosting Operator Enabling Major Crimeware ConvictedA Romanian national was
*2023-6-16 21:0:47
Author: [www.sentinelone.com(查看原文)](/jump-169083.htm)
阅读量:15
收藏*

---

## The Good | Bulletproof Hosting Operator Enabling Major Crimeware Convicted

A Romanian national was sentenced this week to three years in prison for running a bulletproof hosting service used by cybercriminals in various cyberattack operations. Mihai Ionut Paunescu, also known online as “Virus”, has been charged with conspiracy to commit computer intrusion for his involvement enabling a variety of cybercrimes from [DDoS](https://www.sentinelone.com/cybersecurity-101/what-is-denial-of-service-dos/) and spam-based attacks to [info-stealers](https://www.sentinelone.com/blog/detecting-xloader-a-macos-malware-as-a-service-info-stealer-and-keylogger/) and [banking malware](https://www.sentinelone.com/blog/goznym-banking-malware-gang-busted/).

[![](https://www.sentinelone.com/wp-content/uploads/2023/06/Mihai_Ionut_Paunescu.jpg)](https://www.sentinelone.com/?attachment_id=81696)

Source: ObservatorNews

[Bulletproof hosting](https://www.sentinelone.com/cybersecurity-101/bulletproof-hosting/) services enable cybercriminals to spread [malware](https://www.sentinelone.com/cybersecurity-101/what-is-malware-everything-you-need-to-know/) focused on stealing confidential information. These sites are unlawfully lenient about what material they allow their users to upload and are strategically located outside law enforcement jurisdictions, giving criminals the anonymity needed to host malware kits, [data stashes](https://www.sentinelone.com/cybersecurity-101/what-is-a-data-breach/), hidden [dark markets](https://www.sentinelone.com/cybersecurity-101/what-is-the-dark-web/), and more.

In a [statement](https://www.justice.gov/usao-sdny/pr/romanian-national-who-operated-bulletproof-hosting-service-facilitated-distribution) by the DoJ, Paunescu’s bulletproof hosting service played an intrinsic role in distributing some of the world’s most harmful malware including the Gozi virus, Zeus trojan, SpyEye trojan, and BlackEnergy malware. These are notorious names in the infosec world. Gozi, for example, is said to have infected more than a million systems, stealing banking information and passwords from government entities and businesses globally.

Court documents say that Paunescu was well-aware of the illegal doings of his criminal customer base. Not only did he shield paying customers from law enforcement groups by renting IP addresses from legitimate internet service providers (ISPs), he also provided C2 infrastructure for [botnet](https://www.sentinelone.com/cybersecurity-101/botnets/) operations and proxies to hide malicious traffic. Paunescu also monitored IP address spam lists for those under his control to stop them from being blocked and maintained a database of all rented servers – many of which were attached to known malware.

Paunescu has pleaded guilty to all charges and ordered to forfeit $3,510,000 and pay $18,945 in restitution and will face another three years of supervision after serving his term in prison.

## The Bad | Critical RCE Flaw In Fortinet SSL VPN Opens the Door to Further Attacks

After releasing a patch for a critical remote code execution (RCE) vulnerability in its FortiOS SSL VPN, Fortinet is now warning customers that the flaw may have been exploited in emerging attacks on government and critical infrastructure entities. The flaw, tracked as [CVE-2023-27997](https://nvd.nist.gov/vuln/detail/CVE-2023-27997), is described as a heap-based buffer overflow weakness in both the FortiOS and FortiProxy SSL VPN that could allow threat actors to gain RCE through malicious requests.

Fortinet’s latest [report](https://www.fortinet.com/blog/psirt-blogs/analysis-of-cve-2023-27997-and-clarifications-on-volt-typhoon-campaign) on the flaw found that one issue tracked as [FG-IR-23-097](https://www.fortiguard.com/psirt/FG-IR-23-097) was likely to have been exploited in a number of cases and that the company was working closely with its customers to monitor the developing situation. Fortinet also touched on the possibility that the Chinese-based threat actors linked to the recent [Volt Typhoon attacks](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a) could have their eyes set on the CVE-2023-27997 flaw. No confirmed link has been made between the two at the time of this writing, but the company does expect any unpatched vulnerabilities to continue facing exploitation in popular software and devices. Fortinet urges all its customers to continue prioritizing patching immediately upon release.

> Confirmed: Volt Typhoon used an auth bypass CVE-2022-40684 in FortiOS products for initial access
>
> Unconfirmed: If Volt Typhoon used the new CVE-2023-27997 in SSL VPNs – but Fortinet expects many threat actors, including Volt Typhoon, may have a go at it<https://t.co/y9Dlbjw9dY> <https://t.co/tbZDOfDGHU>
>
> — Will (@BushidoToken) [June 13, 2023](https://twitter.com/BushidoToken/status/1668415858605948934?ref_src=twsrc%5Etfw)

Due to their internet-facing nature and access to enterprise intranets, SSL VPNs continue to be a lucrative target for threat actors. Pre-authentication flaws such as CVE-2023-27997 are especially valuable to actors since they bypass the need for valid credentials.  Additionally to following stringent patch management processes, organizations can proactively protect themselves against new vulnerabilities by implementing [zero trust](https://www.sentinelone.com/cybersecurity-101/zero-trust-architecture/) policies and advanced security solutions such as [EDR](https://www.sentinelone.com/cybersecurity-101/what-is-endpoint-detection-and-response-edr/) and [XDR](https://www.sentinelone.com/cybersecurity-101/extended-detection-response-xdr/).

## The Ugly | BatCloak Obfuscation Tool Evading Static Antivirus Engines

Security researchers this week [warn](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/23/f/analyzing-the-fud-malware-obfuscation-engine-batcloak/tb-the-dark-evolution-advanced-malicious-actors-unveil-malware-modification-progression.pdf) the community about an obfuscation tool called “[BatCloak](https://www.youtube.com/watch?v=fuCOiKABGFM)” allowing actors to deliver malicious code under the guise of batch (.BAT) files. Having a high success rate, tools that leverage the BatCloak component have become increasingly popular amongst threat actors of all skill levels for its ease of use.

BatCloak is currently promoted as “fully undetectable malware”, or “FUD”, by its authors. FUD status is supposed to signify to buyers that the malware is sophisticated enough to remain completely undetectable in compromised systems. Slipping past [legacy AV](https://www.sentinelone.com/resources/7-reasons-to-move-away-from-legacy-av/) detection suites, FUD malware allows threat actors to carry out a variety of malicious activities. Though tools of this nature are tuned to evade static detection engines, they are readily detectable by modern behavioral and AI-powered solutions like SentinelOne.

According to the latest [research](https://www.trendmicro.com/en_us/research/23/f/analyzing-the-fud-malware-obfuscation-engine-batcloak.html) on BatCloak, the tool is said to demonstrate a remarkable ability to persistently avoid static detection. Samples going back to 2022 show that, through BatCloak, threat actors have been able to load numerous malware families ...