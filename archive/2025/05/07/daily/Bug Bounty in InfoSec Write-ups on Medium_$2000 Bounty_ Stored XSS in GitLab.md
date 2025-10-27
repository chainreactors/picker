---
title: $2000 Bounty: Stored XSS in GitLab
url: https://infosecwriteups.com/2000-bounty-stored-xss-in-gitlab-c71b2d7a3c21?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-05-07
fetch_date: 2025-10-06T22:25:37.029443
---

# $2000 Bounty: Stored XSS in GitLab

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc71b2d7a3c21&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F2000-bounty-stored-xss-in-gitlab-c71b2d7a3c21&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F2000-bounty-stored-xss-in-gitlab-c71b2d7a3c21&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c71b2d7a3c21---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c71b2d7a3c21---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# $2000 Bounty: Stored XSS in GitLab

## Exploiting a stored XSS in GitLab’s repository viewer for $2000

[![Monika sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---byline--c71b2d7a3c21---------------------------------------)

[Monika sharma](https://medium.com/%40commanak46?source=post_page---byline--c71b2d7a3c21---------------------------------------)

4 min read

·

May 6, 2025

--

Share

Press enter or click to view image in full size

![]()

### Introduction

Cross-Site Scripting (XSS) continues to be one of the most impactful web vulnerabilities even in large and mature platforms like GitLab. In this write-up we’ll explore an interesting stored XSS vulnerability discovered by security researcher kannthu in GitLab’s repository file viewer earning a $2000 bounty for their finding under report ID #1072868.

We’ll break down how the vulnerability was found, the root cause, the proof of concept (PoC), and why it posed a real security risk.

### What was the vulnerability?

GitLab uses an embedded Swagger UI to display OpenAPI specifications within repository files. Unfortunately the version of Swagger UI in use was outdated and relied on an old version of DOMPurify (a popular JavaScript sanitizer library).

This older DOMPurify version didn’t properly sanitize all malicious HTML attributes leaving the application vulnerable to XSS.

This meant an attacker could upload a malicious OpenAPI file (like openapi.yaml) containing crafted payloads. When a user viewed this file via GitLab’s interface the payload would be stored and executed leading to a stored XSS.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c71b2d7a3c21---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c71b2d7a3c21---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--c71b2d7a3c21---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--c71b2d7a3c21---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--c71b2d7a3c21---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Monika sharma](https://miro.medium.com/v2/resize:fill:96:96/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--c71b2d7a3c21---------------------------------------)

[![Monika sharma](https://miro.medium.com/v2/resize:fill:128:128/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--c71b2d7a3c21---------------------------------------)

[## Written by Monika sharma](https://medium.com/%40commanak46?source=post_page---post_author_info--c71b2d7a3c21---------------------------------------)

[2K followers](https://medium.com/%40commanak46/followers?source=post_page---post_author_info--c71b2d7a3c21---------------------------------------)

·[7 following](https://medium.com/%40commanak46/following?source=post_page---post_author_info--c71b2d7a3c21---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----c71b2d7a3c21---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----c71b2d7a3c21---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----c71b2d7a3c21---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----c71b2d7a3c21---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----c71b2d7a3c21---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----c71b2d7a3c21---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----c71b2d7a3c21---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----c71b2d7a3c21---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----c71b2d7a3c21---------------------------------------)