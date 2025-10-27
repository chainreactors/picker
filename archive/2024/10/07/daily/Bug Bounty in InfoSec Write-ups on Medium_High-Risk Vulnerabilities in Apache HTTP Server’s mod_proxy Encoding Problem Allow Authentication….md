---
title: High-Risk Vulnerabilities in Apache HTTP Server’s mod_proxy Encoding Problem Allow Authentication…
url: https://infosecwriteups.com/high-risk-vulnerabilities-in-apache-http-servers-mod-proxy-encoding-problem-allow-authentication-cbe8d422738d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-10-07
fetch_date: 2025-10-06T18:49:40.448126
---

# High-Risk Vulnerabilities in Apache HTTP Server’s mod_proxy Encoding Problem Allow Authentication…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fcbe8d422738d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhigh-risk-vulnerabilities-in-apache-http-servers-mod-proxy-encoding-problem-allow-authentication-cbe8d422738d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhigh-risk-vulnerabilities-in-apache-http-servers-mod-proxy-encoding-problem-allow-authentication-cbe8d422738d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-cbe8d422738d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-cbe8d422738d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **High-Risk Vulnerabilities in Apache HTTP Server’s mod\_proxy Encoding Problem Allow Authentication Bypass — $$$ Bounty**

[![Ajay Naik](https://miro.medium.com/v2/resize:fill:64:64/1*_IX9-hF0QxJXhyR65v8Fww.jpeg)](https://medium.com/%40ajaynaikhack?source=post_page---byline--cbe8d422738d---------------------------------------)

[Ajay Naik](https://medium.com/%40ajaynaikhack?source=post_page---byline--cbe8d422738d---------------------------------------)

4 min read

·

Oct 6, 2024

--

Share

**Apache HTTP Server — ACL Bypass**

## **CVE-2024–38473 Overview:**

Press enter or click to view image in full size

![]()

## **Description:**

**The vulnerability is due to an encoding problem in mod\_proxy, which allows request URLs with incorrect encoding to be sent to backend services. This can potentially bypass authentication via crafted requests.** **The vulnerability could allow attackers to bypass authentication mechanisms, leading to unauthorized access**

* **Severity: High**
* **CVSS Score: 8.1 (Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:H)**
* **Weakness: CWE-116: Improper Encoding or Escaping of Output**

## **Impact:**

· **Compromised Authentication**: Attackers may be able to bypass security barriers intended to protect sensitive areas, thereby gaining unauthorized access to restricted resources or services.

· **Sensitive Data Exposure**: Once inside, unauthorized users could access confidential information that should otherwise be secured behind authentication measures.

· **Elevation of Privileges**: Upon breaching authenticated zones, attackers might escalate their privileges or find new…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--cbe8d422738d---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--cbe8d422738d---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--cbe8d422738d---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--cbe8d422738d---------------------------------------)

·[Last published 3 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--cbe8d422738d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ajay Naik](https://miro.medium.com/v2/resize:fill:96:96/1*_IX9-hF0QxJXhyR65v8Fww.jpeg)](https://medium.com/%40ajaynaikhack?source=post_page---post_author_info--cbe8d422738d---------------------------------------)

[![Ajay Naik](https://miro.medium.com/v2/resize:fill:128:128/1*_IX9-hF0QxJXhyR65v8Fww.jpeg)](https://medium.com/%40ajaynaikhack?source=post_page---post_author_info--cbe8d422738d---------------------------------------)

[## Written by Ajay Naik](https://medium.com/%40ajaynaikhack?source=post_page---post_author_info--cbe8d422738d---------------------------------------)

[313 followers](https://medium.com/%40ajaynaikhack/followers?source=post_page---post_author_info--cbe8d422738d---------------------------------------)

·[276 following](https://medium.com/%40ajaynaikhack/following?source=post_page---post_author_info--cbe8d422738d---------------------------------------)

Cyber security Expert with a Strong Focus on Penetration Testing, Threat Intelligence, and Bug Bounty Hunting.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----cbe8d422738d---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----cbe8d422738d---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----cbe8d422738d---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----cbe8d422738d---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----cbe8d422738d---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----cbe8d422738d---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----cbe8d422738d---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----cbe8d422738d---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----cbe8d422738d---------------------------------------)