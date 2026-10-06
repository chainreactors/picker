---
title: Smashing the token limit with overlapping fragments
url: https://portswigger.net/research/smashing-the-token-limit
source: PortSwigger Research
date: 2026-10-05
fetch_date: 2026-10-06T08:24:56.147778
---

# Smashing the token limit with overlapping fragments

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

# Smashing the token limit with overlapping fragments

[ ]

![Gareth Heyes](/content/images/profiles/callout_gareth_heyes_114px.png)

### [Gareth Heyes](/research/gareth-heyes)

Researcher

[@garethheyes](https://twitter.com/garethheyes)

* **Published:** Monday, 5 October 2026 at 15:04 UTC
* **Updated:** Tuesday, 6 October 2026 at 08:09 UTC

![Shows a ribbon stitched together](/cms/images/b6/10/923f-article-article.png)

I'm delighted to introduce [Alex](https://x.com/Alex_______C), my fellow swigger who I've collaborated with in the past with tools like [DOM Invader](https://portswigger.net/blog/introducing-dom-invader). He showed me that it's possible to exfiltrate larger tokens than demonstrated in my original "[CSS: the bomb inside your inbox](https://portswigger.net/research/css-the-bomb-inside-your-inbox)" post. Rather than bruteforcing large amounts of token characters he found that stitching together a large amount of smaller chunks can allow you to extract tokens **hundreds of characters in length**. Over to you Alex:

## How far can one stylesheet go?

When Gareth previewed [CSS: the bomb inside your inbox](https://portswigger.net/research/css-the-bomb-inside-your-inbox) I was blown away. He could steal a login token with CSS alone, without having to recursively load another stylesheet for every character. Then I watched the browser wrestle with roughly 250 MB of CSS to recover a 12-character hex token. It worked. But such a large payload for 12 characters made me think there must be a better way.

That evening I went back through his slides. Gareth had a fragment from the start, one from the end, and a way to find a matching fragment in the middle. Why stop at one piece in the middle? If I collected short pieces from *everywhere* in the link, perhaps I could join them until the whole token emerged. I pulled out my old theoretical computer science notes and started drawing the overlaps as a graph.

I set myself two challenges. First, reproduce Gareth's 12-character result with the least CSS I could manage. Then keep his original CSS budget and see how long a token I could extract. For both I calculated a version that required a single correct candidate at least 99% of the time and a more realistic one which allowed for at most five candidates at least 90% of the time. The small sheets came out at 1.33 MB and 223 KB. With Gareth's full byte budget, the answers reached 210 characters with one guess and 640 characters with up to five. Here's how I got there.

![](/cms/images/01/b6/0837-article-image1.png)

## A token is a route through fragments

Gareth’s CSS can tell us which short chunks appear in a link, but it can’t tell us where they appear. That turns out to be enough to start rebuilding the token.

Take `c2e16a1781ed`. The first few chunks are `c2e`, `2e1`, `e16` and `16a`. Each shares two characters with the next:

`c2e` → `2e1` → `e16` → `16a`

Read from left to right, they give us `c2e16a`. We can carry on in the same way until we reach the end of the token.

This was the graph theory connection I saw in Gareth’s slides. Draw `c2e` as an arrow from `c2` to `2e`. The next chunk, `2e1`, picks up at `2e` and takes us to `e1`. Following the arrows lets us build a token one character at a time. Gareth’s start and end checks tell us where that route should begin and finish.

![](/cms/images/2c/f8/a92a-article-image2.png)

The catch is that two chunks can fit together on our graph even if they came from different parts of the link. If a chunk appears twice, we still only get one report for it. So there may be several routes between the start and end. The reconstruction script has to count every token that fits, rather than stop at the first plausible one.

A longer chunk can help us check a join. Reports for `c2e` and `2e1` could come from different places; a report for `c2e1` tells us those four characters appeared together somewhere. But checking every possible four-character hex chunk takes 65,536 CSS rules, compared with 4,096 for three-character chunks. I wanted the extra certainty without making the stylesheet sixteen times bigger. But how do we tell which joins were worth checking?

## Making the questions cheaper

To test my new approach I needed a harness to prove if it worked or not. I built a test around the URL fr...