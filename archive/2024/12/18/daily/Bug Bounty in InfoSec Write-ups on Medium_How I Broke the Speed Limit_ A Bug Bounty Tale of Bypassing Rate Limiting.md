---
title: How I Broke the Speed Limit: A Bug Bounty Tale of Bypassing Rate Limiting
url: https://infosecwriteups.com/how-i-broke-the-speed-limit-a-bug-bounty-tale-of-bypassing-rate-limiting-29a1ec4e8681?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-18
fetch_date: 2025-10-06T19:42:02.246659
---

# How I Broke the Speed Limit: A Bug Bounty Tale of Bypassing Rate Limiting

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F29a1ec4e8681&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-broke-the-speed-limit-a-bug-bounty-tale-of-bypassing-rate-limiting-29a1ec4e8681&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-broke-the-speed-limit-a-bug-bounty-tale-of-bypassing-rate-limiting-29a1ec4e8681&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40myselfakash20)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-29a1ec4e8681---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-29a1ec4e8681---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How I Broke the Speed Limit: A Bug Bounty Tale of Bypassing Rate Limiting

[![Akash Ghosh](https://miro.medium.com/v2/resize:fill:64:64/1*xbttpz6vUW1KE6Wd1M2OEg.png)](https://myselfakash20.medium.com/?source=post_page---byline--29a1ec4e8681---------------------------------------)

[Akash Ghosh](https://myselfakash20.medium.com/?source=post_page---byline--29a1ec4e8681---------------------------------------)

4 min read

·

Dec 17, 2024

--

Share

Press enter or click to view image in full size

![]()

You know that feeling when you’re staring at a secure application, a masterpiece of security controls? Every endpoint you poke at seems ironclad — no SQL injection, no XSS, no misconfigurations. **The walls are solid.**

But as every bug bounty hunter knows, the devil hides in the details.

I was working on a private program on one of the well-known bug bounty platforms. The target was a fintech application — a shiny platform handling payments and user authentication. At first glance, **everything screamed “tight security.”** Standard rate limits were in place on login and API endpoints to prevent brute force attacks. Responses were polished, and logs showed clean behaviors.

Or so they thought.

As I tested the login functionality, I noticed the rate-limiting mechanism kicking in after five failed login attempts. I got the infamous **“Too many requests”** message — a response every bug bounty hunter dreads because it signals proper implementation. But something didn’t feel right. There was no delay between attempts — no increasing timeout or CAPTCHA.

This was my cue to slow down, analyze, and find that crack. And trust me, **it didn’t take long for the speedometer to hit redline.**

> The Setup: Reverse…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--29a1ec4e8681---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--29a1ec4e8681---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--29a1ec4e8681---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--29a1ec4e8681---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--29a1ec4e8681---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Akash Ghosh](https://miro.medium.com/v2/resize:fill:96:96/1*xbttpz6vUW1KE6Wd1M2OEg.png)](https://myselfakash20.medium.com/?source=post_page---post_author_info--29a1ec4e8681---------------------------------------)

[![Akash Ghosh](https://miro.medium.com/v2/resize:fill:128:128/1*xbttpz6vUW1KE6Wd1M2OEg.png)](https://myselfakash20.medium.com/?source=post_page---post_author_info--29a1ec4e8681---------------------------------------)

[## Written by Akash Ghosh](https://myselfakash20.medium.com/?source=post_page---post_author_info--29a1ec4e8681---------------------------------------)

[658 followers](https://myselfakash20.medium.com/followers?source=post_page---post_author_info--29a1ec4e8681---------------------------------------)

·[2 following](https://medium.com/%40myselfakash20/following?source=post_page---post_author_info--29a1ec4e8681---------------------------------------)

Akash Ghosh|Ethical Hacker | Cybersecurity Expert | Web & Mobile Security Expert

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----29a1ec4e8681---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----29a1ec4e8681---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----29a1ec4e8681---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----29a1ec4e8681---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----29a1ec4e8681---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----29a1ec4e8681---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----29a1ec4e8681---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----29a1ec4e8681---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----29a1ec4e8681---------------------------------------)