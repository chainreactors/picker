---
title: This Is How I Could Have Reactivated Your Instagram Account Without Your Knowledge
url: https://infosecwriteups.com/this-is-how-i-could-have-reactivated-your-instagram-account-without-your-knowledge-9d220bda5620?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-04-29
fetch_date: 2026-04-30T05:28:59.796191
---

# This Is How I Could Have Reactivated Your Instagram Account Without Your Knowledge

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthis-is-how-i-could-have-reactivated-your-instagram-account-without-your-knowledge-9d220bda5620&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthis-is-how-i-could-have-reactivated-your-instagram-account-without-your-knowledge-9d220bda5620&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-9d220bda5620---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-9d220bda5620---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

# This Is How I Could Have Reactivated Your Instagram Account Without Your Knowledge

## In this write-up, I have shared the story of an Instagram bug where deactivated account could be silently reactivated without victim’s knowledge.

[![Shubham Bhamare](https://miro.medium.com/v2/resize:fill:64:64/1*YJZ3Ns7NJ_u8GA9ad3G3-A.png)](https://theshubh77.medium.com/?source=post_page---byline--9d220bda5620---------------------------------------)

[Shubham Bhamare](https://theshubh77.medium.com/?source=post_page---byline--9d220bda5620---------------------------------------)

5 min read

·

1 day ago

--

4

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D9d220bda5620&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthis-is-how-i-could-have-reactivated-your-instagram-account-without-your-knowledge-9d220bda5620&source=---header_actions--9d220bda5620---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

Image created/designed by the author

> ✨ Non-members can read this write-up for free using [this link](https://theshubh77.medium.com/9d220bda5620?sk=96a35d54ca5a559d1e41236dbb3d4954).

Hi everyone, this is [Shubham Bhamare](https://linktr.ee/theshubh77). Today, I’m going to share the story of one of the most creative and painful findings of my bug hunting journey. The target? Instagram, which of course means Meta. 😅

This one is special, not because of the bounty (spoiler: there isn’t one 🥲), but because of everything around it. A last-minute hunt on New Year’s Eve just to keep a streak alive. A bug that could silently reactivate someone’s Instagram account without them ever touching their phone. A Meta security analyst who told me it would get a bounty. And then… well. You’ll see. 😅

Let’s get into it! 🚀

**Long story short:**

Let me set the scene before we get into the bug. 😄

I’ve been on the [Meta Whitehat Hall of Fame](https://bugbounty.meta.com/leaderboard/) for 4 consecutive years: 2018, 2019, 2020, and 2021.

--

--

4

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--9d220bda5620---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--9d220bda5620---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--9d220bda5620---------------------------------------)

[85K followers](/followers?source=post_page---post_publication_info--9d220bda5620---------------------------------------)

·[Last published just now](/intigriti-april-2026-xss-challenge-writeup-a85b483e86f8?source=post_page---post_publication_info--9d220bda5620---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Shubham Bhamare](https://miro.medium.com/v2/resize:fill:96:96/1*YJZ3Ns7NJ_u8GA9ad3G3-A.png)](https://theshubh77.medium.com/?source=post_page---post_author_info--9d220bda5620---------------------------------------)

[![Shubham Bhamare](https://miro.medium.com/v2/resize:fill:128:128/1*YJZ3Ns7NJ_u8GA9ad3G3-A.png)](https://theshubh77.medium.com/?source=post_page---post_author_info--9d220bda5620---------------------------------------)

[## Written by Shubham Bhamare](https://theshubh77.medium.com/?source=post_page---post_author_info--9d220bda5620---------------------------------------)

[496 followers](https://theshubh77.medium.com/followers?source=post_page---post_author_info--9d220bda5620---------------------------------------)

·[30 following](https://medium.com/%40theshubh77/following?source=post_page---post_author_info--9d220bda5620---------------------------------------)

An ORDINARY guy with EXTRAORDINARY dreams!

## Responses (4)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----9d220bda5620---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----9d220bda5620---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----9d220bda5620---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----9d220bda5620---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----9d220bda5620---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----9d220bda5620---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----9d220bda5620---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----9d220bda5620---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----9d220bda5620---------------------------------------)