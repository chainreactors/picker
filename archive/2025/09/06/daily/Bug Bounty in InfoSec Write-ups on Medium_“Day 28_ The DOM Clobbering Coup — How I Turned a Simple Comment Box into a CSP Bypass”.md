---
title: “Day 28: The DOM Clobbering Coup — How I Turned a Simple Comment Box into a CSP Bypass”
url: https://infosecwriteups.com/day-28-the-dom-clobbering-coup-how-i-turned-a-simple-comment-box-into-a-csp-bypass-109af0e954a6?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-06
fetch_date: 2025-10-02T19:44:22.085681
---

# “Day 28: The DOM Clobbering Coup — How I Turned a Simple Comment Box into a CSP Bypass”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F109af0e954a6&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-28-the-dom-clobbering-coup-how-i-turned-a-simple-comment-box-into-a-csp-bypass-109af0e954a6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-28-the-dom-clobbering-coup-how-i-turned-a-simple-comment-box-into-a-csp-bypass-109af0e954a6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-109af0e954a6---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-109af0e954a6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# “Day 28: The DOM Clobbering Coup — How I Turned a Simple Comment Box into a CSP Bypass”

## Hijacking JavaScript with Nothing But HTML and a Quirk of the Browser

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--109af0e954a6---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--109af0e954a6---------------------------------------)

5 min read

·

Sep 4, 2025

--

Share

Welcome to Day 28! Today’s vulnerability is one of my favorites because it feels like magic. The target was a news site with a strict Content Security Policy (CSP) that blocked all inline scripts and only allowed scripts from trusted domains. This made classic XSS nearly impossible. The site had a comment section that allowed limited HTML tags (`<a>`, `<img>`, `<div>`). My goal wasn't to inject script; it was to inject *structure*. By abusing an ancient browser behavior called DOM Clobbering, I was able to hijack the page's JavaScript without executing a single line of code myself. The result was a full CSP bypass and a $3000 bounty.

[FREE LINK](https://amannsharmaa.medium.com/day-28-the-dom-clobbering-coup-how-i-turned-a-simple-comment-box-into-a-csp-bypass-109af0e954a6?sk=420c3fc98b0a1aca8c1544a9c0a6c170)

Press enter or click to view image in full size

![]()

## What is DOM Clobbering?

DOM Clobbering is an attack where HTML injection is used to overwrite JavaScript properties and variables in the global scope. It exploits the fact that browsers automatically create references to HTML elements with `id` or `name` attributes in the global `window` object.

The Magic Trick:

> *If you inject* `<a id="config">`*, you can access it in JavaScript as* `window.config`*. If the app has a variable*…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--109af0e954a6---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--109af0e954a6---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--109af0e954a6---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--109af0e954a6---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--109af0e954a6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--109af0e954a6---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--109af0e954a6---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--109af0e954a6---------------------------------------)

[739 followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--109af0e954a6---------------------------------------)

·[14 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--109af0e954a6---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----109af0e954a6---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----109af0e954a6---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----109af0e954a6---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----109af0e954a6---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----109af0e954a6---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----109af0e954a6---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----109af0e954a6---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----109af0e954a6---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----109af0e954a6---------------------------------------)