---
title: Bug Bounty Recon: Tokens, PII, and CI/CD Metadata Leaked via JavaScript
url: https://infosecwriteups.com/bug-bounty-recon-tokens-pii-and-ci-cd-metadata-leaked-via-javascript-76e3c2594957?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-21
fetch_date: 2025-10-06T23:21:35.078614
---

# Bug Bounty Recon: Tokens, PII, and CI/CD Metadata Leaked via JavaScript

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F76e3c2594957&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-recon-tokens-pii-and-ci-cd-metadata-leaked-via-javascript-76e3c2594957&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-recon-tokens-pii-and-ci-cd-metadata-leaked-via-javascript-76e3c2594957&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-76e3c2594957---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-76e3c2594957---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Bug Bounty Recon: Tokens, PII, and CI/CD Metadata Leaked via JavaScript

[![Medusa](https://miro.medium.com/v2/resize:fill:64:64/1*f2U6mEKEJfzwHgsgrqFAXw.jpeg)](https://medusa0xf.medium.com/?source=post_page---byline--76e3c2594957---------------------------------------)

[Medusa](https://medusa0xf.medium.com/?source=post_page---byline--76e3c2594957---------------------------------------)

4 min read

·

Jul 19, 2025

--

3

Share

Press enter or click to view image in full size

![]()

Friend link: <https://medium.com/bugbountywriteup/bug-bounty-recon-tokens-pii-and-ci-cd-metadata-leaked-via-javascript-76e3c2594957?sk=06fa272455d9a2e13839efad005bbc9c>

## Introduction

I was casually looking around a public education website when I stumbled on something unexpected, a JavaScript file packed with sensitive internal data. At first, I thought it was just some leftover debug script, but as I kept scrolling, things got more interesting (and a little concerning).

Inside the file were hardcoded secrets, CI/CD details, internal repository links, email addresses of real employees, and even references to internal comms like Slack and Teams. All of this was publicly accessible which it shouldn’t be.

This blog walks you through how I found it, what kind of data was exposed, and why stuff like this is more common (and dangerous) than people realize. Sometimes you’ll come across things in a JS file that might seem as informative bug. This post will help you learn how to spot the kind of information that’s actually confidential, and why it’s worth keeping an eye out for it.

## Recon: How I Stumbled on It?

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--76e3c2594957---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--76e3c2594957---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--76e3c2594957---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--76e3c2594957---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--76e3c2594957---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Medusa](https://miro.medium.com/v2/resize:fill:96:96/1*f2U6mEKEJfzwHgsgrqFAXw.jpeg)](https://medusa0xf.medium.com/?source=post_page---post_author_info--76e3c2594957---------------------------------------)

[![Medusa](https://miro.medium.com/v2/resize:fill:128:128/1*f2U6mEKEJfzwHgsgrqFAXw.jpeg)](https://medusa0xf.medium.com/?source=post_page---post_author_info--76e3c2594957---------------------------------------)

[## Written by Medusa](https://medusa0xf.medium.com/?source=post_page---post_author_info--76e3c2594957---------------------------------------)

[1.7K followers](https://medusa0xf.medium.com/followers?source=post_page---post_author_info--76e3c2594957---------------------------------------)

·[39 following](https://medium.com/%40medusa0xf/following?source=post_page---post_author_info--76e3c2594957---------------------------------------)

Security Researcher & Content Creator <https://medusa0xf.com/>

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----76e3c2594957---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----76e3c2594957---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----76e3c2594957---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----76e3c2594957---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----76e3c2594957---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----76e3c2594957---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----76e3c2594957---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----76e3c2594957---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----76e3c2594957---------------------------------------)