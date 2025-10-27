---
title: SSRF — Server Side Request Forgery
url: https://infosecwriteups.com/ssrf-server-side-request-forgery-2865e87efc3?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-08
fetch_date: 2025-10-04T05:57:47.236536
---

# SSRF — Server Side Request Forgery

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2865e87efc3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fssrf-server-side-request-forgery-2865e87efc3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fssrf-server-side-request-forgery-2865e87efc3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40cyberw1ng)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2865e87efc3---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2865e87efc3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# SSRF — Server Side Request Forgery — Everything You need to Know |2023

## Simple Brief Explanation of SSRF | Karthikeyan Nagaraj

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---byline--2865e87efc3---------------------------------------)

[Karthikeyan Nagaraj](https://cyberw1ng.medium.com/?source=post_page---byline--2865e87efc3---------------------------------------)

3 min read

·

Jan 30, 2023

--

Listen

Share

Press enter or click to view image in full size

![]()

## What is SSRF?

* SSRF — Server-side request forgery (also known as SSRF) is a web security vulnerability that allows an attacker to induce the server-side application to make requests to an unintended location
* Server-Side Request Forgery (SSRF) is a vulnerability in web applications that allows attackers to send unauthorized requests from the vulnerable server to other internal systems.
* This can lead to sensitive information disclosure, as well as compromising the security of the affected systems.
* SSRF attacks can be launched through manipulated URLs or by exploiting weak input validation in the application code.
* To prevent SSRF, it’s essential to properly validate all user inputs and restrict the origin of the requests to trusted sources.
* Additionally, implementing network segmentation, firewalls, and access controls can limit the reach of SSRF attacks within an organization’s infrastructure.

## How to Find SSRF Vulnerability?

Finding Server-Side Request Forgery (SSRF) vulnerabilities in web applications can be a challenging task, but it is essential to ensure the security of your systems. Here are a few methods to detect SSRF vulnerabilities:

1. Scanning: Use web application security scanners to search for SSRF vulnerabilities in your applications. These tools automate the process of searching for SSRF vulnerabilities.
2. Manual testing: Conduct manual testing to verify the security of the application’s input handling and request generation. This involves sending carefully crafted requests to the application and analyzing its behavior.
3. Monitoring: Monitor the application’s log files to detect any suspicious or unauthorized requests.
4. Code review: Conduct code reviews to identify any weak input validation or lack of security controls in the application’s code.

## Impact of SSRF

Server-Side Request Forgery (SSRF) is a critical vulnerability that can have severe impacts on an organization’s security.

* The main impact of SSRF is the ability of attackers to access sensitive information and execute unauthorized actions on behalf of the vulnerable server.
* It can lead to data leakages, such as the disclosure of internal network addresses, credentials, and other confidential information.
* It can also allow attackers to perform actions like port scanning, firewall bypass, and even compromise other systems on the network.
* The consequences of SSRF can be severe, such as loss of sensitive information, disruption of business operations, and reputational damage.
* In some cases, SSRF attacks can result in the complete compromise of an organization’s network, allowing attackers to gain access to critical systems and sensitive data.

Therefore, it is crucial to be proactive in detecting and mitigating SSRF vulnerabilities. Implementing secure coding practices, validating user inputs, and restricting the origin of requests to trusted sources can effectively reduce the risks posed by SSRF attacks.

By being aware of the potential impacts of SSRF, organizations can take necessary measures to protect themselves from these critical vulnerabilities

## Prevention

Preventing Server-Side Request Forgery (SSRF) vulnerabilities requires a multi-layered approach that includes both secure coding practices and effective security measures. Here are a few ways to prevent SSRF:

1. Input validation: Validate all user inputs and ensure that requests are made to trusted sources.
2. Network segmentation: Implement network segmentation and access controls to limit the reach of SSRF attacks.
3. Firewalls: Use firewalls to prevent unauthorized access to internal systems.
4. Code review: Conduct regular code reviews to identify any weak input validation or security gaps in the application’s code.
5. Monitoring: Monitor the application’s log files to detect any suspicious or unauthorized requests.

## Conclusion:

Server-Side Request Forgery (SSRF) is a critical vulnerability that can have severe impacts on an organization’s security. SSRF attacks can result in the compromise of sensitive information, disruption of business operations, and reputational damage.

To prevent SSRF, organizations must adopt secure coding practices, validate user inputs, implement network security measures, and conduct continuous monitoring.

By being proactive and taking the necessary steps to protect their systems, organizations can effectively mitigate the risks posed by SSRF attacks and maintain the security of their information and systems.

Feel Free to Ask Queries via [LinkedIn](https://www.linkedin.com/in/karthikeyan-nagaraj) and to Buy me a Cofee : )

[![]()](http://buymeacoffee.com/cyberw1ng)

Thank you for Reading!!

Happy Hunting ~

```
Author : karthikeyan Nagaraj
```

[Ssrf](https://medium.com/tag/ssrf?source=post_page-----2865e87efc3---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----2865e87efc3---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----2865e87efc3---------------------------------------)

[Web Development](https://medium.com/tag/web-development?source=post_page-----2865e87efc3---------------------------------------)

[Articles](https://medium.com/tag/articles?source=post_page-----2865e87efc3---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro....