---
title: DAST without disruption: Burp Suite DAST winter update 2025
url: https://portswigger.net/blog/burp-suite-dast-winter-update-2025
source: PortSwigger Blog
date: 2025-12-11
fetch_date: 2025-12-12T03:21:05.282537
---

# DAST without disruption: Burp Suite DAST winter update 2025

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

# DAST without disruption: Burp Suite DAST winter update 2025

[ ]

Rob Samuels |
11 December 2025 at 13:09 UTC

AppSec teams are under constant pressure to secure fast-moving applications without slowing anything down. But scanning windows, fragile authentication, and sprawling API estates often get in the way of true automation.

[The latest updates to Burp Suite DAST](http://portswigger.com/burp/dast/winter-2025-update) are designed to remove that friction. We’ve introduced a set of new features that make scanning more reliable, more flexible, and far easier to manage at scale, so you can keep improving security without disrupting your workflow.

Here’s a quick summary of what’s new:

## 1. Run scans on your terms

### Scan freeze windows

![](/cms/images/9b/a9/5985-article-screenshot_2025-12-10_at_10.16.53.png)

Many teams need scans to respect deployment cycles, maintenance windows, and change freezes. Until now, that often meant manually pausing or cancelling scans.

Scan freeze windows automate all of this. Define the times when scans shouldn’t run, and [Burp Suite DAST](/burp/dast) will pause scanning automatically. No babysitting, no lost progress, and far smoother automation overall.

**[Take a demo of scan freeze windows](https://app.getreprise.com/launch/wy1MNBy/).**

### Improved performance for large portfolios

Managing large site inventories is now quicker and more consistent. Whether you’re structuring folders, scheduling scans, or reshaping your site tree, Burp Suite DAST handles large estates more smoothly than before.

### Intuitive folder-based organisation for CI-driven scans

If you trigger scans through [CI/CD](/developers/ci-cd-security), Burp Suite DAST will now place them into the right folders automatically. This keeps environments tidy and makes it much easier to track results across teams and pipelines.

## 2. Stronger, clearer authenticated scanning

### Simplified recorded login management

![](/cms/images/bc/de/65bd-article-screenshot_2025-12-10_at_11.33.06.png)

Login flows change, and when they do, authenticated scans often break. Instead of re-recording everything from scratch, the new recorded login editor lets you update individual steps directly. You can adjust fields, selectors, and interactions in seconds, keeping scans accurate with far less effort.

**[Try the interactive demo here](https://app.getreprise.com/launch/BXZ2aEX/).**

### Authentication visibility

Diagnosing authentication issues shouldn’t rely on guesswork. Burp Suite DAST now shows you what’s happening behind the scenes in real time, including screenshots and responses when something fails. Troubleshooting becomes much simpler and faster.

### XPath/CSS authentication checks

Modern single-page applications rely heavily on dynamic UI changes. Flexible XPath and CSS checks help DAST confirm whether a session is still authenticated, making scans more reliable across dynamic and JavaScript-heavy apps.

### Authentication status checker

This gives you immediate visibility when a session drops. If authentication breaks mid-scan, you’ll know straight away, reducing blind spots and preventing wasted scanning time.

## 3. Scanning built for the age of APIs

### Support for environment variables when scanning Postman Collections

You can now import Postman collections together with environment variables. This means faster, cleaner setup and more accurate reproduction of real-world API traffic.

### Auto-validation of OpenAPI definitions

If an OpenAPI definition contains issues, a scan may fail before it even begins. Burp Suite DAST now highlights these problems upfront so you can fix them before running the scan, improving reliability and reducing manual rework.

### More consistent accuracy across API scans

With better handling of authentication, environment variables, and definition structure, Burp Suite DAST delivers more stable results across modern API estates, especially at scale.

## Experience DAST without disruption

These updates are all about making scanning smoother, more predictable, and better aligned with how enterprise engineering teams actually work.

*Ready to see it in action?*

**[Request a demo to find out how Burp Suite DAST can streamline your AppSec program](https://staging.portswigger.com/burp/dast/trial?ps_medium=organic&ps_source=campaign%20lp&ps_campaign=dast-winter-campaign-2025&ps_content=request-a-demo).**

[ ]

![Rob Samuels](/cms/profiles/rob-samuels.png)

This page requires JavaScript for an enhanced user experience.

Latest Posts

[### How to detect React2Shell with Burp Suite

05 December 2025
How to detect React2Shell with Burp Suite](/blog/how-to-detect-react2shell-with-burp-suite)
[### PortSwigger x TryHackMe: Supporting Advent of Cyber

01 December 2025
PortSwigger x TryHackMe: Supporting Advent of Cyber](/blog/portswigger...