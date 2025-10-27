---
title: 17. My Favorite Bug Classes (and Why They Work)
url: https://infosecwriteups.com/17-my-favorite-bug-classes-and-why-they-work-b67a03ab8c43?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-21
fetch_date: 2025-10-02T20:28:35.963223
---

# 17. My Favorite Bug Classes (and Why They Work)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb67a03ab8c43&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F17-my-favorite-bug-classes-and-why-they-work-b67a03ab8c43&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F17-my-favorite-bug-classes-and-why-they-work-b67a03ab8c43&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b67a03ab8c43---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b67a03ab8c43---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 17. My Favorite Bug Classes (and Why They Work)

## Turning Small Flaws into Big Wins: A Practical Guide to My Favorite Bug Classes

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:64:64/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--b67a03ab8c43---------------------------------------)

[Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--b67a03ab8c43---------------------------------------)

9 min read

·

Sep 19, 2025

--

1

Share

🔐Free Article [Link](https://medium.com/%40kumawatabhijeet2002/17-my-favorite-bug-classes-and-why-they-work-b67a03ab8c43?sk=d93001f8e7026f52030a914fb3282537)

> “Bug bounty hunting isn’t about luck — it’s about knowing which classes of bugs consistently pay off, and learning to see them where others don’t.”

Press enter or click to view image in full size

![]()

Created by Gemini

Hey hackers 👋

I’m **Abhijeet Kumawat**, a passionate cybersecurity enthusiast, bug bounty hunter, and someone who **started with literally zero technical background.**

This write-up is the **fourth** **part of my series: “Bug Bounty from Scratch”**, where I’ll be posting **25+ deep-dive stories** on everything you need to know to start and succeed in the world of ethical hacking.

> *“And the best part? Everything I share is something I wish — — — — — someone told me when I was starting.” — — — —*

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b67a03ab8c43---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b67a03ab8c43---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b67a03ab8c43---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--b67a03ab8c43---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--b67a03ab8c43---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:96:96/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--b67a03ab8c43---------------------------------------)

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:128:128/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--b67a03ab8c43---------------------------------------)

[## Written by Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--b67a03ab8c43---------------------------------------)

[2.3K followers](https://medium.com/%40kumawatabhijeet2002/followers?source=post_page---post_author_info--b67a03ab8c43---------------------------------------)

·[33 following](https://medium.com/%40kumawatabhijeet2002/following?source=post_page---post_author_info--b67a03ab8c43---------------------------------------)

Radhe Radhe ✨ || Security Researcher || Bug Hunter || Web Application Penetration Tester || Ethical Hacker ||

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----b67a03ab8c43---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----b67a03ab8c43---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----b67a03ab8c43---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----b67a03ab8c43---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----b67a03ab8c43---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----b67a03ab8c43---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----b67a03ab8c43---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----b67a03ab8c43---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----b67a03ab8c43---------------------------------------)