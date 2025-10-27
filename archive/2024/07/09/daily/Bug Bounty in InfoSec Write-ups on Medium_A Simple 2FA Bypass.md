---
title: A Simple 2FA Bypass
url: https://infosecwriteups.com/a-simple-2fa-bypass-43c8af9006ec?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-07-09
fetch_date: 2025-10-06T17:43:00.619392
---

# A Simple 2FA Bypass

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F43c8af9006ec&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fa-simple-2fa-bypass-43c8af9006ec&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fa-simple-2fa-bypass-43c8af9006ec&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-43c8af9006ec---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-43c8af9006ec---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# A Simple 2FA Bypass

[![hackerdevil](https://miro.medium.com/v2/resize:fill:64:64/1*sVg7V08AyUPzAzA_Hx-UYg.png)](https://devilwrites.medium.com/?source=post_page---byline--43c8af9006ec---------------------------------------)

[hackerdevil](https://devilwrites.medium.com/?source=post_page---byline--43c8af9006ec---------------------------------------)

2 min read

·

Jul 6, 2024

--

4

Listen

Share

2FA bypass through response manipulation

Two-Factor Authentication (2FA) serves as a robust shield against unauthorized access. However, during a recent engagement in a RVDP, I found a critical vulnerability that allows an attacker to bypass 2FA using response manipulation.

Press enter or click to view image in full size

![]()

[Bug-bounty (zoom.us)](https://blog.zoom.us/wp-content/uploads/2022/03/Bug-bounty.png)

Below are the steps that led to bypass 2FA:

1. I logged-in as a normal user and enabled 2FA for that account
2. Next, I logged out and logged-in again with login credentials
3. Then I entered the wrong OTP and captured that response to that request as shown below

![]()

Wrong OTP Response

4. The response had 401 Unauthorized and the body had wrong OTP message

5. I manipulated the response code to 200 OK and replaced the body with the content of valid OTP

![]()

Manipulated Response

6. That’s it, with this I was able to bypass the 2FA of that account.

And to confirm if it has really bypassed the 2FA, after logging in I disabled the 2FA, logged out and then logged in again and this time it didn’t asked for a 2FA code to be entered.

[## hackerdevil

### Buy me some coffee to help write more of such content!!

buymeacoffee.com](https://buymeacoffee.com/devil09?source=post_page-----43c8af9006ec---------------------------------------)

Stay safe, stay informed, and keep coming back for more empowering insights.

Thank You for reading. Knowledge is power, so keep gaining!!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----43c8af9006ec---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----43c8af9006ec---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----43c8af9006ec---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----43c8af9006ec---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----43c8af9006ec---------------------------------------)

--

--

4

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--43c8af9006ec---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--43c8af9006ec---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--43c8af9006ec---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--43c8af9006ec---------------------------------------)

·[Last published 2 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--43c8af9006ec---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![hackerdevil](https://miro.medium.com/v2/resize:fill:96:96/1*sVg7V08AyUPzAzA_Hx-UYg.png)](https://devilwrites.medium.com/?source=post_page---post_author_info--43c8af9006ec---------------------------------------)

[![hackerdevil](https://miro.medium.com/v2/resize:fill:128:128/1*sVg7V08AyUPzAzA_Hx-UYg.png)](https://devilwrites.medium.com/?source=post_page---post_author_info--43c8af9006ec---------------------------------------)

[## Written by hackerdevil](https://devilwrites.medium.com/?source=post_page---post_author_info--43c8af9006ec---------------------------------------)

[193 followers](https://devilwrites.medium.com/followers?source=post_page---post_author_info--43c8af9006ec---------------------------------------)

·[51 following](https://medium.com/%40devilwrites/following?source=post_page---post_author_info--43c8af9006ec---------------------------------------)

CRTP • CEH • VAPT • Foodie • Infosec Writer

## Responses (4)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----43c8af9006ec---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----43c8af9006ec---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----43c8af9006ec---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----43c8af9006ec---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----43c8af9006ec---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----43c8af9006ec---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----43c8af9006ec---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----43c8af9006ec---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----43c8af9006ec---------------------------------------)