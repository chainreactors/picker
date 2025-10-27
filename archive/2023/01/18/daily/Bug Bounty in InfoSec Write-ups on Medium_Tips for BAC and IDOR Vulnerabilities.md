---
title: Tips for BAC and IDOR Vulnerabilities
url: https://infosecwriteups.com/tips-for-bac-and-idor-vulnerabilities-8a3e58f79d95?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-18
fetch_date: 2025-10-04T04:08:22.366238
---

# Tips for BAC and IDOR Vulnerabilities

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8a3e58f79d95&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ftips-for-bac-and-idor-vulnerabilities-8a3e58f79d95&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ftips-for-bac-and-idor-vulnerabilities-8a3e58f79d95&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8a3e58f79d95---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8a3e58f79d95---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Tips for BAC and IDOR Vulnerabilities

## Step-by-step guide for uncovering Broken Access Control and Indirect Object Reference vulnerabilities for bug bounty hunters and pentesters.

[![Mike Takahashi (TakSec)](https://miro.medium.com/v2/resize:fill:64:64/1*oeaksoi-GPEkdXjmR0uMFA.jpeg)](https://taksec.medium.com/?source=post_page---byline--8a3e58f79d95---------------------------------------)

[Mike Takahashi (TakSec)](https://taksec.medium.com/?source=post_page---byline--8a3e58f79d95---------------------------------------)

5 min read

·

Jan 16, 2023

--

Share

![]()

### Introduction

As bug bounty hunters and pentesters, one of the most rewarding vulnerabilities to uncover are **Broken Access Control (BAC)** and **Insecure Direct Object Reference (IDOR)**. In this article, we’ll discuss what BAC and IDOR vulnerabilities are, basic testing methodology, IDOR with UUID, Blind IDOR, and automating with the Auth Analyzer Burp Extension.

### What is a BAC Vulnerability?

Broken access control (BAC) is a type of vulnerability where users can access or perform actions they should not have permission to access due to lack of proper validation or authentication checks.

**Example BAC:**

1. The admin account page at `/admin` is not visible on the front end.
2. A regular user account tries to access it directly and it works.
3. This escalates privileges to expose admin account information.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8a3e58f79d95---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8a3e58f79d95---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--8a3e58f79d95---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--8a3e58f79d95---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--8a3e58f79d95---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Mike Takahashi (TakSec)](https://miro.medium.com/v2/resize:fill:96:96/1*oeaksoi-GPEkdXjmR0uMFA.jpeg)](https://taksec.medium.com/?source=post_page---post_author_info--8a3e58f79d95---------------------------------------)

[![Mike Takahashi (TakSec)](https://miro.medium.com/v2/resize:fill:128:128/1*oeaksoi-GPEkdXjmR0uMFA.jpeg)](https://taksec.medium.com/?source=post_page---post_author_info--8a3e58f79d95---------------------------------------)

[## Written by Mike Takahashi (TakSec)](https://taksec.medium.com/?source=post_page---post_author_info--8a3e58f79d95---------------------------------------)

[2.3K followers](https://taksec.medium.com/followers?source=post_page---post_author_info--8a3e58f79d95---------------------------------------)

·[768 following](https://medium.com/%40taksec/following?source=post_page---post_author_info--8a3e58f79d95---------------------------------------)

Pentester | Bug Bounty Hunter | AI Red Team <https://twitter.com/TakSec>

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----8a3e58f79d95---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----8a3e58f79d95---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----8a3e58f79d95---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----8a3e58f79d95---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----8a3e58f79d95---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----8a3e58f79d95---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----8a3e58f79d95---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----8a3e58f79d95---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----8a3e58f79d95---------------------------------------)