---
title: OAuth and the flaws in its implementation
url: https://infosecwriteups.com/oauth-and-the-flaws-in-its-implementation-74de16f115c0?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-10-28
fetch_date: 2025-10-03T21:06:55.246525
---

# OAuth and the flaws in its implementation

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F74de16f115c0&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Foauth-and-the-flaws-in-its-implementation-74de16f115c0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Foauth-and-the-flaws-in-its-implementation-74de16f115c0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-74de16f115c0---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-74de16f115c0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# OAuth and the flaws in its implementation

[![Security Lit Limited](https://miro.medium.com/v2/resize:fill:64:64/1*yrQrISi6PlPkHrHAS2ai3g.png)](https://securitylit.medium.com/?source=post_page---byline--74de16f115c0---------------------------------------)

[Security Lit Limited](https://securitylit.medium.com/?source=post_page---byline--74de16f115c0---------------------------------------)

7 min read

·

Oct 27, 2022

--

Share

Press enter or click to view image in full size

![]()

Photo by [freestocks](https://unsplash.com/%40freestocks?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/%40freestocks?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

What is OAuth?

Open Authorization (also known as OAuth) is an open-source framework that allows you to create accounts on websites without having to create a different user account for each website. They rely on authentic third-party websites, such as Facebook or Google, to perform the authentication process for them.

It is:

1. It is used to log into websites without the need to form an account first.
2. Resource sharing is performed through this method.
3. SSO is also utilised in businesses and enterprise networks for a variety of purposes (Single Sign On)

Isn’t it intriguing to think about? But what are the options for gaining access to something without having to create an account? Let’s see how well it works out for you.

**How OAuth Works?**

Press enter or click to view image in full size

![]()

[Source](https://goteleport.com/blog/how-oauth-authentication-works/)

To simplify the work flow let’s first isolate the entities involved.

They are:

1. User (i.e., you)
2. Application that you want to access
3. Authorization Server

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--74de16f115c0---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--74de16f115c0---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--74de16f115c0---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--74de16f115c0---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--74de16f115c0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Security Lit Limited](https://miro.medium.com/v2/resize:fill:96:96/1*yrQrISi6PlPkHrHAS2ai3g.png)](https://securitylit.medium.com/?source=post_page---post_author_info--74de16f115c0---------------------------------------)

[![Security Lit Limited](https://miro.medium.com/v2/resize:fill:128:128/1*yrQrISi6PlPkHrHAS2ai3g.png)](https://securitylit.medium.com/?source=post_page---post_author_info--74de16f115c0---------------------------------------)

[## Written by Security Lit Limited](https://securitylit.medium.com/?source=post_page---post_author_info--74de16f115c0---------------------------------------)

[2K followers](https://securitylit.medium.com/followers?source=post_page---post_author_info--74de16f115c0---------------------------------------)

·[150 following](https://medium.com/%40securitylit/following?source=post_page---post_author_info--74de16f115c0---------------------------------------)

<https://securitylit.com/contact>

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----74de16f115c0---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----74de16f115c0---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----74de16f115c0---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----74de16f115c0---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----74de16f115c0---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----74de16f115c0---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----74de16f115c0---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----74de16f115c0---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----74de16f115c0---------------------------------------)