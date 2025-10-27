---
title: Burp Suite roadmap update: January 2023
url: https://portswigger.net/blog/burp-suite-roadmap-update-january-2023
source: PortSwigger Blog
date: 2023-01-28
fetch_date: 2025-10-04T05:04:07.166376
---

# Burp Suite roadmap update: January 2023

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

# Burp Suite roadmap update: January 2023

[ ]

Matt Atkinson |
27 January 2023 at 14:48 UTC

[Burp Suite](/blog/burp-suite)

![Burp Suite roadmap 2023](/cms/images/fb/00/9f33-article-2023-road-map-article.png)

**The roadmap shown here is out of date.** Please see our [July 2023 roadmap update](https://portswigger.net/blog/burp-suite-roadmap-update-july-2023).

Believe it or not, it's January once again. And this can mean only one thing - it's time to update you on the changes we've got in store for [Burp Suite](https://portswigger.net/burp) over the next six months.

But this edition of the Burp roadmap also comes with a slight caveat - because this year we can neither confirm nor deny that we may also have a few surprises up our collective sleeves. [Watch this space](https://twitter.com/PortSwigger) to stay in the know.

## Burp Scanner

[Burp Scanner](https://portswigger.net/burp/vulnerability-scanner) is used in Burp Suite Enterprise Edition, Burp Suite Professional, and now (to a slightly more limited extent) in our free CI/CD product,  [Dastardly](https://portswigger.net/burp/dastardly). It enables tens of thousands of users to scan the modern web both efficiently and effectively.

But PortSwigger isn't exactly known for resting on its laurels, and the first half of 2023 is looking good for [Burp Scanner](/burp/vulnerability-scanner) users in terms of releases. Over the next six months, you'll see Burp Scanner gain yet more automated capability - and an exciting new way to customize your scans.

Done **Support for popups in recorded login sequences** - The 2022.12.4 release added support for recorded login sequences that open new windows or tabs. This enables you to run [authenticated scans](https://portswigger.net/burp/vulnerability-scanner/authenticated-scanning) on websites with login mechanisms that require you to interact with popups, such as Microsoft and Amazon's SSO services.

Done **Revamped browser powered scanning** - The 2022.12.4 release fundamentally changed the way that [Burp Scanner navigates using its built-in browser](https://portswigger.net/blog/browser-powered-scanning-2-0). This improves scanning of applications that make heavy use of client-side JavaScript for navigation, and lays a strong foundation for further development of the scanner.

WIP **Declarative scan checks** - Work is progressing on a new framework to add scan checks to Burp Scanner using a simplified language we've created specifically for this purpose. This will enable you to create custom scan checks more easily (without writing a BApp extension).

WIP **React form handling** - Work is progressing on improving the way Burp Scanner handles forms when scanning single page applications (SPAs) built on React. Specifically, this will improve Burp Scanner's handling of input elements that do not have an enclosing form tag.

Added **Improved scanning of JavaScript frameworks** - Further to the improvements we have already made to Burp Scanner's coverage of applications built using the React library, we will continue to develop our capabilities in this area, and include apps built using Angular, Vue.js, and other frameworks.

Added **Seed scan from uploaded API definition** - We will give Burp Scanner the ability to ingest an API definition as part of its launch process. It will use this API definition to seed its scan - enhancing Burp Suite's ability to [scan APIs and microservices](https://portswigger.net/burp/vulnerability-scanner/api-security-testing).

Added **[GraphQL](/web-security/graphql) scan checks** - We will give Burp Scanner the ability to check for a number of security vulnerabilities relating to APIs using the GraphQL language.

Added **[Access control](/web-security/access-control) scan checks** - We will give Burp Scanner the ability to check for a number of security vulnerabilities relating to [access control](https://portswigger.net/web-security/access-control).

Note that [Burp Suite Enterprise Edition](/burp/enterprise) and [Burp Suite Professional](/burp/pro) both contain Burp Scanner and will benefit from its roadmap.

## Burp Suite Enterprise Edition

As I write, [Burp Suite Enterprise Edition](https://portswigger.net/burp/enterprise) is now sitting at well over 1,000 subscribers. But as well as users, 2022 saw Enterprise Edition gain some powerful new features - like the ability to replay recorded login sequences. And with the plans outlined in this roadmap, 2023 is shaping up to be another cracker.

This year, you'll see some efficient new ways to scale scanning across your whole web portfolio. And further improvements to Burp Suite Enterprise Edition's already [class-leading scanning engine](#burp-scanner) will take its ability to sca...