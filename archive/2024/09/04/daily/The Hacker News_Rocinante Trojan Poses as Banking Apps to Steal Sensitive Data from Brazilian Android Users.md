---
title: Rocinante Trojan Poses as Banking Apps to Steal Sensitive Data from Brazilian Android Users
url: https://thehackernews.com/2024/09/rocinante-trojan-poses-as-banking-apps.html
source: The Hacker News
date: 2024-09-04
fetch_date: 2025-10-06T18:37:43.741020
---

# Rocinante Trojan Poses as Banking Apps to Steal Sensitive Data from Brazilian Android Users

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

# [Rocinante Trojan Poses as Banking Apps to Steal Sensitive Data from Brazilian Android Users](https://thehackernews.com/2024/09/rocinante-trojan-poses-as-banking-apps.html)

**Sep 03, 2024**Ravie LakshmananMalware / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJAdPoxpvEfQDGEEYuGxCUFXihU1c-w36FHZqHo0mRCU2ueYsBZQerX3uVFnMRO9e7MKTHzKU5lI-gxROvtRgddBciS8LbJeCkbJt9-mpNPKQrnUSnxB2_IZqXNOECuIxX7ZPy6xqS3iYggMlt-oWtp63p7k0rGUefh89c53KjUUBPqR_OLn_m3GNJVqoW/s790-rw-e365/android%20%281%29.jpg)

Mobile users in Brazil are the target of a new malware campaign that delivers a new Android banking trojan named Rocinante.

"This malware family is capable of performing keylogging using the Accessibility Service, and is also able to steal PII from its victims using phishing screens posing as different banks," Dutch security company ThreatFabric [said](https://www.threatfabric.com/blogs/the-trojan-horse-that-wanted-to-fly-rocinante).

"Finally, it can use all this exfiltrated information to perform device takeover (DTO) of the device, by leveraging the accessibility service privileges to achieve full remote access on the infected device."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Some of the prominent targets of the malware include financial institutions such as Itaú Shop, Santander, with the phony apps masquerading as Bradesco Prime and Correios Celular, among others -

* Livelo Pontos (com.resgatelivelo.cash)
* Correios Recarga (com.correiosrecarga.android)
* Bradesco Prime (com.resgatelivelo.cash)
* Módulo de Segurança (com.viberotion1414.app)

Source code analysis of the malware has revealed that Rocinante is being internally called by the operators as Pegasus (or PegasusSpy). It's worth noting that the name Pegasus has no connections to a cross-platform spyware developed by commercial surveillance vendor NSO Group.

That said, Pegasus is assessed to be the work of a threat actor dubbed DukeEugene, who is also known for similar malware strains such as ERMAC, BlackRock, Hook, and Loot, per a [recent analysis](https://thehackernews.com/2024/08/czech-mobile-users-targeted-in-new.html) by Silent Push.

ThreatFabric said it identified parts of the Rocinante malware that are directly influenced by early iterations of ERMAC, although it's believed that the leak of ERMAC's source code in 2023 may have played a role.

"This is the first case in which an original malware family took the code from the leak and implemented just some part of it in their code," it pointed out. "It is also possible that these two versions are separate forks of the same initial project."

Rocinante is mainly distributed via phishing sites that aim to trick unsuspecting users into installing the counterfeit dropper apps that, once installed, requests for accessibility service privileges to record all activities on the infected device, intercept SMS messages, and serve phishing login pages.

It also establishes contact with a command-and-control (C2) server to await further instructions – simulating touch and swipe events – to be executed remotely. The harvested personal information is exfiltrated to a Telegram bot.

"The bot extracts the useful PII obtained using the bogus login pages posing as the target banks. It then publishes this information, formatted, into a chat that criminals have access to," ThreatFabric noted.

"The information slightly changes based on which fake login page was used to obtain it, and includes device information such as model and telephone number, CPF number, password, or account number."

In a statement shared with The Hacker News, a Google spokesperson said no apps containing the malware have been detected on the Play Store. It also said that all Android users are secured against the threat by Google Play Protect, which is enabled by default on Android devices with Google Play Services, even if the apps are downloaded from other app store sources.

The development comes as Symantec highlighted another banking trojan malware campaign that exploits the secureserver[.]net domain to target Spanish and Portuguese-speaking regions.

"The multistage attack begins with malicious URLs leading to an archive containing an obfuscated .hta file," the Broadcom-owned company [said](https://www.broadcom.com/support/security-center/protection-bulletin/malware-campaign-exploits-secureserver-net-domain-to-deploy-banking-trojan).

"This file leads to a JavaScript payload that performs multiple AntiVM and AntiAV checks before downloading the final AutoIT payload. This payload is loaded using process injection with the goal of stealing banking information and credentials from the victim's system and exfiltrating them to a C2 server."

It also follows the emergence of a new "extensionware-as-a-service" that's advertised for sale through an updated version of the [Genesis Market](https://thehackernews.com/2023/04/fbi-cracks-down-on-genesis-market-119.html), which was shuttered by law enforcement in early 2023. The kit is designed

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The activity, active since mid-2023 and targeting Mexico and other LATAM nations, has been attributed to an e-crime group named Cybercartel, which offers these types of services to other cybercriminal crews. The extensions are no longer available for download.

"The malicious Google Chrome extension disguises itself as a legitimate application, tricking users into installing it from compromised websites or phishing campaigns," security researchers Ramses Vazquez of Karla Gomez of the Metabase Q Ocelot Threat Intelligence Team [said](https://www.metabaseq.com/threat/cybercartel-bringing-genesis-market-business-to-latam/).

"Once the extension is installed, it injects JavaScript code into the web pages that the user visits. This code can intercept and manipulate the content of the pages, as well as capture sensitive data such as login cr...