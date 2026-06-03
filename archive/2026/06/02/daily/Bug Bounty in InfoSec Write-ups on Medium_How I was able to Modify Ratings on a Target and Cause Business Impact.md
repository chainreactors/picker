---
title: How I was able to Modify Ratings on a Target and Cause Business Impact
url: https://infosecwriteups.com/how-i-was-able-to-modify-ratings-on-a-target-and-cause-business-impact-f690fa0695b8?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-02
fetch_date: 2026-06-03T06:45:21.656605
---

# How I was able to Modify Ratings on a Target and Cause Business Impact

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-was-able-to-modify-ratings-on-a-target-and-cause-business-impact-f690fa0695b8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-was-able-to-modify-ratings-on-a-target-and-cause-business-impact-f690fa0695b8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f690fa0695b8---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f690fa0695b8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

# How I was able to Modify Ratings on a Target and Cause Business Impact

[![RivuDon](https://miro.medium.com/v2/resize:fill:64:64/1*mx_9qWzpuFvMAzbCHJeWsA.jpeg)](https://rivudon.medium.com/?source=post_page---byline--f690fa0695b8---------------------------------------)

[RivuDon](https://rivudon.medium.com/?source=post_page---byline--f690fa0695b8---------------------------------------)

6 min read

·

1 day ago

--

2

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Df690fa0695b8&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-was-able-to-modify-ratings-on-a-target-and-cause-business-impact-f690fa0695b8&source=---header_actions--f690fa0695b8---------------------post_audio_button------------------)

Share

Learn how I found this interesting bug

Press enter or click to view image in full size

![]()

📩 Read for Free [**CLICK HERE.**](https://rivudon.medium.com/f690fa0695b8?sk=55f927318c10fb599411761106a8aa2f)

> *Hi, I’m* ***Rivek Raj Tamang (RivuDon)****, a Security Researcher, Bug Hunter, and Ethical Hacker with a Master’s in Cybersecurity, a Certified Ethical Hacker from Sikkim, India. I have secured numerous companies, received bounties, swags, Hall of Fames mentions, Letter of Appreciation / Recognition, CVEs and more.*
>
> *Feel free to connect with me! You can find out more about me on my* [***LinkedIn****,*](https://www.linkedin.com/in/rivektamang/) *I am active there.*

**Hi readers,** this is a detailed write-up on **how I was able to manipulate ratings on a target and demonstrate real business impact.** It was actually a really interesting and fun bug to discover.

> **What if you could change the overall rating of a google review?**
>
> **for example, if it had a rating of 4.5/5 in the first place and after manipulation you could decrease the rating and lower the overall rating to 1/5.**

Without further ado, let’s get started!

## The Hunt

One fine day, while browsing LinkedIn like any other random day, I saw a post of someone showing a swag they received from a target. It was a tech-based platform that offered coding/programming exams as a…

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f690fa0695b8---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f690fa0695b8---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--f690fa0695b8---------------------------------------)

[86K followers](/followers?source=post_page---post_publication_info--f690fa0695b8---------------------------------------)

·[Last published 1 day ago](/how-i-was-able-to-modify-ratings-on-a-target-and-cause-business-impact-f690fa0695b8?source=post_page---post_publication_info--f690fa0695b8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![RivuDon](https://miro.medium.com/v2/resize:fill:96:96/1*mx_9qWzpuFvMAzbCHJeWsA.jpeg)](https://rivudon.medium.com/?source=post_page---post_author_info--f690fa0695b8---------------------------------------)

[![RivuDon](https://miro.medium.com/v2/resize:fill:128:128/1*mx_9qWzpuFvMAzbCHJeWsA.jpeg)](https://rivudon.medium.com/?source=post_page---post_author_info--f690fa0695b8---------------------------------------)

[## Written by RivuDon](https://rivudon.medium.com/?source=post_page---post_author_info--f690fa0695b8---------------------------------------)

[989 followers](https://rivudon.medium.com/followers?source=post_page---post_author_info--f690fa0695b8---------------------------------------)

·[115 following](https://medium.com/%40rivudon/following?source=post_page---post_author_info--f690fa0695b8---------------------------------------)

Security Researcher | Bug Hunter | Hacker | Tech | Lifestyle LinkedIn: @RivekRajTamang

[Help](https://help.medium.com/hc/en-us?source=post_page-----f690fa0695b8---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----f690fa0695b8---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----f690fa0695b8---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----f690fa0695b8---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----f690fa0695b8---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----f690fa0695b8---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----f690fa0695b8---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----f690fa0695b8---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----f690fa0695b8---------------------------------------)