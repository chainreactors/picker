---
title: RA World Ransomware Attack in South Asia Links to Chinese Espionage Toolset
url: https://thehackernews.com/2025/02/hackers-exploited-pan-os-flaw-to-deploy.html
source: The Hacker News
date: 2025-02-14
fetch_date: 2025-10-06T20:39:40.511272
---

# RA World Ransomware Attack in South Asia Links to Chinese Espionage Toolset

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

# [RA World Ransomware Attack in South Asia Links to Chinese Espionage Toolset](https://thehackernews.com/2025/02/hackers-exploited-pan-os-flaw-to-deploy.html)

**Feb 13, 2025**Ravie LakshmananThreat Intelligence / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigMOJ2zqeU_8qv-e5X3aefijCv7czLi1hBsrIm3J2KvhXi5aVIaMju6cEmX1nLQ0nYjEkIPRvBxdektXYSAxR43WuUT9y0S1ClJ24D4HTV-eJAnu9C3FqEc7grJ0zytIAcgUoWLI_N6YI07x7rFFa13-hGSukCblrz-jXs1N0w8neqnR6po-eTzDHHgXdJ/s790-rw-e365/ransomware.png)

An RA World ransomware attack in November 2024 targeting an unnamed Asian software and services company involved the use of a malicious tool exclusively used by China-based cyber espionage groups, raising the possibility that the threat actor may be moonlighting as a ransomware player in an individual capacity.

"During the attack in late 2024, the attacker deployed a distinct toolset that had previously been used by a China-linked actor in classic espionage attacks," the Symantec Threat Hunter Team, part of Broadcom, [said](https://www.security.com/threat-intelligence/chinese-espionage-ransomware) in a report shared with The Hacker News.

"In all the prior intrusions involving the toolset, the attacker appeared to be engaged in classic espionage, seemingly solely interested in maintaining a persistent presence on the targeted organizations by installing backdoors."

This included a July 2024 compromise of the Foreign Ministry of a country in southeastern Europe that involved the use of classic DLL side-loading techniques to deploy [PlugX](https://thehackernews.com/2025/01/fbi-deletes-plugx-malware-from-4250.html) (aka Korplug), a malware [repeatedly](https://thehackernews.com/2024/02/mustang-panda-targets-asia-with.html) [used](https://thehackernews.com/2025/01/reddelta-deploys-plugx-malware-to.html) by the Mustang Panda (aka Fireant and RedDelta) actor.

Specifically, the attack chains entails the use of a legitimate Toshiba executable named "toshdpdb.exe" to sideload a malicious DLL named "toshdpapi.dll," which, in turn, acts as a conduit to load the encrypted PlugX payload.

Other intrusions linked to the same toolset have been observed in connection with attacks targeting two different government entities in Southeastern Europe and Southeast Asia in August 2024, a telecom operator in September 2024, and another government ministry in a different Southeast Asian country in January 2025.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

However, Symantec noted that it observed the PlugX variant being deployed in November 2024 as part of a criminal extortion campaign against a medium-sized software and services company in South Asia.

It's not exactly clear how the company's network was compromised, although the attacker claimed to have done so by exploiting a known security flaw in Palo Alto Networks PAN-OS software ([CVE-2024-0012](https://thehackernews.com/2024/11/pan-os-firewall-vulnerability-under.html)). The attack culminated with the machines getting encrypted with the RA World ransomware, but not before the Toshiba binary was used to launch the PlugX malware.

At this point, it's worth noting that prior analyses from Cisco Talos and Palo Alto Networks Unit 42 have [uncovered](https://thehackernews.com/2023/05/new-ransomware-gang-ra-group-hits-us.html) [tradecraft overlaps](https://unit42.paloaltonetworks.com/ra-world-ransomware-group-updates-tool-set/) between RA World (formerly called RA Group) and a Chinese threat group known as [Bronze Starlight](https://thehackernews.com/2022/06/state-backed-hackers-using-ransomware.html) (aka Storm-401 and Emperor Dragonfly) that has a history of using short-lived ransomware families.

While it's not known why an espionage actor is also conducting a financially motivated attack, Symantec theorized that a lone actor is likely behind the effort and that they were attempting to make some quick gains on the side. This assessment also lines up with Sygnia's analysis of Emperor Dragonfly in October 2022, which it [described](https://thehackernews.com/2022/10/researchers-link-cheerscrypt-linux.html) as a "single threat actor."

This form of moonlighting, while rarely observed in the Chinese hacking ecosystem, is a lot more [prevalent](https://thehackernews.com/2024/08/us-agencies-warn-of-iranian-hacking.html) [among](https://thehackernews.com/2024/07/north-korean-hackers-shift-from-cyber.html) [threat actors](https://thehackernews.com/2024/10/north-korean-group-collaborates-with.html) from Iran and North Korea.

"Another form of financially motivated activity supporting state goals are groups whose main mission may be state-sponsored espionage are, either tacitly or explicitly, allowed to conduct financially motivated operations to supplement their income," the Google Threat Intelligence Group (GTIG) [said](https://cloud.google.com/blog/topics/threat-intelligence/cybercrime-multifaceted-national-security-threat) in a report published this week.

"This can allow a government to offset direct costs that would be required to maintain groups with robust capabilities."

### Salt Typhoon Exploits Vulnerable Cisco Devices to Breach Telcos

The development comes as the Chinese nation-state hacking group referred to as [Salt Typhoon](https://thehackernews.com/2025/01/us-sanctions-chinese-cybersecurity-firm.html) has been linked to a set of cyber attacks that leverage known security flaws in Cisco network devices ([CVE-2023-20198](https://thehackernews.com/2023/10/warning-unpatched-cisco-zero-day.html) and [CVE-2023-20273](https://thehackernews.com/2023/10/cisco-zero-day-exploited-to-implant.html)) to penetrate multiple networks.

The malicious cyber activity is assessed to have singled out a U.S.-based affiliate of a significant U.K.-based telecommunications provider, a South African telecommunications provider, and an Italian internet service, and a large Thailand telecommunications provider based on communications...