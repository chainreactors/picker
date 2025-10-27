---
title: Disabling js for the win
url: https://infosecwriteups.com/disabling-js-for-the-win-9d13c606f910?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-11
fetch_date: 2025-10-04T06:19:59.522960
---

# Disabling js for the win

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F9d13c606f910&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdisabling-js-for-the-win-9d13c606f910&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdisabling-js-for-the-win-9d13c606f910&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-9d13c606f910---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-9d13c606f910---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Disabling js for the win

## ,or how reading the html code w/ care lead to rce through file upload

[![Vuk Ivanovic](https://miro.medium.com/v2/resize:fill:64:64/1*6QX8KKh6p2FhUxOAq1QQ8Q.png)](https://medium.com/%40vuk.ivanovic9000?source=post_page---byline--9d13c606f910---------------------------------------)

[Vuk Ivanovic](https://medium.com/%40vuk.ivanovic9000?source=post_page---byline--9d13c606f910---------------------------------------)

3 min read

·

Feb 10, 2023

--

Share

Javascript. Used practically everywhere, even in your washing machine (this is a joke, I think (: ) And if you really want to know how unavoidable it is just turn off js globally using either extension or manually, and try using any of the popular websites — good luck with that :) I mean, I had js disabled globally some time ago, and I have obvious websites whitelisted for js, which means that every now and again I find myself visiting some website that heavily relies on js, to the point where it’s impossible to read its content without enabling js. But, it has lead me to accessing various admin panels without logging in, if the website relied on js to determine if you should be redirected to the login screen or admin panel (which in most cases is just access to the design/layout of the admin panel without any functionality that relies on authenticated access), but this article is about the recent bug hunt session where I found a functional file upload area that was hidden by the devs instead of being fully removed or better protected. It does require authenticated access though, but even as an authenticated user, the js code verifies if you’re on that page and if so for some reason dev(s) decided to hide the file upload form. Why? Perhaps they knew that a bug was present? Or it was meant to be under construction/patching process?

**Step 1 — Disable js**

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--9d13c606f910---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--9d13c606f910---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--9d13c606f910---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--9d13c606f910---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--9d13c606f910---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Vuk Ivanovic](https://miro.medium.com/v2/resize:fill:96:96/1*6QX8KKh6p2FhUxOAq1QQ8Q.png)](https://medium.com/%40vuk.ivanovic9000?source=post_page---post_author_info--9d13c606f910---------------------------------------)

[![Vuk Ivanovic](https://miro.medium.com/v2/resize:fill:128:128/1*6QX8KKh6p2FhUxOAq1QQ8Q.png)](https://medium.com/%40vuk.ivanovic9000?source=post_page---post_author_info--9d13c606f910---------------------------------------)

[## Written by Vuk Ivanovic](https://medium.com/%40vuk.ivanovic9000?source=post_page---post_author_info--9d13c606f910---------------------------------------)

[808 followers](https://medium.com/%40vuk.ivanovic9000/followers?source=post_page---post_author_info--9d13c606f910---------------------------------------)

·[40 following](https://medium.com/%40vuk.ivanovic9000/following?source=post_page---post_author_info--9d13c606f910---------------------------------------)

IT Security and bug bounty hunting, knowledge collector especially anything with word quantum, and sometimes writer of fiction.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----9d13c606f910---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----9d13c606f910---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----9d13c606f910---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----9d13c606f910---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----9d13c606f910---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----9d13c606f910---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----9d13c606f910---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----9d13c606f910---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----9d13c606f910---------------------------------------)