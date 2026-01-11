---
title: MuddyWater Launches RustyWater RAT via Spear-Phishing Across Middle East Sectors
url: https://thehackernews.com/2026/01/muddywater-launches-rustywater-rat-via.html
source: The Hacker News
date: 2026-01-10
fetch_date: 2026-01-11T03:41:41.595586
---

# MuddyWater Launches RustyWater RAT via Spear-Phishing Across Middle East Sectors

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

# [MuddyWater Launches RustyWater RAT via Spear-Phishing Across Middle East Sectors](https://thehackernews.com/2026/01/muddywater-launches-rustywater-rat-via.html)

**Jan 10, 2026**Ravie LakshmananCyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJ8l0NucKedkyhQLr7E5BKEvF8JlDztA0fBd3dL1lku0PJHK4PqEpa1mkpxpWhYKq4MpxuL1fr9p6NbpkU8GfhFTct25hVf6bMPsTJDTfQz71Y_aQD0gv0ln0gYFDYMEbTQ1s-52sSJz0OgoVjhaDkq1TExIJzTdIrLUjmZPwe1tzKEHDO_7-JKV9_BDRQ/s790-rw-e365/1000046762.jpg)

The Iranian threat actor known as [MuddyWater](https://thehackernews.com/2025/10/iran-linked-muddywater-targets-100.html) has been attributed to a spear-phishing campaign targeting diplomatic, maritime, financial, and telecom entities in the Middle East with a Rust-based implant codenamed **RustyWater**.

"The campaign uses icon spoofing and malicious Word documents to deliver Rust based implants capable of asynchronous C2, anti-analysis, registry persistence, and modular post-compromise capability expansion," CloudSEK resetter Prajwal Awasthi [said](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant) in a report published this week.

The latest development reflects continued evolution of MuddyWater's tradecraft, which has gradually-but-steadily [reduced its reliance](https://thehackernews.com/2026/01/threatsday-bulletin-rustfs-flaw-iranian.html#iranian-group-evolves) on legitimate remote access software as a post-exploitation tool in favor of a diverse custom malware arsenal comprising tools like [Phoenix, UDPGangster](https://thehackernews.com/2025/12/muddywater-deploys-udpgangster-backdoor.html), [BugSleep (aka MuddyRot), and MuddyViper](https://thehackernews.com/2025/12/iran-linked-hackers-hits-israeli_2.html).

Also tracked as Mango Sandstorm, Static Kitten, and TA450, the hacking group is assessed to be affiliated with Iran's Ministry of Intelligence and Security (MOIS). It's been operational since at least 2017.

Attack chains distributing RustyWater are fairly straightforward: spear-phishing emails masquerading as cybersecurity guidelines come attacked with a Microsoft Word document that, when opened, instructs the victim to "[Enable content](https://thehackernews.com/2024/06/hackers-use-ms-excel-macro-to-launch.html)" so as to activate the execution of a malicious VBA macro that's responsible for deploying the Rust implant binary.

Also referred to as Archer RAT and RUSTRIC, RustyWater gathers victim machine information, detects installed security software, sets up persistence by means of a Windows Registry key, and establishes contact with a command-and-control (C2) server ("nomercys.it[.]com") to facilitate file operations and command execution.

It's worth noting that use of RUSTRIC was [flagged](https://thehackernews.com/2025/12/threatsday-bulletin-stealth-loaders-ai.html#israel-targeted-phishing) by Seqrite Labs late last month as part of attacks targeting Information Technology (IT), Managed Service Providers (MSPs), human resources, and software development companies in Israel. The activity is being tracked by the cybersecurity company under the names UNG0801 and Operation IconCat.

"Historically, MuddyWater has relied on PowerShell and VBS loaders for initial access and post-compromise operations," CloudSEK said. "The introduction of Rust-based implants represents a notable tooling evolution toward more structured, modular, and low noise RAT capabilities."

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

[Advanced Persistent Threats](https://thehackernews.com/search/label/Advanced%20Persistent%20Threats)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[email security](https://thehackernews.com/search/label/email%20security)[Malware](https://thehackernews.com/search/label/Malware)[Nation-State Hacking](https://thehackernews.com/search/label/Nation-State%20Hacking)[Remote Access Trojans](https://thehackernews.com/search/label/Remote%20Access%20Trojans)[Spear Phishing](https://thehackernews.com/search/label/Spear%20Phishing)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

Trending News

[![DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide](data:image/svg+xml;base64... "DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide")

DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide](https://thehackernews.com/2025/12/darkspectre-browser-extension-campaigns.html)

[![⚡ Weekly Recap: IoT Exploits, Wallet Breaches, Rogue Extensions, AI Abuse and More](data:image/svg+xml;base64... "⚡ Weekly Recap: IoT Exploits, Wallet Breaches, Rogue Extensions, AI Abuse and More")

⚡ Weekly Recap: IoT Exploits, Wallet Breaches, Rogue Extensions, AI Abuse and More](https://thehackernews.com/2026/01/weekly-recap-iot-exploits-wallet.html)

[![Kimwolf Android Botnet Infects Over 2 Million Devices via Exposed ADB and Proxy Networks](data:image/svg+xml;base64... "Kim...