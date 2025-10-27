---
title: P4 Bugs and POC | Part-8
url: https://infosecwriteups.com/p4-bugs-and-poc-part-8-2b4ed878c53a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-09
fetch_date: 2025-10-06T20:08:36.786570
---

# P4 Bugs and POC | Part-8

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2b4ed878c53a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fp4-bugs-and-poc-part-8-2b4ed878c53a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fp4-bugs-and-poc-part-8-2b4ed878c53a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2b4ed878c53a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2b4ed878c53a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# P4 Bugs and POC | Part-8

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:64:64/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--2b4ed878c53a---------------------------------------)

[Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--2b4ed878c53a---------------------------------------)

4 min read

·

Jan 6, 2025

--

Share

**Hi everyone!** 👋
I’m **Abhijeet Kumawat**, a passionate **bug bounty hunter** and **security researcher** who loves exploring the fascinating world of vulnerabilities. I believe that even the smallest bugs — like P4 bugs — can be impactful when handled right. Through this blog series, I aim to share my experiences, insights, and hands-on Proof of Concepts (PoCs) to help you uncover these often-overlooked vulnerabilities.

Let’s kick things off with **two interesting P4 bugs** and learn how to find and exploit them effectively. If you follow these steps and test them on real-world targets, you’re bound to discover some amazing bugs! 😎

Press enter or click to view image in full size

![]()

## 🎯 Bug 1: HTML Email Injection

[## $150 💵 Easy HTML Injection Vulnerability

### Hello, everyone! 👋

medium.com](https://medium.com/%40kumawatabhijeet2002/150-easy-html-injection-vulnerability-5c176b5d07fa?source=post_page-----2b4ed878c53a---------------------------------------)

## 📝 What is it?

HTML Email Injection occurs when an application fails to sanitize user input properly and renders it as HTML in email content. This bug can lead to **phishing attacks** or the manipulation of official emails.

## 🔍 How to Find It

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2b4ed878c53a---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2b4ed878c53a---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--2b4ed878c53a---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--2b4ed878c53a---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--2b4ed878c53a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:96:96/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--2b4ed878c53a---------------------------------------)

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:128:128/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--2b4ed878c53a---------------------------------------)

[## Written by Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--2b4ed878c53a---------------------------------------)

[2.4K followers](https://medium.com/%40kumawatabhijeet2002/followers?source=post_page---post_author_info--2b4ed878c53a---------------------------------------)

·[33 following](https://medium.com/%40kumawatabhijeet2002/following?source=post_page---post_author_info--2b4ed878c53a---------------------------------------)

Radhe Radhe ✨ || Security Researcher || Bug Hunter || Web Application Penetration Tester || Ethical Hacker ||

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----2b4ed878c53a---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----2b4ed878c53a---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----2b4ed878c53a---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----2b4ed878c53a---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----2b4ed878c53a---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----2b4ed878c53a---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----2b4ed878c53a---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----2b4ed878c53a---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----2b4ed878c53a---------------------------------------)