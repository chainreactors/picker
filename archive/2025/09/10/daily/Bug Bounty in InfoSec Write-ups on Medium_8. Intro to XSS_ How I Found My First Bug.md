---
title: 8. Intro to XSS: How I Found My First Bug
url: https://infosecwriteups.com/8-intro-to-xss-how-i-found-my-first-bug-0046a4dbec4b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-10
fetch_date: 2025-10-02T19:54:02.191115
---

# 8. Intro to XSS: How I Found My First Bug

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F0046a4dbec4b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F8-intro-to-xss-how-i-found-my-first-bug-0046a4dbec4b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F8-intro-to-xss-how-i-found-my-first-bug-0046a4dbec4b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-0046a4dbec4b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-0046a4dbec4b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 8. Intro to XSS: How I Found My First Bug

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:64:64/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--0046a4dbec4b---------------------------------------)

[Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--0046a4dbec4b---------------------------------------)

7 min read

·

Aug 26, 2025

--

3

Share

🔐Free Article [Link](https://medium.com/%40kumawatabhijeet2002/8-intro-to-xss-how-i-found-my-first-bug-0046a4dbec4b?sk=3b9030ef1e7df9fe772e8deeb1fe7297).

> “XSS is not just about popping an alert box — it’s about hijacking trust, one script at a time.”

Press enter or click to view image in full size

![]()

Created by Gemini

Hey hackers 👋

I’m **Abhijeet Kumawat**, a passionate cybersecurity enthusiast, bug bounty hunter, and someone who **started with literally zero technical background.**

This write-up is the **fourth** **part of my series: “Bug Bounty from Scratch”**, where I’ll be posting **25+ deep-dive stories** on everything you need to know to start and succeed in the world of ethical hacking.

> “And the best part? Everything I share is something I wish — — — — — someone told me when I was starting.” — — — —

![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:40:40/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)

[Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page-----0046a4dbec4b---------------------------------------)

## Bug Bounty from Scratch Series #1 to #25

[View list](https://medium.com/%40kumawatabhijeet2002/list/bug-bounty-from-scratch-series-1-to-25-b594b64abc45?source=post_page-----0046a4dbec4b---------------------------------------)

17 stories

![](https://miro.medium.com/v2/resize:fill:388:388/1*pTZRFheNJs776YoUVPbOcw.png)

![](https://miro.medium.com/v2/resize:fill:388:388/1*EjJJMjMwPDdKeDpSOrJKuQ.png)

![](https://miro.medium.com/v2/resize:fill:388:388/1*HDyXVmPUzOjahm0FtQ-2_g.png)

## My First Encounter with XSS (A Story)

I still remember the night I found my first **XSS bug**. I was starting bug bounty, with Burp Suite, caffeine, and a stubborn mindset.

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0046a4dbec4b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0046a4dbec4b---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--0046a4dbec4b---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--0046a4dbec4b---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--0046a4dbec4b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:96:96/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--0046a4dbec4b---------------------------------------)

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:128:128/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--0046a4dbec4b---------------------------------------)

[## Written by Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--0046a4dbec4b---------------------------------------)

[2.3K followers](https://medium.com/%40kumawatabhijeet2002/followers?source=post_page---post_author_info--0046a4dbec4b---------------------------------------)

·[33 following](https://medium.com/%40kumawatabhijeet2002/following?source=post_page---post_author_info--0046a4dbec4b---------------------------------------)

Radhe Radhe ✨ || Security Researcher || Bug Hunter || Web Application Penetration Tester || Ethical Hacker ||

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----0046a4dbec4b---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----0046a4dbec4b---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----0046a4dbec4b---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----0046a4dbec4b---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----0046a4dbec4b---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----0046a4dbec4b---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----0046a4dbec4b---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----0046a4dbec4b---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----0046a4dbec4b---------------------------------------)