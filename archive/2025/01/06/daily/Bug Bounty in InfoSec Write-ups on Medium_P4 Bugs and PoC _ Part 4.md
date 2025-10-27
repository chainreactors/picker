---
title: P4 Bugs and PoC | Part 4
url: https://infosecwriteups.com/p4-bugs-and-poc-part-4-c65113b489b0?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-06
fetch_date: 2025-10-06T20:07:51.410030
---

# P4 Bugs and PoC | Part 4

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc65113b489b0&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fp4-bugs-and-poc-part-4-c65113b489b0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fp4-bugs-and-poc-part-4-c65113b489b0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c65113b489b0---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c65113b489b0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# P4 Bugs and POC | Part 4

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:64:64/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--c65113b489b0---------------------------------------)

[Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--c65113b489b0---------------------------------------)

4 min read

·

Jan 4, 2025

--

1

Share

**Hi everyone! 👋**
I’m **Abhijeet Kumawat** — a passionate bug bounty hunter and security researcher. I enjoy sharing my knowledge and experiences in bug bounty hunting and penetration testing. Today, I’m thrilled to continue my blog series focusing on **P4 bugs** — those low-severity vulnerabilities that are often overlooked but can yield significant results when properly exploited. 🚀

[## How I Discovered SSTI Vulnerability in Just 5 Minutes 🚀| 💰$300 Bounty

### Hello, everyone! 👋

medium.com](https://medium.com/%40kumawatabhijeet2002/how-i-discovered-ssti-vulnerability-in-just-5-minutes-f7ac31f3f6b0?source=post_page-----c65113b489b0---------------------------------------)

In this series, I’ll break down various vulnerability types, explain their working mechanisms, and provide detailed **proof-of-concept (PoC)** demonstrations. If you follow these techniques diligently and apply them to real-world targets, I’m confident you’ll uncover valid P4 bugs. 🕵️‍♂️

Press enter or click to view image in full size

![]()

Let’s dive into two exciting vulnerabilities:

## 1️⃣ Delete Account Without Password

This vulnerability is as simple as it sounds. Imagine you want to delete your account on a website, and it asks for your account password for verification. However, on some websites, when you click the “Delete Account” button, your account gets deleted **without any password**…

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c65113b489b0---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c65113b489b0---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--c65113b489b0---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--c65113b489b0---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--c65113b489b0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:96:96/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--c65113b489b0---------------------------------------)

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:128:128/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--c65113b489b0---------------------------------------)

[## Written by Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--c65113b489b0---------------------------------------)

[2.4K followers](https://medium.com/%40kumawatabhijeet2002/followers?source=post_page---post_author_info--c65113b489b0---------------------------------------)

·[33 following](https://medium.com/%40kumawatabhijeet2002/following?source=post_page---post_author_info--c65113b489b0---------------------------------------)

Radhe Radhe ✨ || Security Researcher || Bug Hunter || Web Application Penetration Tester || Ethical Hacker ||

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----c65113b489b0---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----c65113b489b0---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----c65113b489b0---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----c65113b489b0---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----c65113b489b0---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----c65113b489b0---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----c65113b489b0---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----c65113b489b0---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----c65113b489b0---------------------------------------)