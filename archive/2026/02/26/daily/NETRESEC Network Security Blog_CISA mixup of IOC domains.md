---
title: CISA mixup of IOC domains
url: https://www.netresec.com/?page=Blog&month=2026-02&post=CISA-mixup-of-IOC-domains
source: NETRESEC Network Security Blog
date: 2026-02-26
fetch_date: 2026-02-27T04:08:26.221443
---

# CISA mixup of IOC domains

Experts in network security monitoring and network forensics
[![Netresec](/images/Netresec_Logo_550x140.png)](https://www.netresec.com/)

[NETRESEC](/?page=Home)|

[Products](/?page=Products)|

[Training](/?page=Training)|

[Resources](/?page=Resources)|

[Blog](/?page=Blog)|

[About Netresec](/?page=AboutNetresec)

[NETRESEC](/)
»
[Blog](/?page=Blog)

Erik Hjelmvik

,

Thursday, 26 February 2026 09:35:00 (UTC/GMT)

## [CISA mixup of IOC domains](/?page=Blog&month=2026-02&post=CISA-mixup-of-IOC-domains)

Google's Threat Intelligence Group (GTIG) and Mandiant's recent [Disrupting the GRIDTIDE Global Cyber Espionage Campaign](https://cloud.google.com/blog/topics/threat-intelligence/disrupting-gridtide-global-espionage-campaign/) report is great and it has lots of good Indicators of Compromise (IOC). Many of these IOCs had already been shared by CISA last year as part of their [Alert AA25-141A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a) titled "Russian GRU Targeting Western Logistics Entities and Technology Companies".
The IOC overlap between these two reports is surprisingly big, provided that the GTIG report covers a Chinese espionage group while the CISA report covers the Russian GRU unit 26165 (aka APT28 / Fancy Bear).

But some of the domain names in CISA's report from last year are strange. For example, the domain name "accesscan[.]org" doesn't seem to ever have been registered. The GTIG report, however, contains the very similar domain "accesscam[.]org". This accesscam domain is registered to the dynamic DNS provider Dynu Systems, whose services are often [abused](https://threatfox.abuse.ch/asn/398019/) by malicious actors. Is it possible that there are typos in the IOCs published by CISA? I think so.

![accesscan glize spelling mistakes](https://media.netresec.com/images/accesscan-glize_2048x887.webp)

Another odd domain in CISA's AA25-141A is "glize[.]com", which I suspect is a typo from either "giize[.]com" or "gleeze[.]com". The two latter domains are listed in the GTIG report and both of them also belong to the dynamic DNS provider Dynu Systems. The domain listed in CISA's alert, on the other hand, appears to be a legit website ([archived page from 2024](https://web.archive.org/web/20241007094326/https%3A//glize.com/)) from the marketing company [Glize](https://www.facebook.com/glizecom) in Malta.

![Screenshot of Glize's website from 2024](https://media.netresec.com/images/glize_520x337.png)

Glize's website seems to have disappeared sometime in 2025.

Posted by Erik Hjelmvik on Thursday, 26 February 2026 09:35:00 (UTC/GMT)

Tags:
#[IOC](/?page=Blog&tag=IOC)​

Short URL:
<https://netresec.com/?b=26233f4>

### Recent Posts

» [CISA mixup of IOC domains](/?page=Blog&month=2026-02&post=CISA-mixup-of-IOC-domains)

» [njRAT runs MassLogger](/?page=Blog&month=2026-02&post=njRAT-runs-MassLogger)

» [Decoding malware C2 with CyberChef](/?page=Blog&month=2026-01&post=Decoding-malware-C2-with-CyberChef)

» [Latrodectus BackConnect](/?page=Blog&month=2025-12&post=Latrodectus-BackConnect)

» [NetworkMiner 3.1 Released](/?page=Blog&month=2025-12&post=NetworkMiner-3-1-Released)

» [Optimizing IOC Retention Time](/?page=Blog&month=2025-11&post=Optimizing-IOC-Retention-Time)

» [Online Network Forensics Class](/?page=Blog&month=2025-10&post=Online-Network-Forensics-Class)

» [Gh0stKCP Protocol](/?page=Blog&month=2025-09&post=Gh0stKCP-Protocol)

### Blog Archive

» [2026 Blog Posts](?page=Blog&year=2026)

» [2025 Blog Posts](?page=Blog&year=2025)

» [2024 Blog Posts](?page=Blog&year=2024)

» [2023 Blog Posts](?page=Blog&year=2023)

» [2022 Blog Posts](?page=Blog&year=2022)

» [2021 Blog Posts](?page=Blog&year=2021)

» [2020 Blog Posts](?page=Blog&year=2020)

» [2019 Blog Posts](?page=Blog&year=2019)

» [2018 Blog Posts](?page=Blog&year=2018)

» [2017 Blog Posts](?page=Blog&year=2017)

» [2016 Blog Posts](?page=Blog&year=2016)

» [2015 Blog Posts](?page=Blog&year=2015)

» [2014 Blog Posts](?page=Blog&year=2014)

» [2013 Blog Posts](?page=Blog&year=2013)

» [2012 Blog Posts](?page=Blog&year=2012)

» [2011 Blog Posts](?page=Blog&year=2011)

[List all blog posts](/?page=Blog&blogPostList=true)

[Video blog posts](/?page=Video)

### News Feeds

» [FeedBurner](https://feeds.feedburner.com/Netresec-Network-Security-Blog)

» [RSS Feed](https://www.netresec.com/rss.ashx)

![X / twitter](/images/X_100x90.png)

𝕏:
[@netresec](https://x.com/netresec)

---

![Bluesky](/images/bluesky_100x88.png)

Bluesky:
[@netresec.com](https://bsky.app/profile/netresec.com)

---

![Mastodon](/images/mastodon_100x107.png)

Mastodon:
[@netresec@infosec.exchange](https://infosec.exchange/%40netresec)

𝙽𝙴𝚃𝚁𝙴𝚂𝙴𝙲 |
[Contact](/?page=AboutNetresec)
|
[Privacy](/?page=Privacy)
|
[Mastodon](https://infosec.exchange/%40netresec)
|
[Bluesky](https://bsky.app/profile/netresec.com)
|
[𝕏](https://x.com/netresec)
|
[RSS](https://www.netresec.com/rss.ashx)