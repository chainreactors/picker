---
title: PortSwigger at Black Hat &amp; DEF CON 33
url: https://portswigger.net/blog/portswigger-at-black-hat-amp-def-con-33
source: PortSwigger Blog
date: 2025-07-09
fetch_date: 2025-10-06T23:39:51.490128
---

# PortSwigger at Black Hat &amp; DEF CON 33

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

# PortSwigger at Black Hat & DEF CON 33

[ ]

Tom Ryder |
08 July 2025 at 09:17 UTC

![](/cms/images/f5/69/0430-article-bh-article.png)

## Las Vegas. August. Protocols are getting torn apart.

This summer, PortSwigger returns to [Black Hat USA](https://www.blackhat.com/)
and [DEF CON 33](https://defcon.org) with a host of new talks, events and ways to meet PortSwigger and the the teams behind Burp Suite.

This year, we have a bold message:

### HTTP/1.1 must die.

![](/cms/images/fb/d4/1112-article-http1inline.png)

Although it's been six years since PortSwigger Research first brought request smuggling to mainstream attention, attempts to mitigate these attacks have repeatedly proven to be ineffective at best and, in some cases, to actually make the situation worse.

The time has come to acknowledge that request smuggling is an inherent flaw in the HTTP/1.1 protocol itself and, as such, its continued use should be considered a vulnerability in its own right.

**Learn more at [http1mustdie.com](https://http1mustdie.com)**.

### BSides Las Vegas - Monday 4 August

There will be a PortSwigger presence at BSides Las Vegas, meeting the community. If you're attending, let us know on socials with #BurpOnTour and #BSidesLV.

## Upstream HTTP/1.1 is inherently insecure: The Desync Endgame

### Wednesday, August 6, 3.20pm

At Black Hat and DEFCON33, PortSwigger's Director of Research, **James Kettle ([@albinowax](https://x.com/albinowax))**, will demonstrate how it was still possible to compromise every single customer of three major CDNs, leaving tens of millions of websites exposed to potentially critical attacks.

He'll unveil new classes of desync attacks and a toolkit to help you identify request smuggling vulnerabilities more easily and reliably than ever before, **the same techniques and tools he used to earn over $200k in bug bounties in just two weeks.**

Tune in to our coverage of Black Hat and DEFCON33:

* Learn cutting-edge smuggling techniques others aren’t using (yet)
* A free toolkit to identify critical flaws in CDNs and edge infrastructure

Whether you still use HTTP/1.1 intentionally, or are forced to due to the limitations of your CDN's infrastructure, we want to challenge the industry to sunset this vulnerable, legacy technology. If we want a secure web, HTTP/1.1 must die!

**Where to watch:**

* Black Hat USA – August 6 (3.20pm PDT, 10.20pm UTC)
* DEF CON 33 – August 8 (4.30pm PDT, 11.30pm UTC)
* PortSwigger post-con stream - TBD

### DEF CON Workshop: Advanced HTTP Smuggling Exploitation

In this session, **Martin Doyhenard ([@tincho\_508](https://x.com/tincho_508)
)** will show you how to dissect HTTP at the stream level, revealing hidden behaviors that traditional tools miss and turning them into powerful exploits. You’ll learn how to spot hidden proxies, exploit subtle errors to desynchronize connections, hijack requests, and uncover vulnerabilities that evade traditional tools.

Through real-world case studies, Martin reveals exactly how you can chain advanced HTTP Desync attacks to secure bounties that others have left behind, transforming complex network architectures into your playground.

### Arsenal Tools That Hit Beyond the Application Layer

We’re not just bringing research, we’re arming you with tools built for modern web security.

#### HTTP Hacker

**Martin Doyhenard (@tincho\_508) — [Black Hat Arsenal | August 6, 1:00–1:55pm](https://portswigger.net/research/talks?talkId=33)**

Your proxy might be lying to you. HTTP Hacker gives you raw stream-level access to see what’s really happening across persistent connections, pipelining, and edge infrastructure.

Built as a Burp Suite extension, it helps you:

* Go beyond what scanners see. Find bugs hidden behind multi-hop routing and caching layers
* Identify smuggling and cache bugs that could enable full credential theft in enterprise systems

If you care about HTTP smuggling, caching bugs, or infrastructure-level attacks, this is the tool you've been waiting for.

#### WebSocket Turbo Intruder

**Zakhar Fedotkin ([@d4d89704243](https://x.com/d4d89704243)
) — [Black Hat Arsenal | August 6, 1:00–1:55pm](https://portswigger.net/research/talks?talkId=31)**

[WebSockets](/web-security/websockets) are everywhere but security testing them has been a pain. That ends now with WebSocket Turbo Intruder.

Under the hood, WebSocket Turbo Intruder allows you to:

* Fuzz WebSockets at scale and find deep protocol-level bugs that others miss
* Automate complex, multi-step WebSocket attacks with ease even without deep scripting skills

If you’ve been ignoring WebSockets because the tooling wasn’t there, this is your moment to start looking at this vast and under-explored attack surface.

### ...