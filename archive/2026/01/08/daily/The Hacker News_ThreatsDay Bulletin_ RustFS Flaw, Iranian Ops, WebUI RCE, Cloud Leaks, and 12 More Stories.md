---
title: ThreatsDay Bulletin: RustFS Flaw, Iranian Ops, WebUI RCE, Cloud Leaks, and 12 More Stories
url: https://thehackernews.com/2026/01/threatsday-bulletin-rustfs-flaw-iranian.html
source: The Hacker News
date: 2026-01-08
fetch_date: 2026-01-09T03:32:02.373673
---

# ThreatsDay Bulletin: RustFS Flaw, Iranian Ops, WebUI RCE, Cloud Leaks, and 12 More Stories

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [ThreatsDay Bulletin: RustFS Flaw, Iranian Ops, WebUI RCE, Cloud Leaks, and 12 More Stories](https://thehackernews.com/2026/01/threatsday-bulletin-rustfs-flaw-iranian.html)

**Jan 08, 2026**Ravie LakshmananCybersecurity / Hacking News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYqkrQT2-0GXXeWkPsNM5dnxJyFwJ5MdeB5Gj_PWzNa168z1Gchyphenhyphenfx3tl6fCSBzjHnmPCD7IDR38mbY36lifKUwB0qBjtX5A8vbCn_fwvsAFZcExFwJi7w4Y6G_R_rZ7QzpZEDlNkfoP7w5gGFlN6nbate4XgsNXm9GUKHlkW_DJs9mlGd7wxNWWuvK0Lu/s790-rw-e365/threatsday.jpg)

The internet never stays quiet. Every week, new hacks, scams, and security problems show up somewhere.

This week's stories show how fast attackers change their tricks, how small mistakes turn into big risks, and how the same old tools keep finding new ways to break in.

Read on to catch up before the next wave hits.

1. Honeypot Traps Hackers

   [Hackers Fall for Resecurity's Honeypot](https://www.resecurity.com/blog/article/synthetic-data-a-new-frontier-for-cyber-deception-and-honeypots)

   Cybersecurity company Resecurity revealed that it deliberately lured threat actors who claimed to be associated with Scattered LAPSUS$ Hunters ([SLH](https://thehackernews.com/2025/11/a-cybercrime-merger-like-no-other.html)) into a trap, after the group claimed on Telegram that it had hacked the company and stolen internal and client data. The company said it set up a honeytrap account populated with fake data designed to resemble real-world business data and planted a fake account on an underground marketplace for compromised credentials after it uncovered a threat actor attempting to conduct malicious activity targeting its resources in November 2025 by probing various publicly facing services and applications. The threat actor is also said to have targeted one of its employees who had no sensitive data or privileged access. "This led to a successful login by the threat actor to one of the emulated applications containing synthetic data," it [said](https://www.resecurity.com/blog/article/synthetic-data-a-new-frontier-for-cyber-deception-and-honeypots). "While the successful login could have enabled the actor to gain unauthorized access and commit a crime, it also provided us with strong proof of their activity. Between December 12 and December 24, the threat actor made over 188,000 requests attempting to dump synthetic data." As of January 4, 2025, the group removed the post announcing the hack from their Telegram channel. Resecurity said the exercise also allowed them to identify the threat actor and link one of their active Gmail accounts to a U.S.-based phone number and a Yahoo account. Regardless of the setback, new findings from CYFIRMA indicate that the loose-knit collective has resurfaced with scaled-up recruitment activity, seeking initial access brokers, insider collaborators, and corporate credentials. "Chatroom discussions repeatedly reference legacy threat brands such as LizardSquad, though these mentions remain unverified and are likely part of an intimidation or reputation-inflation strategy rather than proof of a formal alliance," it [said](https://www.cyfirma.com/research/resurgence-of-scattered-lapsus-hunters/).
2. Crypto Miner via GeoServer

   [Exploitation of GeoServer Flaw](https://asec.ahnlab.com/en/91724/)

   Threat actors are exploiting a known flaw in GeoServer, [CVE-2024-36401](https://thehackernews.com/2025/12/cisa-flags-actively-exploited-geoserver.html), to distribute an XMRig cryptocurrency miner by means of PowerShell commands. "Additionally, the same threat actor is also distributing a coin miner to WegLogic servers," AhnLab [said](https://asec.ahnlab.com/en/91724/). "It appears that they are installing CoinMiner when they scan the systems exposed to the outside world and find vulnerable services." Two other threat actors have also benefited from abusing the flaw to deliver the miner, AnyDesk for remote access, and a custom-made downloader malware dubbed "systemd" from an external server whose exact function remains unknown. "Threat actors are targeting environments where GeoServer is installed and are installing various coin miners," the company said. "The threat actor can then use NetCat, which is installed together with the coin miner, to install other malware or steal information from the system."
3. KEV Catalog Expansion

   [CISA Added 245 Flaws to KEV Catalog in 2025](https://cyble.com/blog/cisa-kev-2025-exploited-vulnerabilities-growth/)

   The U.S. Cybersecurity and Infrastructure Security Agency (CISA) [added](https://cyble.com/blog/cisa-kev-2025-exploited-vulnerabilities-growth/) 245 vulnerabilities to its Known Exploited Vulnerabilities (KEV) catalog in 2025, as the database grew to 1,484 software and hardware flaws at high risk of cyber attacks – an increase of about 20% from the previous year. In comparison, 187 vulnerabilities were added in 2023 and 185 in 2024. Of the 245 flaws, 24 were exploited by ransomware groups. Microsoft, Apple, Cisco, Fortinet, Google Chromium, Ivanti, Linux Kernel, Citrix, D-Link, Oracle, and SonicWall accounted for 105 of the total vulnerabilities added to the catalog. According to Cyble, the oldest vulnerability added to the KEV catalog in 2025 was CVE-2007-0671, a Microsoft Office Excel Remote Code Execution vulnerability. The oldest vulnerability in the catalog is CVE-2002-0367, a privilege escalation vulnerability in the Windows NT and Windows 2000 "smss.exe" debugging subsystem that has been known to be used in ransomware attacks.
4. AI Logs Dispute Deepens

   [OpenAI Ordered to Turn Over 20M ChatGPT Logs in Ongoing Copyright Suit](https://www.nytimes.com/)

   OpenAI has been [ordered](https://news.bloomberglaw.com/ip-law/openai-must-turn-over-20-million-chatgpt-logs-judge-affirms) to turn over 20 million anonymized ChatGPT logs in a consolidated AI copyright case in the U.S. after it failed to convince a federal judge to dismiss a magistrate judge's order, the company said insufficiently weighed privacy con...