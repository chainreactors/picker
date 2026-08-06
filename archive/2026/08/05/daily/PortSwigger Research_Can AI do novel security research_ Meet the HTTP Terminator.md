---
title: Can AI do novel security research? Meet the HTTP Terminator
url: https://portswigger.net/research/http-terminator
source: PortSwigger Research
date: 2026-08-05
fetch_date: 2026-08-06T05:01:29.768217
---

# Can AI do novel security research? Meet the HTTP Terminator

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

# Can AI do novel security research? Meet the HTTP Terminator

[ ]

![James Kettle](/content/images/profiles/callout_james_kettle_112px.png)

### [James Kettle](/research/james-kettle)

Director of Research

[@albinowax](https://twitter.com/albinowax)

* **Published:** Wednesday, 5 August 2026 at 19:30 UTC
* **Updated:** Wednesday, 5 August 2026 at 19:33 UTC

Abstract

We all know AI can find bugs. After a decade of research, I asked a harder question: can an autonomous system invent new attack techniques, and use them to hack live websites at scale? Building this sounded like a bad idea, so I did it.

It worked - I'll share an arsenal of new HTTP desync triggers, gadgets, and exploits that compromised banks, security solutions, and government infrastructure. Then I'll trace each discovery chain back through the HTTP Terminator, showing how to turn your personal expertise into an autonomous weapon - and the dark arts required to make it lethal.

I'll also share discoveries from beyond the autonomy horizon - some only reachable with a tight human/AI research loop, and others beyond AI's reach entirely. These include a powerful undisclosed recon technique, and anomalies that hint at new attack classes offering alternative paths to critical impact. I'll analyze the discovery process, sharing detailed experiments that probe the boundaries of what AI can and can't discover.

You'll leave with new exploits from desync triggers to undisclosed attack classes, and a blueprint for turning your instincts into an autonomous research cascade. And yes, I'll open-source the HTTP Terminator.

This whitepaper is also available as a [printable PDF](https://portswigger.net/kb/papers/gkaicuremal/http-terminator.pdf). If you've seen the size of the scrollbar and you're about to ask for an AI summary, you may prefer to read the [executive summary](https://portswigger.net/kb/papers/gkaicuremal/http-terminator-executive-summary.pdf) instead. This research was presented at [Black Hat USA 2026](https://blackhat.com/us-26/briefings/schedule/#can-ai-do-novel-security-research-meet-the-http-terminator-51894) and [DEF CON 34](https://defcon.org/html/defcon-34/dc-34-speakers.html#content_66581), and this page will be updated with the recording once it's available - follow PortSwigger Research on [X](https://x.com/portswiggerres), [LinkedIn](https://www.linkedin.com/showcase/portswigger-research/posts/?feedView=all&viewAsMember=true) or [RSS](https://portswigger.net/research/rss) to get notified when it lands.

## Contents

* [Introduction](#introduction)

+ [Defining novel HTTP desync research](#defining-novel-http-desync-research)
+ [HTTP Terminator Design](#http-terminator-design)

* [Ideation](#ideation)

+ [The technique rediscovery test](#the-technique-rediscovery-test)
+ [Scaling ideation with micro-inspiration](#scaling-ideation-with-micro-inspiration)

* [Evaluation](#evaluation)

+ [The core evaluation primitive](#the-core-evaluation-primitive)
+ [Evaluation case-study](#evaluation-case-study)
+ [Novel desync triggers](#novel-desync-triggers)

* [Weaponization](#weaponization)

+ [Autonomous RQP](#autonomous-rqp)
+ [Turning the environment into the weapon](#turning-the-environment-into-the-weapon)
+ [Making iteration viable](#making-iteration-viable)
+ [The stacked-response problem](#the-stacked-response-problem)
+ [The dangling-byte technique](#the-dangling-byte-technique)

* [Cascade](#cascade)

+ [Anomaly detection cascade](#anomaly-detection-cascade)
+ [Chasing an autonomous cascade](#chasing-an-autonomous-cascade)
+ [Status-line Injection](#status-line-injection)
+ [Range Cache Poisoning](#range-cache-poisoning)
+ [Shared-Parser Confusion](#shared-parser-confusion)
+ [Scanning for inspiration](#scanning-for-inspiration)

* [Conclusion](#conclusion)

+ [The blueprint](#the-blueprint)
+ [Tool releases](#tool-releases)
+ [Defense](#defense)
+ [Takeaways](#takeaways)

## Introduction

Automation is often focused on efficiency but I believe that when it's approached just right, automation can enable outcomes that were previously impossible. This research is about chasing that promise of something more.

The primary objective of this project was to discover the new frontier of automation-driven security research. I've been practicing automation-driven researc...