---
title: The Bug Behind the Delete Button: How I Found a Critical IDOR
url: https://infosecwriteups.com/the-bug-behind-the-delete-button-how-i-found-a-critical-idor-2ea938226f7b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-21
fetch_date: 2025-10-02T20:28:31.390706
---

# The Bug Behind the Delete Button: How I Found a Critical IDOR

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2ea938226f7b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-bug-behind-the-delete-button-how-i-found-a-critical-idor-2ea938226f7b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-bug-behind-the-delete-button-how-i-found-a-critical-idor-2ea938226f7b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2ea938226f7b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2ea938226f7b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# The Bug Behind the Delete Button: How I Found a Critical IDOR

[![Antonio Rivera Poblete](https://miro.medium.com/v2/resize:fill:64:64/1*siOJ2ehEhoi5wuXduCKMPA.jpeg)](https://medium.com/%40anripo2006?source=post_page---byline--2ea938226f7b---------------------------------------)

[Antonio Rivera Poblete](https://medium.com/%40anripo2006?source=post_page---byline--2ea938226f7b---------------------------------------)

2 min read

·

Sep 14, 2025

--

1

Listen

Share

![]()

## 👨‍💻 Introduction

*Hi, I’m* ***Antonio Rivera****, a Security Researcher, Bug Hunter, and Ethical Hacker. I have secured some companies, received bounties, Hall of Fame mentions* and received Letters of Appreciation and Recognition*.*

> This is the story of how I ran into a Broken Object Level Authorization (BOLA) vulnerability while poking around a web application.

## 🕵️‍♂️ The Recon Phase

The first thing I do when testing a new application is create a few accounts. It helps me see how the app behaves from different perspectives.

I spent some time exploring forms, menus, and pages to understand how data moved between users.

Once I understood the app, I started testing for IDORs on my own account. At first, nothing happened. I tried other tests, like race conditions and business logic checks, but still, nothing produced results.

## 💥 The IDOR

Then, while reviewing some requests, one **caught my attention**:

* *POST /restapi/soa2/ID/userDelete*

```
{"operation":"userDelete","params":{"uid":"MyID","companyId":"clapthispost1234"}}
```

Press enter or click to view image in full size

![]()

It looked ordinary, but I decided to test it with a token from another account. To my surprise, it worked, That was when I realized an **IDOR** existed.

Press enter or click to view image in full size

![]()

## 🏁 The Lesson

This reinforced a simple truth: **careful observation** and thinking like an attacker often reveal issues that automated tools miss.

## 😔Unfortunately

![]()

![]()

[Idor](https://medium.com/tag/idor?source=post_page-----2ea938226f7b---------------------------------------)

[Idor Vulnerability](https://medium.com/tag/idor-vulnerability?source=post_page-----2ea938226f7b---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----2ea938226f7b---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----2ea938226f7b---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----2ea938226f7b---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2ea938226f7b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2ea938226f7b---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--2ea938226f7b---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--2ea938226f7b---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--2ea938226f7b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Antonio Rivera Poblete](https://miro.medium.com/v2/resize:fill:96:96/1*siOJ2ehEhoi5wuXduCKMPA.jpeg)](https://medium.com/%40anripo2006?source=post_page---post_author_info--2ea938226f7b---------------------------------------)

[![Antonio Rivera Poblete](https://miro.medium.com/v2/resize:fill:128:128/1*siOJ2ehEhoi5wuXduCKMPA.jpeg)](https://medium.com/%40anripo2006?source=post_page---post_author_info--2ea938226f7b---------------------------------------)

[## Written by Antonio Rivera Poblete](https://medium.com/%40anripo2006?source=post_page---post_author_info--2ea938226f7b---------------------------------------)

[45 followers](https://medium.com/%40anripo2006/followers?source=post_page---post_author_info--2ea938226f7b---------------------------------------)

·[18 following](https://medium.com/%40anripo2006/following?source=post_page---post_author_info--2ea938226f7b---------------------------------------)

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----2ea938226f7b---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----2ea938226f7b---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----2ea938226f7b---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----2ea938226f7b---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----2ea938226f7b---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----2ea938226f7b---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----2ea938226f7b---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----2ea938226f7b---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----2ea938226f7b-----------------------------------...