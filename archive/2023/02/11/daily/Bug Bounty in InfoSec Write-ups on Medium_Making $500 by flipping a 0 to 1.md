---
title: Making $500 by flipping a 0 to 1
url: https://infosecwriteups.com/making-500-by-flipping-a-0-to-1-d2f5a36f3f84?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-11
fetch_date: 2025-10-04T06:20:09.760139
---

# Making $500 by flipping a 0 to 1

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd2f5a36f3f84&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmaking-500-by-flipping-a-0-to-1-d2f5a36f3f84&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmaking-500-by-flipping-a-0-to-1-d2f5a36f3f84&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d2f5a36f3f84---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d2f5a36f3f84---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Making $500 by flipping a 0 to 1

[![Adam J Sturge](https://miro.medium.com/v2/resize:fill:64:64/1*AX1cAqP11mihW4R-ONoVTA.png)](https://adamjsturge.medium.com/?source=post_page---byline--d2f5a36f3f84---------------------------------------)

[Adam J Sturge](https://adamjsturge.medium.com/?source=post_page---byline--d2f5a36f3f84---------------------------------------)

3 min read

·

Feb 9, 2023

--

Share

I recently found my first vulnerability in the wild. The vulnerability was a P1 and all I had to do was turn a 0 into a 1.

Press enter or click to view image in full size

![]()

Photo by [Moritz Erken](https://unsplash.com/%40moritzerken?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

## Setting up the attacker environment

The app was one that I used multiple times a week. I knew someone who worked with it a lot, and he was friends with the founder of the app. I was told that it was very secure, but I realized it was only because no one knew how to intercept an app to get any http request. I immediately went to setup Burp to go through my Android device, but because of limitations, I had to use an emulator and decided to write a guide shortly after submitting my report.

[## Burp Suite Android Emulator

### Guide to setup Burp Suite on your Android Emulator

infosecwriteups.com](/burp-suite-android-emulator-5c030d420394?source=post_page-----d2f5a36f3f84---------------------------------------)

## Finding the Vulnerability

After figuring out how to get the emulator working (which took longer than finding the vulnerability), I started to use the app as I normally would. Reading all the http history in burp.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d2f5a36f3f84---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d2f5a36f3f84---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--d2f5a36f3f84---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--d2f5a36f3f84---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--d2f5a36f3f84---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Adam J Sturge](https://miro.medium.com/v2/resize:fill:96:96/1*AX1cAqP11mihW4R-ONoVTA.png)](https://adamjsturge.medium.com/?source=post_page---post_author_info--d2f5a36f3f84---------------------------------------)

[![Adam J Sturge](https://miro.medium.com/v2/resize:fill:128:128/1*AX1cAqP11mihW4R-ONoVTA.png)](https://adamjsturge.medium.com/?source=post_page---post_author_info--d2f5a36f3f84---------------------------------------)

[## Written by Adam J Sturge](https://adamjsturge.medium.com/?source=post_page---post_author_info--d2f5a36f3f84---------------------------------------)

[369 followers](https://adamjsturge.medium.com/followers?source=post_page---post_author_info--d2f5a36f3f84---------------------------------------)

·[21 following](https://medium.com/%40adamjsturge/following?source=post_page---post_author_info--d2f5a36f3f84---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----d2f5a36f3f84---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----d2f5a36f3f84---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----d2f5a36f3f84---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----d2f5a36f3f84---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----d2f5a36f3f84---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----d2f5a36f3f84---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----d2f5a36f3f84---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----d2f5a36f3f84---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----d2f5a36f3f84---------------------------------------)