---
title: P4 Bugs and POC | Part 7
url: https://infosecwriteups.com/p4-bugs-and-poc-part-7-a379f057ba96?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-09
fetch_date: 2025-10-06T20:08:32.182291
---

# P4 Bugs and POC | Part 7

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fa379f057ba96&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fp4-bugs-and-poc-part-7-a379f057ba96&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fp4-bugs-and-poc-part-7-a379f057ba96&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-a379f057ba96---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-a379f057ba96---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# P4 Bugs and POC | Part 7

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:64:64/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--a379f057ba96---------------------------------------)

[Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--a379f057ba96---------------------------------------)

4 min read

·

Jan 6, 2025

--

Share

**Hi everyone!**
👋 I’m **Abhijeet Kumawat** — a passionate **bug bounty hunter** and **security researcher** who loves exploring and sharing knowledge about web application vulnerabilities and penetration testing. Today, I’m thrilled to launch a blog series focusing on **P4 bugs** — those seemingly low-severity vulnerabilities that, when properly exploited, can have a notable impact.

In this series, we’ll dive deep into each bug type, explore how they work, and provide step-by-step **proof-of-concept (PoC)** demonstrations. Trust me, if you stay consistent and apply these techniques, you’re bound to find **valid P4 bugs** on real-world targets. Let’s kick things off with some exciting vulnerabilities! 🚀

Press enter or click to view image in full size

![]()

## 1. Exif Geolocation Vulnerability 🗺️

This bug may be labeled as **P4**, but its **impact can escalate to P3** depending on the exposure. Let’s unpack what it’s all about and how to exploit it effectively.

[## Received an Appreciation Letter from NASA 🏆

### How I Got an Appreciation Letter from NASA 🚀

medium.com](https://medium.com/%40kumawatabhijeet2002/received-an-appreciation-letter-from-nasa-927c3d1ae828?source=post_page-----a379f057ba96---------------------------------------)

## 🔍 What Is Exif Geolocation Vulnerability?

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a379f057ba96---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a379f057ba96---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--a379f057ba96---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--a379f057ba96---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--a379f057ba96---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:96:96/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--a379f057ba96---------------------------------------)

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:128:128/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--a379f057ba96---------------------------------------)

[## Written by Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--a379f057ba96---------------------------------------)

[2.4K followers](https://medium.com/%40kumawatabhijeet2002/followers?source=post_page---post_author_info--a379f057ba96---------------------------------------)

·[33 following](https://medium.com/%40kumawatabhijeet2002/following?source=post_page---post_author_info--a379f057ba96---------------------------------------)

Radhe Radhe ✨ || Security Researcher || Bug Hunter || Web Application Penetration Tester || Ethical Hacker ||

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----a379f057ba96---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----a379f057ba96---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----a379f057ba96---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----a379f057ba96---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----a379f057ba96---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----a379f057ba96---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----a379f057ba96---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----a379f057ba96---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----a379f057ba96---------------------------------------)