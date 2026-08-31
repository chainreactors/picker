---
title: He Sent 200,000 Reset Codes to Instagram in 10 Minutes. Instagram Paid Him $30,000.
url: https://infosecwriteups.com/he-sent-200-000-reset-codes-to-instagram-in-10-minutes-instagram-paid-him-30-000-0afd2bcaa3b2?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-08-30
fetch_date: 2026-08-31T07:52:18.199751
---

# He Sent 200,000 Reset Codes to Instagram in 10 Minutes. Instagram Paid Him $30,000.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhe-sent-200-000-reset-codes-to-instagram-in-10-minutes-instagram-paid-him-30-000-0afd2bcaa3b2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhe-sent-200-000-reset-codes-to-instagram-in-10-minutes-instagram-paid-him-30-000-0afd2bcaa3b2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-0afd2bcaa3b2---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-0afd2bcaa3b2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page---header_tags--0afd2bcaa3b2---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page---header_tags--0afd2bcaa3b2---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page---header_tags--0afd2bcaa3b2---------------------------------------)

[Artificial Intelligence](https://medium.com/tag/artificial-intelligence?source=post_page---header_tags--0afd2bcaa3b2---------------------------------------)

[Programming](https://medium.com/tag/programming?source=post_page---header_tags--0afd2bcaa3b2---------------------------------------)

# He Sent 200,000 Reset Codes to Instagram in 10 Minutes. Instagram Paid Him $30,000.

[![Vivek PS](https://miro.medium.com/v2/resize:fill:64:64/1*gswVWtLbFDKYFuLKsi063g.png)](https://medium.com/%40vivekps143?source=post_page---byline--0afd2bcaa3b2---------------------------------------)

[Vivek PS](https://medium.com/%40vivekps143?source=post_page---byline--0afd2bcaa3b2---------------------------------------)

5 min read

·

Aug 17, 2026

--

1

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D0afd2bcaa3b2&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhe-sent-200-000-reset-codes-to-instagram-in-10-minutes-instagram-paid-him-30-000-0afd2bcaa3b2&source=---header_actions--0afd2bcaa3b2---------------------post_audio_button------------------)

Share

> **Quick note — I built** [**HackThrough**](https://hackthrough.live) **. It turns real bug bounty writeups into interactive step-by-step challenges. This bug is on there. Go play it instead of just reading if that sounds interesting.**

Most developers assume that if you put a 6-digit OTP behind a rate limiter, brute force is dead.

You have 1,000,000 possible combinations. The code expires in 10 minutes. If someone types the wrong code 5 times, you lock them out for an hour. Problem solved.

That’s the theory. In practice, concurrency and distributed infrastructure make rate limiting one of the hardest things to get right at scale.

> [**Free Link to read this article**](https://medium.com/%40vivekps143/he-sent-200-000-reset-codes-to-instagram-in-10-minutes-instagram-paid-him-30-000-0afd2bcaa3b2?sk=e9f6ea6a0145875ec70399cfe81e286b)

Press enter or click to view image in full size

![]()

In 2019, security researcher **Laxman Muthiyah** looked at Instagram’s password reset endpoint and found two logic blind spots. By chaining them together, he proved he could reset the password on any Instagram account in under 10 minutes for about $150 in cloud compute.

Facebook acknowledged the critical severity and paid him **$30,000**.

Here’s the breakdown of how he did it, why the rate limiter broke, and what backend engineers keep getting wrong about OTP verification.

## The Target Endpoint

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0afd2bcaa3b2---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0afd2bcaa3b2---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--0afd2bcaa3b2---------------------------------------)

[88K followers](/followers?source=post_page---post_publication_info--0afd2bcaa3b2---------------------------------------)

·[Last published 2 days ago](/when-a-single-text-file-breaks-a-trust-boundary-bug-bounty-writeup-824c1e2dc9f0?source=post_page---post_publication_info--0afd2bcaa3b2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Vivek PS](https://miro.medium.com/v2/resize:fill:96:96/1*gswVWtLbFDKYFuLKsi063g.png)](https://medium.com/%40vivekps143?source=post_page---post_author_info--0afd2bcaa3b2---------------------------------------)

[![Vivek PS](https://miro.medium.com/v2/resize:fill:128:128/1*gswVWtLbFDKYFuLKsi063g.png)](https://medium.com/%40vivekps143?source=post_page---post_author_info--0afd2bcaa3b2---------------------------------------)

[## Written by Vivek PS](https://medium.com/%40vivekps143?source=post_page---post_author_info--0afd2bcaa3b2---------------------------------------)

[1.2K followers](https://medium.com/%40vivekps143/followers?source=post_page---post_author_info--0afd2bcaa3b2---------------------------------------)

·[83 following](https://medium.com/%40vivekps143/following?source=post_page---post_author_info--0afd2bcaa3b2---------------------------------------)

I’m a programmer, web security researcher and chess player, focused on innovation, learning, and creating impactful solutions for growth.

[Help](https://help.medium.com/hc/en-us?source=post_page-----0afd2bcaa3b2---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----0afd2bcaa3b2---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----0afd2bcaa3b2---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----0afd2bcaa3b2---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----0afd2bcaa3b2---------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----0afd2bcaa3b2---------------------------------------)

...