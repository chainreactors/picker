---
title: “Day 25: The Cloud Heist — How a Forgotten Webhook Tester Gave Me the Keys to AWS”
url: https://infosecwriteups.com/day-25-the-cloud-heist-how-a-forgotten-webhook-tester-gave-me-the-keys-to-aws-0e2876b515a8?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-14
fetch_date: 2025-10-02T20:08:45.291043
---

# “Day 25: The Cloud Heist — How a Forgotten Webhook Tester Gave Me the Keys to AWS”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F0e2876b515a8&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-25-the-cloud-heist-how-a-forgotten-webhook-tester-gave-me-the-keys-to-aws-0e2876b515a8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-25-the-cloud-heist-how-a-forgotten-webhook-tester-gave-me-the-keys-to-aws-0e2876b515a8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-0e2876b515a8---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-0e2876b515a8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# “Day 24: The Cloud Heist — How a Forgotten Webhook Tester Gave Me the Keys to AWS”

## Turning a Blind SSRF into a $1000 Cloud Compromise

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--0e2876b515a8---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--0e2876b515a8---------------------------------------)

6 min read

·

Aug 30, 2025

--

Share

The target was a SaaS company built entirely on AWS. Their main application was a fortress. But during recon, I stumbled upon a forgotten subdomain: `devtools.coolstartup.com`. It hosted an internal tool for developers to test webhooks. This tool had a critical flaw: it would make HTTP requests to any URL provided. This seemingly minor oversight—a blind Server-Side Request Forgery (SSRF)—became the initial thread I pulled to unravel their entire cloud infrastructure, leading to a $1000 bounty. This is the story of how internal tools become external threats.

[free link](https://amannsharmaa.medium.com/day-25-the-cloud-heist-how-a-forgotten-webhook-tester-gave-me-the-keys-to-aws-0e2876b515a8?sk=d2cf06193a7c5929bd9df422b3da129b)

Press enter or click to view image in full size

![]()

## Why Internal Tools Are a Goldmine

Internal tools are often built without the same security rigor as customer-facing applications. They assume a trusted user base and a protected network. This makes them prime targets for attackers who can reach them. Common pitfalls include:

* Lax authentication or default credentials.
* Powerful functionality meant for debugging.
* No logging or monitoring for malicious use.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0e2876b515a8---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0e2876b515a8---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--0e2876b515a8---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--0e2876b515a8---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--0e2876b515a8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--0e2876b515a8---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--0e2876b515a8---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--0e2876b515a8---------------------------------------)

[739 followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--0e2876b515a8---------------------------------------)

·[14 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--0e2876b515a8---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----0e2876b515a8---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----0e2876b515a8---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----0e2876b515a8---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----0e2876b515a8---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----0e2876b515a8---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----0e2876b515a8---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----0e2876b515a8---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----0e2876b515a8---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----0e2876b515a8---------------------------------------)