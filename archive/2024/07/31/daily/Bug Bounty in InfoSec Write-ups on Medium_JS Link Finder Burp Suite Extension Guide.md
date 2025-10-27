---
title: JS Link Finder Burp Suite Extension Guide
url: https://infosecwriteups.com/js-link-finder-burp-suite-extension-guide-e4809a6da268?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-07-31
fetch_date: 2025-10-06T17:42:13.807284
---

# JS Link Finder Burp Suite Extension Guide

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe4809a6da268&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fjs-link-finder-burp-suite-extension-guide-e4809a6da268&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fjs-link-finder-burp-suite-extension-guide-e4809a6da268&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e4809a6da268---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e4809a6da268---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# JS Link Finder Burp Suite Extension Guide

## Improve your bug bounty hunting, pentesting, and appsec skills with the JS Link Finder Burp Suite Extension. Discover hidden endpoints and test for vulnerabilities such as authentication bypass, broken access control, XSS, and SQLi.

[![Mike Takahashi (TakSec)](https://miro.medium.com/v2/resize:fill:64:64/1*oeaksoi-GPEkdXjmR0uMFA.jpeg)](https://taksec.medium.com/?source=post_page---byline--e4809a6da268---------------------------------------)

[Mike Takahashi (TakSec)](https://taksec.medium.com/?source=post_page---byline--e4809a6da268---------------------------------------)

4 min read

·

Jul 29, 2024

--

Share

Press enter or click to view image in full size

![]()

## Why JS Link Finder?

It’s simple. This tool scans JavaScript files to uncover hidden endpoints and parameters that could be your ticket to discovering unauthenticated access points, broken access control vulnerabilities, and even injections. 🚀

## Getting Started: Installing JS Link Finder

First things first, let’s get this bad boy installed.

1. **Open Burp Suite**: Fire up Burp Suite. (Duh! 😜)
2. **Navigate to BApp Store**: Head over to the Extender tab and hit the BApp Store.
3. **Search & Install**: Look for “JS Link Finder” and smash that install button. Done and dusted! 🛠️

Press enter or click to view image in full size

![]()

## Walking the Site: Scouting for Gold

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e4809a6da268---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e4809a6da268---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e4809a6da268---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e4809a6da268---------------------------------------)

·[Last published 2 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--e4809a6da268---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Mike Takahashi (TakSec)](https://miro.medium.com/v2/resize:fill:96:96/1*oeaksoi-GPEkdXjmR0uMFA.jpeg)](https://taksec.medium.com/?source=post_page---post_author_info--e4809a6da268---------------------------------------)

[![Mike Takahashi (TakSec)](https://miro.medium.com/v2/resize:fill:128:128/1*oeaksoi-GPEkdXjmR0uMFA.jpeg)](https://taksec.medium.com/?source=post_page---post_author_info--e4809a6da268---------------------------------------)

[## Written by Mike Takahashi (TakSec)](https://taksec.medium.com/?source=post_page---post_author_info--e4809a6da268---------------------------------------)

[2.3K followers](https://taksec.medium.com/followers?source=post_page---post_author_info--e4809a6da268---------------------------------------)

·[768 following](https://medium.com/%40taksec/following?source=post_page---post_author_info--e4809a6da268---------------------------------------)

Pentester | Bug Bounty Hunter | AI Red Team <https://twitter.com/TakSec>

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----e4809a6da268---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----e4809a6da268---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----e4809a6da268---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----e4809a6da268---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----e4809a6da268---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----e4809a6da268---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----e4809a6da268---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----e4809a6da268---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----e4809a6da268---------------------------------------)