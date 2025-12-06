---
title: How to detect React2Shell with Burp Suite
url: https://portswigger.net/blog/how-to-detect-react2shell-with-burp-suite
source: PortSwigger Blog
date: 2025-12-05
fetch_date: 2025-12-06T03:10:17.965625
---

# How to detect React2Shell with Burp Suite

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

# How to detect React2Shell with Burp Suite

[ ]

Tom Ryder |
05 December 2025 at 13:53 UTC

## Detecting React2Shell with Burp Suite

React2Shell vulnerabilities in [Next.js](http://Next.js) applications are now scannable across Burp Suite, making it fast to validate your exposure and begin automated coverage using:

* [Burp Suite Professional](/burp/pro) – for manual investigation and validation
* [Burp Suite DAST](/burp/dast) – for continuous, automated coverage across many apps

Both editions of Burp Suite now have access to the latest React2Shell detection logic for Next.js with ActiveScan++ (v2.0.8). Burp Suite Professional also enables targeted custom scan checks for deeper investigation.

## How to test for React2Shell in Burp Suite Professional

### Manual testing, instant visibility

Burp Suite Professional lets you quickly investigate React2Shell behaviour and validate specific endpoints during hands-on testing. You have two main detection options:

1. **ActiveScan++ (v2.0.8) – recommended**

   Ensure you have the latest version of [ActiveScan++](https://portswigger.net/bappstore/3123d5b5f25c4128894d97ea1acc4976), which includes a dedicated React2Shell check, giving you automated detection directly inside Burp Suite Professional. Once installed, it:

   * Adds React2Shell coverage into your existing manual workflow
   * Runs automatically as part of your active scanning
   * Is ideal for quick investigation and triage of suspected Next.js (React server components) targets

   Note: Current automated checks focus on Next.js applications. Other React frameworks may still require manual investigation and bespoke testing.
2. **Custom scan check (Bambda) for targeted checks**

   If you need more focused, on-demand testing, you can import the community-created [React2Shell Bambda](https://github.com/PortSwigger/bambdas/blob/main/CustomScanChecks/CVE-2025-55182CVE-2025-66478-React2Shell.bambda) and run it against specific endpoints or applications.

   This is ideal for quickly validating a suspected vulnerable app or probing specific components to reproduce reported behaviour.

   How to import and run the custom scan check:

   * Download the [Bambda](https://github.com/PortSwigger/bambdas/blob/main/CustomScanChecks/CVE-2025-55182CVE-2025-66478-React2Shell.bambda)
   * In Burp Suite Professional, go to Extensions > Bambda library.
   * Click Import. The Import scripts dialog opens.
   * Select .bambda files or a folder containing .bambda files.
   * Click Open.

## How to scan for React2Shell in Burp Suite DAST

If you need to understand React2Shell exposure across many applications or environments, Burp Suite DAST gives you continuous, automated detection at scale.

### ActiveScan++ (v2.0.8) in Burp Suite DAST

Burp Suite DAST supports the updated [ActiveScan++ extension](https://portswigger.net/bappstore/3123d5b5f25c4128894d97ea1acc4976). Once installed, ActiveScan++ enables automated React2Shell coverage across your Next.js estate, with scans running on a schedule or through your [CI/CD](/developers/ci-cd-security) pipelines, and results delivered centrally to your AppSec team.

### How to enable ActiveScan++ in Burp Suite DAST

* Download the ActiveScan++ BApp here:
  [ActiveScan++ extension](https://portswigger.net/bappstore/3123d5b5f25c4128894d97ea1acc4976)
* For a full breakdown of how to install BApps in Burp Suite DAST, go to the [user guide.](https://portswigger.net/burp/documentation/dast/user-guide/extensions/adding-extensions)

## Start scanning now

Whether you are using Burp Suite Professional yourself or Burp Suite DAST for broad, automated coverage, you can start detecting Next.js-based React2Shell today.

* Install or update ActiveScan++ v2.0.8 in either product.
* (Optional) Add the React2Shell Bambda custom scan check to your Burp Suite Professional application for targeted tests.

We will continue to publish updates as more information and broader detection techniques for other React frameworks become available.

### Join the React2Shell conversation

We would love to hear from you. Jump into the PortSwigger Discord to share feedback, tips, and requests with the team and the community.

[Join the PortSwigger Discord.](https://discord.com/invite/portswigger)

## What is React2Shell?

Two new critical vulnerabilities, collectively known as React2Shell (CVE-2025-55182 and CVE-2025-66478), are rapidly gaining traction in the security community. With a CVSS score of 10.0 and unauthenticated remote code execution, many expect a trajectory similar to Log4j, including rapid weaponisation by ransomware groups.

React2Shell affects React and Next.js applications and potentially other frameworks that use React server components.

Because these frameworks underpin a huge number of production apps, a successful exploit can lead to major compromise...