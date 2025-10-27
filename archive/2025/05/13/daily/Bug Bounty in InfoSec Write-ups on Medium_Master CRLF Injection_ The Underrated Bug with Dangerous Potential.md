---
title: Master CRLF Injection: The Underrated Bug with Dangerous Potential
url: https://infosecwriteups.com/master-crlf-injection-the-underrated-bug-with-dangerous-potential-33bb0d62e031?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-05-13
fetch_date: 2025-10-06T22:25:25.779169
---

# Master CRLF Injection: The Underrated Bug with Dangerous Potential

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F33bb0d62e031&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmaster-crlf-injection-the-underrated-bug-with-dangerous-potential-33bb0d62e031&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmaster-crlf-injection-the-underrated-bug-with-dangerous-potential-33bb0d62e031&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-33bb0d62e031---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-33bb0d62e031---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

Featured

# Master CRLF Injection: The Underrated Bug with Dangerous Potential

## Learn how attackers exploit CRLF Injection to manipulate HTTP responses, hijack headers and unlock hidden vulnerabilities in modern web applications

[![coffinxp](https://miro.medium.com/v2/resize:fill:64:64/1*PjsjomDRyS2MomLQcc4nOw.png)](https://coffinxp.medium.com/?source=post_page---byline--33bb0d62e031---------------------------------------)

[coffinxp](https://coffinxp.medium.com/?source=post_page---byline--33bb0d62e031---------------------------------------)

8 min read

·

May 12, 2025

--

3

Share

Press enter or click to view image in full size

![]()

## Introduction

In web security some vulnerabilities don’t get as much attention but can still cause major problems. One of these is **CRLF Injection**. Although it’s not as well-known as SQL Injection or Cross-Site Scripting, CRLF Injection can lead to serious issues like HTTP response splitting, web cache poisoning and even XSS attacks all of which can put a website at risk

## What is CRLF Injection?

CRLF stands for Carriage Return (CR, %0d) and Line Feed (LF, %0a), which are special characters used to denote the end of a line in HTTP headers. CRLF Injection occurs when an attacker is able to inject these characters into HTTP headers or responses, manipulating how the server or client interprets the response.

By injecting CRLF sequences, an attacker can prematurely terminate headers and inject arbitrary headers or even body content leading to various attacks such as:

* HTTP Response Splitting
* Web Cache Poisoning

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--33bb0d62e031---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--33bb0d62e031---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--33bb0d62e031---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--33bb0d62e031---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--33bb0d62e031---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![coffinxp](https://miro.medium.com/v2/resize:fill:96:96/1*PjsjomDRyS2MomLQcc4nOw.png)](https://coffinxp.medium.com/?source=post_page---post_author_info--33bb0d62e031---------------------------------------)

[![coffinxp](https://miro.medium.com/v2/resize:fill:128:128/1*PjsjomDRyS2MomLQcc4nOw.png)](https://coffinxp.medium.com/?source=post_page---post_author_info--33bb0d62e031---------------------------------------)

[## Written by coffinxp](https://coffinxp.medium.com/?source=post_page---post_author_info--33bb0d62e031---------------------------------------)

[6.3K followers](https://coffinxp.medium.com/followers?source=post_page---post_author_info--33bb0d62e031---------------------------------------)

·[0 following](https://medium.com/%40coffinxp/following?source=post_page---post_author_info--33bb0d62e031---------------------------------------)

Helping organizations stay secure through Bug Hunting, OSINT and Security Research | Sharing knowledge as a Content Creator

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----33bb0d62e031---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----33bb0d62e031---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----33bb0d62e031---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----33bb0d62e031---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----33bb0d62e031---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----33bb0d62e031---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----33bb0d62e031---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----33bb0d62e031---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----33bb0d62e031---------------------------------------)