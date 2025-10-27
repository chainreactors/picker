---
title: 2023 OWASP Top-10 Series: API1:2023 Broken Object Level Authorization
url: https://buaq.net/go-173200.html
source: unSafe.sh - 不安全
date: 2023-07-30
fetch_date: 2025-10-04T11:51:01.216488
---

# 2023 OWASP Top-10 Series: API1:2023 Broken Object Level Authorization

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

![](https://8aqnet.cdn.bcebos.com/19b18374a73cfe31fa865d957f1ad87a.jpg)

2023 OWASP Top-10 Series: API1:2023 Broken Object Level Authorization

Welcome to the 2nd post in our weekly series on the new 2023 OWASP API Security Top-10 list,
*2023-7-29 21:45:0
Author: [lab.wallarm.com(查看原文)](/jump-173200.htm)
阅读量:31
收藏*

---

Welcome to the 2nd post in our weekly series on the new [2023 OWASP API Security Top-10](https://owasp.org/API-Security/editions/2023/en/0x00-header/) list, with a particular focus on security practitioners. This post will focus on [API1:2023 Broken Object Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/).

In this series we are taking an in-depth look at each category – the details, the impact and what you can do about it. To see previous posts you might have missed, [click here](https://lab.wallarm.com/category/owasp/).

## TL;DR

The application behind the API fails to validate permissions for every call to every object. The attacker manipulates the object in the API call to gain access to data or functionality they shouldn’t have.

## The Details

To understand Broken Object Level Authorization (BOLA), you need to start with the concepts of authentication and authorization. Simply put, authentication is about confirming identity and authorization is about permissions for that confirmed identity to do something specific. When I log into an application, it’s authenticating me. When I try to do something in that application, it’s authorizing the identity with which I authenticated to do that thing.

As we’re talking about APIs specifically, the concepts remain the same, but the details change a little. Authentication generally takes place at the beginning of a session and is persisted for that session. Once authenticated, the application should validate that the authenticated user has permission to carry out an operation each time the request to do so. In other words, the application should perform authorization at the object level.

If the application doesn’t do so, then the authenticated user may be able to access objects they shouldn’t. In most cases, this is accomplished by manipulating the object included in the API call. For example, an API call to change a password may reference a user object by an ID. If changing that ID to another user results in a successful password change for that user, then the application is vulnerable to BOLA.

## What’s the Impact?

Obviously, attackers can use BOLA vulnerabilities to access data that should be restricted. They can also use them to execute an account takeover or elevate permissions. In reality, the impact is as variable as the capabilities of the application itself. If it’s a banking application, then there are obvious potential financial impacts. If the application stores sensitive information, then compromise of that information is possible.

## What Can You Do About It?

Addressing BOLA ultimately requires changes to the application itself to adequately enforce object level authorization. In order to do so, however, you have to identify the issue first. Detection of BOLA vulnerabilities, both in development and in production, is the first step in mitigating the risk. Changing code and redeploying applications takes time, and comes with some risk as well. For cases where you either can’t fix the BOLA issues or where you can’t fix them right away, it’s important to have an inline API security tool that can identify and block BOLA attacks.

## How Wallarm Can Help

Wallarm offers BOLA protection as part of our [Advanced API Security](https://www.wallarm.com/product/advanced-api-security) subscription. When enabled, Wallarm will identify API endpoints that are vulnerable to BOLA and actively protect them automatically. Additionally, the Wallarm platform allows users to create custom triggers to respond to BOLA attacks with specific actions or notifications beyond simply blocking the attack.

## **Learn More**

Come back next week as we dig into the details of another category of the new 2023 OWASP Top-10 API Security Risks list – or [click here](https://lab.wallarm.com/category/owasp/) to see previous posts you might have missed.

In the meantime, here are some other resources which might help on your journey to end-to-end API security:

* Solution Brief: [OWASP API Security Top-10 2023 Reference Guide](https://hubspot.wallarm.com/hubfs/OWASP%20APIsec%20Top-10%202023%20Reference%20Guide.pdf) (PDF)
* Blog Post: [OWASP API Security Top-10 Risks for 2023 Released](https://lab.wallarm.com/owasp-api-security-top-10-risks-for-2023-released/)
* Blog Post: [OWASP API Security Top-10 for 2023 Risk Ratings](https://lab.wallarm.com/owasp-api-security-top-10-for-2023-risk-ratings/)
* On-Demand Webinar: [A Practitioner’s Guide to the New 2023 OWASP API Security Update](https://www.wallarm.com/webinars/practitioners-guide-2023-owasp-api-security)
* On-Demand Webinar: [A CISOs Guide to the New 2023 OWASP API Security Update](https://www.wallarm.com/webinars/new-2023-owasp-api-security)
* Research Report: [2022 Year-End API ThreatStats™ Report](https://lab.wallarm.com/2022-year-end-api-threatstats-report/) (blog and linked full report)

## **Protect Your APIs from OWASP API Security Top-10 Threats**

Wallarm End-to-End API Security solution provides comprehensive protection against the OWASP API Security Top-10 threats. And in 2023, we’ve made it even easier for you!

The **Wallarm 2023 OWASP API Security Top-10 Dashboard** provides you with complete visibility into the security state of your APIs, easy identification of your most critical security risks, and ability to immediately apply protective measures.

[![](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2023/07/Wallarm_OWASP_APIsec_Top-10_2923_Dashboard.png?resize=770%2C550&ssl=1)](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2023/07/Wallarm_OWASP_APIsec_Top-10_2923_Dashboard.png?ssl=1)

If you are interested in learning more about how we can help you protect your APIs, please [**schedule a demo**](https://www.wallarm.com/request-demo) with one of our security experts today!

文章来源: https://lab.wallarm.com/api12023-broken-object-level-authorization/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)