---
title: Browser powered scanning 2.0
url: https://portswigger.net/blog/browser-powered-scanning-2-0
source: PortSwigger Blog
date: 2022-12-16
fetch_date: 2025-10-04T01:39:39.787393
---

# Browser powered scanning 2.0

[**Your agentic AI partner in Burp Suite - Discover Burp AI now**

**Read more**](https://portswigger.net/burp/ai)

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

What's the difference between Pro and Enterprise Edition?

![Burp Suite Professional vs Burp Suite Enterprise Edition](/mega-nav/images/burp-suite.jpg)](/burp/enterprise/resources/enterprise-edition-vs-professional)

[**Support Center**
Get help and advice from our experts on all things Burp.](/support)
[**Documentation**
Tutorials and guides for Burp Suite.](/burp/documentation)
[**Get Started - Professional**
Get started with Burp Suite Professional.](/burp/documentation/desktop/getting-started)
[**Get Started - Enterprise**
Get started with Burp Suite Enterprise Edition.](/burp/documentation/enterprise/getting-started)
[**User Forum**
Get your questions answered in the User Forum.](https://forum.portswigger.net/)
[**Downloads**
Download the latest version of Burp Suite.](/burp/releases)

[Visit the Support Center](/support)

[**Downloads**

Download the latest version of Burp Suite.

![The latest version of Burp Suite software for download](/mega-nav/images/latest-burp-suite-software-download.jpg)](/burp/releases)

# Browser powered scanning 2.0

[ ]

Tom Shelton-Lefley |
15 December 2022 at 14:30 UTC

[Burp Suite](/blog/burp-suite)

![That's no moon](/cms/images/7c/e0/7b0f-article-browser-powered-scanning-2-full.png)

It's been two years since we [unleashed browser powered scanning on the world](https://portswigger.net/blog/browser-powered-scanning-in-burp-suite), and we decided what better way to celebrate than to start again from scratch!

## It started out as a task, how did it end up like this?

As the [Burp Scanner](/burp/vulnerability-scanner) development team has been reminded several times over the last few months, completely re-writing the entirety of our embedded browser integration layer wasn't what we set out to achieve at the start of the quarter. So how did it happen?

The catalyst for this mammoth undertaking was something that's been an elephant in the room with users for a while now: the ability to handle browser actions that open new tabs or windows (specifically in [recorded logins](/burp/vulnerability-scanner/authenticated-scanning)). [Recorded logins](https://portswigger.net/blog/recorded-logins-in-burp-scanner) was a feature developed with external SSO providers in mind, many of which open a new tab at the start of their sign-in sequence, so this feature has been on everyone's list for some time.

You probably don't think this sounds too difficult, and neither did we - the ticket was assigned an "XS" t-shirt size when created and left as a quick win to be picked up by someone with a day or two free. We miscalculated.

Burp Scanner uses [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/) to drive its embedded Chromium browser. When getting everything set up for this, there are two ways of initiating a connection:

1. Attach to a specific target, sending and receiving events over a connection isolated to only that tab or window.
2. Connect to the whole browser, multiplexing target events over a single connection.

Back when we started browser powered scanning, past us¹ decided that it would be adequate to use method 1. Whilst limiting in the long run, at the time it made everything a lot easier and suited our use-case. [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it), [KISS](https://en.wikipedia.org/wiki/KISS_principle), [et al.](https://en.wikipedia.org/wiki/Overengineering) said it was the way to go.

The problem with talking to a single target is that if something happens to create a new one, it's not part of the conversation (and if something happens to close the existing one, we're really stuffed!). Fundamentally, we couldn't track and control tabs or windows created beyond the one we were initially connected to. Herein lay the problem: To achieve our innocuous "sounds like a Friday afternoon job" ticket would require changing the absolute core of our embedded browser integration.

## A forced metaphor

So how does needing to change our Chromium connection lead us to rewriting the entire integration module?

Imagine you have a neat and tidy desk at home. Your computer and all of its peripherals are in their proper place and all of the cables are bundled and routed properly². Everything is kept untangled from everything else. If you need to replace your keyboard, or a monitor, or even the computer itself you can do so without disturbing any of the other components. Bliss.

Now imagine you need to replace the desk. Less bliss. Suddenly the fact that all of your immaculately arranged cables are zip-tied down the table legs is less than ideal …

We needed to replace our desk: Even though all of our browser powered code was nicely compartmentalized and encapsulated, changing the principle it was all built on made it easier to rip it all out and start again.

## Blowing the whole thing up is a good excuse to rebuild without a fatally flawed exhaust port

Whilst being a daunting prospect, starting again from scratch actually presented us with an opportunity to improve code and functionality at a scale not normally possible.

When we first started working on browser powered scanning in 2019 we had no idea what we were doing - it hadn't been done before. There was a lot of trial and error involved, a lot of hurdles that popped up out of nowhere, and a lot of coffee. We were very pleased with what we achieved, and have continued to improve upon it since. However (as is to be expected) we were also left with plenty of "what would you do differently next time"-s.

When we started browser powered scanning again, we *did* know what we were doing³ - it *had* been done before. *Do you know an "Obi-Wan" Chromenobi? Well of course I do, he's me.* We knew where all of the bumps in the road would be ahead of t...