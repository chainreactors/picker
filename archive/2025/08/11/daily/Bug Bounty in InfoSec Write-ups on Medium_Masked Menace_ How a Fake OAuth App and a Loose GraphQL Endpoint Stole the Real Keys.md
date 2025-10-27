---
title: Masked Menace: How a Fake OAuth App and a Loose GraphQL Endpoint Stole the Real Keys
url: https://infosecwriteups.com/masked-menace-how-a-fake-oauth-app-and-a-loose-graphql-endpoint-stole-the-real-keys-cec06ed964cd?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-11
fetch_date: 2025-10-07T00:16:49.259704
---

# Masked Menace: How a Fake OAuth App and a Loose GraphQL Endpoint Stole the Real Keys

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fcec06ed964cd&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmasked-menace-how-a-fake-oauth-app-and-a-loose-graphql-endpoint-stole-the-real-keys-cec06ed964cd&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmasked-menace-how-a-fake-oauth-app-and-a-loose-graphql-endpoint-stole-the-real-keys-cec06ed964cd&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-cec06ed964cd---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-cec06ed964cd---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🎭 Masked Menace: How a Fake OAuth App and a Loose GraphQL Endpoint Stole the Real Keys 🔑

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--cec06ed964cd---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--cec06ed964cd---------------------------------------)

4 min read

·

Aug 9, 2025

--

1

Share

## ☕ How It All Started (and Why Coffee is My Only Real OAuth)

Free [link](https://medium.com/%40iski/cec06ed964cd?sk=0bc8ea41f09c59b13cafb806143e2347) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by Perplexity AI

One cold morning (well… the AC was on), I was running mass recon.
 You know the drill: Spotify playing in the background, multiple terminal windows open, and me praying my internet wouldn’t drop mid-`ffuf` scan.

That’s when I stumbled upon something… *shiny*.
 A **GraphQL endpoint** sitting quietly behind an OAuth authorization flow.
 The kind of thing that doesn’t scream “I’m vulnerable,” but whispers, *“Psst… I’ve got secrets.”*

## 🕵️ Recon Phase: The Hunter’s Breakfast 🍳

I wasn’t looking for your regular boring `?id=123` stuff. I wanted **juicy** — the kind of endpoint that corporate lawyers lose sleep over.
 So I fired up my mass recon:

```
subfinder -d target.com | httpx -title -status-code -content-length -mc 200
```

Out popped a suspicious domain:

```
auth-api.target.com
```

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--cec06ed964cd---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--cec06ed964cd---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--cec06ed964cd---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--cec06ed964cd---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--cec06ed964cd---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--cec06ed964cd---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--cec06ed964cd---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--cec06ed964cd---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--cec06ed964cd---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--cec06ed964cd---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----cec06ed964cd---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----cec06ed964cd---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----cec06ed964cd---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----cec06ed964cd---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----cec06ed964cd---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----cec06ed964cd---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----cec06ed964cd---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----cec06ed964cd---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----cec06ed964cd---------------------------------------)