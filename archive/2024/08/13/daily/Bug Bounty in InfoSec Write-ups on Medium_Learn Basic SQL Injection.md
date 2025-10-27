---
title: Learn Basic SQL Injection
url: https://infosecwriteups.com/sql-injection-part-1%EF%B8%8F%E2%83%A3-eead93a673a2?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-08-13
fetch_date: 2025-10-06T18:04:35.610481
---

# Learn Basic SQL Injection

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Feead93a673a2&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-part-1%25EF%25B8%258F%25E2%2583%25A3-eead93a673a2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-part-1%25EF%25B8%258F%25E2%2583%25A3-eead93a673a2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-eead93a673a2---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-eead93a673a2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Learn Basic SQL Injection

## Comprehensive guide on manually detecting Classic SQL injection vulnerabilities.

[![Neetrox](https://miro.medium.com/v2/resize:fill:64:64/1*MQkphkThmCsQrJCIK97LFA.png)](https://aloulouomarr.medium.com/?source=post_page---byline--eead93a673a2---------------------------------------)

[Neetrox](https://aloulouomarr.medium.com/?source=post_page---byline--eead93a673a2---------------------------------------)

4 min read

·

Aug 5, 2024

--

1

Share

Press enter or click to view image in full size

![]()

## Introduction

**SQL Injection (SQLi)** represents a severe web security vulnerability that enables attackers to manipulate an application’s database queries. Through these manipulations, attackers can access, alter, or delete data, perform administrative tasks, or even gain full control over the database server.

This vulnerabilities arise primarily due to poor handling of user input by applications. When developers insert user-supplied data directly into SQL queries without proper sanitization or parameterization, it creates opportunities for exploitation.

A successful SQL injection attack can lead to unauthorized access to sensitive data, including:

* Passwords
* Credit card details
* Personal user informations

In some cases, attackers can install a persistent backdoor into an organization’s systems, also can escalate a SQL injection attack to compromise the underlying server or other back-end infrastructure. It can also enable them to perform denial-of-service attacks.

## Types of SQL Injection:

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--eead93a673a2---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--eead93a673a2---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--eead93a673a2---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--eead93a673a2---------------------------------------)

·[Last published 3 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--eead93a673a2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Neetrox](https://miro.medium.com/v2/resize:fill:96:96/1*MQkphkThmCsQrJCIK97LFA.png)](https://aloulouomarr.medium.com/?source=post_page---post_author_info--eead93a673a2---------------------------------------)

[![Neetrox](https://miro.medium.com/v2/resize:fill:128:128/1*MQkphkThmCsQrJCIK97LFA.png)](https://aloulouomarr.medium.com/?source=post_page---post_author_info--eead93a673a2---------------------------------------)

[## Written by Neetrox](https://aloulouomarr.medium.com/?source=post_page---post_author_info--eead93a673a2---------------------------------------)

[206 followers](https://aloulouomarr.medium.com/followers?source=post_page---post_author_info--eead93a673a2---------------------------------------)

·[45 following](https://medium.com/%40aloulouomarr/following?source=post_page---post_author_info--eead93a673a2---------------------------------------)

Cybersecurity Enthusiast | Security+ | CySA+ | THM SAL1

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----eead93a673a2---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----eead93a673a2---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----eead93a673a2---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----eead93a673a2---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----eead93a673a2---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----eead93a673a2---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----eead93a673a2---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----eead93a673a2---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----eead93a673a2---------------------------------------)