---
title: CRLF-Powered Desync Attacks: Beheading HTTP Streams
url: https://portswigger.net/research/crlf-powered-desync-attacks
source: PortSwigger Research
date: 2026-08-05
fetch_date: 2026-08-06T05:01:28.867614
---

# CRLF-Powered Desync Attacks: Beheading HTTP Streams

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

[ ]

Articles

* [Overview](/research)
* [ ]

  Core Topics

  [Black Hat](/research/black-hat)
  [XSS](/research/cross-site-scripting-research)
  [Request Smuggling](/research/request-smuggling)
  [Template Injection](/research/template-injection)
  [Top 10 Hacking Techniques](/research/top-10-web-hacking-techniques)
* [Articles](/research/articles)
* [ ]

  Meet the Researchers

  [James Kettle](/research/james-kettle)
  [Gareth Heyes](/research/gareth-heyes)
  [Zakhar Fedotkin](/research/zakhar-fedotkin)
  [Tom Stacey](/research/tom-stacey)
* [Talks](/research/talks)
* [RSS](/research/rss)

# CRLF-Powered Desync Attacks: Beheading HTTP Streams

[ ]

![Tom Stacey](/content/images/profiles/callout_tom_stacey_114px.png)

### [Tom Stacey](/research/tom-stacey)

Researcher

[@t0xodile](https://twitter.com/t0xodile)

* **Published:** Wednesday, 5 August 2026 at 23:30 UTC
* **Updated:** Wednesday, 5 August 2026 at 23:30 UTC

## Abstract

In this paper we’ll show that HTTP Header Injection is severely underestimated. Forget open redirects or [Cross-Site Scripting](/web-security/cross-site-scripting) and instead, embrace the catastrophic potential of the CRLF-Powered Desync Worm.

We’ll begin by teaching you how to take a simple header injection primitive and transform it into a full-blown desync worm. Next, we’ll introduce novel methods to detect and exploit IP and connection-locked desyncs which prevent cross-network exploitation by shifting the desync’s execution into the victim's browser to generate an XSS out of thin air and steal HTTPOnly cookies.

Along the way, we’ll help you avoid accidental desync disasters like logging every active user of your target into your own account causing your shopping cart to be overwritten with random users’ items on every refresh.

## Collaboration

This paper was co-authored with [Tobia Righi](https://x.com/m4st3rspl1nt3r) from [TurtleSec](https://turtlesec.io/). Over the last year, we've collaborated on this research in order to ensure that every single technique was pushed to its absolute limit. This went rather well, and we ended up co-presenting the results at BHUSA and DEFCON. You can read his own version of the paper on [TurtleSec’s blog](https://turtlesec.io/blog/posts/crlf-powered-desync-attacks/).

* [Research Origins](#research-origins)
* [HTTP Request Smuggling](#http-request-smuggling)
* [Request Header Injection](#request-header-injection)
* [Detecting Request Header Injection](#detecting-request-header-injection)
* [HTTP Request Splitting](#http-request-splitting)

+ [Response Queue Poisoning via Request Splitting](#response-queue-poisoning-via-request-splitting)
+ [RQP Inside the Infrastructure of a CDN](#rqp-inside-the-infrastructure-of-a-cdn)
+ [Header Injection via Custom Upstream Header](#header-injection-via-custom-upstream-header)
+ [Header Injection via Non-Path Insertion Points](#header-injection-via-non-path-insertion-points)
+ [AI-Generated Detection Techniques](#ai-generated-detection-techniques)

* [CRLF-Powered CL.TE Desync Attacks](#crlf-powered-cl.te-desync-attacks)

+ [The Desync Disaster](#the-desync-disaster)
+ [The Nested Response Mystery](#the-nested-response-mystery)
+ [Cache Poisoning & AI-Generated HEAD Gadget](#cache-poisoning-and-ai-generated-head-gadget)

* [Browser-Powered CRLF Desync Attacks](#browser-powered-crlf-desync-attacks)

+ [CRLF-Powered Desync Worms](#crlf-powered-desync-worms)
+ [HTTP Request Tunnelling](#http-request-tunnelling)

- [Bypassing Blind Request Tunnelling](#bypassing-blind-request-tunnelling)
- [Bypassing Access Controls via Request Tunnelling](#bypassing-access-controls-via-request-tunnelling)

+ [Browser-Powered Connection-Locked Desyncs](#browser-powered-connection-locked-desyncs)

- [Browser-Powered 0.CL](#browser-powered-0.cl)

+ [Browser-Powered IP-Locked Desyncs](#browser-powered-ip-locked-desyncs)

- [Browser-Powered Request Splitting - HEAD + Range](#browser-powered-request-splitting-head-range)
- [Browser-Powered Request Splitting - Stealing HTTPOnly Cookies](#browser-powered-request-splitting---stealing-httponly-cookies)

* [Bypassing Response Header Removal](#bypassing-response-header-removal)
* [Response Header Injection](#response-header-injection)

+ [Cookie Tossing - TikTok](#cookie-tossing-tiktok)
+ [XSS on a Redirect](#xss-on-a-redirect-response)
+ [Reverse Desync Attacks](#reverse-desync-attacks)

* [Defence](#defence)
* [Tooling](#tooling)
* [Further Research](#further-research)
* [Key Takeaways](#key-takeaways)
* [Conclusion](#conclusion)

## Research Origins

Around 1 year ago, we came across [this post on Bluesky](https://bsky.app/profile/aroly.bsky.social/post/3lq7obuqcrk2m) which mentioned an attack technique we’d heard of, but never come across in the wild. This post bothered us, as it claimed the attack was “not that uncommon” in spite of our failure to ever find it. On top of this, we knew of at le...