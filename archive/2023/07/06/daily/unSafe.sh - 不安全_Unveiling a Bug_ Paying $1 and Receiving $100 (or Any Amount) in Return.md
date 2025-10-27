---
title: Unveiling a Bug: Paying $1 and Receiving $100 (or Any Amount) in Return
url: https://buaq.net/go-171303.html
source: unSafe.sh - 不安全
date: 2023-07-06
fetch_date: 2025-10-04T11:51:21.120722
---

# Unveiling a Bug: Paying $1 and Receiving $100 (or Any Amount) in Return

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Unveiling a Bug: Paying $1 and Receiving $100 (or Any Amount) in Return

Photo by Emilio Takas on UnsplashHi everyone, this write-up is about a vulnerability I discovered in
*2023-7-5 23:37:36
Author: [infosecwriteups.com(查看原文)](/jump-171303.htm)
阅读量:17
收藏*

---

Photo by [Emilio Takas](https://unsplash.com/%40emiliotakas?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

Hi everyone, this write-up is about a vulnerability I discovered in a private bug bounty program. Due to privacy & legal concerns, I will be providing sample requests and screenshots to illustrate the vulnerability.

If you are interested in my previous write-ups, you can find them below:

In this write-up, I will discuss a critical bug that I discovered within a payment system, which allowed me to exploit a payment of $1 and receive $100 in return. This vulnerability exposed a significant flaw in the system’s payment processing logic, enabling me to leverage it for personal gain. Through meticulous testing and analysis, I successfully identified and verified the bug, highlighting the potential risks involved and providing recommendations for remediation.

The application I was testing had a payment option where, to recharge my account, I needed to enter the desired amount and click on the recharge button. This action would redirect me to an IPG (Internet Payment Gateway). However, when I intercepted the traffic using Burp Suite, I observed that the web application made additional requests and verifications before directly sending the request to the IPG. The vulnerable request is depicted in the image below.

Sample Request

As seen in the image above, there are two endpoints where the amount is specified. Based on my analysis, the ***“payment\_amount”*** endpoint is responsible for deducting $100 from my credit card, while the ***“recharge\_amount”*** endpoint determines the amount to be recharged into my account.

The vulnerability lies in the fact that the ***“payment\_amount”*** endpoint lacks proper data validation. This allowed me to manipulate the payment amount and deduct only $1 from my credit card while simultaneously recharging $100 into my account. I attempted to enter $0, but it failed at the IPG stage due to an invalid amount.

So, the vulnerable request would be similar to the image shown below, where the “***payment\_amount”*** is set to $1 and the ***“recharge\_amount”*** is set to $100.

Vulnerable request

After the above request is sent, the IPG accepts the payment and updates it as a credit card payment of $1, as shown in the image below.

Accepts by IPG

IPG Request

Finally, when I entered my card details and paid $1, my account was recharged by $100. And similarly, I tested the vulnerability up to $50,000 without raising any suspicion until I responsibly reported to them.

## **Impact and Potential Risks**

The impact of this bug is significant, as it allows any user to manipulate the payment system for personal gain. This not only exposes the organization to financial losses but also undermines the integrity of the payment infrastructure. The potential risks associated with this vulnerability include fraudulent activities, financial exploitation, and severe reputational damage to the affected organization.

## **Recommendations**

In light of this discovery, it is crucial for the organization to address this vulnerability promptly. To remediate the bug, I recommend the following actions:

1. Implement thorough input validation and robust payment processing logic to ensure accurate handling of transactions.
2. Conduct comprehensive code reviews and security testing to identify and rectify similar vulnerabilities throughout the application.
3. Regularly monitor payment transactions for any suspicious activity or anomalies.
4. Consider establishing a bug bounty program or engaging in security audits to leverage the expertise of the wider security community in identifying and mitigating vulnerabilities.

## **Summary of my write-up**

> This write-up discusses a critical vulnerability discovered within a payment system during a private bug bounty program. The vulnerability allowed the author to exploit a payment of $1 and receive $100 in return. By analyzing the system’s payment processing logic, the author identified a flaw in the validation of payment amounts, enabling them to manipulate the payment request. Through sample requests and screenshots, the author demonstrated how they set the payment amount to $1 and the recharge amount to $100, successfully recharging their account without deducting the appropriate payment from their credit card. The author also highlighted that they tested the vulnerability up to $50,000 without detection. The potential impact and risks of the vulnerability were discussed, including financial losses, fraudulent activities, and reputational damage. Recommendations were provided to fix the vulnerability.
>
> Please remember to use this knowledge responsibly and comply with legal and ethical guidelines when conducting security assessments and disclosing vulnerabilities.

文章来源: https://infosecwriteups.com/unveiling-a-bug-paying-1-and-receiving-100-or-any-amount-in-return-33c5d8321b2d?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)