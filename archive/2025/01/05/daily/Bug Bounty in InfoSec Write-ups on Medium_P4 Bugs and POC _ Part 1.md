---
title: P4 Bugs and POC | Part 1
url: https://infosecwriteups.com/p4-bugs-and-poc-part-1-0dab3517bbe9?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-05
fetch_date: 2025-10-06T20:07:42.166943
---

# P4 Bugs and POC | Part 1

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F0dab3517bbe9&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fp4-bugs-and-poc-part-1-0dab3517bbe9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fp4-bugs-and-poc-part-1-0dab3517bbe9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-0dab3517bbe9---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-0dab3517bbe9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# P4 Bugs and POC | Part 1

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:64:64/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--0dab3517bbe9---------------------------------------)

[Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--0dab3517bbe9---------------------------------------)

5 min read

·

Jan 3, 2025

--

Share

## P4 Bugs and POC | Part 1: Broken Link Hijacking

👋 **Hi everyone!**
I’m **Abhijeet Kumawat**, a passionate **bug bounty hunter** and **security researcher**. I thrive on exploring vulnerabilities and sharing my insights with the community. Today, I’m thrilled to kick off a new blog series focused on **P4 bugs** — those often-overlooked low-severity vulnerabilities that can still pack a punch when properly exploited.

In this series, I’ll break down various **P4 vulnerabilities**, explaining how they work and providing detailed **proof-of-concept (PoC)** demonstrations to help you sharpen your skills. By following along and applying these techniques, you’re bound to uncover **valid P4 bugs** on real-world targets. 🕵️‍♂️

For the first part, let’s dive into **Broken Link Hijacking (BLH)** — a simple yet impactful vulnerability that’s often hiding in plain sight.

Press enter or click to view image in full size

![]()

## 🚨 What Is Broken Link Hijacking?

In simple terms, **Broken Link Hijacking** occurs when an organization’s website points to an **external resource** (like a social media account, JavaScript file, or image) that no longer exists. If this external resource is up for grabs — such as an **expired domain** or an available **social media handle** — an attacker can claim it and exploit the broken link.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0dab3517bbe9---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0dab3517bbe9---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--0dab3517bbe9---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--0dab3517bbe9---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--0dab3517bbe9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:96:96/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--0dab3517bbe9---------------------------------------)

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:128:128/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--0dab3517bbe9---------------------------------------)

[## Written by Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--0dab3517bbe9---------------------------------------)

[2.4K followers](https://medium.com/%40kumawatabhijeet2002/followers?source=post_page---post_author_info--0dab3517bbe9---------------------------------------)

·[33 following](https://medium.com/%40kumawatabhijeet2002/following?source=post_page---post_author_info--0dab3517bbe9---------------------------------------)

Radhe Radhe ✨ || Security Researcher || Bug Hunter || Web Application Penetration Tester || Ethical Hacker ||

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----0dab3517bbe9---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----0dab3517bbe9---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----0dab3517bbe9---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----0dab3517bbe9---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----0dab3517bbe9---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----0dab3517bbe9---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----0dab3517bbe9---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----0dab3517bbe9---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----0dab3517bbe9---------------------------------------)