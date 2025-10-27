---
title: A Deep Dive into a Potential Privilege Escalation Issue
url: https://infosecwriteups.com/a-deep-dive-into-a-potential-privilege-escalation-issue-313a6040d458?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-11
fetch_date: 2025-10-07T00:16:57.010900
---

# A Deep Dive into a Potential Privilege Escalation Issue

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F313a6040d458&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fa-deep-dive-into-a-potential-privilege-escalation-issue-313a6040d458&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fa-deep-dive-into-a-potential-privilege-escalation-issue-313a6040d458&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-313a6040d458---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-313a6040d458---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# A Deep Dive into a Potential Privilege Escalation Issue

## A Deep Dive into the Security Report and How to Identify Similar Issues

[![Monika sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---byline--313a6040d458---------------------------------------)

[Monika sharma](https://medium.com/%40commanak46?source=post_page---byline--313a6040d458---------------------------------------)

7 min read

·

Aug 10, 2025

--

1

Share

Press enter or click to view image in full size

![]()

## Introduction

A security researcher named ngalog submitted a report to Shopify’s bug bounty program on HackerOne, highlighting a potential privilege escalation vulnerability involving Shopify’s Multipass feature. This article explains what privilege escalation is, why it matters, how the Multipass vulnerability was identified, and how you can detect similar issues in web applications. Written in simple English, this informative guide breaks down the technical details of the report, its implications, and practical steps for identifying such vulnerabilities.

## What is Privilege Escalation?

Privilege escalation is a type of security vulnerability where an attacker or user gains access to permissions or data beyond what they are authorized to have. For example, a regular employee with limited access might exploit a flaw to gain admin-level control, allowing them to view sensitive customer information or modify critical settings.

There are two main types of privilege escalation:

* **Vertical Privilege Escalation**: A user gains higher-level access, like moving from a regular user to an admin.

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--313a6040d458---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--313a6040d458---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--313a6040d458---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--313a6040d458---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--313a6040d458---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Monika sharma](https://miro.medium.com/v2/resize:fill:96:96/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--313a6040d458---------------------------------------)

[![Monika sharma](https://miro.medium.com/v2/resize:fill:128:128/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--313a6040d458---------------------------------------)

[## Written by Monika sharma](https://medium.com/%40commanak46?source=post_page---post_author_info--313a6040d458---------------------------------------)

[2K followers](https://medium.com/%40commanak46/followers?source=post_page---post_author_info--313a6040d458---------------------------------------)

·[7 following](https://medium.com/%40commanak46/following?source=post_page---post_author_info--313a6040d458---------------------------------------)

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----313a6040d458---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----313a6040d458---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----313a6040d458---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----313a6040d458---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----313a6040d458---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----313a6040d458---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----313a6040d458---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----313a6040d458---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----313a6040d458---------------------------------------)