---
title: Burp, Bounce, and Break: How SSRF to Redis Gave Me the Keys to the Castle
url: https://infosecwriteups.com/burp-bounce-and-break-how-ssrf-to-redis-gave-me-the-keys-to-the-castle-19ba546093e4?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-14
fetch_date: 2025-10-06T23:22:54.224648
---

# Burp, Bounce, and Break: How SSRF to Redis Gave Me the Keys to the Castle

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F19ba546093e4&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fburp-bounce-and-break-how-ssrf-to-redis-gave-me-the-keys-to-the-castle-19ba546093e4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fburp-bounce-and-break-how-ssrf-to-redis-gave-me-the-keys-to-the-castle-19ba546093e4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-19ba546093e4---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-19ba546093e4---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🏰💣 Burp, Bounce, and Break: How SSRF to Redis Gave Me the Keys to the Castle

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--19ba546093e4---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--19ba546093e4---------------------------------------)

4 min read

·

Jul 12, 2025

--

2

Share

Free [Link](https://medium.com/bugbountywriteup/burp-bounce-and-break-how-ssrf-to-redis-gave-me-the-keys-to-the-castle-19ba546093e4?sk=08375bc97a295b7111bca0ebd70f8986) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by Gemini AI

## “If you stare long enough into a Burp Collaborator tab, it’ll eventually stare back… usually with Redis creds.” 😵‍💫

I was just having one of *those* lazy Sundays. You know, the kind where you open Burp Suite *just* to “poke around” for a few minutes, and 14 hours later you’re still sitting in the same chair with caffeine in your blood and Redis access in your logs. 😅

Little did I know… that day I’d stumble into an SSRF so juicy, it opened the gates to an exposed Redis instance, and let me toss payloads like I was Yeeting keys into a royal vault.

[## Bypassing Like a Pro: How I Fooled the WAF and Made It Pay 💸🧢

### Hi there!

infosecwriteups.com](/bypassing-like-a-pro-how-i-fooled-the-waf-and-made-it-pay-e433193e1d9d?source=post_page-----19ba546093e4---------------------------------------)

## 🧭 Recon: Hunting Beyond the Login Page

I started with the usual mass recon routine:

* `assetfinder --subs-only target.com`
* `httpx -status -title -tech-detect -follow-redirects -timeout 10`

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--19ba546093e4---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--19ba546093e4---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--19ba546093e4---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--19ba546093e4---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--19ba546093e4---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--19ba546093e4---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--19ba546093e4---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--19ba546093e4---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--19ba546093e4---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--19ba546093e4---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----19ba546093e4---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----19ba546093e4---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----19ba546093e4---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----19ba546093e4---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----19ba546093e4---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----19ba546093e4---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----19ba546093e4---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----19ba546093e4---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----19ba546093e4---------------------------------------)