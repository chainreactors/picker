---
title: How I Got an Appreciation Letter from NASA for Finding a Simple Bug
url: https://infosecwriteups.com/how-i-got-an-appreciation-letter-from-nasa-for-finding-a-simple-bug-8812852d0337?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-08-27
fetch_date: 2025-10-06T18:03:29.419300
---

# How I Got an Appreciation Letter from NASA for Finding a Simple Bug

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8812852d0337&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-got-an-appreciation-letter-from-nasa-for-finding-a-simple-bug-8812852d0337&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-got-an-appreciation-letter-from-nasa-for-finding-a-simple-bug-8812852d0337&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8812852d0337---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8812852d0337---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How I Got an Appreciation Letter from NASA for Finding a Simple Bug

[![Om Arora](https://miro.medium.com/v2/resize:fill:64:64/1*U8R9eNJGqjynbAqgcH8uzw@2x.jpeg)](https://omarora1603.medium.com/?source=post_page---byline--8812852d0337---------------------------------------)

[Om Arora](https://omarora1603.medium.com/?source=post_page---byline--8812852d0337---------------------------------------)

3 min read

·

Aug 23, 2024

--

3

Share

So this is a story from when I started Bug Bounties about a year ago, when I posted my first blog “How I found 3 bugs in an hours” which went viral.

One day, while scrolling through LinkedIn, I stumbled upon a post from someone in the cybersecurity community who proudly shared an appreciation letter they had received from NASA. Without a second thought, I looked up NASA’s bug bounty program to understand the scope of their testing environment.

I followed the recon process detailed in one of my earlier blogs which included finding the subdomains, using aquatone, filtering the interesting subdomains, etc, and made a mindmap.

Press enter or click to view image in full size

![]()

### Google Dorking: The First Breakthrough

Then I decided to start with Google Dorking, and started with looking for index of pages

```
site:site.com intitle:index.of
```

and after some time I found two websites with index pages exposed, This is the part of the report —

Press enter or click to view image in full size

![]()

I was very happy to find this even though it is a very small bug because I was just starting out in bug bounties…

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8812852d0337---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8812852d0337---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--8812852d0337---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--8812852d0337---------------------------------------)

·[Last published 2 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--8812852d0337---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Om Arora](https://miro.medium.com/v2/resize:fill:96:96/1*U8R9eNJGqjynbAqgcH8uzw@2x.jpeg)](https://omarora1603.medium.com/?source=post_page---post_author_info--8812852d0337---------------------------------------)

[![Om Arora](https://miro.medium.com/v2/resize:fill:128:128/1*U8R9eNJGqjynbAqgcH8uzw@2x.jpeg)](https://omarora1603.medium.com/?source=post_page---post_author_info--8812852d0337---------------------------------------)

[## Written by Om Arora](https://omarora1603.medium.com/?source=post_page---post_author_info--8812852d0337---------------------------------------)

[2.6K followers](https://omarora1603.medium.com/followers?source=post_page---post_author_info--8812852d0337---------------------------------------)

·[19 following](https://medium.com/%40omarora1603/following?source=post_page---post_author_info--8812852d0337---------------------------------------)

A 20yo Cyber Security Enthusiast currently pursuing Btech 3rd year. Email: omarora1603@gmail.com,[linktr.ee/om1603](http://linktr.ee/om1603) Want to sponsor my content? Let’s collaborate!

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----8812852d0337---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----8812852d0337---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----8812852d0337---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----8812852d0337---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----8812852d0337---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----8812852d0337---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----8812852d0337---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----8812852d0337---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----8812852d0337---------------------------------------)