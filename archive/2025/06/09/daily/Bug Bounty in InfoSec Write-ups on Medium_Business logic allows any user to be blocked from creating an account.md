---
title: Business logic allows any user to be blocked from creating an account
url: https://infosecwriteups.com/business-logic-allows-any-user-to-be-blocked-from-creating-an-account-6a7ab7013ccc?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-06-09
fetch_date: 2025-10-06T22:51:46.430033
---

# Business logic allows any user to be blocked from creating an account

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6a7ab7013ccc&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbusiness-logic-allows-any-user-to-be-blocked-from-creating-an-account-6a7ab7013ccc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbusiness-logic-allows-any-user-to-be-blocked-from-creating-an-account-6a7ab7013ccc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6a7ab7013ccc---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6a7ab7013ccc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Business logic allows any user to be blocked from creating an account

[![JEETPAL](https://miro.medium.com/v2/resize:fill:64:64/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---byline--6a7ab7013ccc---------------------------------------)

[JEETPAL](https://jeetpal2007.medium.com/?source=post_page---byline--6a7ab7013ccc---------------------------------------)

2 min read

·

Jun 7, 2025

--

3

Share

[**FREE READ**](https://medium.com/%40jeetpal2007/business-logic-allows-any-user-to-be-blocked-from-creating-an-account-6a7ab7013ccc?sk=c198fab2e073fe475a848b74e3d9371b)

Hello

Today, I will share with you how a Business logic allows me to block any User from creating account

Press enter or click to view image in full size

![]()

Image from internet

The testing started with one of the programs, I decided to hunt there and started with some recon and subdomain enumeration.

Till the `Subfinder` finishes, I decided to hunt on the main target.com, and I started my Burp Suite and scrolled through the whole site. I tested a few vulnerabilities like SQLi, ATO. Still, I didn’t find anything, so I just went to the profile to check the if any vulnerability is there While checking the site I Found we can change the email so new email where the new email isn’t verify at that time so I put a random mail and tried to create an account with that new mail and exactly what you think I got error

```
Email already exists in the database
```

I decided to reset the password. If I can, I will reset the link, but here, since the mail is not verified, the link is not sent to the user even after several tries. So I decided to report this low-hanging Vulnerability and created a report to submit it, and after submitting it, I got the notification in just 2 hours.

It got a duplicate (2 days late) of the issue, which is triaged in status

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6a7ab7013ccc---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6a7ab7013ccc---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--6a7ab7013ccc---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--6a7ab7013ccc---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--6a7ab7013ccc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![JEETPAL](https://miro.medium.com/v2/resize:fill:96:96/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--6a7ab7013ccc---------------------------------------)

[![JEETPAL](https://miro.medium.com/v2/resize:fill:128:128/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--6a7ab7013ccc---------------------------------------)

[## Written by JEETPAL](https://jeetpal2007.medium.com/?source=post_page---post_author_info--6a7ab7013ccc---------------------------------------)

[2.3K followers](https://jeetpal2007.medium.com/followers?source=post_page---post_author_info--6a7ab7013ccc---------------------------------------)

·[3 following](https://medium.com/%40jeetpal2007/following?source=post_page---post_author_info--6a7ab7013ccc---------------------------------------)

A security researcher,Auditor Web3 & Developer Connect me on social media via <https://linktr.ee/jeetpal2007> query:jeetpal2007@gmail.com

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----6a7ab7013ccc---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----6a7ab7013ccc---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----6a7ab7013ccc---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----6a7ab7013ccc---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----6a7ab7013ccc---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----6a7ab7013ccc---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----6a7ab7013ccc---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----6a7ab7013ccc---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----6a7ab7013ccc---------------------------------------)