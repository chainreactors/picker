---
title: Stored XSS to Admin in Unauthenticated-WordPress
url: https://infosecwriteups.com/stored-xss-to-admin-in-unauthenticated-wordpress-cb76bae66623?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-19
fetch_date: 2025-10-06T20:08:34.190245
---

# Stored XSS to Admin in Unauthenticated-WordPress

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fcb76bae66623&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fstored-xss-to-admin-in-unauthenticated-wordpress-cb76bae66623&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fstored-xss-to-admin-in-unauthenticated-wordpress-cb76bae66623&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-cb76bae66623---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-cb76bae66623---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Stored XSS to Admin in Unauthenticated-WordPress

## Abusing security features the right way

[![c0d3x27](https://miro.medium.com/v2/resize:fill:64:64/1*Kj6QOt5K6dTAPyZ9xrbcbA.png)](https://c0d3x27.medium.com/?source=post_page---byline--cb76bae66623---------------------------------------)

[c0d3x27](https://c0d3x27.medium.com/?source=post_page---byline--cb76bae66623---------------------------------------)

6 min read

·

Jan 18, 2025

--

Share

Press enter or click to view image in full size

![]()

### Keywords:

* **nonce**
* **HttpOnly**
* **Secure**

### Introduction:

The [All in One SEO Pack](https://aioseo.com/) plugin, a widely-used SEO tool for *WordPress* with over 1 million active installs, has a critical security vulnerability in one of its feature. This vulnerability, identified as **Unauthenticated Stored Cross-Site Scripting (XSS)**, allows attackers to inject malicious JavaScript code through the headers, leading to execution of harmful scripts on WordPress administrator pages.

This vulnerability expose websites to attacks where an attacker can execute arbitrary JavaScript on the site simply by visiting the public-facing pages.

### Blocker Functionalities

In the case of the **All in One SEO Pack** plugin, the stored XSS vulnerability is triggered by its Blocker functionality. While this feature can help prevent malicious bots from accessing the site, the issue arises when the Track Blocked Bots setting is enabled. When this setting is turned on and a bot requests is detected based on a matching header predefined list of bot names such as [bots](https://gist.github.com/dvlop/fca36213ad6237891609e1e038a3bbc1), the plugin blocks the request and logs the event. This information…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--cb76bae66623---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--cb76bae66623---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--cb76bae66623---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--cb76bae66623---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--cb76bae66623---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![c0d3x27](https://miro.medium.com/v2/resize:fill:96:96/1*Kj6QOt5K6dTAPyZ9xrbcbA.png)](https://c0d3x27.medium.com/?source=post_page---post_author_info--cb76bae66623---------------------------------------)

[![c0d3x27](https://miro.medium.com/v2/resize:fill:128:128/1*Kj6QOt5K6dTAPyZ9xrbcbA.png)](https://c0d3x27.medium.com/?source=post_page---post_author_info--cb76bae66623---------------------------------------)

[## Written by c0d3x27](https://c0d3x27.medium.com/?source=post_page---post_author_info--cb76bae66623---------------------------------------)

[1.8K followers](https://c0d3x27.medium.com/followers?source=post_page---post_author_info--cb76bae66623---------------------------------------)

·[15 following](https://medium.com/%40c0d3x27/following?source=post_page---post_author_info--cb76bae66623---------------------------------------)

OSCP || OSWE || eMAPT || CompTIA CYSA+, Sec+, A+, ITF+, CSAP | | 0-day Researcher | | Security Consultant

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----cb76bae66623---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----cb76bae66623---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----cb76bae66623---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----cb76bae66623---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----cb76bae66623---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----cb76bae66623---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----cb76bae66623---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----cb76bae66623---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----cb76bae66623---------------------------------------)