---
title: 2023 OWASP Top-10 Series: API5:2023 Broken Function Level Authorization
url: https://buaq.net/go-175480.html
source: unSafe.sh - 不安全
date: 2023-08-27
fetch_date: 2025-10-04T11:58:54.419858
---

# 2023 OWASP Top-10 Series: API5:2023 Broken Function Level Authorization

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

2023 OWASP Top-10 Series: API5:2023 Broken Function Level Authorization

Welcome to the 6th post in our weekly series on the new 2023 OWASP API Security Top-10 list,
*2023-8-26 21:45:0
Author: [lab.wallarm.com(查看原文)](/jump-175480.htm)
阅读量:35
收藏*

---

Welcome to the 6th post in our weekly series on the new [2023 OWASP API Security Top-10](https://owasp.org/API-Security/editions/2023/en/0x00-header/) list, with a particular focus on security practitioners. This post will focus on [API5:2023 Broken Function Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/).

In this series we are taking an in-depth look at each category – the details, the impact and what you can do about it. To see previous posts you might have missed, [click here](https://lab.wallarm.com/tag/owasp-apisec-top-10-2023-series/).

## TL;DR

The short summary for Broken Function Level Authorization is very simple: API users can access functions for which they are not authorized. That’s it. Easy to explain, but difficult to avoid.

## The Details

Authorization issues are a theme in the OWASP API Top 10 because they continue to be an issue in APIs deployed in production. In this case, we’re talking about authorization to specific functions. A function might include something like creating a user, adding a new product, transferring money, or changing a price. Generally speaking, function level authorization issues can be broken down into two classes: unauthorized access to specific endpoints and unauthorized access to specific methods.

A couple of examples might help. Let’s say an application has an endpoint /api/{account}/users that lists the users in a particular account, but also has an endpoint /api/admin/users that list all the users in every account. If that second endpoint isn’t appropriately restricted, that would be a function level authorization issue.

A second example involves an endpoint that supports multiple methods. The endpoint /api/products supports the GET method for any user so that all users can view the products available. The POST method is used to add or update products. If POST is not appropriately restricted, this would constitute a Broken Function Level Authorization vulnerability.

You might be wondering why this isn’t a [Broken Object Level Authorization (BOLA)](https://lab.wallarm.com/api12023-broken-object-level-authorization/) or [Broken Object Property Level Authorization vulnerability](https://lab.wallarm.com/api32023-broken-object-property-level-authorization/). If the API endpoint in question is an object, then this would constitute BOLA. In the case of both a broken function and object level authorization issue, there’s no manipulation of a specific property involved, but there certainly is with Broken Object Property Level Authorization. That being said, all three vulnerabilities center around a user having access to something they shouldn’t, so there is strong commonality between all three. For a developer, the distinction is important because it determines how the vulnerability will be fixed. For a security practitioner, it’s less important, but still material to how the vulnerability can be identified and mitigated by security controls.

## What’s the Impact?

As described above, the primary impact of all authorization vulnerabilities is that a user has access to something (object, property, function) they shouldn’t. In this case, the impact is determined by the function to which the unauthorized user has access. They might be able to create or delete users, or perhaps they can edit the price of a product, or even transfer money between accounts. If you’re considering how to model this threat, then you need to understand the functions your API provides and what they allow a user to do.

## What Can You Do About It?

As with most of the OWASP API vulnerabilities, remediation takes place in the code or application. Properly restricting function access is the best way to address this vulnerability, and ensuring consistency in how functions are presented in the API can help make sure that vulnerabilities don’t fall through the cracks.

If you don’t control the API or don’t have access to the developers, or if you simply can’t get a fix completed immediately, then you should look at viable mitigations to reduce the risk. Deploying API monitoring tools that can detect anomalous activity or specific attacks can help identify when this vulnerability is being exploited. Additionally, an inline tool that can actively block attacks can provide stronger mitigation than detection alone.

Exploits of authorization-based vulnerabilities can be difficult to detect because the exploited function is being used within specification, just by a user who shouldn’t be authorized. One way to reduce the overall risk is to maintain good API hygiene. That means ensuring that you have an accurate inventory of APIs and endpoints, that you have API specifications for anything deployed to production, and that you don’t have shadow, orphan, or zombie endpoints.

## How Wallarm Can Help

The [Wallarm Integrated App and API Security platform](https://www.wallarm.com/product/api-security-platform) provides real-time attack detection and mitigation for Broken Function Level Authorization vulnerabilities, including path traversal, forced browsing, open redirects, and cross-site request forgery. Wallarm can also detect vulnerabilities related to Broken Function Level Authorization so that you can reduce the risk before an attack occurs. [Wallarm API Disc](https://www.wallarm.com/product/api-discovery)[overy](https://www.wallarm.com/product/api-discovery) allows you to keep an up-to-date inventory of all your APIs and endpoints, and compare them to API specifications to identify shadow, orphan, and zombie APIs.

## **Learn More**

Come back next week as we dig into the details of another category of the new 2023 OWASP Top-10 API Security Risks list – or [click here](https://lab.wallarm.com/tag/owasp-apisec-top-10-2023-series/) to see previous posts you might have missed.

In the meantime, here are some other resources which might help on your journey to end-to-end API security:

* Solution Brief: [OWASP API Security Top-10 2023 Reference Guide](https://hubspot.wallarm.com/hubfs/OWASP%20APIsec%20Top-10%202023%20Reference%20Guide.pdf) (PDF)
* Blog Post: [OWASP API Security Top-10 Risks for 2023 Released](https://lab.wallarm.com/owasp-api-security-top-10-risks-for-2023-released/)
* Blog Post: [OWASP API Security Top-10 for 2023 Risk Ratings](https://lab.wallarm.com/owasp-api-security-top-10-for-2023-risk-ratings/)
* On-Demand Webinar: [A Practitioner’s Guide to the New 2023 OWASP API Security Update](https://www.wallarm.com/webinars/practitioners-guide-2023-owasp-api-security)
* On-Demand Webinar: [A CISOs Guide to the New 2023 OWASP API Security Update](https://www.wallarm.com/webinars/new-2023-owasp-api-security)
* Research Report: [2022 Year-End API ThreatStats™ Report](https://lab.wallarm.com/2022-year-end-api-threatstats-report/) (blog and linked full report)

## **Protect Your APIs from OWASP API Security Top-10 Threats**

Wallarm End-to-End API Security solution provides comprehensive protection against the OWASP API Security Top-10 threats. And in 2023, we’ve made it even easier for you!

The **Wallarm 2023 OWASP API Security Top-10 Dashboard** provides you with complete visibility into the security state of your APIs, easy identification of your most critical security risks, and ability to immediately a...