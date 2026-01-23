---
title: New Osiris Ransomware Emerges as New Strain Using POORTRY Driver in BYOVD Attack
url: https://thehackernews.com/2026/01/new-osiris-ransomware-emerges-as-new.html
source: The Hacker News
date: 2026-01-22
fetch_date: 2026-01-23T03:33:35.786508
---

# New Osiris Ransomware Emerges as New Strain Using POORTRY Driver in BYOVD Attack

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

# [New Osiris Ransomware Emerges as New Strain Using POORTRY Driver in BYOVD Attack](https://thehackernews.com/2026/01/new-osiris-ransomware-emerges-as-new.html)

**Ravie Lakshmanan**Jan 22, 2026

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYzbCMSUAN1p1M0CnYPBeFVA3mYmKz-XYLo2R-0OUmaSxvarUieSUkbxkOexloc74_koPBcfuIcHXj2taolqWDe8nhE4Uo8maY_rioqDFiWgi9OWuQseJ5VLk4nf74YzkJ1nPf2sQlFyNBbHMktJ7Fe7XbJbJJa-Viv28SJ28jmrceB3dSGpVNIQbS8UYZ/s1600-e365/ransomware.jpg)

Cybersecurity researchers have disclosed details of a new ransomware family called **Osiris** that targeted a major food service franchisee operator in Southeast Asia in November 2025.

The attack leveraged a malicious driver called [POORTRY](https://thehackernews.com/2024/09/cosmicbeetle-deploys-custom-scransom.html) as part of a known technique referred to as bring your own vulnerable driver (BYOVD) to disarm security software, the Symantec and Carbon Black Threat Hunter Team said.

It's worth noting that Osiris is assessed to be a brand-new ransomware strain, sharing no similarities with [another variant](https://www.tripwire.com/state-of-security/osiris-locky-ransomware-afterlife-files) of the [same name](https://www.acronis.com/en/blog/posts/osiris-ransomware-new-addition-locky-family/) that emerged in December 2016 as an iteration of the Locky ransomware. It's currently not known who the developers of the locker are, or if it's advertised as a ransomware-as-a-service (RaaS).

However, the Broadcom-owned cybersecurity division said it identified clues that suggest the threat actors who deployed the ransomware may have been previously associated with [INC ransomware](https://thehackernews.com/2024/09/microsoft-warns-of-new-inc-ransomware.html) (aka Warble).

"A wide range of living off the land and dual-use tools were used in this attack, as was a malicious POORTRY driver, which was likely used as part of a bring your own vulnerable driver (BYOVD) attack to disable security software," the company [said](https://www.security.com/threat-intelligence/new-ransomware-osiris) in a report shared with The Hacker News.

"The exfiltration of data by the attackers to Wasabi buckets, and the use of a version of Mimikatz that was previously used, with the same filename (kaz.exe), by attackers deploying the INC ransomware, point to potential links between this attack and some attacks involving INC."

Described as an "effective encryption payload" that's likely wielded by experienced attackers, Osiris makes use of a hybrid encryption scheme and a unique encryption key for each file. It's also flexible in that it can stop services, specify which folders and extensions need to be encrypted, terminate processes, and drop a ransom note.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

By default, it's designed to kill a long list of processes and services related to Microsoft Office, Exchange, Mozilla Firefox, WordPad, Notepad, Volume Shadow Copy, and Veeam, among others.

First signs of malicious activity on the target's network involved the exfiltration of sensitive data using Rclone to a Wasabi cloud storage bucket prior to the ransomware deployment. Also utilized in the attack were a number of dual-use tools like Netscan, Netexec, and MeshAgent, as well as a custom version of the Rustdesk remote desktop software.

POORTRY is a little different from traditional BYOVD attacks in that it uses a bespoke driver expressly designed for elevating privileges and terminating security tools, as opposed to deploying a legitimate-but-vulnerable driver to the target network.

"KillAV, which is a tool used to deploy vulnerable drivers for terminating security processes, was also deployed on the target's network," the Symantec and Carbon Black Threat Hunter Team noted. "RDP was also enabled on the network, likely to provide the attackers with remote access."

The development comes as ransomware remains a significant enterprise threat, with the landscape constantly shifting as some groups close their doors and others quickly rise from their ashes or move in to take their place. According to an analysis of data leak sites by Symantec and Carbon Black, ransomware actors claimed a total of 4,737 attacks during 2025, up from 4,701 in 2024, a 0.8% increase.

The [most active](https://cyble.com/blog/ransomware-groups-july-2025-attacks/) players during the past year were Akira (aka Darter or Howling Scorpius), Qilin (aka Stinkbug or Water Galura), Play (aka Balloonfly), INC, SafePay, RansomHub (aka Greenbottle), DragonForce (aka Hackledorb), Sinobi, Rhysida, and CACTUS. Some of the other notable developments in the space are listed below -

* Threat actors using the Akira ransomware have leveraged a [vulnerable Throttlestop driver](https://thehackernews.com/2025/08/sonicwall-investigating-potential-ssl.html), along with the Windows CardSpace User Interface Agent and Microsoft Media Foundation Protected Pipeline, to sideload the [Bumblebee](https://thehackernews.com/2024/02/bumblebee-malware-returns-with-new.html) loader in attacks observed in mid-to-late 2025.
* Akira ransomware campaigns have also [exploited](https://reliaquest.com/blog/threat-spotlight-akira-ransomwares-sonicwall-campaign-creates-enterprise-m%26a-risk) SonicWall SSL VPNs to breach small- to medium-sized business environments during mergers and acquisitions and ultimately obtain access to the bigger, acquiring enterprises. Another Akira attack has been [found](https://unit42.paloaltonetworks.com/fake-captcha-to-compromise/) to leverage [ClickFix](https://thehackernews.com/2025/08/clickfix-malware-campaign-exploits.html)-style CAPTCHA verification lures to drop a .NET remote access trojan called [SectopRAT](https://thehackernews.com/2025/07/hackers-use-leaked-shellter-tool.html), which serves as a conduit for remote control and ransomware delivery.
* LockBit (aka Syrphid), which [partnered](https://thehackernews.com/2025/10/lockbit-qilin-and-dragonforce-join.html) with DragonForce and Qilin in October 2025, has continued to [maintain its infrastructure](https://flare.io/learn/resources/blog/inside-lockbit-5-0/) despite a [law enforcement operation](https://thehackernews.com/2024/02/lockbit-ransomware-group-resurfaces.html) to shut down its operations in early 2024. It has also released variants of [LockBit 5.0](h...