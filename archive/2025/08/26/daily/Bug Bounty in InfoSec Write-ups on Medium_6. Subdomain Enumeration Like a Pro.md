---
title: 6. Subdomain Enumeration Like a Pro
url: https://infosecwriteups.com/6-subdomain-enumeration-like-a-pro-8461c8a92e25?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-26
fetch_date: 2025-10-07T00:47:43.349316
---

# 6. Subdomain Enumeration Like a Pro

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8461c8a92e25&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F6-subdomain-enumeration-like-a-pro-8461c8a92e25&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F6-subdomain-enumeration-like-a-pro-8461c8a92e25&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8461c8a92e25---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8461c8a92e25---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 6. Subdomain Enumeration Like a Pro

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:64:64/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--8461c8a92e25---------------------------------------)

[Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--8461c8a92e25---------------------------------------)

7 min read

·

Aug 21, 2025

--

7

Share

🔐Free Article [Link](https://medium.com/%40kumawatabhijeet2002/6-subdomain-enumeration-like-a-pro-8461c8a92e25?sk=3e042b2ae13a709736f861348a8b6966).

> “Subdomains are like doors — the main entrance may be locked, but sometimes the side doors are wide open.”

Press enter or click to view image in full size

![]()

Created by Gemini

Hey hackers 👋

I’m **Abhijeet Kumawat**, a passionate cybersecurity enthusiast, bug bounty hunter, and someone who **started with literally zero technical background.**

This write-up is the **fourth** **part of my series: “Bug Bounty from Scratch”**, where I’ll be posting **25+ deep-dive stories** on everything you need to know to start and succeed in the world of ethical hacking.

![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:40:40/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)

[Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page-----8461c8a92e25---------------------------------------)

## Bug Bounty from Scratch Series #1 to #25

[View list](https://medium.com/%40kumawatabhijeet2002/list/bug-bounty-from-scratch-series-1-to-25-b594b64abc45?source=post_page-----8461c8a92e25---------------------------------------)

17 stories

![](https://miro.medium.com/v2/resize:fill:388:388/1*pTZRFheNJs776YoUVPbOcw.png)

![](https://miro.medium.com/v2/resize:fill:388:388/1*EjJJMjMwPDdKeDpSOrJKuQ.png)

![](https://miro.medium.com/v2/resize:fill:388:388/1*HDyXVmPUzOjahm0FtQ-2_g.png)

> “And the best part? Everything I share is something I wish — — — — — someone told me when I was starting.” — — — —

### 📝 **Note from Me**

> I want to sincerely apologize for being inactive these past weeks. Unfortunately, my grandfather passed away, and I was going through a phase of depression and trauma. It took me some time to process…

--

--

7

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8461c8a92e25---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8461c8a92e25---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--8461c8a92e25---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--8461c8a92e25---------------------------------------)

·[Last published 4 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--8461c8a92e25---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:96:96/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--8461c8a92e25---------------------------------------)

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:128:128/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--8461c8a92e25---------------------------------------)

[## Written by Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--8461c8a92e25---------------------------------------)

[2.4K followers](https://medium.com/%40kumawatabhijeet2002/followers?source=post_page---post_author_info--8461c8a92e25---------------------------------------)

·[33 following](https://medium.com/%40kumawatabhijeet2002/following?source=post_page---post_author_info--8461c8a92e25---------------------------------------)

Radhe Radhe ✨ || Security Researcher || Bug Hunter || Web Application Penetration Tester || Ethical Hacker ||

## Responses (7)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----8461c8a92e25---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----8461c8a92e25---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----8461c8a92e25---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----8461c8a92e25---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----8461c8a92e25---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----8461c8a92e25---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----8461c8a92e25---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----8461c8a92e25---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----8461c8a92e25---------------------------------------)