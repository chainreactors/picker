---
title: HTTP/1.1 Must Die: What This Means for AppSec Leadership
url: https://portswigger.net/blog/http-1-1-must-die-what-this-means-for-appsec-leadership
source: PortSwigger Blog
date: 2025-08-07
fetch_date: 2025-10-07T00:18:30.150442
---

# HTTP/1.1 Must Die: What This Means for AppSec Leadership

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

# HTTP/1.1 Must Die: What This Means for AppSec Leadership

[ ]

Andrzej Matykiewicz |
06 August 2025 at 22:23 UTC

![](/cms/images/2a/9d/20a2-article-http1mustdieblogheader1.png)

At Black Hat USA and DEFCON 2025, PortSwigger's Director of Research, James Kettle, issued a stark warning: request smuggling isn't dying out, it's evolving and thriving.

Despite years of defensive efforts, new research unveiled by Kettle proves that [HTTP request smuggling](/web-security/request-smuggling) (or "desync" attacks) remains a systemic, protocol-level threat, compromising tens of millions of supposedly well-secured websites worldwide.

In his groundbreaking new research, [HTTP/1.1 Must Die: The Desync Endgame](https://portswigger.net/research/http1-must-die), Kettle challenges the security community to completely rethink its approach to request smuggling. He argues that, in practical terms, it's nigh on impossible to consistently and reliably determine the boundaries between HTTP/1.1 requests, especially when implemented across the chains of interconnected systems that comprise modern web architectures. Mistakes such as parsing discrepancies are inevitable, and when using upstream HTTP/1.1, even the tiniest of bugs often have critical security impact, including complete site takeover.

This research demonstrates unequivocally that patching individual implementations will never be enough to eliminate the threat of request smuggling. Using upstream HTTP/2 offers a robust solution.

**If we are serious about securing the modern web, it's time to retire HTTP/1.1 for good.**

In the meantime, audit your portfolio using [the only DAST scanner capable of reliably testing for desync vulnerabilities](https://portswigger.net/blog/the-desync-delusion-are-you-really-protected-against-http-request-smuggling): [Burp Suite DAST](/burp/dast).

## Widespread Exposure with Critical Consequences

Desync attacks exploit the ambiguity in HTTP/1.1 parsing to hijack sessions, poison caches, and leak user data. What's now clear is that HTTP/1.1's core design, with its lenient text-based message parsing, multiple length-specification mechanisms, and decades-old compatibility quirks, make it impossible to defend reliably.

PortSwigger's 2025 research demonstrates how supposedly "patched" systems, including those protected by major CDNs and WAFs, are still vulnerable on a widespread scale. This isn't an academic risk; the research team were awarded over $200,000 in bug bounties from these techniques over just two weeks, proving that several major CDNs were vulnerable, potentially compromising every one of their 24m customers' web infrastructure. This only serves to highlight the prevalence and severity of the problem.

For AppSec leaders, this presents a strategic concern: even if your organization believes it's covered, you may be relying on brittle defenses and dangerous assumptions that simply don't stand up to scrutiny.

## Complacency is the Enemy

You may have implemented the available defensive measures and patched request smuggling bugs over the years as new vectors are discovered. But the attack class hasn't gone away; it's simply evolved. PortSwigger's latest research reveals that desync vulnerabilities are still extremely prevalent, especially where systems quietly downgrade HTTP/2 to HTTP/1.1 behind the scenes, adding yet more complexity and ambiguity that can potentially be exploited.

**Key takeaways:**

* If you use HTTP/1.1 anywhere in your architecture you may be at risk.
* Supposedly mature defenses often rely on regex-based heuristics or input sanitization that fail to provide any protection whatsoever against novel payloads and desync variants. In fact, they merely mask the problem by preventing standard detection techniques.
* Downgrade scenarios are especially dangerous. Many systems appear to use HTTP/2 but secretly rely on vulnerable HTTP/1.1 internally, including some CDNs that claim to provide end-to-end HTTP/2 support.

## What Security Leaders Should Do Next

AppSec leaders are in a unique position to drive meaningful change. Here's what we recommend:

1. **Audit for desync exposure:** Conduct a protocol-layer audit to locate legacy HTTP/1.1 dependencies. Use tooling like Burp Suite's HTTP Request Smuggler and HTTP Hacker to identify parser discrepancies, or scan your estate at scale with Burp Suite DAST; [the only DAST scanner capable of genuine automated detection of the latest request smuggling threats.](https://portswigger.net/blog/the-desync-delusion-are-you-really-protected-against-http-request-smuggling)
2. **Revise threat models:** Include request smuggling and desync attacks explicitly in your threat models and [pentesting](/solutions/penetration-te...