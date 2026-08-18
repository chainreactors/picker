---
title: Hacker Holidays 2026: Day 8 Walkthrough (Towel on the Sunbed)
url: https://infosecwriteups.com/hacker-holidays-2026-day-8-walkthrough-towel-on-the-sunbed-4cd1f708eb3c?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-08-17
fetch_date: 2026-08-18T02:52:10.548369
---

# Hacker Holidays 2026: Day 8 Walkthrough (Towel on the Sunbed)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhacker-holidays-2026-day-8-walkthrough-towel-on-the-sunbed-4cd1f708eb3c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhacker-holidays-2026-day-8-walkthrough-towel-on-the-sunbed-4cd1f708eb3c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40dhanushnehru)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4cd1f708eb3c---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4cd1f708eb3c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

Hacker Holidays 2026

Tryhackme

Cybersecurity

Race Condition

Bug Bounty

# Hacker Holidays 2026: Day 8 Walkthrough (Towel on the Sunbed)

## **A rewards system let you claim 50 points every 24 hours. We claimed it three times in the same millisecond. Welcome to race conditions.**

[![Dhanush N](https://miro.medium.com/v2/resize:fill:64:64/1*g-aoUi88UKMpAxezY9NcmQ.png)](https://dhanushnehru.medium.com/?source=post_page---byline--4cd1f708eb3c---------------------------------------)

[Dhanush N](https://dhanushnehru.medium.com/?source=post_page---byline--4cd1f708eb3c---------------------------------------)

6 min read

·

Aug 4, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D4cd1f708eb3c&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhacker-holidays-2026-day-8-walkthrough-towel-on-the-sunbed-4cd1f708eb3c&source=---header_actions--4cd1f708eb3c---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

*This is part of my Hacker Holidays 2026 walkthrough series.*

*Read all walkthroughs here:*

[## TryHackMe Walkthroughs: Hacker Holidays 2026

### TryHackMe Walkthroughs: Hacker Holidays 2026 · 15 stories on Medium

dhanushnehru.medium.com](https://dhanushnehru.medium.com/list/tryhackme-walkthroughs-hacker-holidays-2026-2a4c4e1e9924?source=post_page-----4cd1f708eb3c---------------------------------------)

This is Day 8 of my Hacker Holidays 2026 walkthrough series. After the intense multi-stage Boot2Root on Day 7, today’s challenge is elegant in its simplicity. We are exploiting a **race condition** to bypass a rewards system and reach a balance we should never have been able to achieve.

The concept is deceptively simple but the real-world implications are massive. Race conditions have been used to steal real money from financial platforms, duplicate in-game items worth thousands of dollars and bypass access controls on production systems.

## The Setup

The challenge gives us a clear itinerary:

1. Create a guest account and…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4cd1f708eb3c---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4cd1f708eb3c---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4cd1f708eb3c---------------------------------------)

[88K followers](/followers?source=post_page---post_publication_info--4cd1f708eb3c---------------------------------------)

·[Last published 6 hours ago](/proving-grounds-practice-authby-3da2d1396a23?source=post_page---post_publication_info--4cd1f708eb3c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Dhanush N](https://miro.medium.com/v2/resize:fill:96:96/1*g-aoUi88UKMpAxezY9NcmQ.png)](https://dhanushnehru.medium.com/?source=post_page---post_author_info--4cd1f708eb3c---------------------------------------)

[![Dhanush N](https://miro.medium.com/v2/resize:fill:128:128/1*g-aoUi88UKMpAxezY9NcmQ.png)](https://dhanushnehru.medium.com/?source=post_page---post_author_info--4cd1f708eb3c---------------------------------------)

[## Written by Dhanush N](https://dhanushnehru.medium.com/?source=post_page---post_author_info--4cd1f708eb3c---------------------------------------)

[1.6K followers](https://dhanushnehru.medium.com/followers?source=post_page---post_author_info--4cd1f708eb3c---------------------------------------)

·[30 following](https://medium.com/%40dhanushnehru/following?source=post_page---post_author_info--4cd1f708eb3c---------------------------------------)

CISO 🛡️ Cybersecurity Enthusiast. I build, break and hack systems while exploring the art of problem-solving. 🔗 [https://www.youtube.com/@dhanushnehru](https://www.youtube.com/%40dhanushnehru)

[Help](https://help.medium.com/hc/en-us?source=post_page-----4cd1f708eb3c---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----4cd1f708eb3c---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----4cd1f708eb3c---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----4cd1f708eb3c---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----4cd1f708eb3c---------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----4cd1f708eb3c---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----4cd1f708eb3c---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----4cd1f708eb3c---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----4cd1f708eb3c---------------------------------------)