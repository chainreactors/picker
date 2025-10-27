---
title: How I Used SSRF to Gain Admin Access: Step-by-Step with Payloads
url: https://infosecwriteups.com/how-i-used-ssrf-to-gain-admin-access-step-by-step-with-payloads-6717457a125a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-17
fetch_date: 2025-10-06T23:28:28.618661
---

# How I Used SSRF to Gain Admin Access: Step-by-Step with Payloads

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6717457a125a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-used-ssrf-to-gain-admin-access-step-by-step-with-payloads-6717457a125a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-used-ssrf-to-gain-admin-access-step-by-step-with-payloads-6717457a125a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6717457a125a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6717457a125a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 💥 How I Used SSRF to Gain Admin Access: Step-by-Step with Payloads

[![Vipul Sonule](https://miro.medium.com/v2/resize:fill:64:64/1*3BWnARhHAdOwHCGvC440qA.png)](https://medium.com/%40vipulsonule71?source=post_page---byline--6717457a125a---------------------------------------)

[Vipul Sonule](https://medium.com/%40vipulsonule71?source=post_page---byline--6717457a125a---------------------------------------)

4 min read

·

Jul 16, 2025

--

Share

Press enter or click to view image in full size

![]()

> *“The admin dashboard was supposed to be internal-only. Until I showed them it wasn’t.”*

It started with a coffee-fueled recon session on a bug bounty target. A relatively simple app with a few features, nothing flashy. But like many modern web platforms, it had microservices and internal routes lurking just beneath the surface.

What I didn’t expect was that a simple URL preview endpoint would become my golden ticket. Using **Server-Side Request Forgery (SSRF)**, I pivoted into the internal network, uncovered an admin panel, and walked away with a high-impact vulnerability disclosure (and a solid bounty).

In this post, I’ll walk you through exactly how I did it:

* The initial discovery
* Step-by-step exploitation
* Real payloads that worked
* Tools I used
* How to protect your apps from SSRF
* And bonus tips to avoid SSRF vulnerabilities

Let’s dive in.

## 🔍 What is SSRF, and Why Is It So Dangerous?

**Server-Side Request Forgery (SSRF)** occurs when an attacker can make a server send HTTP requests to other systems, either inside or outside its…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6717457a125a---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6717457a125a---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--6717457a125a---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--6717457a125a---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--6717457a125a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Vipul Sonule](https://miro.medium.com/v2/resize:fill:96:96/1*3BWnARhHAdOwHCGvC440qA.png)](https://medium.com/%40vipulsonule71?source=post_page---post_author_info--6717457a125a---------------------------------------)

[![Vipul Sonule](https://miro.medium.com/v2/resize:fill:128:128/1*3BWnARhHAdOwHCGvC440qA.png)](https://medium.com/%40vipulsonule71?source=post_page---post_author_info--6717457a125a---------------------------------------)

[## Written by Vipul Sonule](https://medium.com/%40vipulsonule71?source=post_page---post_author_info--6717457a125a---------------------------------------)

[2.1K followers](https://medium.com/%40vipulsonule71/followers?source=post_page---post_author_info--6717457a125a---------------------------------------)

·[497 following](https://medium.com/%40vipulsonule71/following?source=post_page---post_author_info--6717457a125a---------------------------------------)

I’m a cybersecurity enthusiast and bug bounty hunter who loves programming, exploring AI, and sharing tips on hacking, coding, and tech.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----6717457a125a---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----6717457a125a---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----6717457a125a---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----6717457a125a---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----6717457a125a---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----6717457a125a---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----6717457a125a---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----6717457a125a---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----6717457a125a---------------------------------------)