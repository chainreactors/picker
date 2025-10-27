---
title: Missing Rate Limit on Several Endpoints $1300
url: https://infosecwriteups.com/missing-rate-limit-on-several-endpoints-1300-60f37e16be6b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-05-07
fetch_date: 2025-10-06T22:25:47.521631
---

# Missing Rate Limit on Several Endpoints $1300

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F60f37e16be6b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmissing-rate-limit-on-several-endpoints-1300-60f37e16be6b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmissing-rate-limit-on-several-endpoints-1300-60f37e16be6b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-60f37e16be6b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-60f37e16be6b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Missing Rate Limit on Several Endpoints $1300

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:64:64/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---byline--60f37e16be6b---------------------------------------)

[Ehtesham Ul Haq](https://ehteshamulhaq198.medium.com/?source=post_page---byline--60f37e16be6b---------------------------------------)

5 min read

·

Jan 10, 2025

--

3

Share

Free Article Link: [Click for free!](https://ehteshamulhaq198.medium.com/missing-rate-limit-on-several-endpoints-1300-60f37e16be6b?sk=fbb8ab48539d4959d922d7442b227ad1)

Hello, hunters!

In this blog post, I’ll share the journey of uncovering a rate-limit vulnerability on multiple endpoints that ultimately enabled an account takeover. Let’s dive into the details!

**Description**

Rate limiting is a mechanism designed to control the volume of requests directed at a specific API endpoint within a given timeframe. Its primary purpose is to protect APIs from misuse and ensure system reliability. For instance, rate limiting can prevent brute force attacks by capping the number of login attempts made to an endpoint.

There are generally two types of rate limiters:

* Strict Rate Limiter: This approach blocks all requests once the limit is exceeded, ensuring strict adherence to the set threshold.
* Flexible Rate Limiter: This allows the threshold to be temporarily exceeded for a brief period before throttling requests, offering a more lenient solution.

Rate limiters serve multiple purposes, such as:

* Preventing Resource Exhaustion: Safeguarding systems from being overwhelmed by excessive usage.
* Controlling Costs: Avoiding overuse of pay-per-use services by enforcing request caps.
* Enhancing Security: Protecting APIs from malicious activities, such as automated attacks or spam.

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--60f37e16be6b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--60f37e16be6b---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--60f37e16be6b---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--60f37e16be6b---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--60f37e16be6b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:96:96/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--60f37e16be6b---------------------------------------)

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:128:128/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--60f37e16be6b---------------------------------------)

[## Written by Ehtesham Ul Haq](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--60f37e16be6b---------------------------------------)

[520 followers](https://ehteshamulhaq198.medium.com/followers?source=post_page---post_author_info--60f37e16be6b---------------------------------------)

·[99 following](https://medium.com/%40ehteshamulhaq198/following?source=post_page---post_author_info--60f37e16be6b---------------------------------------)

Penetration Tester & Bug Bounty Hunter focused on finding vulnerabilities and helping organizations stay ahead of cyber threats.

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----60f37e16be6b---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----60f37e16be6b---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----60f37e16be6b---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----60f37e16be6b---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----60f37e16be6b---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----60f37e16be6b---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----60f37e16be6b---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----60f37e16be6b---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----60f37e16be6b---------------------------------------)