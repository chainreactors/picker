---
title: HTTP/1.1 Must Die: What This Means for Bug Bounty Hunters
url: https://portswigger.net/blog/http-1-1-must-die-what-this-means-for-bug-bounty-hunters
source: PortSwigger Blog
date: 2025-08-07
fetch_date: 2025-10-07T00:47:37.775486
---

# HTTP/1.1 Must Die: What This Means for Bug Bounty Hunters

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

# HTTP/1.1 Must Die: What This Means for Bug Bounty Hunters

[ ]

Andrzej Matykiewicz |
06 August 2025 at 22:23 UTC

![](/cms/images/2a/9d/20a2-article-http1mustdieblogheader1.png)

At Black Hat USA and DEFCON 2025, PortSwigger's Director of Research, James Kettle, issued a stark warning: request smuggling isn't dying out, it's evolving and thriving.

Despite years of defensive efforts, new research unveiled by Kettle proves that [HTTP request smuggling](/web-security/request-smuggling) (or "desync" attacks) remain not only rampant but dangerously underestimated, compromising tens of millions of supposedly well-secured websites worldwide, netting $200k+ in bounties in the space of just two weeks.

In his groundbreaking new research, [HTTP/1.1 Must Die: The Desync Endgame](https://portswigger.net/research/http1-must-die), Kettle challenges the security community to completely rethink its approach to request smuggling. He argues that, in practical terms, it's nigh on impossible to consistently and reliably determine the boundaries between HTTP/1.1 requests, especially when implemented across the chains of interconnected systems that comprise modern web architectures. Mistakes such as parsing discrepancies are inevitable, and when using upstream HTTP/1.1, even the tiniest of bugs often have critical security impact, including complete site takeover.

This research demonstrates unequivocally that patching individual implementations will never be enough to eliminate the threat of request smuggling. Upstream HTTP/2 offers a robust solution.

**If we are serious about securing the modern web, it's time to retire HTTP/1.1 for good.**

As a bug bounty hunter, this is a huge opportunity. The attack surface is bigger than ever. If you've not got request smuggling in your arsenal, now's the time to dive in, with new vectors, new tooling, and new strategies that bypass current defenses.

## Why This Research Matters to Bug Bounty Hunters

* **It still pays. Big time.**

  This research reveals critical desync flaws leading to mass compromise of top-tier platforms that may have remained undetected for years. In fact, Kettle and the team behind the research netted over $200k in bug bounties in the course of just a couple of weeks. Desync attacks are still massively underexplored, especially on CDN-backed apps and microservices. While the rest of the crowd is spraying for [XSS](/web-security/cross-site-scripting) or hoping to bag an [IDOR](/web-security/access-control/idor), you can be honing in on high-impact, high-reward request smuggling vulns.
* **Unmined Gold in Familiar Places.**

  You might think the targets you've tested aren't vulnerable due to WAFs, patches and other supposed defences. This research shows that traditional fixes can be easily bypassed by making minor tweaks to known attacks. These subtle variations can be detected much more reliably by looking for desync primitives, or the underlying parser discrepancies at the root of the issue, rather than jumping straight to firing exploits to see what sticks. That means your old targets just became a fertile hunting ground for critical vulnerabilities.
* **It gives you an edge.**

  Burp Suite's new and improved tools like HTTP Request Smuggler v3.0 and HTTP Hacker help you surface the underlying desync primitives that indicate potential request smuggling vectors. Understanding how to wield them gives you a real advantage over hunters who are still blasting outdated payloads that are blocked by superficial, fingerprint-based defences.
* **It reveals hidden vulnerabilities.**

  Some of the most successful bugs came from places you might not be testing: internal redirects, backend APIs, and edge case behaviors like handling of `Expect` headers. The lesson? You don't need a massive attack surface, just the right parser mismatch.

## Underestimated Angles that Could Net You Bounties

* **Vulnerabilities beyond the application layer:** These bugs live deep in the HTTP stack, between CDNs, load balancers, and backend servers. They're invisible to most tools, and often untouched by traditional bounty hunters, especially those using subpar tooling with limited support for testing beyond basic injection flaws.
* **New Desync Variants:** The paper introduces brand new forms of request smuggling and new techniques for detecting classic desync vectors. By testing for the parsing discrepancies at the heart of the problem, rather than sending payloads, you can find swathes of request smuggling bugs that may have remained undetected until now.
* **Forget WAFs:** Most of the affected platforms used edge protections. But regex-based defenses don't cut it when the flaw is buried in protocol-level behavior. One of the ...