---
title: What's new in Burp Suite Professional: A year of innovation
url: https://portswigger.net/blog/whats-new-in-burp-suite-professional-a-year-of-innovation
source: PortSwigger Blog
date: 2025-05-15
fetch_date: 2025-10-06T22:26:49.591940
---

# What's new in Burp Suite Professional: A year of innovation

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

# What's new in Burp Suite Professional: A year of innovation

[ ]

Eleanor Clarke |
14 May 2025 at 08:26 UTC

![A year of innovation](/cms/images/83/05/16cc-article-e6ab4469-0e05-4e45-b9d4-9dc6f1600133.png)Over the past year, we’ve been hard at work making [Burp Suite Professional](/burp/pro) faster, smarter, and more powerful than ever before. From the launch of Burp AI to major performance upgrades, there's never been a better time to use Burp.

Here’s a roundup of some of the biggest updates we’ve introduced this year to supercharge your testing workflow. To make the most of these improvements, make sure you're running the [latest version](https://portswigger.net/burp/releases#professional) of [Burp Suite Professional](https://portswigger.net/burp/upgrade-community-to-pro). To update, go to the top **Help** menu in Burp and click **Check for updates**.

## Performance wins

We've delivered some major performance boosts to help Burp stay fast and responsive, even under a heavy load:

* Site map and table filtering is significantly quicker.
* Scans now complete more quickly with reduced resource usage.
* Large responses now display much faster and use less memory.
* Browser load times are faster as we now reuse HTTP/1
  connections for outbound requests from the proxy.
* Project files with large numbers of Repeater tabs no longer cause Burp's interface to lag.
* Intruder attacks now run more efficiently - by configuring a [capture filter](https://portswigger.net/burp/documentation/desktop/tools/intruder/results/filtering-results#capture-filter), you can avoid capturing unnecessary responses and reduce overhead.

These improvements are already making a difference to our users:

> I was surprised when a very large table sorted in one second. If that’s due to the new performance stuff, I’m really happy about it! Nice stuff!
>
> - t0xodile, Burp Suite user.

> Keep the performance upgrades coming, they're LIT 🔥
>
> - M0PAM, Burp Suite user.

We hope these changes have made a big difference to your everyday use of Burp. If you're still experiencing any performance issues, we'd love to hear from you. Please email us at support@portswigger.net.

## Build your own Burp features

This year, Bambdas have become one of the most flexible and powerful tools in your testing toolkit. Bambdas are custom scripts that you can write and run directly in Burp, enabling you to automate repetitive tasks, tailor Burp to your workflow, and unlock new ways of working. You can now use these to:

* Extract and analyze data in Burp Repeater with [custom actions](https://portswigger.net/burp/documentation/desktop/tools/repeater/http-messages/custom-actions/index.html).
* Create [advanced match and replace rules](https://portswigger.net/burp/documentation/desktop/tools/proxy/match-and-replace/bambdas.html) to manipulate HTTP traffic.
* Add [custom table columns](https://portswigger.net/burp/documentation/desktop/extend-burp/bambdas/index.html#adding-custom-columns) to surface the data you care about.
* Dynamically [filter the site map](https://portswigger.net/burp/documentation/desktop/tools/target/site-map/bambdas.html) to cut through the noise.

To support your use of Bambdas, we've also added:

* A dedicated output console for debugging scripts.
* A [Bambda library](https://portswigger.net/burp/documentation/desktop/extend-burp/bambdas/managing.html) so you can organize, reuse, and share your favorite scripts with ease.

![Bambda library](/cms/images/0e/0d/e650-article-screenshot_2025-05-12_at_15.03.00.png)

If you get hooked on Bambdas, why not take things further by building your own extensions? You can now kickstart development with our ready-to-use starter project.

Plus, we've expanded the Montoya API with powerful new capabilities for writing extensions and Bambdas. For example, you can now parse, add, delete, and update JSON parameters, and register custom hotkeys.

## A more intuitive user interface

We've refreshed several key areas of Burp to help you work more efficiently:

* Burp Intruder now has a cleaner, more intuitive side panel layout, allowing you to configure attacks without switching between tabs.
* Proxy Intercept lets you manage messages more easily. You can now view an ordered queue of intercepted messages, manage messages in bulk, and manage messages in any order you like.
* Site map navigation is clearer than ever, with alphabetically sorted content, new and refreshed icons, and the ability to toggle between the **URL view** and the [**Crawl paths view**](https://portswigger.net/burp/documentation/desktop/tools/target/crawl-paths).
* You can now [hide HTTP headers](https://portswigger.net/burp/documentation/desktop/settings/ui/message-editor.html#uni...