---
title: Secret Sauce in Robots.txt  — How I Found Hidden Admin Panels and Debug URLs
url: https://infosecwriteups.com/secret-sauce-in-robots-txt-how-i-found-hidden-admin-panels-and-debug-urls-b7e8a11ea36f?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-04-27
fetch_date: 2025-10-06T22:03:51.761937
---

# Secret Sauce in Robots.txt  — How I Found Hidden Admin Panels and Debug URLs

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb7e8a11ea36f&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsecret-sauce-in-robots-txt-how-i-found-hidden-admin-panels-and-debug-urls-b7e8a11ea36f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsecret-sauce-in-robots-txt-how-i-found-hidden-admin-panels-and-debug-urls-b7e8a11ea36f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b7e8a11ea36f---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b7e8a11ea36f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🍔 Secret Sauce in Robots.txt 🤫 — How I Found Hidden Admin Panels and Debug URLs

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--b7e8a11ea36f---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--b7e8a11ea36f---------------------------------------)

3 min read

·

Apr 25, 2025

--

10

Share

Free [Link](https://medium.com/%40iski/secret-sauce-in-robots-txt-how-i-found-hidden-admin-panels-and-debug-urls-b7e8a11ea36f?sk=4401ba13d2d74fe9a6addca8530333d5)🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by Copilot AI

## You ever open a fast-food menu, order the usual, and suddenly wonder, “What if there’s a secret item they’re hiding from me?” 🍔👀

That’s exactly how I felt scrolling through subdomains during a late-night recon session. Hungry for bugs, exhausted, and hoping for some “hacker happy meal.”

Little did I know, I was about to get served with a hot plate of misconfigured `robots.txt` that exposed more than just web crawlers. 😏

Let me serve you the story of how a plain text file spilled the beans on hidden admin panels, debug URLs, and more!

## 🔍 Recon Days: Scanning Like a Nosy Neighbor

It was a lazy Sunday. The kind of day where you’re half-debugging a script and half-watching Netflix. I decided to run a passive recon scan on a target that looked boring at first — but you know how boring apps have the dirtiest secrets 👀.

As part of my routine recon, I always check the basics:

* `sitemap.xml`
* `robots.txt`
* `/.git/`

--

--

10

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b7e8a11ea36f---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b7e8a11ea36f---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b7e8a11ea36f---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--b7e8a11ea36f---------------------------------------)

·[Last published 1 hour ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--b7e8a11ea36f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--b7e8a11ea36f---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--b7e8a11ea36f---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--b7e8a11ea36f---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--b7e8a11ea36f---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--b7e8a11ea36f---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (10)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----b7e8a11ea36f---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----b7e8a11ea36f---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----b7e8a11ea36f---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----b7e8a11ea36f---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----b7e8a11ea36f---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----b7e8a11ea36f---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----b7e8a11ea36f---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----b7e8a11ea36f---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----b7e8a11ea36f---------------------------------------)