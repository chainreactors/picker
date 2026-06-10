---
title: How GraphQL Mutation Aliasing Led to a $12,500 DoS Bug in HackerOne’s Account Recovery Flow
url: https://infosecwriteups.com/how-graphql-mutation-aliasing-led-to-a-12-500-dos-bug-in-hackerones-account-recovery-flow-a0635b2f3997?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-09
fetch_date: 2026-06-10T06:15:29.937315
---

# How GraphQL Mutation Aliasing Led to a $12,500 DoS Bug in HackerOne’s Account Recovery Flow

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-graphql-mutation-aliasing-led-to-a-12-500-dos-bug-in-hackerones-account-recovery-flow-a0635b2f3997&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-graphql-mutation-aliasing-led-to-a-12-500-dos-bug-in-hackerones-account-recovery-flow-a0635b2f3997&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-a0635b2f3997---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-a0635b2f3997---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Press enter or click to view image in full size

![]()

Member-only story

# How GraphQL Mutation Aliasing Led to a $12,500 DoS Bug in HackerOne’s Account Recovery Flow

[![Abhishek meena](https://miro.medium.com/v2/resize:fill:64:64/1*g4tYjgpvB52xwZPNMcvefg.png)](https://medium.com/%40Aacle?source=post_page---byline--a0635b2f3997---------------------------------------)

[Abhishek meena](https://medium.com/%40Aacle?source=post_page---byline--a0635b2f3997---------------------------------------)

8 min read

·

1 day ago

--

1

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Da0635b2f3997&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-graphql-mutation-aliasing-led-to-a-12-500-dos-bug-in-hackerones-account-recovery-flow-a0635b2f3997&source=---header_actions--a0635b2f3997---------------------post_audio_button------------------)

Share

A small GraphQL behavior created a very real availability problem.

Most bug bounty hunters look for obvious impact.

Account takeover. Sensitive data leaks. IDORs. SSRF. RCE.

But sometimes the bug is not about stealing data.

Sometimes the right question is:

> Can the application be forced to do expensive work repeatedly from a single request?

That was the core idea behind this HackerOne report.

In this article, I am breaking down a Denial-of-Service report involving HackerOne’s GraphQL API, where the `verifyAccountRecoveryPhoneNumber` mutation could be executed multiple times inside one request using GraphQL aliases.

The original report was submitted by `@hellokbit`. My goal here is to analyze the thinking approach behind the report and make the vulnerability easy to understand for people learning bug bounty and GraphQL security.

The reported bounty was:

## $12,500

This writeup breaks down the reporter’s approach in a simple way, especially for beginner to intermediate bug bounty hunters who are learning GraphQL testing.

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a0635b2f3997---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a0635b2f3997---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--a0635b2f3997---------------------------------------)

[87K followers](/followers?source=post_page---post_publication_info--a0635b2f3997---------------------------------------)

·[Last published 21 hours ago](/i-found-the-entire-admin-ui-of-a-live-platformjust-by-tweaking-traffic-in-burp-suite-c788db767598?source=post_page---post_publication_info--a0635b2f3997---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Abhishek meena](https://miro.medium.com/v2/resize:fill:96:96/1*g4tYjgpvB52xwZPNMcvefg.png)](https://medium.com/%40Aacle?source=post_page---post_author_info--a0635b2f3997---------------------------------------)

[![Abhishek meena](https://miro.medium.com/v2/resize:fill:128:128/1*g4tYjgpvB52xwZPNMcvefg.png)](https://medium.com/%40Aacle?source=post_page---post_author_info--a0635b2f3997---------------------------------------)

[## Written by Abhishek meena](https://medium.com/%40Aacle?source=post_page---post_author_info--a0635b2f3997---------------------------------------)

[1.6K followers](https://medium.com/%40Aacle/followers?source=post_page---post_author_info--a0635b2f3997---------------------------------------)

·[25 following](https://medium.com/%40Aacle/following?source=post_page---post_author_info--a0635b2f3997---------------------------------------)

Co Founder & COO At <http://Vulncure.com> | Bug Hunter ✦ 🖊️ Tester 🤝 Committed to infosec 📬 Open for DMs

[Help](https://help.medium.com/hc/en-us?source=post_page-----a0635b2f3997---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----a0635b2f3997---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----a0635b2f3997---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----a0635b2f3997---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----a0635b2f3997---------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----a0635b2f3997---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----a0635b2f3997---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----a0635b2f3997---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----a0635b2f3997---------------------------------------)