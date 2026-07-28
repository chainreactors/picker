---
title: How a Simple Profile Update Led to Cross-Tenant Data Exposure
url: https://infosecwriteups.com/how-a-simple-profile-update-led-to-cross-tenant-data-exposure-b945842678e2?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-27
fetch_date: 2026-07-28T04:58:49.303218
---

# How a Simple Profile Update Led to Cross-Tenant Data Exposure

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-a-simple-profile-update-led-to-cross-tenant-data-exposure-b945842678e2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-a-simple-profile-update-led-to-cross-tenant-data-exposure-b945842678e2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b945842678e2---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b945842678e2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

# How a Simple Profile Update Led to Cross-Tenant Data Exposure

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:64:64/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---byline--b945842678e2---------------------------------------)

[Ehtesham Ul Haq](https://ehteshamulhaq198.medium.com/?source=post_page---byline--b945842678e2---------------------------------------)

5 min read

·

5 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Db945842678e2&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-a-simple-profile-update-led-to-cross-tenant-data-exposure-b945842678e2&source=---header_actions--b945842678e2---------------------post_audio_button------------------)

Share

Free Article Link: [Click for free!](https://ehteshamulhaq198.medium.com/how-a-simple-profile-update-led-to-cross-tenant-data-exposure-b945842678e2?sk=0d91e1a19ce25b7714531f9aaacc1426)

Press enter or click to view image in full size

![]()

For responsible disclosure reasons, I’ll refer to the affected application as **target.com** throughout this article. The technical details have been preserved, but the company’s identity and sensitive implementation details have been intentionally withheld.

One of the biggest misconceptions in application security is that **Broken Access Control** only exists around admin panels or sensitive endpoints.

In reality, some of the most impactful vulnerabilities begin in places almost nobody pays attention to.

During one of my recent security assessments on **target.com**, I was exploring what looked like a completely ordinary account settings page. Like most profile pages, it allowed users to update their personal information and preferences. Nothing about it immediately suggested that it could lead to a security issue.

As I spent more time understanding how the application handled profile updates, that seemingly harmless feature turned into a **cross-tenant Broken Access Control vulnerability** that allowed an authenticated user to associate their account with other organizations and disclose sensitive metadata belonging to completely different customers.

The report was acknowledged by the security team within just six hours of submission, but more importantly, it reinforced another lesson I’ve learned repeatedly throughout bug hunting:

**Sometimes the most dangerous vulnerabilities are hiding inside the features users interact with every day.**

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b945842678e2---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b945842678e2---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b945842678e2---------------------------------------)

[87K followers](/followers?source=post_page---post_publication_info--b945842678e2---------------------------------------)

·[Last published 1 day ago](/unauthenticated-disclosure-of-a-b-test-data-in-convert-pro-how-two-forgotten-ajax-endpoints-dbefc9c3e440?source=post_page---post_publication_info--b945842678e2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:96:96/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--b945842678e2---------------------------------------)

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:128:128/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--b945842678e2---------------------------------------)

[## Written by Ehtesham Ul Haq](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--b945842678e2---------------------------------------)

[612 followers](https://ehteshamulhaq198.medium.com/followers?source=post_page---post_author_info--b945842678e2---------------------------------------)

·[95 following](https://medium.com/%40ehteshamulhaq198/following?source=post_page---post_author_info--b945842678e2---------------------------------------)

Penetration Tester & Bug Bounty Hunter focused on finding vulnerabilities and helping organizations stay ahead of cyber threats.

[Help](https://help.medium.com/hc/en-us?source=post_page-----b945842678e2---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----b945842678e2---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----b945842678e2---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----b945842678e2---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----b945842678e2---------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----b945842678e2---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----b945842678e2---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----b945842678e2---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----b945842678e2---------------------------------------)