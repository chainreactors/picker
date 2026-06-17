---
title: Bug Bounty Bootcamp #45: Token?
url: https://infosecwriteups.com/bug-bounty-bootcamp-45-token-2b606811c7ba?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-16
fetch_date: 2026-06-17T07:02:19.666109
---

# Bug Bounty Bootcamp #45: Token?

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-bootcamp-45-token-2b606811c7ba&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-bootcamp-45-token-2b606811c7ba&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2b606811c7ba---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2b606811c7ba---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

# Bug Bounty Bootcamp #45: Token? What Token? — How Leaky APIs and Reset Flows Hand You Admin on a Silver Platter

## You found a password reset that leaks the magic token in the API response. Or worse — the devs left an endpoint that just *gives* you anyone’s reset code. Grab your popcorn, we’re about to take over accounts without even brute-forcing.

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--2b606811c7ba---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--2b606811c7ba---------------------------------------)

5 min read

·

4 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D2b606811c7ba&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-bootcamp-45-token-2b606811c7ba&source=---header_actions--2b606811c7ba---------------------post_audio_button------------------)

Share

[*Free Link/ Friend Link*](https://amannsharmaa.medium.com/bug-bounty-bootcamp-45-token-2b606811c7ba?sk=15d95f2b34407f75d30189983c93c016)

Press enter or click to view image in full size

![]()

Welcome back, you magnificent bug-hunting gremlin. You’ve already learned to brute-force OTPs and find hidden registration pages. But sometimes, the universe (and lazy developers) just *gives* you the keys. No guessing. No wordlists. Just a juicy API response that whispers `"resetToken": "secret123"` in your ear.

> **Today, we’re hunting leaked reset tokens, misconfigured API endpoints, and forged password reset requests that let you slip into any account like a digital ninja.**

## 1. The “Oops, I Leaked the Reset Token” Vulnerability

Imagine this: You click “Forgot Password” for the user `admin`. The app says "Reset link sent." But you, being a suspicious little hacker, check the API response in Burp.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2b606811c7ba---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2b606811c7ba---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--2b606811c7ba---------------------------------------)

[87K followers](/followers?source=post_page---post_publication_info--2b606811c7ba---------------------------------------)

·[Last published 2 days ago](/host-network-penetration-testing-network-based-attacks-ctf-1-ejpt-ine-675f149b7c1c?source=post_page---post_publication_info--2b606811c7ba---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--2b606811c7ba---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--2b606811c7ba---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--2b606811c7ba---------------------------------------)

[1.6K followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--2b606811c7ba---------------------------------------)

·[22 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--2b606811c7ba---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

[Help](https://help.medium.com/hc/en-us?source=post_page-----2b606811c7ba---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----2b606811c7ba---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----2b606811c7ba---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----2b606811c7ba---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----2b606811c7ba---------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----2b606811c7ba---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----2b606811c7ba---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----2b606811c7ba---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----2b606811c7ba---------------------------------------)