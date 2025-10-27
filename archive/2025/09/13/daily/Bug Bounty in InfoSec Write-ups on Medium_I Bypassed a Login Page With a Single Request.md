---
title: I Bypassed a Login Page With a Single Request
url: https://infosecwriteups.com/i-bypassed-a-login-page-with-a-single-request-cf7b415b2423?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-13
fetch_date: 2025-10-02T20:05:36.142345
---

# I Bypassed a Login Page With a Single Request

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fcf7b415b2423&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-bypassed-a-login-page-with-a-single-request-cf7b415b2423&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-bypassed-a-login-page-with-a-single-request-cf7b415b2423&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-cf7b415b2423---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-cf7b415b2423---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# I Bypassed a Login Page With a Single Request

## How a Misconfigured CDN Led to a Critical Authentication Bypass. A Web Cache Deception bug bounty story.

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:64:64/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---byline--cf7b415b2423---------------------------------------)

[Ibtissam hammadi](https://medium.com/%40ibtissamhammadi1?source=post_page---byline--cf7b415b2423---------------------------------------)

5 min read

·

Sep 12, 2025

--

Share

Press enter or click to view image in full size

![Web Cache Deception attack diagram showing a single request bypassing a login portal.]()

Here’s how I found this critical Web Cache Deception flaw and how you can too.

I was manually testing a target on a private bug bounty program, poking at the login flow. I was looking for the usual suspects: weak tokens, response manipulation, IDORs. I never expected to find a complete **login bypass** with one simple, almost lazy, request.

The vulnerability wasn’t in the application’s logic. It was in a silent, misunderstood conversation between the server and its **CDN**. I’d accidentally triggered a **Web Cache Deception** attack.

**Authentication Bypass** vulnerabilities are the crown jewels of **bug bounty** and **penetration testing**. They are often complex. This one was shockingly simple. It shows how a tiny misconfiguration can open a direct path to user data.

In this write-up, you will see exactly how it was done. No fancy tools are needed, just an understanding of how caches think.

### What is Web Cache Deception? (A Quick Primer)

Imagine a CDN (Content Delivery Network) is a helpful librarian.

You ask for a popular book, *“Great\_Novel.pdf”*. The librarian has a copy behind the desk. They hand you that copy…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--cf7b415b2423---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--cf7b415b2423---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--cf7b415b2423---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--cf7b415b2423---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--cf7b415b2423---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:96:96/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--cf7b415b2423---------------------------------------)

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:128:128/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--cf7b415b2423---------------------------------------)

[## Written by Ibtissam hammadi](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--cf7b415b2423---------------------------------------)

[4.2K followers](https://medium.com/%40ibtissamhammadi1/followers?source=post_page---post_author_info--cf7b415b2423---------------------------------------)

·[98 following](https://medium.com/%40ibtissamhammadi1/following?source=post_page---post_author_info--cf7b415b2423---------------------------------------)

I am a Senior Data Scientist exploring Cybersecurity, Infosec, Programming, and AI technologies.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----cf7b415b2423---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----cf7b415b2423---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----cf7b415b2423---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----cf7b415b2423---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----cf7b415b2423---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----cf7b415b2423---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----cf7b415b2423---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----cf7b415b2423---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----cf7b415b2423---------------------------------------)