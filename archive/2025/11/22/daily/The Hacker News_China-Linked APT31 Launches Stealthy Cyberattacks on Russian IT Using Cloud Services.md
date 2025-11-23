---
title: China-Linked APT31 Launches Stealthy Cyberattacks on Russian IT Using Cloud Services
url: https://thehackernews.com/2025/11/china-linked-apt31-launches-stealthy.html
source: The Hacker News
date: 2025-11-22
fetch_date: 2025-11-23T03:27:34.902071
---

# China-Linked APT31 Launches Stealthy Cyberattacks on Russian IT Using Cloud Services

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [China-Linked APT31 Launches Stealthy Cyberattacks on Russian IT Using Cloud Services](https://thehackernews.com/2025/11/china-linked-apt31-launches-stealthy.html)

**Nov 22, 2025**Ravie LakshmananCyber Espionage / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0ApbbGy1VeM3uMCY8dVuTIzKS2QJ1wsy4n57G1cLRnEfWcZ2UIsRx8AhTUv8lqBkZb3CQPhalZOTRXo1E8A8LR8EHjecR51E7dgfDI_mHhTYmYulkhNmv82ET56xgGl3qaT7so9t02M3e1JB9pxi_0HCX9cRYUP7qPn9wAg9Yv3JBDj8zpY7bPRuO41rc/s790-rw-e365/russia.jpg)

The China-linked advanced persistent threat (APT) group known as **APT31** has been attributed to cyber attacks targeting the Russian information technology (IT) sector between 2024 and 2025 while staying undetected for extended periods of time.

"In the period from 2024 to 2025, the Russian IT sector, especially companies working as contractors and integrators of solutions for government agencies, faced a series of targeted computer attacks," Positive Technologies researchers Daniil Grigoryan and Varvara Koloskova [said](https://ptsecurity.com/research/pt-esc-threat-intelligence/striking-panda-attacks-apt31-today/) in a technical report.

APT31, also known as Altaire, Bronze Vinewood, Judgement Panda, PerplexedGoblin, RedBravo, Red Keres, and Violet Typhoon (formerly Zirconium), is assessed to be active since at least 2010. It has a track record of striking a wide range of sectors, including governments, financial, and aerospace and defense, high tech, construction and engineering, telecommunications, media, and insurance.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

The cyber espionage group is primarily focused on gathering intelligence that can provide Beijing and state-owned enterprises with political, economic, and military advantages. In May 2025, the hacking crew was [blamed](https://thehackernews.com/2025/05/czech-republic-blames-china-linked.html) by the Czech Republic for targeting its Ministry of Foreign Affairs.

The attacks aimed at Russia are characterized by the use of legitimate cloud services, mainly those prevalent in the country, like Yandex Cloud, for command-and-control (C2) and data exfiltration in an attempt to blend in with normal traffic and escape detection.

The adversary is also said to have staged encrypted commands and payloads in social media profiles, both domestic and foreign, while also conducting their attacks during weekends and holidays. In at least one attack targeting an IT company, APT31 breached its network as far back as late 2022, before escalating the activity coinciding with the 2023 New Year holidays.

In another intrusion detected in December 2024, the threat actors sent a spear-phishing email containing a RAR archive that, in turn, included a Windows Shortcut (LNK) responsible for launching a Cobalt Strike loader dubbed CloudyLoader via DLL side-loading. Details of this activity were [previously documented](https://securelist.ru/cobalt-strike-attacks-using-quora-github-social-media/113139/) by Kaspersky in July 2025, while identifying some overlaps with a threat cluster known as [EastWind](https://thehackernews.com/2024/08/russian-government-hit-by-eastwind.html).

The Russian cybersecurity company also said it identified a ZIP archive lure that masqueraded as a report from the Ministry of Foreign Affairs of Peru to ultimately deploy CloudyLoader.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

To facilitate subsequent stages of the attack cycle, APT31 has leveraged an extensive set of publicly available and custom tools. Persistence is achieved by setting up scheduled tasks that mimic legitimate applications, such as Yandex Disk and Google Chrome. Some of them are listed below -

* [SharpADUserIP](https://github.com/evilashz/SharpADUserIP), a C# utility for reconnaissance and discovery
* [SharpChrome.exe](https://github.com/GhostPack/SharpDPAPI), to extract passwords and cookies from Google Chrome and Microsoft Edge browsers
* [SharpDir](https://github.com/jnqpblc/SharpDir), to search files
* [StickyNotesExtract.exe](https://github.com/V1V1/SharpScribbles), to extract data from the Windows Sticky Notes database
* Tailscale VPN, to create an encrypted tunnel and set up a peer-to-peer (P2P) network between the compromised host and their infrastructure
* [Microsoft dev tunnels](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/overview), to tunnel traffic
* [Owawa](https://thehackernews.com/2021/12/hackers-using-malicious-iis-server.html), a malicious IIS module for credential theft
* AufTime, a Linux backdoor that uses the wolfSSL library to communicate with C2
* COFFProxy, a Golang backdoor that supports commands for tunneling traffic, executing commands, managing files, and delivering additional payloads
* VtChatter, a tool that uses Base64-encoded comments to a [text file hosted on VirusTotal](https://www.virustotal.com/gui/file/adc9bf081e1e9da2fbec962ae11212808e642096a9788159ac0acef879fd31e8/community) as a two-way C2 channel every two hours
* OneDriveDoor, a backdoor that uses Microsoft OneDrive as C2
* [LocalPlugX](https://rt-solar.ru/solar-4rays/blog/3829/), a variant of [PlugX](https://thehackernews.com/2025/01/fbi-deletes-plugx-malware-from-4250.html) that's used to spread within the local network, rather than to communicate with C2
* [CloudSorcerer](https://thehackernews.com/2024/07/new-apt-group-cloudsorcerer-targets.html), a backdoor that used cloud services as C2
* YaLeak, a .NET tool to upload information to Yandex Cloud

"APT31 is constantly replenishing its arsenal: although they continue to use some of their old tools," Positive Technologies said. "As C2, attackers actively use cloud services, in particular, Yandex and Microsoft OneDrive services. Many tools are also configured to work in server mode, waiting for attackers to connect to an infected host."

"In addition, the grouping exfiltrates data through Yandex's cloud storage. These tool...