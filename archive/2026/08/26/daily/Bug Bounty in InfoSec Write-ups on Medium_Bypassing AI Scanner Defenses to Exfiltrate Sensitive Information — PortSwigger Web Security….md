---
title: Bypassing AI Scanner Defenses to Exfiltrate Sensitive Information — PortSwigger Web Security…
url: https://infosecwriteups.com/bypassing-ai-scanner-defenses-to-exfiltrate-sensitive-information-portswigger-web-security-346b99f322ef?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-08-26
fetch_date: 2026-08-27T12:12:35.114353
---

# Bypassing AI Scanner Defenses to Exfiltrate Sensitive Information — PortSwigger Web Security…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-ai-scanner-defenses-to-exfiltrate-sensitive-information-portswigger-web-security-346b99f322ef&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-ai-scanner-defenses-to-exfiltrate-sensitive-information-portswigger-web-security-346b99f322ef&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-346b99f322ef---------------------------------------)

·

1. [🎯 Lab Overview](/?source=post_page-----346b99f322ef---------------------------------------#14a2 "🎯 Lab Overview")
2. [🏁 Objective](/?source=post_page-----346b99f322ef---------------------------------------#cce9 "🏁 Objective")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-346b99f322ef---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page---header_tags--346b99f322ef---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page---header_tags--346b99f322ef---------------------------------------)

[AI](https://medium.com/tag/ai?source=post_page---header_tags--346b99f322ef---------------------------------------)

[LLM](https://medium.com/tag/llm?source=post_page---header_tags--346b99f322ef---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page---header_tags--346b99f322ef---------------------------------------)

# 🤖 Bypassing AI Scanner Defenses to Exfiltrate Sensitive Information — PortSwigger Web Security Academy

## AI-powered security scanners are becoming increasingly common. They can authenticate to applications, browse sensitive areas, inspect content, and even perform security audits.

[![Mukilan Baskaran](https://miro.medium.com/v2/resize:fill:64:64/1*tif1c7lTx883WhLR92OsxA.jpeg)](https://mukibas37.medium.com/?source=post_page---byline--346b99f322ef---------------------------------------)

[Mukilan Baskaran](https://mukibas37.medium.com/?source=post_page---byline--346b99f322ef---------------------------------------)

9 min read

·

Aug 8, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D346b99f322ef&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-ai-scanner-defenses-to-exfiltrate-sensitive-information-portswigger-web-security-346b99f322ef&source=---header_actions--346b99f322ef---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

Friend’s link for non-members access: [link](https://mukibas37.medium.com/bypassing-ai-scanner-defenses-to-exfiltrate-sensitive-information-portswigger-web-security-346b99f322ef?sk=9fa79120cd4452a429e9aa02425cf88f)

But what happens when the **AI scanner itself can be manipulated by content inside the application?** 🤔

That is exactly what this **PortSwigger Web Security Academy** lab demonstrates.

In this lab, an AI-powered scanner has access to sensitive information, including users’ API keys. It is authenticated as the victim user **Carlos** and is designed to explore authenticated areas of the application.

The challenge is to exploit **indirect prompt injection** to make the AI scanner reveal Carlos’s API key. 🔐

## 🎯 Lab Overview

**Lab:** Bypassing AI scanner defenses to exfiltrate sensitive information

**Difficulty:** 🟠 Practitioner

## 🏁 Objective

The goal is to:

> *🔑 Exfiltrate and submit the API key*…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--346b99f322ef---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--346b99f322ef---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--346b99f322ef---------------------------------------)

[88K followers](/followers?source=post_page---post_publication_info--346b99f322ef---------------------------------------)

·[Last published 1 day ago](/one-email-one-click-one-enterprise-wide-ransomware-incident-995808f1150a?source=post_page---post_publication_info--346b99f322ef---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Mukilan Baskaran](https://miro.medium.com/v2/resize:fill:96:96/1*tif1c7lTx883WhLR92OsxA.jpeg)](https://mukibas37.medium.com/?source=post_page---post_author_info--346b99f322ef---------------------------------------)

[![Mukilan Baskaran](https://miro.medium.com/v2/resize:fill:128:128/1*tif1c7lTx883WhLR92OsxA.jpeg)](https://mukibas37.medium.com/?source=post_page---post_author_info--346b99f322ef---------------------------------------)

[## Written by Mukilan Baskaran](https://mukibas37.medium.com/?source=post_page---post_author_info--346b99f322ef---------------------------------------)

[876 followers](https://mukibas37.medium.com/followers?source=post_page---post_author_info--346b99f322ef---------------------------------------)

·[1.1K following](https://medium.com/%40mukibas37/following?source=post_page---post_author_info--346b99f322ef---------------------------------------)

CTF player | Cyber Security Enthusiast

[Help](https://help.medium.com/hc/en-us?source=post_page-----346b99f322ef---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----346b99f322ef---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----346b99f322ef---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----346b99f322ef---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----346b99f322ef---------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----346b99f322ef---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----346b99f322ef--------------------------------...