---
title: How I Found My First 3 Bugs Within An Hour
url: https://infosecwriteups.com/how-i-found-my-first-3-bugs-within-an-hour-5421c0aab8b8?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-08-21
fetch_date: 2025-10-04T11:59:11.581666
---

# How I Found My First 3 Bugs Within An Hour

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F5421c0aab8b8&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-my-first-3-bugs-within-an-hour-5421c0aab8b8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-my-first-3-bugs-within-an-hour-5421c0aab8b8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-5421c0aab8b8---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-5421c0aab8b8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How I Found My First 3 Bugs Within An Hour

[![Om Arora](https://miro.medium.com/v2/resize:fill:64:64/1*U8R9eNJGqjynbAqgcH8uzw@2x.jpeg)](https://omarora1603.medium.com/?source=post_page---byline--5421c0aab8b8---------------------------------------)

[Om Arora](https://omarora1603.medium.com/?source=post_page---byline--5421c0aab8b8---------------------------------------)

4 min read

·

Jul 27, 2023

--

5

Share

Hey Everyone, Welcome to my Blog, Today I am going to discuss about how I found my first 3 bugs in .gov websites within 1 Hour So lets begin

So like most other people I was also stuck in a constant loop of learning and watching bug bounty videos but never actually go looking for vulnerabilities in actual websites. Even when I did I tried finding in websites where competition was high.

So one fine day I decided to pick a target and start hunting on it properly as I knew it was hard finding bugs on paid programs I started finding good VDPs and then I came across **NCIIPC** where we can report any bugs found in .gov websites and even possibly get hall of fame.

Press enter or click to view image in full size

![]()

You can also try it out as it has very less competition, Find more details about it in the following link:

<https://nciipc.gov.in/RVDP.html>

And to report the vulnerability found You can fill the given form and mail it to them:

<https://nciipc.gov.in/documents/Vulnerability_Disclosure_Form.pdf>

So lets talk about how I found the bugs, As I was researching more about the NCIIPC and reading writeups about bugs found on .gov websites I came across a writeup where the author found a broken twitter link in a gov website, The bug is also called broken link hijacking

--

--

5

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5421c0aab8b8---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5421c0aab8b8---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--5421c0aab8b8---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--5421c0aab8b8---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--5421c0aab8b8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Om Arora](https://miro.medium.com/v2/resize:fill:96:96/1*U8R9eNJGqjynbAqgcH8uzw@2x.jpeg)](https://omarora1603.medium.com/?source=post_page---post_author_info--5421c0aab8b8---------------------------------------)

[![Om Arora](https://miro.medium.com/v2/resize:fill:128:128/1*U8R9eNJGqjynbAqgcH8uzw@2x.jpeg)](https://omarora1603.medium.com/?source=post_page---post_author_info--5421c0aab8b8---------------------------------------)

[## Written by Om Arora](https://omarora1603.medium.com/?source=post_page---post_author_info--5421c0aab8b8---------------------------------------)

[2.6K followers](https://omarora1603.medium.com/followers?source=post_page---post_author_info--5421c0aab8b8---------------------------------------)

·[19 following](https://medium.com/%40omarora1603/following?source=post_page---post_author_info--5421c0aab8b8---------------------------------------)

A 20yo Cyber Security Enthusiast currently pursuing Btech 3rd year. Email: omarora1603@gmail.com,[linktr.ee/om1603](http://linktr.ee/om1603) Want to sponsor my content? Let’s collaborate!

## Responses (5)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----5421c0aab8b8---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----5421c0aab8b8---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----5421c0aab8b8---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----5421c0aab8b8---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----5421c0aab8b8---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----5421c0aab8b8---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----5421c0aab8b8---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----5421c0aab8b8---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----5421c0aab8b8---------------------------------------)