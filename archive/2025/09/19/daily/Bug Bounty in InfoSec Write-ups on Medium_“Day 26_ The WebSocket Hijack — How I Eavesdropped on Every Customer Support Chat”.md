---
title: “Day 26: The WebSocket Hijack — How I Eavesdropped on Every Customer Support Chat”
url: https://infosecwriteups.com/day-26-the-websocket-hijack-how-i-eavesdropped-on-every-customer-support-chat-de5ddc819ad2?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-19
fetch_date: 2025-10-02T20:21:52.036838
---

# “Day 26: The WebSocket Hijack — How I Eavesdropped on Every Customer Support Chat”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fde5ddc819ad2&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-26-the-websocket-hijack-how-i-eavesdropped-on-every-customer-support-chat-de5ddc819ad2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-26-the-websocket-hijack-how-i-eavesdropped-on-every-customer-support-chat-de5ddc819ad2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-de5ddc819ad2---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-de5ddc819ad2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# “Day 26: The WebSocket Hijack — How I Eavesdropped on Every Customer Support Chat”

## Exploiting the Trusting Handshake of Real-Time Communication

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--de5ddc819ad2---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--de5ddc819ad2---------------------------------------)

5 min read

·

Sep 2, 2025

--

Share

The target was a major bank’s customer support portal. They had a sleek, modern live chat feature powered by WebSockets. It felt responsive and secure. But during testing, I noticed the initial WebSocket connection didn’t use a typical Authorization header. My curiosity turned to shock when I realized the authentication mechanism was a simple, predictable token passed in the URL. By manipulating this token, I didn’t just hijack one chat — I gained the ability to connect to *any* active support session in real-time, listening in and even injecting messages. This breach of confidentiality led to a $6000 bounty.

[free link](https://amannsharmaa.medium.com/day-26-the-websocket-hijack-how-i-eavesdropped-on-every-customer-support-chat-de5ddc819ad2?sk=54034a8721ebc56fb0d123d4725ef88c)

Press enter or click to view image in full size

![]()

## Why WebSockets Are a Unique Attack Surface

WebSockets provide full-duplex, persistent communication channels over a single TCP connection. This is great for real-time apps like chat, notifications, and trading platforms. But this persistence creates new risks:

* Custom Protocols: They often implement bespoke authentication and authorization logic, bypassing standard HTTP security controls.
* Statefulness: The connection is stateful. If you can…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--de5ddc819ad2---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--de5ddc819ad2---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--de5ddc819ad2---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--de5ddc819ad2---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--de5ddc819ad2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--de5ddc819ad2---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--de5ddc819ad2---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--de5ddc819ad2---------------------------------------)

[739 followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--de5ddc819ad2---------------------------------------)

·[14 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--de5ddc819ad2---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----de5ddc819ad2---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----de5ddc819ad2---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----de5ddc819ad2---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----de5ddc819ad2---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----de5ddc819ad2---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----de5ddc819ad2---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----de5ddc819ad2---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----de5ddc819ad2---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----de5ddc819ad2---------------------------------------)