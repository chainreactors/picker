---
title: SQL injection in largest Electricity Board of Sri Lanka
url: https://infosecwriteups.com/sql-injection-in-largest-electricity-board-of-sri-lanka-1a55c12104bd?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-25
fetch_date: 2025-10-06T20:08:33.976271
---

# SQL injection in largest Electricity Board of Sri Lanka

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F1a55c12104bd&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-in-largest-electricity-board-of-sri-lanka-1a55c12104bd&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-in-largest-electricity-board-of-sri-lanka-1a55c12104bd&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-1a55c12104bd---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-1a55c12104bd---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **SQL injection in largest Electricity Board of Sri Lanka**

## In this article I’ll describe how I found SQL injection vulnerabilities by bypassing WAF with origin IP, IDOR and information disclosure bugs.

[![coffinxp](https://miro.medium.com/v2/resize:fill:64:64/1*PjsjomDRyS2MomLQcc4nOw.png)](https://coffinxp.medium.com/?source=post_page---byline--1a55c12104bd---------------------------------------)

[coffinxp](https://coffinxp.medium.com/?source=post_page---byline--1a55c12104bd---------------------------------------)

8 min read

·

Jan 24, 2025

--

17

Share

Press enter or click to view image in full size

![]()

## Introduction

SQL Injection is a technique used by attackers to take advantage of vulnerabilities in a websites database. By inserting harmful SQL code into inputs such as forms or search fields they can reach, modify or even erase sensitive information. This vulnerability may result in unauthorized entry, data compromise, or complete server control categorizing SQLi as one of the most significant and prevalent cybersecurity threats.

### Story

One day a subscriber reached out and asked if I could test for SQL injection vulnerabilities on their national Electricity Board website which was protected by Cloudflare WAF. As many of you know I often share techniques and methods for identifying SQL injection vulnerabilities so I decided to take on the challenge. So let’s begin with how I discovered this!

## How i find this vulnerability

I visited the website and used the Wappalyzer extension to check the site technology stack. The extension revealed that the site was built…

--

--

17

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1a55c12104bd---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1a55c12104bd---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--1a55c12104bd---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--1a55c12104bd---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--1a55c12104bd---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![coffinxp](https://miro.medium.com/v2/resize:fill:96:96/1*PjsjomDRyS2MomLQcc4nOw.png)](https://coffinxp.medium.com/?source=post_page---post_author_info--1a55c12104bd---------------------------------------)

[![coffinxp](https://miro.medium.com/v2/resize:fill:128:128/1*PjsjomDRyS2MomLQcc4nOw.png)](https://coffinxp.medium.com/?source=post_page---post_author_info--1a55c12104bd---------------------------------------)

[## Written by coffinxp](https://coffinxp.medium.com/?source=post_page---post_author_info--1a55c12104bd---------------------------------------)

[6.3K followers](https://coffinxp.medium.com/followers?source=post_page---post_author_info--1a55c12104bd---------------------------------------)

·[0 following](https://medium.com/%40coffinxp/following?source=post_page---post_author_info--1a55c12104bd---------------------------------------)

Helping organizations stay secure through Bug Hunting, OSINT and Security Research | Sharing knowledge as a Content Creator

## Responses (17)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----1a55c12104bd---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----1a55c12104bd---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----1a55c12104bd---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----1a55c12104bd---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----1a55c12104bd---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----1a55c12104bd---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----1a55c12104bd---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----1a55c12104bd---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----1a55c12104bd---------------------------------------)