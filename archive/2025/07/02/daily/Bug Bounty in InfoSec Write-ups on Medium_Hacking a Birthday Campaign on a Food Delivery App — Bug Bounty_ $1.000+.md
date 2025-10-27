---
title: Hacking a Birthday Campaign on a Food Delivery App — Bug Bounty: $1.000+
url: https://infosecwriteups.com/hacking-a-birthday-campaign-on-a-food-delivery-app-bug-bounty-1-000-22926fee1c31?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-02
fetch_date: 2025-10-06T23:50:07.448080
---

# Hacking a Birthday Campaign on a Food Delivery App — Bug Bounty: $1.000+

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F22926fee1c31&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhacking-a-birthday-campaign-on-a-food-delivery-app-bug-bounty-1-000-22926fee1c31&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhacking-a-birthday-campaign-on-a-food-delivery-app-bug-bounty-1-000-22926fee1c31&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-22926fee1c31---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-22926fee1c31---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Hacking a Birthday Campaign on a Food Delivery App — Bug Bounty: $1.000+

[![Erkan Kavas](https://miro.medium.com/v2/resize:fill:64:64/1*wcG-Gq6DQdotbzUlkwr0ig.jpeg)](https://medium.com/%40erkankavas?source=post_page---byline--22926fee1c31---------------------------------------)

[Erkan Kavas](https://medium.com/%40erkankavas?source=post_page---byline--22926fee1c31---------------------------------------)

2 min read

·

Jul 1, 2025

--

2

Share

**Everyone wishes they could celebrate their birthday more than once a year… especially if it comes with free rewards, right?**

While poking around the Android app of a popular food delivery service, I stumbled across a surprising oversight: you can actually change your birthday to **any future date** via a simple request — and claim the birthday campaign rewards **again and again**. 🎉

![]()

image @ pinterest

Here’s what I found, how I tested it, and why this seemingly harmless bug can have a bigger impact than you’d think.

Inside the app, there’s a feature that lets users set their birthday — but only once, during registration. Normally, the date picker prevents you from choosing a date too far in the future… as you’d expect.

But when I looked at the network traffic using tools like Burp Suite and Frida, I noticed something odd: the app sends the birthday to an API endpoint, and **that backend doesn’t actually validate it.** So, I crafted a manual request with a birthday like `"1 January 2030"`... and it worked.

The backend happily accepted it. ✅

This app has a birthday campaign — you set your birthday, and when that day arrives, bam! 🎁 You get special offers: **discounts**, **promos**, maybe even **free food** (depending on how **generous** they’re…

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--22926fee1c31---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--22926fee1c31---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--22926fee1c31---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--22926fee1c31---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--22926fee1c31---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Erkan Kavas](https://miro.medium.com/v2/resize:fill:96:96/1*wcG-Gq6DQdotbzUlkwr0ig.jpeg)](https://medium.com/%40erkankavas?source=post_page---post_author_info--22926fee1c31---------------------------------------)

[![Erkan Kavas](https://miro.medium.com/v2/resize:fill:128:128/1*wcG-Gq6DQdotbzUlkwr0ig.jpeg)](https://medium.com/%40erkankavas?source=post_page---post_author_info--22926fee1c31---------------------------------------)

[## Written by Erkan Kavas](https://medium.com/%40erkankavas?source=post_page---post_author_info--22926fee1c31---------------------------------------)

[625 followers](https://medium.com/%40erkankavas/followers?source=post_page---post_author_info--22926fee1c31---------------------------------------)

·[685 following](https://medium.com/%40erkankavas/following?source=post_page---post_author_info--22926fee1c31---------------------------------------)

Cybersecurity Analyst

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----22926fee1c31---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----22926fee1c31---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----22926fee1c31---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----22926fee1c31---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----22926fee1c31---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----22926fee1c31---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----22926fee1c31---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----22926fee1c31---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----22926fee1c31---------------------------------------)