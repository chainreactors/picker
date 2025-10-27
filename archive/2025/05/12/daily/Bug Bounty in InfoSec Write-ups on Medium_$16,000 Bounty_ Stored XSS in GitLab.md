---
title: $16,000 Bounty: Stored XSS in GitLab
url: https://infosecwriteups.com/16-000-bounty-stored-xss-in-gitlab-a0f57e5c4245?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-05-12
fetch_date: 2025-10-06T22:24:59.150479
---

# $16,000 Bounty: Stored XSS in GitLab

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fa0f57e5c4245&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F16-000-bounty-stored-xss-in-gitlab-a0f57e5c4245&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F16-000-bounty-stored-xss-in-gitlab-a0f57e5c4245&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-a0f57e5c4245---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-a0f57e5c4245---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# $16,000 Bounty: Stored XSS in GitLab

## From Regex to XSS: Inside a $16,000 Vulnerability in GitLab

[![Monika sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---byline--a0f57e5c4245---------------------------------------)

[Monika sharma](https://medium.com/%40commanak46?source=post_page---byline--a0f57e5c4245---------------------------------------)

3 min read

·

May 11, 2025

--

Share

Press enter or click to view image in full size

![]()

### Introduction

Security vulnerabilities often hide in the smallest implementation details. One such critical flaw was uncovered by security researcher vakzz who discovered a Stored Cross-Site Scripting (XSS) vulnerability in GitLab’s markdown rendering engine via the DesignReferenceFilter.

This vulnerability not only bypassed GitLab’s Content Security Policy (CSP) but also allowed attackers to inject arbitrary JavaScript anywhere markdown was processed such as issues comments and more.

For responsibly disclosing this high impact bug GitLab awarded a $16,000 bounty under report ID #1212067.

Let’s dive into how this vulnerability worked its potential impact and how other bug hunters can approach finding similar issues.

> **The Vulnerability: Breaking Out of Attributes via Filename Injection**

GitLab allows users to upload design files (like images) that can be referenced in issues via markdown links. When rendering markdown GitLab uses a filter called DesignReferenceFilter to parse these references.

Under the hood a regex pattern was used to match filenames:

```
valid_char = %r{[^/\s]} #…
```

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a0f57e5c4245---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a0f57e5c4245---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--a0f57e5c4245---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--a0f57e5c4245---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--a0f57e5c4245---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Monika sharma](https://miro.medium.com/v2/resize:fill:96:96/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--a0f57e5c4245---------------------------------------)

[![Monika sharma](https://miro.medium.com/v2/resize:fill:128:128/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--a0f57e5c4245---------------------------------------)

[## Written by Monika sharma](https://medium.com/%40commanak46?source=post_page---post_author_info--a0f57e5c4245---------------------------------------)

[2K followers](https://medium.com/%40commanak46/followers?source=post_page---post_author_info--a0f57e5c4245---------------------------------------)

·[7 following](https://medium.com/%40commanak46/following?source=post_page---post_author_info--a0f57e5c4245---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----a0f57e5c4245---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----a0f57e5c4245---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----a0f57e5c4245---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----a0f57e5c4245---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----a0f57e5c4245---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----a0f57e5c4245---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----a0f57e5c4245---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----a0f57e5c4245---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----a0f57e5c4245---------------------------------------)