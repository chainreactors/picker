---
title: Unveiling a Bug: Paying $1 and Receiving $100 (or Any Amount) in Return
url: https://infosecwriteups.com/unveiling-a-bug-paying-1-and-receiving-100-or-any-amount-in-return-33c5d8321b2d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-07-06
fetch_date: 2025-10-04T11:53:07.806316
---

# Unveiling a Bug: Paying $1 and Receiving $100 (or Any Amount) in Return

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F33c5d8321b2d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funveiling-a-bug-paying-1-and-receiving-100-or-any-amount-in-return-33c5d8321b2d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funveiling-a-bug-paying-1-and-receiving-100-or-any-amount-in-return-33c5d8321b2d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-33c5d8321b2d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-33c5d8321b2d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Unveiling a Bug: Paying $1 and Receiving $100 (or Any Amount) in Return

[![Supun Halangoda (Suppa)](https://miro.medium.com/v2/resize:fill:64:64/1*ZPhvLhGm-ccWEXH2ZJAx2A.jpeg)](https://medium.com/%40suppaboy?source=post_page---byline--33c5d8321b2d---------------------------------------)

[Supun Halangoda (Suppa)](https://medium.com/%40suppaboy?source=post_page---byline--33c5d8321b2d---------------------------------------)

4 min read

·

Jun 23, 2023

--

3

Listen

Share

Press enter or click to view image in full size

![]()

Photo by [Emilio Takas](https://unsplash.com/%40emiliotakas?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Hi everyone, this write-up is about a vulnerability I discovered in a private bug bounty program. Due to privacy & legal concerns, I will be providing sample requests and screenshots to illustrate the vulnerability.

If you are interested in my previous write-ups, you can find them below:

[## IDOR Vulnerability that exposed 17 Million user data (IDOR Diaries)

### Hi all, this write-up is about a vulnerability I discovered a few months back on a private bug bounty program.

infosecwriteups.com](/idor-vulnerability-that-exposed-17-million-user-data-idor-diaries-f0365ffe7a75?source=post_page-----33c5d8321b2d---------------------------------------)

## **Introduction**

In this write-up, I will discuss a critical bug that I discovered within a payment system, which allowed me to exploit a payment of $1 and receive $100 in return. This vulnerability exposed a significant flaw in the system’s payment processing logic, enabling me to leverage it for personal gain. Through meticulous testing and analysis, I successfully identified and verified the bug, highlighting the potential risks involved and providing recommendations for remediation.

The application I was testing had a payment option where, to recharge my account, I needed to enter the desired amount and click on the recharge button. This action would redirect me to an IPG (Internet Payment Gateway). However, when I intercepted the traffic using Burp Suite, I observed that the web application made additional requests and verifications before directly sending the request to the IPG. The vulnerable request is depicted in the image below.

Press enter or click to view image in full size

![]()

Sample Request

As seen in the image above, there are two endpoints where the amount is specified. Based on my analysis, the ***“payment\_amount”*** endpoint is responsible for deducting $100 from my credit card, while the ***“recharge\_amount”*** endpoint determines the amount to be recharged into my account.

The vulnerability lies in the fact that the ***“payment\_amount”*** endpoint lacks proper data validation. This allowed me to manipulate the payment amount and deduct only $1 from my credit card while simultaneously recharging $100 into my account. I attempted to enter $0, but it failed at the IPG stage due to an invalid amount.

So, the vulnerable request would be similar to the image shown below, where the “***payment\_amount”*** is set to $1 and the ***“recharge\_amount”*** is set to $100.

Press enter or click to view image in full size

![]()

Vulnerable request

After the above request is sent, the IPG accepts the payment and updates it as a credit card payment of $1, as shown in the image below.

Press enter or click to view image in full size

![]()

Accepts by IPG

![]()

IPG Request

Finally, when I entered my card details and paid $1, my account was recharged by $100. And similarly, I tested the vulnerability up to $50,000 without raising any suspicion until I responsibly reported to them.

### **Impact and Potential Risks**

The impact of this bug is significant, as it allows any user to manipulate the payment system for personal gain. This not only exposes the organization to financial losses but also undermines the integrity of the payment infrastructure. The potential risks associated with this vulnerability include fraudulent activities, financial exploitation, and severe reputational damage to the affected organization.

### **Recommendations**

In light of this discovery, it is crucial for the organization to address this vulnerability promptly. To remediate the bug, I recommend the following actions:

1. Implement thorough input validation and robust payment processing logic to ensure accurate handling of transactions.
2. Conduct comprehensive code reviews and security testing to identify and rectify similar vulnerabilities throughout the application.
3. Regularly monitor payment transactions for any suspicious activity or anomalies.

### **Summary of my write-up**

> This write-up discusses a critical vulnerability discovered within a payment system during a private bug bounty program. The vulnerability allowed the author to exploit a payment of $1 and receive $100 in return. By analyzing the system’s payment processing logic, the author identified a flaw in the validation of payment amounts, enabling them to manipulate the payment request. Through sample requests and screenshots, the author demonstrated how they set the payment amount to $1 and the recharge amount to $100, successfully recharging their account without deducting the appropriate payment from their credit card. The author also highlighted that they tested the vulnerability up to $50,000 without detection. The potential impact and risks of the vulnerability were discussed, including financial losses, fraudulent activities, and reputational damage. Recommendations were provided to fix the vulnerability.
>
> Please remember to use this knowledge responsibly and comply with legal and ethical guidelines when conducting security assessments and disclosing vulnerabilities.

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----33c5d8321b2d---------------------------------------)

[Bug...