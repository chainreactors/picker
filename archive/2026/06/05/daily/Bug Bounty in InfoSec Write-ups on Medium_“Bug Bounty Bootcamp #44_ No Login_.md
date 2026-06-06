---
title: “Bug Bounty Bootcamp #44: No Login?
url: https://infosecwriteups.com/bug-bounty-bootcamp-44-no-login-c3302844a47e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-05
fetch_date: 2026-06-06T05:49:33.312756
---

# “Bug Bounty Bootcamp #44: No Login?

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-bootcamp-44-no-login-c3302844a47e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-bootcamp-44-no-login-c3302844a47e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c3302844a47e---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c3302844a47e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

# “Bug Bounty Bootcamp #44: No Login? No Problem — How to Sneak Into Locked Apps Like a Digital Ninja”

## You stumble on a login page. No “Register”, no “Forgot Password”. Just two lonely text boxes staring back at you. Most hunters give up. You? You’re about to find the hidden backdoor, the secret API, or that one dev who left the keys under the mat.

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--c3302844a47e---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--c3302844a47e---------------------------------------)

5 min read

·

1 day ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dc3302844a47e&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-bootcamp-44-no-login-c3302844a47e&source=---header_actions--c3302844a47e---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

[*Friend Link/ Free Link*](https://amannsharmaa.medium.com/bug-bounty-bootcamp-44-no-login-c3302844a47e?sk=434350e403b5b20ad0e79c9dc2a4d5a9)

Welcome back, you beautiful chaos agent. You’ve made it past the easy login pages with weak passwords and default creds. But now you’re facing the wall: a login form with *zero* self-registration, *zero* password reset, and *zero* chill. It’s like the app is saying, “Go away, you’re not on the list.”

But guess what? That “list” might be hiding in plain sight — a forgotten API endpoint, a JavaScript file that accidentally leaks the registration URL, or a misconfigured OTP that lets you brute-force your way into someone else’s account.

Let’s get you inside. No invite needed.

## 1. Content Discovery: The Art of Knocking on Every Door

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c3302844a47e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c3302844a47e---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--c3302844a47e---------------------------------------)

[87K followers](/followers?source=post_page---post_publication_info--c3302844a47e---------------------------------------)

·[Last published 1 day ago](/host-network-penetration-testing-system-host-based-attacks-ctf-1-ejpt-ine-9cca24e33039?source=post_page---post_publication_info--c3302844a47e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--c3302844a47e---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--c3302844a47e---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--c3302844a47e---------------------------------------)

[1.5K followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--c3302844a47e---------------------------------------)

·[22 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--c3302844a47e---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

[Help](https://help.medium.com/hc/en-us?source=post_page-----c3302844a47e---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----c3302844a47e---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----c3302844a47e---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----c3302844a47e---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----c3302844a47e---------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----c3302844a47e---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----c3302844a47e---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----c3302844a47e---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----c3302844a47e---------------------------------------)