---
title: How a Unique Combination Opened the Door to an IDOR
url: https://infosecwriteups.com/how-a-unique-combination-opened-the-door-to-an-idor-f44a3efe51e8?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-11-15
fetch_date: 2025-10-06T19:17:52.240634
---

# How a Unique Combination Opened the Door to an IDOR

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff44a3efe51e8&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-a-unique-combination-opened-the-door-to-an-idor-f44a3efe51e8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-a-unique-combination-opened-the-door-to-an-idor-f44a3efe51e8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f44a3efe51e8---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f44a3efe51e8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How a Unique Combination Opened the Door to an IDOR

[![Supun Halangoda (Suppa)](https://miro.medium.com/v2/resize:fill:64:64/1*ZPhvLhGm-ccWEXH2ZJAx2A.jpeg)](https://medium.com/%40suppaboy?source=post_page---byline--f44a3efe51e8---------------------------------------)

[Supun Halangoda (Suppa)](https://medium.com/%40suppaboy?source=post_page---byline--f44a3efe51e8---------------------------------------)

4 min read

·

Nov 10, 2024

--

3

Listen

Share

Press enter or click to view image in full size

![]()

> Hello everyone! This write-up is part of my **IDOR Diaries** series, where I share insights on the various IDOR vulnerabilities I encounter during my vulnerability hunts.

**Checkout my previous write-ups in this series**

[## IDOR Vulnerability that exposed 17 Million user data (IDOR Diaries)

### Hi all, this write-up is about a vulnerability I discovered a few months back on a private bug bounty program.

infosecwriteups.com](/idor-vulnerability-that-exposed-17-million-user-data-idor-diaries-f0365ffe7a75?source=post_page-----f44a3efe51e8---------------------------------------)

[## Unveiling a Bug: Paying $1 and Receiving $100 (or Any Amount) in Return

### Hi everyone, this write-up is about a vulnerability I discovered in a private bug bounty program. Due to privacy &…

infosecwriteups.com](/unveiling-a-bug-paying-1-and-receiving-100-or-any-amount-in-return-33c5d8321b2d?source=post_page-----f44a3efe51e8---------------------------------------)

[## Hacking Wishlists in an E-commerce Web App (IDOR Diaries)

### If you haven’t checked other writes on the IDOR Diaries series you check below write-ups

infosecwriteups.com](/hacking-wishlists-in-an-e-commerce-web-app-idor-diaries-f6ed9246ae82?source=post_page-----f44a3efe51e8---------------------------------------)

Lets dig in !!

As usual, I was hunting in a program with a limited scope, focusing on a SaaS application. After authenticating in the application, I began exploring its features, specifically testing the ‘**View My Agreements**’ functionality related to an agreement-signing feature. This feature allowed users to check and view their current agreements. The application was well-secured with JWT-based authentication, and most resources were hosted on S3 with signed URLs. However, this particular endpoint’s resources were not hosted in an S3 bucket; instead, they were hosted separately.

Domain e.g: **useragreements.example.com**

The Sample Agreement stored location url was similar to below HTTP Request

Press enter or click to view image in full size

![]()

If you request this URL, it surprisingly displays the specific PDF without any authentication.

**Sample URL:** <https://useragreements.example.com/tenant/signedpdfs/020456760124>

Since the URL ends with a pattern of digits, I tried brute-forcing the digits, but I didn’t receive any valid responses. Instead, the response returned was “**NotFound**.” However, I didn’t give up at this point; I started analyzing the URL further.

I generated more sample PDFs to check how this number pattern was assigned. Then, I noticed an unusual combination within the digits.

**URL Analysis**
Let’s take three sample PDFs generated for this proof of concept (POC). They look as follows:

* /tenant/signedpdfs/020456760124
* /tenant/signedpdfs/020456770124
* /tenant/signedpdfs/020456780124

As you can see, we can break this number pattern into two sections.

Press enter or click to view image in full size

![]()

Whereas the pattern generates **Part 01** as a dynamic value, **Part 02** remains the same.

I then brute-forced the **Part 01** value, thinking I had cracked their pattern. However, I only retrieved my own agreement samples and no unauthorized ones.

After further examination of **Part 02** of the pattern, I cross-referenced the Agreement Signed Date with these values and realized that “0124” represents “**01**” as the month and “**24**” as the year!

I began by changing the month value to brute-force, incrementing each month and brute-forcing **Part 01**.

The brute-force patterns would look like:

**1st Attempt**

```
ffuf -w /path/to/wordlist -u https://useragreements.example.com/tenant/signedpdfs/FUZZ0224
```

**2nd Attempt**

```
ffuf -w /path/to/wordlist -u https://useragreements.example.com/tenant/signedpdfs/FUZZ0324
```

Using this method, I was able to find many PDF agreements containing Personally Identifiable Information (PII) such as Social Security Numbers (SSNs), addresses, names, and dates of birth.

Although this instance was specifically created for a Bug Bounty Program, this misconfiguration allowed access to production data of actual customers.

I reported this vulnerability promptly, and a temporary fix was implemented by adding an authorization token for each request. Later, the entire functionality was migrated to Amazon S3 with signed URLs, providing secure, temporary access and effectively mitigating the risk of unauthorized access to sensitive documents.

I always find these kind of vulnerbiltiies interesting by examing how developers find creative ways to implement these kinds of patterns.

In fact, I recently encountered a similar vulnerability, which you can read about in my write-up below, detailing the discovery process, analysis, and the steps taken to address the issue effectively.

[## Hacking Wishlists in an E-commerce Web App (IDOR Diaries)

### If you haven’t checked other writes on the IDOR Diaries series you check below write-ups

infosecwriteups.com](/hacking-wishlists-in-an-e-commerce-web-app-idor-diaries-f6ed9246ae82?source=post_page-----f44a3efe51e8---------------------------------------)

Thank you for reading my write-up! I’ll be back soon with another one. Happy Hacking !!

![]()

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----f44a3efe51e8---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----f44a3efe51e8-...