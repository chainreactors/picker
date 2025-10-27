---
title: Unlock enhanced API scanning with Burp Suite
url: https://portswigger.net/blog/unlock-enhanced-api-scanning-with-burp-suite
source: PortSwigger Blog
date: 2024-08-01
fetch_date: 2025-10-06T18:04:25.494226
---

# Unlock enhanced API scanning with Burp Suite

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

# Unlock enhanced API scanning with Burp Suite

[ ]

Rob Samuels |
31 July 2024 at 12:17 UTC

![](/cms/images/e6/35/fd8e-article-api_article.png)

## More comprehensive scans. More vulnerabilities identified. More time saved. Enhance your API scanning with Burp Suite.

As web portfolios have diversified, APIs have become an increasingly critical function of modern web applications. According to ESG’s [Securing the API Attack Surface report](https://research.esg-global.com/reportaction/515201654/Marketing), the vast majority of organizations report they now have an average of **26 APIs per application**.

Despite this, scanning APIs for vulnerabilities is often challenging, with many organizations reliant on workarounds. At best this solution is fiddly and time-consuming, and, at worst, leaves your application open to attacks, and affects your ability to scale testing.

> APIs are the biggest gap in our testing at the moment. We’ve done a small amount of scanning, but having a Burp API scan would be amazing. *A [Burp Suite Enterprise Edition](/burp/enterprise) customer*

We’ve been working to remedy this challenge by enhancing our existing [API scanning](/burp/vulnerability-scanner/api-security-testing) capability with enhanced built-in functionality designed for easy, scalable API scanning.

Our improved API scanning functionality allows users to:

* [Test for vulnerabilities without having to host definition files](#host-definition)
* [Easily identify any hosted APIs that have been left accessible to attackers](#hosted-apis)
* [Test a wider range of OpenAPI Specification (OAS) endpoints](#open-api)
* [Scan APIs that require endpoint authentication](#endpoint)

These features are now available for both Burp Suite Enterprise Edition and [Burp Suite Professional](/burp/pro) users.

## How were APIs scanned in Burp previously?

Users of Burp Suite have been able to [scan APIs for some time](https://portswigger.net/burp/documentation/scanner/api-scanning-reqs). However, up to now, API endpoints have been scanned as part of a wider web application crawl & audit.

This approach, however, raises a few challenges.

Firstly, **for pentesters**, this approach means you can’t target APIs specifically in your scans. As your portfolio of APIs increases, this task has gone from a quality-of-life issue to a major obstacle for effective workflows.

For **AppSec teams**, scanning APIs as part of your wider web apps means you have to run a more thorough and time-consuming scan, reducing the ability to scale operations.

> As we look at modernizing web applications and moving towards everything as an API, all of the data is accessible behind that API. We're trying to step up our game in terms of proactive discovery of API-level vulnerabilities. *A Burp Suite Enterprise Edition customer*

Scanning APIs exclusively in this way is no longer fit for purpose. We needed a built-in solution to API scanning.

## Meet our improved API scanning features

We’ve released 4 API scanning features, allowing Burp users to scan their APIs alongside their web apps, and as a standalone too. These can be accessed in both Burp Suite Professional and Burp Suite Enterprise Edition:

### 1. Test for vulnerabilities without having to host definition files

You can now upload OAS definition files directly to Burp Suite. This update enables users to choose whether they want to provide an existing URL, or upload a file directly to Burp. That means quicker, hassle-free scanning, which can be easily scaled.

Read more about testing for vulnerabilities in [Burp Suite Enterprise Edition](https://portswigger.net/burp/documentation/enterprise/user-guide/working-with-sites/add-new-sites/add-new-apis).

Read more about testing for vulnerabilities in [Burp Suite Professional](https://portswigger.net/burp/documentation/desktop/automated-scanning/api-scans).

### 2. Easily identify any hosted APIs that have been left accessible to attackers

Burp now checks whether you have left any hosted OAS definitions that may be accessed by attackers. This helps flag any potential security threats - particularly while you transition away from having to scan APIs via hosting them yourself.

### 3. Test a wider range of OpenAPI Specification (OAS) endpoints

When crawling your APIs, you can now include HTTP headers, allowing you to scan a much wider range of OAS endpoints. More comprehensive scans. More vulnerabilities identified.

Read more about testing [OAS endpoints](https://portswigger.net/burp/documentation/scanner/api-scanning-reqs#:~:text=as%20absolute%20URLs.-,API%20endpoint%20requirements,-Burp%20Scanner%20can).

### 4. Scan APIs that require endpoint authentication

Finally, for Burp Suite Enterprise Edition ...