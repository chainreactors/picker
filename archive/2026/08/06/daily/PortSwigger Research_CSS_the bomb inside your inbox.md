---
title: CSS:the bomb inside your inbox
url: https://portswigger.net/research/css-the-bomb-inside-your-inbox
source: PortSwigger Research
date: 2026-08-06
fetch_date: 2026-08-07T04:26:13.591632
---

# CSS:the bomb inside your inbox

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

# CSS:the bomb inside your inbox

[ ]

![Gareth Heyes](/content/images/profiles/callout_gareth_heyes_114px.png)

### [Gareth Heyes](/research/gareth-heyes)

Researcher

[@garethheyes](https://twitter.com/garethheyes)

* **Published:** Thursday, 6 August 2026 at 22:00 UTC
* **Updated:** Thursday, 6 August 2026 at 22:00 UTC

[Gareth Heyes](https://portswigger.net/research/gareth-heyes) - gareth.heyes@portswigger.net - [@garethheyes](https://x.com/garethheyes)

**It's quite common for webmail clients to render untrusted CSS in a trusted UI. They attempt to make this safe using CSS sanitization. In this paper I'm going to show you how to break out of trust boundaries, exfiltrate tokens, compromise 3rd party websites and even steal passwords.**

## Table of contents

* [Introduction](#introduction)
* [Abusing allowed HTML/CSS](#abusing-allowed-html-css)
  + [Abusing HTML labels to perform UI actions](#abusing-html-labels-to-perform-ui-actions)
  + [Controlling AI browsers via email](#controlling-ai-browsers-via-email)
  + [Account takeover from pasting into a draft email](#account-takeover-from-pasting-into-a-draft-email)
  + [Exfiltrating tokens when CSP is blocking all external resources](#exfiltrating-tokens-when-csp-is-blocking-all-external-resources)
* [Bypassing CSS sanitization](#bypassing-css-sanitization)
  + [Making external requests](#making-external-requests)
  + [Syntax quirks](#syntax-quirks)
  + [Image proxy bypasses](#image-proxy-bypasses)
    - [Tracking if email is viewed in Fastmail](#tracking-if-email-is-viewed-in-fastmail)
    - [Displaying your IP address in ProtonMail](#displaying-your-ip-address-in-protonmail)
    - [Tracking if email is viewed in Gmail](#tracking-if-email-is-viewed-in-gmail)
  + [Combining an image proxy bypass with indirect prompt injection](#combining-an-image-proxy-bypass-with-indirect-prompt-injection)
  + [CSS mutation in Fastmail](#css-mutation-in-fastmail)
* [Exploitation with CSS](#exploitation-with-css)
  + [Defacing Outlook using CSS gadgets](#defacing-outlook-using-css-gadgets)
  + [CSS hotwiring in Fastmail](#css-hotwiring-in-fastmail)
  + [Stealing passwords](#stealing-passwords)
* [Defences](#defences)
* [Future attacks](#future-attacks)
  + [HTML only keylogger](#html-only-keylogger)
  + [Chrome real time keylogger](#chrome-real-time-keylogger)
* [References](#references)
* [Materials](#materials)

## Introduction

Webmail has been around for decades and it's always had to solve a very difficult problem of taking untrusted HTML and displaying it to the user in a safe way. This is made even more challenging by each web standard evolving at a relentless pace. To solve this problem webmail uses sanitizers, they attempt to take the HTML provided and restrict it so that it can be displayed to users safely. Trouble is you can create discrepancies between what the sanitizer thinks is safe and what the browser actually renders. Some webmail clients go a step further by letting the browser parse the HTML and CSS first, then filtering the browser's interpreted output rather than the original source. Yet even this can be mutated into something malicious.

Over the last few months I've been looking at webmail clients like Yahoo Mail, AOL Mail, Fastmail, ProtonMail, GMail and Outlook. In search of discrepancies in their parsers and weak points in their sanitizers to produce a range of novel techniques to help exploit them.

## Abusing allowed HTML/CSS

In this section I looked at the various "allow listed" CSS properties and HTML. With the goal of abusing them to spoof UI actions, control browsers, take over accounts or steal tokens. I targeted Fastmail, OpenAI's Atlas, Firefox, AOL Mail, Yahoo Mail and Outlook.

### Abusing HTML labels to perform UI actions

HTML labels are an often overlooked element, using label tags you can target specific form elements that have an id attribute by using the label's for attribute. This works on any form element and you inherit the click action attached to the element. They are often missed by HTML sanitizers and I found at least 3 webmail clients that were vulnerable to this. I found a real bug in Outlook which would enable me to control Outlook's UI from an email message.

`<label for="RibbonModeToggle">
Click me first</label>
<br><br>
<label for="548">
Click ...