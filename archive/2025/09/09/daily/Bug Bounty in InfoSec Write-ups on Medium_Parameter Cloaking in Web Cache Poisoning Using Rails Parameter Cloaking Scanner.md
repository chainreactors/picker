---
title: Parameter Cloaking in Web Cache Poisoning Using Rails Parameter Cloaking Scanner
url: https://infosecwriteups.com/parameter-cloaking-in-web-cache-poisoning-using-rails-parameter-cloaking-scanner-489b571587c4?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-09
fetch_date: 2025-10-02T19:49:59.662602
---

# Parameter Cloaking in Web Cache Poisoning Using Rails Parameter Cloaking Scanner

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F489b571587c4&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fparameter-cloaking-in-web-cache-poisoning-using-rails-parameter-cloaking-scanner-489b571587c4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fparameter-cloaking-in-web-cache-poisoning-using-rails-parameter-cloaking-scanner-489b571587c4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-489b571587c4---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-489b571587c4---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Parameter Cloaking in Web Cache Poisoning Using Rails Parameter Cloaking Scanner

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:64:64/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---byline--489b571587c4---------------------------------------)

[Bash Overflow](https://bashoverflow.com/?source=post_page---byline--489b571587c4---------------------------------------)

4 min read

·

Sep 8, 2025

--

Share

**Learn how parameter cloaking enables attackers to bypass cache keys, poison responses, and deliver malicious content at scale**.

🔓 [**Free Link**](https://bashoverflow.com/489b571587c4?sk=a4e83c34dec69a52c00af34c2f271727)

Press enter or click to view image in full size

![Parameter Cloaking in Web Cache Poisoning Using Rails Parameter Cloaking Scanner — Bashoverflow Medium]()

Parameter Cloaking in Web Cache Poisoning Using Rails Parameter Cloaking Scanner

> **Disclaimer:**
> The techniques described in this document are intended solely for ethical use and educational purposes. Unauthorized use of these methods outside approved environments is strictly prohibited, as it is illegal, unethical, and may lead to severe consequences.
>
> It is crucial to act responsibly, comply with all applicable laws, and adhere to established ethical guidelines. Any activity that exploits security vulnerabilities or compromises the safety, privacy, or integrity of others is strictly forbidden.

## Table of Contents

1. [**Summary of the Vulnerability**](#bae8)
2. [**Steps to Reproduce & Proof of Concept (PoC)**](#d391)
3. [**Impact**](#851d)

## Summary of the Vulnerability

Parameter cloaking is a web cache poisoning technique that exploits discrepancies in how different components of a web application handle query parameters. In this lab scenario, the cache system ignores certain parameters (such as UTM tracking values) when generating cache keys, while the back-end application…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--489b571587c4---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--489b571587c4---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--489b571587c4---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--489b571587c4---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--489b571587c4---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:96:96/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---post_author_info--489b571587c4---------------------------------------)

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:128:128/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---post_author_info--489b571587c4---------------------------------------)

[## Written by Bash Overflow](https://bashoverflow.com/?source=post_page---post_author_info--489b571587c4---------------------------------------)

[150 followers](https://bashoverflow.com/followers?source=post_page---post_author_info--489b571587c4---------------------------------------)

·[11 following](https://medium.com/%40bashoverflow/following?source=post_page---post_author_info--489b571587c4---------------------------------------)

Cybersecurity Enthusiast | Sharing insights through some writeups | Passionate about advancing knowledge in the field of cybersecurity

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----489b571587c4---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----489b571587c4---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----489b571587c4---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----489b571587c4---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----489b571587c4---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----489b571587c4---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----489b571587c4---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----489b571587c4---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----489b571587c4---------------------------------------)