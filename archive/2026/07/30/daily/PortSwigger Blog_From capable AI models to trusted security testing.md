---
title: From capable AI models to trusted security testing
url: https://portswigger.net/blog/from-capable-ai-models-to-trusted-security-testing
source: PortSwigger Blog
date: 2026-07-30
fetch_date: 2026-07-31T05:30:07.726007
---

# From capable AI models to trusted security testing

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

# From capable AI models to trusted security testing

[ ]

Kieron Hughes |
Thursday, 30 July 2026 at 14:58 UTC

![Burp AT](/cms/images/00/44/d301-article-burp_at_banner_-02_(1).png)

This week, [we launched Burp AT in public beta](https://portswigger.net/blog/introducing-burp-at) for [Burp Suite Professional](/burp/pro) users. Next week at Black Hat, PortSwigger Research will reveal more of the work that helped shape our direction.

Burp AT is our product response to what that research is showing us. AI will take on more of the work of a pentest, which makes the tools, expertise, and controls around it increasingly important.

AI can already find and exploit vulnerabilities. PortSwigger Research has been exploring whether an agentic system can go further by absorbing an expert research methodology, generating and testing hypotheses, interpreting evidence, and producing genuinely novel findings.

That research feeds directly into the techniques, tools, and skills in [Burp AT](https://portswigger.net/burp/burp-at). The product challenge is to make agentic capability useful for real-world security testing, where you need control over what happens, evidence of what happened, and results you can stand behind.

## Control must sit outside the model

Models are useful in offensive security because they are creative, persistent, and willing to pursue unexpected paths. Those same qualities also mean they cannot be trusted to police themselves.

They can ignore an instruction, misunderstand the target, or describe their own actions inaccurately. That unpredictability can help when forming hypotheses, but it cannot enforce scope or produce an authoritative audit trail.

Prompting agents to stay in scope is not scope enforcement. Asking one model to supervise another does not change the structural problem, because both rely on the same probabilistic technology.

Control therefore has to sit outside the model. In Burp AT, agents can decide what they want to try, but permissions and scope boundaries are enforced by Burp. Burp blocks disallowed actions and, where your settings require it, pauses for your approval. Requests and tool activity are recorded in the project alongside your own work, so you can inspect what actually happened.

The more capable agents become, the more important this separation is. Agents that can pursue longer chains of work with less supervision can create more value, but they can also make more consequential mistakes. This does not mean stopping agents at every step. Routine work can proceed within the boundaries you have set, while decisions involving risk, ambiguity, or judgment come back to you.

Daf explored this distinction in [The beast needs a cage](https://portswigger.net/blog/the-beast-needs-a-cage-whats-next-for-appsec-post-mythos).

## Tools become more valuable when agents can use them

Because models can write code and construct HTTP requests, it is tempting to assume that security tools will matter less. In practice, we have found the opposite.

Agents can hand-craft requests, write scripts, and process responses. But rebuilding the mechanics of security testing from scratch is expensive, inconsistent, and fragile. Authentication state, browser behavior, malformed traffic, protocol quirks, response comparison, session handling, and application-specific logic all create edge cases that mature tools already know how to handle.

The model can spend its context on hypotheses, decisions, and interpretation instead of reproducing plumbing that already exists. Testing becomes more repeatable, and the requests and responses remain visible in the same project you are using.

An agent improvising every operation will struggle to match one working through a mature, specialized toolkit. Burp Suite’s tools have been developed over more than 20 years and tested at scale against real applications, protocols, and technology stacks. Giving agents access to that tooling makes it more valuable, not less.

## Turning research expertise into reusable skills

Frontier models are broad generalists. They can reason across many domains, but they do not arrive with the methods of the best security researchers.

[PortSwigger Research](https://portswigger.net/research) has always shaped what Burp can do. New vulnerability classes become testing techniques, scan checks, and deeper support for the protocols and behaviors you encounter. Agentic systems create another route for that expertise to reach the product.

James Kettle’s recent work demonstrates the approach. Over the past year, he has turned parts of his research process into a system that can generate and test hypotheses, interpret results, and pursue the most promising lines of investigation. At Black Hat, [he will share the research](https://blackhat.com/us-26/briefings/schedule/index.html#can-ai-do-novel-security-research-meet-the-http-terminator-51894) and the bluepr...