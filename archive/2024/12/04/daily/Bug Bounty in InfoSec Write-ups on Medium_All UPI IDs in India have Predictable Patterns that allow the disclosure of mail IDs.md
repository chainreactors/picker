---
title: All UPI IDs in India have Predictable Patterns that allow the disclosure of mail IDs
url: https://infosecwriteups.com/all-upi-ids-in-india-have-predictable-patterns-that-allow-the-disclosure-of-mail-ids-eede37a35758?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-04
fetch_date: 2025-10-06T19:37:36.280904
---

# All UPI IDs in India have Predictable Patterns that allow the disclosure of mail IDs

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Feede37a35758&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fall-upi-ids-in-india-have-predictable-patterns-that-allow-the-disclosure-of-mail-ids-eede37a35758&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fall-upi-ids-in-india-have-predictable-patterns-that-allow-the-disclosure-of-mail-ids-eede37a35758&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-eede37a35758---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-eede37a35758---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **All UPI IDs in India have Predictable Patterns that allow the disclosure of mail IDs**

[![JEETPAL](https://miro.medium.com/v2/resize:fill:64:64/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---byline--eede37a35758---------------------------------------)

[JEETPAL](https://jeetpal2007.medium.com/?source=post_page---byline--eede37a35758---------------------------------------)

3 min read

·

Dec 2, 2024

--

3

Share

Press enter or click to view image in full size

![]()

Photo by [SumUp](https://unsplash.com/%40sumup?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Read free : <https://medium.com/bugbountywriteup/all-upi-ids-in-india-have-predictable-patterns-that-allow-the-disclosure-of-mail-ids-eede37a35758?sk=fdeb1f95bf11c17eb8e745d817501d91>

Hey, security enthusiasts! 🌟

As UPI (Unified Payments Interface) dominates the Indian digital payments landscape, I noticed a **privacy loophole** across **all major UPI platforms** that could expose sensitive user information. This isn’t just about UPI apps — it’s a systemic issue! 🛑

Let’s break it down step by step. 🕵️‍♂️💻

## 🔍 How UPI IDs Work Across Platforms

UPI IDs are generated based on **your email address** or **phone number**. Most platforms like PhonePe, Google Pay, Paytm, and others follow similar patterns:

1. **Email-Based UPI IDs**

* If your email is **pal6504@gmail.com**, your UPI ID becomes:
  👉 **pal6504@oksbi**,**pal6504@okaxis**, or **pal6504@okhdfcbank** (depending on your bank).

**2. Phone Number-Based UPI IDs**

* If your phone number is **9876543210**, your UPI ID becomes:
  👉 **9876543210@oksbi**, **9876543210@okicici**, etc.

**3. Multiple Accounts with the Same Email**

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--eede37a35758---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--eede37a35758---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--eede37a35758---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--eede37a35758---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--eede37a35758---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![JEETPAL](https://miro.medium.com/v2/resize:fill:96:96/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--eede37a35758---------------------------------------)

[![JEETPAL](https://miro.medium.com/v2/resize:fill:128:128/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--eede37a35758---------------------------------------)

[## Written by JEETPAL](https://jeetpal2007.medium.com/?source=post_page---post_author_info--eede37a35758---------------------------------------)

[2.3K followers](https://jeetpal2007.medium.com/followers?source=post_page---post_author_info--eede37a35758---------------------------------------)

·[3 following](https://medium.com/%40jeetpal2007/following?source=post_page---post_author_info--eede37a35758---------------------------------------)

A security researcher,Auditor Web3 & Developer Connect me on social media via <https://linktr.ee/jeetpal2007> query:jeetpal2007@gmail.com

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----eede37a35758---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----eede37a35758---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----eede37a35758---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----eede37a35758---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----eede37a35758---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----eede37a35758---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----eede37a35758---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----eede37a35758---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----eede37a35758---------------------------------------)