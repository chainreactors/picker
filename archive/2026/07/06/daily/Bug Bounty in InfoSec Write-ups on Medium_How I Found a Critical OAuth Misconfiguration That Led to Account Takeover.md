---
title: How I Found a Critical OAuth Misconfiguration That Led to Account Takeover
url: https://infosecwriteups.com/how-i-found-a-critical-oauth-misconfiguration-that-led-to-account-takeover-abfec43eaea6?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-06
fetch_date: 2026-07-07T06:03:28.552131
---

# How I Found a Critical OAuth Misconfiguration That Led to Account Takeover

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-a-critical-oauth-misconfiguration-that-led-to-account-takeover-abfec43eaea6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-a-critical-oauth-misconfiguration-that-led-to-account-takeover-abfec43eaea6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-abfec43eaea6---------------------------------------)

·

1. [Introduction](/?source=post_page-----abfec43eaea6---------------------------------------#8a26 "Introduction")
2. [Understanding the Environment](/?source=post_page-----abfec43eaea6---------------------------------------#add7 "Understanding the Environment")
3. [Finding #1: Open OAuth Client Registration](/?source=post_page-----abfec43eaea6---------------------------------------#bf8d "Finding #1: Open OAuth Client Registration")
4. [Finding #2: Authorization Requests Were Processed Without Authentication](/?source=post_page-----abfec43eaea6---------------------------------------#89dd "Finding #2: Authorization Requests Were Processed Without Authentication")
5. [Finding #3: PKCE Didn’t Fully Protect the Flow](/?source=post_page-----abfec43eaea6---------------------------------------#ad80 "Finding #3: PKCE Didn’t Fully Protect the Flow")
6. [Finding #4: Wildcard CORS](/?source=post_page-----abfec43eaea6---------------------------------------#7da9 "Finding #4: Wildcard CORS")
7. [Finding #5: Google SSO Auto-Provisioning](/?source=post_page-----abfec43eaea6---------------------------------------#eacf "Finding #5: Google SSO Auto-Provisioning")
8. [Building the Attack Chain](/?source=post_page-----abfec43eaea6---------------------------------------#2501 "Building the Attack Chain")
9. [Step 1](/?source=post_page-----abfec43eaea6---------------------------------------#74d3 "Step 1")
10. [Step 2](/?source=post_page-----abfec43eaea6---------------------------------------#48d8 "Step 2")
11. [Step 3](/?source=post_page-----abfec43eaea6---------------------------------------#2925 "Step 3")
12. [Step 4](/?source=post_page-----abfec43eaea6---------------------------------------#1706 "Step 4")
13. [Step 5](/?source=post_page-----abfec43eaea6---------------------------------------#e2ba "Step 5")
14. [Step 6](/?source=post_page-----abfec43eaea6---------------------------------------#e095 "Step 6")
15. [Impact](/?source=post_page-----abfec43eaea6---------------------------------------#96b4 "Impact")
16. [Why This Vulnerability Was Critical](/?source=post_page-----abfec43eaea6---------------------------------------#ff98 "Why This Vulnerability Was Critical")
17. [Remediation](/?source=post_page-----abfec43eaea6---------------------------------------#4e34 "Remediation")
    1. [Authenticate OAuth Client Registration](/?source=post_page-----abfec43eaea6---------------------------------------#d1d6 "Authenticate OAuth Client Registration")
    2. [Validate Redirect URIs](/?source=post_page-----abfec43eaea6---------------------------------------#3635 "Validate Redirect URIs")
    3. [Enforce Authentication](/?source=post_page-----abfec43eaea6---------------------------------------#ce4e "Enforce Authentication")
    4. [Strengthen OAuth Client Validation](/?source=post_page-----abfec43eaea6---------------------------------------#bba7 "Strengthen OAuth Client Validation")
    5. [Restrict CORS](/?source=post_page-----abfec43eaea6---------------------------------------#34ff "Restrict CORS")
    6. [Monitor OAuth Abuse](/?source=post_page-----abfec43eaea6---------------------------------------#d985 "Monitor OAuth Abuse")
18. [Lessons Learned](/?source=post_page-----abfec43eaea6---------------------------------------#b2bc "Lessons Learned")
19. [Responsible Disclosure](/?source=post_page-----abfec43eaea6---------------------------------------#2184 "Responsible Disclosure")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-abfec43eaea6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# How I Found a Critical OAuth Misconfiguration That Led to Account Takeover

[![Shafayat Ahmed Alif](https://miro.medium.com/v2/resize:fill:64:64/1*W4tcAgumVwu7Sr8in6z-FA.jpeg)](https://medium.com/%40iamshafayat?source=post_page---byline--abfec43eaea6---------------------------------------)

[Shafayat Ahmed Alif](https://medium.com/%40iamshafayat?source=post_page---byline--abfec43eaea6---------------------------------------)

7 min read

·

Jun 9, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dabfec43eaea6&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-a-critical-oauth-misconfiguration-that-led-to-account-takeover-abfec43eaea6&source=---header_actions--abfec43eaea6---------------------post_audio_button------------------)

Share

*A bug bounty story about OAuth, PKCE, open client registration, and how multiple low-level issues chained together into a critical account takeover vulnerability.*

## Introduction

While testing a self-hosted platform during a bug bounty engagement, my teammate [Kazi Sabbir](https://www.linkedin.com/in/kazisabbir1337/) and I discovered a series of OAuth misconfigurations that could be chained together to achieve full account takeover of authenticated users.

Individually, some of these findings might not appear critical. However, when combined, they created a dangerous attack path that allowed an attacker to obtain valid OAuth tokens belonging to another user and gain persistent access to their account.

After responsibly disclosing the issue, the vulnerability was validated and rewarded.

In this writeup, I’ll walk through the discovery process, explain the OAuth flow involved, and show how several seemingly minor security weaknesses combined into a critical vulnerability.

Press enter or click to view image in full size

![]()

Photo Credit: Gemini

## Understanding the Environment

During reconnaissance, I used my tool **JSpider** (<https://iamshafayat.github.io/JSpider/>) and its **Sensitive Path Prober** feature to look for interesting files and endpoints that are commonly exposed by web applications.

One of the paths that returned a **200 OK** response was:

```
GET /.well-known/oauth-authorization-server
```

Finding this endpoint immediately caught my attention because OAuth authorization server metadata often reveals valuable information about how authentication and authorization are implemented.

After visiting the endpoint, I found the following configuration details:

```
{
  "issuer": "https...