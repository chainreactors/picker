---
title: "The entire internet is broken": ethical hacking expert John Hammond meets James Kettle
url: https://portswigger.net/blog/the-entire-internet-is-broken-ethical-hacking-expert-john-hammond-meets-james-kettle
source: PortSwigger Blog
date: 2025-08-28
fetch_date: 2025-10-07T00:47:56.300286
---

# "The entire internet is broken": ethical hacking expert John Hammond meets James Kettle

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

# "The entire internet is broken": ethical hacking expert John Hammond meets James Kettle

[ ]

Amelia Coen |
27 August 2025 at 09:11 UTC

![](/cms/images/6f/fe/1ca3-article-copy_of_two_months_of_(3).png)

### In a [brand-new collaboration](https://www.youtube.com/watch?v=n3Bw8CASnHE) between ethical hacking and AppSec expert John Hammond and world-renowned security researcher James Kettle, the pair explore how tens of millions of websites are compromised.

In [this video](https://www.youtube.com/watch?v=n3Bw8CASnHE), John and James dive deep into James’ new [HTTP/1.1 Must Die](https://http1mustdie.com/) research, the cutting edge of web security, focusing on the inherent insecurity of HTTP/1.1. As James explains, upstream HTTP/1.1 routinely exposes millions of websites to hostile takeover. For over six years, vendors have rolled out mitigation after mitigation, but researchers have consistently found ways to bypass them.

## Watch the video

[![](/cms/images/4a/cb/209d-article-copy_of_two_months_of.png)](https://www.youtube.com/watch?v=n3Bw8CASnHE)

## Why must HTTP/1.1 Die?

In PortSwigger’s [latest research](https://http1mustdie.com/), James introduces new classes of HTTP desync attack and demonstrates critical vulnerabilities affecting tens of millions of websites, including core infrastructure within major CDNs. A live demo makes the threat all the more tangible, showing how attackers exploit fundamental protocol flaws to devastating effect.

The takeaway is clear: HTTP/1.1 has a fatal flaw. It allows attackers to create dangerous ambiguity about where one request ends and the next begins. By contrast, HTTP/2 eliminates this ambiguity, making desync attacks virtually impossible—provided it’s used not only at the edge, but also for the upstream connection between reverse proxies and origin servers.

## What do I need to do?

Act Now: Join the Mission to Kill HTTP/1.1

* [Read the research: HTTP/1.1 Must Die: The Desync Endgame](https://http1mustdie.com/)
* [Sharpen your skills: Try the 20+ free request smuggling labs, including the new 0.CL lab, on the Web Security Academy](https://portswigger.net/web-security/request-smuggling/advanced/lab-request-smuggling-0cl-request-smuggling).
* Defend systems still using HTTP/1.1: Detect threats with Burp Suite extensions, including [HTTP Request Smuggler v3.0](https://github.com/PortSwigger/http-request-smuggler) and [HTTP Hacker](https://github.com/PortSwigger/http-hacker), and use recurring scans to stay ahead.
* Move to HTTP/2: Ensure your origin servers support HTTP/2, then enable upstream HTTP/2 across your front-end systems.

## Join the movement

There’s thousands of security testers, bug bounty hunters, and AppSec professionals over on the official [PortSwigger Discord](https://discord.com/invite/portswigger).

[Join the server today](https://discord.com/invite/portswigger) to join the discussion and hear about how others are killing HTTP/1.1 across their applications.

[ ]

![Amelia Coen](/cms/profiles/amelia-coen.png)

This page requires JavaScript for an enhanced user experience.

Latest Posts

[### Hacking smarter with Burp AI: NahamSec puts Burp AI to the test

01 October 2025
Hacking smarter with Burp AI: NahamSec puts Burp AI to the test](/blog/hacking-smarter-with-burp-ai-nahamsec-puts-burp-ai-to-the-test)
[### Welcome to AI pentesting - add on-demand AI assistance directly to your workflow with new, agentic Burp AI capabilities

24 September 2025
Welcome to AI pentesting - add on-demand AI assistance directly to your workflow with new, agentic Burp AI capabilities](/blog/welcome-to-ai-pentesting-add-on-demand-ai-assistance-directly-to-your-workflow-with-new-agentic-burp-ai-capabilities)
[### How to join the desync endgame: Practical tips from pentester Tom Stacey

18 September 2025
How to join the desync endgame: Practical tips from pentester Tom Stacey](/blog/how-to-join-the-desync-endgame-practical-tips-from-pentester-tom-stacey)

Burp Suite

[Web vulnerability scanner](/burp/vulnerability-scanner)
[Burp Suite Editions](/burp)
[Release Notes](/burp/releases)

Vulnerabilities

[Cross-site scripting (XSS)](/web-security/cross-site-scripting)
[SQL injection](/web-security/sql-injection)
[Cross-site request forgery](/web-security/csrf)
[XML external entity injection](/web-security/xxe)
[Directory traversal](/web-security/file-path-traversal)
[Server-side request forgery](/web-security/ssrf)

Customers

[Organizations](/organizations)
[Testers](/testers)
[Developers](/developers)

Company

[About](/about)
[Careers](/careers)
[Contact](/about/contact)
[Legal](/legal)
[Privacy Notice](/privacy)

Insights

[Web Security Academy](/web-security)
[Blog](/blog)
[Research](/research)

[![PortSwigger...