---
title: $25,000 Bounty just for sensitive information disclosure
url: https://infosecwriteups.com/25-000-bounty-just-for-sensitive-information-disclosure-c4f6c5a81795?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-04-07
fetch_date: 2025-10-06T22:03:50.539255
---

# $25,000 Bounty just for sensitive information disclosure

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc4f6c5a81795&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F25-000-bounty-just-for-sensitive-information-disclosure-c4f6c5a81795&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F25-000-bounty-just-for-sensitive-information-disclosure-c4f6c5a81795&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c4f6c5a81795---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c4f6c5a81795---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# $25,000 Bounty just for sensitive information disclosure

[![Mr Horbio](https://miro.medium.com/v2/resize:fill:64:64/1*uney5OKbxxfykdlwmeosyg.jpeg)](https://medium.com/%40hrofficial62?source=post_page---byline--c4f6c5a81795---------------------------------------)

[Mr Horbio](https://medium.com/%40hrofficial62?source=post_page---byline--c4f6c5a81795---------------------------------------)

2 min read

·

Apr 2, 2025

--

Share

This is Hacker One report that helps to understand which kind of Vulnerability we will find in our target and Learn about new methodologies to earn more bounty.

Press enter or click to view image in full size

![]()

Mr.Horbio [Picture]

Hi, My dear hackers

[Mr Horbio](https://medium.com/u/291e52d51b1a?source=post_page---user_mention--c4f6c5a81795---------------------------------------)

 this side with fresh and interesting article. This article helps to identify some hidden bugs which we ignore sometimes. But this article will open your eye. After reading this article you think about some endpoints that you missed during your testing.

This found from HackerOne hactivity. HackeOne gave him $25,000 Bounty for this Vulnerability.

> **POC [Proof of Concept]:**

There is some Endpoint that helps to see the HackerOne reports. When he saw the disclosed report then he identified the one endpoint that is

```
GET /reports/***.json HTTP/2
Host: hackerone.com
```

This Endpoint disclose some sensitive information

> reporter’s email, OTP backup codes, reporter’s phone number, “graphql\_secret\_token”, tshirt size all the reporter account’s internal details etc.

Sensitive data leaked such as:-

```
email
"changed_password_at"
"totp_secret"
"allow_next_sign_in_attempt_at…
```

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c4f6c5a81795---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c4f6c5a81795---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--c4f6c5a81795---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--c4f6c5a81795---------------------------------------)

·[Last published 1 hour ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--c4f6c5a81795---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Mr Horbio](https://miro.medium.com/v2/resize:fill:96:96/1*uney5OKbxxfykdlwmeosyg.jpeg)](https://medium.com/%40hrofficial62?source=post_page---post_author_info--c4f6c5a81795---------------------------------------)

[![Mr Horbio](https://miro.medium.com/v2/resize:fill:128:128/1*uney5OKbxxfykdlwmeosyg.jpeg)](https://medium.com/%40hrofficial62?source=post_page---post_author_info--c4f6c5a81795---------------------------------------)

[## Written by Mr Horbio](https://medium.com/%40hrofficial62?source=post_page---post_author_info--c4f6c5a81795---------------------------------------)

[980 followers](https://medium.com/%40hrofficial62/followers?source=post_page---post_author_info--c4f6c5a81795---------------------------------------)

·[8 following](https://medium.com/%40hrofficial62/following?source=post_page---post_author_info--c4f6c5a81795---------------------------------------)

Here u get bug bounty tips and techniques , grow you learning and earn from this world to survive here🌎

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----c4f6c5a81795---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----c4f6c5a81795---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----c4f6c5a81795---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----c4f6c5a81795---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----c4f6c5a81795---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----c4f6c5a81795---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----c4f6c5a81795---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----c4f6c5a81795---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----c4f6c5a81795---------------------------------------)