---
title: Threat Actors Turn to Sliver as Open Source Alternative to Popular C2 Frameworks
url: https://thehackernews.com/2023/01/threat-actors-turn-to-sliver-as-open.html
source: The Hacker News
date: 2023-01-24
fetch_date: 2025-10-04T04:40:54.024401
---

# Threat Actors Turn to Sliver as Open Source Alternative to Popular C2 Frameworks

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Threat Actors Turn to Sliver as Open Source Alternative to Popular C2 Frameworks](https://thehackernews.com/2023/01/threat-actors-turn-to-sliver-as-open.html)

**Jan 23, 2023**Ravie LakshmananThreat Detection / Infosec

[![Silver C2 Framework](data:image/png;base64... "Silver C2 Framework")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0KuMZ1t9xqCDu4w156XXY_oqt3vh8M_rMSzPleSrBMeATilO_VBiRWDBlWOVMz6vkOP-X-u0tmYGfPdBB3l2jX7Y3q5XcdQt8L9FiHvsRWBmXFUsbrO16gUB-tNcmdA2C71-sJ-OnyfGBdBc8j_B-iUvBrYmSsW26a17VlySrPcr-giKVNISOgDCb/s790-rw-e365/silver-c2.png)

The legitimate command-and-control (C2) framework known as Sliver is [gaining](https://thehackernews.com/2021/05/top-11-security-flaws-russian-spy.html) [more traction](https://thehackernews.com/2022/08/cybercrime-groups-increasingly-adopting.html) from threat actors as it emerges as an open source alternative to [Cobalt Strike](https://thehackernews.com/2022/11/google-identifies-34-cracked-versions.html) and Metasploit.

The findings come from Cybereason, which [detailed](https://www.cybereason.com/blog/sliver-c2-leveraged-by-many-threat-actors) its inner workings in an exhaustive analysis last week.

Sliver, developed by cybersecurity company BishopFox, is a Golang-based cross-platform post-exploitation framework that's designed to be used by security professionals in their red team operations.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Its myriad features for adversary simulation – including dynamic code generation, in-memory payload execution, and process injection – have also made it an appealing tool for threat actors looking to gain elevated access to the target system upon gaining an initial foothold.

[![Silver C2 Framework](data:image/png;base64... "Silver C2 Framework")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEishpEqvU7v2ZMnRGOlJTdKKdKCFZxGt9Zz5Oqjam3L0467KNGBd2oDPDOyeZeSXtk2ZghIdCtLSj0c63ZeXD0vzjfkyuOXvWGcbFDuV_XMvH3vSQDa8eXH9bFVDj0FVm3eCfQffXYH9EVQI_DC0e3pTaIuubC2m3erK73Ikbx60P6s0_RL2lRCw_be/s790-rw-e365/silver-1.png)

In other words, the software is used as a second-stage to conduct next steps of the attack chain after already compromising a machine using one of the initial intrusion vectors such as spear-phishing or exploitation of unpatched flaws.

"Silver C2 implant is executed on the workstation as stage two payload, and from [the] Sliver C2 server we get a shell session," Cybereason researchers Loïc Castel and Meroujan Antonyan said. "This session provides multiple methods to execute commands and other scripts or binaries."

A hypothetical attack sequence detailed by the Israeli cybersecurity company shows that Sliver could be leveraged for privilege escalation, following it up by credential theft and lateral movement to ultimately take over the domain controller for exfiltration of sensitive data.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Sliver has been weaponized in recent years by the Russia-linked [APT29](https://thehackernews.com/2021/05/top-11-security-flaws-russian-spy.html) group (aka Cozy Bear) as well as cybercrime operators like [Shathak](https://www.proofpoint.com/us/blog/security-briefs/ta551-uses-sliver-red-team-tool-new-activity) (aka TA551) and [Exotic Lily](https://thehackernews.com/2023/01/the-evolving-tactics-of-vidar-stealer.html) (aka Projector Libra), the latter of which is attributed to the Bumblebee malware loader.

[![Silver C2 Framework](data:image/png;base64... "Silver C2 Framework")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjEL8WmoS86_zoz59L8il6UhJTcyY5KkU1skyYB1MSGkNtK4w94-bVgPNidSGXNblfwzw-1ep3TdKV-EuUs1sLr7HY61qy4U5x_wjMGpEWerJuUUcxfFH06rYXNeWbyXQsgyTf1orfMWua46tuyBSxBTh8YcXTG2K_Mu7FrUXQywZxHiadZ0oxTcgmQ/s790-rw-e365/silver-2.png)

That said, Sliver is far from the only open source framework to be exploited for malicious ends. Last month, Qualys [disclosed](https://blog.qualys.com/vulnerabilities-threat-research/2022/12/12/dissecting-the-empire-c2-framework) how several hacking groups, including [Turla](https://thehackernews.com/2023/01/russian-turla-hackers-hijack-decade-old.html), [Vice Society](https://thehackernews.com/2022/12/vice-society-ransomware-attackers-adopt.html), and [Wizard Spider](https://thehackernews.com/2022/07/trickbot-malware-shifted-its-focus-on.html), have utilized Empire for post-exploitation and to expand their foothold in victim environments.

"Empire is an impressive post-exploitation framework with expansive capabilities," Qualys security researcher Akshat Pradhan said. "This has led to it becoming a frequent favorite toolkit of several adversaries."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[BishopFox](https://thehackernews.com/search/label/BishopFox)[Cobalt Strike](https://thehackernews.com/search/label/Cobalt%20Strike)[Command-and-control](https://thehackernews.com/search/label/Command-and-control)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Metasploit](https://thehackernews.com/search/label/Metasploit)[Open Source](https://thehackernews.com/search/label/Open%20Source)

[![c](data:image/svg+xml;base64...)](https://theha...