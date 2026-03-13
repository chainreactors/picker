---
title: Automation without alignment: The hidden cost of modern DAST
url: https://portswigger.net/blog/automation-without-alignment-the-hidden-cost-of-modern-dast
source: PortSwigger Blog
date: 2026-03-12
fetch_date: 2026-03-13T04:06:04.265337
---

# Automation without alignment: The hidden cost of modern DAST

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

# Automation without alignment: The hidden cost of modern DAST

[ ]

Dafydd Stuttard |
12 March 2026 at 12:02 UTC

![Burp Suite DAST x Burp Suite Professional](/cms/images/24/79/10e7-article-better-together_v2_blog_header_(940x400)_.png)

I'm a firm believer that if you want to understand how secure an application really is, you have to test how it behaves, not just how it was written. Automation has become essential to that. No AppSec team can test at the velocity and scale demanded by modern release cycles through manual means alone. As a result, dynamic scanning (DAST) tools are now embedded into the daily rhythm of mature security teams everywhere, often bundled as part of an all-in-one AST platform.

On paper, this looks like a well-rounded approach: Manual testing for depth, automated scanning for scale. And yet, AppSec leaders feel that they're scanning more than ever, but getting increasingly diminishing returns on that investment.

The way most organizations combine DAST automation with manual [pentesting](/solutions/penetration-testing) rarely works as well as it should. Not because the team lacks skill. Not because the processes are poorly designed. But because the tools were developed in isolation from each other.

I've made no secret of the fact that the first version of Burp Suite was built for one user: me. I was a web app pentester and just built the tool I wished I had, enabling me to scale myself exponentially. That practitioner-driven background shapes how we think at PortSwigger even to this day.

I believe that to unlock the full value of DAST, it's crucial to remember that it's an extension of what started as manual pentesting and still relies heavily on humans in the loop. DAST is inherently part of modern practitioner workflows and should be treated as such, rather than grounding it in a parallel ecosystem of broad-brush automation tools.

## The translation tax

Regardless of which automated solutions you implement, some level of manual intervention is always necessary. Automated systems lack judgment. They surface potential issues, but it takes human expertise to determine what actually matters. That's still true despite the staggering advances we've all seen in AI over recent years.

But there's friction most teams don't fully account for. [Burp Suite Professional](/burp/pro) has been the practitioner's tool of choice for web security testing for decades. Whichever DAST solution a team is running, the findings are almost certainly being validated and investigated using Burp Suite.

Think through what that process actually looks like from a practitioner's perspective. The findings arrive in a format that belongs to a different tool, built on a different scanning engine, with its own issue taxonomy, its own evidence model, its own confidence signals. Before your pentesters can even begin to validate anything, they first have to translate it. They have to map the scanner's output to their own mental model and reproduce it in Burp Suite; the tool they actually work in.

This is invisible overhead. It happens for every finding and every scan cycle, across every application in your portfolio. What starts as mild friction compounds, at scale, into a significant drain on your team's time and attention.

Instead of automation freeing up your pentesters to better prioritize and focus on the highest impact activities, their role is reduced to slowly working their way through a seemingly endless backlog of issues. Rather than extending your team's capacity, automation ends up consuming it.

## Expertise that's left on the table

Over years of using Burp Suite Professional, good security teams build up a remarkable amount of institutional knowledge: Custom scan configurations finely tuned to specific tech stacks, innovative extensions that encode expert methodologies and powerful automation, and test cases developed from real findings, refined over time into repeatable checks. This isn't just tooling; it's the codified expertise of skilled practitioners, accumulated over thousands of hours of applying their craft.

None of that is accessible to the DAST component of your AST platform. Because it's built on a fundamentally different engine, with its own scanning logic, its own configuration model, its own extension framework, it has no way to draw on what your team has built up in Burp. That expertise exists. It shapes every manual test your team runs. But it simply cannot cross into a tool built around an entirely different foundation.

Consider what this means. You've invested in a highly skilled team. They've invested in deeply understanding your applications. But when your DAST scanner runs, it operates entirely in isolation. By far your most valuable security asset, practitioner expertise, simply isn't accessible to a scanner that was never buil...