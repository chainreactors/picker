---
title: Extract — Load — Upload | A $20000 File Read Bug POC Methodology
url: https://infosecwriteups.com/extract-load-upload-a-20000-file-read-bug-poc-methodology-931383c987b2?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-19
fetch_date: 2025-10-02T20:21:45.165602
---

# Extract — Load — Upload | A $20000 File Read Bug POC Methodology

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F931383c987b2&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fextract-load-upload-a-20000-file-read-bug-poc-methodology-931383c987b2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fextract-load-upload-a-20000-file-read-bug-poc-methodology-931383c987b2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-931383c987b2---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-931383c987b2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Extract — Load — Upload | A $20000 File Read Bug POC Methodology

[![It4chis3c](https://miro.medium.com/v2/resize:fill:64:64/1*ekYPXyjIXBk7Zvd1Tb0oBw.jpeg)](https://it4chis3c.medium.com/?source=post_page---byline--931383c987b2---------------------------------------)

[It4chis3c](https://it4chis3c.medium.com/?source=post_page---byline--931383c987b2---------------------------------------)

4 min read

·

Sep 13, 2025

--

5

Share

Visual & Practical Breakdown of one of the highest paid arbitrary file read vulnerability POC

[Friend Link | Free Link](https://it4chis3c.medium.com/extract-load-upload-a-20000-file-read-bug-poc-methodology-931383c987b2?sk=381576654c90a69c97cdaded8cbfadff)

Hi geeks, ***it4chis3c*** ([Twitter](https://x.com/it4chis3c)) came-up with another bounty earning write-up in the Bug Bounty Hunting Series:

![It4chis3c](https://miro.medium.com/v2/resize:fill:40:40/1*ekYPXyjIXBk7Zvd1Tb0oBw.jpeg)

[It4chis3c](https://it4chis3c.medium.com/?source=post_page-----931383c987b2---------------------------------------)

## Bug Bounty Hunting Series

[View list](https://it4chis3c.medium.com/list/bug-bounty-hunting-series-fb1cd38823f1?source=post_page-----931383c987b2---------------------------------------)

43 stories

![](https://miro.medium.com/v2/resize:fill:388:388/1*5-rzwuDYy6rm9GggmhkRtw.png)

![](https://miro.medium.com/v2/resize:fill:388:388/1*3W5rcFkvh_LYTEoEzjEs6Q.png)

![](https://miro.medium.com/v2/resize:fill:388:388/1*JH5F-vhNDF3wXYiMLIbN_w.png)

Press enter or click to view image in full size

![]()

Credit: Gemini | Imagen

Here’s a breakdown write-up of another high paid bounty on a simple bug: [File Read via bulk imports UploadsPipeline](https://hackerone.com/reports/1439593) (reported by [William Bowling aka vakzz](https://hackerone.com/vakzz?type=user)).

On observation I found out that this bug is following a certain workflow provided in below chart diagram:

Press enter or click to view image in full size

![]()

To understand this bug you have to know what ***symlink***actually means.
“*A Symlink also referred as Symbolic Link or Soft Link is a file that acts as a shortcut or pointer to another file or directory in a file system.*”

**The Flaw:**

--

--

5

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--931383c987b2---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--931383c987b2---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--931383c987b2---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--931383c987b2---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--931383c987b2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![It4chis3c](https://miro.medium.com/v2/resize:fill:96:96/1*ekYPXyjIXBk7Zvd1Tb0oBw.jpeg)](https://it4chis3c.medium.com/?source=post_page---post_author_info--931383c987b2---------------------------------------)

[![It4chis3c](https://miro.medium.com/v2/resize:fill:128:128/1*ekYPXyjIXBk7Zvd1Tb0oBw.jpeg)](https://it4chis3c.medium.com/?source=post_page---post_author_info--931383c987b2---------------------------------------)

[## Written by It4chis3c](https://it4chis3c.medium.com/?source=post_page---post_author_info--931383c987b2---------------------------------------)

[2.5K followers](https://it4chis3c.medium.com/followers?source=post_page---post_author_info--931383c987b2---------------------------------------)

·[27 following](https://medium.com/%40it4chis3c/following?source=post_page---post_author_info--931383c987b2---------------------------------------)

Security Researcher | Bug Bounties | Tips & Tricks

## Responses (5)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----931383c987b2---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----931383c987b2---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----931383c987b2---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----931383c987b2---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----931383c987b2---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----931383c987b2---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----931383c987b2---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----931383c987b2---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----931383c987b2---------------------------------------)