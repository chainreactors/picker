---
title: How I Hack Websites With Just HTML Injection
url: https://infosecwriteups.com/how-i-hack-websites-with-just-html-injection-9ccbc87faf47?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-09
fetch_date: 2025-10-02T19:50:30.896940
---

# How I Hack Websites With Just HTML Injection

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F9ccbc87faf47&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-hack-websites-with-just-html-injection-9ccbc87faf47&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-hack-websites-with-just-html-injection-9ccbc87faf47&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-9ccbc87faf47---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-9ccbc87faf47---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **How I Hack Websites With Just HTML Injection**

## Step-by-Step Guide

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:64:64/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---byline--9ccbc87faf47---------------------------------------)

[Ibtissam hammadi](https://medium.com/%40ibtissamhammadi1?source=post_page---byline--9ccbc87faf47---------------------------------------)

4 min read

·

Sep 8, 2025

--

1

Share

Ever been told that HTML Injection is a “low-risk” and mostly useless vulnerability? Well, it’s time for that myth to be busted.

What if you were told that a simple HTML injection could be used to uncover API keys, internal subdomains, and secret endpoints? This isn’t just theory; it’s a powerful method for **JavaScript Reconnaissance (JS Recon)**.

Press enter or click to view image in full size

![Hacking Websites With Just HTML Injection]()

Photo by [Pankaj Patel](https://unsplash.com/%40pankajpatel?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Modern websites are built on a complex web of JavaScript files. These files often contain hidden secrets. A simple HTML injection flaw can be used as a lens to focus on and extract those secrets, turning a minor bug into a major discovery.

This guide is designed to be **beginner-friendly**, based on real-world experience. Let’s walk through the process, step by step.

### Step 1: Finding the Perfect Injection Point

Not all injection points are created equal. The goal is to find a place where your input is reflected on the page and, crucially, where it will persist so that your **JavaScript reconnaissance** can work.

**Ideal places to test are:**

* **Profile pages** (name, biography, website URL)
* **Comment sections**
* **Support tickets or contact forms**

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--9ccbc87faf47---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--9ccbc87faf47---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--9ccbc87faf47---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--9ccbc87faf47---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--9ccbc87faf47---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:96:96/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--9ccbc87faf47---------------------------------------)

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:128:128/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--9ccbc87faf47---------------------------------------)

[## Written by Ibtissam hammadi](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--9ccbc87faf47---------------------------------------)

[4.2K followers](https://medium.com/%40ibtissamhammadi1/followers?source=post_page---post_author_info--9ccbc87faf47---------------------------------------)

·[98 following](https://medium.com/%40ibtissamhammadi1/following?source=post_page---post_author_info--9ccbc87faf47---------------------------------------)

I am a Senior Data Scientist exploring Cybersecurity, Infosec, Programming, and AI technologies.

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----9ccbc87faf47---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----9ccbc87faf47---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----9ccbc87faf47---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----9ccbc87faf47---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----9ccbc87faf47---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----9ccbc87faf47---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----9ccbc87faf47---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----9ccbc87faf47---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----9ccbc87faf47---------------------------------------)