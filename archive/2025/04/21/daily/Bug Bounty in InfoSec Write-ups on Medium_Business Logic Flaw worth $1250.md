---
title: Business Logic Flaw worth $1250
url: https://infosecwriteups.com/business-logic-flaw-worth-1250-35efcd1b9af9?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-04-21
fetch_date: 2025-10-06T22:03:49.785061
---

# Business Logic Flaw worth $1250

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F35efcd1b9af9&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbusiness-logic-flaw-worth-1250-35efcd1b9af9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbusiness-logic-flaw-worth-1250-35efcd1b9af9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-35efcd1b9af9---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-35efcd1b9af9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **Business Logic Flaw worth $1250**

[![the_unlucky_guy](https://miro.medium.com/v2/resize:fill:64:64/1*6WsUIHpOpn943C_P_cdWng.jpeg)](https://vijetareigns.medium.com/?source=post_page---byline--35efcd1b9af9---------------------------------------)

[the\_unlucky\_guy](https://vijetareigns.medium.com/?source=post_page---byline--35efcd1b9af9---------------------------------------)

4 min read

·

Apr 19, 2025

--

6

Share

[FREE ARTICLE LINK](/business-logic-flaw-worth-1250-35efcd1b9af9?sk=9d91ba2d74daef2e6c0d76582bc51e09)👈

Ciao hackers, I hope you’re hacking well. In this write-up, I’m going to share a business logic flaws on a **crypto wallet** website that can lead to the takeover of any victim’s wallet account. I will be using **redacted.com** as the main domain.

The company is a crypto wallet to earn, buy, store, and stake tokens.

The front end of the application is at **app.redacted.tv** and all the backend APIs are at **api.redacted.tv.** As usual, I fired up my burp suite and started exploring the application.

I created an account on the website, to verify email an email verification code is being sent to given email address. I verified the account and on the next page, 2FA is compulsory to set up. After finishing up the registration my account is ready to use. Below is the flow of registration:

```
1. Enter Name, Email address and Password
2. Enter verification code on verify email page
3. Setup 2FA
4. Logged in to the account.
```

In the step of verification of email, I notice that the URL is `[https://app.redacted.tv/verify?email=user@gmail.com](https://app.redacted.tv/verify?email=user%40gmail.com)`. I thought, let’s open this URL in an incognito tab or another browser. After forced browsing the URL the verification page opened **without** entering password and asked for the verification code.

Press enter or click to view image in full size

![]()

--

--

6

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--35efcd1b9af9---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--35efcd1b9af9---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--35efcd1b9af9---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--35efcd1b9af9---------------------------------------)

·[Last published 1 hour ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--35efcd1b9af9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![the_unlucky_guy](https://miro.medium.com/v2/resize:fill:96:96/1*6WsUIHpOpn943C_P_cdWng.jpeg)](https://vijetareigns.medium.com/?source=post_page---post_author_info--35efcd1b9af9---------------------------------------)

[![the_unlucky_guy](https://miro.medium.com/v2/resize:fill:128:128/1*6WsUIHpOpn943C_P_cdWng.jpeg)](https://vijetareigns.medium.com/?source=post_page---post_author_info--35efcd1b9af9---------------------------------------)

[## Written by the\_unlucky\_guy](https://vijetareigns.medium.com/?source=post_page---post_author_info--35efcd1b9af9---------------------------------------)

[1.4K followers](https://vijetareigns.medium.com/followers?source=post_page---post_author_info--35efcd1b9af9---------------------------------------)

·[26 following](https://medium.com/%40vijetareigns/following?source=post_page---post_author_info--35efcd1b9af9---------------------------------------)

Security Engineer | Never Forgive Never Forget

## Responses (6)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----35efcd1b9af9---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----35efcd1b9af9---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----35efcd1b9af9---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----35efcd1b9af9---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----35efcd1b9af9---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----35efcd1b9af9---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----35efcd1b9af9---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----35efcd1b9af9---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----35efcd1b9af9---------------------------------------)