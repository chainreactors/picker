---
title: How I Bypassed Account Verification with a Simple Host Header Trick
url: https://infosecwriteups.com/how-i-bypassed-account-verification-with-a-simple-host-header-trick-728368ae877b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-06
fetch_date: 2025-10-06T23:26:58.802660
---

# How I Bypassed Account Verification with a Simple Host Header Trick

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F728368ae877b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-bypassed-account-verification-with-a-simple-host-header-trick-728368ae877b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-bypassed-account-verification-with-a-simple-host-header-trick-728368ae877b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-728368ae877b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-728368ae877b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How I Bypassed Account Verification with a Simple Host Header Trick

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:64:64/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---byline--728368ae877b---------------------------------------)

[Ehtesham Ul Haq](https://ehteshamulhaq198.medium.com/?source=post_page---byline--728368ae877b---------------------------------------)

3 min read

·

Jul 3, 2025

--

Share

Free Article Link: [Click for free!](https://ehteshamulhaq198.medium.com/how-i-bypassed-account-verification-with-a-simple-host-header-trick-728368ae877b?sk=2921e5036f85ec8678d089edc2a2efb0)

![]()

Hey Security Enthusiasts,

I hope you’re all doing great. Today, I’m sharing a critical vulnerability I discovered that led to both **verification bypass** and **authentication bypass** — a pretty dangerous combination if left unchecked. It’s one of those bugs that shows how something as simple as a manipulated header can have a big impact.

## What is Host Header Injection?

Host Header Injection is a type of web vulnerability where an attacker manipulates the `Host` header of an HTTP request to force a server to generate links, redirects, or behaviors that point to an attacker-controlled domain. This typically happens when the backend relies on the `Host` header for generating absolute URLs, verification links, or redirects—without validating if it actually belongs to the trusted domain.

If exploited properly, this can lead to a wide range of attacks:

* Token or link hijacking
* Internal access exposure
* Open redirect
* Bypassing verification or authentication steps

Let’s walk through how this happened on the target platform.

## The Vulnerability

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--728368ae877b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--728368ae877b---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--728368ae877b---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--728368ae877b---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--728368ae877b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:96:96/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--728368ae877b---------------------------------------)

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:128:128/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--728368ae877b---------------------------------------)

[## Written by Ehtesham Ul Haq](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--728368ae877b---------------------------------------)

[520 followers](https://ehteshamulhaq198.medium.com/followers?source=post_page---post_author_info--728368ae877b---------------------------------------)

·[99 following](https://medium.com/%40ehteshamulhaq198/following?source=post_page---post_author_info--728368ae877b---------------------------------------)

Penetration Tester & Bug Bounty Hunter focused on finding vulnerabilities and helping organizations stay ahead of cyber threats.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----728368ae877b---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----728368ae877b---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----728368ae877b---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----728368ae877b---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----728368ae877b---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----728368ae877b---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----728368ae877b---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----728368ae877b---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----728368ae877b---------------------------------------)