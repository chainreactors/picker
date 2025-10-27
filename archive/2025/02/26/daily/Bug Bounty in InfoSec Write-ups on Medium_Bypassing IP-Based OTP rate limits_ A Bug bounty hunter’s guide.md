---
title: Bypassing IP-Based OTP rate limits: A Bug bounty hunter’s guide
url: https://infosecwriteups.com/bypassing-ip-based-otp-rate-limits-a-bug-bounty-hunters-guide-16ce8a1f2c71?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-02-26
fetch_date: 2025-10-06T20:34:23.251485
---

# Bypassing IP-Based OTP rate limits: A Bug bounty hunter’s guide

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F16ce8a1f2c71&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-ip-based-otp-rate-limits-a-bug-bounty-hunters-guide-16ce8a1f2c71&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-ip-based-otp-rate-limits-a-bug-bounty-hunters-guide-16ce8a1f2c71&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-16ce8a1f2c71---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-16ce8a1f2c71---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Bypassing IP-Based OTP rate limits: A Bug bounty hunter’s guide

[![Vivek PS](https://miro.medium.com/v2/resize:fill:64:64/1*gswVWtLbFDKYFuLKsi063g.png)](https://medium.com/%40vivekps143?source=post_page---byline--16ce8a1f2c71---------------------------------------)

[Vivek PS](https://medium.com/%40vivekps143?source=post_page---byline--16ce8a1f2c71---------------------------------------)

4 min read

·

Feb 25, 2025

--

Share

Press enter or click to view image in full size

![]()

## Introduction

Rate limiting is one of the most common protections implemented in OTP-based authentication. However, many applications rely solely on IP-based restrictions, making them vulnerable to bypass techniques. As a bug bounty hunter, identifying these flaws can lead to critical security reports and potential payouts.

This article explores how attackers bypass IP-based OTP rate limits with real-world techniques, PoC scripts, and key misconfigurations to look for while testing.

## How IP-Based OTP Rate Limiting Works

Many applications enforce OTP request restrictions based on the user’s IP address. Typical implementations include:

* **Per-IP Rate Limits:** Blocking OTP requests after a certain threshold (e.g., 5 attempts per minute per IP).
* **Cooldown Periods:** Enforcing a wait time before the next OTP request.
* **IP Blacklisting:** Blocking an IP after too many requests.
* **Geo-based Restrictions:** Preventing requests from certain locations.

The assumption is that limiting OTP requests per IP will prevent brute-force or spam attacks. However, bug bounty hunters can often bypass these limitations using multiple…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--16ce8a1f2c71---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--16ce8a1f2c71---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--16ce8a1f2c71---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--16ce8a1f2c71---------------------------------------)

·[Last published just now](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--16ce8a1f2c71---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Vivek PS](https://miro.medium.com/v2/resize:fill:96:96/1*gswVWtLbFDKYFuLKsi063g.png)](https://medium.com/%40vivekps143?source=post_page---post_author_info--16ce8a1f2c71---------------------------------------)

[![Vivek PS](https://miro.medium.com/v2/resize:fill:128:128/1*gswVWtLbFDKYFuLKsi063g.png)](https://medium.com/%40vivekps143?source=post_page---post_author_info--16ce8a1f2c71---------------------------------------)

[## Written by Vivek PS](https://medium.com/%40vivekps143?source=post_page---post_author_info--16ce8a1f2c71---------------------------------------)

[420 followers](https://medium.com/%40vivekps143/followers?source=post_page---post_author_info--16ce8a1f2c71---------------------------------------)

·[69 following](https://medium.com/%40vivekps143/following?source=post_page---post_author_info--16ce8a1f2c71---------------------------------------)

I’m a programmer, web security researcher and chess player, focused on innovation, learning, and creating impactful solutions for growth.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----16ce8a1f2c71---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----16ce8a1f2c71---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----16ce8a1f2c71---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----16ce8a1f2c71---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----16ce8a1f2c71---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----16ce8a1f2c71---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----16ce8a1f2c71---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----16ce8a1f2c71---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----16ce8a1f2c71---------------------------------------)