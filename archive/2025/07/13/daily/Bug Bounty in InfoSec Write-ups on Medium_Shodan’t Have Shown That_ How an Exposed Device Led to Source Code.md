---
title: Shodan’t Have Shown That: How an Exposed Device Led to Source Code
url: https://infosecwriteups.com/shodant-have-shown-that-how-an-exposed-device-led-to-source-code-27346a93f22e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-13
fetch_date: 2025-10-06T23:27:54.711724
---

# Shodan’t Have Shown That: How an Exposed Device Led to Source Code

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F27346a93f22e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fshodant-have-shown-that-how-an-exposed-device-led-to-source-code-27346a93f22e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fshodant-have-shown-that-how-an-exposed-device-led-to-source-code-27346a93f22e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-27346a93f22e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-27346a93f22e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Shodan’t Have Shown That: How an Exposed Device Led to Source Code 📡📜

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--27346a93f22e---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--27346a93f22e---------------------------------------)

3 min read

·

Jul 9, 2025

--

1

Share

Free [Link](https://medium.com/%40iski/shodant-have-shown-that-how-an-exposed-device-led-to-source-code-27346a93f22e?sk=e2739d2842dad3b94b5dc88780f24422) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by Gemini AI

You know you’ve reached peak hacker mode when your morning routine is:

1. Coffee.
2. Shodan.
3. Accidentally breaking into someone’s DevOps pipeline while still in pajamas. ☕️👷‍

One morning, while I was pretending to be productive (a.k.a. checking memes), I remembered that I hadn’t done a proper Shodan recon in a while. So, I did what every responsible adult does:

[## 🚷 Forbidden but Not Forgotten: How an HTTP 403 Made Me a Superadmin 👑🔥

### Hey there!😁

infosecwriteups.com](/forbidden-but-not-forgotten-how-an-http-403-made-me-a-superadmin-6f769c4a9952?source=post_page-----27346a93f22e---------------------------------------)

> *I fired up Shodan, typed* `port:8080 Jenkins`*, and went treasure hunting.*

Little did I know, I was about to fall face-first into a Jenkins server more open than my Google Docs in 2015.

## Step 1: Mass Recon with Shodan 🧰

To begin, I searched for:

```
port:8080 title:Jenkins country:"IN"
```

Boom. Over 200+ exposed Jenkins servers — some login-protected, most… *not*.

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--27346a93f22e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--27346a93f22e---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--27346a93f22e---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--27346a93f22e---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--27346a93f22e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--27346a93f22e---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--27346a93f22e---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--27346a93f22e---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--27346a93f22e---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--27346a93f22e---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----27346a93f22e---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----27346a93f22e---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----27346a93f22e---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----27346a93f22e---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----27346a93f22e---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----27346a93f22e---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----27346a93f22e---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----27346a93f22e---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----27346a93f22e---------------------------------------)