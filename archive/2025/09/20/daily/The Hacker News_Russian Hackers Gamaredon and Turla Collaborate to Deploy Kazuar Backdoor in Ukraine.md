---
title: Russian Hackers Gamaredon and Turla Collaborate to Deploy Kazuar Backdoor in Ukraine
url: https://thehackernews.com/2025/09/russian-hackers-gamaredon-and-turla.html
source: The Hacker News
date: 2025-09-20
fetch_date: 2025-10-02T20:27:24.331765
---

# Russian Hackers Gamaredon and Turla Collaborate to Deploy Kazuar Backdoor in Ukraine

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

# [Russian Hackers Gamaredon and Turla Collaborate to Deploy Kazuar Backdoor in Ukraine](https://thehackernews.com/2025/09/russian-hackers-gamaredon-and-turla.html)

**Sep 19, 2025**Ravie LakshmananMalware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgcan4EP6KxSTEnSsJgfX0N54PGEI1FQyqKhlC1m8OdisihSBdoh0CghuD5-YHwZIVA_PAno_-ytpdZZIGcaCumRg7XVQ8ymexMJaS9bvmgu7x9tfnhy62KTQiPKFqcM8ClLnaZoibmg1ZK0MnjolDBaCnwi-_QQxiepIJubgdYP0Gg9uCguWavfE_r7VlN/s790-rw-e365/russian-hackers.jpg)

Cybersecurity researchers have discerned evidence of two Russian hacking groups [Gamaredon](https://thehackernews.com/2025/03/russia-linked-gamaredon-uses-troop.html) and [Turla](https://thehackernews.com/2024/12/russia-linked-turla-exploits-pakistani.html) collaborating together to target and co-comprise Ukrainian entities.

Slovak cybersecurity company ESET [said](https://www.welivesecurity.com/en/eset-research/gamaredon-x-turla-collab/) it observed the Gamaredon tools PteroGraphin and PteroOdd being used to execute Turla group's Kazuar backdoor on an endpoint in Ukraine in February 2025, indicating that Turla is very likely actively collaborating with Gamaredon to gain access to specific machines in Ukraine and deliver the Kazuar backdoor.

"PteroGraphin was used to restart the Kazuar v3 backdoor, possibly after it crashed or was not launched automatically," ESET said in a report shared with The Hacker News. "Thus, PteroGraphin was probably used as a recovery method by Turla."

In a separate instance in April and June 2025, ESET said it also detected the deployment of Kazuar v2 through two other Gamaredon malware families tracked as PteroOdd and PteroPaste.

Both Gamaredon (aka Aqua Blizzard and Armageddon) and Turla (aka Secret Blizzard and Venomous Bear) are assessed to be affiliated with the Russian Federal Security Service (FSB), and are [known](https://thehackernews.com/2025/04/gamaredon-uses-infected-removable.html) for their [attacks](https://thehackernews.com/2025/07/secret-blizzard-deploys-malware-in-isp.html) targeting Ukraine.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Gamaredon has been active since at least 2013. It is responsible for many attacks, mostly against Ukrainian governmental institutions," ESET said.

"Turla, also known as Snake, is an infamous cyber espionage group that has been active since at least 2004, possibly extending back into the late 1990s. It mainly focuses on high-profile targets, such as governments and diplomatic entities, in Europe, Central Asia, and the Middle East. It is known for having breached major organizations such as the US Department of Defense in 2008 and the Swiss defense company RUAG in 2014."

The cybersecurity company said Russia's full-scale invasion of Ukraine in 2022 likely fueled this convergence, with the attacks primarily focusing on the Ukrainian defense sector in recent months.

One of Turla's staple implants is [Kazuar](https://unit42.paloaltonetworks.com/unit42-kazuar-multiplatform-espionage-backdoor-api-access/), a frequently updated malware that has previously [leveraged](https://thehackernews.com/2024/12/secret-blizzard-deploys-kazuar-backdoor.html) Amadey bots to deploy a backdoor called Tavdig, which then drops the .NET-based tool. Early artifacts associated with the malware have been spotted in the wild as far back as 2016, per [Kaspersky](https://securelist.com/sunburst-backdoor-kazuar/99981/).

PteroGraphin, PteroOdd, and PteroPaste, on the other hand, are part of a [growing arsenal](https://thehackernews.com/2024/12/hackers-leveraging-cloudflare-tunnels.html) of [tools](https://thehackernews.com/2025/08/cert-ua-warns-of-hta-delivered-c.html) developed by Gamaredeon to deliver additional payloads. PteroGraphin is a PowerShell tool that uses Microsoft Excel add-ins and scheduled tasks as a persistence mechanism and uses the Telegraph API for command-and-control (C2). It was first discovered in August 2024.

The exact initial access vector used by Gamaredon is not clear, but the group has a history of using spear-phishing and malicious LNK files on removable drives using tools like PteroLNK for propagation.

In all, Turla-related indicators have been detected on seven machines in Ukraine over the past 18 months, out of which four were breached by Gamaredon in January 2025. The deployment of the latest version of Kazuar (Kazuar v3) is said to have taken place towards the end of February.

"Kazuar v2 and v3 are fundamentally the same malware family and share the same codebase," ESET said. "Kazuar v3 comprises around 35% more C# lines than Kazuar v2 and introduces additional network transport methods: over web sockets and Exchange Web Services."

The attack chain involved Gamaredon deploying PteroGraphin, which was used to download a PowerShell downloader dubbed PteroOdd that, in turn, retrieved a payload from Telegraph to execute Kazuar. The payload is also designed to gather and exfiltrate the victim's computer name and system drive's volume serial number to a Cloudflare Workers sub-domain, before launching Kazuar.

That said, it's important to note here that there are signs suggesting Gamaredon downloaded Kazuar, as the backdoor is said to have been present on the system since February 11, 2025.

In a sign that this was not an isolated phenomenon, ESET revealed that it identified another PteroOdd sample on a different machine in Ukraine in March 2025, on which Kazuar was also present. The malware is capable of harvesting a wide range of system information, along with a list of installed .NET versions, and transmitting them to an external domain ("eset.ydns[.]eu").

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The fact that Gamaredon's toolset lacks any .NET malware and Turla's Kazuar is based in .NET suggests this data gathering step is likely meant for Turla, the company assessed with medium confidence.

The second set of...