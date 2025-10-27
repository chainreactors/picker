---
title: GamaCopy Mimics Gamaredon Tactics in Cyber Espionage Targeting Russian Entities
url: https://thehackernews.com/2025/01/gamacopy-mimics-gamaredon-tactics-in.html
source: The Hacker News
date: 2025-01-28
fetch_date: 2025-10-06T20:12:53.802269
---

# GamaCopy Mimics Gamaredon Tactics in Cyber Espionage Targeting Russian Entities

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

# [GamaCopy Mimics Gamaredon Tactics in Cyber Espionage Targeting Russian Entities](https://thehackernews.com/2025/01/gamacopy-mimics-gamaredon-tactics-in.html)

**Jan 27, 2025**Ravie LakshmananCyber Espionage / Threat Intelligence

[![Cyber Espionage](data:image/png;base64... "Cyber Espionage")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRlH9GS8HmHTsccsr9C_O9JHntOBD3VQT7nb2A5MvJ4aT-3R7f0u1_MlueIVVa_lZmutu_QRg9WfZLLT_QoPguIVbPCWJxvnfAZ_WXX2lGBTGPRmRbPTS1HNb6t8qEwb9CsXK85ffccfwbRn_WZSupZNmOGyaXUkHubBWcrjgsVYa4FkVECwh6h_DspBbe/s790-rw-e365/russia.png)

A previously unknown threat actor has been observed copying the tradecraft associated with the Kremlin-aligned [Gamaredon](https://thehackernews.com/2024/12/gamaredon-deploys-android-spyware.html) hacking group in its cyber attacks targeting Russian-speaking entities.

The campaign has been attributed to a threat cluster dubbed **GamaCopy**, which is assessed to share overlaps with another hacking group named [Core Werewolf](https://thehackernews.com/2024/10/cyberattack-group-awaken-likho-targets.html), also tracked as Awaken Likho and PseudoGamaredon.

According to the Knownsec 404 Advanced Threat Intelligence team, the attacks leverage content related to military facilities as lures to drop UltraVNC, allowing threat actors to remotely access the compromised hosts.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The TTP (Tactics, Techniques, and Procedures) of this organization imitates that of the Gamaredon organization which conducts attacks against Ukraine," the company [said](https://medium.com/%40knownsec404team/love-and-hate-under-war-the-gamacopy-organization-which-imitates-the-russian-gamaredon-uses-560ba5e633fa) in a report published last week.

The disclosure arrives nearly four months after Kaspersky revealed that Russian government agencies and industrial entities have been the target of Core Werewolf, with the spear-phishing attacks paving the way for the MeshCentral platform instead of UltraVNC.

The starting point of the attack chain mirrors the one detailed by the Russian cybersecurity company wherein a self-extracting (SFX) archive file created using 7-Zip acts as a conduit to drop next-stage payloads. This includes a batch script that's responsible for delivering UltraVNC, while also displaying a decoy PDF document.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjxdjRvm1cwsCaxOpBEWAk2tnW1DGu3dVlti7uTvZKeHMCJ-BLT75zy06xg1q6i4fKzddQSE8OqH6BOlhH1KQd0PVC3SoEHDUWXl3zIUciYtM0aIsPMrCD-PjcHj-x8TqXyspaPpkcVmhiTCiTKATqT3sN6DGgCpKRkATY9eIf4fk4BiCyfbyDFeAqeC3M/s790-rw-e365/malware-attacl.png)

The UltraVNC executable is given the name "OneDrivers.exe" in a likely effort to evade detection by passing it off as a binary associated with Microsoft OneDrive.

Knownsec 404 said the activity shares several similarities with Core Werewolf campaigns, including using 7z-SFX files to install and execute UltraVNC, port 443 to connect to the server, and the use of the [EnableDelayedExpansion command](https://ss64.com/nt/delayedexpansion.html).

"Since its exposure, this organization has frequently mimicked the TTPs used by the Gararedon organization and cleverly used open-source tools as a shield to achieve its own goals while confusing the public," the company said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

GamaCopy is one of the [many threat actors](https://thehackernews.com/2025/01/cert-ua-warns-of-cyber-scams-using-fake.html) that have targeted Russian organizations in the wake of the Russo-Ukrainian war, such as Sticky Werewolf (aka [PhaseShifters](https://global.ptsecurity.com/analytics/pt-esc-threat-intelligence/kids-don-t-copy-the-new-techniques-of-the-phaseshifters-group)), Venture Wolf, and Paper Werewolf.

"Groups like PhaseShifters, PseudoGamaredon, and [Fluffy Wolf](https://thehackernews.com/2024/06/sticky-werewolf-expands-cyber-attack.html) stand out for their relentless phishing campaigns aimed at data theft," Positive Technologies' Irina Zinovkina [said](https://global.ptsecurity.com/analytics/cyberthreats-evolve-while-forecasts-signal-more-sophisticated-risks-ahead).

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

[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Gamaredon](https://thehackernews.com/search/label/Gamaredon)[malware analysis](https://thehackernews.com/search/label/malware%20analysis)[Open-Source](https://thehackernews.com/search/label/Open-Source)[Russian hackers](https://thehackernews.com/search/label/Russian%20hackers)[Spear Phishing](https://thehackernews.com/search/label/Spear%20Phishing)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](...