---
title: Breaking In Through the Backdoor: Password Reset Gone Wrong
url: https://infosecwriteups.com/breaking-in-through-the-backdoor-password-reset-gone-wrong-6e5243c16a19?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-05-16
fetch_date: 2025-10-06T22:25:49.126162
---

# Breaking In Through the Backdoor: Password Reset Gone Wrong

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6e5243c16a19&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbreaking-in-through-the-backdoor-password-reset-gone-wrong-6e5243c16a19&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbreaking-in-through-the-backdoor-password-reset-gone-wrong-6e5243c16a19&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6e5243c16a19---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6e5243c16a19---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Breaking In Through the Backdoor: Password Reset Gone Wrong

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:64:64/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---byline--6e5243c16a19---------------------------------------)

[Ehtesham Ul Haq](https://ehteshamulhaq198.medium.com/?source=post_page---byline--6e5243c16a19---------------------------------------)

4 min read

·

May 14, 2025

--

2

Share

Free Article Link: [Click for free!](https://ehteshamulhaq198.medium.com/breaking-in-through-the-backdoor-password-reset-gone-wrong-6e5243c16a19?sk=cfa15a592fc8490d5f80c762543f9fec)

Press enter or click to view image in full size

![]()

Imagine being able to take over any user’s account on a platform — even without their interaction. No phishing, no social engineering, and no need for access to their inbox. Just a few crafted steps using the password reset feature, and suddenly, you’re inside their account with full control.

That’s exactly what I discovered on target.com during a deeper investigation into how their password reset system works. This vulnerability was not just dangerous — it was critical. It affected every user on the platform, regardless of whether they were verified or not. In this article, I’ll walk you through how a misconfiguration in their routing allowed full account takeover for any user with just their email address.

## **How the Vulnerability Works**

When a user requests a password reset on target.com, they receive a link in their email. This link usually leads to a secure password reset form and also includes a **six-digit code**. So far, that seems normal.

But here’s the problem: the six-digit code received in the email isn’t just used for resetting the password. Due to a **misconfigured routing setup**, this same code also works on another route — **the email verification endpoint**.

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6e5243c16a19---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6e5243c16a19---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--6e5243c16a19---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--6e5243c16a19---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--6e5243c16a19---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:96:96/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--6e5243c16a19---------------------------------------)

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:128:128/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--6e5243c16a19---------------------------------------)

[## Written by Ehtesham Ul Haq](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--6e5243c16a19---------------------------------------)

[520 followers](https://ehteshamulhaq198.medium.com/followers?source=post_page---post_author_info--6e5243c16a19---------------------------------------)

·[99 following](https://medium.com/%40ehteshamulhaq198/following?source=post_page---post_author_info--6e5243c16a19---------------------------------------)

Penetration Tester & Bug Bounty Hunter focused on finding vulnerabilities and helping organizations stay ahead of cyber threats.

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----6e5243c16a19---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----6e5243c16a19---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----6e5243c16a19---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----6e5243c16a19---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----6e5243c16a19---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----6e5243c16a19---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----6e5243c16a19---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----6e5243c16a19---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----6e5243c16a19---------------------------------------)