---
title: Hack File Inclusion in DVWA: A Full Walkthrough — StackZero
url: https://infosecwriteups.com/hack-file-inclusion-in-dvwa-a-full-walkthrough-stackzero-ae0ed2670d23?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-20
fetch_date: 2025-10-04T04:21:50.169900
---

# Hack File Inclusion in DVWA: A Full Walkthrough — StackZero

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fae0ed2670d23&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhack-file-inclusion-in-dvwa-a-full-walkthrough-stackzero-ae0ed2670d23&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhack-file-inclusion-in-dvwa-a-full-walkthrough-stackzero-ae0ed2670d23&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ae0ed2670d23---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ae0ed2670d23---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Hack File Inclusion in DVWA: A Full Walkthrough — StackZero

[![StackZero](https://miro.medium.com/v2/resize:fill:64:64/1*NfCOWe2r5LeicNQD3t8xMA.png)](https://medium.com/%40stackzero?source=post_page---byline--ae0ed2670d23---------------------------------------)

[StackZero](https://medium.com/%40stackzero?source=post_page---byline--ae0ed2670d23---------------------------------------)

8 min read

·

Jan 18, 2023

--

Share

Press enter or click to view image in full size

![]()

> This is a summary of the article in my blog: [https://www.stackzero.net/file-inclusion-introduction/](https://www.stackzero.net/hack-file-inclusion-in-dvwa-a-full-walkthrough/)

In this tutorial, I’m going to show you how to exploit the file inclusion vulnerability in DVWA! But before doing that, for those of you who have not yet read my [previous article](https://www.stackzero.net/file-inclusion-introduction/), here is a very brief introduction!

Basically, file inclusion vulnerabilities happen when a website or application allows users to specify a file that should be included in the application’s code. This is usually done to make it easier for developers to update and maintain the application, but it can also be a major security vulnerability if not properly handled.

Imagine you have a website that allows users to upload profile pictures. If the website doesn’t properly check which files are being uploaded, a hacker could potentially upload a malicious file and trick the website into including it in the code. This could allow the hacker to gain unauthorized access to the system or even take it over completely.

To avoid file inclusion vulnerabilities, it’s crucial for developers to properly validate and sanitize the input of any file inclusion requests. This way, they can ensure that only safe and legitimate files are included in the code.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ae0ed2670d23---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ae0ed2670d23---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--ae0ed2670d23---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--ae0ed2670d23---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--ae0ed2670d23---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![StackZero](https://miro.medium.com/v2/resize:fill:96:96/1*NfCOWe2r5LeicNQD3t8xMA.png)](https://medium.com/%40stackzero?source=post_page---post_author_info--ae0ed2670d23---------------------------------------)

[![StackZero](https://miro.medium.com/v2/resize:fill:128:128/1*NfCOWe2r5LeicNQD3t8xMA.png)](https://medium.com/%40stackzero?source=post_page---post_author_info--ae0ed2670d23---------------------------------------)

[## Written by StackZero](https://medium.com/%40stackzero?source=post_page---post_author_info--ae0ed2670d23---------------------------------------)

[362 followers](https://medium.com/%40stackzero/followers?source=post_page---post_author_info--ae0ed2670d23---------------------------------------)

·[61 following](https://medium.com/%40stackzero/following?source=post_page---post_author_info--ae0ed2670d23---------------------------------------)

I have a passion for sharing my knowledge and helping others stay safe online. I just want to share tips and advice useful for me.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----ae0ed2670d23---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----ae0ed2670d23---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----ae0ed2670d23---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----ae0ed2670d23---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----ae0ed2670d23---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----ae0ed2670d23---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----ae0ed2670d23---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----ae0ed2670d23---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----ae0ed2670d23---------------------------------------)