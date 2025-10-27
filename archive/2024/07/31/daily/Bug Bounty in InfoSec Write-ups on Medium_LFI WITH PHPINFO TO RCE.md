---
title: LFI WITH PHPINFO TO RCE
url: https://infosecwriteups.com/lfi-with-phpinfo-to-rce-78318f0dc9ce?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-07-31
fetch_date: 2025-10-06T17:41:57.860338
---

# LFI WITH PHPINFO TO RCE

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F78318f0dc9ce&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Flfi-with-phpinfo-to-rce-78318f0dc9ce&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Flfi-with-phpinfo-to-rce-78318f0dc9ce&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-78318f0dc9ce---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-78318f0dc9ce---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# LFI WITH PHPINFO TO RCE

## LFI vulnerabilities when testing PHP applications

[![c0d3x27](https://miro.medium.com/v2/resize:fill:64:64/1*Kj6QOt5K6dTAPyZ9xrbcbA.png)](https://c0d3x27.medium.com/?source=post_page---byline--78318f0dc9ce---------------------------------------)

[c0d3x27](https://c0d3x27.medium.com/?source=post_page---byline--78318f0dc9ce---------------------------------------)

3 min read

·

Jul 30, 2024

--

2

Share

Press enter or click to view image in full size

![]()

Photo by [Growtika](https://unsplash.com/%40growtika?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

### **Introduction**

During assessments it is still common to find LFI vulnerabilities when testing PHP applications. Depending on the server configuration it is often possible to convert these into code execution primitives through known techniques such as;

* */proc/self/environ*
* */proc/self/fd/…*
* */var/log/…*
* */var/lib/php/session/ (PHP Sessions)*
* */tmp/ (PHP Sessions)*
* *php://input wrapper*
* *php://filter wrapper*
* *data: wrapper*

There is a paper where the author documents information related to how the PHP file upload feature works. In particular he notes that if **file\_uploads = on** is set in the PHP configuration file, then PHP will accept a file upload post to any PHP file. He also notes that the upload file will be stored in the *tmp* location, until the requested PHP page is fully processed.

This is also included in the PHP documentation;

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--78318f0dc9ce---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--78318f0dc9ce---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--78318f0dc9ce---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--78318f0dc9ce---------------------------------------)

·[Last published 2 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--78318f0dc9ce---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![c0d3x27](https://miro.medium.com/v2/resize:fill:96:96/1*Kj6QOt5K6dTAPyZ9xrbcbA.png)](https://c0d3x27.medium.com/?source=post_page---post_author_info--78318f0dc9ce---------------------------------------)

[![c0d3x27](https://miro.medium.com/v2/resize:fill:128:128/1*Kj6QOt5K6dTAPyZ9xrbcbA.png)](https://c0d3x27.medium.com/?source=post_page---post_author_info--78318f0dc9ce---------------------------------------)

[## Written by c0d3x27](https://c0d3x27.medium.com/?source=post_page---post_author_info--78318f0dc9ce---------------------------------------)

[1.8K followers](https://c0d3x27.medium.com/followers?source=post_page---post_author_info--78318f0dc9ce---------------------------------------)

·[15 following](https://medium.com/%40c0d3x27/following?source=post_page---post_author_info--78318f0dc9ce---------------------------------------)

OSCP || OSWE || eMAPT || CompTIA CYSA+, Sec+, A+, ITF+, CSAP | | 0-day Researcher | | Security Consultant

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----78318f0dc9ce---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----78318f0dc9ce---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----78318f0dc9ce---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----78318f0dc9ce---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----78318f0dc9ce---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----78318f0dc9ce---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----78318f0dc9ce---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----78318f0dc9ce---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----78318f0dc9ce---------------------------------------)