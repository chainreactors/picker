---
title: Stored XSS Filter Bypass in the Skills section
url: https://infosecwriteups.com/stored-xss-filter-bypass-in-the-skills-section-7bf5e33c8ace?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-11-15
fetch_date: 2025-10-06T19:17:49.451754
---

# Stored XSS Filter Bypass in the Skills section

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7bf5e33c8ace&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fstored-xss-filter-bypass-in-the-skills-section-7bf5e33c8ace&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fstored-xss-filter-bypass-in-the-skills-section-7bf5e33c8ace&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-7bf5e33c8ace---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-7bf5e33c8ace---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Stored XSS Filter Bypass in the Skills section

[![Krishna Kumar](https://miro.medium.com/v2/resize:fill:64:64/1*BZbDP0Rryv1evj1rWveHPA.jpeg)](https://xalgord.medium.com/?source=post_page---byline--7bf5e33c8ace---------------------------------------)

[Krishna Kumar](https://xalgord.medium.com/?source=post_page---byline--7bf5e33c8ace---------------------------------------)

3 min read

·

Aug 16, 2023

--

8

Share

Inspired by my recent post on LinkedIn, I’m excited to share my first-ever write-up on Medium. In this article, I’ll take you through my experience of finding a stored Cross-Site Scripting (XSS) vulnerability by getting around filters. Let’s dive into the details of my journey. For non-premium medium members, here you can read it for free: [https://infosecwriteups.com/stored-xss-filter-bypass-in-the-skills-section-7bf5e33c8ace?source=friends\_link&sk=2ce56c0e6ed7356d0365210c756f16b1](/stored-xss-filter-bypass-in-the-skills-section-7bf5e33c8ace?sk=2ce56c0e6ed7356d0365210c756f16b1)

So let’s get started.

![]()

1. **Finding the Target**:

I chose a target website and explored it as a regular user. After signing up and logging in, I checked out the different sections available to users with accounts.

![]()

2. **Exploring the Vulnerable Section**:

Among the options, I clicked on “Settings” and then “Profile Summary.” Here, I found a place where users could list their skills, which seemed like a good spot to test for an XSS exploit.

--

--

8

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7bf5e33c8ace---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7bf5e33c8ace---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--7bf5e33c8ace---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--7bf5e33c8ace---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--7bf5e33c8ace---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Krishna Kumar](https://miro.medium.com/v2/resize:fill:96:96/1*BZbDP0Rryv1evj1rWveHPA.jpeg)](https://xalgord.medium.com/?source=post_page---post_author_info--7bf5e33c8ace---------------------------------------)

[![Krishna Kumar](https://miro.medium.com/v2/resize:fill:128:128/1*BZbDP0Rryv1evj1rWveHPA.jpeg)](https://xalgord.medium.com/?source=post_page---post_author_info--7bf5e33c8ace---------------------------------------)

[## Written by Krishna Kumar](https://xalgord.medium.com/?source=post_page---post_author_info--7bf5e33c8ace---------------------------------------)

[264 followers](https://xalgord.medium.com/followers?source=post_page---post_author_info--7bf5e33c8ace---------------------------------------)

·[13 following](https://medium.com/%40xalgord/following?source=post_page---post_author_info--7bf5e33c8ace---------------------------------------)

Penetration tester | Bug Bounty Hunter

## Responses (8)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----7bf5e33c8ace---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----7bf5e33c8ace---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----7bf5e33c8ace---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----7bf5e33c8ace---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----7bf5e33c8ace---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----7bf5e33c8ace---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----7bf5e33c8ace---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----7bf5e33c8ace---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----7bf5e33c8ace---------------------------------------)