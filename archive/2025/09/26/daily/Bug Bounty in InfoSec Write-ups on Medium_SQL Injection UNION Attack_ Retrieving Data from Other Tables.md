---
title: SQL Injection UNION Attack: Retrieving Data from Other Tables
url: https://infosecwriteups.com/sql-injection-union-attack-retrieving-data-from-other-tables-aa79bd7862b6?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-26
fetch_date: 2025-10-02T20:42:26.399423
---

# SQL Injection UNION Attack: Retrieving Data from Other Tables

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Faa79bd7862b6&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-union-attack-retrieving-data-from-other-tables-aa79bd7862b6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-union-attack-retrieving-data-from-other-tables-aa79bd7862b6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-aa79bd7862b6---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-aa79bd7862b6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# SQL Injection UNION Attack: Retrieving Data from Other Tables

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:64:64/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---byline--aa79bd7862b6---------------------------------------)

[Bash Overflow](https://bashoverflow.com/?source=post_page---byline--aa79bd7862b6---------------------------------------)

4 min read

·

Sep 24, 2025

--

Share

**How SQL Injection UNION Attacks Reveal Hidden Data from Other Tables**.

🔓 [**Free Link**](https://bashoverflow.com/aa79bd7862b6?sk=651072458da4d16beedae8b52d2da9ed)

Press enter or click to view image in full size

![SQL Injection UNION Attack: Retrieving Data from Other Tables]()

SQL Injection UNION Attack: Retrieving Data from Other Tables

> **Disclaimer:**
> The techniques described in this document are intended solely for ethical use and educational purposes. Unauthorized use of these methods outside approved environments is strictly prohibited, as it is illegal, unethical, and may lead to severe consequences.
>
> It is crucial to act responsibly, comply with all applicable laws, and adhere to established ethical guidelines. Any activity that exploits security vulnerabilities or compromises the safety, privacy, or integrity of others is strictly forbidden.

## Table of Contents

1. [**Summary of the Vulnerability**](#cd76)
2. [**Steps to Reproduce & Proof of Concept (PoC)**](#e765)
3. [**Impact**](#8df4)

## Summary of the Vulnerability

This lab demonstrates how a SQL injection vulnerability in a product category filter can be escalated to access sensitive information stored in other database tables. The application dynamically incorporates user input into SQL queries without proper sanitization or parameterization. As a result, an attacker can manipulate the query by injecting malicious SQL code.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--aa79bd7862b6---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--aa79bd7862b6---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--aa79bd7862b6---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--aa79bd7862b6---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--aa79bd7862b6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:96:96/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---post_author_info--aa79bd7862b6---------------------------------------)

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:128:128/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---post_author_info--aa79bd7862b6---------------------------------------)

[## Written by Bash Overflow](https://bashoverflow.com/?source=post_page---post_author_info--aa79bd7862b6---------------------------------------)

[150 followers](https://bashoverflow.com/followers?source=post_page---post_author_info--aa79bd7862b6---------------------------------------)

·[11 following](https://medium.com/%40bashoverflow/following?source=post_page---post_author_info--aa79bd7862b6---------------------------------------)

Cybersecurity Enthusiast | Sharing insights through some writeups | Passionate about advancing knowledge in the field of cybersecurity

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----aa79bd7862b6---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----aa79bd7862b6---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----aa79bd7862b6---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----aa79bd7862b6---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----aa79bd7862b6---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----aa79bd7862b6---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----aa79bd7862b6---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----aa79bd7862b6---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----aa79bd7862b6---------------------------------------)