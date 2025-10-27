---
title: How I ‘Hacked’ NASA Without Going to Jail
url: https://infosecwriteups.com/how-did-i-hacked-nasa-without-go-to-the-jail-4bf0eebc934b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-21
fetch_date: 2025-10-02T20:28:28.621040
---

# How I ‘Hacked’ NASA Without Going to Jail

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4bf0eebc934b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-did-i-hacked-nasa-without-go-to-the-jail-4bf0eebc934b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-did-i-hacked-nasa-without-go-to-the-jail-4bf0eebc934b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4bf0eebc934b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4bf0eebc934b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How I ‘Hacked’ NASA Without Going to Jail

[![Antonio Rivera Poblete](https://miro.medium.com/v2/resize:fill:64:64/1*siOJ2ehEhoi5wuXduCKMPA.jpeg)](https://medium.com/%40anripo2006?source=post_page---byline--4bf0eebc934b---------------------------------------)

[Antonio Rivera Poblete](https://medium.com/%40anripo2006?source=post_page---byline--4bf0eebc934b---------------------------------------)

2 min read

·

Sep 13, 2025

--

Listen

Share

How you can too…

*Hi, I’m* ***Antonio Rivera****, a Security Researcher, Bug Hunter, and Ethical Hacker. I have secured some companies, received bounties, Hall of Fame mentions* and recived Letters of Appreciation and Recognition*.*

Press enter or click to view image in full size

![]()

## 🌌 Hacking NASA — A Journey Full of Challenges

> Let me tell you — hacking NASA (ethically, of course!) isn’t something that happens overnight. This achievement was the result **of continuous effort, learning, and bug hunting** on their platform.

## 🔍 Now the Actual Thing: The Vulnerability I Found

I was prowling a subdomain something like vuln.nasa.gov poking at it the old-fashioned way: manual tests, small probes, looking for IDORs, CSTI, XSS and the usual suspects.

I clicked into a calendar form just to see what it would do. Nothing flashy: a date picker, a few fields, the kind of UI people build and forget about. I decided to be petty and inject the simplest thing possible a single-quote payload: `'` Immediately, the site crashed.

Not a graceful error page, not a polite “something went wrong” an ugly Django traceback appeared. Debug mode was on. The stack trace spilled internal configuration and environment details that should never leave to the public.

In short, a development convenience had become an open door.

Press enter or click to view image in full size

![]()

## 📅 Timeline of the Report

```
Submitted : 08 Apr 2025
Triaged: 13 Apr 2025
Resolved: 22 May 2025 ✅
LoR: 11 Jun 2025 🎉
```

### The LOR😊:

Press enter or click to view image in full size

![]()

## How to do it:

[## National Aeronautics and Space Administration (NASA) - Vulnerability Disclosure Program | Bugcrowd

### Bugcrowd's bug bounty and vulnerability disclosure platform connects the global security researcher community with your…

bugcrowd.com](https://bugcrowd.com/engagements/nasa-vdp?source=post_page-----4bf0eebc934b---------------------------------------)

Press enter or click to view image in full size

![]()

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----4bf0eebc934b---------------------------------------)

[NASA](https://medium.com/tag/nasa?source=post_page-----4bf0eebc934b---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----4bf0eebc934b---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----4bf0eebc934b---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4bf0eebc934b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4bf0eebc934b---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4bf0eebc934b---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--4bf0eebc934b---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--4bf0eebc934b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Antonio Rivera Poblete](https://miro.medium.com/v2/resize:fill:96:96/1*siOJ2ehEhoi5wuXduCKMPA.jpeg)](https://medium.com/%40anripo2006?source=post_page---post_author_info--4bf0eebc934b---------------------------------------)

[![Antonio Rivera Poblete](https://miro.medium.com/v2/resize:fill:128:128/1*siOJ2ehEhoi5wuXduCKMPA.jpeg)](https://medium.com/%40anripo2006?source=post_page---post_author_info--4bf0eebc934b---------------------------------------)

[## Written by Antonio Rivera Poblete](https://medium.com/%40anripo2006?source=post_page---post_author_info--4bf0eebc934b---------------------------------------)

[45 followers](https://medium.com/%40anripo2006/followers?source=post_page---post_author_info--4bf0eebc934b---------------------------------------)

·[18 following](https://medium.com/%40anripo2006/following?source=post_page---post_author_info--4bf0eebc934b---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----4bf0eebc934b---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----4bf0eebc934b---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----4bf0eebc934b---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----4bf0eebc934b---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----4bf0eebc934b---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----4bf0eebc934b---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----4bf0eebc934b-----------...