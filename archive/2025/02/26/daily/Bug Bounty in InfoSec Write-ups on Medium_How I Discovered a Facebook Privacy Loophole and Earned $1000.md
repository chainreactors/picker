---
title: How I Discovered a Facebook Privacy Loophole and Earned $1000
url: https://infosecwriteups.com/how-i-discovered-a-facebook-privacy-loophole-and-earned-1000-44318d196bfc?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-02-26
fetch_date: 2025-10-06T20:34:11.188547
---

# How I Discovered a Facebook Privacy Loophole and Earned $1000

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F44318d196bfc&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-discovered-a-facebook-privacy-loophole-and-earned-1000-44318d196bfc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-discovered-a-facebook-privacy-loophole-and-earned-1000-44318d196bfc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-44318d196bfc---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-44318d196bfc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How I Discovered a Facebook Privacy Loophole and Earned $1000

[![Vivek PS](https://miro.medium.com/v2/resize:fill:64:64/1*gswVWtLbFDKYFuLKsi063g.png)](https://medium.com/%40vivekps143?source=post_page---byline--44318d196bfc---------------------------------------)

[Vivek PS](https://medium.com/%40vivekps143?source=post_page---byline--44318d196bfc---------------------------------------)

3 min read

·

Feb 25, 2025

--

3

Share

> **My article is open to everyone; non-member readers can click** [**this link**](https://medium.com/%40vivekps143/44318d196bfc?sk=724e42f0a41e1ae19ed81996d4bd09d9) **to read the full text.**

Press enter or click to view image in full size

![]()

## Introduction: A Privacy Flaw Hiding in Plain Sight

What if I told you that your private RSVP status on Facebook events wasn’t actually private? Imagine marking yourself as “Going” or “Not Going” to a public event, believing only the event host could see it — only to realize that a friend could expose your choice using a simple trick.

That’s exactly what I discovered. A small but critical flaw in Facebook’s event system allowed an attacker to bypass privacy settings and reveal hidden RSVP statuses.

The best part? Facebook acknowledged the issue, patched it, and rewarded me with **$1000** for reporting it.

Here’s how I found the bug, why it mattered, and what you can learn from it.

## The Discovery: Cracking Facebook’s RSVP Privacy

Facebook lets users RSVP to public events while keeping their responses private from friends. However, I discovered a loophole that allowed a mutual friend (the attacker) to determine someone’s RSVP status with two simple steps:

1. **The Invitation Test** — If a user can’t be invited, they’ve…

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--44318d196bfc---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--44318d196bfc---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--44318d196bfc---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--44318d196bfc---------------------------------------)

·[Last published just now](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--44318d196bfc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Vivek PS](https://miro.medium.com/v2/resize:fill:96:96/1*gswVWtLbFDKYFuLKsi063g.png)](https://medium.com/%40vivekps143?source=post_page---post_author_info--44318d196bfc---------------------------------------)

[![Vivek PS](https://miro.medium.com/v2/resize:fill:128:128/1*gswVWtLbFDKYFuLKsi063g.png)](https://medium.com/%40vivekps143?source=post_page---post_author_info--44318d196bfc---------------------------------------)

[## Written by Vivek PS](https://medium.com/%40vivekps143?source=post_page---post_author_info--44318d196bfc---------------------------------------)

[420 followers](https://medium.com/%40vivekps143/followers?source=post_page---post_author_info--44318d196bfc---------------------------------------)

·[69 following](https://medium.com/%40vivekps143/following?source=post_page---post_author_info--44318d196bfc---------------------------------------)

I’m a programmer, web security researcher and chess player, focused on innovation, learning, and creating impactful solutions for growth.

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----44318d196bfc---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----44318d196bfc---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----44318d196bfc---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----44318d196bfc---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----44318d196bfc---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----44318d196bfc---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----44318d196bfc---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----44318d196bfc---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----44318d196bfc---------------------------------------)