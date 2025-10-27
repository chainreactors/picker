---
title: Unverified Email Change Flaw on Apps.Target.com: A Sneaky Account Takeover Trick
url: https://infosecwriteups.com/unverified-email-change-flaw-on-apps-target-com-a-sneaky-account-takeover-trick-2d3402223f4f?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-02-20
fetch_date: 2025-10-06T20:34:41.493463
---

# Unverified Email Change Flaw on Apps.Target.com: A Sneaky Account Takeover Trick

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2d3402223f4f&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funverified-email-change-flaw-on-apps-target-com-a-sneaky-account-takeover-trick-2d3402223f4f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funverified-email-change-flaw-on-apps-target-com-a-sneaky-account-takeover-trick-2d3402223f4f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2d3402223f4f---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2d3402223f4f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Unverified Email Change Flaw on Apps.Target.com: A Sneaky Account Takeover Trick

[![JEETPAL](https://miro.medium.com/v2/resize:fill:64:64/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---byline--2d3402223f4f---------------------------------------)

[JEETPAL](https://jeetpal2007.medium.com/?source=post_page---byline--2d3402223f4f---------------------------------------)

2 min read

·

Feb 18, 2025

--

Share

[**READ IT FOR FREE**](https://medium.com/%40jeetpal2007/unverified-email-change-flaw-on-apps-target-com-a-sneaky-account-takeover-trick-2d3402223f4f?sk=40e756259b7ea1ea636beab9e3f88fe6)

## Introduction

Imagine waking up one day, trying to sign up for a website, only to find out that your email is already in use — by someone else. Worse, you can’t even reclaim it. That’s exactly what I discovered while testing [apps.target.com](https://apps.target.com/). A flaw in the email change process allows attackers to hijack email identities without verification, effectively locking real users out.

## How This Works (Step-by-Step Exploit)

Here’s how an attacker can exploit this issue to take over someone’s email identity:

1. **Create Two Accounts:**

* The attacker creates one account using their own email (e.g., attacker@example.com).
* The victim already has or plans to create an account using their email (e.g., victim@example.com).

**2. Change the Email (Without Verification!):**

* The attacker logs into their account.
* They navigate to the account settings and change their email to **victim@example.com**.
* No confirmation or verification is required. The email is changed instantly.
* Attacker enable 2FA so victim Can’t reset password anymore

**3. Blocking the Victim from Their Own Email:**

* If the victim tries to **sign up** using their email…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2d3402223f4f---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2d3402223f4f---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--2d3402223f4f---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--2d3402223f4f---------------------------------------)

·[Last published just now](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--2d3402223f4f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![JEETPAL](https://miro.medium.com/v2/resize:fill:96:96/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--2d3402223f4f---------------------------------------)

[![JEETPAL](https://miro.medium.com/v2/resize:fill:128:128/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--2d3402223f4f---------------------------------------)

[## Written by JEETPAL](https://jeetpal2007.medium.com/?source=post_page---post_author_info--2d3402223f4f---------------------------------------)

[2.3K followers](https://jeetpal2007.medium.com/followers?source=post_page---post_author_info--2d3402223f4f---------------------------------------)

·[3 following](https://medium.com/%40jeetpal2007/following?source=post_page---post_author_info--2d3402223f4f---------------------------------------)

A security researcher,Auditor Web3 & Developer Connect me on social media via <https://linktr.ee/jeetpal2007> query:jeetpal2007@gmail.com

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----2d3402223f4f---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----2d3402223f4f---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----2d3402223f4f---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----2d3402223f4f---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----2d3402223f4f---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----2d3402223f4f---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----2d3402223f4f---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----2d3402223f4f---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----2d3402223f4f---------------------------------------)