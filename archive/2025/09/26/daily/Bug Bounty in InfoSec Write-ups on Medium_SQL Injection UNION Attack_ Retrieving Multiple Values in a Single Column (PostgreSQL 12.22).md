---
title: SQL Injection UNION Attack: Retrieving Multiple Values in a Single Column (PostgreSQL 12.22)
url: https://infosecwriteups.com/sql-injection-union-attack-retrieving-multiple-values-in-a-single-column-postgresql-12-22-d5cfb569a38b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-26
fetch_date: 2025-10-02T20:42:31.309579
---

# SQL Injection UNION Attack: Retrieving Multiple Values in a Single Column (PostgreSQL 12.22)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd5cfb569a38b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-union-attack-retrieving-multiple-values-in-a-single-column-postgresql-12-22-d5cfb569a38b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-union-attack-retrieving-multiple-values-in-a-single-column-postgresql-12-22-d5cfb569a38b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d5cfb569a38b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d5cfb569a38b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# SQL Injection UNION Attack: Retrieving Multiple Values in a Single Column (PostgreSQL 12.22)

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:64:64/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---byline--d5cfb569a38b---------------------------------------)

[Bash Overflow](https://bashoverflow.com/?source=post_page---byline--d5cfb569a38b---------------------------------------)

4 min read

·

Sep 25, 2025

--

1

Share

**Discover how a UNION-based SQL injection can be used to retrieve multiple values from a single column, and why this vulnerability poses a serious risk to real-world applications**.

🔓 [**Free Link**](https://bashoverflow.com/d5cfb569a38b?sk=40dd5cfa86bfaa1b7a5774e91d70201b)

Press enter or click to view image in full size

![SQL Injection UNION Attack — Retrieving Multiple Values in a Single Column (PostgreSQL 12.22) — Bashoverflow Medium]()

SQL Injection UNION Attack: Retrieving Multiple Values in a Single Column (PostgreSQL 12.22)

> **Disclaimer:**
> The techniques described in this document are intended solely for ethical use and educational purposes. Unauthorized use of these methods outside approved environments is strictly prohibited, as it is illegal, unethical, and may lead to severe consequences.
>
> It is crucial to act responsibly, comply with all applicable laws, and adhere to established ethical guidelines. Any activity that exploits security vulnerabilities or compromises the safety, privacy, or integrity of others is strictly forbidden.

## Table of Contents

1. [**Summary of the Vulnerability**](#f9c8)
2. [**Steps to Reproduce & Proof of Concept (PoC)**](#fc20)
3. [**Impact**](#f766)

## Summary of the Vulnerability

This lab demonstrates a SQL injection flaw in the product category filter. The underlying SQL query dynamically incorporates user input without proper validation, allowing attackers to manipulate the query. By leveraging the `UNION`…

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d5cfb569a38b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d5cfb569a38b---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--d5cfb569a38b---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--d5cfb569a38b---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--d5cfb569a38b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:96:96/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---post_author_info--d5cfb569a38b---------------------------------------)

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:128:128/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---post_author_info--d5cfb569a38b---------------------------------------)

[## Written by Bash Overflow](https://bashoverflow.com/?source=post_page---post_author_info--d5cfb569a38b---------------------------------------)

[150 followers](https://bashoverflow.com/followers?source=post_page---post_author_info--d5cfb569a38b---------------------------------------)

·[11 following](https://medium.com/%40bashoverflow/following?source=post_page---post_author_info--d5cfb569a38b---------------------------------------)

Cybersecurity Enthusiast | Sharing insights through some writeups | Passionate about advancing knowledge in the field of cybersecurity

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----d5cfb569a38b---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----d5cfb569a38b---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----d5cfb569a38b---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----d5cfb569a38b---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----d5cfb569a38b---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----d5cfb569a38b---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----d5cfb569a38b---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----d5cfb569a38b---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----d5cfb569a38b---------------------------------------)