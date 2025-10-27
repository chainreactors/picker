---
title: SSRF via Flawed Request Parsing Leads to Internal Admin Access
url: https://infosecwriteups.com/ssrf-via-flawed-request-parsing-leads-to-ssrf-and-internal-admin-access-ffac4b3103db?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-27
fetch_date: 2025-10-06T23:17:17.746479
---

# SSRF via Flawed Request Parsing Leads to Internal Admin Access

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fffac4b3103db&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fssrf-via-flawed-request-parsing-leads-to-ssrf-and-internal-admin-access-ffac4b3103db&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fssrf-via-flawed-request-parsing-leads-to-ssrf-and-internal-admin-access-ffac4b3103db&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ffac4b3103db---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ffac4b3103db---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# SSRF via Flawed Request Parsing Leads to Internal Admin Access

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:64:64/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---byline--ffac4b3103db---------------------------------------)

[Bash Overflow](https://bashoverflow.com/?source=post_page---byline--ffac4b3103db---------------------------------------)

4 min read

·

Jul 26, 2025

--

1

Share

**Exploiting Misconfigured Routing to Breach Internal Networks through SSRF**.

🔓 [**Free Link**](https://bashoverflow.com/ffac4b3103db?sk=89fe34340f4325ccbd31d0e174ad4d67)

Press enter or click to view image in full size

![SSRF via Flawed Request Parsing Leads to SSRF and Internal Admin Access — Bashoverflow Medium]()

SSRF via Flawed Request Parsing Leads to SSRF and Internal Admin Access

> **Disclaimer:**
> The techniques described in this document are intended solely for ethical use and educational purposes. Unauthorized use of these methods outside approved environments is strictly prohibited, as it is illegal, unethical, and may lead to severe consequences.
>
> It is crucial to act responsibly, comply with all applicable laws, and adhere to established ethical guidelines. Any activity that exploits security vulnerabilities or compromises the safety, privacy, or integrity of others is strictly forbidden.

## Table of Contents

1. [**Summary of the Vulnerability**](#be46)
2. [**Steps to Reproduce & Proof of Concept (PoC)**](#7701)
3. [**Impact**](#83d3)

## Summary of the Vulnerability

The vulnerability arises from **inconsistent parsing of the request host**, particularly in how different components of a web application (like front-end reverse proxies, load balancers, or the backend logic) interpret the Host header and other URL parts.

In this specific lab environment from [PortSwigger’s Web Security Academy](https://portswigger.net/web-security/host-header/exploiting/lab-host-header-ssrf-via-flawed-request-parsing), the application suffers from…

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ffac4b3103db---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ffac4b3103db---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--ffac4b3103db---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--ffac4b3103db---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--ffac4b3103db---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:96:96/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---post_author_info--ffac4b3103db---------------------------------------)

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:128:128/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---post_author_info--ffac4b3103db---------------------------------------)

[## Written by Bash Overflow](https://bashoverflow.com/?source=post_page---post_author_info--ffac4b3103db---------------------------------------)

[150 followers](https://bashoverflow.com/followers?source=post_page---post_author_info--ffac4b3103db---------------------------------------)

·[11 following](https://medium.com/%40bashoverflow/following?source=post_page---post_author_info--ffac4b3103db---------------------------------------)

Cybersecurity Enthusiast | Sharing insights through some writeups | Passionate about advancing knowledge in the field of cybersecurity

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----ffac4b3103db---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----ffac4b3103db---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----ffac4b3103db---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----ffac4b3103db---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----ffac4b3103db---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----ffac4b3103db---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----ffac4b3103db---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----ffac4b3103db---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----ffac4b3103db---------------------------------------)