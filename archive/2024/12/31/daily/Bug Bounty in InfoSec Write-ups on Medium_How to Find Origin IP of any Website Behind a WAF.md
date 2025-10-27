---
title: How to Find Origin IP of any Website Behind a WAF
url: https://infosecwriteups.com/how-to-find-origin-ip-of-any-website-behind-a-waf-c85095156ef7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-31
fetch_date: 2025-10-06T19:38:34.352741
---

# How to Find Origin IP of any Website Behind a WAF

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc85095156ef7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-find-origin-ip-of-any-website-behind-a-waf-c85095156ef7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-find-origin-ip-of-any-website-behind-a-waf-c85095156ef7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c85095156ef7---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c85095156ef7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **How to Find Origin IP of any Website Behind a WAF**

## **In today guide I’ll share some amazing methods to find the origin IP of any website protected by a Web Application Firewall (WAF).**

[![coffinxp](https://miro.medium.com/v2/resize:fill:64:64/1*PjsjomDRyS2MomLQcc4nOw.png)](https://coffinxp.medium.com/?source=post_page---byline--c85095156ef7---------------------------------------)

[coffinxp](https://coffinxp.medium.com/?source=post_page---byline--c85095156ef7---------------------------------------)

8 min read

·

Dec 30, 2024

--

4

Share

Press enter or click to view image in full size

![]()

## **Introduction**

Web Application Firewalls are often used to improve security by hiding a website’s true IP address which adds a strong layer of protection but can make security assessments and bug bounty testing more difficult. By identifying the source IP address you can bypass these layers of protection and assess the server directly, This can uncover vulnerabilities that your WAF or CDN may have hidden.

### **Let’s explore advanced methods for uncovering source IP addresses and Performing detailed security checks**

## **WAF Reconnaissance**

The first thing you should always do is check if your target has a web application firewall. There are a few easy ways to do this but the first thing you should do is ping your target. It will show you all the information about the IP address, you can see in the screenshot the IP address is pointing to the CloudFront server which means its behind the WAF.

--

--

4

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c85095156ef7---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c85095156ef7---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--c85095156ef7---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--c85095156ef7---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--c85095156ef7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![coffinxp](https://miro.medium.com/v2/resize:fill:96:96/1*PjsjomDRyS2MomLQcc4nOw.png)](https://coffinxp.medium.com/?source=post_page---post_author_info--c85095156ef7---------------------------------------)

[![coffinxp](https://miro.medium.com/v2/resize:fill:128:128/1*PjsjomDRyS2MomLQcc4nOw.png)](https://coffinxp.medium.com/?source=post_page---post_author_info--c85095156ef7---------------------------------------)

[## Written by coffinxp](https://coffinxp.medium.com/?source=post_page---post_author_info--c85095156ef7---------------------------------------)

[6.3K followers](https://coffinxp.medium.com/followers?source=post_page---post_author_info--c85095156ef7---------------------------------------)

·[0 following](https://medium.com/%40coffinxp/following?source=post_page---post_author_info--c85095156ef7---------------------------------------)

Helping organizations stay secure through Bug Hunting, OSINT and Security Research | Sharing knowledge as a Content Creator

## Responses (4)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----c85095156ef7---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----c85095156ef7---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----c85095156ef7---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----c85095156ef7---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----c85095156ef7---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----c85095156ef7---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----c85095156ef7---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----c85095156ef7---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----c85095156ef7---------------------------------------)