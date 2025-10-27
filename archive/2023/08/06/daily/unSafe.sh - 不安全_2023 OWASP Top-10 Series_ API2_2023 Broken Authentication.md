---
title: 2023 OWASP Top-10 Series: API2:2023 Broken Authentication
url: https://buaq.net/go-173761.html
source: unSafe.sh - 不安全
date: 2023-08-06
fetch_date: 2025-10-04T11:58:59.318363
---

# 2023 OWASP Top-10 Series: API2:2023 Broken Authentication

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

2023 OWASP Top-10 Series: API2:2023 Broken Authentication

Welcome to the 3rd post in our weekly series on the new 2023 OWASP API Security Top-10 list,
*2023-8-5 21:45:0
Author: [lab.wallarm.com(查看原文)](/jump-173761.htm)
阅读量:42
收藏*

---

Welcome to the 3rd post in our weekly series on the new [2023 OWASP API Security Top-10](https://owasp.org/API-Security/editions/2023/en/0x00-header/) list, with a particular focus on security practitioners. This post will focus on [API2:2023 Broken Authentication](https://owasp.org/API-Security/editions/2023/en/0xa2-broken-authentication/).

In this series we are taking an in-depth look at each category – the details, the impact and what you can do about it. To see previous posts you might have missed, [click here](https://lab.wallarm.com/category/owasp/).

## TL;DR

Broken Authentication is a class of vulnerabilities that includes everything from weak passwords to failing to properly re-authenticate users changing sensitive parameters. There isn’t a single issue here, but rather a collection of related vulnerabilities.

## The Details

Obviously authentication is a critical security function for any application, and APIs are no exception. APIs, however, provide some new potential vectors for attack. It’s best to think of Broken Authentication as more of a class of vulnerabilities that can impact APIs. We could attempt to enumerate all the ways in which authentication can be broken, but the list would never be complete. Let’s consider a handful of examples in order to illustrate the basic idea.

**Weak Passwords** seem like an obvious example. An API that allows users to configure weak passwords is subject to more than one type of attack. Weak passwords are more likely to be common passwords, and therefore guessable. Variations of the word “password” or the name of a company are examples of common passwords. Weak passwords are also more easily cracked using automated tools.

Failing to **Limit Authentication Attempts** can make APIs vulnerable to credential stuffing and brute force attacks. Credential stuffing is the act of trying to authenticate with lots of different credentials, usually from another security incident, in the hopes that some of them work. It’s similar to, but different from brute forcing, which is attempting to authenticate by trying different passwords. When an API doesn’t limit the number of authentication attempts from a single IP address or for a single login, it can be vulnerable to these attacks.

Failure to **Validate Authentication Tokens** is another way in which authentication might be broken, and one that is especially applicable to APIs. With APIs, authentication state is often passed from one application to another. A good example of this is when you ‘login with Google’ or similar mechanisms. In these cases, one service passes a token to the other that says “I authenticated this user already and here’s the information you need to accept that authentication.” An API that doesn’t adequately validate the token or its attributes can be potentially abused. For example, failing to adhere to the authentication expiration timestamp or allowing weakly signed tokens to be passed can result in attackers gaining access.

Those are a few examples of broken authentication, but you might also consider:

* Embedding sensitive information in the URL such as tokens or passwords
* Failing to re-authenticate users when they change sensitive data such as email address or password.
* Using weak or poorly implemented encryption
* Missing or broken authentication

## What’s the Impact?

Ultimately, the impact of broken authentication is that an unauthorized user can gain access to the data and capabilities of the application. That may allow them to take over an account or to simply transfer funds out of an account. An API’s authentication mechanism is the first line of defense for ensuring that only authorized users can access the application. As such, you can think of broken authentication as leaving the proverbial gate open for attackers.

## What Can You Do About It?

The first step that security teams should take to address broken authentication is to put in place a detective control that can catch and block relevant attacks. In order to do this effectively, the control has to cover all the ingress points from which an attack might be seen.

The second step that security practitioners can take is to identify where APIs are vulnerable to broken authentication. Assessing your APIs for broken authentication vulnerabilities on a regular basis, both pre-production and in production, will give you a picture of how big the problem is for your organization. Identify those that present the highest risk and make a plan to address them. There are two paths for addressing the vulnerabilities once discovered.

If you control the application directly, then you’re in the position to have developers fix the vulnerabilities discovered. That may sound easy, but it’s definitely a process. A good place to start is with development management’s buy-in on the importance of addressing vulnerabilities.

If you don’t control the application, i.e. it’s a third-party application, then you’ll be relying on your detective control to block attacks while you work with the vendor to get the vulnerabilities fixed. Start by validating that you’re on the most current version of the application or service, then reach out to the vendor to report the vulnerabilities. Make sure you’re armed with evidence and priorities to help them move forward. Handing a vendor an unprioritized list of vulnerability names isn’t going to be effective.

## How Wallarm Can Help

Wallarm’s [API Security Platform](https://www.wallarm.com/product/advanced-api-security) detects and blocks attacks that leverage broken authentication in APIs. Wallarm nodes analyze traffic and identify a variety of attacks that leverage broken authentication, such as weak JSON Web Tokens (JWT), brute force attacks on authentication endpoints, and using weak encryption. These attacks can be blocked, monitored, or users can configure custom triggers to take a specific action. Users can also leverage Wallarm’s [API Leak detection](https://www.wallarm.com/api-leak-management-early-release) to identify credentials and authentication tokens embedded in URLs.

Identifying and blocking attacks is an effective detective control, but the best way to mitigate broken authentication attacks is to find and fix the corresponding vulnerabilities. Wallarm’s platform also includes vulnerability assessment and security testing, giving security teams the tools to extend their detective controls into proactive risk reduction as well.

## Learn More

Come back next week as we dig into the details of another category of the new 2023 OWASP Top-10 API Security Risks list – or [click here](https://lab.wallarm.com/category/owasp/) to see previous posts you might have missed.

In the meantime, here are some other resources which might help on your journey to end-to-end API security:

* Solution Brief: [OWASP API Security Top-10 2023 Reference Guide](https://hubspot.wallarm.com/hubfs/OWASP%20APIsec%20Top-10%202023%20Reference%20Guide.pdf) (PDF)
* Blog Post: [OWASP API Security Top-10 Risks for 2023 Released](https://lab.wallarm.com/owasp-api-security-top-10-risks-for-2023-released/)
* Blog Post: [OWASP API Security Top-10 for 2023 Risk Ratings](https://lab.wallarm.com/owasp-api-security-top-10-for-2023-risk-ratings/)
* On-Demand Webinar: [A Practitioner’s Guide to the New 2023 OWASP API Security...