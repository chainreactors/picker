---
title: Burp Suite Enterprise Edition spring update 2024
url: https://portswigger.net/blog/burp-suite-enterprise-edition-spring-update-2024
source: PortSwigger Blog
date: 2024-05-17
fetch_date: 2025-10-06T17:15:48.928331
---

# Burp Suite Enterprise Edition spring update 2024

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

# Burp Suite Enterprise Edition spring update 2024

[ ]

Amelia Coen |
16 May 2024 at 13:31 UTC

![Burp Suite roadmap July 2022](/cms/images/35/6f/0190-article-spring_update_image.jpg)

We understand the unique challenges AppSec teams face—from navigating the rapid pace of development to achieving comprehensive coverage against new vulnerabilities. That’s why we’ve focused our latest updates on not just improving the automated testing capabilities of [Burp Suite Enterprise Edition](/burp/enterprise), but also on simplifying and enhancing workflows for you and your teams.

Here's what we've recently released in Burp Suite Enterprise Edition...

#### At a glance:

* [Burp Suite Enterprise Edition in the Cloud](#cloud)
* [Custom scan checks](#bchecks)
* [CI-driven scans](#ci-scans)
* [Scanning performance improvements](#scanner-improvements)
* [ISO 27001 2022](#ISO)
* [Coming soon in 2024](#coming-soon)

## Burp Suite - now available in the Cloud

Burp Suite Enterprise Edition is now available in PortSwigger’s secure cloud.

Your team can now scale up your scanning efforts with automated, scheduled [DAST](/burp/application-security-testing/dast) scans, without the need to host and maintain your own infrastructure.

This new Cloud-based version enables you to:

1. Scan your applications like an actual attacker would.
2. Set up recurring, scheduled scans within minutes.
3. Share access and reports easily with all of your team.

[Read full details in our launch blog post.](https://portswigger.net/blog/introducing-dast-scanning-in-the-cloud-with-burp-suite-enterprise-edition)

> Being able to scan unlimited sites is very generous. I'm used to getting a maximum of 5 or 6 applications when we have tried other products. Unlimited is really nice!

A major UK-based university

#### Want a free trial of Burp Suite Enterprise Edition in the Cloud?

[Book a call with one of our Enterprise Experts](https://meetings.hubspot.com/jamie-mackay/spring-update-may-2024?uuid=cd194c7e-2648-4341-8e39-669b06913ff1), and we’ll get you set up with a free trial of the new Cloud version for you and your team.

## Custom scan checks

Building on the extensibility added to [Burp Suite Professional](/burp/pro), you can now import custom scan checks created in Burp Suite Professional into Burp Suite Enterprise Edition.

Custom scan checks - BChecks - enable you to extend [Burp Scanner](/burp/vulnerability-scanner) in a quick and simple way. Tailor scans to your own applications’ framework, and achieve targeted coverage for new and novel vulnerabilities.

> When we came across [BChecks], we were just like, hey, this is this little nugget of awesome power and we can immediately start to see how we can use something like this across a massive scale.

[Nicholas Anastasi, Sprocket Security](https://portswigger.net/blog/supporting-sprocket-securitys-offensive-security-testing-with-bchecks-from-burp-suite)

Take a look at our extensive  [GitHub repository](https://github.com/PortSwigger/BChecks) of community-created scan checks, which can also be imported into Burp Suite Enterprise Edition.

[Read more about custom scan checks here.](https://portswigger.net/burp/pro/features/bchecks)

## CI-driven scans

Preventing vulnerable apps from hitting production is one of the biggest AppSec challenges - we’re aiming to make this much easier with CI-driven scans.

It’s now quick and easy to integrate automated, scheduled DAST scans with any [CI/CD](/developers/ci-cd-security) platform. This enables you to get fast security feedback to your web developers - saving on time and costs, while keeping your web estate more secure.

You can choose to digest results in our centralized dashboard, or use our GraphQL API to import the results into your vulnerability management platform.

Learn more in our [documentation.](https://portswigger.net/burp/documentation/enterprise/user-guide/ci-cd/ci-driven-scans)

## Scanning performance improvements

There's also been improvements made to scanning performance recently, including:

* Reducing the number of browsers that Burp Scanner creates during the audit phase, making scans more memory efficient.
* Further improvements in memory usage for browser-powered scans.
* Improved Burp’s ability to identify - and disregard - duplicate items in different areas of applications during scans.

These improvements are all designed to make Burp Scanner faster, more efficient, and more accurate than ever before.

## ISO 27001 2022

We’re delighted to announce we have recently acquired a certification of compliance with ISO 27001 2022.

Compliance with these international standards is evidence of PortSwigger’s ongoing commitment to ensuring information security is at the forefront...