---
title: Dev Mode Disaster: How an Open GraphQL Playground Let Me Query Everything, Including Your…
url: https://infosecwriteups.com/dev-mode-disaster-how-an-open-graphql-playground-let-me-query-everything-including-your-c2496948b162?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-29
fetch_date: 2025-10-06T23:51:47.029007
---

# Dev Mode Disaster: How an Open GraphQL Playground Let Me Query Everything, Including Your…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc2496948b162&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdev-mode-disaster-how-an-open-graphql-playground-let-me-query-everything-including-your-c2496948b162&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdev-mode-disaster-how-an-open-graphql-playground-let-me-query-everything-including-your-c2496948b162&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c2496948b162---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c2496948b162---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🧠💥 Dev Mode Disaster: How an Open GraphQL Playground Let Me Query Everything, Including Your Salary!

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--c2496948b162---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--c2496948b162---------------------------------------)

4 min read

·

Jul 28, 2025

--

1

Share

Free [Link](https://medium.com/%40iski/dev-mode-disaster-how-an-open-graphql-playground-let-me-query-everything-including-your-c2496948b162?sk=78b0feaa394549f81728e7c8ce20fba9) 🎈

**Hey there!😁**

Press enter or click to view image in full size

![]()

Image by Gemini AI

> *💭* “Just like how you don’t leave your diary open on the table, you shouldn’t leave your dev tools open on production. Unfortunately, someone did — and I peeked inside their diary… and their HR files. 😏💸”

## ☕️ It All Started with Late-Night Recon (and Too Much Coffee)

Alright, here’s the tea. It was 2:00 AM, and I was neck-deep in my usual recon rabbit hole. Caffeine was flowing through my veins like TCP packets through a firewall, and I had this itch — **what if I poked around some forgotten subdomains with dev tools accidentally exposed?**

I wasn’t wrong to try.

## 🔎 Step 1: Subdomain Enumeration Like a Stalker Ex

Used tools like:

* `assetfinder`
* `dnsx`
* `Sublist3r`
* `chaos`
* and some **dark web breach combo dumps** to correlate email dev instances

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c2496948b162---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c2496948b162---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--c2496948b162---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--c2496948b162---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--c2496948b162---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--c2496948b162---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--c2496948b162---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--c2496948b162---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--c2496948b162---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--c2496948b162---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----c2496948b162---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----c2496948b162---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----c2496948b162---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----c2496948b162---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----c2496948b162---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----c2496948b162---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----c2496948b162---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----c2496948b162---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----c2496948b162---------------------------------------)