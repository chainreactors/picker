---
title: Lazarus Deploys RemotePE Memory-Only RAT Against Financial and Crypto Firms
url: https://thehackernews.com/2026/05/lazarus-deploys-remotepe-memory-only.html
source: The Hacker News
date: 2026-05-25
fetch_date: 2026-05-26T06:11:12.519955
---

# Lazarus Deploys RemotePE Memory-Only RAT Against Financial and Crypto Firms

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [Lazarus Deploys RemotePE Memory-Only RAT Against Financial and Crypto Firms](https://thehackernews.com/2026/05/lazarus-deploys-remotepe-memory-only.html)

**Ravie Lakshmanan**May 25, 2026Endpoint Security / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEinuOeS1qVC0UHhPnJ0jlSdfScsZDRtkI6VU366iePjKdNTqLiqHcqjRcGL-sNBdUkShUH71YDDVwavzXM1cIu2UU9zE8VYgbJYsRUQeWRZAO75JC2vQHYs4saWOM3rQZKFPqNvlL8ASBocRiZXdO1jLgqLuCCeLHX0bAA1EQEhiBAq3i3Os97qHt_xF5ub/s1700-e365/crypto-firms.jpg)

Cybersecurity researchers have shed light on a cross-platform malware called **RemotePE** that has been put to use by the North Korea-linked Lazarus Group in attacks targeting financial and cryptocurrency organizations.

RemotePE, per NCC Group subsidiary Fox-IT, is part of a multi-stage attack chain that involves two loaders tracked as DPAPILoader and RemotePELoader.

"DPAPILoader decrypts and loads RemotePELoader from disk using the Windows Data Protection API ([DPAPI](https://learn.microsoft.com/en-us/dotnet/standard/security/how-to-use-data-protection))," security researchers Yun Zheng Hu and Mick Koomen [said](https://blog.fox-it.com/2026/05/22/remotepe-the-lazarus-rat-that-lives-in-memory/). "RemotePELoader beacons to a C2 server and waits until it receives the next stage: RemotePE, a RAT executed entirely in memory and never written to disk, leaving no filesystem artifacts."

RemotePE was [first highlighted](https://thehackernews.com/2025/09/lazarus-group-expands-malware-arsenal.html) by the security vendor in September 2025 in connection with an attack targeting an unnamed organization in the decentralized finance (DeFi) sector, leading to the deployment of three malware families, including PondRAT, ThemeForestRAT, and RemotePE.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

The intrusion commenced with the compromise of an employee's device through social engineering, after having approached the victim on Telegram under the guise of an existing employee of a trading company and scheduling a meeting on fake Calendly and Picktime domains.

The RemotePE infection sequence goes through three stages, with the DPAPILoader DLL ("Iassvc.dll") responsible for decrypting and loading an encrypted payload from disk using DPAPI. The earliest DPAPILoader artifact dates back to November 2023.

The decrypted payload is another loader, RemotePELoader, which is designed to contact a remote server ("aes-secure[.]net") over HTTP, fetch the core module, and execute it in memory, but not before taking steps to evade detection using techniques like [Hell's Gate](https://redops.at/en/blog/exploring-hells-gate) and patching Event Tracing for Windows ([ETW](https://learn.microsoft.com/en-us/windows-hardware/test/wpt/event-tracing-for-windows)).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqmMPxISomwXcWytlbLezGrDEPALs6lQmO8iYfcr6KWOszZfpCH0K_u8-fKXBjLoGZvoBMZdyX43rhktIzwhGz9QQikxg4931vGOsqE7H_oduwQrwRzQzjF3pN1A2VMs9TnR8X4wDWjZOdoWlmbvmLRTHft5XEbauPFcAu-M1RgQ3ut55KCDHmNkLI-GDO/s1700-e365/stage.png)

The final stage is a full-fledged remote access trojan named RemotePE that's written in C++ and polls a command-and-control (C2) server for further instructions. The malware supports six categories of commands, allowing it to -

* Obtain or modify the C2 configuration
* Get or change the current working directory, register a new DLL module, get loaded DLLs, and unload a DLL
* Perform file operations
* Get a list of running processes, create a new process, or kill process by ID
* Sleep for a predetermined interval or exit RemotePE
* Ping the server

A notable aspect of the file deletion command is that it overwrites each file with constant bytes seven times before renaming and deleting it, a pattern also observed in PondRAT and POOLRAT (aka SIMPLESEA). [PondRAT](https://thehackernews.com/2024/09/new-pondrat-malware-hidden-in-python.html) is assessed to be a lightweight version of POOLRAT.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Fox-IT said it obtained four RemotePE samples that indicate the RAT was under active development between mid-2023 and mid-2024. The first version has a compilation timestamp of July 4, 2023.

"The toolset's environmental keying, memory-only execution, EDR evasion, and low forensic footprint suggest it is purpose-built for long-term observation campaigns," the researchers said. "This allows the actor to quietly maintain access over an extended period before moving to a high-impact final objective such as data theft or a large-scale financial heist, consistent with this actor's known history."

"The actor-in-the-loop delivery model and the toolset's low detection rate (neither RemotePELoader nor RemotePE appeared on VirusTotal prior to this publication) suggest this toolset may be reserved for high-value targets where long-term, stealthy access is the objective, consistent with this Lazarus subgroup's known focus on financial and cryptocurrency organizations."

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

[cryptocurrency](https://the...