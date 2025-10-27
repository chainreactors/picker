---
title: P4 Bugs and PoC | Part 3
url: https://infosecwriteups.com/p4-bugs-and-poc-part-3-8ca9776c87bc?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-05
fetch_date: 2025-10-06T20:08:00.111857
---

# P4 Bugs and PoC | Part 3

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8ca9776c87bc&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fp4-bugs-and-poc-part-3-8ca9776c87bc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fp4-bugs-and-poc-part-3-8ca9776c87bc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8ca9776c87bc---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8ca9776c87bc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# P4 Bugs and POC | Part 3

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:64:64/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--8ca9776c87bc---------------------------------------)

[Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--8ca9776c87bc---------------------------------------)

4 min read

·

Jan 3, 2025

--

Share

👋 **Hi everyone!**
I’m **Abhijeet Kumawat**, a passionate bug bounty hunter and security researcher. I love sharing my experiences and insights in bug bounty hunting and penetration testing. Today, I’m thrilled to continue my **P4 Bug Series** — where I uncover some low-severity vulnerabilities that are often overlooked but can provide significant learning and even impactful results when exploited.

In this post, I’ll cover two interesting P4 vulnerabilities: **Content Spoofing** and **Failure to Invalidate Session on Password Reset/Change**. Both of these bugs are relatively simple to understand and exploit, making them perfect for beginner bug hunters or those looking to sharpen their skills. 🚀

Press enter or click to view image in full size

![]()

Created by Copilot

[## Received an Appreciation Letter from NASA 🏆

### How I Got an Appreciation Letter from NASA 🚀

medium.com](https://medium.com/%40kumawatabhijeet2002/received-an-appreciation-letter-from-nasa-927c3d1ae828?source=post_page-----8ca9776c87bc---------------------------------------)

## 🔍 1. Content Spoofing

**Description:**
Content Spoofing allows attackers to manipulate how content appears on a webpage, misleading users by displaying fake messages or misleading information under the guise of a trusted domain. This vulnerability is often exploited in **social engineering attacks**, where users are tricked into taking unintended actions, such as entering…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8ca9776c87bc---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8ca9776c87bc---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--8ca9776c87bc---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--8ca9776c87bc---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--8ca9776c87bc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:96:96/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--8ca9776c87bc---------------------------------------)

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:128:128/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--8ca9776c87bc---------------------------------------)

[## Written by Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--8ca9776c87bc---------------------------------------)

[2.4K followers](https://medium.com/%40kumawatabhijeet2002/followers?source=post_page---post_author_info--8ca9776c87bc---------------------------------------)

·[33 following](https://medium.com/%40kumawatabhijeet2002/following?source=post_page---post_author_info--8ca9776c87bc---------------------------------------)

Radhe Radhe ✨ || Security Researcher || Bug Hunter || Web Application Penetration Tester || Ethical Hacker ||

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----8ca9776c87bc---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----8ca9776c87bc---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----8ca9776c87bc---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----8ca9776c87bc---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----8ca9776c87bc---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----8ca9776c87bc---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----8ca9776c87bc---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----8ca9776c87bc---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----8ca9776c87bc---------------------------------------)