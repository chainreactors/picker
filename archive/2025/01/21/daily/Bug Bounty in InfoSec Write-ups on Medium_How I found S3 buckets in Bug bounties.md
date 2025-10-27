---
title: How I found S3 buckets in Bug bounties
url: https://infosecwriteups.com/how-i-found-s3-buckets-in-bug-bounties-501faf76c3f9?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-21
fetch_date: 2025-10-06T20:09:16.721824
---

# How I found S3 buckets in Bug bounties

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F501faf76c3f9&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-s3-buckets-in-bug-bounties-501faf76c3f9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-s3-buckets-in-bug-bounties-501faf76c3f9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-501faf76c3f9---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-501faf76c3f9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How I found S3 buckets in Bug bounties

## Cloud enumeration and exploitation

[![Mukilan Baskaran](https://miro.medium.com/v2/resize:fill:64:64/1*tif1c7lTx883WhLR92OsxA.jpeg)](https://mukibas37.medium.com/?source=post_page---byline--501faf76c3f9---------------------------------------)

[Mukilan Baskaran](https://mukibas37.medium.com/?source=post_page---byline--501faf76c3f9---------------------------------------)

2 min read

·

Jan 20, 2025

--

Share

Welcome back infosec guys and bug hunters today I came up with the art of finding and exploiting misconfigured s3 buckets for finding vulnerabilities.

Press enter or click to view image in full size

![]()

Photo by [Donny Jiang](https://unsplash.com/%40dotnny?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

**Cloud Enumeration:**

AWS stands for Amazon Web Services. Through this, we can access enormous amounts of unstructured data, such as images and videos. Cloud enumeration is a hopeful way to find exposed information wisely.

So we are going to the art of enumeration and exploitation of misconfigured s3 buckets.

Press enter or click to view image in full size

![]()

Photo by [Abdullah Aslam](https://unsplash.com/%40abdullahaslam_11575630_sink?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

**AWS S3 bucket enumeration:**

An S3 (Simple Storage Service) is a storage resource provided by Amazon to store and retrieve large numbers of unstructured data including images, videos, and backup files.

**Naming Conventions and Discovery:**

***Standard Convention:***

> format for the standard convention: [bucket-name].s3.amazonaws.com
>
> example for the standard convention: example.s3.amazonaws.com

***Alternative Convention:***

> format for the…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--501faf76c3f9---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--501faf76c3f9---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--501faf76c3f9---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--501faf76c3f9---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--501faf76c3f9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Mukilan Baskaran](https://miro.medium.com/v2/resize:fill:96:96/1*tif1c7lTx883WhLR92OsxA.jpeg)](https://mukibas37.medium.com/?source=post_page---post_author_info--501faf76c3f9---------------------------------------)

[![Mukilan Baskaran](https://miro.medium.com/v2/resize:fill:128:128/1*tif1c7lTx883WhLR92OsxA.jpeg)](https://mukibas37.medium.com/?source=post_page---post_author_info--501faf76c3f9---------------------------------------)

[## Written by Mukilan Baskaran](https://mukibas37.medium.com/?source=post_page---post_author_info--501faf76c3f9---------------------------------------)

[806 followers](https://mukibas37.medium.com/followers?source=post_page---post_author_info--501faf76c3f9---------------------------------------)

·[1K following](https://medium.com/%40mukibas37/following?source=post_page---post_author_info--501faf76c3f9---------------------------------------)

CTF player | Cyber Security Enthusiast

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----501faf76c3f9---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----501faf76c3f9---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----501faf76c3f9---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----501faf76c3f9---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----501faf76c3f9---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----501faf76c3f9---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----501faf76c3f9---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----501faf76c3f9---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----501faf76c3f9---------------------------------------)