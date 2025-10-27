---
title: Exposed Client Secret in JavaScript Resulted in Quick Bug Bounty $$$
url: https://infosecwriteups.com/exposed-client-secret-in-javascript-resulted-in-quick-bug-bounty-35a609be138d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-06-30
fetch_date: 2025-10-06T22:51:35.532329
---

# Exposed Client Secret in JavaScript Resulted in Quick Bug Bounty $$$

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F35a609be138d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fexposed-client-secret-in-javascript-resulted-in-quick-bug-bounty-35a609be138d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fexposed-client-secret-in-javascript-resulted-in-quick-bug-bounty-35a609be138d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-35a609be138d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-35a609be138d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Exposed Client Secret in JavaScript Resulted in Quick Bug Bounty $$$

[![Medusa](https://miro.medium.com/v2/resize:fill:64:64/1*f2U6mEKEJfzwHgsgrqFAXw.jpeg)](https://medusa0xf.medium.com/?source=post_page---byline--35a609be138d---------------------------------------)

[Medusa](https://medusa0xf.medium.com/?source=post_page---byline--35a609be138d---------------------------------------)

5 min read

·

Jun 28, 2025

--

1

Share

Press enter or click to view image in full size

![]()

Friend link: [https://infosecwriteups.com/exposed-client-secret-in-javascript-resulted-in-quick-bug-bounty-35a609be138d?sk=879a02f5277d7fecc32c591daa424ebe](/exposed-client-secret-in-javascript-resulted-in-quick-bug-bounty-35a609be138d?sk=879a02f5277d7fecc32c591daa424ebe)

## Introduction

Sometimes, a quick glance is all it takes to spot something valuable. While analyzing a public beta site, I reviewed one of its JavaScript files and noticed a small but critical mistake, a **hardcoded client secret** embedded in frontend code.

It didn’t take complex tools or deep exploitation. Just a simple string search and a few minutes of code reading. That one exposed secret led to a **bug bounty payout (aka quick $$$)**.

In this post, I’ll walk you through what I found, how I verified it, why it’s a serious security risk, and why clear and effective report writing can make all the difference in getting your bug bounty rewarded.

## Manual Recon in JavaScript

While inspecting the JavaScript bundle further, I found a block of environment-style configuration values directly defined inside the frontend code. Among those values was something that immediately stood out, a hardcoded `clientSecret`. Below is a simplified and redacted version of what the code looked like:

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--35a609be138d---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--35a609be138d---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--35a609be138d---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--35a609be138d---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--35a609be138d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Medusa](https://miro.medium.com/v2/resize:fill:96:96/1*f2U6mEKEJfzwHgsgrqFAXw.jpeg)](https://medusa0xf.medium.com/?source=post_page---post_author_info--35a609be138d---------------------------------------)

[![Medusa](https://miro.medium.com/v2/resize:fill:128:128/1*f2U6mEKEJfzwHgsgrqFAXw.jpeg)](https://medusa0xf.medium.com/?source=post_page---post_author_info--35a609be138d---------------------------------------)

[## Written by Medusa](https://medusa0xf.medium.com/?source=post_page---post_author_info--35a609be138d---------------------------------------)

[1.7K followers](https://medusa0xf.medium.com/followers?source=post_page---post_author_info--35a609be138d---------------------------------------)

·[39 following](https://medium.com/%40medusa0xf/following?source=post_page---post_author_info--35a609be138d---------------------------------------)

Security Researcher & Content Creator <https://medusa0xf.com/>

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----35a609be138d---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----35a609be138d---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----35a609be138d---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----35a609be138d---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----35a609be138d---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----35a609be138d---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----35a609be138d---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----35a609be138d---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----35a609be138d---------------------------------------)