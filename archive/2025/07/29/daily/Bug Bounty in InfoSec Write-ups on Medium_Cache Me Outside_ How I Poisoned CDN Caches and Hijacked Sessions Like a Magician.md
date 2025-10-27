---
title: Cache Me Outside: How I Poisoned CDN Caches and Hijacked Sessions Like a Magician
url: https://infosecwriteups.com/cache-me-outside-how-i-poisoned-cdn-caches-and-hijacked-sessions-like-a-magician-4be2e65167f4?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-29
fetch_date: 2025-10-06T23:52:13.709600
---

# Cache Me Outside: How I Poisoned CDN Caches and Hijacked Sessions Like a Magician

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4be2e65167f4&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcache-me-outside-how-i-poisoned-cdn-caches-and-hijacked-sessions-like-a-magician-4be2e65167f4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcache-me-outside-how-i-poisoned-cdn-caches-and-hijacked-sessions-like-a-magician-4be2e65167f4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4be2e65167f4---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4be2e65167f4---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🎩 Cache Me Outside: How I Poisoned CDN Caches and Hijacked Sessions Like a Magician 🌀

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--4be2e65167f4---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--4be2e65167f4---------------------------------------)

4 min read

·

Jul 27, 2025

--

1

Share

Free [Link](https://medium.com/%40iski/cache-me-outside-how-i-poisoned-cdn-caches-and-hijacked-sessions-like-a-magician-4be2e65167f4?sk=a343a5468fe48918c5d11099c2cf14dd) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by AI

> ***“They said, ‘Clear your cache!’ — I said, ‘No thanks, I’d rather weaponize it 😏’.”***

## ✨ The Beginning: From Boredom to Bounty

You know that feeling when you’ve refreshed HackerOne 47 times and still no juicy target shows up? That was me.

There I was, lying in bed at 3AM, existential-crisis-level tired, when I thought — *“What if the cache could cache something… evil?”* 😈

No scope expansions, no magic recon tool buzzwords this time. Just pure headers, stale cache, and curiosity.

What followed was a 72-hour hyperfocus session powered by black coffee, spaghetti code, and the dark urge to poison something — preferably a CDN.

[## When Amazon Gave Me Free Storage (But I Gave It Back)

### Free link🎈

medium.com](https://medium.com/%40iski/when-amazon-gave-me-free-storage-but-i-gave-it-back-9734c058cd05?source=post_page-----4be2e65167f4---------------------------------------)

## 🧙‍♂️ Chapter 1: Mass Reconnaissance — The Hunt Begins

> ***Goal:*** *Find cacheable endpoints behind a CDN that reflect sensitive data via*…

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4be2e65167f4---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4be2e65167f4---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4be2e65167f4---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--4be2e65167f4---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--4be2e65167f4---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--4be2e65167f4---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--4be2e65167f4---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--4be2e65167f4---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--4be2e65167f4---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--4be2e65167f4---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----4be2e65167f4---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----4be2e65167f4---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----4be2e65167f4---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----4be2e65167f4---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----4be2e65167f4---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----4be2e65167f4---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----4be2e65167f4---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----4be2e65167f4---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----4be2e65167f4---------------------------------------)