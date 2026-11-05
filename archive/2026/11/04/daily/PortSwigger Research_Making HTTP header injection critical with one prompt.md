---
title: Making HTTP header injection critical with one prompt
url: https://portswigger.net/research/making-http-header-injection-critical-with-one-prompt
source: PortSwigger Research
date: 2026-11-04
fetch_date: 2026-11-05T08:43:38.612314
---

# Making HTTP header injection critical with one prompt

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
  [Alex Craig](/research/alex-craig)
* [Talks](/research/talks)
* [RSS](/research/rss)

# Making HTTP header injection critical with one prompt

[ ]

![Tom Stacey](/content/images/profiles/callout_tom_stacey_114px.png)

### [Tom Stacey](/research/tom-stacey)

Researcher

[@t0xodile](https://twitter.com/t0xodile)

* **Published:** Wednesday, 4 November 2026 at 15:12 UTC
* **Updated:** Wednesday, 4 November 2026 at 15:12 UTC

You can now escalate HTTP header injection to a CRLF-Powered Desync and exploit it to serve random users a redirect to your collaborator, in a single prompt. We’ve just introduced a new scan check for HTTP Request Header Injection and distilled [CRLF-Powered Desync Attacks: Beheading HTTP Stream’s](https://portswigger.net/research/crlf-powered-desync-attacks) exploitation methodology into Burp AT. Watch it in action below:

[Video tags are not supported by your browser.](/cms/videos/4c/5c/dab146c4840f-crlf-powered-desync-skill.mp4)

[HTTP request smuggling](/web-security/request-smuggling) attacks are devastating. To make matters worse, they’re so widespread and so complex that we’ve released [six](https://portswigger.net/research/request-smuggling) BlackHat USA research presentations about them. That’s a lot of new hacking techniques to consume if you don’t want to miss critical vulnerabilities in your engagements.

To help testers discover more cutting-edge critical vulnerabilities, we’re distilling the PortSwigger Research team’s knowledge into Burp AT skills. This allows it to autonomously perform our research grade methodology in the background, all while you continue your own manual testing.

## Our CRLF-Powered Desync methodology

To illustrate what we mean, here are the steps Burp AT is taking for you in the background. The skill expects a HTTP request header injection issue from burp, and uses it to run several phases, each of which is a step in the methodology we used during our research:

#### Phase 1 - Identify the upstream injection location

Just because your insertion point is the path, doesn’t mean that your injected header ends up in the path upstream. We encountered several cases where the path was re-written to a custom header upstream, meaning that to achieve request splitting, we needed to identify if the custom header occurred before or after the existing host header.

For example, if the following produces normal looking status code:

`GET /%0d%0a%0d%0a HTTP/1.1`

But the adding a host header like so triggers a 400:

`GET /%0d%0aHost:%20x%0d%0a%0d%0a HTTP/1.1`

Upstream request:

`GET / HTTP/1.1
Host: example.com
X-Original-path: /
Host: x`

Then we can be fairly certain that our injection is occurring inside of a custom header that appears after the upstream request’s host header.

Note: the skill and scan check both support any insertion point, not just the path

#### Phase 2 - Validate the desync via request splitting

Next, we need to build our request splitting payload and prove that we can achieve a desync. To do this, we use the structure provided by phase 1 to build a request splitting payload with prefixes like so:

`GET /%0d%0a%0d%0aGET%20/%20HTTP/13.37%0d%0aHost:%20example.com
%0d%0aContent-Length:%20150%0d%0a%0d%0a HTTP/1.1`
`GET /%0d%0a%0d%0aTRACE%20/%20HTTP/1.1%0d%0aHost:%20example.com
%0d%0aContent-Length:%20150%0d%0a%0d%0a HTTP/1.1`

The skill will fuzz several different prefix payloads in order to try and produce unique status codes. Once it has collected 2 or 3 we know our prefixes are modifying our requests upstream and it’ll move into exploitation.

#### Phase 3 - Find an exploit gadget

This phase will launch a mini-crawl against the domain you are targeting, in an attempt to find open redirects that can be induced via the Host header, the X-Forwarded-Host header or an absolute URL.

#### Phase 4 - Exploit the target

Assuming we found a gadget in phase 3, we can now build our exploit by combining our phase 2 request structure with our phase 3 gadget. For example, if phase 3 identified that a request towards `/assets` redirected to `/assets/` and used the host header to determine the location of said redirect, phase 4 attempts the following exploit:

`GET /%0d%0a%0d%0aGET%20/assets%20HTTP/1.1%0d%0aHost:%20collaborator.net%0d%0a
Content-Length:%20150%0d%0a%0d%0a HTTP/1.1`

If repeatedly sending this request over different co...