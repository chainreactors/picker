---
title: CSRF in 2025: “Solved” But Still Bypassable
url: https://infosecwriteups.com/csrf-in-2025-solved-but-still-bypassable-942ca382ab77?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-03-01
fetch_date: 2025-10-06T21:57:44.362794
---

# CSRF in 2025: “Solved” But Still Bypassable

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F942ca382ab77&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcsrf-in-2025-solved-but-still-bypassable-942ca382ab77&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcsrf-in-2025-solved-but-still-bypassable-942ca382ab77&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-942ca382ab77---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-942ca382ab77---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# CSRF in 2025: “Solved” But Still Bypassable

[![Vivek PS](https://miro.medium.com/v2/resize:fill:64:64/1*gswVWtLbFDKYFuLKsi063g.png)](https://medium.com/%40vivekps143?source=post_page---byline--942ca382ab77---------------------------------------)

[Vivek PS](https://medium.com/%40vivekps143?source=post_page---byline--942ca382ab77---------------------------------------)

4 min read

·

Feb 28, 2025

--

1

Share

Press enter or click to view image in full size

![]()

A few years ago, if you reported a **Cross-Site Request Forgery (CSRF)** vulnerability, many companies would shrug it off. **“We use SameSite cookies.”** **“CSRF tokens are in place.”** **“This isn’t exploitable anymore.”**

Yet here we are in 2025, and **CSRF bypasses are still happening.**

They don’t look like the old-school “force a logged-in user to change their email” type of attacks anymore. **They’re sneakier.** They exploit **modern web APIs, misconfigured OAuth flows, and CORS screw-ups** that make apps think they’re safe when they’re really not.

Let me walk you through **how attackers are still pulling off CSRF in 2025** — and why developers keep getting it wrong.

## The “CSRF is Dead” Myth

A lot of developers think **SameSite cookies** solved CSRF forever. They’re not wrong — **if configured correctly.**

But in bug bounty hunting, you don’t look for **perfect implementations**. You look for **misconfigurations, edge cases, and forgotten endpoints**.

Here’s where CSRF protections fail in 2025:

1. **SameSite=None without proper CORS rules** → Allows cross-origin requests with cookies intact.
2. **CSRF tokens being leaked in API responses** → Attackers steal them and forge requests.

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--942ca382ab77---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--942ca382ab77---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--942ca382ab77---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--942ca382ab77---------------------------------------)

·[Last published 1 hour ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--942ca382ab77---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Vivek PS](https://miro.medium.com/v2/resize:fill:96:96/1*gswVWtLbFDKYFuLKsi063g.png)](https://medium.com/%40vivekps143?source=post_page---post_author_info--942ca382ab77---------------------------------------)

[![Vivek PS](https://miro.medium.com/v2/resize:fill:128:128/1*gswVWtLbFDKYFuLKsi063g.png)](https://medium.com/%40vivekps143?source=post_page---post_author_info--942ca382ab77---------------------------------------)

[## Written by Vivek PS](https://medium.com/%40vivekps143?source=post_page---post_author_info--942ca382ab77---------------------------------------)

[420 followers](https://medium.com/%40vivekps143/followers?source=post_page---post_author_info--942ca382ab77---------------------------------------)

·[69 following](https://medium.com/%40vivekps143/following?source=post_page---post_author_info--942ca382ab77---------------------------------------)

I’m a programmer, web security researcher and chess player, focused on innovation, learning, and creating impactful solutions for growth.

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----942ca382ab77---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----942ca382ab77---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----942ca382ab77---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----942ca382ab77---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----942ca382ab77---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----942ca382ab77---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----942ca382ab77---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----942ca382ab77---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----942ca382ab77---------------------------------------)