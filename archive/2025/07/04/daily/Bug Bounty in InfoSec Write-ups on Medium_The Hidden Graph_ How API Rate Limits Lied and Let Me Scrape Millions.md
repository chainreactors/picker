---
title: The Hidden Graph: How API Rate Limits Lied and Let Me Scrape Millions
url: https://infosecwriteups.com/the-hidden-graph-how-api-rate-limits-lied-and-let-me-scrape-millions-761a7cc99270?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-04
fetch_date: 2025-10-06T23:50:19.805470
---

# The Hidden Graph: How API Rate Limits Lied and Let Me Scrape Millions

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F761a7cc99270&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-hidden-graph-how-api-rate-limits-lied-and-let-me-scrape-millions-761a7cc99270&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-hidden-graph-how-api-rate-limits-lied-and-let-me-scrape-millions-761a7cc99270&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-761a7cc99270---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-761a7cc99270---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# The Hidden Graph: How API Rate Limits Lied and Let Me Scrape Millions 📈💸

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--761a7cc99270---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--761a7cc99270---------------------------------------)

4 min read

·

Jul 2, 2025

--

Share

Free [Link](https://medium.com/%40iski/the-hidden-graph-how-api-rate-limits-lied-and-let-me-scrape-millions-761a7cc99270?sk=a61c326cafbfe965a9dfe9874d4c935a) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by Gemini AI

> *Life tip: Don’t trust someone who says “I’ll call you back” or an API that says “You’ve reached your limit.” Both are lying. 😂📞💔*

It was 2:47 AM. I had just finished watching an episode of Black Mirror, where AI takes over the world, and I decided to do something safer — like poking around GraphQL endpoints. You know, normal stuff.

Little did I know, I was about to stumble upon a goldmine of user data — all because a GraphQL API said “no more” and then kept handing me *everything* like a lying ex who still sends you good morning texts. 🫣

[## 404 to Root: How a Forgotten Subdomain Led to Server Takeover 🔍🏴‍☠️

### Hey there!😁

infosecwriteups.com](/404-to-root-how-a-forgotten-subdomain-led-to-server-takeover-%EF%B8%8F-d60e65fdbc18?source=post_page-----761a7cc99270---------------------------------------)

## 🔍 The Recon: One Endpoint to Rule Them All

As usual, I started with mass recon:

```
subfinder -d target.com | httpx -mc 200 > alive.txt
```

While spidering through JavaScript files using `getJS` and `linkfinder`, I found a spicy line like this:

```
fetch('https://api.target.com/graph…
```

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--761a7cc99270---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--761a7cc99270---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--761a7cc99270---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--761a7cc99270---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--761a7cc99270---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--761a7cc99270---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--761a7cc99270---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--761a7cc99270---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--761a7cc99270---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--761a7cc99270---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----761a7cc99270---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----761a7cc99270---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----761a7cc99270---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----761a7cc99270---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----761a7cc99270---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----761a7cc99270---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----761a7cc99270---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----761a7cc99270---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----761a7cc99270---------------------------------------)