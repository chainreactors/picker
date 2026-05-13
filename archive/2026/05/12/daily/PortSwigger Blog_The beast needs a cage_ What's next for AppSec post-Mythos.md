---
title: The beast needs a cage: What's next for AppSec post-Mythos
url: https://portswigger.net/blog/the-beast-needs-a-cage-whats-next-for-appsec-post-mythos
source: PortSwigger Blog
date: 2026-05-12
fetch_date: 2026-05-13T05:46:12.195189
---

# The beast needs a cage: What's next for AppSec post-Mythos

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
[**User Forum**
Get your questions answered in the User Forum.](https://forum.portswigger.net/)
[**Downloads**
Download the latest version of Burp Suite.](/burp/releases)

[Visit the Support Center](/support)

[**Downloads**

Download the latest version of Burp Suite.

![The latest version of Burp Suite software for download](/mega-nav/images/latest-burp-suite-software-download.jpg)](/burp/releases)

# The beast needs a cage: What's next for AppSec post-Mythos

[ ]

Dafydd Stuttard |
Tuesday, 12 May 2026 at 14:18 UTC

![](/cms/images/d2/a1/feec-article-the_beast_needs_a_cage_article_header.png)

Now that the dust has settled on Mythos dropping, there is space for more considered reflection on the direction of travel.

Mythos wasn't a surprise; it's another data point on a trajectory that's been clear for some time. Frontier lab capabilities are moving at pace, with major implications for all domains, not least cybersecurity.

Open-weight models are following the same trajectory, with a modest lag. It's fairly likely that they'll match today's frontier capabilities within a few months. Anyone with suitable compute power will have access to Mythos-like capabilities. This was a key topic of discussion when [James Kettle](https://portswigger.net/research/james-kettle) and I recently [appeared on the *Risky Business* podcast](https://www.youtube.com/watch?v=GdFG85oCWFI).

In this post, I'll set out where I think this leaves us: the structural limits that still matter, what changes for the security practitioner, and how we're approaching all of this in the next generation of Burp Suite.

## The interesting question isn't what AI can do. It's what it can't

For AppSec, it's likely that the whole traditional value chain of finding vulnerabilities, proving they're real, and then fixing them, will be automatable end-to-end.

The question stops being *"Can AI do this?"* and becomes *"How do we do this responsibly, at scale?"*.

To think this through, I've found it useful to distinguish between model capability gaps and structural limitations.

In terms of model capabilities, we should just assume that the gaps get filled. Models are just going to get better and better and do everything that models can in principle do. If you start building something yourself on the edge of frontier model capabilities, it's highly likely that you're wasting your time; it'll be overtaken by an upcoming model update soon enough.

Then there's stuff that LLM models structurally can't do. LLMs are non-deterministic. Run the same query twice, you get two different results. That's useful when you're generating ideas and output. But if you give the model agency (the ability to perform actions), it's a potential problem. And if you give it access to offensive AppSec tools, it's a dangerous problem. An unrestrained model can do damage, attack the wrong target, leak sensitive data, or deliberately cover its tracks.

For anyone looking for proper assurance of their security, they need reliability, reproducibility, effective safety guards, and a robust audit trail. You can't prompt any of this into models. Fundamentally, this technology cannot self-govern.

As model capabilities improve, the structural limitations actually get more significant, not less. More capable models take bigger, more consequential actions with less oversight. As capability gaps close, the stakes go up, and the structural limitations matter more.

The power of LLMs to transform AppSec is clear. We've proven some amazing capabilities in our research labs, and we'll be sharing details of those soon. It's as if we've created a magical beast. It can do amazing things that weren't possible before. But that beast has claws. Let it loose, and it will create mayhem. To unlock the beast's power in a controlled way, we need a strong cage around it.

Architecturally, what this looks like is a strong safety and governance layer around the agentic core. Every time the model wants to perform an action, it goes through this layer, with deterministic policy enforcement, human-in-the-loop decisions, and a proper audit trail. This doesn't have to involve friction or overhead; rather, it's what enables serious users to access the sheer power in a controlled way.

## The job of the security practitioner is about to get harder, not easier

The question on many pentesters' minds right now is whether they're being replaced.

The honest answer is no, but the job is going to change. And we already know the shape of the change because software engineering is going through it.

When we discussed PortSwigger's research and products recently on *Risky Business.*

The path ahead for security practitioners, pentesters, and security engineers is likely to follow a similar trajectory as software engineers. The best developers today are not typing code into their IDE. They are overseeing the agentic engine. They are making architectural decisions. They are guiding it and taking a risk-based approach to what PRs they actually look at. But they didn't stop being software engineers.

Security testers will make the same transition.

In the near future, you'll no longer have to set up your Intruder attacks, configure the payloads and the filters, and monitor the results. You might not even need to think about which attacks would be wort...