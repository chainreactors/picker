---
title: Dorks For Sensitive Information Disclosure Part-2
url: https://infosecwriteups.com/dorks-for-sensitive-information-disclosure-part-2-4355b479d2aa?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-08
fetch_date: 2025-10-07T00:16:43.965652
---

# Dorks For Sensitive Information Disclosure Part-2

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4355b479d2aa&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdorks-for-sensitive-information-disclosure-part-2-4355b479d2aa&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdorks-for-sensitive-information-disclosure-part-2-4355b479d2aa&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4355b479d2aa---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4355b479d2aa---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Dorks For Sensitive Information Disclosure Part-2

[![Devansh Patel](https://miro.medium.com/v2/resize:fill:64:64/1*UbOj48VcY7qPnQSGWQhuaA.jpeg)](https://medium.com/%40devanshpatel930?source=post_page---byline--4355b479d2aa---------------------------------------)

[Devansh Patel](https://medium.com/%40devanshpatel930?source=post_page---byline--4355b479d2aa---------------------------------------)

3 min read

·

Jul 22, 2025

--

Share

Oh Look, Your Secrets Are on Google (Again)

Press enter or click to view image in full size

![]()

## 📖 The Dork Library

Below are categories of useful dorks, each with examples you can drop into Google as-is.
 Just replace `example.com` with your own target domain if you’d like.

I used these a lot for OSINT and BugBounty Purposes and also if you haven’t checked out our first part check that

[## Dorks For Sensitive Information Disclosure

### Hello everyone, This is my 6th Blog first about Bugs and Bug bounty

medium.com](https://medium.com/%40devanshpatel930/dorks-for-sensitive-information-disclosure-31fb90ad6f21?source=post_page-----4355b479d2aa---------------------------------------)

> If you can’t read further there a [**free link**](https://medium.com/%40devanshpatel930/dorks-for-sensitive-information-disclosure-part-2-4355b479d2aa?sk=34babb3bfc29e5f799d006f69a829b23) Brother *🤑*

## 1. Exposed `.git` Repositories

Developers sometimes leave `.git/` folders accessible on web servers.
 These can reveal source code, commit history, and credential

```
inurl:"/.git" example.com -github
```

What’s happening here?
 We’re asking Google to find URLs on `example.com` that include `.git`, but excluding results from GitHub.

## 2. Backup Files

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4355b479d2aa---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4355b479d2aa---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4355b479d2aa---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--4355b479d2aa---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--4355b479d2aa---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Devansh Patel](https://miro.medium.com/v2/resize:fill:96:96/1*UbOj48VcY7qPnQSGWQhuaA.jpeg)](https://medium.com/%40devanshpatel930?source=post_page---post_author_info--4355b479d2aa---------------------------------------)

[![Devansh Patel](https://miro.medium.com/v2/resize:fill:128:128/1*UbOj48VcY7qPnQSGWQhuaA.jpeg)](https://medium.com/%40devanshpatel930?source=post_page---post_author_info--4355b479d2aa---------------------------------------)

[## Written by Devansh Patel](https://medium.com/%40devanshpatel930?source=post_page---post_author_info--4355b479d2aa---------------------------------------)

[78 followers](https://medium.com/%40devanshpatel930/followers?source=post_page---post_author_info--4355b479d2aa---------------------------------------)

·[9 following](https://medium.com/%40devanshpatel930/following?source=post_page---post_author_info--4355b479d2aa---------------------------------------)

Hacking legally so companies don’t get hacked illegally. Cybersecurity analyst | Bug bounty hunter | Breaking things so others can call it ‘secure’

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----4355b479d2aa---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----4355b479d2aa---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----4355b479d2aa---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----4355b479d2aa---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----4355b479d2aa---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----4355b479d2aa---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----4355b479d2aa---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----4355b479d2aa---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----4355b479d2aa---------------------------------------)