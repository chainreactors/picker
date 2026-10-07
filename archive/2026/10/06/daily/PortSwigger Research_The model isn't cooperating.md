---
title: The model isn't cooperating
url: https://portswigger.net/research/the-model-isnt-cooperating
source: PortSwigger Research
date: 2026-10-06
fetch_date: 2026-10-07T07:55:08.425560
---

# The model isn't cooperating

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

# The model isn't cooperating

[ ]

![James Kettle](/content/images/profiles/callout_james_kettle_112px.png)

### [James Kettle](/research/james-kettle)

Director of Research

[@albinowax](https://twitter.com/albinowax)

* **Published:** Tuesday, 6 October 2026 at 17:14 UTC
* **Updated:** Tuesday, 6 October 2026 at 17:14 UTC

Have you ever felt like a model isn't actually trying to do what you asked? Did you just ask it wrong, or is there something else at play here? In this post, I'll briefly explore this phenomenon, the impact, and what you can do about it.

## Background

At Black Hat USA a couple of months ago, I published [Can AI do novel security research? Meet the HTTP Terminator](https://portswigger.net/research/can-ai-do-novel-security-research). This proved that AI can perform original security research and invent genuinely novel hacking techniques, but it also highlighted an area where models really struggle. A [research cascade](https://portswigger.net/research/can-ai-do-novel-security-research#cascade) is where one discovery is used as fuel for more discoveries affecting different targets (not to be confused with bug chaining), and models consistently underperform at this process.

After publication, I decided to push hard to overcome this barrier and achieve an autonomous cascade, in order to get some fresh material for the [Offensive AI Con](https://www.offensiveaicon.com/schedule#sz-tab-46300) edition of my presentation. I broke my cascade methodology down into multiple steps, and threw a swarm of agents at every aspect of it, giving them the tools to test arbitrary ideas at scale so they weren't confined to the HTTP Desync research space:

![](/cms/images/52/73/85aa-article-screenshot_2026-10-06_at_10.04.21.png)

This process burned quite a few tokens, and only yielded one significant discovery. I was genuinely quite surprised so I took a closer look at the traces, and began to develop a suspicion.

## The suspicion

Broadly speaking, original security research means seeking out high-impact behaviors that are hard to observe. Nobody cares about low-impact behaviors, and if something is easy to observe then someone else probably already found it so you're not really doing original research.

As I analyzed the traces, it seemed like the model was steering toward low-impact behaviors that were easy to observe. The model would try to complete its objective, but use the wiggle-room in the prompt to steer in a direction that actually sabotaged its performance.

Specific, highly-focused tasks like "use this HTTP desync trigger to achieve response queue poisoning on this website" worked fine since they offered minimal wiggle-room. But when given a broad prompt like "Explore other threats arising from the same root cause", the model would silently sabotage its performance.

It seemed like the more ambitious and open-ended your research, the more you'd get silently sabotaged.

## The eval

I initially observed this behavior on OpenAI's daybreak-blue which is powered by gpt-5.6-sol, and thought that the behavior might be caused by the model's alignment, and a less-heavily aligned open-weight model might solve the problem, so I did the logical thing and built a dirty eval using the heavyweight cascade process above, with a panel of LLM models as judges.

Here are the models ranked by intelligence (as rated by Artificial Analysis), with their research-score on the right. Note that no refusals were received from any models during this evaluation.

![](/cms/images/0f/7c/85c3-article-screenshot_2026-10-06_at_10.06.11.png)

The outcome was not what I expected. I speculated that Opus 4.6 might simply be more aggressive by default, so I ran a followup eval with an initial prompt steering the models toward high-impact outcomes. Hilariously, the model that responded the best to this steering was... Opus 4.6.

From here, it looks like the next step is to get my hands on an abliterated model and throw it at this eval, to see if this is really an alignment issue or something else - I'll report back. For now, I'll be sticking to tightly scoped tasks with minimal wiggle-room, and breaking out Opus 4.6 for anything broader.

I'm interested to know what the community thinks - is this surprising to you or something you've personally experienced alr...