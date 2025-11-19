---
title: Microsoft Mitigates Record 15.72 Tbps DDoS Attack Driven by AISURU Botnet
url: https://thehackernews.com/2025/11/microsoft-mitigates-record-572-tbps.html
source: The Hacker News
date: 2025-11-18
fetch_date: 2025-11-19T03:14:55.143973
---

# Microsoft Mitigates Record 15.72 Tbps DDoS Attack Driven by AISURU Botnet

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

# [Microsoft Mitigates Record 15.72 Tbps DDoS Attack Driven by AISURU Botnet](https://thehackernews.com/2025/11/microsoft-mitigates-record-572-tbps.html)

**Nov 18, 2025**Ravie LakshmananIoT Security / Botnet

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2dO5PMH9gIwAVDF-XFgn5ydvp3uKTXTcpVHUMVoYtn02VkUCLM3d43lZH2KJMaoDkE2jZeroOAmDeoUnbTP_V7nONKGdkOGG5SlK4VBzY90xNuwT4IUv44rFNMpPo7x2zlFcVa4Kz1tyVMtEjWFCjX0Spsm3YvR8Jl2UlJXmokwESYjLXEzoBWJe07tq3/s790-rw-e365/ddos.jpg)

Microsoft on Monday disclosed that it automatically detected and neutralized a distributed denial-of-service (DDoS) attack targeting a single endpoint in Australia that measured 15.72 terabits per second (Tbps) and nearly 3.64 billion packets per second (pps).

The tech giant said it was the largest DDoS attack ever observed in the cloud, and that it originated from a TurboMirai-class Internet of Things (IoT) botnet known as **[AISURU](https://thehackernews.com/2025/10/researchers-warn-rondodox-botnet-is.html)**. It's currently not known who was targeted by the attack.

"The attack involved extremely high-rate UDP floods targeting a specific public IP address, launched from over 500,000 source IPs across various regions," Microsoft's Sean Whalen [said](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/defending-the-cloud-azure-neutralized-a-record-breaking-15-tbps-ddos-attack/4470422).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

"These sudden UDP bursts had minimal source spoofing and used random source ports, which helped simplify traceback and facilitated provider enforcement."

According to data from QiAnXin XLab, the AISURU botnet is [powered](https://thehackernews.com/2025/09/shadowv2-botnet-exploits-misconfigured.html) by nearly 300,000 infected devices, most of which are routers, security cameras, and DVR systems. It has been attributed to some of the biggest DDoS attacks recorded to date. In a report published last month, NETSCOUT [classified](https://thehackernews.com/2025/10/experts-reports-sharp-increase-in.html) the DDoS-for-hire botnet as operating with a restricted clientele.

"Operators have reportedly implemented preventive measures to avoid attacking governmental, law enforcement, military, and other national security properties," the company said. "Most observed AISURU attacks to date appear to be related to online gaming."

Botnets like AISURU also enable multi-use functions, going beyond DDoS attacks exceeding 20Tbps to facilitate other illicit activities like credential stuffing, artificial intelligence (AI)-driven web scraping, spamming, and phishing. AISURU also incorporates a residential proxy service.

"Attackers are scaling with the internet itself. As fiber-to-the-home speeds rise and IoT devices get more powerful, the baseline for attack size keeps climbing," Microsoft said.

The disclosure comes as NETSCOUT [detailed](https://www.netscout.com/blog/asert/161-days-eleven11) another TurboMirai botnet called [Eleven11](https://www.bitsight.com/blog/rapperbot-infection-ddos-split-second) (aka RapperBot) that's estimated to have launched about 3,600 DDoS attacks powered by hijacked IoT devices between late February and August 2025, around the same time authorities [disclosed](https://thehackernews.com/2025/08/doj-charges-22-year-old-for-running.html) an arrest and the dismantling of the botnet.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

Some of the command-and-control (C2) servers associated with the botnet are registered with the ".libre" top-level domain (TLD), which is part of OpenNIC, an alternative DNS root operated independently of ICANN and has been embraced by other DDoS botnets like [CatDDoS and Fodcha](https://thehackernews.com/2024/05/researchers-warn-of-catddos-botnet-and.html).

"Although the botnet has likely been rendered inoperable, compromised devices remain vulnerable," it said. "It is likely a matter of time until hosts are hijacked again and conscripted as a compromised node for the next botnet."

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

[botnet](https://thehackernews.com/search/label/botnet)[Cloud Infrastructure](https://thehackernews.com/search/label/Cloud%20Infrastructure)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[ddos attack](https://thehackernews.com/search/label/ddos%20attack)[digital forensics](https://thehackernews.com/search/label/digital%20forensics)[iot security](https://thehackernews.com/search/label/iot%20security)[Malware](https://thehackernews.com/search/label/Malware)[Network Traffic](https://thehackernews.com/search/label/Network%20Traffic)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/wiz-aws-ai-security)

Trending News

[![⚡ Weekly Recap: Hyper-V Malware, Malicious AI Bots, RDP Exploits, WhatsApp Lockdown and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Hyper-V Malware, Malicious AI Bots, RDP Exploits, WhatsApp Lockdown and More")

⚡ Weekly Recap: Hyper-V Malware, Malicious AI Bots, RDP Exploits, WhatsApp Lockdown and More](h...