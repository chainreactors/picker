---
title: IDOR Exposed: How a Simple ID Can Leak Millions of Records
url: https://infosecwriteups.com/idor-exposed-how-a-simple-id-can-leak-millions-of-records-890d9f200d0a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-04-10
fetch_date: 2025-10-06T22:04:46.164918
---

# IDOR Exposed: How a Simple ID Can Leak Millions of Records

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F890d9f200d0a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fidor-exposed-how-a-simple-id-can-leak-millions-of-records-890d9f200d0a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fidor-exposed-how-a-simple-id-can-leak-millions-of-records-890d9f200d0a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-890d9f200d0a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-890d9f200d0a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **IDOR Exposed: How a Simple ID Can Leak Millions of Records**

## **Real-World Examples + Tools to Find Insecure Direct Object Reference (IDOR) Vulnerabilities**

[![Elie Attieh](https://miro.medium.com/v2/resize:fill:64:64/1*8AkmY-S1N8ExOpCH--DB-A.jpeg)](https://medium.com/%40ElieAttieh?source=post_page---byline--890d9f200d0a---------------------------------------)

[Elie Attieh](https://medium.com/%40ElieAttieh?source=post_page---byline--890d9f200d0a---------------------------------------)

4 min read

·

Apr 7, 2025

--

2

Share

### **What Is an IDOR?**

**Insecure Direct Object Reference (IDOR)** is a type of access control vulnerability where an application exposes internal object references (like user IDs or document numbers) without properly verifying if the user is authorized to access them.

This happens when developers assume users will only request their own data and fail to enforce proper checks on the backend.

Press enter or click to view image in full size

![]()

**What can go wrong? Attackers can:**

* View private user data
* Modify information they don’t own
* Delete sensitive records

All just by manipulating a single parameter in the URL or request.

> **⚠️ Disclaimer**
>
> This article is for educational purposes only. All testing should be conducted **legally** on platforms you own or through approved bug bounty programs (e.g. HackerOne, Bugcrowd).

Let’s break it down and show how easy it is to test for these bugs using real examples and tools.

### **Why IDOR Is the Silent Killer of Web Apps**

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--890d9f200d0a---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--890d9f200d0a---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--890d9f200d0a---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--890d9f200d0a---------------------------------------)

·[Last published 1 hour ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--890d9f200d0a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Elie Attieh](https://miro.medium.com/v2/resize:fill:96:96/1*8AkmY-S1N8ExOpCH--DB-A.jpeg)](https://medium.com/%40ElieAttieh?source=post_page---post_author_info--890d9f200d0a---------------------------------------)

[![Elie Attieh](https://miro.medium.com/v2/resize:fill:128:128/1*8AkmY-S1N8ExOpCH--DB-A.jpeg)](https://medium.com/%40ElieAttieh?source=post_page---post_author_info--890d9f200d0a---------------------------------------)

[## Written by Elie Attieh](https://medium.com/%40ElieAttieh?source=post_page---post_author_info--890d9f200d0a---------------------------------------)

[220 followers](https://medium.com/%40ElieAttieh/followers?source=post_page---post_author_info--890d9f200d0a---------------------------------------)

·[434 following](https://medium.com/%40ElieAttieh/following?source=post_page---post_author_info--890d9f200d0a---------------------------------------)

Cyber Security Engineer | Microsoft Cloud Security | Penetration Tester | Intune | Vulnerability Assessment | Threat Intelligence | Microsoft Sentinel | SOC |

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----890d9f200d0a---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----890d9f200d0a---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----890d9f200d0a---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----890d9f200d0a---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----890d9f200d0a---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----890d9f200d0a---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----890d9f200d0a---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----890d9f200d0a---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----890d9f200d0a---------------------------------------)