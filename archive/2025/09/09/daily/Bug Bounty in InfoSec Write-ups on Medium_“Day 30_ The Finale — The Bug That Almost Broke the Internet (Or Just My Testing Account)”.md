---
title: “Day 30: The Finale — The Bug That Almost Broke the Internet (Or Just My Testing Account)”
url: https://infosecwriteups.com/day-30-the-finale-the-bug-that-almost-broke-the-internet-or-just-my-testing-account-d63112e13427?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-09
fetch_date: 2025-10-02T19:50:27.491736
---

# “Day 30: The Finale — The Bug That Almost Broke the Internet (Or Just My Testing Account)”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd63112e13427&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-30-the-finale-the-bug-that-almost-broke-the-internet-or-just-my-testing-account-d63112e13427&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-30-the-finale-the-bug-that-almost-broke-the-internet-or-just-my-testing-account-d63112e13427&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d63112e13427---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d63112e13427---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# “Day 30: The Finale — The Bug That Almost Broke the Internet (Or Just My Testing Account)”

## How a Simple API Call Triggered a $25,000 Cloud Bill and a Temporary Ban

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--d63112e13427---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--d63112e13427---------------------------------------)

5 min read

·

Sep 6, 2025

--

2

Share

Well, folks, we’ve reached Day 30. It’s been a wild ride, and I’ve saved one of my most memorable stories for last. This wasn’t just a bug; it was a digital avalanche. The target was a new “serverless” platform promising effortless auto-scaling. My goal was to test its limits. I found an API endpoint that managed background workers. A simple miscalculation with a parameter — a number that was too big — unleashed a chain reaction. Within minutes, their system had spun up over 1000 virtual servers to handle my request, triggering a massive cloud bill and automatic alerts that got my testing account instantly banned. The vendor was initially furious, but after understanding the flaw, they awarded a $7,500 bounty and reinstated my access. This is the story of the day I (accidentally) stress-tested the cloud.

[free link](https://amannsharmaa.medium.com/day-30-the-finale-the-bug-that-almost-broke-the-internet-or-just-my-testing-account-d63112e13427?sk=6b585a8783f29022e33d9b8e28ebf26d)

![]()

## The Peril of “Unlimited” Scale

Cloud platforms and serverless architectures promise infinite, automatic scaling. This is powerful for developers but creates a terrifying attack vector: resource exhaustion. The question isn’t just “can I access data?” but “can I make…

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d63112e13427---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d63112e13427---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--d63112e13427---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--d63112e13427---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--d63112e13427---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--d63112e13427---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--d63112e13427---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--d63112e13427---------------------------------------)

[739 followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--d63112e13427---------------------------------------)

·[14 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--d63112e13427---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----d63112e13427---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----d63112e13427---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----d63112e13427---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----d63112e13427---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----d63112e13427---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----d63112e13427---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----d63112e13427---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----d63112e13427---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----d63112e13427---------------------------------------)