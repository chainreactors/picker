---
title: Take control of your security posture: The Burp Suite Enterprise Edition winter update
url: https://portswigger.net/blog/take-control-of-your-security-posture-the-burp-suite-enterprise-edition-winter-update
source: PortSwigger Blog
date: 2024-10-31
fetch_date: 2025-10-06T18:53:10.910900
---

# Take control of your security posture: The Burp Suite Enterprise Edition winter update

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

# Take control of your security posture: The Burp Suite Enterprise Edition winter update

[ ]

Rob Samuels |
30 October 2024 at 09:12 UTC

![taking control of web apps vector image](/cms/images/0a/19/d0bd-article-blog-post-header.png)

## Manage your security, your way.

Managing a complex, enterprise-level web estate requires robust compliance, streamlined management of audits, and visibility of your security coverage.

In other words - effective web app and API security requires control.
However, meeting these needs becomes difficult when you can't easily identify and prioritise the vulnerabilities that matter most. Additionally, limited visibility of scanned URLs can leave you uncertain of your scan coverage, while restrictions to [API scanning](/burp/vulnerability-scanner/api-security-testing) make it even harder to manage security efficiently.

> Yes, tools surface plenty of vulnerabilities - but there's a lot of manual work that goes on in terms of prioritizing. What is critical for a tool might not be critical for us. We would like Enterprise to help us prioritize vulnerabilities based on our context. *Senior AppSec Manager at a FinTech company*

We’ve been working on a number of new features for [Burp Suite Enterprise Edition](/burp/enterprise) to alleviate these challenges, empowering you to:

* Take control of your priorities by **managing your own issue severity ratings**.
* Simplify auditing by **marking issues as accepted risks**.
* **Integrate Burp Suite Enterprise Edition with Splunk** for seamless security analytics and threat response.
* Gain **full visibility of URLs discovered by your scans**, with additional context for URLs that have not been included in the audit.
* Enhance your scan capability with **extensions for CI-driven scans**.
* Extend your security coverage with **support for SOAP APIs**.

These features are being launched across three updates - version 2024.9 (launched in September), version 2024.10 (launched at the end of October), and version 2024.11 (due for launch later in November).

**Interested in Burp Suite Enterprise Edition for your organization?  [Click here to request your free, fully-featured trial](https://portswigger.net/burp/enterprise/trial).**

## Available now in Burp Suite Enterprise Edition

### Take control of your priorities by managing your own issue severity ratings

In  [Burp Suite Enterprise Edition version 2024.9](https://portswigger.net/burp/releases/enterprise-edition-2024-9?requestededition=enterprise) we introduced two important issue management options to help enhance your audit prioritization.

Firstly, severity ratings have been pre-defined in Burp Suite Enterprise Edition previously, making it harder to prioritise vulnerabilities based on your unique environment and security management framework.

Editable issue severity has been a highly-requested feature in Burp Suite Enterprise Edition - and you can now increase or decrease the severity rating of issues identified during a scan. You can also leave notes on the issue record to add further context and keep track of why decisions have been made.

This feature will help you manage vulnerabilities more efficiently and ensure your team remains focused on what matters most. See it below:

![Issue management menu](/cms/images/2e/cc/9597-article-issue_management_menu.png)

### Simplify auditing - mark issues as accepted risks

Secondly, in addition to editing issue severity, you can also mark an issue as an accepted risk. This feature allows greater control of vulnerability management for issues that don’t require further action, or where you may have other mitigating security measures in place:

You can also leave notes in the same way as editing issue severity - ensuring you have a clear record log for auditing purposes. See how it works below:

![Mark issues as an accepted risk](/cms/images/5b/e0/a12f-article-mark_as_accepted_risk.png)

These two issue severity improvements supplement the existing false positive option to provide greater customisation of your issue management, helping simplify your processes.

### Integrate Burp Suite Enterprise Edition with Splunk for seamless security analytics and threat response

Splunk is a vulnerability management platform used by many enterprises to manage their Security Information and Event Management (SIEM).

[Burp Suite Enterprise Edition 2024.10](https://portswigger.net/burp/releases/enterprise-edition-2024-10?requestededition=enterprise) offers a native integration, which streams issues directly into Splunk for advanced analysis. This streamlines security operations using real-time data instead of relying on manually exporting and importing data between platforms.

### Gain full visibility...