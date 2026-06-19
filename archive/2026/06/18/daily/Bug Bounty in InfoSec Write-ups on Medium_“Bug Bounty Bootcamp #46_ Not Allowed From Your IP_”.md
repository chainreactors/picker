---
title: “Bug Bounty Bootcamp #46: Not Allowed From Your IP?”
url: https://infosecwriteups.com/bug-bounty-bootcamp-46-not-allowed-from-your-ip-8df1b1f96a30?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-18
fetch_date: 2026-06-19T07:07:18.175519
---

# “Bug Bounty Bootcamp #46: Not Allowed From Your IP?”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-bootcamp-46-not-allowed-from-your-ip-8df1b1f96a30&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-bootcamp-46-not-allowed-from-your-ip-8df1b1f96a30&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8df1b1f96a30---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8df1b1f96a30---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

# “Bug Bounty Bootcamp #46: Not Allowed From Your IP?”

## — How to Spoof, Brute-Force, and Mass-Assign Your Way Past Authentication Walls”

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--8df1b1f96a30---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--8df1b1f96a30---------------------------------------)

6 min read

·

3 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D8df1b1f96a30&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-bootcamp-46-not-allowed-from-your-ip-8df1b1f96a30&source=---header_actions--8df1b1f96a30---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

[Free link/ Friend Link](https://amannsharmaa.medium.com/bug-bounty-bootcamp-46-not-allowed-from-your-ip-8df1b1f96a30?sk=ee581e50216f6d9a773a19780c07f712)

Welcome back, my favorite little chaos agents. You’ve made it through weak passwords, hidden registration pages, and leaked reset tokens. Now we enter the forbidden zone: authentication systems that think they’re clever. They check your IP, they hide behind SSO, they make you wait for approval. Cute.

> ***“You can’t register here.” “Only internal IPs allowed.” “Your account is pending approval.” Yeah, yeah, we’ve heard it all before. Watch me inject myself into password reset emails, spoof internal headers, and approve my own damn account — no admin needed.***

### Today, we break all of that. We’re going to:

* Inject ourselves into password reset emails (because arrays are scary)
* Spoof `X-Forwarded-For` headers like we own the internal network
* Brute-force internal IP ranges until one lets us in
* Mass-assign `"status": "approved"` to skip the waiting list
* Poke through SSO redirects and dead hosts for hidden APIs

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8df1b1f96a30---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8df1b1f96a30---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--8df1b1f96a30---------------------------------------)

[87K followers](/followers?source=post_page---post_publication_info--8df1b1f96a30---------------------------------------)

·[Last published 1 day ago](/slort-rfi-via-php-allow-url-include-writable-scheduled-task-binary-to-administrator-offsec-pg-ac72c40761ae?source=post_page---post_publication_info--8df1b1f96a30---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--8df1b1f96a30---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--8df1b1f96a30---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--8df1b1f96a30---------------------------------------)

[1.6K followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--8df1b1f96a30---------------------------------------)

·[22 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--8df1b1f96a30---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

[Help](https://help.medium.com/hc/en-us?source=post_page-----8df1b1f96a30---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----8df1b1f96a30---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----8df1b1f96a30---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----8df1b1f96a30---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----8df1b1f96a30---------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----8df1b1f96a30---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----8df1b1f96a30---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----8df1b1f96a30---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----8df1b1f96a30---------------------------------------)