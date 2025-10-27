---
title: “Day 26: The Logic Bomb — How I Hacked 0.1% of a Million-User Platform in 10 Minutes”
url: https://infosecwriteups.com/day-26-the-logic-bomb-how-i-hacked-0-1-of-a-million-user-platform-in-10-minutes-7dcb23f488cb?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-03
fetch_date: 2025-10-02T19:33:20.637375
---

# “Day 26: The Logic Bomb — How I Hacked 0.1% of a Million-User Platform in 10 Minutes”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7dcb23f488cb&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-26-the-logic-bomb-how-i-hacked-0-1-of-a-million-user-platform-in-10-minutes-7dcb23f488cb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-26-the-logic-bomb-how-i-hacked-0-1-of-a-million-user-platform-in-10-minutes-7dcb23f488cb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-7dcb23f488cb---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-7dcb23f488cb---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# “Day 25: The Logic Bomb — How I Hacked 0.1% of a Million-User Platform in 10 Minutes”

## Exploiting a Flawed State Machine in Password Reset

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--7dcb23f488cb---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--7dcb23f488cb---------------------------------------)

6 min read

·

Sep 1, 2025

--

1

Share

Hey everyone! We’re at Day 25 of our bug bounty deep dive, and today’s find is a classic example of why you should never trust a process just because it *looks* secure. The target was a popular social media platform with over a million users. Their password reset flow was textbook: enter email, get a link, set a new password. But during testing, I noticed a tiny, almost imperceptible quirk. If you requested two reset emails in quick succession, the system got confused. This confusion was the tip of the iceberg. By exploiting a fundamental flaw in the application’s “state machine” — the logic that governs the status of a reset process — I was able to create a script that automatically compromised user accounts faster than their owners could secure them. The platform paid a $5000 bounty for this critical logic flaw.

[free link](https://amannsharmaa.medium.com/day-26-the-logic-bomb-how-i-hacked-0-1-of-a-million-user-platform-in-10-minutes-7dcb23f488cb?sk=dddf36b10a17a5790773accbcdf4d1c4)

Press enter or click to view image in full size

![]()

## The Psychology of Password Reset

Password reset is a critical trust pathway. Users are trained to click the link in their email without a second thought. This makes it a prime target for attackers. Most tests focus on token leakage or predictability. But the real vulnerability often lies in the…

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7dcb23f488cb---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7dcb23f488cb---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--7dcb23f488cb---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--7dcb23f488cb---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--7dcb23f488cb---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--7dcb23f488cb---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--7dcb23f488cb---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--7dcb23f488cb---------------------------------------)

[739 followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--7dcb23f488cb---------------------------------------)

·[14 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--7dcb23f488cb---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----7dcb23f488cb---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----7dcb23f488cb---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----7dcb23f488cb---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----7dcb23f488cb---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----7dcb23f488cb---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----7dcb23f488cb---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----7dcb23f488cb---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----7dcb23f488cb---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----7dcb23f488cb---------------------------------------)