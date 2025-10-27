---
title: Cache-Busting Bonanza: How I Bypassed Rate Limits Using HTTP Weirdness
url: https://infosecwriteups.com/cache-busting-bonanza-how-i-bypassed-rate-limits-using-http-weirdness-6d0d137cb7d7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-06-12
fetch_date: 2025-10-06T22:51:36.344148
---

# Cache-Busting Bonanza: How I Bypassed Rate Limits Using HTTP Weirdness

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6d0d137cb7d7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcache-busting-bonanza-how-i-bypassed-rate-limits-using-http-weirdness-6d0d137cb7d7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcache-busting-bonanza-how-i-bypassed-rate-limits-using-http-weirdness-6d0d137cb7d7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6d0d137cb7d7---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6d0d137cb7d7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Cache-Busting Bonanza: How I Bypassed Rate Limits Using HTTP Weirdness 🚀📥

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--6d0d137cb7d7---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--6d0d137cb7d7---------------------------------------)

3 min read

·

Jun 10, 2025

--

1

Share

Free [Link](https://medium.com/%40iski/cache-busting-bonanza-how-i-bypassed-rate-limits-using-http-weirdness-6d0d137cb7d7?sk=0b5f0749672b4053843cde5f157baece) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by Gemini AI

**Life Tip #291:** When life rate-limits you, try a weird HTTP header.

**Life Tip #292:** If that doesn’t work, just add a dot, a slash, and a sprinkle of chaos.

**Life Tip #293:** Never trust the cache. It remembers too much and forgets what it shouldn’t. 🤖

Let me tell you how I turned a dusty forgotten cache layer into my personal speedway past rate limits and security filters — all thanks to a little HTTP mischief and some good old recon magic.

[## 🕵️‍♂️ The Unwanted Guest: How Misconfigured Firebase Gave Me All the Data 📲🎁

### Free Link🎈

medium.com](https://medium.com/%40iski/%EF%B8%8F-%EF%B8%8F-the-unwanted-guest-how-misconfigured-firebase-gave-me-all-the-data-80e0e23b7250?source=post_page-----6d0d137cb7d7---------------------------------------)

## 🚦 Act 1: The Hunt Begins — and So Do the Limits

It all started on a target with a juicy `/api/upload` endpoint.

I was running a basic rate-limit test to brute-force an internal parameter. But boom — after 20 requests, I hit a **429 Too Many Requests**.

Classic.

But I wasn’t giving up that easily. My recon had already told me that there were at…

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6d0d137cb7d7---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6d0d137cb7d7---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--6d0d137cb7d7---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--6d0d137cb7d7---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--6d0d137cb7d7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--6d0d137cb7d7---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--6d0d137cb7d7---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--6d0d137cb7d7---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--6d0d137cb7d7---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--6d0d137cb7d7---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----6d0d137cb7d7---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----6d0d137cb7d7---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----6d0d137cb7d7---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----6d0d137cb7d7---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----6d0d137cb7d7---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----6d0d137cb7d7---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----6d0d137cb7d7---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----6d0d137cb7d7---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----6d0d137cb7d7---------------------------------------)