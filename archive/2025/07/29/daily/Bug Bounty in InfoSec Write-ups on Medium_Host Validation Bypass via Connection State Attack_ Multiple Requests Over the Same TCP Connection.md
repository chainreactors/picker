---
title: Host Validation Bypass via Connection State Attack: Multiple Requests Over the Same TCP Connection
url: https://infosecwriteups.com/host-validation-bypass-via-connection-state-attack-multiple-requests-over-the-same-tcp-connection-9fc2406d2fe1?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-29
fetch_date: 2025-10-06T23:51:28.193580
---

# Host Validation Bypass via Connection State Attack: Multiple Requests Over the Same TCP Connection

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F9fc2406d2fe1&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhost-validation-bypass-via-connection-state-attack-multiple-requests-over-the-same-tcp-connection-9fc2406d2fe1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhost-validation-bypass-via-connection-state-attack-multiple-requests-over-the-same-tcp-connection-9fc2406d2fe1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-9fc2406d2fe1---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-9fc2406d2fe1---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Host Validation Bypass via Connection State Attack: Multiple Requests Over the Same TCP Connection

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:64:64/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---byline--9fc2406d2fe1---------------------------------------)

[Bash Overflow](https://bashoverflow.com/?source=post_page---byline--9fc2406d2fe1---------------------------------------)

4 min read

·

Jul 27, 2025

--

Share

**Discover how persistent connections and weak Host validation open the doors to internal systems**.

🔓 [**Free Link**](https://bashoverflow.com/9fc2406d2fe1?sk=3ab7c44191a0c9002b71087b87af93f1)

Press enter or click to view image in full size

![Host Validation Bypass via Connection State Attack — Bashoverflow Medium]()

Host Validation Bypass via Connection State Attack

> **Disclaimer:**
> The techniques described in this document are intended solely for ethical use and educational purposes. Unauthorized use of these methods outside approved environments is strictly prohibited, as it is illegal, unethical, and may lead to severe consequences.
>
> It is crucial to act responsibly, comply with all applicable laws, and adhere to established ethical guidelines. Any activity that exploits security vulnerabilities or compromises the safety, privacy, or integrity of others is strictly forbidden.

## Table of Contents

1. [**Summary of the Vulnerability**](#dec8)
2. [**Steps to Reproduce & Proof of Concept (PoC)**](#40ee)
3. [**Impact**](#c0c6)

## Summary of the Vulnerability

In this specific scenario, the front-end server uses connection-based assumptions to validate the Host header. It analyzes only the first HTTP request in a persistent connection (usually with `Connection: keep-alive`) to determine if the Host header is valid.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--9fc2406d2fe1---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--9fc2406d2fe1---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--9fc2406d2fe1---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--9fc2406d2fe1---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--9fc2406d2fe1---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:96:96/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---post_author_info--9fc2406d2fe1---------------------------------------)

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:128:128/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---post_author_info--9fc2406d2fe1---------------------------------------)

[## Written by Bash Overflow](https://bashoverflow.com/?source=post_page---post_author_info--9fc2406d2fe1---------------------------------------)

[150 followers](https://bashoverflow.com/followers?source=post_page---post_author_info--9fc2406d2fe1---------------------------------------)

·[11 following](https://medium.com/%40bashoverflow/following?source=post_page---post_author_info--9fc2406d2fe1---------------------------------------)

Cybersecurity Enthusiast | Sharing insights through some writeups | Passionate about advancing knowledge in the field of cybersecurity

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----9fc2406d2fe1---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----9fc2406d2fe1---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----9fc2406d2fe1---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----9fc2406d2fe1---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----9fc2406d2fe1---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----9fc2406d2fe1---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----9fc2406d2fe1---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----9fc2406d2fe1---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----9fc2406d2fe1---------------------------------------)