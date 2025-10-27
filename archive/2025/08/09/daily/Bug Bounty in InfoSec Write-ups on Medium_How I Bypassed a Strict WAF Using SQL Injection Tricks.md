---
title: How I Bypassed a Strict WAF Using SQL Injection Tricks
url: https://infosecwriteups.com/how-i-bypassed-a-strict-waf-using-sql-injection-tricks-b0a500b712d8?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-09
fetch_date: 2025-10-07T00:18:32.080693
---

# How I Bypassed a Strict WAF Using SQL Injection Tricks

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb0a500b712d8&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-bypassed-a-strict-waf-using-sql-injection-tricks-b0a500b712d8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-bypassed-a-strict-waf-using-sql-injection-tricks-b0a500b712d8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b0a500b712d8---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b0a500b712d8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How I Bypassed a Strict WAF Using SQL Injection Tricks

## The Silent SQL Injection Cloudflare Almost Hid From Me

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:64:64/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---byline--b0a500b712d8---------------------------------------)

[Ibtissam hammadi](https://medium.com/%40ibtissamhammadi1?source=post_page---byline--b0a500b712d8---------------------------------------)

3 min read

·

Aug 8, 2025

--

Share

M**ost bug hunters would’ve missed this — here’s how I spotted a hidden SQLi behind Cloudflare’s strict WAF.**

Press enter or click to view image in full size

![Strict WAF Using SQL Injection Tricks]()

Photo by [Sunder Muthukumaran](https://unsplash.com/%40sunder_2k25?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

It started with a simple API endpoint: `/users/public?search=`. At first glance, it seemed harmless—just a search feature for public profiles. But something felt off. When a single quote (`'`) was entered, the results vanished. No errors, no warnings. Just silence.

**“No errors showed up — just silent SQL failures. Here’s why manual testing beats tools.”**

Automated scanners would’ve skipped this. No `500 Internal Server Error`, no `SQL syntax` warnings. But silence can be a vulnerability’s loudest scream.

### When a Missing Result Means Everything

The search parameter was supposed to filter users by name. Typing `deepak` returned profiles. But adding a quote (`'OR testing1337`) made the page empty.

**Burp Suite revealed the truth.** While the frontend showed nothing, the HTTP response hinted at a broken SQL query. Most testers rely on visible errors, but **hidden SQL failures** are where real exploits hide.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b0a500b712d8---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b0a500b712d8---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b0a500b712d8---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--b0a500b712d8---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--b0a500b712d8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:96:96/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--b0a500b712d8---------------------------------------)

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:128:128/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--b0a500b712d8---------------------------------------)

[## Written by Ibtissam hammadi](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--b0a500b712d8---------------------------------------)

[4.2K followers](https://medium.com/%40ibtissamhammadi1/followers?source=post_page---post_author_info--b0a500b712d8---------------------------------------)

·[102 following](https://medium.com/%40ibtissamhammadi1/following?source=post_page---post_author_info--b0a500b712d8---------------------------------------)

I am a Senior Data Scientist exploring Cybersecurity, Infosec, Programming, and AI technologies.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----b0a500b712d8---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----b0a500b712d8---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----b0a500b712d8---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----b0a500b712d8---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----b0a500b712d8---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----b0a500b712d8---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----b0a500b712d8---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----b0a500b712d8---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----b0a500b712d8---------------------------------------)