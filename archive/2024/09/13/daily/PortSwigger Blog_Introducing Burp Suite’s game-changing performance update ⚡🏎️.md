---
title: Introducing Burp Suite’s game-changing performance update ⚡🏎️
url: https://portswigger.net/blog/introducing-burp-suites-game-changing-performance-update
source: PortSwigger Blog
date: 2024-09-13
fetch_date: 2025-10-06T18:27:12.929154
---

# Introducing Burp Suite’s game-changing performance update ⚡🏎️

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

# Introducing Burp Suite’s game-changing performance update ⚡🏎️

[ ]

Amelia Coen |
12 September 2024 at 11:55 UTC

![](/cms/images/03/90/dbe6-article-pp_blog_header.png)

## Hands-on security testers need the best tools for the job. Tools you have faith in, and enjoy using all day long. Burp Suite has long been that tool, and now, it's faster than ever.

We’ve listened to your feedback and introduced key performance updates to ensure the core tools you rely on are faster, more efficient, and use less memory.

## A more efficient Burp Suite

### Drastically reduced sorting time for tables

Tables are a core component of Burp Suite. Most of the data produced in Burp is presented in table format. Being able to manipulate this data through sorting is key to your workflow.

Tables which previously would take minutes to sort, are now sorted in a matter of seconds, increasing responsiveness and reducing UI freezes.

![](/cms/images/72/86/7266-article-screenshot_2024-09-12_at_09.20.03.png)

> I was surprised when a very large table sorted in one second. If that’s due to the new performance stuff, I’m really happy about it! Nice stuff!
> - t0xodile, [Burp Suite Professional](/burp/pro) user.

### Reduced UI lag and load times

In Burp Suite, your large project files now load faster, even if you’ve got a large number of Repeater tabs. These new changes have significantly reduced memory usage, and will noticeably reduce UI lagging.

![](/cms/images/b4/00/3b97-article-screenshot_2024-09-12_at_12.02.42.png)

### Improved loading times in the HTTP history

Multiple changes have been introduced to improve loading times when viewing requests and responses in the HTTP history to prevent the UI from freezing.

### Faster site map filtering

Similarly, sitemap filtering time has been significantly minimized. Large sitemaps, which potentially may have taken hours to filter, can now be filtered in a matter of minutes.

### Reduced Intruder memory usage

Memory usage in Intruder has been significantly reduced, improving loading times and minimizing the possibility of UI freezes.

If you're interested in more technical details about how we've achieved these improvements, [check out this blog post](https://portswigger.net/blog/burp-suite-performance-improvements) from one of our software engineers.

![](/cms/images/f5/d6/303f-article-screenshot_2024-09-12_at_09.31.59.png)

## Optimizing your workflow with Burp

### An easy-to-use Proxy Intercept View

The new and improved Proxy Intercept view allows you to have better control when working with websites and functionality that trigger a large number of requests, helping you work more efficiently and at pace.

This new update now allows you to…

* View multiple queued requests in a table and manage them in bulk.
* View requests and responses in a single view.
* Forward all requests.
* Highlight and comment on requests and responses.
* Pull through any highlights or comments to the HTTP history.

## Coming soon…

### New UI improvements to Intruder

Intruder is one of the core tools you will use when manual testing, so we’re streamlining the UI to help make your workflow as efficient as possible.

This includes…

* Tabs being easier to access on the right side of the screen.
* Side by side view of the results table and tabs, making it easier to add columns.
* The ability to replace section characters more easily within the request template editor.

![](/cms/images/56/bd/36ef-article-intruder_redesign.png)

### Proxy Match and Replace

We’re adding a match and replace tab directly within the Proxy, making it more discoverable and easier to access. Additionally, we’re implementing a test capability within the HTTP match and replace dialog to make writing match and replace rules easier.

Soon, you’ll also be able to write HTTP match and replace Bambdas, enabling more powerful match and replace rules to be utilized.

![](/cms/images/a1/ba/2ce7-article-match_and_replace_gif.gif)

## Burp’s future, driven by performance

Performance is not a one-time fix. We’re making an on-going commitment to improve performance in Burp Suite, ensuring that efficiency, accuracy, and thoroughness are at the forefront of every new update and feature.

As Burp Suite evolves, this performance-first mindset will continue to inform the product decisions of today and tomorrow. Our team is actively using telemetry and regression testing to help identify issues, including those that may previously have been invisible to us, allowing us to act quickly to improve your experience with Burp.

![](/cms/images/08/69/657f-article-screenshot_2024-09-12_at_12.05.47.png)

## Ready to unleash the power of these new updates?

Say goodbye to frustrating performance blo...