---
title: Security Engineer Interview Questions Part-1
url: https://infosecwriteups.com/security-engineer-interview-questions-part-1-c5c9a5267468?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-02
fetch_date: 2025-10-02T19:30:53.896143
---

# Security Engineer Interview Questions Part-1

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc5c9a5267468&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsecurity-engineer-interview-questions-part-1-c5c9a5267468&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsecurity-engineer-interview-questions-part-1-c5c9a5267468&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c5c9a5267468---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c5c9a5267468---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Security Engineer Interview Questions Part-1

[![Saurabh Jain](https://miro.medium.com/v2/resize:fill:64:64/1*gXBGFSeHBrBmuEzFs-eAkQ.png)](https://saurabh-jain.medium.com/?source=post_page---byline--c5c9a5267468---------------------------------------)

[Saurabh Jain](https://saurabh-jain.medium.com/?source=post_page---byline--c5c9a5267468---------------------------------------)

6 min read

·

Sep 17, 2024

--

Share

Press enter or click to view image in full size

![]()

With 6+ years of experience in the field of security, I’ve had the opportunity to participate in numerous interviews for Security Engineering roles. Throughout these experiences, I have collected some unique and amazing questions which were asked in the interview which tests both technical knowledge and practical application.

I’m sharing a curated series of questions with answers asked in good companies such as Big 4s, Amazon, Google, Cisco, Grab etc.

1. **With IDS (*Intrusion Detection System*), IPS (*Intrusion Prevention System*), and WAF (*Web Application Firewall*) in your architecture, how should these components be positioned in sequence?**

The ideal placement should look like this :

Press enter or click to view image in full size

![]()

### Reason Behind :

1. The **WAF** is placed at the front, directly facing web traffic coming from the internet acting as first line of defense, protecting against application-layer attacks like SQLi, (XSS), and other threats.
2. Behind **WAF**, the **IPS** should be deployed as it actively monitors incoming traffic and blocks known attack patterns, protecting the system from threats like malware, DoS attacks…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c5c9a5267468---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c5c9a5267468---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--c5c9a5267468---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--c5c9a5267468---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--c5c9a5267468---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Saurabh Jain](https://miro.medium.com/v2/resize:fill:96:96/1*gXBGFSeHBrBmuEzFs-eAkQ.png)](https://saurabh-jain.medium.com/?source=post_page---post_author_info--c5c9a5267468---------------------------------------)

[![Saurabh Jain](https://miro.medium.com/v2/resize:fill:128:128/1*gXBGFSeHBrBmuEzFs-eAkQ.png)](https://saurabh-jain.medium.com/?source=post_page---post_author_info--c5c9a5267468---------------------------------------)

[## Written by Saurabh Jain](https://saurabh-jain.medium.com/?source=post_page---post_author_info--c5c9a5267468---------------------------------------)

[103 followers](https://saurabh-jain.medium.com/followers?source=post_page---post_author_info--c5c9a5267468---------------------------------------)

·[105 following](https://medium.com/%40saurabh-jain/following?source=post_page---post_author_info--c5c9a5267468---------------------------------------)

Security Enthusiast Linkedin : <https://www.linkedin.com/in/saurabh-jain-503991165/>

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----c5c9a5267468---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----c5c9a5267468---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----c5c9a5267468---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----c5c9a5267468---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----c5c9a5267468---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----c5c9a5267468---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----c5c9a5267468---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----c5c9a5267468---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----c5c9a5267468---------------------------------------)