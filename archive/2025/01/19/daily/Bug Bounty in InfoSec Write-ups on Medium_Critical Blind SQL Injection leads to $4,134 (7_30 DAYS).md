---
title: Critical Blind SQL Injection leads to 
$4,134 (7/30 DAYS)
url: https://infosecwriteups.com/critical-blind-sql-injection-leads-to-4-134-7-30-days-d8918ff3d2d0?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-19
fetch_date: 2025-10-06T20:08:24.039138
---

# Critical Blind SQL Injection leads to 
$4,134 (7/30 DAYS)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd8918ff3d2d0&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcritical-blind-sql-injection-leads-to-4-134-7-30-days-d8918ff3d2d0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcritical-blind-sql-injection-leads-to-4-134-7-30-days-d8918ff3d2d0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d8918ff3d2d0---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d8918ff3d2d0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Critical Blind SQL Injection leads to $4,134 (7/30 DAYS)

[![0day stories](https://miro.medium.com/v2/resize:fill:64:64/1*I-E0Gt_pLw23iS_YcGunQQ.jpeg)](https://medium.com/%40zerodaystories?source=post_page---byline--d8918ff3d2d0---------------------------------------)

[0day stories](https://medium.com/%40zerodaystories?source=post_page---byline--d8918ff3d2d0---------------------------------------)

4 min read

·

Jan 15, 2025

--

1

Share

**Understanding the Risk:** How a Blind SQL Injection Was Discovered in inDrive

## **Hi Bug Bounty Hunters!!!**

I’m a security researcher, and I’ve taken on the challenge of explaining one bug bounty report every day for the next **30 days — 30 reports!**

The goal is to make these reports easy to understand, share the cool stuff I learn along the way, and inspire others to dive into the world of bug bounties too. Whether you’re a pro or just curious, I hope you’ll find something interesting in this series.

I’ll also share useful tips at the end of each report to help you level up your bug-hunting game. Let’s get started!

Today’s Report: **Blind SQL** Injection Vulnerability in **inDrive API**

## **Introduction**

Security researcher identified a significant security flaw in inDrive’s API. The vulnerability was a blind SQL injection, which allowed attackers to manipulate database queries and extract sensitive information. This report highlights how the vulnerability was discovered, how it could be exploited, and why it was a serious security risk.

Press enter or click to view image in full size

![]()

## **What Is Blind SQL Injection?**

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d8918ff3d2d0---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d8918ff3d2d0---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--d8918ff3d2d0---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--d8918ff3d2d0---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--d8918ff3d2d0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![0day stories](https://miro.medium.com/v2/resize:fill:96:96/1*I-E0Gt_pLw23iS_YcGunQQ.jpeg)](https://medium.com/%40zerodaystories?source=post_page---post_author_info--d8918ff3d2d0---------------------------------------)

[![0day stories](https://miro.medium.com/v2/resize:fill:128:128/1*I-E0Gt_pLw23iS_YcGunQQ.jpeg)](https://medium.com/%40zerodaystories?source=post_page---post_author_info--d8918ff3d2d0---------------------------------------)

[## Written by 0day stories](https://medium.com/%40zerodaystories?source=post_page---post_author_info--d8918ff3d2d0---------------------------------------)

[759 followers](https://medium.com/%40zerodaystories/followers?source=post_page---post_author_info--d8918ff3d2d0---------------------------------------)

·[31 following](https://medium.com/%40zerodaystories/following?source=post_page---post_author_info--d8918ff3d2d0---------------------------------------)

Weekly insights into bug bounty reports, discoveries, and tips. Stay curious, stay secure!

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----d8918ff3d2d0---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----d8918ff3d2d0---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----d8918ff3d2d0---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----d8918ff3d2d0---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----d8918ff3d2d0---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----d8918ff3d2d0---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----d8918ff3d2d0---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----d8918ff3d2d0---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----d8918ff3d2d0---------------------------------------)