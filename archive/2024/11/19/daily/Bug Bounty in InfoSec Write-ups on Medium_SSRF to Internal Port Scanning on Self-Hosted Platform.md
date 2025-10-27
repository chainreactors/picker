---
title: SSRF to Internal Port Scanning on Self-Hosted Platform
url: https://infosecwriteups.com/ssrf-to-internal-port-scanning-on-self-hosted-platform-05a17a461eed?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-11-19
fetch_date: 2025-10-06T19:16:40.531962
---

# SSRF to Internal Port Scanning on Self-Hosted Platform

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F05a17a461eed&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fssrf-to-internal-port-scanning-on-self-hosted-platform-05a17a461eed&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fssrf-to-internal-port-scanning-on-self-hosted-platform-05a17a461eed&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-05a17a461eed---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-05a17a461eed---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# SSRF to Internal Port Scanning on Self-Hosted Platform 🚀

[![JEETPAL](https://miro.medium.com/v2/resize:fill:64:64/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---byline--05a17a461eed---------------------------------------)

[JEETPAL](https://jeetpal2007.medium.com/?source=post_page---byline--05a17a461eed---------------------------------------)

2 min read

·

Oct 31, 2024

--

1

Share

[**Free Artices**](https://medium.com/%40jeetpal2007/ssrf-to-internal-port-scanning-on-self-hosted-platform-05a17a461eed?sk=e2cd54aca1118ebdb7ea5eb4e635f75e)

While exploring a self-hosted platform’s webhook feature, I discovered a Server-Side Request Forgery (SSRF) vulnerability that allowed me to scan internal network ports. This unexpected find opened up a world of network mapping possibilities. Big thanks to my friend who invited me over at [Discord](https://discord.gg/Y467qAFM4X) for making the hunt even more fun and insightful! 🎉

### Discovery Phase 🔍

I started with a pretty simple task: testing out the webhook feature of this self-hosted platform. Typically, webhooks let users forward data to a specified URL, so I entered a `webhook.site` URL to see what kind of response I’d get. The server sent an outbound request as expected, which made me think—*what if I could direct this request internally?* SSRF possibilities started brewing in my mind.

### Testing the Profile for SSRF 🧪

To confirm the vulnerability, I swapped the external URL with an internal IP, like `http://127.0.0.1`, just to see if the server would follow along. It worked! The platform processed my internal IP and even returned a response, confirming that I had access to the internal network through SSRF. With this in place, I decided to dig a little deeper and see if I could go beyond just reaching internal IPs.

Press enter or click to view image in full size

![]()

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--05a17a461eed---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--05a17a461eed---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--05a17a461eed---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--05a17a461eed---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--05a17a461eed---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![JEETPAL](https://miro.medium.com/v2/resize:fill:96:96/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--05a17a461eed---------------------------------------)

[![JEETPAL](https://miro.medium.com/v2/resize:fill:128:128/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--05a17a461eed---------------------------------------)

[## Written by JEETPAL](https://jeetpal2007.medium.com/?source=post_page---post_author_info--05a17a461eed---------------------------------------)

[2.3K followers](https://jeetpal2007.medium.com/followers?source=post_page---post_author_info--05a17a461eed---------------------------------------)

·[3 following](https://medium.com/%40jeetpal2007/following?source=post_page---post_author_info--05a17a461eed---------------------------------------)

A security researcher,Auditor Web3 & Developer Connect me on social media via <https://linktr.ee/jeetpal2007> query:jeetpal2007@gmail.com

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----05a17a461eed---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----05a17a461eed---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----05a17a461eed---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----05a17a461eed---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----05a17a461eed---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----05a17a461eed---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----05a17a461eed---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----05a17a461eed---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----05a17a461eed---------------------------------------)