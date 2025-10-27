---
title: P4 Bugs and PoC | Part 2
url: https://infosecwriteups.com/p4-bugs-and-poc-part-2-0842039eddf3?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-05
fetch_date: 2025-10-06T20:07:57.019006
---

# P4 Bugs and PoC | Part 2

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F0842039eddf3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fp4-bugs-and-poc-part-2-0842039eddf3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fp4-bugs-and-poc-part-2-0842039eddf3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-0842039eddf3---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-0842039eddf3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# P4 Bugs and POC | Part 2

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:64:64/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--0842039eddf3---------------------------------------)

[Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--0842039eddf3---------------------------------------)

4 min read

·

Jan 3, 2025

--

Share

[## P4 Bugs and POC | Part 1

### P4 Bugs and POC | Part 1: Broken Link Hijacking

medium.com](https://medium.com/%40kumawatabhijeet2002/p4-bugs-and-poc-part-1-0dab3517bbe9?source=post_page-----0842039eddf3---------------------------------------)

**Hi everyone! 👋**

I’m **Abhijeet Kumawat** — a passionate bug bounty hunter and security researcher. I love sharing my knowledge and experiences in bug bounty hunting and penetration testing. 🚀

Today, I’m thrilled to continue my **P4 bug series**, where I dive into low-severity vulnerabilities that often go unnoticed but can have significant consequences when exploited properly.

In this post, we’ll explore two commonly overlooked yet critical vulnerabilities: **Weak Registration Implementation** and **Weak Password Reset Implementation**. I’ll explain how these bugs work, show you how to reproduce them step-by-step, and provide **proof-of-concept (PoC)** techniques. Let’s get started!

Press enter or click to view image in full size

![]()

Created by Copilot

## 1️⃣ Weak Registration Implementation

## 🧐 What’s the Issue?

During the **user registration process**, websites often send a verification link to your email. If this link is sent over **HTTP** instead of **HTTPS**, it’s considered a vulnerability under certain conditions.

## ⚠️ Condition:

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0842039eddf3---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0842039eddf3---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--0842039eddf3---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--0842039eddf3---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--0842039eddf3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:96:96/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--0842039eddf3---------------------------------------)

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:128:128/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--0842039eddf3---------------------------------------)

[## Written by Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--0842039eddf3---------------------------------------)

[2.4K followers](https://medium.com/%40kumawatabhijeet2002/followers?source=post_page---post_author_info--0842039eddf3---------------------------------------)

·[33 following](https://medium.com/%40kumawatabhijeet2002/following?source=post_page---post_author_info--0842039eddf3---------------------------------------)

Radhe Radhe ✨ || Security Researcher || Bug Hunter || Web Application Penetration Tester || Ethical Hacker ||

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----0842039eddf3---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----0842039eddf3---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----0842039eddf3---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----0842039eddf3---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----0842039eddf3---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----0842039eddf3---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----0842039eddf3---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----0842039eddf3---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----0842039eddf3---------------------------------------)