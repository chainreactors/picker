---
title: Meet Burp Suite DAST: Your questions answered
url: https://portswigger.net/blog/meet-burp-suite-dast-your-questions-answered
source: PortSwigger Blog
date: 2025-05-30
fetch_date: 2025-10-06T22:26:35.740047
---

# Meet Burp Suite DAST: Your questions answered

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

# Meet Burp Suite DAST: Your questions answered

[ ]

Andrzej Matykiewicz |
29 May 2025 at 09:29 UTC

![Meet Burp Suite DAST](/cms/images/10/5d/3492-article-burp_suite_dast_gif.gif)We recently hosted a webinar to introduce [Burp Suite DAST](/burp/dast), the new name for [Burp Suite Enterprise Edition](/burp/enterprise), the best-in-class, automated web application and API security scanning solution for modern AppSec teams at any scale.

We were thrilled to see the high level of engagement and insightful questions from the thousands of attendees from across the AppSec industry. In this post, we'll answer some of the most frequently asked questions from the webinar.

* [Why have you changed the name to Burp Suite DAST?](#why-have-you-changed-the-name-to-burp-suite-dast)
* [How does Burp Suite DAST complement Burp Suite Professional?](#how-does-burp-suite-dast-complement-burp-suite-professional)
* [How does Burp Suite DAST perform with larger web estates comprising hundreds of apps?](#how-does-burp-suite-dast-perform-with-larger-web-estates-comprising-hundreds-of-apps)
* [Can it also scan my APIs?](#can-burp-suite-dast-scan-my-apis)
* [How does Burp Suite DAST integrate with the other tools in my AppSec workflow?](#how-does-burp-suite-dast-integrate-with-the-other-tools-in-my-appsec-workflow)
* [Can I use Burp Suite DAST to run vulnerability scans from my CI/CD pipeline?](#can-i-use-burp-suite-dast-to-run-vulnerability-scans-from-my-ci-cd-pipeline)
* [Does Burp Suite DAST come with additional capabilities?](#does-burp-suite-dast-come-with-additional-capabilities)
* [What's on the roadmap for Burp Suite DAST?](#what-s-on-the-roadmap-for-burp-suite-dast)
* [What onboarding and support are available?](#what-onboarding-and-support-are-available)
* [Can I use my existing extensions from Burp Suite Professional in Burp Suite DAST?](#can-i-use-my-existing-extensions-from-burp-suite-professional-in-burp-suite-dast)
* [What next?](#what-next)
* [Watch the full webinar](#watch-the-full-webinar)
* [Honorable mention](#honorable-mention)

## Why have you changed the name to Burp Suite DAST?

The transition from "Burp Suite Enterprise Edition" to "Burp Suite DAST" was driven by the need for clarity and precision in conveying the product's purpose. The previous name often led to confusion, with some assuming it was merely a multi-user version of [Burp Suite Professional](/burp/pro). As a result, some organizations were unaware that we offered a distinct, but complementary DAST solution to sit alongside Burp Suite Professional and they've been needlessly putting up with subpar DAST scanners for years.

By adopting the name "Burp Suite DAST", we aim to alleviate this confusion and more clearly articulate the product's core value: a scalable, automated solution for [dynamic application security testing](/burp/application-security-testing/dast) that integrates seamlessly with the tools your team are already using, including Burp Suite Professional. This change ensures that potential users immediately recognize the product's role in their security stack, especially when evaluating DAST solutions to enhance their broader security strategies or integrate automated security testing into their [CI/CD](/developers/ci-cd-security) pipelines.

Burp Suite DAST continues to be powered by the same industry-leading scanning engine trusted by over 17,000 organizations, including SAP, Microsoft, and Mastercard, and we have ambitious plans to further optimize our solution for organizations at any scale.

## How does Burp Suite DAST complement Burp Suite Professional?

Burp Suite DAST and Burp Suite Professional are built to work together. Burp Suite DAST handles automated, scheduled scanning at scale, helping teams identify potential vulnerabilities across their web estate. Security teams can then use Burp Suite Professional to dive deeper, validating issues, eliminating false positives, and crafting detailed remediation advice. This workflow ensures efficient use of time and resources.

No other DAST vendor offers a complementary manual testing toolkit, and your manual testers are almost certainly using Burp Suite Professional already. So if you're not familiar with Burp Suite DAST, now is the perfect time to see how you can level up your AppSec by bridging the gap between automation and manual testing.

## How does Burp Suite DAST perform with larger web estates comprising hundreds of apps?

For organizations with large web estates, Burp Suite DAST scales seamlessly to scan thousands of applications. Supporting large web estates has been a key focus over the last six months, with a number of improvements introduced explicitly targeting enhanced performance for customers scanning hun...