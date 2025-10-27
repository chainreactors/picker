---
title: Cybersecurity In The Fast Lane | Why Speed Is Key In Incident Response & Mitigation
url: https://buaq.net/go-171390.html
source: unSafe.sh - 不安全
date: 2023-07-07
fetch_date: 2025-10-04T11:52:27.818155
---

# Cybersecurity In The Fast Lane | Why Speed Is Key In Incident Response & Mitigation

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

![](https://8aqnet.cdn.bcebos.com/2a42915349e82617ac7ccc5bd89734fc.jpg)

Cybersecurity In The Fast Lane | Why Speed Is Key In Incident Response & Mitigation

Threat actors are constantly evolving, consistently developing the tools, tactics, and procedures (
*2023-7-6 21:59:58
Author: [www.sentinelone.com(查看原文)](/jump-171390.htm)
阅读量:20
收藏*

---

Threat actors are constantly evolving, consistently developing the tools, tactics, and procedures ([TTPs](https://www.sentinelone.com/blog/inside-the-mind-of-a-cyber-attacker-tactics-techniques-and-procedures-ttps-every-security-practitioner-should-know/)) they use in attacks. In today’s threat landscape, enterprises of all sizes and industries find themselves pitted against professional cybercriminal gangs, [advanced persistent threat](https://www.sentinelone.com/cybersecurity-101/advanced-persistent-threat-apt/) (APT) groups, and even nation-state actors – all of whom are leveraging faster attack methods than ever before.

In addition to sophisticated TTPs and how organized many cybercrime-as-a-service models have become, enterprises also face the reality of how quickly active threats can become full-blown incidents. Speed, in both cybersecurity and cyberattacks, is the key metric to pay attention to as it defines the success of either the attacker or the defender.

This blog discusses the metric of speed in context of modern [threat actors](https://www.sentinelone.com/cybersecurity-101/threat-actor/), their methods, and how enterprise security teams can shave off critical seconds and minutes in their own detection and response processes.

![](https://www.sentinelone.com/wp-content/uploads/2023/07/Cybersecurity-In-The-Fast-Lane-Why-Speed-Is-Key-In-Incident-Response-Mitigation-6.jpg)

## Threat Actors Are Picking Up Their Speed

Technology has changed dramatically in the last few years alone, becoming smarter, faster, and more advanced. While enterprises use the latest software and tools to further their businesses, threat actors have done the same to level up their attack methods.

### Ransomware Attacks

Consider one of the most significant takeaways from Mandiant’s latest [M-Trends report](https://www.mandiant.com/resources/blog/m-trends-2023): The global median dwell time – the time marking the beginning of an intrusion and the moment it is identified – is dropping year over year. At a mere 16 days of average dwell time for 2022, this may seem like a positive development as threat actors are spending less time inside a system post-entry. However, skyrocketing counts of [ransomware](https://www.sentinelone.com/cybersecurity-101/ransomware/) attacks on global businesses give a good indication as to why average dwell times are on the decline.

Though some of the reduction in dwell time is attributed to improved detection and response capabilities, ransomware has become a digital pandemic, targeting victims in all industry verticals. Given its high earning potential for a relatively short attack time frame, ransomware attacks are highly lucrative for threat actors and are protected by security experts to continue rising in both frequency and severity.

### Drive-By Download Attacks

As their name suggests, drive-by downloads are stealthy, fast, and often happen before the victim even knows what’s happening. This type of cyberattack is employed by cybercriminals to infect a victim’s device with [malware](https://www.sentinelone.com/cybersecurity-101/what-is-malware-everything-you-need-to-know/) without their knowledge or consent. It typically occurs when they visit a compromised website or click on a malicious link embedded in an email or advertisement.

The attack then takes advantage of vulnerabilities in web browsers, plugins, or operating systems, allowing the malware to be automatically downloaded and executed on the victim’s device. Drive-by downloads require only the bare minimum of a victim’s interaction, making them a potent tool for spreading malware, stealing sensitive information, and gaining unauthorized access to systems.

### Mass Scanning For Vulnerabilities

Based on new [research](https://www.paloaltonetworks.com/unit42/2022-incident-response-report), security defenders have a real race against the clock to patch new vulnerabilities. Researchers have found that threat actors start to perform mass, internet-wide scans for vulnerable [endpoints](https://www.sentinelone.com/cybersecurity-101/endpoint-security/) within just 15 minutes after a new CVE is disclosed. Threat actors consistently monitor vendor bulletins and software update channels for the latest announcements on vulnerabilities and proof of concepts that they can leverage in their next attack. Oftentimes, these fresh vulnerabilities provide them with the capability to perform remote code execution (RCE) and gain access to corporate networks.

Patch management is a continuous and, for many organizations, arduous task that requires security teams to try to keep up with all the latest security threats and issues in various operating systems. Since performing these internet-wide scans do not require a deep skill set, even low-level criminals are able to take advantage, sometimes even selling their scan results to more experienced actors.

### Zero-Day Exploits

Threat actors are gaining momentum on how quickly they can exploit [zero-days](https://www.sentinelone.com/cybersecurity-101/zero-day-vulnerabilities-attacks/). In a recent [Vulnerability Intelligence Report](https://www.rapid7.com/blog/post/2023/02/28/a-shifting-attack-landscape-rapid7s-2022-vulnerability-intelligence-report/), researchers cited time-to-exploit as being the critical metric for security practitioners. Over the past three years, the time measured between disclosure and known exploitation has decreased steadily, going from 30% of vulnerabilities exploited in the wild within one week in 2020 to 56% found exploited within one week in 2022. Zero-days are most often exploited to provide initial access for ransomware gangs.

### Growing Availability of Off-The-Shelf-Tools

Apart from APT groups, full-fledged ransomware gangs, and nation-backed threat actors, low-level cybercriminals are taking their shot on enterprises due to the widening availability of ready-to-use hacking tools. These tools, including exploit kits, infostealers, scanners, [password](https://www.sentinelone.com/cybersecurity-101/password-security-business-tips/) crackers, and attack simulation tools, are commonly available on forums and [darknet markets](https://www.sentinelone.com/blog/more-evil-markets-how-its-never-been-easier-to-buy-initial-access-to-compromised-networks/) and significantly lower the barrier to launching serious cyberattacks.

As the market for selling pre-made tools continues to expand, cybercriminals with little to no technical expertise are now able to quickly find and purchase pre-existing scripts to launch attacks on computer systems and networks.

## Deciphering How Actors Move Across The Cyber Attack Lifecycle

Though cyber threat actors are moving swiftly, there are ways for enterprise businesses to stay ahead and safeguard their critical data and systems. Understanding how actors [maneuver](https://www.sentinelone.com/cybersecurity-101/cyber-kill-chain/) before and during their attacks allows defenders to put in the right safeguards in place.

* Planning Phase – Before the act of attack, threat actors will select their target and work to identify exploitable aspects of their operations. This refers to any low hanging fruits such as unpatched vulnerabilities, misconfigurations, administrative users on unprotected devices, and...