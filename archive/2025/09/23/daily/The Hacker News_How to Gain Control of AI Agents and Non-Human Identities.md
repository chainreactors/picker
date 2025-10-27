---
title: How to Gain Control of AI Agents and Non-Human Identities
url: https://thehackernews.com/2025/09/how-to-gain-control-of-ai-agents-and.html
source: The Hacker News
date: 2025-09-23
fetch_date: 2025-10-02T20:33:00.605412
---

# How to Gain Control of AI Agents and Non-Human Identities

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [How to Gain Control of AI Agents and Non-Human Identities](https://thehackernews.com/2025/09/how-to-gain-control-of-ai-agents-and.html)

**Sep 22, 2025**The Hacker NewsAI Security / Cloud Security

[![AI Agents and Non-Human Identities](data:image/png;base64... "AI Agents and Non-Human Identities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgX1w-Un0FwFvuOLMysATZBECLAfNADKcpYLZS46XufH7UN-HdLFw6pjEV0w4bLsKRavGNcQI9PELtJGwFXi2C1R9oOFZv8EPqPCwl8CPfc9sEGRPTnPuCNDFCreLdIJNYOuujjdMnXiXlLdivPwkCvBINHXFr-an1zI0TXc46_g8MtEi9fxW636c4ijUE/s790-rw-e365/ai-agents.jpg)

We hear this a lot:

**"We've got hundreds of service accounts and AI agents running in the background. We didn't create most of them. We don't know who owns them. How are we supposed to secure them?"**

Every enterprise today runs on more than users. Behind the scenes, thousands of non-human identities, from service accounts to API tokens to AI agents, access systems, move data, and execute tasks around the clock.

They're not new. But they're multiplying fast. And most weren't built with security in mind.

Traditional identity tools assume intent, context, and ownership. Non-human identities have none of those. They don't log in and out. They don't get offboarded. And with the rise of autonomous agents, they're beginning to make their own decisions, often with broad permissions and little oversight.

It's already creating new blind spots. But we're only at the beginning.

In this post, we'll look at how non-human identity risk is evolving, where most organizations are still exposed, and how an identity security fabric helps security teams get ahead before the scale becomes unmanageable.

## The rise (and risk) of non-human identities

Cloud-first architectures increased infrastructure complexity and triggered a surge in background identities. As these environments grow, the number of background identities grows with them, many of which get created automatically, without clear ownership or oversight. In many cases, these identities outnumber human users [by more than 80 to 1](https://finance.yahoo.com/news/machine-identities-outnumber-humans-more-122700291.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAA4-IGr14JPbKI_IiE9lWi8UlnWAWGLzdEjbzJJB7Q6OkadtU0PZKs-76HkR8uV7k1vF7dqfoo_16r7v3fBHTBd5iFjvaq3bTEODmdpw5PSMlcwjscA06tN1sEeRQ8FGH6uPTAQMgUYVkgE1zrB72xT_XBNV7e8okW7C9Vx9NrVW).

What makes that especially risky is how little most teams know about them. NHIs often get created automatically during deployment or provisioning, then disappear from the radar, untracked, unowned, and often over-permissioned.

Service accounts, in particular, are everywhere. They move data between systems, run scheduled jobs, and authenticate headless services. But their sprawl is rarely visible, and their permissions are rarely reviewed. Over time, they become perfect vehicles for lateral movement and privilege escalation.

But service accounts are only part of the picture. As AI adoption grows, a new category of non-human identity introduces even more unpredictable risk.

### Why AI agents behave differently and why that matters

Unlike most machine identities, AI agents initiate actions on their own; interacting with APIs, querying data, and making decisions autonomously.

That autonomy comes at a cost. AI agents often need access to sensitive data and APIs, but few organizations have guardrails for what they can do or how to revoke that access.

Worse, most AI agents lack clear ownership, follow no standard lifecycle, and offer little visibility into their real-world behavior. They can be deployed by developers, embedded in tools, or called via external APIs. Once live, they can run indefinitely, often with persistent credentials and elevated permissions.

And because they're not tied to a user or session, AI agents are difficult to monitor using traditional identity signals like IP, location, or device context.

### The cost of invisible access

Secrets get hardcoded. Tokens get reused. Orphaned identities remain active for months, sometimes years.

These risks are not new, but static credentials and wide-open access may have been manageable when you had a few dozen service accounts. But with thousands, or tens of thousands, of NHIs operating independently across cloud services, manual tracking simply doesn't scale.

That's why many security teams are revisiting how they define identity in the first place. Because if an AI agent can authenticate, access data, and make decisions, it *is* an identity. And if that identity isn't governed, it's a liability.

## Common NHI security challenges

Understanding that non-human identities represent a growing risk is one thing; managing that risk is another. The core problem is that the tools and processes built for human identity management don't translate to the world of APIs, service accounts, and AI agents. This disconnect creates several distinct and dangerous security challenges that many organizations are only beginning to confront.

### You can't protect what you can't see

The most fundamental challenge in securing NHIs is visibility. Most security teams don't have a complete inventory of every non-human identity operating in their environment. These identities are often created dynamically by developers or automated systems to serve a specific, temporary function. They get spun up to support a new microservice, run a deployment script, or integrate a third-party application.

Once created, however, they rarely get documented or tracked in a central identity management system. They become "shadow" identities, active and functional, but completely invisible to security and IT. Without a comprehensive view of what NHIs exist, who (or what) created them, and what they are accessing, it's impossible to build a meaningful security strategy. You are left trying to secure an attack surface of an unknown size.

### Why "set it and forget it" is a security liability

A common practice for developers an...