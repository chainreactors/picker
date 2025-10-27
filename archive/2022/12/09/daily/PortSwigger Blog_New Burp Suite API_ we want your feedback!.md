---
title: New Burp Suite API: we want your feedback!
url: https://portswigger.net/blog/new-burp-suite-api-we-want-your-feedback
source: PortSwigger Blog
date: 2022-12-09
fetch_date: 2025-10-04T01:00:08.779317
---

# New Burp Suite API: we want your feedback!

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

# New Burp Suite API: we want your feedback!

[ ]

Sean Burns |
08 December 2022 at 10:45 UTC

![New Burp Suite API - we want your feedback](/cms/images/92/74/05c2-article-montoya_api_article.png)

If you follow the [Burp Suite roadmap](https://portswigger.net/blog/burp-suite-roadmap-update-july-2022), then you'll know that we're working on a complete rewrite of the "Wiener" API used in [Burp Suite Professional](https://portswigger.net/burp/pro) and [Burp Suite Community Edition](https://portswigger.net/burp/communitydownload). The new API is codenamed "Montoya", and will eventually expose much more of Burp Suite's core functionality - providing richer capabilities for writers of Burp extensions.

As one of the devs working on this project, I'm pleased to announce that things are going well. The feature-parity [Montoya API](https://github.com/PortSwigger/burp-extensions-montoya-api) has been available since [Burp Suite 2022.9.5](https://portswigger.net/burp/releases/professional-community-2022-9-5), and we're going to be adding more functionality very soon (like in [2022.11](https://portswigger.net/burp/releases/professional-community-2022-11), which added API support for WebSocket listeners).

## Have your say

I'm also here to ask a favor - because we want your feedback. If you currently use Burp Suite's Wiener API to write extensions, or if you've always fancied writing a Burp Suite extension in Java, then we'd love for you to put the new Montoya API through its paces. More specifically, if you want to [report a bug](https://github.com/PortSwigger/burp-extensions-montoya-api/issues), or have any [suggestions for the new API](https://github.com/PortSwigger/burp-extensions-montoya-api/discussions), then we're very open to both of those things.

These are exciting times to be an author of Burp Suite extensions - because we're going to be continuously improving and adding to the new API. In the near future, you can expect to see new functionality exposed around project files (enabling you to persist data), scan configurations, and table customization (adding custom columns in just about any Burp Suite table you can think of). This will all add up to give you access to even more of Burp Suite's power in your extensions - and we're already planning what to add after that.

Let us know what you think over on the [Montoya API GitHub site](https://github.com/PortSwigger/burp-extensions-montoya-api). And of course, if you want any inspiration, then check out [the BApp Store](https://portswigger.net/bappstore), for a huge range of open source Burp Suite extensions written using the old API. Until next time, happy coding!

[ ]

![Sean Burns](/cms/profiles/sean-burns.png)

This page requires JavaScript for an enhanced user experience.

Latest Posts

[### Hacking smarter with Burp AI: NahamSec puts Burp AI to the test

01 October 2025
Hacking smarter with Burp AI: NahamSec puts Burp AI to the test](/blog/hacking-smarter-with-burp-ai-nahamsec-puts-burp-ai-to-the-test)
[### Welcome to AI pentesting - add on-demand AI assistance directly to your workflow with new, agentic Burp AI capabilities

24 September 2025
Welcome to AI pentesting - add on-demand AI assistance directly to your workflow with new, agentic Burp AI capabilities](/blog/welcome-to-ai-pentesting-add-on-demand-ai-assistance-directly-to-your-workflow-with-new-agentic-burp-ai-capabilities)
[### How to join the desync endgame: Practical tips from pentester Tom Stacey

18 September 2025
How to join the desync endgame: Practical tips from pentester Tom Stacey](/blog/how-to-join-the-desync-endgame-practical-tips-from-pentester-tom-stacey)

Burp Suite

[Web vulnerability scanner](/burp/vulnerability-scanner)
[Burp Suite Editions](/burp)
[Release Notes](/burp/releases)

Vulnerabilities

[Cross-site scripting (XSS)](/web-security/cross-site-scripting)
[SQL injection](/web-security/sql-injection)
[Cross-site request forgery](/web-security/csrf)
[XML external entity injection](/web-security/xxe)
[Directory traversal](/web-security/file-path-traversal)
[Server-side request forgery](/web-security/ssrf)

Customers

[Organizations](/organizations)
[Testers](/testers)
[Developers](/developers)

Company

[About](/about)
[Careers](/careers)
[Contact](/about/contact)
[Legal](/legal)
[Privacy Notice](/privacy)

Insights

[Web Security Academy](/web-security)
[Blog](/blog)
[Research](/research)

[![PortSwigger Logo](/content/images/logos/portswigger-logo.svg)](/)
 [Follow us](https://twitter.com/Burp_Suite)

© 2025 PortSwigger Ltd.