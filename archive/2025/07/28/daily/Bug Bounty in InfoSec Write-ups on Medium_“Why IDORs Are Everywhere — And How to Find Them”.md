---
title: “Why IDORs Are Everywhere — And How to Find Them”
url: https://infosecwriteups.com/why-idors-are-everywhere-and-how-to-find-them-3ba45128e0f3?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-28
fetch_date: 2025-10-06T23:18:13.938762
---

# “Why IDORs Are Everywhere — And How to Find Them”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F3ba45128e0f3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhy-idors-are-everywhere-and-how-to-find-them-3ba45128e0f3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhy-idors-are-everywhere-and-how-to-find-them-3ba45128e0f3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-3ba45128e0f3---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-3ba45128e0f3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# **“Why IDORs Are Everywhere — And How to Find Them” — Part I**

[![Het Patel](https://miro.medium.com/v2/resize:fill:64:64/1*0xmi1m3lKtIdhh3vz8hFsA.jpeg)](https://hettt.medium.com/?source=post_page---byline--3ba45128e0f3---------------------------------------)

[Het Patel](https://hettt.medium.com/?source=post_page---byline--3ba45128e0f3---------------------------------------)

4 min read

·

Jun 15, 2025

--

3

Listen

Share

Press enter or click to view image in full size

![]()

*This write-up has been prepared under the guidance of* [*Amish Patel*](https://medium.com/%40cyberexpertamish)*,* [*Lay Patel*](https://medium.com/%40cynex) *at* [*Hacker4Help*](https://medium.com/%40hacker4help) *as part of our learning initiative on cybersecurity awareness.*

## Introduction 🔍

Insecure Direct Object Reference (IDOR) is a common yet critical vulnerability in web applications that has consistently remained in the **OWASP Top 10** for over a decade. Often overlooked during development, it allows attackers to access unauthorized resources simply by manipulating input parameters. Despite its apparent simplicity, IDOR has led to major data breaches affecting millions of users, making it one of the most exploited vulnerabilities in modern web applications.

The beauty (and danger) of IDOR lies in its simplicity — no complex exploit chains, no advanced tools required. Just basic parameter manipulation that any curious user could stumble upon.

![]()

## What is IDOR?

IDOR occurs when an application exposes internal object references (like database keys, file names, or user IDs) in a way that allows attackers to manipulate them and gain unauthorized access to resources they shouldn’t be able to view or modify.

**Simple Example:**

```
Normal request: https://banking-app.com/account/12345
Malicious request: https://banking-app.com/account/12346
```

If the application doesn’t verify that the logged-in user owns account `12346`, the attacker gains access to someone else's banking information.

![]()

## Types of IDOR Vulnerabilities

**1. Horizontal IDOR** — Access data at the same privilege level

* User A accessing User B’s profile
* Customer viewing another customer’s orders

**2. Vertical IDOR** — Privilege escalation to higher access levels

* Regular user accessing admin functionalities
* Customer accessing employee-only resources

**3. Blind IDOR** — No direct data exposure but actions can be performed

* Deleting other users’ files without seeing them
* Modifying records without viewing the content

## My Real-World Finding: Exposing Invoices via IDOR

![]()

### The Discovery Process

While conducting a security assessment on a beta e-commerce platform, I discovered a critical IDOR vulnerability that exposed thousands of customer invoices. Here’s how it unfolded:

**Initial Observation:** After making a purchase and navigating to my account dashboard, I noticed the invoice URL:

```
https://redacted-shop.in/myaccount/invoice/print/16?type=print
```

The sequential number `16` immediately caught my attention. In my experience, predictable identifiers are often vulnerable to IDOR attacks.

Press enter or click to view image in full size

![]()

*Address and Mobile number — both are dummy — lol.*

Once i clicked on Invoice:

Press enter or click to view image in full size

![]()

**Testing Methodology:**

1. **Baseline Test**: Confirmed I could access my own invoice.
2. **Parameter Manipulation**: Changed the ID to `17`, `18`, `19`, etc.
3. **Access Verification**: Successfully accessed other users’ invoices
4. **Impact Assessment**: Tested both directions (lower and higher IDs

**What I Found:**

* **Complete invoice access** for other customers
* **Personal information exposure**: Names, addresses, phone numbers
* **Purchase history**: Products bought, quantities, prices
* **Payment details**: Last 4 digits of credit cards, payment methods
* **Order patterns**: Shipping preferences, delivery addresses

All I needed was to be logged into **my own account**. If not logged in, the endpoint

**What This Means** 🧪**:** The server was exposing internal object references (invoice IDs) without verifying if the current user had permission to view them. Anyone with a valid session could access other users’ sensitive data just by manipulating the URL.

**Security Issue** 🔐**:** This is a textbook example of IDOR. The application should have enforced access controls to ensure that only the **logged-in user** could access their own invoices.

**Impact** 🎯**:**

* Unauthorized access to user data
* Potential privacy violations
* Risk of legal and regulatory non-compliance

## How IDOR Happens

* Lack of access control checks
* Exposing predictable object IDs
* Poor session management

## Impact of IDOR Vulnerabilities

* Data leakage
* Account takeover
* Unauthorized actions (modifying or deleting records)
* Full privilege escalation

## Final Thoughts

IDOR is a prime example of how simple mistakes can lead to serious consequences. It reinforces the importance of secure coding practices, regular testing, and awareness among developers and testers alike.

So next time you see a URL with a numeric ID, test it — you might just stumble upon your next big find.

**Follow Me for more deep dives into real-world vulnerabilities and ethical hacking insights. 💡**

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----3ba45128e0f3---------------------------------------)

[Idor](https://medium.com/tag/idor?source=post_page-----3ba45128e0f3---------------------------------------)

[Idor Vulnerability](https://medium.com/tag/idor-vulnerability?source=post_page-----3ba45128e0f3---------------------------------------)

[Poc](https://medium.com/tag/poc?source=post_page-----3ba45128e0f3---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----3ba45128e0f3---------------------------------------)

--

--

3

[![InfoSe...