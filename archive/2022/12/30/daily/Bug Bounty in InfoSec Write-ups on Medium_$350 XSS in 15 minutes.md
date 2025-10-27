---
title: $350 XSS in 15 minutes
url: https://infosecwriteups.com/350-xss-in-15-minutes-dcb74ad93d5f?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-30
fetch_date: 2025-10-04T02:43:57.855277
---

# $350 XSS in 15 minutes

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fdcb74ad93d5f&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F350-xss-in-15-minutes-dcb74ad93d5f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F350-xss-in-15-minutes-dcb74ad93d5f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-dcb74ad93d5f---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-dcb74ad93d5f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# $350 XSS in 15 minutes

## Bug Bounty Writeup about DOM XSS via JSONP + Parameter pollution

[![Anton (therceman)](https://miro.medium.com/v2/resize:fill:64:64/1*ya4CrhcriQRsR6QTK_3FJg.png)](https://therceman.medium.com/?source=post_page---byline--dcb74ad93d5f---------------------------------------)

[Anton (therceman)](https://therceman.medium.com/?source=post_page---byline--dcb74ad93d5f---------------------------------------)

3 min read

·

Dec 23, 2022

--

7

Share

Press enter or click to view image in full size

![Bug Bounty Writeup: $350 XSS in 15 minutes]()

Photo by [Pepi Stojanovski](https://unsplash.com/%40timbatec?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Hello 👋

This is my first and last Bug Bounty Writeup this year. 😀

I am sharing with you my latest XSS finding, which I’ve found 2 weeks ago.

This was the fastest and a bit unusual flow that I normally do when I search for XSS.

So let’s dive in…

* Company asked me to retest an old XSS report.
* I’ve checked that XSS and confirmed that it was fixed properly.
* The specific endpoint had `name` a param that was vulnerable to Reflected XSS injection.

```
example.com/profile?name=<img+src=1+onerror=alert(1337)>
```

* I’ve started to search for a bypass and used the Search function in Chrome Developer tools to search this endpoint `/profile` in all JS files to check for another vulnerable param, but found another endpoint:

```
example.com/services
```

* The first idea that came to my mind was to put this URL in the google search engine and see if this endpoint was cached somewhere on the google web space with params.
* After the first try, I found a cached endpoint with params on the first page of the results, the endpoint had ID…

--

--

7

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--dcb74ad93d5f---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--dcb74ad93d5f---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--dcb74ad93d5f---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--dcb74ad93d5f---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--dcb74ad93d5f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Anton (therceman)](https://miro.medium.com/v2/resize:fill:96:96/1*ya4CrhcriQRsR6QTK_3FJg.png)](https://therceman.medium.com/?source=post_page---post_author_info--dcb74ad93d5f---------------------------------------)

[![Anton (therceman)](https://miro.medium.com/v2/resize:fill:128:128/1*ya4CrhcriQRsR6QTK_3FJg.png)](https://therceman.medium.com/?source=post_page---post_author_info--dcb74ad93d5f---------------------------------------)

[## Written by Anton (therceman)](https://therceman.medium.com/?source=post_page---post_author_info--dcb74ad93d5f---------------------------------------)

[2.1K followers](https://therceman.medium.com/followers?source=post_page---post_author_info--dcb74ad93d5f---------------------------------------)

·[3.9K following](https://medium.com/%40therceman/following?source=post_page---post_author_info--dcb74ad93d5f---------------------------------------)

💰 Bug Bounty Hunter 💻 Software Developer 🌐 [www.therceman.dev](http://www.therceman.dev)

## Responses (7)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----dcb74ad93d5f---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----dcb74ad93d5f---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----dcb74ad93d5f---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----dcb74ad93d5f---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----dcb74ad93d5f---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----dcb74ad93d5f---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----dcb74ad93d5f---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----dcb74ad93d5f---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----dcb74ad93d5f---------------------------------------)