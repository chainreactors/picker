---
title: SSRF: Blacklist and Whitelist-Based Input Filters
url: https://infosecwriteups.com/ssrf-blacklist-and-whitelist-based-input-filters-1c602b872731?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-08-11
fetch_date: 2025-10-06T18:02:24.291508
---

# SSRF: Blacklist and Whitelist-Based Input Filters

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F1c602b872731&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fssrf-blacklist-and-whitelist-based-input-filters-1c602b872731&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fssrf-blacklist-and-whitelist-based-input-filters-1c602b872731&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-1c602b872731---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-1c602b872731---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# SSRF: Blacklist and Whitelist-Based Input Filters

## Explain and Try To Bypass Blacklist and Whitelist Input Filters

[![Neetrox](https://miro.medium.com/v2/resize:fill:64:64/1*MQkphkThmCsQrJCIK97LFA.png)](https://aloulouomarr.medium.com/?source=post_page---byline--1c602b872731---------------------------------------)

[Neetrox](https://aloulouomarr.medium.com/?source=post_page---byline--1c602b872731---------------------------------------)

6 min read

·

Aug 7, 2024

--

1

Share

Press enter or click to view image in full size

![]()

**Server-Side Request Forgery (SSRF)** is a web security vulnerability that enables an attacker to manipulate a server-side application into making HTTP requests to arbitrary destinations. This can lead to unauthorized interactions with internal systems, potentially exposing sensitive information or allowing further exploitation.

### **Types of SSRF:**

***SSRF Targeting the Server:*** Attackers manipulate the application to send HTTP requests to the server’s loopback adapter. For instance, by modifying a request in an eCommerce app, they can access admin pages and bypass access controls.

***SSRF Targeting the Back End:*** Attackers interact with backend systems, typically with private IP addresses and weaker security, to access protected functionalities like administrative interfaces.

***Blind SSRF:*** These attacks focus on performing malicious actions without visible data return. For example, repeatedly requesting a large file can crash the server, causing a denial of service (DoS).

### **Risks of SSRF:**

A successful Server-Side Request Forgery (SSRF) attack can manipulate a web server to perform malicious actions or…

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1c602b872731---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1c602b872731---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--1c602b872731---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--1c602b872731---------------------------------------)

·[Last published 2 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--1c602b872731---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Neetrox](https://miro.medium.com/v2/resize:fill:96:96/1*MQkphkThmCsQrJCIK97LFA.png)](https://aloulouomarr.medium.com/?source=post_page---post_author_info--1c602b872731---------------------------------------)

[![Neetrox](https://miro.medium.com/v2/resize:fill:128:128/1*MQkphkThmCsQrJCIK97LFA.png)](https://aloulouomarr.medium.com/?source=post_page---post_author_info--1c602b872731---------------------------------------)

[## Written by Neetrox](https://aloulouomarr.medium.com/?source=post_page---post_author_info--1c602b872731---------------------------------------)

[206 followers](https://aloulouomarr.medium.com/followers?source=post_page---post_author_info--1c602b872731---------------------------------------)

·[45 following](https://medium.com/%40aloulouomarr/following?source=post_page---post_author_info--1c602b872731---------------------------------------)

Cybersecurity Enthusiast | Security+ | CySA+ | THM SAL1

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----1c602b872731---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----1c602b872731---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----1c602b872731---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----1c602b872731---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----1c602b872731---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----1c602b872731---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----1c602b872731---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----1c602b872731---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----1c602b872731---------------------------------------)