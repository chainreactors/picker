---
title: Find GraphQL API vulnerabilities, with Burp Suite Professional
url: https://portswigger.net/blog/find-graphql-api-vulnerabilities-with-burp-suite-professional
source: PortSwigger Blog
date: 2023-07-05
fetch_date: 2025-10-04T11:53:57.285359
---

# Find GraphQL API vulnerabilities, with Burp Suite Professional

[**Your agentic AI partner in Burp Suite - Discover Burp AI now**

**Read more**](https://portswigger.net/burp/ai)

[Login](/users)

[ ]

Products

Solutions

[Research](/research)
[Academy](/web-security)

Support

Company

[Customers](/customers)
[About](/about)
[Blog](/blog)
[Careers](/careers)
[Legal](/legal)
[Contact](/contact)
[Resellers](/support/reseller-faqs)

[My account](/users/youraccount)
[Customers](/customers)
[About](/about)
[Blog](/blog)
[Careers](/careers)
[Legal](/legal)
[Contact](/contact)
[Resellers](/support/reseller-faqs)

[![Burp Suite DAST](/content/images/svg/icons/enterprise.svg)
**Burp Suite DAST**
The enterprise-enabled dynamic web vulnerability scanner.](/burp/enterprise)
[![Burp Suite Professional](/content/images/svg/icons/professional.svg)
**Burp Suite Professional**
The world's #1 web penetration testing toolkit.](/burp/pro)
[![Burp Suite Community Edition](/content/images/svg/icons/community.svg)
**Burp Suite Community Edition**
The best manual tools to start web security testing.](/burp/communitydownload)
[View all product editions](/burp)

[**Burp Scanner**

Burp Suite's web vulnerability scanner

![Burp Suite's web vulnerability scanner'](/mega-nav/images/burp-suite-scanner.jpg)](/burp/vulnerability-scanner)

[**Attack surface visibility**
Improve security posture, prioritize manual testing, free up time.](/solutions/attack-surface-visibility)
[**CI-driven scanning**
More proactive security - find and fix vulnerabilities earlier.](/solutions/ci-driven-scanning)
[**Application security testing**
See how our software enables the world to secure the web.](/solutions)
[**DevSecOps**
Catch critical bugs; ship more secure software, more quickly.](/solutions/devsecops)
[**Penetration testing**
Accelerate penetration testing - find more bugs, more quickly.](/solutions/penetration-testing)
[**Automated scanning**
Scale dynamic scanning. Reduce risk. Save time/money.](/solutions/automated-security-testing)
[**Bug bounty hunting**
Level up your hacking and earn more bug bounties.](/solutions/bug-bounty-hunting)
[**Compliance**
Enhance security monitoring to comply with confidence.](/solutions/compliance)

[View all solutions](/solutions)

[**Product comparison**

What's the difference between Pro and Enterprise Edition?

![Burp Suite Professional vs Burp Suite Enterprise Edition](/mega-nav/images/burp-suite.jpg)](/burp/enterprise/resources/enterprise-edition-vs-professional)

[**Support Center**
Get help and advice from our experts on all things Burp.](/support)
[**Documentation**
Tutorials and guides for Burp Suite.](/burp/documentation)
[**Get Started - Professional**
Get started with Burp Suite Professional.](/burp/documentation/desktop/getting-started)
[**Get Started - Enterprise**
Get started with Burp Suite Enterprise Edition.](/burp/documentation/enterprise/getting-started)
[**User Forum**
Get your questions answered in the User Forum.](https://forum.portswigger.net/)
[**Downloads**
Download the latest version of Burp Suite.](/burp/releases)

[Visit the Support Center](/support)

[**Downloads**

Download the latest version of Burp Suite.

![The latest version of Burp Suite software for download](/mega-nav/images/latest-burp-suite-software-download.jpg)](/burp/releases)

# Find GraphQL API vulnerabilities, with Burp Suite Professional

[ ]

Gareth Heyes |
04 July 2023 at 13:00 UTC

[GraphQL](/blog/graphql)
[Burp Suite](/blog/burp-suite)
[scanning](/blog/scanning)

![Showing a radar with the GraphQL logo in the middle with submarines for each GraphQL detection type such as introspection](/cms/images/a3/0c/b5bf-article-graphql-article.png)

As a penetration tester, you need your tools to find the latest vulnerabilities. [GraphQL](/web-security/graphql) APIs are widely used on today’s websites, and expose attack surface for a wide range of security issues.

Burp Scanner’s new GraphQL checks will automatically report many instances of GraphQL vulnerabilities on your penetration tests. [Get the latest version of Burp Suite Professional](https://portswigger.net/burp/releases/professional-community-2023-6), and start finding these issues today.

## GraphQL scan checks

We added support for GraphQL in Burp Suite to enable you to detect known endpoints, find hidden endpoints, detect when introspection or suggestions are enabled, and report when an endpoint does not validate the content type.

### Finding known endpoints

It can be tedious to manually trawl through a web site to determine the GraphQL endpoint. We've made this easier by getting [Burp Scanner](/burp/vulnerability-scanner) to do the work for you. We've defined some passive and active scan checks to find known endpoints automatically, allowing you to focus on finding the vulnerabilities.

### Finding hidden endpoints

Sometimes a developer will deploy a GraphQL endpoint without using it on the site - for example, if it was accidentally deployed to production. Burp Suite will look for common endpoints and find hidden GraphQL deployments even without the site using it. These endpoints could be a valuable resource for a tester, as it's likely a vulnerability will be found if it's an accidental deployment.

### Detecting introspection

Introspection allows you to run a query on the actual schema to see what queries it supports. It's often turned off in production because a site might not want to expose the inner workings of its API to the world. Burp will detect if introspection is enabled - although this isn't a vulnerability in itself, it could be useful for a tester to aid testing the site and useful for a developer to remind them to turn it off in production.

### Detecting suggestions

Some GraphQL servers like Apollo will make suggestions when you make an invalid query, to help you construct a valid one. This can be used by a tester to discover the underlying schema by using a dictionary of words and the suggestion response as an oracle, even when introspection is disabled. A tool such as [clairvoyance](https://github.com/nikitastupin/clairvoyance) can be used to construct a valid schema from a dictionary. Burp will enable you to find endpoints that have suggestions enabled and report them.

### Invalidated content type

Most GraphQL endpoints use a POST method with an application/json content type. If the content type is validated correctly, then a browser can't make this request without using [CORS](/web-security/cors) as it will be unable to send the correct content type. This makes the endpoint secure against [CSRF](/web-security/csrf). However, if a site does not validate the content type and does not implement some form of CSRF token, it could be possible to abuse the GraphQL endpoint by forging requests provided mitigations like [SameSite](/web-security/csrf/bypassing-samesite-restrictions) cookies can be bypassed or neutralized because of the SameSite None flag. Burp will report if it's possible to forge the request to the endpoint using a GET request or application/x-www-form-urlencoded POST request.

## Try it out for yourself

If you want to learn more about GraphQL - including an overview of how it works, discovery and exploitation techniques, and how GraphQL vulnerabilities can lead to information disclosure and CSRF -  take a look at the Web Security Academy. We've prepared thorough [learning materials](https://portswigger.net/web-security/graphql/) and [interactive labs](https://portswigger.net/web-security/graphql/lab-graphql-reading-private-posts) where you can practise your skills - go check them out!

[GraphQL](/blog/graphql)
[Burp Suite](/blog/burp-suite)
[scanning](/blog/scanning)

[ ]

![Gareth Heyes](/cms/profiles/gareth-heyes.png)

This page requires JavaScript for an enhanced user experience.

Latest Posts

[### Hacking smarter with Burp AI: NahamSec puts Burp AI to the test

01 October 2025
Hacking smarter with Burp AI: NahamSec puts Burp AI to the test](/blog/hacking-smarter-with-burp-ai-nahamsec-puts-burp-ai-to-the-test)
[### Welcome...