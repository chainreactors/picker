---
title: How this seasoned bug bounty hunter combines Burp Suite and HackerOne to uncover high-impact vulnerabilities
url: https://portswigger.net/blog/how-this-seasoned-bug-bounty-hunter-combines-burp-suite-and-hackerone-to-uncover-high-impact-vulnerabilities
source: PortSwigger Blog
date: 2025-09-13
fetch_date: 2025-10-02T20:05:53.858066
---

# How this seasoned bug bounty hunter combines Burp Suite and HackerOne to uncover high-impact vulnerabilities

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

# How this seasoned bug bounty hunter combines Burp Suite and HackerOne to uncover high-impact vulnerabilities

[ ]

Amelia Coen |
12 September 2025 at 12:21 UTC

![](/cms/images/aa/d7/3a0a-article-chatgpt_image_sep_12,_2025,_11_29_01_am.png)

### Arman S. (Tess), a full-time independent security researcher and bug bounty hunter, talked us through how he uses [Burp Suite Professional](https://portswigger.net/burp/pro) and [HackerOne](https://www.hackerone.com/) in tandem to find and report high-value security vulnerabilities, and how this has secured him thousands of dollars in bounties.

## What is Burp Suite? And what is HackerOne?

* **[Burp Suite Professional](https://portswigger.net/burp/pro)** is a leading [web vulnerability scanner](/burp/vulnerability-scanner) and proxy tool developed by PortSwigger, used by security professionals to intercept, manipulate, and analyze HTTP requests in real time. Its extensibility and powerful features make it indispensable for web application testing.
* **[HackerOne](https://www.hackerone.com/)** is a premier bug bounty platform that connects ethical hackers with organizations to report security issues in return for monetary rewards. It offers structured programs, scope definitions, and mediation services.

Together, these tools empower security researchers to work efficiently and responsibly.

## Getting started as a hacker

Getting started in the industry, Tess began hacking at age 16 by experimenting with Wi-Fi networks and phishing for fun. After discovering bug bounties on Twitter, he shifted to ethical hacking and quickly realized its professional potential.

> I started doing bug bounties full-time in college, dropped out, and never looked back. I was making good money, learning fast, and loving it.

## Why Burp Suite is integral to every hunt

> Let me be honest with you, if a hacker tells you he's not using Burp Suite, then he's not a hacker. It's like a microscope for web applications.

When participating in HackerOne programs, Burp Suite becomes essential:

* Tess starts by downloading the Burp project file provided in the program’s scope on HackerOne.
* He proxies all his traffic through Burp Suite, using it to intercept requests, explore endpoints, and uncover hidden behaviors in the application.
* With Burp Extensions like [JS Miner](https://portswigger.net/bappstore/0ab7a94d8e11449daaf0fb387431225b) and the [HTTP Request Smuggler](https://portswigger.net/bappstore/aaaa60ef945341e8a450217a54a11646), he’s able to automate and extend his testing capabilities.

> You wouldn’t believe the time Burp saved me by catching backend requests the browser never shows. That’s how you find the real bugs.

HackerOne provides the platform for Tess to focus on impactful, in-scope targets. It also simplifies communication and triage:

> Everything is so systematic: find the bug, report it, and if needed, open mediation. Without HackerOne, I don’t think the bug bounty ecosystem would function as well.

With this combination, Tess has seen big wins and real results. One of Tess’ most notable wins, a $38,000 bug bounty, was uncovered using Burp’s [HTTP Request Smuggler](https://portswigger.net/bappstore/aaaa60ef945341e8a450217a54a11646) extension:

> I was testing an API on Zoom’s bug bounty program and Burp flagged possible smuggling. That lead turned into a $38K bounty.

## Why this combination works

* **[Burp Suite](https://portswigger.net/burp/pro)** gives hackers granular control, automation, and observability.
* **[HackerOne](https://www.hackerone.com/)** streamlines the process from discovery to reward.
* Burp’s project files provide reproducibility and evidence when submitting reports.

> Sometimes I send the Burp project file directly to the triage team. It proves the bug existed at a specific time.

Tess credits much of his success to the [Web Security Academy](https://portswigger.net/web-security), [James Kettle’s research](https://portswigger.net/research), and the [wider community](https://discord.com/invite/portswigger).

> Solving labs helped me understand attacks deeply. When I see something in the wild, I go, 'Oh, I saw that on PortSwigger.

He also appreciates the responsiveness of PortSwigger’s support and the utility of the Discord community.

## Advice for new hackers

> Start with [PortSwigger Labs](https://portswigger.net/web-security) and HackerOne CTFs. Pick one type of vulnerability, like [XSS](/web-security/cross-site-scripting), and go deep. Learn the tools, practice the labs, and follow the research.

For Tess, Burp Suite and HackerOne aren’t optional, they’re foundational.

> Burp Suite runs in the background even when I’m not actively using it. It’s my evidence, my toolkit, my safety...