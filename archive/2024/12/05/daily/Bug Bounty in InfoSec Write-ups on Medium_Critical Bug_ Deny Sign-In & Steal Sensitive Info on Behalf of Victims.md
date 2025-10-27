---
title: Critical Bug: Deny Sign-In & Steal Sensitive Info on Behalf of Victims
url: https://infosecwriteups.com/critical-bug-deny-sign-in-steal-sensitive-info-on-behalf-of-victims-cad4ced9227d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-05
fetch_date: 2025-10-06T19:37:36.361494
---

# Critical Bug: Deny Sign-In & Steal Sensitive Info on Behalf of Victims

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fcad4ced9227d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcritical-bug-deny-sign-in-steal-sensitive-info-on-behalf-of-victims-cad4ced9227d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcritical-bug-deny-sign-in-steal-sensitive-info-on-behalf-of-victims-cad4ced9227d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-cad4ced9227d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-cad4ced9227d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🚨 Critical Bug: Deny Sign-In & Steal Sensitive Info on Behalf of Victims 🚨

[![JEETPAL](https://miro.medium.com/v2/resize:fill:64:64/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---byline--cad4ced9227d---------------------------------------)

[JEETPAL](https://jeetpal2007.medium.com/?source=post_page---byline--cad4ced9227d---------------------------------------)

2 min read

·

Dec 3, 2024

--

1

Share

[**Read Free**](https://medium.com/%40jeetpal2007/critical-bug-deny-sign-in-steal-sensitive-info-on-behalf-of-victims-cad4ced9227d?sk=3621153542e9675edc1f77509ea1ccdb)

## What’s the Bug? 🐞

This vulnerability allows me (or any attacker 😈) to:
1️⃣ **Block anyone’s sign-in**, order request, or password reset **without their permission** — totally locking them out of their account!
2️⃣ View **private details** about the victim, such as:

* 🌐 **IP Address**
* 📍 **Location**
* 💻 **Device Info**
* 📲 **Sign-In Method** (phone or email).

And no, I didn’t need any authentication to do all this. Pretty scary, right? 😱

## Why Does It Matter? 🔥

Here’s why this bug is a big deal:

1️⃣ **Denial of Service (DoS):**

* I can repeatedly deny a user’s actions, essentially **locking them out of their account**.

2️⃣ **Sensitive Data Exposure:**

* The victim’s **IP, location, and device info** are exposed for anyone to see. This violates privacy big time.

3️⃣ **Unauthorized Control:**

* Attackers can perform these actions without any authentication, acting **on behalf of the victim**.

4️⃣ **Privacy Violations:**

* Imagine the legal trouble for exposing sensitive user data — **GDPR**, **CCPA**, and other laws might come knocking.

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--cad4ced9227d---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--cad4ced9227d---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--cad4ced9227d---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--cad4ced9227d---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--cad4ced9227d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![JEETPAL](https://miro.medium.com/v2/resize:fill:96:96/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--cad4ced9227d---------------------------------------)

[![JEETPAL](https://miro.medium.com/v2/resize:fill:128:128/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--cad4ced9227d---------------------------------------)

[## Written by JEETPAL](https://jeetpal2007.medium.com/?source=post_page---post_author_info--cad4ced9227d---------------------------------------)

[2.3K followers](https://jeetpal2007.medium.com/followers?source=post_page---post_author_info--cad4ced9227d---------------------------------------)

·[3 following](https://medium.com/%40jeetpal2007/following?source=post_page---post_author_info--cad4ced9227d---------------------------------------)

A security researcher,Auditor Web3 & Developer Connect me on social media via <https://linktr.ee/jeetpal2007> query:jeetpal2007@gmail.com

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----cad4ced9227d---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----cad4ced9227d---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----cad4ced9227d---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----cad4ced9227d---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----cad4ced9227d---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----cad4ced9227d---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----cad4ced9227d---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----cad4ced9227d---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----cad4ced9227d---------------------------------------)