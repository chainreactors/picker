---
title: How I Used Sequential IDs to Download an Entire Company’s User Database (And The Joker Helped)
url: https://infosecwriteups.com/how-i-used-sequential-ids-to-download-an-entire-companys-user-database-and-the-joker-helped-2a8dd23127e6?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-11-03
fetch_date: 2025-11-04T03:09:40.052378
---

# How I Used Sequential IDs to Download an Entire Company’s User Database (And The Joker Helped)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2a8dd23127e6&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-used-sequential-ids-to-download-an-entire-companys-user-database-and-the-joker-helped-2a8dd23127e6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-used-sequential-ids-to-download-an-entire-companys-user-database-and-the-joker-helped-2a8dd23127e6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2a8dd23127e6---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2a8dd23127e6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How I Used Sequential IDs to Download an Entire Company’s User Database (And The Joker Helped) 🃏

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--2a8dd23127e6---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--2a8dd23127e6---------------------------------------)

7 min read

·

Oct 21, 2025

--

Share

Hey there!😁

Free [Link](https://medium.com/%40iski/how-i-used-sequential-ids-to-download-an-entire-companys-user-database-and-the-joker-helped-2a8dd23127e6?sk=f969b757f5da5672e5442d0c64271a8c) 🎈

Press enter or click to view image in full size

![]()

Image by AI

You know that feeling when you’re counting sheep to fall asleep, and you realize you could probably count everyone’s bank accounts too? Yeah, that’s basically what happened to me last week. I found a sequential ID vulnerability that turned into a digital all-you-can-eat data buffet. And for some reason, The Joker decided to be my imaginary consultant throughout the whole thing. 🎭

[## Forget Me Not: How Broken Logout Functionality Let Me Ride Sessions Forever 🔄💥

### Hey there!😁

infosecwriteups.com](/forget-me-not-how-broken-logout-functionality-let-me-ride-sessions-forever-3435e6d98845?source=post_page-----2a8dd23127e6---------------------------------------)

It all started when I was testing “SecureCorp,” a company that apparently thought “secure” was just a catchy prefix. I had a basic user account and was ready for another boring session of poking around APIs. Little did I know I was about to harvest more data than a combine harvester in a wheat field.

## Act 1: The Innocent Discovery — Counting is Fun! 🔢

After my standard recon (I think `subfinder` and I need couples counseling at this point), I found SecureCorp's main API. I created a…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2a8dd23127e6---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2a8dd23127e6---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--2a8dd23127e6---------------------------------------)

[73K followers](/followers?source=post_page---post_publication_info--2a8dd23127e6---------------------------------------)

·[Last published 2 days ago](/how-i-cracked-the-ejpt-exam-in-just-3-hours-with-a-score-of-85-badc569e68ba?source=post_page---post_publication_info--2a8dd23127e6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--2a8dd23127e6---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--2a8dd23127e6---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--2a8dd23127e6---------------------------------------)

[1.92K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--2a8dd23127e6---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--2a8dd23127e6---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----2a8dd23127e6---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----2a8dd23127e6---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----2a8dd23127e6---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----2a8dd23127e6---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----2a8dd23127e6---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----2a8dd23127e6---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----2a8dd23127e6---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----2a8dd23127e6---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----2a8dd23127e6---------------------------------------)