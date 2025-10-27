---
title: Hackers Create Malicious Dota 2 Game Modes to Secretly Access Players' Systems
url: https://thehackernews.com/2023/02/hackers-create-malicious-dota-2-game.html
source: The Hacker News
date: 2023-02-14
fetch_date: 2025-10-04T06:33:39.803592
---

# Hackers Create Malicious Dota 2 Game Modes to Secretly Access Players' Systems

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

# [Hackers Create Malicious Dota 2 Game Modes to Secretly Access Players' Systems](https://thehackernews.com/2023/02/hackers-create-malicious-dota-2-game.html)

**Feb 13, 2023**Ravie LakshmananGame Hacking / Cyber Threat

[![Dota 2 Game Modes](data:image/png;base64... "Dota 2 Game Modes")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZ5EqGS9M-uWz6i8kYOjBKdLpSXrkKSk6QNM-jbWSUnjAa0fMoI-9Jo9UWv4Hhrt7PKl1E8_KhYdxQu-1EEKyXUbalRCjNiUSmVYb7Y3OwGbHb3GCieFJCSGkvxMOMWSIhqWGTQcRRSHSiPgQLQKDXfl03fJ53evbWAIGV2FbKx7UTCAUWvp2MDL9a/s790-rw-e365/dota2.png)

An unknown threat actor created malicious game modes for the Dota 2 multiplayer online battle arena (MOBA) video game that could have been exploited to establish backdoor access to players' systems.

The modes exploited a [high-severity flaw](https://starlabs.sg/blog/2022/12-the-hole-new-world-how-a-small-leak-will-sink-a-great-browser-cve-2021-38003/) in the V8 JavaScript engine tracked as [CVE-2021-38003](https://nvd.nist.gov/vuln/detail/CVE-2021-38003) (CVSS score: 8.8), which was [exploited as a zero-day](https://thehackernews.com/2021/10/google-releases-urgent-chrome-update-to.html) and addressed by Google in October 2021.

"Since V8 was not sandboxed in Dota, the exploit on its own allowed for remote code execution against other Dota players," Avast researcher Jan Vojtěšek [said](https://decoded.avast.io/janvojtesek/dota-2-under-attack-how-a-v8-bug-was-exploited-in-the-game/) in a report published last week.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Following responsible disclosure to Valve, the game publisher [shipped fixes](https://www.dota2.com/news/updates) on January 12, 2023, by upgrading the version of V8.

Game modes are essentially [custom capabilities](https://dota2.fandom.com/wiki/Game_modes) that can either augment an existing title or offer completely new gameplay in a manner that deviates from the standard rules.

While publishing a custom game mode to the Steam store includes a vetting process from Valve, the malicious game modes discovered by the antivirus vendor managed to slip through the cracks.

These game modes, which have since been taken down, are "test addon plz ignore," "Overdog no annoying heroes," "Custom Hero Brawl," and "Overthrow RTZ Edition X10 XP." The threat actor is also said to have published a fifth game mode named "Brawl in Petah Tiqwa" that did not pack any rogue code.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhk3nBsPsMeqEwHfBlV_VBFgxDava3pfbAj25xlNU2UzOMa2p_qpJ6SImA8vlYA4g3fN4YuTntn090Y-CDI__zAaCoQtFtVW5SK52TsuN9yIS28b29zxkY6nsXRjc4VQ8-iERrdW1FuyR84ZBLfb83hgphi_Am3cYDqKqttn3TXw5-ckFZgu3kakylk/s790-rw-e365/hack.png)

Embedded inside "test addon plz ignore" is an exploit for the V8 flaw that could be weaponized to execute custom shellcode.

The three others, on the other hand, take a more covert approach in that the malicious code is designed to reach out to a remote server to fetch a JavaScript payload, which is also likely to be an exploit for CVE-2021-38003 since the server is no longer reachable.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

In a hypothetical attack scenario, a player launching one of the above game modes could be targeted by the threat actor to achieve remote access to the infected host and deploy additional malware for further exploitation.

It's not immediately known what the developer's end goals were behind creating the game modes, but they are unlikely to be for benign research purposes, Avast noted.

"First, the attacker did not report the vulnerability to Valve (which would generally be considered a nice thing to do)," Vojtěšek said. "Second, the attacker tried to hide the exploit in a stealthy backdoor."

"Regardless, it's also possible that the attacker didn't have purely malicious intentions either, since such an attacker could arguably abuse this vulnerability with a much larger impact."

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

[Chrome](https://thehackernews.com/search/label/Chrome)[game hacking](https://thehackernews.com/search/label/game%20hacking)[Google](https://thehackernews.com/search/label/Google)[zero-day](https://thehackernews.com/search/label/zero-day)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AW...