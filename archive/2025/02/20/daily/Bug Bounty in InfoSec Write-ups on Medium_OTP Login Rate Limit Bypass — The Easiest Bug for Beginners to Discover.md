---
title: OTP Login Rate Limit Bypass — The Easiest Bug for Beginners to Discover
url: https://infosecwriteups.com/otp-login-rate-limit-bypass-the-easiest-bug-for-beginners-to-discover-74cbf2432b72?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-02-20
fetch_date: 2025-10-06T20:34:32.476162
---

# OTP Login Rate Limit Bypass — The Easiest Bug for Beginners to Discover

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F74cbf2432b72&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fotp-login-rate-limit-bypass-the-easiest-bug-for-beginners-to-discover-74cbf2432b72&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fotp-login-rate-limit-bypass-the-easiest-bug-for-beginners-to-discover-74cbf2432b72&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-74cbf2432b72---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-74cbf2432b72---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **OTP Login Rate Limit Bypass — The Easiest Bug for Beginners to Discover**

[![Vivek PS](https://miro.medium.com/v2/resize:fill:64:64/1*gswVWtLbFDKYFuLKsi063g.png)](https://medium.com/%40vivekps143?source=post_page---byline--74cbf2432b72---------------------------------------)

[Vivek PS](https://medium.com/%40vivekps143?source=post_page---byline--74cbf2432b72---------------------------------------)

4 min read

·

Feb 19, 2025

--

1

Share

***My article is open to everyone; non-member readers can click*** [***this link***](/otp-login-rate-limit-bypass-the-easiest-bug-for-beginners-to-discover-74cbf2432b72?sk=a455d7662bf1301ad8c1c9a2e417daa4) ***to read the full text.***

*“This story was originally published on my previous Medium account, which was unfortunately deleted. The original post garnered significant attention, with many views and followers, and I’m republishing it here to share my journey with a new audience and reconnect with readers who may remember it*.”

## Hello friends,

Today, I’m going to share a vulnerability that might motivate beginners struggling to find their first bug. It’s a simple yet impactful issue: **OTP login rate limit bypass**. If you’re new to bug bounty, I highly recommend testing for this, as it’s easier to find than other technical vulnerabilities. Look for web applications or mobile apps that allow users to log in using OTP.

## Finding the Bug

I started by searching for Indian startup web applications and luckily found a few that used OTP-based login. This write-up is about one such case that I found in **cricheros.in** and the method I used to exploit it.

I picked the website, entered my mobile number on the login page, and requested an OTP. As expected, I received a **6-digit code** on my phone. But instead of entering the correct OTP, I deliberately entered a **wrong 6-digit number** while monitoring the network requests using Firefox’s Developer Tools.

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--74cbf2432b72---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--74cbf2432b72---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--74cbf2432b72---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--74cbf2432b72---------------------------------------)

·[Last published just now](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--74cbf2432b72---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Vivek PS](https://miro.medium.com/v2/resize:fill:96:96/1*gswVWtLbFDKYFuLKsi063g.png)](https://medium.com/%40vivekps143?source=post_page---post_author_info--74cbf2432b72---------------------------------------)

[![Vivek PS](https://miro.medium.com/v2/resize:fill:128:128/1*gswVWtLbFDKYFuLKsi063g.png)](https://medium.com/%40vivekps143?source=post_page---post_author_info--74cbf2432b72---------------------------------------)

[## Written by Vivek PS](https://medium.com/%40vivekps143?source=post_page---post_author_info--74cbf2432b72---------------------------------------)

[420 followers](https://medium.com/%40vivekps143/followers?source=post_page---post_author_info--74cbf2432b72---------------------------------------)

·[69 following](https://medium.com/%40vivekps143/following?source=post_page---post_author_info--74cbf2432b72---------------------------------------)

I’m a programmer, web security researcher and chess player, focused on innovation, learning, and creating impactful solutions for growth.

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----74cbf2432b72---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----74cbf2432b72---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----74cbf2432b72---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----74cbf2432b72---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----74cbf2432b72---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----74cbf2432b72---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----74cbf2432b72---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----74cbf2432b72---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----74cbf2432b72---------------------------------------)