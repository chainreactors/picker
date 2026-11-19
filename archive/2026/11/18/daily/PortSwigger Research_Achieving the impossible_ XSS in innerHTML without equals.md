---
title: Achieving the impossible: XSS in innerHTML without equals
url: https://portswigger.net/research/achieving-the-impossible-xss-in-innerhtml-without-equals
source: PortSwigger Research
date: 2026-11-18
fetch_date: 2026-11-19T09:46:00.673234
---

# Achieving the impossible: XSS in innerHTML without equals

[Login](/users)

[ ]

Products    Solutions   [Research](/research) [Academy](/web-security)  Support    Company

[Customers](/customers) [About](/about) [Blog](/blog) [Careers](/careers) [Legal](/legal) [Contact](/contact) [Resellers](/support/reseller-faqs)

[My account](/users/youraccount) [Customers](/customers) [About](/about) [Blog](/blog) [Careers](/careers) [Legal](/legal) [Contact](/contact) [Resellers](/support/reseller-faqs)

[![Burp AT](/_ps-components/0.3.0/fragments/meganav/burp-at.svg) **Burp AT** Agentic AI that extends human-led pentesting.](/burp/burp-at)   [![Burp Suite DAST](/_ps-components/0.3.0/fragments/meganav/enterprise.svg) **Burp Suite DAST** The enterprise-enabled dynamic web vulnerability scanner.](/burp/dast)   [![Burp Suite Professional](/_ps-components/0.3.0/fragments/meganav/professional.svg) **Burp Suite Professional** The world's #1 web penetration testing toolkit.](/burp/pro)   [![Burp Suite Community Edition](/_ps-components/0.3.0/fragments/meganav/community.svg) **Burp Suite Community Edition** The best manual tools to start web security testing.](/burp/communitydownload)  [View all product editions](/burp)

[**Burp Scanner**

Burp Suite's web vulnerability scanner

![Burp Suite's web vulnerability scanner'](/_ps-components/0.3.0/fragments/meganav/burp-suite-scanner.jpg)](/burp/vulnerability-scanner)

[**Attack surface visibility** Improve security posture, prioritize manual testing, free up time.](/solutions/attack-surface-visibility)   [**CI-driven scanning** More proactive security - find and fix vulnerabilities earlier.](/solutions/ci-driven-scanning)   [**Application security testing** See how our software enables the world to secure the web.](/solutions)   [**DevSecOps** Catch critical bugs; ship more secure software, more quickly.](/solutions/devsecops)   [**Penetration testing** Accelerate penetration testing - find more bugs, more quickly.](/solutions/penetration-testing)   [**Automated scanning** Scale dynamic scanning. Reduce risk. Save time/money.](/solutions/automated-security-testing)   [**Bug bounty hunting** Level up your hacking and earn more bug bounties.](/solutions/bug-bounty-hunting)   [**Compliance** Enhance security monitoring to comply with confidence.](/solutions/compliance)

[View all solutions](/solutions)

[**Product comparison**

What's the difference between Pro and DAST?

![Burp Suite Professional vs Burp Suite DAST](/_ps-components/0.3.0/fragments/meganav/burp-suite.jpg)](/burp/dast/resources/dast-vs-professional)

[**Support Center** Get help and advice from our experts on all things Burp.](/support)   [**Documentation** Tutorials and guides for Burp Suite.](/burp/documentation)   [**Get Started - Professional** Get started with Burp Suite Professional.](/burp/documentation/desktop/getting-started)   [**Get Started - DAST** Get started with Burp Suite DAST.](/burp/documentation/dast/setup)   [**Downloads** Download the latest version of Burp Suite.](/burp/releases)

[Visit the Support Center](/support)

[**Downloads**

Download the latest version of Burp Suite.

![The latest version of Burp Suite software for download](/_ps-components/0.3.0/fragments/meganav/latest-burp-suite-software-download.jpg)](/burp/releases)

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

# Achieving the impossible: XSS in innerHTML without equals

[ ]

![Gareth Heyes](/content/images/profiles/callout_gareth_heyes_114px.png)

### [Gareth Heyes](/research/gareth-heyes)

Researcher

[@garethheyes](https://twitter.com/garethheyes)

* **Published:** Wednesday, 18 November 2026 at 14:39 UTC
* **Updated:** Wednesday, 18 November 2026 at 14:39 UTC

![Shows a man surrounded by lasers reaching for alert(1)](/cms/images/7e/88/96af-article-impossible-lab-article.png)

## Introduction

I'm delighted to introduce [Masato Kinugawa](https://x.com/kinugawamasato) as a guest web security researcher on the PortSwigger research channel. Masato is a well known web security expert who has found countless high impact bugs and amazingly he solved one of our "impossible" labs. We took this chance to invite him to do a guest post, over to you Masato...

In 2020, Gareth Heyes compiled a list of
[impossible labs](https://portswigger.net/research/documenting-the-impossible-unexploitable-xss-labs), covering various injection scenarios where JavaScript execution was considered impossible.

One of the challenges on this list, "`innerHTML` context but no equals allowed", asks whether arbitrary JavaScript can be executed when an injection occurs in `innerHTML` but the equals sign is not allowed. This challenge had long been considered impossible.

Recently, I discovered a way to solve this challenge using a newly introduced HTML element. Here is the payload:

`` <body>
<script>
document.body.innerHTML=`
<select>
<selectedcontent></selectedcontent>
<option>
<svg>
<script>alert(1)<\/script>`;
</script> ``

Although this payload no longer works in Chrome due to a behavior change introduced in Chrome 153, I have confirmed that it still works in Safari 27.2, the latest version at the time of writing.

In this article, I'll share the story behind this discovery and explore the technical details behind it.

## The starting point

In May 2026, a very interesting
[DOMPurify bypass](https://github.com/cure53/DOMPurify/security/advisories/GHSA-87xg-pxx2-7hvx) discovered by
[Kabir Acharya](https://x.com/Kabir4charya) was disclosed.

What surprised me about this technique was its use of the
`<selectedcontent>` element, which was relatively recently introduced in Chrome and Safari and which I had never seen used in an [XSS](/web-security/cross-site-scripting) vector before. For details of the bypass, see
["Attack Classes & Bypass History" in the DOMPurify wiki](https://github.com/cure53/DOMPurify/wiki/Attack-Classes-%26-Bypass-History#18-engine-deferred-mutation-selectedcontent).

Despite its seemingly harmless name, the
`<selectedcontent>` element has a unique capability.

Let's take a look at the following HTML:

`<select>
<button>
<selectedcontent></selectedcontent>
</button>
<option><b>option 1</b></option>
<option selected><b>option 2</b></option>
</select>`

When this HTML is placed on a page, inspecting the resulting DOM using
`innerHTML` reveals the following:

`<select>
<button>
<selectedcontent><b>option 2</b></selectedcontent>
</button>
<option><b>option 1</b></option>
<option selected=""><b>option 2</b></option>
</select>`

Surprisingly, the contents of option 2 have been copied into
`<selectedcontent>`, including the HTML elements.

This element has the ability to clone the child nodes of the currently selected
`<option>` element. In this example, option 2 is selected by default because it has the
`selected` attribute, so its contents are cloned.

Previously, no HTML element could perform this kind of cloning operation on its own without executing JavaScript. Inspired by Kabir's discovery, I wondered whether this behavior could make other previously impossible things possible, so I began investigating.

## Building an XSS vector

Before investigating the
`innerHTML` case, I discovered that JavaScript could be executed through the following HTML:

`<select>
<button>
<selectedcontent></selectedcontent>
</button>
<option>
<script>alert(1)`

In this example, the HTML document ends immediately after `<script>alert(1)`. When this HTML is opened in Chrome or Safari,...