---
title: How a Failed Payment on a Train Platform Earned Me $400
url: https://infosecwriteups.com/how-a-failed-payment-on-a-train-platform-earned-me-400-23241d204550?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-10
fetch_date: 2025-10-02T19:54:04.858390
---

# How a Failed Payment on a Train Platform Earned Me $400

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F23241d204550&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-a-failed-payment-on-a-train-platform-earned-me-400-23241d204550&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-a-failed-payment-on-a-train-platform-earned-me-400-23241d204550&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-23241d204550---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-23241d204550---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How a Failed Payment on a Train Platform Earned Me $400

[![Hackergod00001](https://miro.medium.com/v2/resize:fill:64:64/1*nzbuvQ-GxktZyqC2ttia3w.jpeg)](https://hackergod00001.medium.com/?source=post_page---byline--23241d204550---------------------------------------)

[Hackergod00001](https://hackergod00001.medium.com/?source=post_page---byline--23241d204550---------------------------------------)

5 min read

·

Sep 9, 2025

--

1

Share

This isn’t another bug bounty story meant to make your eyes sparkle with massive payouts. This is the story of how a normal, boring evening, a forgotten bill and a glitchy app launched my bug bounty journey. And more importantly, it’s about how you can start seeing the world with a hacker’s mindset, too.

> A Perfect example of how a normal, frustrating experience turns into a bug hunter’s **aha!** moment.

Press enter or click to view image in full size

![]()

Photo by [Gilley Aguilar](https://unsplash.com/%40gilleyaguilar?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

It all started around 8 PM on a noisy train platform. The train was late and I was just scrolling on my phone when that sinking feeling hit me — I forgot to pay my credit card bill.

I quickly pulled up a popular payment app I used — let’s call it **PayApp** — to handle the transaction. I went through the steps, entered the amount and hit **“Pay”**. A loading spinner appeared, then a message flashed on the screen:

> **“Payment Failed.”**

**Great,** then another message pops saying:

> **“Bank server is down again.”**

Press enter or click to view image in full size

![]()

Photo by [Andy Vult](https://unsplash.com/%40andyvult?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Annoying, but it happens. I was about to put my phone back in my pocket when a notification from my bank popped up:

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--23241d204550---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--23241d204550---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--23241d204550---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--23241d204550---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--23241d204550---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Hackergod00001](https://miro.medium.com/v2/resize:fill:96:96/1*nzbuvQ-GxktZyqC2ttia3w.jpeg)](https://hackergod00001.medium.com/?source=post_page---post_author_info--23241d204550---------------------------------------)

[![Hackergod00001](https://miro.medium.com/v2/resize:fill:128:128/1*nzbuvQ-GxktZyqC2ttia3w.jpeg)](https://hackergod00001.medium.com/?source=post_page---post_author_info--23241d204550---------------------------------------)

[## Written by Hackergod00001](https://hackergod00001.medium.com/?source=post_page---post_author_info--23241d204550---------------------------------------)

[961 followers](https://hackergod00001.medium.com/followers?source=post_page---post_author_info--23241d204550---------------------------------------)

·[11 following](https://medium.com/%40hackergod00001/following?source=post_page---post_author_info--23241d204550---------------------------------------)

I am Upmanyu Jha AKA Hackergod00001, a Machine Learning Engineer By Day and a Bug Bounty Hunter by Night

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----23241d204550---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----23241d204550---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----23241d204550---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----23241d204550---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----23241d204550---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----23241d204550---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----23241d204550---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----23241d204550---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----23241d204550---------------------------------------)