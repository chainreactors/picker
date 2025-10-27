---
title: $600 Bounty: How Revealed Hidden Read Receipts in Bumble’s Chat API
url: https://infosecwriteups.com/600-bounty-how-revealed-hidden-read-receipts-in-bumbles-chat-api-53bc06c987f5?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-07
fetch_date: 2025-10-06T23:23:05.997828
---

# $600 Bounty: How Revealed Hidden Read Receipts in Bumble’s Chat API

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F53bc06c987f5&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F600-bounty-how-revealed-hidden-read-receipts-in-bumbles-chat-api-53bc06c987f5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F600-bounty-how-revealed-hidden-read-receipts-in-bumbles-chat-api-53bc06c987f5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-53bc06c987f5---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-53bc06c987f5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# $600 Bounty: How to Revealed Hidden Read Receipts in Bumble’s Chat API

## **Exploiting an Overlooked API Endpoint to Access Private Read Statuses — Even When the UI Said Delivered**

[![Monika sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---byline--53bc06c987f5---------------------------------------)

[Monika sharma](https://medium.com/%40commanak46?source=post_page---byline--53bc06c987f5---------------------------------------)

4 min read

·

Jul 6, 2025

--

Share

Press enter or click to view image in full size

![]()

**Introduction**

In messaging apps, privacy expectations are everything. Some users want the read notification, others prefer ambiguity. Bumble chose the latter — messages show delivered but never read preserving a sense of privacy.

But what if the app lied?

Security researcher @ndrong discovered that Bumble’s backend API quietly betrayed this promise, exposing read status of messages even when the frontend never showed them. The flaw earned a $600 bounty and highlights the subtle power of backend APIs — and the risks of mismatched client-server behavior.

## The Privacy Design: “Delivered” But Never “Read”

On Bumble’s mobile app, messages show whether they were delivered — but crucially not whether they were read. The same goes for the web app, which provides an even more stripped-down experience.

This design choice implies user privacy: your matches won’t know if you’ve read their messages — so no pressure, right?

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--53bc06c987f5---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--53bc06c987f5---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--53bc06c987f5---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--53bc06c987f5---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--53bc06c987f5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Monika sharma](https://miro.medium.com/v2/resize:fill:96:96/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--53bc06c987f5---------------------------------------)

[![Monika sharma](https://miro.medium.com/v2/resize:fill:128:128/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--53bc06c987f5---------------------------------------)

[## Written by Monika sharma](https://medium.com/%40commanak46?source=post_page---post_author_info--53bc06c987f5---------------------------------------)

[2K followers](https://medium.com/%40commanak46/followers?source=post_page---post_author_info--53bc06c987f5---------------------------------------)

·[7 following](https://medium.com/%40commanak46/following?source=post_page---post_author_info--53bc06c987f5---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----53bc06c987f5---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----53bc06c987f5---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----53bc06c987f5---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----53bc06c987f5---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----53bc06c987f5---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----53bc06c987f5---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----53bc06c987f5---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----53bc06c987f5---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----53bc06c987f5---------------------------------------)