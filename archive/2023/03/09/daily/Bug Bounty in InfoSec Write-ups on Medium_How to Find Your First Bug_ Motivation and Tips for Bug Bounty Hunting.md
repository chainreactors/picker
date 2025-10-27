---
title: How to Find Your First Bug: Motivation and Tips for Bug Bounty Hunting
url: https://infosecwriteups.com/how-to-find-your-first-bug-motivation-and-tips-for-bug-bounty-hunting-5e7343066d0c?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-09
fetch_date: 2025-10-04T09:00:51.261078
---

# How to Find Your First Bug: Motivation and Tips for Bug Bounty Hunting

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F5e7343066d0c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-find-your-first-bug-motivation-and-tips-for-bug-bounty-hunting-5e7343066d0c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-find-your-first-bug-motivation-and-tips-for-bug-bounty-hunting-5e7343066d0c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-5e7343066d0c---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-5e7343066d0c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How to Find Your First Bug: Motivation and Tips for Bug Bounty Hunting

[![Anton (therceman)](https://miro.medium.com/v2/resize:fill:64:64/1*ya4CrhcriQRsR6QTK_3FJg.png)](https://therceman.medium.com/?source=post_page---byline--5e7343066d0c---------------------------------------)

[Anton (therceman)](https://therceman.medium.com/?source=post_page---byline--5e7343066d0c---------------------------------------)

3 min read

·

Mar 5, 2023

--

5

Share

Press enter or click to view image in full size

![]()

Have you recently entered the world of bug bounty hunting and are having trouble locating your first bug?

Don’t worry, you’re not alone. It’s a common challenge that requires persistence and dedication. In this article, I have prepared some helpful tips to guide you on your bug bounty journey.

First and foremost, it’s essential to take your time to research the application. Don’t rush directly into testing bugs. Instead, take some time to register on the app, look around, and see if you can create new users with different roles, upload any docs, export something into PDF, or call external services using webhooks.

Just play with the app like a regular user, and start questioning yourself:

* What will happen if a regular user can access this admin section?
* Can a non-admin user view this secret doc?
* Can a user upload non-basic doc types, such as PHP files in a PHP application?
* Is it possible to inject HTML tags into exported PDFs, and if so, is it possible to read internal files using an <iframe> tag?
* Is it possible to call localhost when creating a new webhook, or even an AWS metadata address?
* Does the app require an old…

--

--

5

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5e7343066d0c---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5e7343066d0c---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--5e7343066d0c---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--5e7343066d0c---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--5e7343066d0c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Anton (therceman)](https://miro.medium.com/v2/resize:fill:96:96/1*ya4CrhcriQRsR6QTK_3FJg.png)](https://therceman.medium.com/?source=post_page---post_author_info--5e7343066d0c---------------------------------------)

[![Anton (therceman)](https://miro.medium.com/v2/resize:fill:128:128/1*ya4CrhcriQRsR6QTK_3FJg.png)](https://therceman.medium.com/?source=post_page---post_author_info--5e7343066d0c---------------------------------------)

[## Written by Anton (therceman)](https://therceman.medium.com/?source=post_page---post_author_info--5e7343066d0c---------------------------------------)

[2.1K followers](https://therceman.medium.com/followers?source=post_page---post_author_info--5e7343066d0c---------------------------------------)

·[3.9K following](https://medium.com/%40therceman/following?source=post_page---post_author_info--5e7343066d0c---------------------------------------)

💰 Bug Bounty Hunter 💻 Software Developer 🌐 [www.therceman.dev](http://www.therceman.dev)

## Responses (5)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----5e7343066d0c---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----5e7343066d0c---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----5e7343066d0c---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----5e7343066d0c---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----5e7343066d0c---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----5e7343066d0c---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----5e7343066d0c---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----5e7343066d0c---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----5e7343066d0c---------------------------------------)