---
title: From User Enumeration to PII Exposure: Chaining Two APIs Into a $2,000 Bug
url: https://infosecwriteups.com/from-user-enumeration-to-pii-exposure-chaining-two-apis-into-a-2-000-bug-adb9ed54ab30?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-18
fetch_date: 2026-07-19T05:01:49.265238
---

# From User Enumeration to PII Exposure: Chaining Two APIs Into a $2,000 Bug

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-user-enumeration-to-pii-exposure-chaining-two-apis-into-a-2-000-bug-adb9ed54ab30&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-user-enumeration-to-pii-exposure-chaining-two-apis-into-a-2-000-bug-adb9ed54ab30&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-adb9ed54ab30---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-adb9ed54ab30---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

Cybersecurity

Api Security

Bug Bounty

Penetration Testing

Broken Access Control

# From User Enumeration to PII Exposure: Chaining Two APIs Into a $2,000 Bug

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:64:64/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---byline--adb9ed54ab30---------------------------------------)

[Ehtesham Ul Haq](https://ehteshamulhaq198.medium.com/?source=post_page---byline--adb9ed54ab30---------------------------------------)

5 min read

·

5 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dadb9ed54ab30&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-user-enumeration-to-pii-exposure-chaining-two-apis-into-a-2-000-bug-adb9ed54ab30&source=---header_actions--adb9ed54ab30---------------------post_audio_button------------------)

Share

Free Article Link: [Click for free!](https://medium.com/%40ehteshamulhaq198/from-user-enumeration-to-pii-exposure-chaining-two-apis-into-a-2-000-bug-adb9ed54ab30?sk=e894290830a0b49da7eb558af5f35c89)

Press enter or click to view image in full size

![]()

One of the biggest mistakes developers make is thinking that if two API endpoints are individually harmless, using them together will also be harmless.

Unfortunately, that isn’t always true.

During one of my recent security assessments on **target.com**, I came across what initially looked like a simple user search feature inside the company’s Academy platform. At first glance, there wasn’t anything particularly exciting about it. It behaved exactly as I expected a messaging feature to behave.

Or so I thought.

As I spent more time understanding how the application worked, that seemingly harmless feature turned into a chained **Broken Access Control** vulnerability that allowed a low-privileged user to enumerate platform users and expose sensitive personal information at scale.

This eventually resulted in a **$2,000 bounty**, but more importantly, it reminded me why understanding how APIs interact is often more valuable than looking at them individually.

## Looking Beyond the First Request

When I’m testing an application, I rarely stop after finding a single interesting response.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--adb9ed54ab30---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--adb9ed54ab30---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--adb9ed54ab30---------------------------------------)

[87K followers](/followers?source=post_page---post_publication_info--adb9ed54ab30---------------------------------------)

·[Last published 19 hours ago](/device-code-phishing-how-attackers-abuse-microsofts-legitimate-authentication-page-without-cfa189643f45?source=post_page---post_publication_info--adb9ed54ab30---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:96:96/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--adb9ed54ab30---------------------------------------)

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:128:128/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--adb9ed54ab30---------------------------------------)

[## Written by Ehtesham Ul Haq](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--adb9ed54ab30---------------------------------------)

[595 followers](https://ehteshamulhaq198.medium.com/followers?source=post_page---post_author_info--adb9ed54ab30---------------------------------------)

·[96 following](https://medium.com/%40ehteshamulhaq198/following?source=post_page---post_author_info--adb9ed54ab30---------------------------------------)

Penetration Tester & Bug Bounty Hunter focused on finding vulnerabilities and helping organizations stay ahead of cyber threats.

[Help](https://help.medium.com/hc/en-us?source=post_page-----adb9ed54ab30---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----adb9ed54ab30---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----adb9ed54ab30---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----adb9ed54ab30---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----adb9ed54ab30---------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----adb9ed54ab30---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----adb9ed54ab30---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----adb9ed54ab30---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----adb9ed54ab30---------------------------------------)