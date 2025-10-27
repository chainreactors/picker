---
title: Unauthenticated Password Reset Abuse
url: https://infosecwriteups.com/unauthenticated-password-reset-abuse-ad2375b358f5?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-16
fetch_date: 2025-10-06T23:50:38.111716
---

# Unauthenticated Password Reset Abuse

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fad2375b358f5&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funauthenticated-password-reset-abuse-ad2375b358f5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funauthenticated-password-reset-abuse-ad2375b358f5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ad2375b358f5---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ad2375b358f5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Unauthenticated Password Reset Abuse

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:64:64/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---byline--ad2375b358f5---------------------------------------)

[Ehtesham Ul Haq](https://ehteshamulhaq198.medium.com/?source=post_page---byline--ad2375b358f5---------------------------------------)

4 min read

·

Jul 15, 2025

--

2

Share

Free Article Link: [Click for free!](https://ehteshamulhaq198.medium.com/unauthenticated-password-reset-abuse-ad2375b358f5?sk=4a10fb7ed67a2d12a8895533e541f077)

Press enter or click to view image in full size

![]()

Hello fellow researchers and security professionals,

Today, I’d like to walk you through a serious vulnerability I discovered on `target.com` that allowed an attacker to **unauthenticatedly remove user passwords** at scale. This issue, when combined with other common bugs like **user enumeration** and **XSS**, could lead to automated account takeovers affecting a large number of users.

Let’s break down the findings, starting with the core issue: **Captcha enforcement and its weaknesses**.

## Understanding Captcha Weakness and Its Role

Captcha is typically used to prevent bots and automated attacks. In a secure implementation, it acts as a barrier that limits how often a particular action — like a password reset — can be attempted.

However, in this case, the captcha mechanism implemented in the password reset flow on `target.com` lacked effective **rate limiting**. This meant an attacker could continuously send password reset requests using different email addresses without ever getting blocked or throttled. Essentially, the captcha became a checkbox with no real defense power, especially when brute-forced or automated.

## The Core Issue — Password Reset Without…

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ad2375b358f5---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ad2375b358f5---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--ad2375b358f5---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--ad2375b358f5---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--ad2375b358f5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:96:96/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--ad2375b358f5---------------------------------------)

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:128:128/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--ad2375b358f5---------------------------------------)

[## Written by Ehtesham Ul Haq](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--ad2375b358f5---------------------------------------)

[520 followers](https://ehteshamulhaq198.medium.com/followers?source=post_page---post_author_info--ad2375b358f5---------------------------------------)

·[99 following](https://medium.com/%40ehteshamulhaq198/following?source=post_page---post_author_info--ad2375b358f5---------------------------------------)

Penetration Tester & Bug Bounty Hunter focused on finding vulnerabilities and helping organizations stay ahead of cyber threats.

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----ad2375b358f5---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----ad2375b358f5---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----ad2375b358f5---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----ad2375b358f5---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----ad2375b358f5---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----ad2375b358f5---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----ad2375b358f5---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----ad2375b358f5---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----ad2375b358f5---------------------------------------)