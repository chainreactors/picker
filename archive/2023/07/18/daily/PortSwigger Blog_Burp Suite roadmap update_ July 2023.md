---
title: Burp Suite roadmap update: July 2023
url: https://portswigger.net/blog/burp-suite-roadmap-update-july-2023
source: PortSwigger Blog
date: 2023-07-18
fetch_date: 2025-10-04T11:54:57.489895
---

# Burp Suite roadmap update: July 2023

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

# Burp Suite roadmap update: July 2023

[ ]

Matt Atkinson |
17 July 2023 at 14:26 UTC

[Burp Suite](/blog/burp-suite)

![Burp Suite July 2023 roadmap update](/cms/images/85/0c/509d-article-2023-road-map-article-update.png)

Check out our roadmap for [Burp Suite](https://portswigger.net/burp) and find out what exciting features are coming your way over the next 12 months.

## Burp Suite Professional

### Added to the roadmap

Added **BChecks - testing tool** - When creating custom [BChecks](https://portswigger.net/blog/bchecks-houston-we-have-a-solution) for [Burp Scanner](/burp/vulnerability-scanner), it's vital to test them thoroughly, to gain confidence that they're working correctly. We're going to make it just as easy to test your BChecks as it was to write them, by introducing a BCheck testing tool. You'll be able to send suitable requests to the tool, and use them as test cases to confirm that your BCheck is working.

Added **Code your own view filters** - Sometimes, Burp's built-in options for filters like the Proxy HTTP history filter don't do exactly what you need. You're limited by the checkboxes provided and the ways the settings are combined. We're going to give you a brand new way to customize Burp Suite using your own code, directly from the UI. You'll be able to quickly and easily create a view filter that does exactly what you need, showing just the items you are interested in.

Added **Burp Scanner auto configuration** - Currently, you have to manually configure Burp Scanner to ensure good performance when scanning certain types of web application. Failure to do this could mean missed attack surface. We will give Burp Scanner the ability to configure itself based on the type of web application you are scanning. This will improve crawl coverage, without the need for any manual configuration.

Added **Notes everywhere** - If you've used comments in Burp's tables to record information about HTTP messages, then you'll know that they can be a bit cramped and difficult to use. We're going to introduce a much-improved Notes feature - enabling you to write free-form multi-line notes, to capture everything you know about an HTTP message.

Added **Enhanced tables** - If you've ever used Burp Suite in anger, you'll know that it makes heavy use of tables to display key data. But these can be somewhat inflexible, with little scope for customization. We're going to change tables in Burp so that they work more consistently - and enhance them to give you more control. You'll be able to show and hide different columns, move them around, and you'll gain new capabilities for search and export.

Added **Service worker networking** - Burp Scanner's crawler doesn't properly support service workers and [WebSockets](/web-security/websockets) messages that occur during scans. This can cause some applications to function incorrectly - potentially leading to incomplete scan coverage. We will give Burp Scanner the ability to properly crawl service workers and WebSockets messages - eliminating this problem.

Added **[API scanning](/burp/vulnerability-scanner/api-security-testing) improvements** - Although Burp Scanner can understand many features of an OpenAPI definition and scan them appropriately, coverage isn't always as good as it could be. This is because scanning currently doesn't support some popular API features. We will add these features to Burp Scanner - enabling greatly improved coverage of web APIs.

Added **Browser performance enhancements** - Burp Scanner uses embedded browsers to navigate web sites effectively while scanning. But using a pool of browsers can consume significant system resources, which impairs performance. We will change Burp Scanner so that it uses fewer browser instances, each containing multiple isolated tabs, to enable parallel navigation. This will make scanning more efficient.

### Work in progress

WIP **Improved Burp Scanner interface** - It's not always easy to see the actions that Burp Scanner has carried out during a scan - or the attack surface it's discovered. [Burp Suite Professional](/burp/pro) 2023.5.2 brought you a new [crawl paths view](https://www.youtube.com/watch?v=Z8YWwWEyOmg&list=PLoX0sUafNGbGlLmZItn6zG2wRo5JOouiB&index=8) - which goes some way to addressing this problem. But more improvements to Burp Scanner's interface are currently in development, and in coming releases, you'll see some exciting new ways to visualize scan activity.

WIP **Customizable user interface** - Burp is a complex beast - and most testers have their own idiosyncratic way of working with it. This means that a fixed user interface will never be optimized for everyone. Especially once you start extending Burp Suite with BApps, you m...