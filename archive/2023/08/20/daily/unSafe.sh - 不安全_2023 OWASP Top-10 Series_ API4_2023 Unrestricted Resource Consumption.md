---
title: 2023 OWASP Top-10 Series: API4:2023 Unrestricted Resource Consumption
url: https://buaq.net/go-174832.html
source: unSafe.sh - 不安全
date: 2023-08-20
fetch_date: 2025-10-04T11:58:44.299575
---

# 2023 OWASP Top-10 Series: API4:2023 Unrestricted Resource Consumption

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

2023 OWASP Top-10 Series: API4:2023 Unrestricted Resource Consumption

Welcome to the 5th post in our weekly series on the new 2023 OWASP API Security Top-10 list,
*2023-8-19 21:45:0
Author: [lab.wallarm.com(查看原文)](/jump-174832.htm)
阅读量:38
收藏*

---

Welcome to the 5th post in our weekly series on the new [2023 OWASP API Security Top-10](https://owasp.org/API-Security/editions/2023/en/0x00-header/) list, with a particular focus on security practitioners. This post will focus on [API4:2023 Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/).

In this series we are taking an in-depth look at each category – the details, the impact and what you can do about it. To see previous posts you might have missed, [click here](https://lab.wallarm.com/category/owasp/).

## TL;DR

Delivering an API requires computing resources, but they’re not infinite. Any time an API’s resources can be consumed beyond desired limits or to exhaustion of those resources, that API is vulnerable to Unrestricted Resource Consumption.

## The Details

An API endpoint is a gateway to resources, including compute, storage, memory, and more. When an application interacts with an API, resources are inevitably consumed. And that’s good! APIs are meant to deliver a service, and to consume resources in doing so. Resource consumption becomes a problem when it either exceeds the available resources or is entirely unrestricted. It might help to think about unrestricted resource consumption in terms of “too many, too much, too fast.”

### **Too Many**

Any resource that’s counted in increments may be subject to the problem of ‘too many.’ For example, a datastore that can only handle a certain number of concurrent connections. If an attacker can execute enough requests to an API to exceed the number of supportable concurrent connections, then the service will be impacted. This is a ‘too many’ resource consumption problem.

### **Too Much**

Any resource that’s measured in terms of volume or size may be subject to the problem of ‘too much.’ Our poor datastore can be the example here as well. An obvious problem might be that the datastore simply runs out of space, but a more subtle example is probably more realistic in today’s world. A field in that datastore may be restricted in size, but the API endpoint inserting data may not have the same restriction, resulting in an attacker sending too much data into that field.

### **Too Fast**

It might not be the amount or size of API requests that cause a problem, but the volume in a given time period. You might be thinking that there’s overlap here with the ‘too many’ problem, and you’re right. It can be hard to distinguish between ‘too many’ and ‘too fast’ in some cases. The key is the emphasis on *in a given time period.*

As an example, let’s talk about a password reset function. There’s no limit on the number of times you can reset your password, but the developers didn’t expect anyone to do so 100,000 times in an hour. Password history is kept, but once a day any passwords older than 30 days are dropped. In this scenario, an attacker could fill that password history storage by sending password reset requests too fast.

## What’s the Impact?

Generally, the impact of a resource consumption attack is going to be some kind of denial of service. The form that DoS takes and the actual impact to the business will depend on the specific resource being consumed. For example, if the resource exhausted is a login service, the impact might be that users can’t login, but that users who are already authenticated can continue using the service.

There is an example where the impact isn’t a denial of service, and that’s the consumption of financial resources. Let’s say that a company offers a free tier of service, and that each account created uses some amount of storage, for which the company is paying on a consumption basis. An attack might create tens or hundreds of thousands of accounts, consuming storage space, and costing the company money. There’s no technical denial of service here, but there is a financial impact as the resource (storage) is consumed.

## What Can You Do About It?

It may seem obvious, but in order to prevent unrestricted resource consumption from occurring, you have to restrict the resources that can be consumed. That’s often easier said than done.

The ideal way to accomplish this objective is through the development of the app behind the API itself, but it’s not always possible to do so. It might be difficult organizationally to get such changes implemented or it might not be an application over which you have direct control.

As a security practitioner, you can develop a threat model for resource consumption by identifying which resources a particular application uses. You can then look at security controls external to the application that can impose relevant limits.

For example, you may be able to impose external limits on the size of data in an API request, or rate limit certain types of requests. You might also be able to change how datastores are automatically scaled to handle increased load, or limit automatic scaling where appropriate. By understanding the resource consumption threat model for an application, you can make risk mitigation decisions, even without direct control of the application code.

## How Wallarm Can Help

The Wallarm platform can address unrestricted resource consumption issues by detecting and blocking some specific attack types. For example, Wallarm will detect and block [Brute Force](https://docs.wallarm.com/attacks-vulns-list/#brute-force-attack) attacks, which may cause login APIs to consume resources. Wallarm will detect and block [Data Bomb](https://docs.wallarm.com/attacks-vulns-list/#data-bomb) attacks, in which a zip or XML file is crafted to consume resources. Wallarm will also detect and block [API Abuse](https://docs.wallarm.com/about-wallarm/api-abuse-prevention/), using machine learning and other techniques to identify malicious bot traffic that might consume resources.

While detecting and blocking these specific attacks is important, Wallarm can also be customized and tuned to do more to protect against unrestricted resource consumption. Users can create rules to apply advanced [rate limiting](https://docs.wallarm.com/user-guides/rules/rate-limiting/) to API traffic. The rate limiting configuration is flexible enough to be used in specific circumstances where resource exhaustion may be a risk.

## Learn More

Come back next week as we dig into the details of another category of the new 2023 OWASP Top-10 API Security Risks list – or [click here](https://lab.wallarm.com/category/owasp/) to see previous posts you might have missed.

In the meantime, here are some other resources which might help on your journey to end-to-end API security:

* Solution Brief: [OWASP API Security Top-10 2023 Reference Guide](https://hubspot.wallarm.com/hubfs/OWASP%20APIsec%20Top-10%202023%20Reference%20Guide.pdf) (PDF)
* Blog Post: [OWASP API Security Top-10 Risks for 2023 Released](https://lab.wallarm.com/owasp-api-security-top-10-risks-for-2023-released/)
* Blog Post: [OWASP API Security Top-10 for 2023 Risk Ratings](https://lab.wallarm.com/owasp-api-security-top-10-for-2023-risk-ratings/)
* On-Demand Webinar: [A Practitioner’s Guide to the New 2023 OWASP API Security Update](https://www.wallarm.com/webinars/practitioners-guide-2023-owasp-api-security)
* On-Demand Webinar: [A CISOs Guide to the New 2023 OWASP API Security...