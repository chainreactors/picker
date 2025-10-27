---
title: How I Earned a Hall of Fame Spot at UNESCO by Bypassing 403 Forbidden
url: https://infosecwriteups.com/how-i-earned-a-hall-of-fame-spot-at-unesco-by-bypassing-403-forbidden-fdb2185383f7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-02-20
fetch_date: 2025-10-06T20:34:37.916003
---

# How I Earned a Hall of Fame Spot at UNESCO by Bypassing 403 Forbidden

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ffdb2185383f7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-earned-a-hall-of-fame-spot-at-unesco-by-bypassing-403-forbidden-fdb2185383f7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-earned-a-hall-of-fame-spot-at-unesco-by-bypassing-403-forbidden-fdb2185383f7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-fdb2185383f7---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-fdb2185383f7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How I Earned a Hall of Fame Spot at UNESCO by Bypassing 403 Forbidden

[![Krunal Patel](https://miro.medium.com/v2/resize:fill:64:64/1*cB1XmLM3ppI-3Naqqm-akA.jpeg)](https://medium.com/%40KpCyberInfo?source=post_page---byline--fdb2185383f7---------------------------------------)

[Krunal Patel](https://medium.com/%40KpCyberInfo?source=post_page---byline--fdb2185383f7---------------------------------------)

4 min read

·

Feb 19, 2025

--

1

Share

**Hello, amazing people and bug bounty hunters!** 👋

This is **Krunal Patel**, and I hope you all are doing great! ❤️

In this write-up, I want to share how I achieved my **first Hall of Fame at UNESCO** and how I was able to bypass **403 Forbidden** using a simple HTTP method trick. So, let’s dive in! 🚀

## 🔥 Understanding 403 Forbidden

Press enter or click to view image in full size

![]()

Before we get into the fun part, let’s understand what **403 Forbidden** really is.

A **403 status code** is returned when an unauthorized user tries to access a restricted page. The server blocks access and responds with a **403 Forbidden error**, preventing users from viewing or interacting with that resource.

## ❓ What is a 403 Forbidden Bypass?

Bypassing **403 Forbidden** means finding a way to access restricted resources **even when the server tries to block us**. Attackers may exploit **misconfiguration in access controls** to gain access to sensitive endpoints.

## 🕵️‍♂️ Recon: Choosing the Target

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--fdb2185383f7---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--fdb2185383f7---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--fdb2185383f7---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--fdb2185383f7---------------------------------------)

·[Last published just now](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--fdb2185383f7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Krunal Patel](https://miro.medium.com/v2/resize:fill:96:96/1*cB1XmLM3ppI-3Naqqm-akA.jpeg)](https://medium.com/%40KpCyberInfo?source=post_page---post_author_info--fdb2185383f7---------------------------------------)

[![Krunal Patel](https://miro.medium.com/v2/resize:fill:128:128/1*cB1XmLM3ppI-3Naqqm-akA.jpeg)](https://medium.com/%40KpCyberInfo?source=post_page---post_author_info--fdb2185383f7---------------------------------------)

[## Written by Krunal Patel](https://medium.com/%40KpCyberInfo?source=post_page---post_author_info--fdb2185383f7---------------------------------------)

[71 followers](https://medium.com/%40KpCyberInfo/followers?source=post_page---post_author_info--fdb2185383f7---------------------------------------)

·[7 following](https://medium.com/%40KpCyberInfo/following?source=post_page---post_author_info--fdb2185383f7---------------------------------------)

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----fdb2185383f7---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----fdb2185383f7---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----fdb2185383f7---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----fdb2185383f7---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----fdb2185383f7---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----fdb2185383f7---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----fdb2185383f7---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----fdb2185383f7---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----fdb2185383f7---------------------------------------)