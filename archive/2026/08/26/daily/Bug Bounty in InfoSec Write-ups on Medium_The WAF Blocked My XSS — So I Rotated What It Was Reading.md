---
title: The WAF Blocked My XSS — So I Rotated What It Was Reading
url: https://infosecwriteups.com/the-waf-blocked-my-xss-so-i-rotated-what-it-was-reading-47bc630c17ae?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-08-26
fetch_date: 2026-08-27T12:12:34.321483
---

# The WAF Blocked My XSS — So I Rotated What It Was Reading

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-waf-blocked-my-xss-so-i-rotated-what-it-was-reading-47bc630c17ae&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-waf-blocked-my-xss-so-i-rotated-what-it-was-reading-47bc630c17ae&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-47bc630c17ae---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-47bc630c17ae---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page---header_tags--47bc630c17ae---------------------------------------)

[Xss](https://medium.com/tag/xs?source=post_page---header_tags--47bc630c17ae---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page---header_tags--47bc630c17ae---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page---header_tags--47bc630c17ae---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page---header_tags--47bc630c17ae---------------------------------------)

# The WAF Blocked My XSS — So I Rotated What It Was Reading

[![Nitin yadav](https://miro.medium.com/v2/resize:fill:64:64/1*46gfQYRZ6po8nWu68GB5LA.png)](https://kd-200.medium.com/?source=post_page---byline--47bc630c17ae---------------------------------------)

[Nitin yadav](https://kd-200.medium.com/?source=post_page---byline--47bc630c17ae---------------------------------------)

5 min read

·

Aug 8, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D47bc630c17ae&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-waf-blocked-my-xss-so-i-rotated-what-it-was-reading-47bc630c17ae&source=---header_actions--47bc630c17ae---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

What’s up everyone! Nitin here 👋

Real talk: the WAF is not there to stop you. It’s there to stop the *first payload you copy-pasted from a tweet*. That’s it. The moment you understand that, half of these “unexploitable” open redirects turn into real, paying XSS bugs. This is the post I wish someone handed me when I was staring at an Akamai block page thinking the bug was dead. It’s not dead — you just knocked on the front door when the whole point is to walk around the back.

## Why open redirect + XSS live in the same house

Most hunters treat these as two separate bugs. That’s the mistake. An open redirect is you controlling **where the browser goes next**. XSS is you controlling **what the browser executes**. The bridge between them is the humble `javascript:` URI scheme.

When a redirect param drops your value into `Location: <your-value>` or into client-side code like `window.location = params.get('next')`, you don't just control a destination — you potentially control a *scheme*. And `javascript:alert(document.domain)` is a perfectly valid URL scheme as far as a browser is concerned.

> Open redirect = “I control the URL.” If I control the URL, I might control the scheme. If I control the scheme, javascript: = XSS.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--47bc630c17ae---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--47bc630c17ae---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--47bc630c17ae---------------------------------------)

[88K followers](/followers?source=post_page---post_publication_info--47bc630c17ae---------------------------------------)

·[Last published 1 day ago](/one-email-one-click-one-enterprise-wide-ransomware-incident-995808f1150a?source=post_page---post_publication_info--47bc630c17ae---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Nitin yadav](https://miro.medium.com/v2/resize:fill:96:96/1*46gfQYRZ6po8nWu68GB5LA.png)](https://kd-200.medium.com/?source=post_page---post_author_info--47bc630c17ae---------------------------------------)

[![Nitin yadav](https://miro.medium.com/v2/resize:fill:128:128/1*46gfQYRZ6po8nWu68GB5LA.png)](https://kd-200.medium.com/?source=post_page---post_author_info--47bc630c17ae---------------------------------------)

[## Written by Nitin yadav](https://kd-200.medium.com/?source=post_page---post_author_info--47bc630c17ae---------------------------------------)

[714 followers](https://kd-200.medium.com/followers?source=post_page---post_author_info--47bc630c17ae---------------------------------------)

·[14 following](https://medium.com/%40kd-200/following?source=post_page---post_author_info--47bc630c17ae---------------------------------------)

Computer Science Student | Bug Hunter | Cyber Security Enthusiast | Contact : <https://linktr.ee/ydv_nitin>

[Help](https://help.medium.com/hc/en-us?source=post_page-----47bc630c17ae---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----47bc630c17ae---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----47bc630c17ae---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----47bc630c17ae---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----47bc630c17ae---------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----47bc630c17ae---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----47bc630c17ae---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----47bc630c17ae---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----...