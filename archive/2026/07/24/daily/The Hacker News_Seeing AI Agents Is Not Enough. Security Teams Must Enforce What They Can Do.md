---
title: Seeing AI Agents Is Not Enough. Security Teams Must Enforce What They Can Do
url: https://thehackernews.com/2026/07/seeing-ai-agents-is-not-enough-security.html
source: The Hacker News
date: 2026-07-24
fetch_date: 2026-07-25T05:00:48.990333
---

# Seeing AI Agents Is Not Enough. Security Teams Must Enforce What They Can Do

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Seeing AI Agents Is Not Enough. Security Teams Must Enforce What They Can Do](https://thehackernews.com/2026/07/seeing-ai-agents-is-not-enough-security.html)

**The Hacker News**Jul 24, 2026Enterprise Security / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrpwR_tXhzpbt7F1FuALLW8MYrTuwWibwuWjsRDROepxJKdbvSNlbcZLHbL54SmyG_Q_oYFTjI5fqkudKNtfJkg68jAz4STq0xXHEOXnMeOq7fxPz2UslZesQBy_pWKn3IKYNEbltVsjbZDypkqi56JOeznD5hcGEKO6yB-qS2l5cPHlcX0cli_WOHNGM/s1700-e365/pixer.jpg)

AI agent security is moving through a familiar maturity curve: adoption, then visibility, and finally, control. But what we've collectively discovered is that enforcing least privilege for AI agents is harder than we ever imagined. This is why there are so many approaches, from prompt filtering to identity-layer access controls. Where we've collectively landed is that understanding the intent of AI agents is essential to securing them. It's not easy, but it's the only path forward.

Organizations approach this challenge with different levels of sophistication. For many, the current goal is simply to find the AI agents already operating across the business. That is a necessary first step. AI agents are appearing in SaaS platforms, developer environments, cloud workflows, customer support systems, productivity tools, and internal applications. Some are sanctioned, and others are not.

But discovery alone isn't useful. AI agents are not passive; they reason, plan, call tools, invoke APIs, access data, and take action without a human in the loop. The risk is not that an organization has too many agents. The risk is that those agents can operate across systems without consistent identity, intent, ownership, and enforcement. There are also [different types of AI agents](https://www.token.security/the-agentic-pulse?utm_source=thehackernews&utm_medium=3rdparty&utm_campaign=thehackernews&utm_content=jul-24), each requiring a different approach to securing them.

Recent guidance on the [careful adoption of agentic AI services](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services) makes the point clear: agentic AI introduces privilege, authentication, accountability, design, and behavioral risks that security teams need to address before these systems become embedded in critical workflows. Visibility is the starting line, but enforcement is what matters.

## The Visibility Trap

Most security programs begin with the question: "What do we have?" That made sense for cloud, SaaS, endpoints, identities, and vulnerabilities. It also makes sense for AI agents.

But the risk of stopping at visibility alone for AI agents is greater than in every other environment in the list because of the speed with which AI agents are being created, what they have access to, and how they can be shared.

An AI agent inventory that does not connect to enforcement becomes another static asset list. It may show that an agent exists, but it cannot tell you whether the agent's access is appropriate, its behavior matches its purpose, its owner remains accountable, or when its permissions should be revoked as conditions change. For AI agents, visibility without enforcement creates a dangerous kind of confidence, where it's easy to feel in control when the reality is far different.

## Why AI Agents Break Static Access Models

Traditional access control assumes some level of predictability. Human Identity and Access Management has it the easiest, as each person has a job function. Non-human or machine identity management is more complex, but a service account still supports a defined workload. These assumptions are imperfect, but they gave security teams a foundation for roles, entitlements, approvals, access reviews, and periodic cleanup.

AI agents are far from static. An agent is defined less by a fixed workflow and more by a goal. It may interpret instructions, call different tools, and adapt its actions based on context. Two agents with similar permissions may have a very different risk profile, depending on what each is trying to accomplish.

Static access is not enough because AI agents are more likely to be used in ways not anticipated when access was granted. The issue is not always malicious behavior but ambiguity that poses a risk, such as a task that expands beyond its original purpose.

The question security teams need to ask is not only "what can this agent access?" The more important question is: What should this agent be allowed to do, under these conditions, for this purpose? That is an enforcement question.

## Enforcement Starts With Better Understanding

Effective AI agent enforcement cannot be bolted onto a basic, non-contextual inventory. Security teams need to correlate information across owners, consumers, identities, systems, permissions, and intent before they can define meaningful controls.

That means understanding an agent across several dimensions:

* **Ownership:** Who owns the agent? (This can be more difficult than you may think.)
* **Consumers:** Who is using the agent?
* **Identity:** Which identities, tokens, secrets, OAuth grants, and service accounts does the agent use?
* **Intent:** What is the agent supposed to accomplish?
* **Access:** Which systems, applications, data stores, APIs, and infrastructure can it reach?
* **Usage:** What has the agent actually done, and how often?
* **Origin:** How was the agent created?
* **Lifecycle:** Is the agent active, dormant, or no longer tied to its original purpose?

This is where many organizations struggle because agent context is scattered. Identity data lives in one place. Cloud permissions are somewhere else. SaaS integrations have their own models. Infrastructure as code can reveal intended deployment patterns, but that context is rarely correlated with the rest. Ownership may be obvious to the person who created the agent and invisible to everyone else.

Without ...