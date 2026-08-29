---
title: China-Made ZBT Routers Ship With Two Implants Giving Unauthenticated Attackers Root Access
url: https://thehackernews.com/2026/08/china-made-zbt-routers-ship-with-two.html
source: The Hacker News
date: 2026-08-28
fetch_date: 2026-08-29T08:33:13.037289
---

# China-Made ZBT Routers Ship With Two Implants Giving Unauthenticated Attackers Root Access

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [China-Made ZBT Routers Ship With Two Implants Giving Unauthenticated Attackers Root Access](https://thehackernews.com/2026/08/china-made-zbt-routers-ship-with-two.html)

**Swati Khandelwal**Aug 28, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0i2viN2zKBeSxzTqoxZkPNq_6lPMDBLb18zbLPwufsY4mFm494ydDDAWi6gGwy6PsmRGublHFmdmcEiGKViLuUgaJwWux_YUW7HQHuGbbf04HGNpoZa6QLmvf1IHE04TeTT89Yc1_jo0z6mptCbX-fIhVEVQzg5GnfU2Uya4HHASHbttTBGMxl7KMkbM/s1700-e365/router-malware.jpg)

VulnCheck has disclosed two previously undocumented factory implants in firmware for routers built by Shenzhen Zhibotong Electronics (**ZBT**), each of which gives an unauthenticated remote attacker the ability to run commands as root on affected devices.

The implants, named **SPEAKINGSTONE** and **DARKLANTERN** by the company's zero-day research team, are tracked as **CVE-2026-74232** and **CVE-2026-74233**.

VulnCheck, which assigned both identifiers as a CVE Numbering Authority (CNA), rated each 9.3 on the CVSS 4.0 scoring system and 9.8 on CVSS 3.1. Both vectors record a network attack requiring no privileges and no user interaction.

SPEAKINGSTONE, which runs as the service `yunmgrd`, sends beacons over UDP port 10000 to a hardcoded command-and-control (C2) server. Because the implant dials outward, it functions from behind NAT and ordinary egress filtering.

Its protocol supports message types that execute arbitrary commands as root, exfiltrate the WAN PPPoE username and password, write and read a DNS hijack list, and open a reverse SSH tunnel.

"This is a surveillance implant with root access to every device it runs on," VulnCheck said in [its supply chain research](https://www.vulncheck.com/blog/zbt-darklantern-speakingstone).

DARKLANTERN operates as the service `infosrvd` on UDP port 9992, which the router's stock firewall opens to inbound connections from any internet address. VulnCheck's advisory describes the service's authentication as ineffective, resting on a hardcoded salt and an all-zero wildcard MAC value that bypasses its own address check.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Between August 18 and August 21, VulnCheck identified 203 internet-facing DARKLANTERN instances across 22 countries, self-reporting 16 distinct models. The figure counts hosts that answered a probe rather than devices found compromised.

Both implants were found on an $88 Deep Orange 3G/4G/LTE Router bought from a U.S. supplier, a white-labeled ZBT-WE826-T2 whose firmware was built in 2019. That unit predates ENDLESSDOORS (CVE-2026-66747), the phone-home implant VulnCheck disclosed on August 5 and found in at least [20 Zbtlink router models](https://thehackernews.com/2026/08/chinese-made-zbtlink-routers-ship-with.html).

VulnCheck's advisory for [the DARKLANTERN command injection](https://www.vulncheck.com/advisories/zbtlink-mqwrt-infosrvd-command-injection) and its advisory for [the SPEAKINGSTONE C2 implant](https://www.vulncheck.com/advisories/zbtlink-mqwrt-yunmgrd-cloud-c2-implant) name the following models and firmware builds -

* **CVE-2026-74233 (DARKLANTERN)** - Zbtlink WE1326, WE357, WE5926, WE5926-WD, WE826-Q, WE826-T2, WE826-WD, WG108 and WG3526 on firmware 19.1101, WE2426-C on 19.1112, WE5926-EC\_QP on 20.0516 and WF3526-P on 19.051, plus CTN720-W1, LF-1541 and MT7620N on 19.1101 and WRC1 on 20.0622, which the CVE record lists under an unidentified vendor.
* **CVE-2026-74232 (SPEAKINGSTONE)** - Zbtlink L3\_V2\_8 on 3.0.0.4.528, WE826-T2 on 19.1101, ZBT-7628 on 1.0.0.2.007 and ZBT-ZBT7621 on 1.0.0.3.001, MoreQuick MQAC-7620, MQAC-7620A, MQAP-7620, MQAP-7620A and MQAP-7628 on 1.0.0.2.000, and AP522 on 1.0.0.2.014, AP7628 and HC5661A on 3.0.0.4.380, APG721B on 19.0809, HK300 on 1.0.0.2.032 and MAP-N10 on 1.0.0.2.044 under an unidentified vendor.

The advisory pages display those builds as upper bounds, while the CVE records name each firmware as a single exact build and set the default status of every other version to unknown. Neither advisory names a fixed firmware release, leaving an owner on a build outside the listed set without a published basis for deciding whether the flaw applies.

Model number rather than brand is the reliable check, because ZBT sells the same hardware and firmware to resellers that put their own name on the case. The Hacker News confirmed via the IEEE-registered MAC prefix database on August 28 that the blocks 78:A3:51 and F8:5E:3C are both assigned to Shenzhen Zhibotong Electronics, letting an owner identify the manufacturer from the device's own address.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJpr-Ua5OEVw1C51WgcvQ3DPtimxeVUHxr4CTHqhI_6hLxVcU-yzWd3jAzkTw8FLSU-mgSV2XUSDwln-VdICbtGKYQy4VNOn_3ALR3mmXsa6W4Rj95rr8qwtSidmUnJco8TJvFehrNrpDK1R7EWHK3rKUCrOJCHSHcFVr4HNEwLTdhqd7A_8HO6snLC70/s1700-e365/exe.png)

SPEAKINGSTONE carries a hardcoded backup C2 domain that the implant reaches for where a primary server was never configured, and VulnCheck found that domain unregistered.

The company registered the domain and stood up a server running a reverse-engineered implementation of the protocol. Beacons began arriving as soon as the server was live.

As of August 21, 392 unique devices had reported in, of which 390 were in China. VulnCheck said 83 percent were on China Mobile's network, that 304 of the 392 broadcast SSIDs beginning with "CMCC", and that 363 self-reported a single model, L3\_V2\_8, running firmware 3.0.0.4.528.

Because a device reaches the backup domain only where a primary C2 was never configured, the 392 are a floor drawn from an unrepresentative subset rather than a count of affected devices.

VulnCheck flags CVE-2026-74233 in its own Known Exploited Vulnerabilities catalog, whose published criteria require that a vulnerability be "publicly-reported as exploited in the wild."

CISA's Vulnrichment enrichment, recorde...