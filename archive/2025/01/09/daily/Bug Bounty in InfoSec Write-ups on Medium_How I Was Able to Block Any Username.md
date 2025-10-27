---
title: How I Was Able to Block Any Username
url: https://infosecwriteups.com/how-i-was-able-to-block-any-username-5707a1fbd25c?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-09
fetch_date: 2025-10-06T20:08:24.316258
---

# How I Was Able to Block Any Username

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F5707a1fbd25c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-was-able-to-block-any-username-5707a1fbd25c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-was-able-to-block-any-username-5707a1fbd25c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-5707a1fbd25c---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-5707a1fbd25c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **How I Was Able to Block Any Username**

[![JEETPAL](https://miro.medium.com/v2/resize:fill:64:64/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---byline--5707a1fbd25c---------------------------------------)

[JEETPAL](https://jeetpal2007.medium.com/?source=post_page---byline--5707a1fbd25c---------------------------------------)

2 min read

·

Jan 6, 2025

--

4

Share

[**FREE ARTICLE**](https://medium.com/%40jeetpal2007/how-i-was-able-to-block-any-username-5707a1fbd25c?sk=1276446f2065297be973e09b4437736a)

Hello Everyone!

Today, I’ll share how I discovered a flaw that allowed me to block or lock any username on a platform.

## The Beginning

I was hunting on a program called **redacted.com**, where the scope was limited to the main website (**redacted.com**). I began testing different areas:

* **Business logic flaws**
* **Session management issues**
* **Known CVEs**

## The Discovery

While exploring, I decided to test the **account deletion feature**. My goal was to see if deleting an account required a password confirmation.

1. I attempted to delete my account.
2. Unfortunately, a **password confirmation was required**, so I provided it and successfully deleted my account.

After deletion, I tried to **recreate my account with the same username** (`jeetpal2007`).

To my surprise:

* The username was **unavailable** for reuse.
* It seemed permanently locked in the system.

So, I created a new account with the username `jeetpal`, which was still available.

## The Core Issue

I noticed a peculiar behavior:

* When an account was deleted, **only the email and password were removed** from the database.

--

--

4

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5707a1fbd25c---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5707a1fbd25c---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--5707a1fbd25c---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--5707a1fbd25c---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--5707a1fbd25c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![JEETPAL](https://miro.medium.com/v2/resize:fill:96:96/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--5707a1fbd25c---------------------------------------)

[![JEETPAL](https://miro.medium.com/v2/resize:fill:128:128/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--5707a1fbd25c---------------------------------------)

[## Written by JEETPAL](https://jeetpal2007.medium.com/?source=post_page---post_author_info--5707a1fbd25c---------------------------------------)

[2.3K followers](https://jeetpal2007.medium.com/followers?source=post_page---post_author_info--5707a1fbd25c---------------------------------------)

·[3 following](https://medium.com/%40jeetpal2007/following?source=post_page---post_author_info--5707a1fbd25c---------------------------------------)

A security researcher,Auditor Web3 & Developer Connect me on social media via <https://linktr.ee/jeetpal2007> query:jeetpal2007@gmail.com

## Responses (4)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----5707a1fbd25c---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----5707a1fbd25c---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----5707a1fbd25c---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----5707a1fbd25c---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----5707a1fbd25c---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----5707a1fbd25c---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----5707a1fbd25c---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----5707a1fbd25c---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----5707a1fbd25c---------------------------------------)