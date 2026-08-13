---
title: Can AI invent new attack techniques? New research from James Kettle and PortSwigger Research
url: https://portswigger.net/blog/can-ai-invent-new-attack-techniques-new-research-from-james-kettle-and-portswigger-research
source: PortSwigger Blog
date: 2026-08-12
fetch_date: 2026-08-13T04:03:42.278246
---

# Can AI invent new attack techniques? New research from James Kettle and PortSwigger Research

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

# Can AI invent new attack techniques? New research from James Kettle and PortSwigger Research

[ ]

Kieron Hughes |
Wednesday, 12 August 2026 at 09:04 UTC

![HTTP Terminator research](/cms/images/7a/4c/6b32-article-james_blog_header_(1).png)

We already know AI can find vulnerabilities. James Kettle, PortSwigger's Director of Research, wanted to answer a harder question: can an autonomous system invent genuinely new attack techniques?

To find out, James built the [HTTP Terminator](https://portswigger.net/research/http-terminator), an autonomous system that invents new attack techniques and uses them to hack live websites at scale. During his research, he used it to apply his own research process to push the boundaries of HTTP desync attacks, an area he has explored through four years of research and several Black Hat and DEF CON talks.

Following his presentation at Black Hat USA, James has now published the [full technical research](https://portswigger.net/research/http-terminator), alongside the HTTP Terminator source code and a blueprint that other researchers can adapt to their own work.

## Turning a research method into a system

James started by breaking down a research process that had previously been largely intuitive. The HTTP Terminator follows four broad stages: ideation, evaluation, weaponization and cascade.

It read 138 technical specifications and broke them into 15,000 fragments of inspiration. From those fragments, it generated 30,000 unique attack vectors, then tested them against live targets authorized through bug bounty programmes.

The system confirmed roughly 700 vulnerable targets and demonstrated real-world impact across government infrastructure, financial institutions and widely deployed enterprise products.

The scale of the results is striking, but the research also revealed something important about the role of the researcher.

The HTTP Terminator could run autonomously, generating and testing new ideas without James directing every step. Its strongest results, however, came when he stepped back in at the discovery cascade: the point where one finding becomes the starting point for the next hypothesis.

As [WIRED highlighted in its coverage](https://www.wired.com/story/the-most-dangerous-ai-hacking-techniques-still-have-human-input/) of the research, this is where human experience and intuition still mattered most. The system could generate more leads, pursue them faster and handle much of the repetitive work. James could focus on recognizing which unusual results were worth taking further.

Rather than removing the researcher from the process, the HTTP Terminator gave his methodology far greater reach.

## Read the full research

James's paper goes into the technical detail: how the system works, the attack techniques it uncovered, the limits he encountered and the discoveries that emerged from the combination of autonomous research and expert input.

He is also making the HTTP Terminator available as an open-source proof of concept, together with a blueprint for other researchers who want to encode their own methods and areas of expertise.

**[Read the full HTTP Terminator research](https://portswigger.net/research/http-terminator)**

## What this means for Burp AT

The HTTP Terminator is not [Burp AT](https://portswigger.net/burp/burp-at). It is a research system built to test the limits of what AI can discover.

Burp AT is designed for professional security testing. It combines agentic reasoning with Burp's specialist tools, live project context, visible evidence and controls over what the agent is allowed to do.

James's work helped shape that approach. The research showed how much more effective an AI system becomes when it can use purpose-built security tools and apply a clear methodology, rather than trying to handle every task from first principles. It also showed that expert judgement still has an important role at the points where it adds the most value.

PortSwigger Research has always influenced what Burp can detect and how security professionals test. As new techniques, tools and methods emerge from that work, they can be turned into practical capabilities for [Burp AT](https://portswigger.net/burp/burp-at) to use during real security testing.

[James's paper](https://portswigger.net/research/http-terminator) explains what the HTTP Terminator found, how it found it and what other researchers can build from it.

[ ]

![Kieron Hughes](/cms/profiles/ae45654f61db45debf66eb798e6837ca.png)

Kieron Hughes

This page requires JavaScript for an enhanced user experience.

Latest Posts

[### Burp AT case study: Ray H

04 August 2026
Burp AT case study: Ray H](/blog/case-study-how-burp-at-helped-expose-whistleblower-reports-via-a-critical-vulnerability-that-was-overlooked-for-years)
[### From capable AI models to trusted security testing

30 July 2026
From capable AI models to trusted securi...