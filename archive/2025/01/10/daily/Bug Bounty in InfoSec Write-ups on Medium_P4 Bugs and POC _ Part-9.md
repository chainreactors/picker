---
title: P4 Bugs and POC | Part-9
url: https://infosecwriteups.com/p4-bugs-and-poc-part-9-16b5a8ffb52d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-10
fetch_date: 2025-10-06T20:07:30.319320
---

# P4 Bugs and POC | Part-9

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F16b5a8ffb52d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fp4-bugs-and-poc-part-9-16b5a8ffb52d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fp4-bugs-and-poc-part-9-16b5a8ffb52d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-16b5a8ffb52d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-16b5a8ffb52d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# P4 Bugs and POC | Part-9

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:64:64/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--16b5a8ffb52d---------------------------------------)

[Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--16b5a8ffb52d---------------------------------------)

4 min read

·

Jan 7, 2025

--

Share

Hi everyone! 👋

I’m **Abhijeet Kumawat** — a passionate **bug bounty hunter** and **security researcher**. I thrive on uncovering vulnerabilities and sharing my knowledge to help others sharpen their skills in **bug bounty hunting** and **penetration testing**.

Today, I’m thrilled to launch a new blog series focusing on **P4 bugs** — those seemingly low-severity vulnerabilities that are often underestimated. Don’t be fooled, though! With the right approach, these bugs can have a tangible impact and even pave the way for higher-severity exploits.

In this series, I’ll explain each vulnerability type in detail and provide step-by-step **proof-of-concept (PoC)** demonstrations. Follow along, and I guarantee you’ll gain the confidence to hunt down valid P4 bugs on real-world targets. 💡

Press enter or click to view image in full size

![]()

## 🐛 Vulnerability #1: No Rate Limit on Reporting Comments

### 📝 Description

The “Report Comment” functionality on many platforms allows users to flag inappropriate or offensive content. However, when this feature lacks **rate limiting**, attackers can exploit it to automate the reporting process. If a certain number of reports triggers comment removal, attackers can abuse this to delete legitimate comments by flooding the system with automated requests.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--16b5a8ffb52d---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--16b5a8ffb52d---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--16b5a8ffb52d---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--16b5a8ffb52d---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--16b5a8ffb52d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:96:96/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--16b5a8ffb52d---------------------------------------)

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:128:128/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--16b5a8ffb52d---------------------------------------)

[## Written by Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--16b5a8ffb52d---------------------------------------)

[2.4K followers](https://medium.com/%40kumawatabhijeet2002/followers?source=post_page---post_author_info--16b5a8ffb52d---------------------------------------)

·[33 following](https://medium.com/%40kumawatabhijeet2002/following?source=post_page---post_author_info--16b5a8ffb52d---------------------------------------)

Radhe Radhe ✨ || Security Researcher || Bug Hunter || Web Application Penetration Tester || Ethical Hacker ||

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----16b5a8ffb52d---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----16b5a8ffb52d---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----16b5a8ffb52d---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----16b5a8ffb52d---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----16b5a8ffb52d---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----16b5a8ffb52d---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----16b5a8ffb52d---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----16b5a8ffb52d---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----16b5a8ffb52d---------------------------------------)