---
title: The Ultimate XSS PoC with ChatGPT-4
url: https://infosecwriteups.com/the-ultimate-xss-poc-with-chatgpt-4-2be606a13a2e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-27
fetch_date: 2025-10-04T10:46:20.457990
---

# The Ultimate XSS PoC with ChatGPT-4

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2be606a13a2e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-ultimate-xss-poc-with-chatgpt-4-2be606a13a2e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-ultimate-xss-poc-with-chatgpt-4-2be606a13a2e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2be606a13a2e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2be606a13a2e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# The Ultimate XSS PoC with ChatGPT-4 🎯

## XSS to Demonstrate Stealing Cookies, Local Storage, and Page Content Generated with ChatGPT-4 🤖

[![Mike Takahashi (TakSec)](https://miro.medium.com/v2/resize:fill:64:64/1*oeaksoi-GPEkdXjmR0uMFA.jpeg)](https://taksec.medium.com/?source=post_page---byline--2be606a13a2e---------------------------------------)

[Mike Takahashi (TakSec)](https://taksec.medium.com/?source=post_page---byline--2be606a13a2e---------------------------------------)

4 min read

·

Mar 26, 2023

--

Share

![]()

Welcome, fellow vulnerability hunters! Today, we’re going to explore a simple yet powerful way to demonstrate Cross-Site Scripting (XSS) vulnerabilities using a Proof of Concept (PoC) generated with ChatGPT model GPT-4. Get ready to level up your ethical hacking skills!

## Step 1: The Prompt 📝

Let’s start with a killer prompt that’ll set the foundation for our PoC:

> Create a single JavaScript file that achieves the following tasks to be embedded in my test web page:
> 1. Display all cookies, local storage, and DOM contents in the console.
> 2. Create a login page that replaces the entire content of the current webpage, and log any submitted form data to the console.
> 3. Apply styling to the login page to give it a professional appearance.
> 4. For every item logged to the console, prepend the label “hacked cookie:” or an equivalent description specific to the type of information displayed.
> 5. Enhance the console output with formatting and colors to make it visually appealing and easy to read.

Got it? Sweet! Now, let’s break it down into smaller tasks and tackle each one.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2be606a13a2e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2be606a13a2e---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--2be606a13a2e---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--2be606a13a2e---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--2be606a13a2e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Mike Takahashi (TakSec)](https://miro.medium.com/v2/resize:fill:96:96/1*oeaksoi-GPEkdXjmR0uMFA.jpeg)](https://taksec.medium.com/?source=post_page---post_author_info--2be606a13a2e---------------------------------------)

[![Mike Takahashi (TakSec)](https://miro.medium.com/v2/resize:fill:128:128/1*oeaksoi-GPEkdXjmR0uMFA.jpeg)](https://taksec.medium.com/?source=post_page---post_author_info--2be606a13a2e---------------------------------------)

[## Written by Mike Takahashi (TakSec)](https://taksec.medium.com/?source=post_page---post_author_info--2be606a13a2e---------------------------------------)

[2.3K followers](https://taksec.medium.com/followers?source=post_page---post_author_info--2be606a13a2e---------------------------------------)

·[768 following](https://medium.com/%40taksec/following?source=post_page---post_author_info--2be606a13a2e---------------------------------------)

Pentester | Bug Bounty Hunter | AI Red Team <https://twitter.com/TakSec>

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----2be606a13a2e---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----2be606a13a2e---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----2be606a13a2e---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----2be606a13a2e---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----2be606a13a2e---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----2be606a13a2e---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----2be606a13a2e---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----2be606a13a2e---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----2be606a13a2e---------------------------------------)