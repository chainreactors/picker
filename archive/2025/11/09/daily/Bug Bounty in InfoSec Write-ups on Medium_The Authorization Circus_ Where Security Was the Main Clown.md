---
title: The Authorization Circus: Where Security Was the Main Clown
url: https://infosecwriteups.com/the-authorization-circus-where-security-was-the-main-clown-f4b84ca9356f?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-11-09
fetch_date: 2025-11-10T03:17:39.710268
---

# The Authorization Circus: Where Security Was the Main Clown

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff4b84ca9356f&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-authorization-circus-where-security-was-the-main-clown-f4b84ca9356f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-authorization-circus-where-security-was-the-main-clown-f4b84ca9356f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f4b84ca9356f---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f4b84ca9356f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# The Authorization Circus: Where Security Was the Main Clown 🤡🎪

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--f4b84ca9356f---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--f4b84ca9356f---------------------------------------)

7 min read

·

2 days ago

--

Share

Free [Link](https://medium.com/%40iski/the-authorization-circus-where-security-was-the-main-clown-f4b84ca9356f?sk=12095e1f0f8f056e304f5b10d0a7169a) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by AI

You know that feeling when you go to the circus and realize the safety inspector is actually one of the clowns? Yeah, that was me last month, except instead of a circus, it was a company’s authorization system, and instead of falling anvils, I found falling access controls. Their security was such a three-ring disaster that I half-expected to see elephants walking tightropes while juggling admin privileges. 🐘

I was testing “CircusTech,” a company that claimed to have “rock-solid authorization” and “military-grade access controls.” What they actually had was more “clown-car security” where everyone could fit into the admin seat if they wiggled just right.

[## ⚔️ Unsafe Eval = Unlimited Control: How a JS Sink Let Me Run Anything 💻💥

### Hey there!😁

infosecwriteups.com](/%EF%B8%8F-unsafe-eval-unlimited-control-how-a-js-sink-let-me-run-anything-60794929a295?source=post_page-----f4b84ca9356f---------------------------------------)

## Act 1: The Ticket Booth That Gave Everyone Backstage Passes 🎟️

After my usual recon (I’ve started giving `subfinder` a standing ovation), I found CircusTech's API. I had a basic user account with permissions so limited I could barely change my profile…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f4b84ca9356f---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f4b84ca9356f---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--f4b84ca9356f---------------------------------------)

[73K followers](/followers?source=post_page---post_publication_info--f4b84ca9356f---------------------------------------)

·[Last published 17 hours ago](/from-wooden-ducks-to-digital-flags-my-first-v1t-ctf-osint-challenge-84c38c9fbcb8?source=post_page---post_publication_info--f4b84ca9356f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--f4b84ca9356f---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--f4b84ca9356f---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--f4b84ca9356f---------------------------------------)

[1.93K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--f4b84ca9356f---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--f4b84ca9356f---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----f4b84ca9356f---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----f4b84ca9356f---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----f4b84ca9356f---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----f4b84ca9356f---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----f4b84ca9356f---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----f4b84ca9356f---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----f4b84ca9356f---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----f4b84ca9356f---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----f4b84ca9356f---------------------------------------)