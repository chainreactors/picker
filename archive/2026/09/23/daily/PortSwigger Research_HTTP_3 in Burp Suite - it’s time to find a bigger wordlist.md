---
title: HTTP/3 in Burp Suite - it’s time to find a bigger wordlist
url: https://portswigger.net/research/http3-in-burp-suite
source: PortSwigger Research
date: 2026-09-23
fetch_date: 2026-09-24T07:06:42.036680
---

# HTTP/3 in Burp Suite - it’s time to find a bigger wordlist

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

# HTTP/3 in Burp Suite - it’s time to find a bigger wordlist

[ ]

![Tom Stacey](/content/images/profiles/callout_tom_stacey_114px.png)

### [Tom Stacey](/research/tom-stacey)

Researcher

[@t0xodile](https://twitter.com/t0xodile)

* **Published:** Wednesday, 23 September 2026 at 14:00 UTC
* **Updated:** Wednesday, 23 September 2026 at 15:27 UTC

![100000 requests per second over HTTP3](/cms/images/26/76/fe7d-article-http3_in_burp_suite_blog-article.png)

How many bugs have you missed because you didn’t send quite enough HTTP requests?

Turbo Intruder now supports HTTP/3, can comfortably exceed 100,000 requests per second over Wi-Fi, and auto-tunes for maximum performance. With our new HTTP/3 Adapter plugin, Burp Suite now supports HTTP/3 too.

Read on to learn how to use this new toolkit to:

* Achieve maximum speed
* Exploit HTTP/3 [Race conditions](/web-security/race-conditions)
* Exploit HTTP/3 downgrading
* Test HTTP/3 only targets

[1 million requests in 10 seconds over Wi-Fi](/cms/videos/a4/aa/06fee33d9850-1-million-in-10-seconds.mp4)

## How to achieve maximum speed in Turbo Intruder

In [Embracing the Billion Request Attack](https://portswigger.net/research/turbo-intruder-embracing-the-billion-request-attack) we were able to hit 30,000 requests per second (RPS) over HTTP/1.1. From my laptop while using the `HTTP3` engine, I was able to hit 100,000 RPS to a remote host over Wi-Fi.

When fuzzing over any protocol, you’ll first want to minimise the size of your request and response (using the HEAD method, or Range header).

`GET / HTTP/1.1
Range: bytes=-1 //Only return the last byte`
`HTTP/1.1 206 Partial Content
Content-Range: bytes 9999-9999/10000
Content-Length: 1
>`
> The `Host` header can be skipped when using the `HTTP3` engine because the `:authority` pseudo header is implied by the target.

Next, you’ll want to adjust the engine’s configuration. If you’re using [Burp Suite Professional](/burp/pro), you can simply swap to the `AUTO` engine, which will automatically select the highest HTTP version available and then dynamically tune the required settings as your attack runs. This is particularly powerful for long-running attacks, where the network state may degrade or improve over time.

> HTTP/1.1's pipelining feature is not supported in the `AUTO` engine. You may be able to achieve higher RPS over HTTP/1.1 when using the `THREADED` engine if you enable pipelining manually.

> If you’re attempting a desync attack, `AUTO` is not recommended. Instead use the `BURP` engine which uses HTTP/1.1 with connection reuse disabled.

If you’re using the Community Edition, you’ll need to configure each setting manually depending on the engine. For each setting you want to increase its value until the RPS counter plateaus, or you start seeing failures. The only exception to this, is when using the `THREADED` engine’s `pipeline` option, which should be set to `True` if the server supports it.

Available tuning options:

| Engine | Tuning Options |
| --- | --- |
| THREADED | concurrentConnections requestsPerConnection pipeline=True |
| BURP2 | concurrentConnections |
| HTTP3 | concurrentConnections |

If you require more speed, run the attack from a box in the cloud that’s hosted in the same region as your target to push the RPS even higher. My best result so far was ~180,000 RPS.

## HTTP/3 race condition techniques

To complement the HTTP3 engine, you can now try out two new race condition techniques. The Single Datagram Attack from [QUIC-er Races: HTTP/3 won’t save you from TOCTOU vulnerabilities](https://link.springer.com/article/10.1007/s10207-026-01258-6) and Server-Side Race Orchestration via the QPACK Blocked Streams technique from [Chaos by Design: The Death of Stochastic Race Conditions in HTTP/3](https://i.blackhat.com/BH-USA-26/Presentations/BHUS26-Chatzoglou-Chaos-by-Design-Slides.pdf). These techniques will give you better groupings than the already blazingly fast [Single-Packet attack](https://portswigger.net/research/the-single-packet-attack-making-remote-race-conditions-local) if the target supports HTTP/3 so you can hit smaller race windows.

Both are only accessible when using the HTTP3 engine and are built into the existing gate system. Turbo Intruder will select the race technique automatically and it only uses the QPA...