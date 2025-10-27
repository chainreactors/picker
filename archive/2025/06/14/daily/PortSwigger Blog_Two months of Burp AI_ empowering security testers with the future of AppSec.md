---
title: Two months of Burp AI: empowering security testers with the future of AppSec
url: https://portswigger.net/blog/two-months-of-burp-ai-empowering-security-testers-with-the-future-of-appsec
source: PortSwigger Blog
date: 2025-06-14
fetch_date: 2025-10-06T22:53:26.065584
---

# Two months of Burp AI: empowering security testers with the future of AppSec

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

# Two months of Burp AI: empowering security testers with the future of AppSec

[ ]

Amelia Coen |
13 June 2025 at 13:51 UTC

![](/cms/images/58/ee/5bff-article-burp_ai_linkedin_image.png)

### It’s been a whirlwind two months since AI-powered features landed in Burp Suite Professional. Thousands of security testers across the world have been using [Burp AI](https://portswigger.net/burp/ai) to find vulnerabilities and secure their applications, and we’ve been blown away by what you have been able to achieve.

### From helping us iterate, and providing valuable feedback, to winning bug bounties, the journey so far has been exciting. Here's a look back at what’s happened, and a glimpse at what’s coming next.

![](/cms/images/11/1f/c676-article-burp_ai_social_proof.png)

## Five new features

Back in April, five major capabilities designed to supercharge security testers, and optimize workflows, with AI were introduced. These are…

### Explore Issue

Turn Burp AI into your personal [pentesting](/solutions/penetration-testing) assistant, automating follow-up analysis of scanner-identified vulnerabilities to save time, reduce blind spots, and uncover deeper insights.

![](/cms/images/4a/92/ebbc-article-explore_issue_gif.gif)

![](/cms/images/58/6d/74ff-article-explore_issue_social_proof.png)

### Explainer

Confused by an unfamiliar cookie? Unsure what a strange header means? Just highlight it in Repeater and let Burp AI explain it from a security perspective.This feature removes the friction of switching tabs and searching docs. It’s like having a security-savvy co-pilot in your tab bar.

![](/cms/images/31/34/b283-article-82bfeda1-161a-4261-b9c9-c9bc5757a0a5.gif)![](/cms/images/1c/25/7197-article-burp_ai_explainer_pre-launch_1.png)

### AI-generated recorded logins

No more fiddling around with browser recordings. Burp AI can now generate login sequences on your behalf, reducing configuration time and ensuring better scan coverage - especially for complex authentication flows.

![](/cms/images/17/2b/9417-article-ebce2e71-267b-4b51-8c33-bcd1c1a401b9.gif)

![](/cms/images/29/8e/c689-article-ai_recorded_log_ins_social_proof.png)

### False positive reduction: broken access control

False positives drain time and energy. With Burp AI, we’ve started cutting down on the noise - starting with one of the hardest vulnerability classes to reliably detect through automation: Broken [Access Control](/web-security/access-control). [Burp Scanner](/burp/vulnerability-scanner) now uses AI to intelligently filter out irrelevant findings, boosting accuracy and freeing you up to focus on real threats.

![](/cms/images/04/0e/c660-article-ai_bac_screen_shot.jpg)

### AI-powered extensibility

The Montoya API and AI extensibility features open up new creative possibilities. Security pros and developers can now use AI to build novel, customized tools right inside Burp Suite.

## BApp store bursts with AI innovation

In just a few short weeks, we’ve seen a surge of new AI-powered extensions land in the BApp Store, created by both the PortSwigger team and our growing user community.

Check out AI-enhanced extensions on the BApp store, including:

* [Shadow Repeater](https://portswigger.net/bappstore/7be1798d600647688bb2f051da37f504) - simply use Burp Repeater as you normally would, and behind the scenes Shadow Repeater will monitor your attacks, try permutations, and report any discoveries via Organizer.
* [HTTP Analyzer](https://portswigger.net/bappstore/36cb140ac1a6449bbab1bafc18df8cfa) - examines HTTP requests and responses for potential security vulnerabilities such as SQL injection, [XSS](/web-security/cross-site-scripting), [CSRF](/web-security/csrf), and other threats.
* [AI Substitutor](https://portswigger.net/bappstore/bd1775972c944060a7051b364b98bd6f) - automatically substitute HTTP request parameters and headers with contextually relevant values.
* [MCP Server](https://portswigger.net/bappstore/9952290f04ed4f628e624d0aa9dccebc) - integrate Burp Suite with AI Clients using the Model Context Protocol (MCP).
* [AI prompt fuzzer](https://portswigger.net/bappstore/d3d1f3c9427e453193eb5deb3b6c115a) - automating prompt fuzzing against AI APIs using customizable payloads, helping identify abnormal or unsafe model behavior.
* [AI Recon Assistant](https://portswigger.net/bappstore/f5ddfbd9bcf24d15bda8b13aa1c19d47) - extract meaningful insights from requests and responses without manual inspection.
* [Document My Pentest](https://portswigger.net/bappstore/bc746627d8494445bf91988e2e20ede1) - create a description of whatever you are trying to test. Whether you're probing for path traversal, SQL injection, XSS, or other vulnerabilities, Document My Pentest tries to understand wha...