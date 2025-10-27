---
title: Mastering Ffuf: Basic and Advanced Commands
url: https://infosecwriteups.com/mastering-ffuf-basic-and-advanced-commands-60e53bdbffc7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-03
fetch_date: 2025-10-02T19:33:15.623528
---

# Mastering Ffuf: Basic and Advanced Commands

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F60e53bdbffc7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmastering-ffuf-basic-and-advanced-commands-60e53bdbffc7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmastering-ffuf-basic-and-advanced-commands-60e53bdbffc7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-60e53bdbffc7---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-60e53bdbffc7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🔍 Mastering Ffuf: Basic and Advanced Commands 🔍

## *Unlocking Hidden Vulnerabilities Through Fuzzing Techniques*

[![BugHunter’s Journal](https://miro.medium.com/v2/resize:fill:64:64/1*1GF8-5GjRBfh2ri72A-yaw.png)](https://medium.com/%40bughuntersjournal?source=post_page---byline--60e53bdbffc7---------------------------------------)

[BugHunter’s Journal](https://medium.com/%40bughuntersjournal?source=post_page---byline--60e53bdbffc7---------------------------------------)

3 min read

·

Sep 1, 2023

--

Share

Press enter or click to view image in full size

![]()

**Ffuf link** :<https://github.com/ffuf/ffuf>

## Basic Ffuf Commands for Effective Fuzzing

## 1. Launching URL Fuzzing with Wordlists

Getting started with Ffuf is all about the basics. Learn how to initiate URL fuzzing using a wordlist

```
Ffuf -w wordlist_location -u http://192.168.1.1/FUZZ
```

🔑 **Pro Tip:** The ‘FUZZ’ parameter acts as a dynamic placeholder for seamless fuzzing.

## 2. Refining Results with HTTP Status Code Filtering

Fine-tuning your results is key. Filter out unwanted HTTP status codes for cleaner insights:

```
Ffuf -w wordlist_location -u http://192.168.1.1/FUZZ -fc 301
```

🎯 **Advanced Filter:** Elevate your exploration by combining filtering with recursion for in-depth subdirectory analysis:

```
Ffuf -w wordlist_location -u http://192.168.1.1/FUZZ -fc 301 --recursion --recursion-depth 2
```

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--60e53bdbffc7---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--60e53bdbffc7---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--60e53bdbffc7---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--60e53bdbffc7---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--60e53bdbffc7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![BugHunter’s Journal](https://miro.medium.com/v2/resize:fill:96:96/1*1GF8-5GjRBfh2ri72A-yaw.png)](https://medium.com/%40bughuntersjournal?source=post_page---post_author_info--60e53bdbffc7---------------------------------------)

[![BugHunter’s Journal](https://miro.medium.com/v2/resize:fill:128:128/1*1GF8-5GjRBfh2ri72A-yaw.png)](https://medium.com/%40bughuntersjournal?source=post_page---post_author_info--60e53bdbffc7---------------------------------------)

[## Written by BugHunter’s Journal](https://medium.com/%40bughuntersjournal?source=post_page---post_author_info--60e53bdbffc7---------------------------------------)

[1.2K followers](https://medium.com/%40bughuntersjournal/followers?source=post_page---post_author_info--60e53bdbffc7---------------------------------------)

·[156 following](https://medium.com/%40bughuntersjournal/following?source=post_page---post_author_info--60e53bdbffc7---------------------------------------)

SQA engineer turned ethical hacker 🔐 | Writing on bugs, pentesting, and cybersecurity | Helping you think like an attacker, stay safe online.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----60e53bdbffc7---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----60e53bdbffc7---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----60e53bdbffc7---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----60e53bdbffc7---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----60e53bdbffc7---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----60e53bdbffc7---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----60e53bdbffc7---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----60e53bdbffc7---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----60e53bdbffc7---------------------------------------)