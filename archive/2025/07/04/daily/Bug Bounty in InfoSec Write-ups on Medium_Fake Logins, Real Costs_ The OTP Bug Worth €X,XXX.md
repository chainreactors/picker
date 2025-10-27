---
title: Fake Logins, Real Costs: The OTP Bug Worth €X,XXX
url: https://infosecwriteups.com/fake-logins-real-costs-the-otp-bug-worth-x-xxx-74a422791385?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-04
fetch_date: 2025-10-06T23:50:16.561821
---

# Fake Logins, Real Costs: The OTP Bug Worth €X,XXX

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F74a422791385&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffake-logins-real-costs-the-otp-bug-worth-x-xxx-74a422791385&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffake-logins-real-costs-the-otp-bug-worth-x-xxx-74a422791385&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-74a422791385---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-74a422791385---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Fake Logins, Real Costs: The OTP Bug Worth €X,XXX

[![Erkan Kavas](https://miro.medium.com/v2/resize:fill:64:64/1*wcG-Gq6DQdotbzUlkwr0ig.jpeg)](https://medium.com/%40erkankavas?source=post_page---byline--74a422791385---------------------------------------)

[Erkan Kavas](https://medium.com/%40erkankavas?source=post_page---byline--74a422791385---------------------------------------)

3 min read

·

Jul 3, 2025

--

1

Share

In modern mobile apps, account verification via SMS and WhatsApp is standard practice. But what happens when a company skips the most basic check — whether an account even exists?

Press enter or click to view image in full size

![]()

image @ g2.com

In a recent test, I discovered that one electric vehicle (EV) company left the door wide open for abuse in their mobile number verification system. Let’s break down what happened, why it’s dangerous, and how it could cost real money — and even lead to platform bans.

## **Discovery — Recon Process**

The target app, a mobile platform developed by a Southeast Asian electric vehicle startup, offers SMS and WhatsApp verification when a user wants to “log in” or “register.” Sounds normal, right? (Yeah very normal…)

But here’s the catch: the server would happily send a verification message to any number, even if that number was never registered.

All I needed was Burp Suite to intercept the request and change the user first register\_before=true then give phone number. Even if I had never created an account with that number, the system responded as if I had — triggering a real SMS or WhatsApp verification message.

There was no backend check to confirm whether the account existed. (Yeeyy!)

## The Consequences

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--74a422791385---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--74a422791385---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--74a422791385---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--74a422791385---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--74a422791385---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Erkan Kavas](https://miro.medium.com/v2/resize:fill:96:96/1*wcG-Gq6DQdotbzUlkwr0ig.jpeg)](https://medium.com/%40erkankavas?source=post_page---post_author_info--74a422791385---------------------------------------)

[![Erkan Kavas](https://miro.medium.com/v2/resize:fill:128:128/1*wcG-Gq6DQdotbzUlkwr0ig.jpeg)](https://medium.com/%40erkankavas?source=post_page---post_author_info--74a422791385---------------------------------------)

[## Written by Erkan Kavas](https://medium.com/%40erkankavas?source=post_page---post_author_info--74a422791385---------------------------------------)

[625 followers](https://medium.com/%40erkankavas/followers?source=post_page---post_author_info--74a422791385---------------------------------------)

·[685 following](https://medium.com/%40erkankavas/following?source=post_page---post_author_info--74a422791385---------------------------------------)

Cybersecurity Analyst

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----74a422791385---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----74a422791385---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----74a422791385---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----74a422791385---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----74a422791385---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----74a422791385---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----74a422791385---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----74a422791385---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----74a422791385---------------------------------------)