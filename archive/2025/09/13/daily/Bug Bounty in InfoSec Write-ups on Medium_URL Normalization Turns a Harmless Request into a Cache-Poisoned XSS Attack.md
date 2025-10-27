---
title: URL Normalization Turns a Harmless Request into a Cache-Poisoned XSS Attack
url: https://infosecwriteups.com/url-normalization-turns-a-harmless-request-into-a-cache-poisoned-xss-attack-57d1a68f08d2?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-13
fetch_date: 2025-10-02T20:05:33.770292
---

# URL Normalization Turns a Harmless Request into a Cache-Poisoned XSS Attack

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F57d1a68f08d2&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Furl-normalization-turns-a-harmless-request-into-a-cache-poisoned-xss-attack-57d1a68f08d2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Furl-normalization-turns-a-harmless-request-into-a-cache-poisoned-xss-attack-57d1a68f08d2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-57d1a68f08d2---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-57d1a68f08d2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# URL Normalization Turns a Harmless Request into a Cache-Poisoned XSS Attack

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:64:64/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---byline--57d1a68f08d2---------------------------------------)

[Bash Overflow](https://bashoverflow.com/?source=post_page---byline--57d1a68f08d2---------------------------------------)

4 min read

·

Sep 10, 2025

--

Share

**Learn how URL normalization flaws can lead to cache poisoning and cross-site scripting (XSS)**.

🔓 [**Free Link**](https://bashoverflow.com/57d1a68f08d2?sk=055aedaf71cc12ab530d5258081fd99d)

Press enter or click to view image in full size

![URL Normalization Turns a Harmless Request into a Cache-Poisoned XSS Attack — Bashoverflow Medium]()

URL Normalization Turns a Harmless Request into a Cache-Poisoned XSS Attack

> **Disclaimer:**
> The techniques described in this document are intended solely for ethical use and educational purposes. Unauthorized use of these methods outside approved environments is strictly prohibited, as it is illegal, unethical, and may lead to severe consequences.
>
> It is crucial to act responsibly, comply with all applicable laws, and adhere to established ethical guidelines. Any activity that exploits security vulnerabilities or compromises the safety, privacy, or integrity of others is strictly forbidden.

## Table of Contents

1. [**Summary of the Vulnerability**](#1f69)
2. [**Steps to Reproduce & Proof of Concept (PoC)**](#aa26)
3. [**Impact**](#c088)

## Summary of the Vulnerability

In this lab, the core weakness lies in how the web cache and browser handle URLs differently. The application contains an XSS vulnerability, but browsers automatically apply URL-encoding, which prevents the payload from executing directly. However, the cache performs ***normalization*** of the URL before storing and serving it.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--57d1a68f08d2---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--57d1a68f08d2---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--57d1a68f08d2---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--57d1a68f08d2---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--57d1a68f08d2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:96:96/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---post_author_info--57d1a68f08d2---------------------------------------)

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:128:128/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---post_author_info--57d1a68f08d2---------------------------------------)

[## Written by Bash Overflow](https://bashoverflow.com/?source=post_page---post_author_info--57d1a68f08d2---------------------------------------)

[150 followers](https://bashoverflow.com/followers?source=post_page---post_author_info--57d1a68f08d2---------------------------------------)

·[11 following](https://medium.com/%40bashoverflow/following?source=post_page---post_author_info--57d1a68f08d2---------------------------------------)

Cybersecurity Enthusiast | Sharing insights through some writeups | Passionate about advancing knowledge in the field of cybersecurity

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----57d1a68f08d2---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----57d1a68f08d2---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----57d1a68f08d2---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----57d1a68f08d2---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----57d1a68f08d2---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----57d1a68f08d2---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----57d1a68f08d2---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----57d1a68f08d2---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----57d1a68f08d2---------------------------------------)