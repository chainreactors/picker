---
title: “Bug Bounty Bootcamp #48: OAuth + XSS ”
url: https://infosecwriteups.com/bug-bounty-bootcamp-48-oauth-xss-04246084a403?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-19
fetch_date: 2026-06-20T06:13:30.717198
---

# “Bug Bounty Bootcamp #48: OAuth + XSS ”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-bootcamp-48-oauth-xss-04246084a403&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-bootcamp-48-oauth-xss-04246084a403&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-04246084a403---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-04246084a403---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

# “Bug Bounty Bootcamp #48: OAuth + XSS ”

## The Ultimate Account Takeover One-Two Punch

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--04246084a403---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--04246084a403---------------------------------------)

6 min read

·

2 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D04246084a403&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-bootcamp-48-oauth-xss-04246084a403&source=---header_actions--04246084a403---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

You found an open redirect in the OAuth flow. Or a reflected XSS. Separate? Meh. Combined? You can steal anyone’s session token, change their email, and reset their password — all in one automated attack. Let’s chain them like a pro.

[Free Link / Friend Link](https://amannsharmaa.medium.com/bug-bounty-bootcamp-48-oauth-xss-04246084a403?sk=cf9e51913857eba9837df2be3a50adef)

Welcome back, you beautiful chain-reaction gremlin. You’ve learned about account takeovers in general. Now we focus on two powerful ATO techniques:

1. OAuth + Open Redirect — Leak the authentication hash by redirecting to your server
2. XSS + CSRF-style POST — Execute JavaScript that changes the user’s email, then triggers a password reset

Both techniques turn “medium” vulnerabilities into critical account takeover exploits. And the best part? You don’t need to be a JavaScript wizard — ChatGPT can write the code for you.

## Part 1: OAuth + Open Redirect — Stealing the Magic Hash

OAuth flows are beautiful and terrifying. The user clicks “Login with Google” (or any provider), gets redirected to the auth server, approves, and gets sent back with a hash or code in the URL fragment (`#access_token=xyz`). If you can control the `redirect_uri`, you can steal…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--04246084a403---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--04246084a403---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--04246084a403---------------------------------------)

[87K followers](/followers?source=post_page---post_publication_info--04246084a403---------------------------------------)

·[Last published 1 day ago](/bitsctf-2026-writeups-osint-and-steganography-forensics-challenges-b91257ca0856?source=post_page---post_publication_info--04246084a403---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--04246084a403---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--04246084a403---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--04246084a403---------------------------------------)

[1.6K followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--04246084a403---------------------------------------)

·[22 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--04246084a403---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

[Help](https://help.medium.com/hc/en-us?source=post_page-----04246084a403---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----04246084a403---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----04246084a403---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----04246084a403---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----04246084a403---------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----04246084a403---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----04246084a403---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----04246084a403---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----04246084a403---------------------------------------)