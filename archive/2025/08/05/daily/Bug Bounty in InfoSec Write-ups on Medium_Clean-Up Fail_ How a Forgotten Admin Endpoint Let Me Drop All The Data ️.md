---
title: Clean-Up Fail: How a Forgotten Admin Endpoint Let Me Drop All The Data ️
url: https://infosecwriteups.com/clean-up-fail-how-a-forgotten-admin-endpoint-let-me-drop-all-the-data-%EF%B8%8F-1e1c376a986a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-05
fetch_date: 2025-10-07T00:17:58.968005
---

# Clean-Up Fail: How a Forgotten Admin Endpoint Let Me Drop All The Data ️

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F1e1c376a986a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fclean-up-fail-how-a-forgotten-admin-endpoint-let-me-drop-all-the-data-%25EF%25B8%258F-1e1c376a986a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fclean-up-fail-how-a-forgotten-admin-endpoint-let-me-drop-all-the-data-%25EF%25B8%258F-1e1c376a986a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-1e1c376a986a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-1e1c376a986a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🧹 Clean-Up Fail: How a Forgotten Admin Endpoint Let Me Drop All The Data 🗑️🔧

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--1e1c376a986a---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--1e1c376a986a---------------------------------------)

4 min read

·

Aug 3, 2025

--

3

Share

Free [Link](https://medium.com/%40iski/clean-up-fail-how-a-forgotten-admin-endpoint-let-me-drop-all-the-data-%EF%B8%8F-1e1c376a986a?sk=fc33abc8f38adbd5db4bd37094e47fd3) 🎈

**Hey there!😁**

Press enter or click to view image in full size

![]()

Image by Perplexity AI

## “I once cleaned my house so well, I couldn’t find my own wallet for three days. Now imagine giving that cleaning power to a stranger on the internet — with one GET request.” 😅

Welcome to the story of how I accidentally (but very responsibly!) stumbled upon a forgotten cleanup endpoint that let me **nuke an entire database** — unauthenticated, unprotected, and hilariously exposed.

Yes, someone really shipped a production app with **god-mode** `/admin/wipe-all` **live in prod**.

Grab your ☕ and buckle up, this one’s a digital spring cleaning gone horribly wrong.

[## WebSocket Wizardry: How a Forgotten Channel Let Me Sniff Private Chats in Real-Time 🔌🕵️‍♂️

### Hey there!😁

infosecwriteups.com](/websocket-wizardry-how-a-forgotten-channel-let-me-sniff-private-chats-in-real-time-%EF%B8%8F-%EF%B8%8F-c8ccde8eee0f?source=post_page-----1e1c376a986a---------------------------------------)

## 🕵️ Recon Begins: The Classic Routine Turned Lucky

This story starts like most bounty adventures — **late at night**, caffeine-fueled, music blasting, and me poking around random…

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1e1c376a986a---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1e1c376a986a---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--1e1c376a986a---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--1e1c376a986a---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--1e1c376a986a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--1e1c376a986a---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--1e1c376a986a---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--1e1c376a986a---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--1e1c376a986a---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--1e1c376a986a---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----1e1c376a986a---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----1e1c376a986a---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----1e1c376a986a---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----1e1c376a986a---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----1e1c376a986a---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----1e1c376a986a---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----1e1c376a986a---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----1e1c376a986a---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----1e1c376a986a---------------------------------------)