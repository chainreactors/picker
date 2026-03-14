---
title: HTTP/1.1 Must Die: Conquering the 0.CL Challenge
url: https://portswigger.net/blog/http-1-1-must-die-conquering-the-0-cl-challenge
source: PortSwigger Blog
date: 2026-03-13
fetch_date: 2026-03-14T04:12:13.926749
---

# HTTP/1.1 Must Die: Conquering the 0.CL Challenge

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

# HTTP/1.1 Must Die: Conquering the 0.CL Challenge

[ ]

Fran Hutchings |
13 March 2026 at 09:21 UTC

![](/cms/images/e2/91/8514-article-blackhat_blog_header.png)

*Note: This is a guest post by pentester Julen Garrido Estévez (@b3xal).*

* [**1. Acknowledgements**](#acknowledgements)
* [**2. Intro**](#intro)
* [**3. Required tools**](#required-tools)
* [**4. Strategy to solve/exploit the lab**](#strategy-to-solve-exploit-the-lab)
* [**5. Detecting 0.CL**](#detecting-0cl)
  + [**5.1. Practical confirmation of 0.CL: “Request A” + “Request B”**](#practical-confirmation-of-0cl-request-a-request-b)
* [**6. Exploitation of 0.CL**](#exploitation-of-0cl)
* [**6.1 Solution A. Ignoring added headers**](#solution-a-ignoring-added-headers)
  + [**Idea**](#idea)
  + [**Variant A1: Using the intentional XSS**](#variant-a1-using-the-intentional-xss)
  + [**Variant A2: forcing XSS with the HEAD technique**](#variant-a2-forcing-xss-with-the-head-technique)
    - [**Integrating the technique into the CL.0**](#integrating-the-technique-into-the-cl0)
* [**6.2 Solution B — Calculating the offset of the injected headers**](#solution-b-calculating-the-offset-of-the-injected-headers)
  + [**Accounting for the Offset**](#accounting-for-the-offset)
  + [**Variant B1: Using the intentional XSS**](#variant-b1-using-the-intentional-xss)
  + [**Variant B2: forcing XSS with the HEAD technique**](#variant-b2-forcing-xss-with-the-head-technique)
* [**Conclusion**](#conclusion)

## 1. Acknowledgements

This article is based on the outstanding work of James Kettle ([Research HTTP/1.1 must die](https://portswigger.net/research/http1-must-die)). From his findings, we joined the Desync Endgame. We break down the 0.CL technique into a technical analysis and a complete walkthrough of the official PortSwigger lab. Any subsequent explanation is an attempt to learn from and teach his research in order to properly defend infrastructures.

## 2. Intro

0.CL is a variant of [HTTP request smuggling](/web-security/request-smuggling) in which the front-end interprets “Content-Length: 0” (or treats it as implicitly 0), while the back-end may interpret the following stream of bytes differently.

That discrepancy allows the first request to absorb bytes from the next request processed by the back-end. In the PortSwigger lab this allows controlling the next request and thus trigger an alert().

For a theoretical, low-level treatment, consult the whitepaper "HTTP/1.1 Must Die" by James Kettle.

## 3. Required tools

* [Burp Suite](https://portswigger.net/burp/documentation/desktop/getting-started/download-and-install) (Professional / Community).

* [HTTP Request Smuggler](https://portswigger.net/bappstore/aaaa60ef945341e8a450217a54a11646): Probes and specific detection of CL/TE/0.CL discrepancies.

* [Turbo Intruder](https://portswigger.net/bappstore/9abaa233088242e8be252cd4ff534988): Raw/pipelined sending (Request A + Request B) with fine control of framing and timing; useful for brute-forcing padding/offset.

## 4. Strategy to solve/exploit the lab

We will cover two main approaches and within each two variants, totalling 4 PoCs. The techniques are organised to facilitate progressive learning.

A) Ignore the headers injected by the frontend: creation of a request that does not depend on the additional content that may be added. It is the easiest and most direct way to understand the mechanics.

* A1: Using the lab's intentional [XSS](/web-security/cross-site-scripting).
* A2: Force an XSS using the “HEAD” technique.

B) Calculate the offset (byte-offset) of the added headers and adjust the payload so that, after the additional headers, the framing is aligned with what the back-end expects.

* B1: Same intentional XSS + calculated offset.
* B2: Force an XSS using the “HEAD” technique + calculated offset.

Important security note: all scripts and payloads that I include are intended exclusively for the PortSwigger lab and controlled environments. Do not use them against systems without authorisation. The vectors, scripts and payloads presented are based on the official PortSwigger examples for this lab.

## 5. Detecting 0.CL

Before attempting any exploitation, the first step is to confirm a discrepancy between the front-end and the back-end: what the load balancer/proxy/WAF/frontend interprets as the end of a request does not match what the back-end interprets. Without that difference there is no 0.CL to exploit.

You can try manual manipulations (spaces, tabs, line breaks in headers), but these are usually slow and not exhaustive.

Instead we run the “Parser discrepancy scan” from the HTTP Request Smuggler extension against the target request: the extension tests combinations and permutations of headers and often finds indications that manual analysis overlooks.

![](/cms/images/87/3a/1cb1-article-image30.png)

T...