---
title: The Gentlemen RaaS Uses GentleKiller EDR Framework Targeting 400 Security Processes
url: https://thehackernews.com/2026/06/the-gentlemen-raas-uses-gentlekiller.html
source: The Hacker News
date: 2026-06-19
fetch_date: 2026-06-20T06:14:42.215242
---

# The Gentlemen RaaS Uses GentleKiller EDR Framework Targeting 400 Security Processes

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [The Gentlemen RaaS Uses GentleKiller EDR Framework Targeting 400 Security Processes](https://thehackernews.com/2026/06/the-gentlemen-raas-uses-gentlekiller.html)

**Ravie Lakshmanan**Jun 19, 2026Ransomware / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjNWtaK_WkFnKnaLTIwg043i_I6YVi5XuZGVzh30SGeK-iutwr6t2Ed3S6Qk0V9uykYueDD5WETtQ4sW1QwG4jldPXW_IM2woF1Dk1PXcNxbwv6sgoprJ6m8pmogRc0vblucj3nf6Tox_ptxOX9bib6iO4bV4SXVVFoVzUGw0C8cSiJEvq3nDgUZ36G9xp/s1700-e365/edr-killer.jpg)

The Gentlemen ransomware-as-a-service (RaaS) operation is actively developing and maintaining a suite of endpoint detection and response (EDR) killers that it hands out to affiliates for impairing system defenses before deploying the encryptor.

This mature portfolio of [EDR-terminating tools](https://thehackernews.com/2026/03/54-edr-killers-use-byovd-to-exploit-34.html) is centered around a framework that's known as **GentleKiller**.

"They also incorporate third-party or leaked tools such as HexKiller, ThrottleBlood, and HavocKiller," ESET security researcher Jakub Souček [said](https://www.welivesecurity.com/en/eset-research/killing-me-gently-inside-gentlemens-edr-killer-framework/) in a report shared with The Hacker News. "These tools are standardized through a shared defense-evasion layer, impersonating predominantly security vendors using fake version information, and copied legitimate certificates and icons."

The Slovakian cybersecurity company also called out the ransomware crew for its ability to "unusually quickly operationalize" newly disclosed proof-of-concept (PoC) exploits related to an attack technique called the bring your own vulnerable driver ([BYOVD](https://thehackernews.com/2026/06/dragonforce-hackers-abuse-microsoft.html)) technique, in many cases within days of their public release.

Since its emergence in March 2025, [The Gentlemen](https://thehackernews.com/2026/06/the-gentlemen-ransomware-claims-478.html) has swiftly risen up the ranks and made a name for itself as one of the most active ransomware groups. Per data from Ransomware.live, the group has claimed [504 victims to date](https://ransomware.live/group/thegentlemen), with most of them located in Southeast Asia, South America, and Western Europe.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Recent reports from cybersecurity journalist Brian Krebs and PRODAFT have revealed that a 36-year-old Russian national named Alexander Andreevich Yapaev (aka hastalamuerte) has been leading the operation, after acting as an affiliate for other ransomware schemes, including Qilin.

ESET has described The Gentlemen as one of the most technically agile RaaS groups, using a set of techniques to ensure that the compiled EDR killer samples sidestep detection. This includes binary protection using Enigma or Themida and using file names that resemble well-known cybersecurity vendors, right down to their version information, digital signatures, and icons.

The most prevalent of them is GentleKiller, which comes in eight different variants, each mimicking a different legitimate product and abusing a different vulnerable or malicious driver as part of the BYOVD attack. GentleKiller specifically looks for 400 processes associated with 48 distinct security programs from a number of vendors.

The list of drivers exploited by each of the variants is as follows -

* Kaspersky ("eb.sys")
* FACEIT Anti-Cheat ("nseckrnl.sys")
* Valorant ("GameDriverX64.sys")
* Javelin ("stpm\_old.sys" or "stpm\_new.sys")
* WatchDog ("dmx.sys")
* Network Blocker ("360netmon\_wfp.sys")
* Cleaner ("IMFForceDelete.sys")
* G11 ("PoisonX.sys")

It's worth noting that the abuse of "PoisonX.sys" has been recorded in recent months in connection with various BYOVD attacks, one of which was [used to kill CrowdStrike Falcon EDR](https://threatlabsnews.xcitium.com/blog/reverse-engineering-a-0-day-poisonx-byovd-driver-bypasses-crowdstrike-edr/). A second campaign, [detailed](https://www.huntress.com/blog/uptick-bomgar-exploitation) by Huntress, involved an intrusion in which unknown threat actors leveraged BeyondTrust Remote Support to successfully deploy ransomware on the network, but not before terminating security tooling via "PoisonX.sys" and "hrwfpdrv.sys."

"When abstracting away the impersonation layer and the specific drivers used, the underlying code reveals numerous structural and behavioral commonalities that strongly suggest the use of a shared development template," Souček said.

"This design prioritizes ease of deployment and operational flexibility for affiliates, while minimizing development effort for the operators. It allows The Gentlemen operators to integrate abused drivers into their toolset very soon after an EDR killer PoC is disclosed."

The third-party, BYOVD-based EDR killers employed by the group are below -

* HexKiller ("googleApiUtil64.sys"), a tool previously assumed to be exclusive to the Warlock ransomware gang
* ThrottleBlood ("ThrottleBlood.sys"), a tool observed in attacks mounted by MedusaLocker and DragonForce affiliates
* HavocKiller or [HwAudKiller](https://thehackernews.com/2026/03/tax-search-ads-deliver-screenconnect.html) ("havoc.sys")

ESET said it also detected a Rust-based credential stealer codenamed OxideHarvest (aka buildx641) that's capable of harvesting data from popular web browsers, including Google Chrome, Microsoft Edge, Torch, Comodo, Epic Privacy Browser, Vivaldi, Brave, Opera, OperaGX, Mozilla Firefox, Waterfox, BlackHawk, and IceCat.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

"While most ransomware gangs continue to delegate EDR killing to affiliates, Gentlemen has chosen to centralize this function by offering affiliates a ready-to-use, standardized EDR-killer suite," ESET said. "This decision makes Gentlemen an attractive operator for affiliates as it materially lowers the entry barrier for them, making...