---
title: Recon to Master: The Complete Bug Bounty Checklist
url: https://infosecwriteups.com/recon-to-master-the-complete-bug-bounty-checklist-95b80ea55ff0?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-17
fetch_date: 2025-10-06T23:28:34.675881
---

# Recon to Master: The Complete Bug Bounty Checklist

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F95b80ea55ff0&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frecon-to-master-the-complete-bug-bounty-checklist-95b80ea55ff0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frecon-to-master-the-complete-bug-bounty-checklist-95b80ea55ff0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-95b80ea55ff0---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-95b80ea55ff0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

Featured

## RECON

# Recon to Master: The Complete Bug Bounty Checklist

## Proven Step-by-Step Recon Techniques to Uncover Your First Vulnerabilities in Bug Bounty Programs

[![coffinxp](https://miro.medium.com/v2/resize:fill:64:64/1*PjsjomDRyS2MomLQcc4nOw.png)](https://coffinxp.medium.com/?source=post_page---byline--95b80ea55ff0---------------------------------------)

[coffinxp](https://coffinxp.medium.com/?source=post_page---byline--95b80ea55ff0---------------------------------------)

16 min read

·

Jul 16, 2025

--

31

Share

Press enter or click to view image in full size

![]()

## Introduction

**Reconnaissance (recon)** is the foundation of any successful bug bounty hunt. Mastering recon means you can uncover hidden assets, vulnerable endpoints and sensitive data that others miss. This guide walks you through the best recon methodologies to elevate your bug bounty skills.

## Table of Contents

```
1. Finding Subdomains with Tools
2. Manual Subdomain Discovery via Public Sources
3. Shodan-Powered Subdomain Finder
4. GitHub Subdomain Enumeration
5. Merging & Sorting Subdomains with DNS Resolution
6. Brute-Forcing Subdomains using FFUF
7. IP Discovery using ASN Mapping & APIs
8. Asset Discovery with Amass Intel
9. Finding Live Hosts using HTTPX
10. Visual Reconnaissance with Aquatone
11. Crawling URLs using Katana and Hakrawler
12. Collecting Historical URLs with GAU & Wayback
13. Extracting Parameters from URLs with Regex & GF
14. Automated Vulnerability Scanning with Nuclei
15. Customizing & Using Nuclei Templates
16. Finding Sensitive Files via Regex & Wordlists
17. Discovering Hidden Parameters with Arjun
18. Directory &…
```

--

--

31

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--95b80ea55ff0---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--95b80ea55ff0---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--95b80ea55ff0---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--95b80ea55ff0---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--95b80ea55ff0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![coffinxp](https://miro.medium.com/v2/resize:fill:96:96/1*PjsjomDRyS2MomLQcc4nOw.png)](https://coffinxp.medium.com/?source=post_page---post_author_info--95b80ea55ff0---------------------------------------)

[![coffinxp](https://miro.medium.com/v2/resize:fill:128:128/1*PjsjomDRyS2MomLQcc4nOw.png)](https://coffinxp.medium.com/?source=post_page---post_author_info--95b80ea55ff0---------------------------------------)

[## Written by coffinxp](https://coffinxp.medium.com/?source=post_page---post_author_info--95b80ea55ff0---------------------------------------)

[6.3K followers](https://coffinxp.medium.com/followers?source=post_page---post_author_info--95b80ea55ff0---------------------------------------)

·[0 following](https://medium.com/%40coffinxp/following?source=post_page---post_author_info--95b80ea55ff0---------------------------------------)

Helping organizations stay secure through Bug Hunting, OSINT and Security Research | Sharing knowledge as a Content Creator

## Responses (31)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----95b80ea55ff0---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----95b80ea55ff0---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----95b80ea55ff0---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----95b80ea55ff0---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----95b80ea55ff0---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----95b80ea55ff0---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----95b80ea55ff0---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----95b80ea55ff0---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----95b80ea55ff0---------------------------------------)