---
title: PHP2Shell x Burp Suite: Detection in your hands within a day of disclosure
url: https://portswigger.net/blog/php2shell-x-burp-suite-detection-in-your-hands-within-a-day-of-disclosure
source: PortSwigger Blog
date: 2026-10-23
fetch_date: 2026-10-24T06:46:00.218670
---

# PHP2Shell x Burp Suite: Detection in your hands within a day of disclosure

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

[![Burp AT](/mega-nav/images/burp-at.svg)
**Burp AT**
Agentic AI that extends human-led pentesting.](/burp/burp-at)
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

What's the difference between Pro and DAST?

![Burp Suite Professional vs Burp Suite DAST](/mega-nav/images/burp-suite.jpg)](/burp/dast/resources/dast-vs-professional)

[**Support Center**
Get help and advice from our experts on all things Burp.](/support)
[**Documentation**
Tutorials and guides for Burp Suite.](/burp/documentation)
[**Get Started - Professional**
Get started with Burp Suite Professional.](/burp/documentation/desktop/getting-started)
[**Get Started - DAST**
Get started with Burp Suite DAST.](/burp/documentation/dast/setup)
[**Downloads**
Download the latest version of Burp Suite.](/burp/releases)

[Visit the Support Center](/support)

[**Downloads**

Download the latest version of Burp Suite.

![The latest version of Burp Suite software for download](/mega-nav/images/latest-burp-suite-software-download.jpg)](/burp/releases)

# PHP2Shell x Burp Suite: Detection in your hands within a day of disclosure

[ ]

Andrzej Matykiewicz |
Friday, 23 October 2026 at 13:50 UTC

![Generic Pro and DAST](/cms/images/78/46/e059-article-10e7-article-better-together_v2_blog_header_(940x400)_.png)

PHP2Shell (CVE-2026-109618 and CVE-2026-109619) became the latest vulnerability to grab headlines around the globe. By some estimates, up to 70% of websites run at least some PHP. So if you're responsible for web applications, you've probably spent the last few days trying to work out if you're exposed as quickly as possible, but without taking your systems offline.

That's why within hours of disclosure, we made sure you could test for PHP2Shell safely using Burp Suite.

In this post, we'll walk you through the options you've now got access to across the Burp Suite ecosystem, and what you can do right now to check your exposure.

**Key highlights**

* Burp AT now has a skill, so agents can now test for PHP2Shell on your behalf. [Find out more](https://portswigger.net/burp/burp-at?utm_source=blog&utm_medium=blog&utm_campaign=php2shell_response_blog)
* You can scan for PHP2Shell at enterprise scale in [Burp Suite DAST](/burp/dast). Just make sure you're on [Burp Scanner](/burp/vulnerability-scanner) version 2026.10.54778 or above.
* There are [active](https://github.com/PortSwigger/bambdas/blob/main/CustomScanChecks/CVE-2026-109618CVE-2026-109619-PHP2Shell.bambda) and [passive](https://github.com/PortSwigger/bambdas/blob/main/CustomScanChecks/CVE-2026-109618CVE-2026-109619-PHP2ShellVulnerablePhpVersion.bambda) scan checks available now for [Burp Suite Professional](/burp/pro).
* [ActiveScan++](https://portswigger.net/bappstore/3123d5b5f25c4128894d97ea1acc4976) detects PHP2Shell, supported in both Burp Suite Professional and Burp Suite DAST.

![Timeline](/cms/images/43/56/49fd-article-php2shell-timeline_1.png)

## Why this keeps happening, and faster

AI is speeding up vulnerability discovery. That's true for researchers, and it's true for attackers.

In practice, that means two things. First, we'll see more critical bugs turn up in mature, widely used systems and codebases. Second, the time between a bug being discovered and it being exploited is getting shorter.

That's why response speed matters even more now than it always did, both for us as a tool vendor and for those of you testing and defending applications.

## Getting detection into your hands, fast

Our mission is to enable the world to secure the web. Moments like this are where that mission gets tested.

PortSwigger's research team picked up the early signals around PHP2Shell and alerted our engineering teams straight away. From there, they dug into the details themselves, while keeping tabs on the latest developments and insights from the wider community.

What followed was a rolling series of enhancements across the Burp Suite ecosystem.

### Passive detection, as early as possible

We were able to release passive detection almost straight away via our extensibility APIs, with a Java-based custom scan check and a DAST-compatible BCheck. James Kettle also updated his [ActiveScan++](https://portswigger.net/bappstore/3123d5b5f25c4128894d97ea1acc4976) extension, which is compatible with both Burp Suite Professional and Burp Suite DAST.

This passive approach was fairly limited, but we wanted to get something in users' hands quickly as the main detection method circulating at the time involved crashing the server. We shipped these checks immediately, while still working on more sophisticated active checks.

### Active detection, tested for safety

Next came active detection, which involved sending a payload to the server. Any active probe can have potentially harmful knock-on effects, and these aren't always obvious at first glance.

Time was still of the essence, hence the decision to release them as custom scan checks. However, we made sure to run the active checks across a range of servers and PHP versions to give us confidence we weren't releasing something that would leave users spraying payloads at their production systems and inadvertently taking vulnerable ones offline.

Once released, you could then run active and passive detection across your applications with confidence.

With the next release of Burp Suite Professional, these checks will be natively integrated with Burp Scanner.

## Beyond the scanner: Burp AT skills for PHP2Shell detection

At Black Hat USA 2026, we launched Burp AT, our approach to bringing agentic tooling into human-led [pentesting](/solutions/penetration-testing). One of the things that sets it apart is its library of dedicated pentesting skills, including ones developed by the PortSwigger Research team.

That library now includes a skill for PHP2Shell, so you can simply ask an agent to test for it.

* **Consistent and proven technique.** A key advantage of these specialized skills...