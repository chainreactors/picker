---
title: What is WAF? & Secret Techniques to Bypass It
url: https://infosecwriteups.com/what-is-waf-secret-techniques-to-bypass-it-2a4de4768131?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-09-11
fetch_date: 2025-10-06T18:26:52.801506
---

# What is WAF? & Secret Techniques to Bypass It

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2a4de4768131&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhat-is-waf-secret-techniques-to-bypass-it-2a4de4768131&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhat-is-waf-secret-techniques-to-bypass-it-2a4de4768131&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2a4de4768131---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2a4de4768131---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **What is WAF? & Secret Techniques to Bypass It**

[![Ajay Naik](https://miro.medium.com/v2/resize:fill:64:64/1*_IX9-hF0QxJXhyR65v8Fww.jpeg)](https://medium.com/%40ajaynaikhack?source=post_page---byline--2a4de4768131---------------------------------------)

[Ajay Naik](https://medium.com/%40ajaynaikhack?source=post_page---byline--2a4de4768131---------------------------------------)

7 min read

·

Sep 5, 2024

--

Share

Press enter or click to view image in full size

![]()

* **WAF (Web Application Firewall)**: A tool designed to filter and monitor HTTP/HTTPS traffic, preventing attacks on web applications at the application layer.
* **WAF Limitations**: While effective, WAFs are part of a broader security framework and should be used in conjunction with other security tools.

**Key Functions of a WAF:**

1. **Application Layer Protection: Operates at the application layer (Layer 7) of the OSI model to protect web applications.**
2. **Traffic Filtering: Inspects incoming and outgoing HTTP/HTTPS requests, blocking harmful requests while allowing legitimate traffic.**
3. **Rule-based Detection: Uses predefined rules or patterns (like regular expressions) to detect malicious payloads, signatures, or abnormal behaviors.**
4. **Real-time Decision Making: Determines whether to allow, block, or log the traffic based on predefined security policies.**
5. **Defense Against Web Exploits: Mitigates common web vulnerabilities such as SQL injection, cross-site scripting, file inclusion, and other OWASP Top 10 threats.**

**Types of WAF:**

* **Network-based WAF: Deployed at the edge of the network for high-speed, low-latency protection.**
* **Host-based WAF: Integrated into the web server**…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2a4de4768131---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2a4de4768131---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--2a4de4768131---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--2a4de4768131---------------------------------------)

·[Last published 3 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--2a4de4768131---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ajay Naik](https://miro.medium.com/v2/resize:fill:96:96/1*_IX9-hF0QxJXhyR65v8Fww.jpeg)](https://medium.com/%40ajaynaikhack?source=post_page---post_author_info--2a4de4768131---------------------------------------)

[![Ajay Naik](https://miro.medium.com/v2/resize:fill:128:128/1*_IX9-hF0QxJXhyR65v8Fww.jpeg)](https://medium.com/%40ajaynaikhack?source=post_page---post_author_info--2a4de4768131---------------------------------------)

[## Written by Ajay Naik](https://medium.com/%40ajaynaikhack?source=post_page---post_author_info--2a4de4768131---------------------------------------)

[313 followers](https://medium.com/%40ajaynaikhack/followers?source=post_page---post_author_info--2a4de4768131---------------------------------------)

·[276 following](https://medium.com/%40ajaynaikhack/following?source=post_page---post_author_info--2a4de4768131---------------------------------------)

Cyber security Expert with a Strong Focus on Penetration Testing, Threat Intelligence, and Bug Bounty Hunting.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----2a4de4768131---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----2a4de4768131---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----2a4de4768131---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----2a4de4768131---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----2a4de4768131---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----2a4de4768131---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----2a4de4768131---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----2a4de4768131---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----2a4de4768131---------------------------------------)