---
title: From CSS to AWS: How a Stylesheet Reference Leaked Cloud Secrets ☁️
url: https://infosecwriteups.com/from-css-to-aws-how-a-stylesheet-reference-leaked-cloud-secrets-%EF%B8%8F-c55e5048777e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-04-21
fetch_date: 2025-10-06T22:04:15.006897
---

# From CSS to AWS: How a Stylesheet Reference Leaked Cloud Secrets ☁️

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc55e5048777e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-css-to-aws-how-a-stylesheet-reference-leaked-cloud-secrets-%25EF%25B8%258F-c55e5048777e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-css-to-aws-how-a-stylesheet-reference-leaked-cloud-secrets-%25EF%25B8%258F-c55e5048777e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c55e5048777e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c55e5048777e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# From CSS to AWS: How a Stylesheet Reference Leaked Cloud Secrets 🎨☁️

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--c55e5048777e---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--c55e5048777e---------------------------------------)

3 min read

·

Apr 17, 2025

--

1

Share

Hey there!

Free [Link](https://medium.com/%40iski/from-css-to-aws-how-a-stylesheet-reference-leaked-cloud-secrets-%EF%B8%8F-c55e5048777e?sk=039ee5c9897c9697be54e523d00e48fd)🎈

Press enter or click to view image in full size

![]()

image by Gemini Ai

> *TL;DR: A harmless-looking CSS file turned out to be a treasure chest of exposed AWS keys. In this story, I’ll walk you through how I found cloud credentials inside a stylesheet during recon, verified access, and escalated it to a full-blown cloud pwn. All wrapped in a real, funny, and technical tale you won’t forget.*

## 😅 Life Be Like…

I was debugging my life, one HTTP response at a time. My bank balance was throwing a 403 Forbidden, my sleep cycle was a 500 Internal Server Error, and my social life? Yeah, that’s a 404 Not Found.

So I did what any responsible adult does: opened my terminal and started recon.

## 🚀 Phase 1: Recon Until Something Breaks

The game began with:

* `subfinder` + `amass` + `httpx` for asset discovery
* JS scraping with `getJS` + `LinkFinder`
* `gau` and `waybackurls` for hidden treasures
* Mass content download using `wget` and `hakrawler`

While going through the responses, I stumbled upon this juicy-looking CSS reference:

```
<link rel="stylesheet"…
```

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c55e5048777e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c55e5048777e---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--c55e5048777e---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--c55e5048777e---------------------------------------)

·[Last published 1 hour ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--c55e5048777e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--c55e5048777e---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--c55e5048777e---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--c55e5048777e---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--c55e5048777e---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--c55e5048777e---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----c55e5048777e---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----c55e5048777e---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----c55e5048777e---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----c55e5048777e---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----c55e5048777e---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----c55e5048777e---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----c55e5048777e---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----c55e5048777e---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----c55e5048777e---------------------------------------)