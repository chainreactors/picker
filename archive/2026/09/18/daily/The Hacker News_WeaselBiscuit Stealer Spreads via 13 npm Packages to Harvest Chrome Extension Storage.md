---
title: WeaselBiscuit Stealer Spreads via 13 npm Packages to Harvest Chrome Extension Storage
url: https://thehackernews.com/2026/09/weaselbiscuit-stealer-spreads-via-13.html
source: The Hacker News
date: 2026-09-18
fetch_date: 2026-09-19T07:02:43.851384
---

# WeaselBiscuit Stealer Spreads via 13 npm Packages to Harvest Chrome Extension Storage

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [WeaselBiscuit Stealer Spreads via 13 npm Packages to Harvest Chrome Extension Storage](https://thehackernews.com/2026/09/weaselbiscuit-stealer-spreads-via-13.html)

**Ravie Lakshmanan**Sep 18, 2026Malware / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZypkEn_5V1qllBxmH8UMxTPyA9qoXxQtKpBpJlFq2rtHgMM1wnknkyq4Vmmy0NiCHn2IjS0nyvtmiZpJ-vYOd6VxMFBexh_p6GXuq3Cjda-YfjDOUE5u5V5HfBBAQzEm5DLX3jg_ZrIfEBFlpcBod65T3Q0pXVR7vERfitlS6cBHYVG2K7ek5ivweYTRq/s1700-nu-rw-lo-l85-e365/npm-chrome.jpg)

Cybersecurity researchers have discovered a cluster of 13 npm packages that have been found to deliver a previously undocumented JavaScript stealer codenamed **WeaselBiscuit**.

The new malware family, per [OpenSourceMalware](https://opensourcemalware.com/blog/introducing-weaselbiscuit), exhibits functional overlaps with two malware strains associated with the Democratic People's Republic of Korea's (DPRK) [Contagious Interview](https://thehackernews.com/2026/06/north-korean-hackers-are-turning.html) campaign: [BeaverTail and OtterCookie](https://thehackernews.com/2025/10/north-korean-hackers-combine-beavertail.html). "It's smaller, lighter, and stripped down, with many of the heavier functions removed entirely," security researcher Paul McCarty (aka 6mile) said.

The [names of the packages](https://opensourcemalware.com/?search=%23weaselbiscuit) are below -

* @biz44/id10-client
* @biz44/id12-client
* @biz44/id44-client
* @biz44/id79-client
* @biz44/id95-client
* @biz44/id99-client
* @biz44/process-runtime-utils
* @biz44/runtime-utils
* engin1
* id79-client
* process-lhpm
* process-mite
* process-tailwind

"It's a stripped down stealer that borrows several functions from DPRK's BeaverTail and OtterCookie, but is much smaller and self-contained," Jenn Gile, co-founder of OpenSourceMalware, said in a statement shared with The Hacker News. "Hence the 'WeaselBiscuit' name, because a weasel is smaller than an otter, and we can argue that biscuits are less fancy than cookies."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

BeaverTail is the name assigned to a [cross-platform information-stealing malware](https://gitlab-com.gitlab.io/gl-security/security-tech-notes/threat-intelligence-tech-notes/north-korean-malware-sept-2025/) and downloader operated by North Korean threat actors behind Contagious Interview to target software developers, IT professionals, and cryptocurrency users. The malware has been active since at least late 2022.

On the other hand, OtterCookie [combines](https://thehackernews.com/2026/07/north-korea-linked-hackers-hide.html) information-stealing capabilities with remote access functionality that allows the operators to execute commands on compromised hosts. The malware was first publicly documented by NTT Security Holdings in December 2024.

WeaselBiscuit is notable for its simplicity, lacking remote access, persistence, cryptocurrency wallet-draining code, and the ability to deliver secondary payloads like InvisibleFerret. Instead, it's triggered via an npm import, which causes the loader ("loader.js") to pull the main malware from an Npoint dead drop and execute it directly in memory.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigMnR9TVPtZvj3-58QIeeKBXRFFztEERnlS0AQr1Q1g7vUoC1vkAZT1KGQNSNvjcG2e3fY92tOSNwtlTvu6j2JSzqDgsxd0o2gxQLG8Ds_8IsWP5XnkbsHPznbnMgWqKMwUBSIzwN-lWKVZOg1clhyzVXJe5FHiE0u8LI4C6lAkAPqdsKXaAq8P1dlOePK/s1700-nu-rw-lo-l85-e365/we.png)

Upon execution, it resolves its command-and-control (C2) configuration from a separate Npoint URL, profiles the compromised host, and harvests Chrome extension storage across Windows, macOS, and Linux. Based on operator commands received from the C2 server ("103.170.217[.]184:8787"), it can also log clipboard contents and keystrokes on Windows machines.

"While this malware does not have the same crypto wallet stealer functions as its big siblings, the Chrome extension-storage capability is financially relevant: it can expose wallet-extension state or other extension-held sensitive data," McCarty explained. "It uploads every readable, nonempty file under the extension's Local Extension Settings directory — a raw LevelDB key/value store — wholesale."

OpenSourceMalware has emphasized that despite the "meaningful overlap with DPRK-associated Contagious Interview tooling," there is no definitive evidence in terms of operator infrastructure, victimology, campaign metadata, or signing material to conclusively attribute it to North Korea.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

Other tradecraft signals that point to North Korea are as follows -

* The use of Npoint.io, a lightweight online JSON storage service – an aspect that was [flagged by NVISO](https://thehackernews.com/2025/11/north-korean-hackers-turn-json-services.html) in November 2025 in connection with Contagious Interview
* The use of nested public-IP and geolocation lookup via api.ipify.org and ip-api.com
* Similarities in C2 architecture that overlap with OtterCookie
* The use of a numerical campaign ID (10, 12, 44, 79, 95, 99) to tag each install, mirroring that of [PolinRider](https://thehackernews.com/2026/07/north-korean-hackers-publish-108.html)

If WeaselBiscuit does turn out to be the latest addition to DPRK's malware arsenal, this wouldn't be the first time the threat actors have attempted to merge the features of BeaverTail and OtterCookie. In October 2025, Cisco Talos [said](https://thehackernews.com/2025/10/north-korean-hackers-combine-beavertail.html) it identified an npm package named "node-nvm-ssh" that "had characteristics of BeaverTail and of OtterCookie, blurring the distinction between the two."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twit...