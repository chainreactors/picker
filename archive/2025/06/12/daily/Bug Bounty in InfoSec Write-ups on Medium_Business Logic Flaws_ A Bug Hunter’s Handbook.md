---
title: Business Logic Flaws: A Bug Hunter’s Handbook
url: https://infosecwriteups.com/business-logic-flaws-a-bug-hunters-handbook-293f6a89a7f4?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-06-12
fetch_date: 2025-10-06T22:51:43.897488
---

# Business Logic Flaws: A Bug Hunter’s Handbook

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F293f6a89a7f4&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbusiness-logic-flaws-a-bug-hunters-handbook-293f6a89a7f4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbusiness-logic-flaws-a-bug-hunters-handbook-293f6a89a7f4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-293f6a89a7f4---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-293f6a89a7f4---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Business Logic Flaws: A Bug Hunter’s Handbook

[![Gr3yG05T](https://miro.medium.com/v2/resize:fill:64:64/1*Wmq_Knpl7rhxYZqheFuINQ.jpeg)](https://gr3yg05t.medium.com/?source=post_page---byline--293f6a89a7f4---------------------------------------)

[Gr3yG05T](https://gr3yg05t.medium.com/?source=post_page---byline--293f6a89a7f4---------------------------------------)

13 min read

·

Jun 7, 2025

--

Listen

Share

Press enter or click to view image in full size

![]()

Business logic flaws, also known as application logic flaws, occur when an application’s legitimate functionality is misused in ways the developers never intended. Unlike typical code bugs like XSS or SQLi, these are **design-level weaknesses**, not implementation errors. As one recent overview puts it, these are flaws where the application works *technically* as intended, but not as per the *business rules.*

In other words, the code might not be insecure in the usual sense, but the design allows users to do things the business never intended. Unlike code-related bugs, logic flaws rely on a creative understanding of the app’s workflows and assumptions. For example, imagine a checkout form that allows users to modify price or quantity fields directly on the client side. If the backend doesn’t revalidate those values, an attacker could quietly alter the final cost, bypassing discounts, limits, or billing checks.

One famous case involved Stripe, where a researcher exploited a race condition to **redeem a $20,000 discount 30 times in parallel**, gifting himself over **$600,000 in credits** [[1](https://hackerone.com/reports/1849626)]. The bug wasn’t in the code’s syntax, but in the **absence of logical locking**. Stripe paid a $5,000 bounty and quickly patched the issue. It stems from wrong assumptions about user behavior or missing checks in workflows. Left unpatched, such flaws can cost companies money, reputation, and regulatory fines. Because logic flaws depend on the *intended flow* of an app, they require human insight to find. As such, they often evade automated scanners and are prized by bounty programs.

According to HackerOne, *10% of all vulnerabilities reported to the cryptocurrency and blockchain industry are logical bugs, and 45% of their total bounty payout dollars go to logic bugs* [[2](https://www.hackerone.com/blog/how-business-logic-vulnerability-led-unlimited-discount-redemption)]. That’s nearly half the budget going toward a class of bugs that most tools can’t detect. In 2025, with surface-level bugs largely patched, more hunters are focusing on logic flaws to make an impact.

## Common Types of Logic Flaws

Real-world logic bugs fall into several broad categories. Here are some frequent patterns seen in bug bounties:

* **Client-Side Trust / Tampering:** The app trusts data such as price, role, or other parameters from the browser without re-validating on the server. An attacker simply uses a proxy to modify form values and bypasses rules. These issues “give clients too much control” and let hackers skip checks. Example: In one finding, a hunter was able to get admin access by inserting `admin` into the `userDetails` field. [[3](https://medium.com/%40gr3yg05t/business-logic-flaws-a-bug-hunters-handbook-293f6a89a7f4)]
* **Insufficient Data Validation:** Unexpected inputs break workflows. For example, allowing *negative* or extremely *large* numberscan reverse logic. If a transfer form accepts a negative amount, the app may send money to you instead of from you. Negative quantity or huge discount values can similarly cheat calculations. These cases often slip through since client-side checks can be bypassed.
* **Workflow Bypass (Assumption Failures):** The app assumes users *follow steps in order*. If you skip step 2 or repeat steps out of sequence, unexpected states occur. Attackers skip steps, remove parameters, or trigger functions in odd sequences to confuse the system. Failure to enforce the intended sequence can let users gain privileges or access data they shouldn’t.
* **Access Control / ID Issues:** Logic flaws often show up as **authentication/authorization bypasses**. For instance, an IDOR (Insecure Direct Object Reference) where attackers supply a different user’s ID and the server serves another user’s data. Strictly speaking this is a flawed access-control logic, not just a missing check.
* **Race Conditions:** Timing issues can subvert logic. The Stripe discount example above was a race condition: rapid, parallel requests let one redemption slip through additional fixes. Any feature that should only happen “once” (single-use coupon, one-time transaction) is a candidate for race-based abuse.
* **Domain-Specific Flaws:** These depend on business rules unique to the app. E.g., loyalty points or discounts might not re-validate when cart contents change, letting people abuse promotions. A classic case: apply discount, then remove items, original discount threshold no longer met, but system never checks again. Every industry has its own quirks, so logic bugs are often bespoke but follow similar themes.
* **Other Patterns:** ID enumeration, payment logic flaws , and broken rate-limit logic are also logic issues. In short, if it’s about how the app’s processes are supposed to work, there’s potential for logic error.

## The Hunting Process

**1. Understand the workflow.** Before testing, use the application like a normal user and map out every step of the user and admin flows. Create a simple diagram or bullet list of the normal flow like how I do it:

```
User adds item to cart → selects shipping → pays via Stripe → order confirmed
```

Take notes in a way that you understand the application logic later you visit the note again.

Identify all business rules like:

* Limits: The Application assigns one free coupon per user
* subscriptions: Free delivery is only available to premium users
* Promotions: After ordering 10 products, a user gets the top user role, etc

This stage ...