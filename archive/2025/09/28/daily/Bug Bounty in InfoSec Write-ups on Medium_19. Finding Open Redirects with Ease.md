---
title: 19. Finding Open Redirects with Ease
url: https://infosecwriteups.com/19-finding-open-redirects-with-ease-0cc59a41702c?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-28
fetch_date: 2025-10-02T20:49:14.163501
---

# 19. Finding Open Redirects with Ease

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F0cc59a41702c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F19-finding-open-redirects-with-ease-0cc59a41702c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F19-finding-open-redirects-with-ease-0cc59a41702c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-0cc59a41702c---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-0cc59a41702c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 19. Finding Open Redirects with Ease

## From parameter to payload: a step-by-step roadmap to uncovering open redirects

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:64:64/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--0cc59a41702c---------------------------------------)

[Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--0cc59a41702c---------------------------------------)

6 min read

·

6 days ago

--

Share

🔐Free Article [Link](https://medium.com/%40kumawatabhijeet2002/19-finding-open-redirects-with-ease-0cc59a41702c?sk=6d84c58f18961a3dab8182cc0e5bcf4f)

> “Small URL flaws make big doors — a single unchecked redirect can open an empire of phishing.”

Press enter or click to view image in full size

![]()

Created by Gemini

Hey hackers 👋

I’m **Abhijeet Kumawat**, a passionate cybersecurity enthusiast, bug bounty hunter, and someone who **started with literally zero technical background.**

This write-up is the **fourth** **part of my series: “Bug Bounty from Scratch”**, where I’ll be posting **25+ deep-dive stories** on everything you need to know to start and succeed in the world of ethical hacking.

> *“And the best part? Everything I share is something I wish — — — — — someone told me when I was starting.” — — — —*

### Tired of reading theoretical vulnerability guides that leave you more confused than when you started?

### Me too. This isn’t one of those. This is a practical, step-by-step blueprint for consistently finding Open Redirect…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0cc59a41702c---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0cc59a41702c---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--0cc59a41702c---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--0cc59a41702c---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--0cc59a41702c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:96:96/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--0cc59a41702c---------------------------------------)

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:128:128/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--0cc59a41702c---------------------------------------)

[## Written by Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--0cc59a41702c---------------------------------------)

[2.3K followers](https://medium.com/%40kumawatabhijeet2002/followers?source=post_page---post_author_info--0cc59a41702c---------------------------------------)

·[33 following](https://medium.com/%40kumawatabhijeet2002/following?source=post_page---post_author_info--0cc59a41702c---------------------------------------)

Radhe Radhe ✨ || Security Researcher || Bug Hunter || Web Application Penetration Tester || Ethical Hacker ||

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----0cc59a41702c---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----0cc59a41702c---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----0cc59a41702c---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----0cc59a41702c---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----0cc59a41702c---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----0cc59a41702c---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----0cc59a41702c---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----0cc59a41702c---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----0cc59a41702c---------------------------------------)