---
title: A Deep Dive into Improper Authentication
url: https://infosecwriteups.com/a-deep-dive-into-improper-authentication-a68a92929f33?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-13
fetch_date: 2025-10-07T00:16:30.856875
---

# A Deep Dive into Improper Authentication

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fa68a92929f33&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fa-deep-dive-into-improper-authentication-a68a92929f33&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fa-deep-dive-into-improper-authentication-a68a92929f33&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-a68a92929f33---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-a68a92929f33---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# A Deep Dive into Improper Authentication

## Exploring How to Detect and Exploit Reusable OTP Issues, with a Case Study from HackerOne Report

[![Monika sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---byline--a68a92929f33---------------------------------------)

[Monika sharma](https://medium.com/%40commanak46?source=post_page---byline--a68a92929f33---------------------------------------)

7 min read

·

Aug 12, 2025

--

Share

Press enter or click to view image in full size

![]()

## Introduction

In the world of cybersecurity, two-factor authentication (2FA) is a cornerstone of protecting user accounts from unauthorized access. It adds an extra layer of security beyond just a username and password. However, like any system, 2FA can have flaws. One such vulnerability is “Improper Authentication” due to reusable One-Time Passwords (OTPs). This issue occurs when an OTP, meant to be single-use and time-limited, can be reused even after it should have expired.

This article will first explain what reusable 2FA OTP vulnerabilities are, why they happen, and most importantly, how you can find them in web applications. We’ll cover step-by-step methods for detection, tools to use, and best practices for ethical testing. Then, we’ll dive into a specific real-world example: HackerOne report #2529780, submitted by researcher xklepxn in June 2024, which highlighted this issue in HackerOne’s own platform. By the end, you’ll have a comprehensive understanding of the vulnerability, its impacts, and how to mitigate it.

## What is 2FA and OTP?

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a68a92929f33---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a68a92929f33---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--a68a92929f33---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--a68a92929f33---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--a68a92929f33---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Monika sharma](https://miro.medium.com/v2/resize:fill:96:96/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--a68a92929f33---------------------------------------)

[![Monika sharma](https://miro.medium.com/v2/resize:fill:128:128/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--a68a92929f33---------------------------------------)

[## Written by Monika sharma](https://medium.com/%40commanak46?source=post_page---post_author_info--a68a92929f33---------------------------------------)

[2K followers](https://medium.com/%40commanak46/followers?source=post_page---post_author_info--a68a92929f33---------------------------------------)

·[7 following](https://medium.com/%40commanak46/following?source=post_page---post_author_info--a68a92929f33---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----a68a92929f33---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----a68a92929f33---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----a68a92929f33---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----a68a92929f33---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----a68a92929f33---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----a68a92929f33---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----a68a92929f33---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----a68a92929f33---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----a68a92929f33---------------------------------------)