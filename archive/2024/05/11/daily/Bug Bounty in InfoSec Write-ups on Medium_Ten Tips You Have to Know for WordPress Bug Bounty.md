---
title: Ten Tips You Have to Know for WordPress Bug Bounty
url: https://infosecwriteups.com/ten-tips-you-have-to-know-for-wordpress-bug-bounty-b2b070f07add?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-05-11
fetch_date: 2025-10-06T17:16:54.255193
---

# Ten Tips You Have to Know for WordPress Bug Bounty

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb2b070f07add&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ften-tips-you-have-to-know-for-wordpress-bug-bounty-b2b070f07add&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ften-tips-you-have-to-know-for-wordpress-bug-bounty-b2b070f07add&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b2b070f07add---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b2b070f07add---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Ten Tips You Have to Know for WordPress Bug Bounty

## From Bounty Platform to Hunting Tricks

[![Peng Zhou](https://miro.medium.com/v2/resize:fill:64:64/1*jxEEMOb5jrxEADVunLJYBw.jpeg)](https://medium.com/%40zpbrent?source=post_page---byline--b2b070f07add---------------------------------------)

[Peng Zhou](https://medium.com/%40zpbrent?source=post_page---byline--b2b070f07add---------------------------------------)

7 min read

·

Apr 14, 2024

--

Share

Press enter or click to view image in full size

![]()

WordPress is the most popular Content Management System (CMS) deployed on today’s Web. It is reported by [W3Techs](https://w3techs.com/technologies/details/cm-wordpress) to share more than 60% of markets of CMS and exceed 40% of all websites. Its success seems mainly due to the well-built WordPress ecosystem that involves millions of third-party plugins and themes. But on the evil side, the authors of these add-ons have very different capabilities for secure coding, leaving a large volume of bugs in the WordPress ecosystem. To this end, hunting bugs across the WordPress codebase is becoming a fad. Many bug bounty platforms have been set to encourage more hunters' participation. In this write-up, I will list ten useful tips to help you get an effective and efficient WordPress bug bounty journey.

### 1, choose your WordPress bug bounty platform wisely.

Till 2024, we can find four bug bounty platforms that publicly accept and reward WordPress vulnerability reports: [Patchstack](https://patchstack.com/articles/bug-bounty-guidelines-rules/), [WordFence](https://www.wordfence.com/threat-intel/bug-bounty-program/), [WPScan](https://wpscan.com/), and [HackerOne](https://hackerone.com/wordpress). These platforms have very different guidelines and rules for rewarding, and thus you can take advantage of this difference to gain more bounties :-)

> [**Patchstack**](https://patchstack.com/articles/bug-bounty-guidelines-rules/): CVE for all the validated reports, and bug bounty via monthly compitetion…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b2b070f07add---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b2b070f07add---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b2b070f07add---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--b2b070f07add---------------------------------------)

·[Last published 2 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--b2b070f07add---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Peng Zhou](https://miro.medium.com/v2/resize:fill:96:96/1*jxEEMOb5jrxEADVunLJYBw.jpeg)](https://medium.com/%40zpbrent?source=post_page---post_author_info--b2b070f07add---------------------------------------)

[![Peng Zhou](https://miro.medium.com/v2/resize:fill:128:128/1*jxEEMOb5jrxEADVunLJYBw.jpeg)](https://medium.com/%40zpbrent?source=post_page---post_author_info--b2b070f07add---------------------------------------)

[## Written by Peng Zhou](https://medium.com/%40zpbrent?source=post_page---post_author_info--b2b070f07add---------------------------------------)

[185 followers](https://medium.com/%40zpbrent/followers?source=post_page---post_author_info--b2b070f07add---------------------------------------)

·[81 following](https://medium.com/%40zpbrent/following?source=post_page---post_author_info--b2b070f07add---------------------------------------)

Half Writer Half Hunter

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----b2b070f07add---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----b2b070f07add---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----b2b070f07add---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----b2b070f07add---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----b2b070f07add---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----b2b070f07add---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----b2b070f07add---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----b2b070f07add---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----b2b070f07add---------------------------------------)