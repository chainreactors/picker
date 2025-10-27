---
title: The Desync Delusion: Are You Really Protected Against HTTP Request Smuggling?
url: https://portswigger.net/blog/the-desync-delusion-are-you-really-protected-against-http-request-smuggling
source: PortSwigger Blog
date: 2025-08-07
fetch_date: 2025-10-07T00:47:42.202647
---

# The Desync Delusion: Are You Really Protected Against HTTP Request Smuggling?

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

# The Desync Delusion: Are You Really Protected Against HTTP Request Smuggling?

[ ]

Andrzej Matykiewicz |
06 August 2025 at 22:22 UTC

![](/cms/images/c0/2e/e2ae-article-dast_article[1].png)

## The Hidden Threat That's Slipping Past Your Security

[HTTP request smuggling](/web-security/request-smuggling) remains one of the most dangerous yet frequently overlooked web vulnerabilities today. Despite being a widely known issue since 2019, traditional [Dynamic Application Security Testing](/burp/application-security-testing/dast) (DAST) tools barely scratch the surface, leaving critical blind spots in many enterprise environments. Vendors often claim to offer comprehensive desync detection, but what does that really mean?

Most DAST tools depend on pre-canned payloads, targeting simple desync vectors like CL.TE or TE.CL, or worse, merely fingerprinting specific CVEs. These simplistic methods primarily identify common, well-known attack scenarios but utterly fail to detect the more complex or novel desync variations that could still be wide open to exploitation by attackers.

[Burp Suite DAST](/burp/dast) changes this entirely. Developed in close collaboration with [James "albinowax" Kettle](https://portswigger.net/research/james-kettle), the leading expert in request smuggling research, Burp Suite DAST is currently the only enterprise-grade solution capable of comprehensive, scalable HTTP request smuggling detection.

## Why Other DAST Tools Fall Short

Many enterprise-grade DAST solutions, from open-source scanners to heavyweight AST platforms, claim to offer automated HTTP request smuggling detection. Yet our analysis reveals some common shortcomings:

* **Highly brittle, pre-canned detection methods:** Often rely on basic regexes detecting obvious header obfuscation or spraying well-known exploits to identify vulnerabilities.
* **Tunnel vision for CVEs:** Detection typically targets specific platform versions or known misconfigurations, not underlying flaws, resulting in massive blindspots to the nuances of different server or proxy implementations.
* **Blind to HTTP downgrade vectors:** Rarely testing HTTP/2, and even fewer handling downgrade scenarios between protocols.

Some tools simply test a single, request smuggling scenario, look for a timeout or basic error, then stop. This approach is a blunt instrument that simply fails against today's evolving threats.

## Burp Suite DAST: Request Smuggling Detection Reinvented, for the Scale You Need

Burp Suite DAST doesn't rely on simplistic signatures. Instead, it probes deeper into desync primitives—the foundational parsing discrepancies between front-end and back-end servers that enable request smuggling in the first place.

This method:

* Identifies vulnerabilities by performing automated analysis at the root-cause level, not just superficial symptoms.
* Provides clues about the presence of as-yet-unknown attack vectors.
* Significantly reduces false positives and false negatives caused by fundamentally flawed mitigation attempts.

This revolutionary approach, driven by PortSwigger's groundbreaking research, represents a complete shift in detection strategy. Instead of merely verifying known payloads, Burp Suite DAST automatically analyses parsing discrepancies unique to your infrastructure, identifying the root cause of desync vulnerabilities. This approach enables significantly more reliable detection of dangerous parsing behavior and potential request smuggling vulnerabilities that may have remained undetected in your systems for years.

## Backed by the World's Leading Authority on Desync Attacks

James Kettle, PortSwigger's Director of Research, [introduced HTTP request smuggling to the broader security community in 2019](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn) and continues to redefine the landscape. His [latest 2025 Black Hat and DEF CON talks](https://portswigger.net/research/http1-must-die) introduced entirely new classes of desync attacks and advanced detection techniques. As Burp Suite DAST aligns directly with this cutting-edge research, its smuggling detection capabilities consistently outpace the industry.

While other tools scramble to catch up, Burp Suite DAST continuously integrates fresh detection logic in parallel with ongoing research developments, enabling you to scan your estate, at any scale, the moment new threats are revealed.

## The Only True Choice for Comprehensive Coverage

Request smuggling is an insidious threat that easily evades conventional testing. If you're tasked with securing complex web apps, especially those involving layered proxies, cloud edge networks, or mixed HTTP protocols, superficial coverage is not enough. ...