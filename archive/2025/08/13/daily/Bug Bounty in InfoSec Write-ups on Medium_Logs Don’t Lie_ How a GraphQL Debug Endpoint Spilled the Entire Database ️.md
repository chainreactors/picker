---
title: Logs Don’t Lie: How a GraphQL Debug Endpoint Spilled the Entire Database ️
url: https://infosecwriteups.com/logs-dont-lie-how-a-graphql-debug-endpoint-spilled-the-entire-database-%EF%B8%8F-a4b859ec6a1c?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-13
fetch_date: 2025-10-07T00:16:26.496833
---

# Logs Don’t Lie: How a GraphQL Debug Endpoint Spilled the Entire Database ️

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fa4b859ec6a1c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Flogs-dont-lie-how-a-graphql-debug-endpoint-spilled-the-entire-database-%25EF%25B8%258F-a4b859ec6a1c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Flogs-dont-lie-how-a-graphql-debug-endpoint-spilled-the-entire-database-%25EF%25B8%258F-a4b859ec6a1c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-a4b859ec6a1c---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-a4b859ec6a1c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 📜 Logs Don’t Lie: How a GraphQL Debug Endpoint Spilled the Entire Database 🗄️💥

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--a4b859ec6a1c---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--a4b859ec6a1c---------------------------------------)

4 min read

·

Aug 12, 2025

--

3

Share

Free [link](https://medium.com/%40iski/logs-dont-lie-how-a-graphql-debug-endpoint-spilled-the-entire-database-%EF%B8%8F-a4b859ec6a1c?sk=c954b197d294600c659df5148023fb74) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by AI

**It all started with coffee.** ☕
 Like every bug hunter, I told myself *“I’ll just check one more domain before bed”*… and then it was 4:37 AM, I had 37 Chrome tabs open, my coffee was cold, and my cat was giving me that *“go to sleep, you idiot”* stare. 🐈

But what I stumbled upon that night was worth every drop of caffeine-induced anxiety.
 Let me take you through **how a seemingly harmless GraphQL debug endpoint decided to go full drama mode and hand me their entire database.**

[## 🪞 Mirror, Mirror in the Cache: The Day I Became a Digital Pickpocket

### Hey there!😁

infosecwriteups.com](/mirror-mirror-in-the-cache-the-day-i-became-a-digital-pickpocket-ce695a86dc87?source=post_page-----a4b859ec6a1c---------------------------------------)

## 🕵️‍♂️ Step 1 — Mass Recon & Weird GraphQL Subdomain

I was running my usual recon workflow:

```
subfinder -d target.com -silent | httpx -silent -mc 200
```

One subdomain stood out:

```
debug-api.target.com
```

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a4b859ec6a1c---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a4b859ec6a1c---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--a4b859ec6a1c---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--a4b859ec6a1c---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--a4b859ec6a1c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--a4b859ec6a1c---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--a4b859ec6a1c---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--a4b859ec6a1c---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--a4b859ec6a1c---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--a4b859ec6a1c---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----a4b859ec6a1c---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----a4b859ec6a1c---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----a4b859ec6a1c---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----a4b859ec6a1c---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----a4b859ec6a1c---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----a4b859ec6a1c---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----a4b859ec6a1c---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----a4b859ec6a1c---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----a4b859ec6a1c---------------------------------------)