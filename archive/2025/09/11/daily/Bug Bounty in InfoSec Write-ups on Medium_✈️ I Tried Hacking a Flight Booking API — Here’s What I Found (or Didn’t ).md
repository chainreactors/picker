---
title: ✈️ I Tried Hacking a Flight Booking API — Here’s What I Found (or Didn’t )
url: https://infosecwriteups.com/%EF%B8%8F-i-tried-hacking-a-flight-booking-api-heres-what-i-found-or-didn-t-bc4391b57d41?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-11
fetch_date: 2025-10-02T19:57:55.566517
---

# ✈️ I Tried Hacking a Flight Booking API — Here’s What I Found (or Didn’t )

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fbc4391b57d41&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F%25EF%25B8%258F-i-tried-hacking-a-flight-booking-api-heres-what-i-found-or-didn-t-bc4391b57d41&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F%25EF%25B8%258F-i-tried-hacking-a-flight-booking-api-heres-what-i-found-or-didn-t-bc4391b57d41&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-bc4391b57d41---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-bc4391b57d41---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# ✈️ I Tried Hacking a Flight Booking API — Here’s What I Found (or Didn’t 😅)

[![Varnith](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*OoqHpgt1k8OSVOcL)](https://medium.com/%40varnithy999?source=post_page---byline--bc4391b57d41---------------------------------------)

[Varnith](https://medium.com/%40varnithy999?source=post_page---byline--bc4391b57d41---------------------------------------)

4 min read

·

Sep 3, 2025

--

Share

> “Can you hack your way to a $5.50 flight to New York?” *That’s what I set out to explore — armed with a proxy, curiosity, and way too much coffee.*

Free Article [Link](https://medium.com/%40varnithy999/%EF%B8%8F-i-tried-hacking-a-flight-booking-api-heres-what-i-found-or-didn-t-bc4391b57d41?sk=a970507a65ad6764a8bf537b323e52c3) [Here](https://medium.com/%40varnithy999/%EF%B8%8F-i-tried-hacking-a-flight-booking-api-heres-what-i-found-or-didn-t-bc4391b57d41?sk=a970507a65ad6764a8bf537b323e52c3)

Welcome to my deep dive into a real-world pentesting session targeting a flight booking platform (name redacted for responsible disclosure). This wasn’t a wild zero-day fest, but a **structured, methodical test** that explored some **juicy attack surfaces** — price manipulation, affiliate spoofing, token abuse, replay attacks — the usual suspects in the bug bounty lineup.

Spoiler: The backend held strong. But the ride? Oh, it was worth documenting.

## Recon & First Signs of Fun🕵️‍♂️

My target? Let’s call it **SkyJet** — an airline booking brand with several regional flavors (think SkyJetUS, SkyJetNL, BudgetFly, etc).

While poking around their frontend, I noticed the booking flow made multiple API calls that looked like this:

* `/edge/order/ace` – cart/order creation
* `/edge/order/pax` – passenger details
* `/edge/order/payment` – payment setup

What caught my eye were the **custom headers** being passed along:

* `Affiliate-Internal-Code`
* `Brand`
* `Cid`
* `Checkout-Session`

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--bc4391b57d41---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--bc4391b57d41---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--bc4391b57d41---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--bc4391b57d41---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--bc4391b57d41---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Varnith](https://miro.medium.com/v2/resize:fill:96:96/0*OoqHpgt1k8OSVOcL)](https://medium.com/%40varnithy999?source=post_page---post_author_info--bc4391b57d41---------------------------------------)

[![Varnith](https://miro.medium.com/v2/resize:fill:128:128/0*OoqHpgt1k8OSVOcL)](https://medium.com/%40varnithy999?source=post_page---post_author_info--bc4391b57d41---------------------------------------)

[## Written by Varnith](https://medium.com/%40varnithy999?source=post_page---post_author_info--bc4391b57d41---------------------------------------)

[14 followers](https://medium.com/%40varnithy999/followers?source=post_page---post_author_info--bc4391b57d41---------------------------------------)

·[5 following](https://medium.com/%40varnithy999/following?source=post_page---post_author_info--bc4391b57d41---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----bc4391b57d41---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----bc4391b57d41---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----bc4391b57d41---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----bc4391b57d41---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----bc4391b57d41---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----bc4391b57d41---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----bc4391b57d41---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----bc4391b57d41---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----bc4391b57d41---------------------------------------)