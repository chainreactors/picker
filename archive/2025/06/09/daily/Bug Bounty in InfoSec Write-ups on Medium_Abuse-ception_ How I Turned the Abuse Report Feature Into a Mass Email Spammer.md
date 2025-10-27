---
title: Abuse-ception: How I Turned the Abuse Report Feature Into a Mass Email Spammer
url: https://infosecwriteups.com/abuse-ception-how-i-turned-the-abuse-report-feature-into-a-mass-email-spammer-38b38a4c3c36?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-06-09
fetch_date: 2025-10-06T22:51:53.339237
---

# Abuse-ception: How I Turned the Abuse Report Feature Into a Mass Email Spammer

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F38b38a4c3c36&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fabuse-ception-how-i-turned-the-abuse-report-feature-into-a-mass-email-spammer-38b38a4c3c36&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fabuse-ception-how-i-turned-the-abuse-report-feature-into-a-mass-email-spammer-38b38a4c3c36&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-38b38a4c3c36---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-38b38a4c3c36---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Abuse-ception: How I Turned the Abuse Report Feature Into a Mass Email Spammer 📧🢨

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--38b38a4c3c36---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--38b38a4c3c36---------------------------------------)

3 min read

·

Jun 7, 2025

--

1

Share

Free [Link](https://medium.com/%40iski/abuse-ception-how-i-turned-the-abuse-report-feature-into-a-mass-email-spammer-38b38a4c3c36?sk=756de542f59358ee21e9530b2e6133d8) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by Gemini AI

> 🪜 Monday Blues, Coffee Brews, and an Accidental Spammer Debut

Let me paint you a picture: It was a Monday morning, my coffee machine had just exploded (again), I was sleep-deprived and mildly annoyed at life. Naturally, I did what any normal bug bounty hunter would do — opened Burp Suite and started poking around a random SaaS app’s abuse reporting feature.

Because who needs peace when you can hack ethically? 🤬

Little did I know… I was about to weaponize the very thing designed to *prevent* abuse. Irony level: **MAXED OUT**.

[## Token of Misfortune: How a Refresh Token Leak Let Me Regenerate Unlimited Sessions 🔁🔑

### Free Link 🎈

infosecwriteups.com](/token-of-misfortune-how-a-refresh-token-leak-let-me-regenerate-unlimited-sessions-bb6693751c85?source=post_page-----38b38a4c3c36---------------------------------------)

## 🕵️️ Reconnaissance: That One Suspicious /report-abuse Endpoint

After some mass recon using tools like `gau`, `waybackurls`, and a sprinkle of `hakrawler`, I stumbled upon this rather innocent-looking endpoint:

```
POST /api/v1/report-abuse
```

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--38b38a4c3c36---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--38b38a4c3c36---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--38b38a4c3c36---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--38b38a4c3c36---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--38b38a4c3c36---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--38b38a4c3c36---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--38b38a4c3c36---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--38b38a4c3c36---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--38b38a4c3c36---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--38b38a4c3c36---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----38b38a4c3c36---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----38b38a4c3c36---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----38b38a4c3c36---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----38b38a4c3c36---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----38b38a4c3c36---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----38b38a4c3c36---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----38b38a4c3c36---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----38b38a4c3c36---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----38b38a4c3c36---------------------------------------)