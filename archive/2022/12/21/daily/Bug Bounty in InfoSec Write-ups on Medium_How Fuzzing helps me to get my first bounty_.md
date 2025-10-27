---
title: How Fuzzing helps me to get my first bounty?
url: https://infosecwriteups.com/how-fuzzing-helps-me-to-get-my-first-bounty-2c63eb864e08?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-21
fetch_date: 2025-10-04T02:04:55.852067
---

# How Fuzzing helps me to get my first bounty?

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2c63eb864e08&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-fuzzing-helps-me-to-get-my-first-bounty-2c63eb864e08&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-fuzzing-helps-me-to-get-my-first-bounty-2c63eb864e08&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2c63eb864e08---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2c63eb864e08---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How Fuzzing helps me to get my first bounty?

[![Praveen Mali (PMMALI)](https://miro.medium.com/v2/resize:fill:64:64/1*mVjG0Iw3pBjMx5xaaWQCgw.png)](https://pmmali.medium.com/?source=post_page---byline--2c63eb864e08---------------------------------------)

[Praveen Mali (PMMALI)](https://pmmali.medium.com/?source=post_page---byline--2c63eb864e08---------------------------------------)

2 min read

·

May 31, 2022

--

3

Listen

Share

![]()

Hello Everyone,

I’m [Praveen Mali](https://www.linkedin.com/in/praveen-mali/) (PMMALI). This is my first writeup and in this writeup I will tell you how fuzzing leads me to my first bounty.

So I was testing the target let say target.com and lots of domains and sub-domains are in scope. On one of the subdomain I saw a default SMS Service page that they were using.

Press enter or click to view image in full size

![]()

Then suddenly my mind triggers me to fuzz for the endpoints.
I fuzz the subdomain with [FFuF](https://github.com/ffuf/ffuf).
Command was: ffuf -w fuzz-Bo0oM.txt -u <https://sms-express.target.com/FUZZ> -mc 200 -ac -recursion

I got one of the endpoint’s status code 200 and the endpoint was .gitignore.

I open the url in browser with the endpoint <https://sms-express.target.com/.gitignore> and one file was downloaded.
There were lots of path of more sensitive directories.

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

I immediately reported the bug and got $100 bounty (My first bounty).

Press enter or click to view image in full size

![]()

Thank you so much for reading 🙏

My LinkedIn ID: <https://www.linkedin.com/in/praveen-mali/>

My Twitter ID: <https://twitter.com/pmmali_>

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----2c63eb864e08---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----2c63eb864e08---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----2c63eb864e08---------------------------------------)

[Hunting](https://medium.com/tag/hunting?source=post_page-----2c63eb864e08---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----2c63eb864e08---------------------------------------)

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2c63eb864e08---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2c63eb864e08---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--2c63eb864e08---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--2c63eb864e08---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--2c63eb864e08---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Praveen Mali (PMMALI)](https://miro.medium.com/v2/resize:fill:96:96/1*mVjG0Iw3pBjMx5xaaWQCgw.png)](https://pmmali.medium.com/?source=post_page---post_author_info--2c63eb864e08---------------------------------------)

[![Praveen Mali (PMMALI)](https://miro.medium.com/v2/resize:fill:128:128/1*mVjG0Iw3pBjMx5xaaWQCgw.png)](https://pmmali.medium.com/?source=post_page---post_author_info--2c63eb864e08---------------------------------------)

[## Written by Praveen Mali (PMMALI)](https://pmmali.medium.com/?source=post_page---post_author_info--2c63eb864e08---------------------------------------)

[56 followers](https://pmmali.medium.com/followers?source=post_page---post_author_info--2c63eb864e08---------------------------------------)

·[5 following](https://medium.com/%40pmmali/following?source=post_page---post_author_info--2c63eb864e08---------------------------------------)

I am a cybersecurity analyst and part-time bug bounty hunter with a passion for staying up-to-date on the latest security threats and trends.

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----2c63eb864e08---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----2c63eb864e08---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----2c63eb864e08---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----2c63eb864e08---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----2c63eb864e08---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----2c63eb864e08---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----2c63eb864e08---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----2c63eb864e08---------------------------------------)
...