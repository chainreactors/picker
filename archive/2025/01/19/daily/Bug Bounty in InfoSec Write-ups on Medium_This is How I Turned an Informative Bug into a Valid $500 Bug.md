---
title: This is How I Turned an Informative Bug into a Valid $500 Bug
url: https://infosecwriteups.com/this-is-how-i-turned-an-informative-bug-into-a-valid-500-bug-174ffeb94737?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-19
fetch_date: 2025-10-06T20:08:37.957256
---

# This is How I Turned an Informative Bug into a Valid $500 Bug

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F174ffeb94737&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthis-is-how-i-turned-an-informative-bug-into-a-valid-500-bug-174ffeb94737&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthis-is-how-i-turned-an-informative-bug-into-a-valid-500-bug-174ffeb94737&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-174ffeb94737---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-174ffeb94737---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# This is How I Turned an Informative Bug into a Valid $500 Bug

## In this write-up, I have shared the story of a simple Facebook bug where the Activity Log and Hacked Flow features weren’t working as intended.

[![Shubham Bhamare](https://miro.medium.com/v2/resize:fill:64:64/1*YJZ3Ns7NJ_u8GA9ad3G3-A.png)](https://theshubh77.medium.com/?source=post_page---byline--174ffeb94737---------------------------------------)

[Shubham Bhamare](https://theshubh77.medium.com/?source=post_page---byline--174ffeb94737---------------------------------------)

5 min read

·

Jan 13, 2025

--

5

Share

Press enter or click to view image in full size

![]()

Image created/designed by the author

> ✨ Non-members can read this write-up for free using [this link](https://theshubh77.medium.com/174ffeb94737?sk=39c5159d92e0198a478c46bdb3b23aad).

Hi everyone, it’s **Shubham Bhamare** again with a new bug bounty write-up. Today, I’m going to share the story of how I turned an “Informative” bug into a valid $500 bug. This was one of the most interesting findings of my life and a very simple one as well. The target platform was, of course, Facebook 😅

The best part? This bug was found just by observation, like many of my previous findings.

So, without further ado, let’s get started! 👉

**Description:**

Let me give you a brief description of this bug. Facebook has two security features: [**Activity Log**](https://www.facebook.com/help/289066827791446/) and [**Hacked Flow**](https://www.facebook.com/help/1216349518398524/).

* The **Activity Log** allows users to view their recent comments, likes, and other activities on Facebook.
* The **Hacked Flow** is designed to help users undo suspicious activities if they believe their account has been compromised.

--

--

5

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--174ffeb94737---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--174ffeb94737---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--174ffeb94737---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--174ffeb94737---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--174ffeb94737---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Shubham Bhamare](https://miro.medium.com/v2/resize:fill:96:96/1*YJZ3Ns7NJ_u8GA9ad3G3-A.png)](https://theshubh77.medium.com/?source=post_page---post_author_info--174ffeb94737---------------------------------------)

[![Shubham Bhamare](https://miro.medium.com/v2/resize:fill:128:128/1*YJZ3Ns7NJ_u8GA9ad3G3-A.png)](https://theshubh77.medium.com/?source=post_page---post_author_info--174ffeb94737---------------------------------------)

[## Written by Shubham Bhamare](https://theshubh77.medium.com/?source=post_page---post_author_info--174ffeb94737---------------------------------------)

[477 followers](https://theshubh77.medium.com/followers?source=post_page---post_author_info--174ffeb94737---------------------------------------)

·[31 following](https://medium.com/%40theshubh77/following?source=post_page---post_author_info--174ffeb94737---------------------------------------)

An ORDINARY guy with EXTRAORDINARY dreams!

## Responses (5)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----174ffeb94737---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----174ffeb94737---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----174ffeb94737---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----174ffeb94737---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----174ffeb94737---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----174ffeb94737---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----174ffeb94737---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----174ffeb94737---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----174ffeb94737---------------------------------------)