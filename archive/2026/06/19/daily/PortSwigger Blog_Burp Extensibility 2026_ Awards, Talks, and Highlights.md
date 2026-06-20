---
title: Burp Extensibility 2026: Awards, Talks, and Highlights
url: https://portswigger.net/blog/burp-extensibility-2026-awards-talks-and-highlights
source: PortSwigger Blog
date: 2026-06-19
fetch_date: 2026-06-20T06:13:34.190511
---

# Burp Extensibility 2026: Awards, Talks, and Highlights

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

What's the difference between Pro and DAST?

![Burp Suite Professional vs Burp Suite DAST](/mega-nav/images/burp-suite.jpg)](/burp/dast/resources/dast-vs-professional)

[**Support Center**
Get help and advice from our experts on all things Burp.](/support)
[**Documentation**
Tutorials and guides for Burp Suite.](/burp/documentation)
[**Get Started - Professional**
Get started with Burp Suite Professional.](/burp/documentation/desktop/getting-started)
[**Get Started - DAST**
Get started with Burp Suite DAST.](/burp/documentation/dast/getting-started)
[**Downloads**
Download the latest version of Burp Suite.](/burp/releases)

[Visit the Support Center](/support)

[**Downloads**

Download the latest version of Burp Suite.

![The latest version of Burp Suite software for download](/mega-nav/images/latest-burp-suite-software-download.jpg)](/burp/releases)

# Burp Extensibility 2026: Awards, Talks, and Highlights

[ ]

Fran Hutchings |
Friday, 19 June 2026 at 12:18 UTC

![](/cms/images/5e/b9/24b8-article-extensions_blog_header.png)

* [**The 2026 Burp Suite Extension Awards**](#the-2026-burp-suite-extension-awards)
  + [**Best Recon & Discovery**](#best-recon-discovery)
  + [**Best Auth & Access Control**](#best-auth-access-control)
  + [**Best Workflow & Manipulation**](#best-workflow-manipulation)
  + [**Best API & Specialist Testing**](#best-api-specialist-testing)
  + [**Hidden Gem**](#hidden-gem)
  + [**Most Nominated**](#most-nominated)
* [**The talks**](#the-talks)
  + [**Intro to Extensibility in Burp**](#intro-to-extensibility-in-burp)
  + [**Submitting extensions to the BApp Store**](#submitting-extensions-to-the-bapp-store)
  + [**Writing your first Burp extension**](#writing-your-first-burp-extension)
  + [**Restoring Testability: Handling Complex Scenarios in Burp Suite with a Custom Extension**](#restoring-testability-handling-complex-scenarios-in-burp-suite-with-a-custom-extension)
  + [**Swapper: A quick rundown**](#swapper-a-quick-rundown)
  + [**ByteBanter - LLM-driven Payload Generator for Burp Intruder**](#bytebanter-llm-driven-payload-generator-for-burp-intruder)
  + [**Extension in the loop: Developing Burp extensions with AI**](#extension-in-the-loop-developing-burp-extensions-with-ai)
  + [**Adventures in Bambda Automation with Claude Code**](#adventures-in-bambda-automation-with-claude-code)
  + [**Build to learn: How PortSwigger uses Burp extensions to prototype ideas**](#build-to-learn-how-portswigger-uses-burp-extensions-to-prototype-ideas)
* [**Try it yourself**](#try-it-yourself)
* [**Get involved**](#get-involved)

Throughout May 2026 we ran Extensibility Month on the [PortSwigger Discord server](https://discord.com/invite/portswigger) - a full month of talks, workshops, community sessions, and the Burp Extension Awards, decided by community vote.

The goal was to showcase the different ways people extend Burp, and highlight the work being shared across the community.

Extensibility in Burp means three things: extensions (BApps), Bambdas, and custom scan checks (BChecks). All three give you ways to tailor Burp to your workflow, whether that's automating something repetitive, adding a check the scanner doesn't have out of the box, or building something entirely new.

## The 2026 Burp Suite Extension Awards

The talks highlight what's possible with Burp's extensibility features, but they only tell part of the story. Running alongside the sessions, the community nominated and voted for the extensions they find most useful in day-to-day testing.

More than 200 nominations were submitted for 46 extensions. Rather than ranking tools just by raw popularity, nominations were also scored on the quality of the reasoning behind them: specificity, real-world use cases, and technical insight.

### Best Recon & Discovery

**Shortlist:** Param Miner, Sensitive Discoverer, Active Scan++, Backslash Powered Scanner, JS Miner, JS Link Finder, Firewall Ferret, GAP (Get All Parameters, Links, and Words), 403 Bypasser

**Backslash Powered Scanner** impressed with its philosophy: *"Instead of looking for known issues, it looks for anomalous behaviour - that often hides known and unknown types of server-side injection vulnerabilities."*

**JS Miner** drew some of the most vivid nominations in the competition: *"I've pulled some really solid findings out of it - hidden endpoints buried in JS files that turned out to expose PII, secrets that were actually exploitable and ended up being critical severity, and in some cases straight up hardcoded credentials and tokens sitting there giving access to internal systems."*

![](/cms/images/af/42/2d07-article-best_recon_&_discovery.png)

### Best Auth & Access Control

**Shortlist:** Autorize, PwnFox For Chromium, JWT Editor, Auth Analyzer, SAML Raider, Burp Variables, Authentication Token Obtain and Replace, AuthMatrix

**JWT Editor** earned nominations for keeping everything in-tool: *"Easy way to decode JWTs without relying on third-party websites or browser extensions. Automatic JWT discovery with a tab that shows the decoded JWT per request."*

**Auth Analyzer:** *"Saves time and nerves, allows doing comprehensive [access control](/web-security/access-control) tests with multiple users at the same time."*

![](/cms/images/01/df/e52a-article-best_auth_access_&_control.png)

### Best Workflow & Manipulation

**Shortlist:** Highlighter And Extractor, CSTC, Modular HTTP Manipulator, Turbo Intruder, Hackvertor, Burpcord, Discord Rich Presence for Burp, Saver Logger, Logger++, Proxy Enriched Sequence Diagrams Exporter, Reshaper, Sheet Intruder, Burp Bounty, Scan Check Builder, Swapper, Piper, HTTP Request Smuggler, Taborator, WebSocket Turbo Intruder

**Highlighter And Extractor** was the single most-nominated extension in the entire competition with 18 votes. *"Highlighter And Extractor acts like a smart filter, immediately drawing my ...