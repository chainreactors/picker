---
title: Parallax RAT Targeting Cryptocurrency Firms with Sophisticated Injection Techniques
url: https://thehackernews.com/2023/03/parallax-rat-targeting-cryptocurrency.html
source: The Hacker News
date: 2023-03-02
fetch_date: 2025-10-04T08:29:14.835635
---

# Parallax RAT Targeting Cryptocurrency Firms with Sophisticated Injection Techniques

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

# [Parallax RAT Targeting Cryptocurrency Firms with Sophisticated Injection Techniques](https://thehackernews.com/2023/03/parallax-rat-targeting-cryptocurrency.html)

**Mar 01, 2023**Ravie LakshmananCryptocurrency / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgqezNklGIEGTNJ1fW7JaSrKf7hSGeIT0gv5ICchgiijntx86BgoYj3KuFP3agp0ImetqqOPDzx2d3JRdMh-OvxLdIZyYIz9lYCh9ya9iFFXhznXCws2S7ug_znCyRHQnp6IiyRAXwksS-Js7XJG_uvBcV5I6m6SBX9Xeu8MruV_wrxQ0w-SKT8OgSb/s790-rw-e365/trojan.png)

Cryptocurrency companies are being targeted as part of a new campaign that delivers a remote access trojan called Parallax RAT.

The malware "uses injection techniques to hide within legitimate processes, making it difficult to detect," Uptycs [said](https://www.uptycs.com/blog/cryptocurrency-entities-at-risk-threat-actor-uses-parallax-rat-for-infiltration) in a new report. "Once it has been successfully injected, attackers can interact with their victim via Windows Notepad that likely serves as a communication channel."

[Parallax RAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.parallax) grants attackers remote access to victim machines. It comes with features to upload and download files as well as record keystrokes and screen captures.

It has been put to use since early 2020 and was [previously delivered](https://blog.talosintelligence.com/coronavirus-themed-malware/) via COVID-19-themed lures. In February 2022, Proofpoint [detailed](https://thehackernews.com/2022/02/experts-warn-of-hacking-group-targeting.html) an activity cluster dubbed TA2541 targeting aviation, aerospace, transportation, manufacturing, and defense industries using different RATs, including Parallax.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The first payload is a Visual C++ malware that employs the [process hollowing](https://attack.mitre.org/techniques/T1055/012/) technique to inject Parallax RAT into a legitimate Windows component called [pipanel.exe](https://strontic.github.io/xcyclopedia/library/pipanel.exe-3C98CEE428375B531A5C98F101B1E063.html).

Parallax RAT, besides gathering system metadata, is also capable of accessing data stored in the clipboard and even remotely rebooting or shutting down the compromised machine.

One notable aspect of the attacks is the use of the Notepad utility to initiate conversations with the victims and instruct them to connect to an actor-controlled Telegram channel.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiFUC-w3oF-qQ7aKtHkUus1P5voeAOyKv5G7yV1x_AGc6XLeql_dVCGJDmODAuLj5JvI-Es2ScgZnUIUG_XYwEqjQ0KNNih3Fz77TELPVCbQbH-M7-Bhq3RG5TPxzo3fiB6_pGUmORq9vbGYr4lqNSd6vABC1qy4wSqlFE63idlIEdZIusEAeHrIPlX/s790-rw-e365/map.png)

Uptycs' analysis of the Telegram chats reveals that the threat actor has an interest in crypto companies such as investment firms, exchanges, and wallet service providers.

The modus operandi entails searching public sources like DNSdumpster for identifying mail servers belonging to the targeted companies via their mail exchanger ([MX](https://en.wikipedia.org/wiki/MX_record)) records and sending phishing emails bearing the Parallax RAT malware.

The development comes as Telegram is increasingly becoming a hub for criminal activities, enabling threat actors to organize their operations, distribute malware, and facilitate the sale of stolen data and other illegal goods in part owing to the platform's lax moderation efforts.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"One reason why Telegram is attractive to cybercriminals is its alleged built-in encryption and the ability to create channels and large, private groups," KELA [disclosed](https://ke-la.com/resource/telegram-how-a-messenger-turned-into-a-cybercrime-ecosystem-by-2023/) in an exhaustive analysis published last month.

"These features make it difficult for law enforcement and security researchers to monitor and track criminal activity on the platform. In addition, cybercriminals often use coded language and alternative spellings to communicate on Telegram, making it even more challenging to decipher their conversations."

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

[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[Malware](https://thehackernews.com/search/label/Malware)[Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches C...