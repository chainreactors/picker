---
title: The Day I Became Everyone: How User Swapping Turned Me into a Digital Shapeshifter
url: https://infosecwriteups.com/the-day-i-became-everyone-how-user-swapping-turned-me-into-a-digital-shapeshifter-91358848a593?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-10-30
fetch_date: 2025-10-31T03:12:51.048318
---

# The Day I Became Everyone: How User Swapping Turned Me into a Digital Shapeshifter

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F91358848a593&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-day-i-became-everyone-how-user-swapping-turned-me-into-a-digital-shapeshifter-91358848a593&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-day-i-became-everyone-how-user-swapping-turned-me-into-a-digital-shapeshifter-91358848a593&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-91358848a593---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-91358848a593---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# The Day I Became Everyone: How User Swapping Turned Me into a Digital Shapeshifter 🎭👥

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--91358848a593---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--91358848a593---------------------------------------)

7 min read

·

2 days ago

--

Share

Hey there!😁

Free [Link](https://medium.com/%40iski/the-day-i-became-everyone-how-user-swapping-turned-me-into-a-digital-shapeshifter-91358848a593?sk=a3420c22df3a5f35a33f75846da7ed3d) 🎈

Press enter or click to view image in full size

![]()

Image by AI

You know that episode of Phineas and Ferb where they build a machine that lets them swap bodies and chaos ensues? Yeah, that was me last week, except instead of a sci-fi machine, I found some poorly validated API endpoints, and instead of swapping with my brother, I became every user in the system. Perry the Platypus would have been so disappointed in their security. 🦦

I was testing “MultiCorp,” a company that bragged about their “role-based access control” and “user isolation.” What they actually had was more “user suggestion control” and “user mild-separation.”

[## How I Used Sequential IDs to Download an Entire Company’s User Database (And The Joker Helped) 🃏

### Hey there!😁

medium.com](https://medium.com/%40iski/how-i-used-sequential-ids-to-download-an-entire-companys-user-database-and-the-joker-helped-2a8dd23127e6?source=post_page-----91358848a593---------------------------------------)

## Act 1: The Accidental Discovery — “Hey, Where’d My Data Go?” 🤔

After my usual recon (I’ve started giving `subfinder` motivational speeches), I found MultiCorp's API. I had two test accounts: `user_a` (basic permissions) and `user_b` (slightly less basic permissions).

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--91358848a593---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--91358848a593---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--91358848a593---------------------------------------)

[73K followers](/followers?source=post_page---post_publication_info--91358848a593---------------------------------------)

·[Last published 18 hours ago](/how-i-hacked-iit-delhi-885a7f810292?source=post_page---post_publication_info--91358848a593---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--91358848a593---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--91358848a593---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--91358848a593---------------------------------------)

[1.91K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--91358848a593---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--91358848a593---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----91358848a593---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----91358848a593---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----91358848a593---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----91358848a593---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----91358848a593---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----91358848a593---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----91358848a593---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----91358848a593---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----91358848a593---------------------------------------)