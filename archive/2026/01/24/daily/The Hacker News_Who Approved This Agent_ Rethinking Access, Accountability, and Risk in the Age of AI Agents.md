---
title: Who Approved This Agent? Rethinking Access, Accountability, and Risk in the Age of AI Agents
url: https://thehackernews.com/2026/01/who-approved-this-agent-rethinking.html
source: The Hacker News
date: 2026-01-24
fetch_date: 2026-01-25T03:56:39.214084
---

# Who Approved This Agent? Rethinking Access, Accountability, and Risk in the Age of AI Agents

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

# [Who Approved This Agent? Rethinking Access, Accountability, and Risk in the Age of AI Agents](https://thehackernews.com/2026/01/who-approved-this-agent-rethinking.html)

**The Hacker News**Jan 24, 2026Enterprise Security / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiW0YdKx3Mn8l9PzpwwxmdeBP5kgWuc5R4LevYs6tP-J1z5nSZcdE16En4Z9Ad89VIFR_f3qxeM-vMtgvfOTPxyoZV8H5Dcaj4WlXB2tmh9NG6vGLY7jfD7CyToCKJ_BHVMkkR2kcJdo6yZhIS-RiV3yVyBUHZcVrodWp4wDHdT1phfyZFDifLQnaqiXBc/s1600-e365/wing.jpg)

AI agents are accelerating how work gets done. They schedule meetings, access data, trigger workflows, write code, and take action in real time, pushing productivity beyond human speed across the enterprise.

Then comes the moment every security team eventually hits:

*“Wait… who approved this?”*

Unlike users or applications, AI agents are often deployed quickly, shared broadly, and granted wide access permissions, making ownership, approval, and accountability difficult to trace. What was once a straightforward question is now surprisingly hard to answer.

## AI Agents Break Traditional Access Models

AI agents are not just another type of user. They fundamentally differ from both humans and traditional service accounts, and those differences are what break existing access and approval models.

Human access is built around clear intent. Permissions are tied to a role, reviewed periodically, and constrained by time and context. Service accounts, while non-human, are typically purpose-built, narrowly scoped, and tied to a specific application or function.

AI agents are different. They operate with delegated authority and can act on behalf of multiple users or teams without requiring ongoing human involvement. Once authorized, they are autonomous, persistent, and often act across systems, moving between various systems and data sources to complete tasks end-to-end.

In this model, delegated access doesn’t just automate user actions, it expands them. Human users are constrained by the permissions they are explicitly granted, but AI agents are often given broader, more powerful access to operate effectively. As a result, the agent can perform actions that the user themselves was never authorized to take. Once that access exists, the agent can act - even if the user never meant to perform the action, or wasn’t aware it was possible, the agent can still execute it. As a result, the agent can create exposure - sometimes accidentally, sometimes implicitly, but always legitimately from a technical standpoint.

This is how access drift occurs. Agents quietly accumulate permissions as their scope expands. Integrations are added, roles change, teams come and go, but the agent’s access remains. They become a powerful intermediary with broad, long-lived permissions and often with no clear owner.

It’s no wonder existing IAM assumptions break down. IAM assumes a clear identity, a defined owner, static roles, and periodic reviews that map to human behavior. AI agents don’t follow those patterns. They don’t fit neatly into user or service account categories, they operate continuously, and their effective access is defined by how they are used, not how they were originally approved. Without rethinking these assumptions, IAM becomes blind to the real risk AI agents introduce.

## The Three Types of AI Agents in the Enterprise

Not all AI agents carry the same risk in enterprise environments. Risk varies based on who owns the agent, how broadly it’s used, and what access it has, resulting in distinct categories with very different security, accountability, and blast-radius implications:

### Personal Agents (User-Owned)

Personal agents are [AI assistants](https://wing.security/ai-code-assistants/) used by individual employees to help with day-to-day tasks. They draft content, summarize information, schedule meetings, or assist with coding, always in the context of a single user.

These agents typically operate within the permissions of the user who owns them. Their access is inherited, not expanded. If the user loses access, the agent does too. Because ownership is clear and scope is limited, the blast radius is relatively small. Risk is tied directly to the individual user, making personal agents the easiest to understand, govern, and remediate.

### Third-Party Agents (Vendor-Owned)

Third-party agents are embedded into SaaS and AI platforms, provided by vendors as part of their product. Examples include AI features embedded into CRM systems, collaboration tools, or security platforms.

These agents are governed through vendor controls, contracts, and shared responsibility models. While customers may have limited visibility into how they work internally, accountability is clearly defined: the vendor owns the agent.

The primary concern here is the [AI supply-chain risk](https://wing.security/use-cases/ai-supply-chain-risks/): trusting that the vendor secures its agents appropriately. But from an enterprise perspective, ownership, approval paths, and responsibility are usually well understood.

### Organizational Agents (Shared and Often Ownerless)

Organizational agents are deployed internally and shared across teams, workflows, and use cases. They automate processes, integrate systems, and act on behalf of multiple users. To be effective, these agents are often granted broad, persistent permissions that exceed any single user’s access.

This is where risk concentrates. Organizational agents frequently have no clear owner, no single approver, and no defined lifecycle. When something goes wrong, it’s unclear who is responsible or even who fully understands what the agent can do.

As a result, organizational agents represent the highest risk and the largest blast radius, not because they are malicious, but because they operate at scale without clear accountability.

## The Agentic Authorization Bypass Problem

As we explained in our article, [agents creating authorization bypass paths](https://thehackernews.com/2026/01/ai-agents-are-becoming-privilege.html), AI agents don’t just execute tasks, they act as access intermediaries. Instead of users interacting directly with systems, agents operate on their behalf, using their own credentials, tokens, and integrations. This shifts where authorization decisions actually happen.

When agents operate on behalf of ind...