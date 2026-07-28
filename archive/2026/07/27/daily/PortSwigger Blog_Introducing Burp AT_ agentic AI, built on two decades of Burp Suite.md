---
title: Introducing Burp AT: agentic AI, built on two decades of Burp Suite
url: https://portswigger.net/blog/introducing-burp-at
source: PortSwigger Blog
date: 2026-07-27
fetch_date: 2026-07-28T04:58:50.016620
---

# Introducing Burp AT: agentic AI, built on two decades of Burp Suite

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

# Introducing Burp AT: agentic AI, built on two decades of Burp Suite

[ ]

Fran Hutchings |
Monday, 27 July 2026 at 12:51 UTC

![](/cms/images/35/a8/8ae4-article-burp_at_banner_-01.png)

### Burp AT brings agentic AI to human-led pentesting, with Burp Suite’s proven tools, your project context, and purpose-built skills. You decide how much work agents take on. Burp enforces the boundaries. Live now in public beta for Burp Suite Professional users.

AI can already find and exploit vulnerabilities. The question is no longer whether the technology is capable. It is what kind of AI you can trust against systems you are responsible for testing.

**Today, we are [launching Burp AT in public beta](https://portswigger.net/burp/burp-at) for Burp Suite Professional users.**

Burp AT lets you put agentic AI to work inside Burp Suite. Agents pursue the tasks you hand them using Burp’s specialist tools, the context gathered in your project, and [pentesting](/solutions/penetration-testing) skills developed with PortSwigger Research, all while you stay in the loop for scope, judgment, and conclusions.

That means you can hand agents investigations that would otherwise compete for your limited time and attention, while you focus your expertise where it matters most. Leads can be pursued further, unfamiliar areas explored more deeply, and worthwhile work that might otherwise go untouched can become part of the test.

## Pentesting takes more than a capable model

Frontier AI models can find and exploit vulnerabilities. Agents can form a hypothesis, act through tools, interpret what they learn, and decide what to try next.

But a professional pentest requires more than capable reasoning. It requires reliable specialist tools, access to relevant context, purpose-built methodology, and boundaries the model cannot bypass.

Burp AT is built around all four:

* **Burp’s tools and your project context.** Agents act through the same battle-hardened tooling professional pentesters have trusted for over 20 years, and draw selectively on the traffic, target structure, issues, and discoveries already in your Burp project so they work alongside you on the test rather than starting from a blank prompt.
* **Purpose-built pentesting skills.** A library of pentesting skills, developed with PortSwigger Research, gives agents structured approaches to apply, instead of improvising a methodology from general model knowledge. As researchers develop new techniques, they become skills agents can use on real tests.
* **Autonomy on your terms.** You decide how much work agents take on, what proceeds, what needs approval, and what is blocked. The right level of autonomy can vary by task, target, risk, and the trust that has been earned.
* **Boundaries enforced by Burp.** Scope, tool access, and approval rules live in Burp’s tooling layer, architecturally separate from the model, and every request and decision is recorded. Agents can propose actions, but they cannot execute actions Burp does not permit. Agents propose. Burp enforces. You decide.

## Deliver more from every pentest

The fastest way to see the value is to hand Burp AT a lead you would usually run out of time to chase. Something as simple as:

*Analyze the minified JavaScript loaded by this target, reconstruct the endpoints and workflows it references, and flag anything that looks sensitive or unauthenticated and worth investigating further.*

In our closed beta, one professional pentester did exactly that against 66,000 lines of minified JavaScript they could never have read by hand inside a four-day engagement. Burp AT helped surface a critical vulnerability that would otherwise have gone untested for at least another year.

> **This is life changing. I cannot begin to express how much easier it started making certain portions of the testing, and how much easier it has made learning.** - Pentester, Closed Beta

Because the work runs through Burp, the resulting requests, responses, and evidence are tracked, so you can reproduce the finding and stand behind it rather than relying on a model’s account of what it did.

## The first phase of Burp AT

This is the first release of Burp AT, available today to [Burp Suite Professional](/burp/pro) users. It brings agentic AI into a human-led pentesting workflow: agents take on more of the work inside Burp, while you retain control of scope, judgment, and conclusions.

Today, Burp AT works alongside you in the Burp workflow. Over time, the same foundation will support more operating modes for teams and enterprises, including more autonomous testing under standing policy, shared visibility, and auditability. Human-led testing remains one of those modes.

We will keep improving its tools, skills, and workflows as more people put it to work and share their feedback, and we will stay clear about what it can do today and where it is still developing.

> **Burp Suite ha...