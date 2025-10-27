---
title: Desync or Die Trying: Smuggling My Way into Internal APIs
url: https://infosecwriteups.com/desync-or-die-trying-smuggling-my-way-into-internal-apis-e59e1bf6f01d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-02
fetch_date: 2025-10-06T23:49:59.520566
---

# Desync or Die Trying: Smuggling My Way into Internal APIs

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe59e1bf6f01d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdesync-or-die-trying-smuggling-my-way-into-internal-apis-e59e1bf6f01d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdesync-or-die-trying-smuggling-my-way-into-internal-apis-e59e1bf6f01d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e59e1bf6f01d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e59e1bf6f01d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **Desync or Die Trying: Smuggling My Way into Internal APIs 🚚🎯**

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--e59e1bf6f01d---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--e59e1bf6f01d---------------------------------------)

3 min read

·

Jul 1, 2025

--

1

Share

Free [Link](https://medium.com/%40iski/desync-or-die-trying-smuggling-my-way-into-internal-apis-e59e1bf6f01d?sk=0ea9797c1f07077408caad777f65280d) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by Gemini AI

**When Life Gives You Desync, Smuggle a Shell In 🌈🤔**

I once burnt toast, missed my cab, spilled coffee, and still managed to compromise a production backend — all before 11 AM. That’s what happens when you’re powered by caffeine, curiosity, and a mild hatred for poorly configured load balancers.

This is the story of how a sneaky HTTP Request Smuggling (HRS) vulnerability turned a boring recon into a jackpot of internal APIs, sensitive data, and the most beautiful `500 Internal Error` I've ever seen.

[## 🕵️ The JSON Backdoor: How I Exploited Insecure Deserialization for RCE 📦🔥

### Hey Doods!😃

infosecwriteups.com](/%EF%B8%8F-the-json-backdoor-how-i-exploited-insecure-deserialization-for-rce-1d8aa4130564?source=post_page-----e59e1bf6f01d---------------------------------------)

## 🔍 Phase 1: Recon Recon Recon

I was running mass recon one fine Tuesday morning. You know the drill:

```
subfinder -d target.com | httpx -mc 200 -title -tech-detect > alive.txt
```

One endpoint screamed “reverse proxy config from 2012” — it was on `api.target.com`. I took a closer look using Burp Suite and noticed this odd behavior:

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e59e1bf6f01d---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e59e1bf6f01d---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e59e1bf6f01d---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e59e1bf6f01d---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--e59e1bf6f01d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--e59e1bf6f01d---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--e59e1bf6f01d---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--e59e1bf6f01d---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--e59e1bf6f01d---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--e59e1bf6f01d---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----e59e1bf6f01d---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----e59e1bf6f01d---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----e59e1bf6f01d---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----e59e1bf6f01d---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----e59e1bf6f01d---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----e59e1bf6f01d---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----e59e1bf6f01d---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----e59e1bf6f01d---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----e59e1bf6f01d---------------------------------------)