---
title: 2023 OWASP Top-10 Series: API3:2023 Broken Object Property Level Authorization
url: https://buaq.net/go-174299.html
source: unSafe.sh - 不安全
date: 2023-08-13
fetch_date: 2025-10-04T11:58:48.127330
---

# 2023 OWASP Top-10 Series: API3:2023 Broken Object Property Level Authorization

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

2023 OWASP Top-10 Series: API3:2023 Broken Object Property Level Authorization

Welcome to the 4th post in our weekly series on the new 2023 OWASP API Security Top-10 list,
*2023-8-12 21:45:0
Author: [lab.wallarm.com(查看原文)](/jump-174299.htm)
阅读量:24
收藏*

---

Welcome to the 4th post in our weekly series on the new [2023 OWASP API Security Top-10](https://owasp.org/API-Security/editions/2023/en/0x00-header/) list, with a particular focus on security practitioners. This post will focus on [API3:2023 Broken Object Property Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/).

In this series we are taking an in-depth look at each category – the details, the impact and what you can do about it. To see previous posts you might have missed, [click here](https://lab.wallarm.com/category/owasp/).

## TL;DR

Not every user should have access to all the properties of an object, even when they are authorized to access some of the properties of that object. Broken Object Property Level Authorization vulnerabilities occur when authorization isn’t performed at a granular enough level. Attackers can take advantage of these vulnerabilities to access or alter properties maliciously.

## The Details

Sometimes the best way to understand how a vulnerability works is to consider an example. Let’s say an application has a *user* object, and it has properties like *first\_name, last\_name, email\_address, is\_admin*.

Those first three properties might be available to the user to edit. In other words, I can change my own name and email. That last property should only be editable by someone with appropriate permissions. I’m not allowed to make myself an admin, right? Maybe the UI for this application doesn’t display that last property at all, so I can’t change it myself, but the API doesn’t actually validate the permissions to edit it.

An API call to update my email address might be maliciously altered to also set that *is\_admin* property to true. While that example illustrates the basic idea of Broken Object Property Level Authorization, it’s important to keep in mind that the possible exploit scenarios are as variable as the API object properties out in the world.

## What’s the Impact?

It should be clear from the example above that the immediate impact of these types of vulnerabilities is that attackers can alter properties to which they shouldn’t have access. They might also have access to data that should be prohibited as well. The specific impact depends on the properties in question. Escalating privileges is certainly a possibility, but so is simply altering data or gaining access to sensitive information.

## What Can You Do About It?

Most of the actions to remediate object property permission issues are targeted at developers, such as making sure that permissions are checked at the property level and avoiding returning all properties in responses. Of course, these are valuable actions to take, if you are a developer or have access to the developers.

But increasingly these vulnerabilities are occurring in third-party APIs over which security teams have relatively little direct control. Even in the cases where an organization owns the code behind the APIs they’re protecting, organizational obstacles can get in the way of remediation. Security teams aren’t powerless, however.

The first step to addressing these conditions to ensure you know about them, so starting with discovery is vital. Identifying vulnerable API endpoints allows you to instruct developers to fix issues, and to report to third-party vendors when their APIs are vulnerable. Additionally, an inline API security tool can monitor traffic for actual attacks, such as Mass Assignment, that exploit these vulnerabilities. A tool that can actively block attacks can give security teams peace of mind for the situations in which a vulnerability can’t be addressed quickly.

## How Wallarm Can Help

One of the consequences of these attacks can be that sensitive information appears in API traffic. Of course, leaking sensitive information is a problem by itself, whether it’s a consequence of broken object property authorization or not. [Wallarm Advanced API Security](https://www.wallarm.com/product/advanced-api-security) will detect sensitive data leakage and show users where that data is leaking.

The previous version of the OWASP API Top 10 contained a listing specifically for Mass Assignment attacks. While this listing has been merged into others in 2023, the attack is still a valid example of broken object property level authorization. Wallarm will detect and block Mass Assignment attacks that seek to leverage this vulnerability by editing properties that aren’t intended to be available to the authenticated user.

## Learn More

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

文章来源: https://lab.wallarm.com/api32023-broken-object-property-level-authorization/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)