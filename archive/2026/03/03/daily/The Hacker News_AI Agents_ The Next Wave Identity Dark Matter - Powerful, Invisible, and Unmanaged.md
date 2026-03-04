---
title: AI Agents: The Next Wave Identity Dark Matter - Powerful, Invisible, and Unmanaged
url: https://thehackernews.com/2026/03/ai-agents-next-wave-identity-dark.html
source: The Hacker News
date: 2026-03-03
fetch_date: 2026-03-04T04:04:34.875604
---

# AI Agents: The Next Wave Identity Dark Matter - Powerful, Invisible, and Unmanaged

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [AI Agents: The Next Wave Identity Dark Matter - Powerful, Invisible, and Unmanaged](https://thehackernews.com/2026/03/ai-agents-next-wave-identity-dark.html)

**The Hacker News**Mar 03, 2026Artificial Intelligence / Enterprise Security

[![](data:image/png;base64...)](https://eu1.hubs.ly/H0sbqmr0)

## **The Rise of MCPs in the Enterprise**

The Model Context Protocol (MCP) is quickly becoming a practical way to push LLMs from “chat” into real work. By providing structured access to applications, APIs, and data, MCP enables prompt-driven AI agents that can retrieve information, take action, and automate end-to-end business workflows across the enterprise. This is already showing up in production through horizontal assistants and custom vertical agents. like Microsoft Copilot, ServiceNow, Zendesk bots, and Salesforce Agentforce, with custom and vertical agents moving fast behind them. This echoes the recent [Gartner](https://gartner.com) “Market Guide for Guardian Agents” [report](https://www.gartner.com/document/7509053), where analysts note that the rapid enterprise adoption of these AI agents is significantly outpacing the maturity of the governance and policy controls required to manage them.

We believe the primary disconnect is that these AI “colleagues” don’t look like humans.

* They don’t join or leave through HR
* They don’t submit access requests
* They don’t retire accounts when projects end

They’re often invisible to traditional IAM, and that’s how they become identity dark matter: real identity risk outside the governance fabric. And agentic systems don’t just use access, they hunt for the path of least resistance. They’re optimized to finish the job with minimal friction: fewer approvals, fewer prompts, fewer blockers. In identity terms, that means they’ll gravitate toward whatever already works, in-app-local accounts, stale service identities, long-lived tokens, API keys, bypass auth paths, and if it works, it gets reused.

Team8’s [2025 CISO Village Survey](https://team8.vc/ciso-village-survey-2025/) found:

* Nearly **70% of enterprises already run AI agents (any system that can answer and act) in production**.
* Another **23% are planning deployments in 2026**.
* **Two-thirds** are building them in-house.

MCP adoption isn’t a question of if; it’s a question of how fast and wisely. It’s already here, and it’s only accelerating. Complicating this further is the reality of hybrid environments. Based on the Gartner research, it seems that organizations face significant hurdles in managing these non-human identities because native platform controls and vendor safeguards generally do not extend beyond their own cloud or platform borders. Without an independent oversight mechanism, cross-cloud agent interactions remain entirely ungoverned. The real question is whether your AI agents become trusted teammates or [unmanaged identity dark matter](https://eu1.hubs.ly/H0sbqmr0)?

​​

## **How Identity Dark Matter Gets Abused by Agent-AI**

As autonomous AI agents that can plan and execute multi-step tasks with minimal human input, Agent AI is a powerful assistant but also a major cyber risk. Interestingly, leading industry analysts seem to expect that the vast majority of unauthorized agent actions will stem from internal enterprise policy violations, such as misguided AI behavior or information oversharing, rather than malicious external attacks.

The typical abuse pattern we see is similar, driven by agent automation and shortcut-seeking:

* Enumerate what exists: Agent crawls apps and integrations, lists users/tokens, discovers “alternate” auth paths.
* Try what’s easy first: Local accounts, legacy creds, long-lived tokens, anything that avoids a fresh approval.
* Lock onto “good enough” access: Even low privilege is enough to pivot: read configuration files, pull logs, discover secrets, map organization structure.
* Upgrade quietly: Find over-scoped tokens, stale entitlements, or dormant-but-privileged identities and escalate with minimal noise.
* Operate at machine speed: Thousands of small actions occur across many systems, too fast and too wide for humans to spot early.

The real risk here is the scale of impact: one neglected identity becomes a reusable shortcut across the estate.

## **The Dark Matter Risks**

In addition to abusing identity dark matter, left unchecked, MCP agents (AI Agents that use the MCP protocol to connect to apps, A2A, APIs, and data sources) introduce their own hidden exposures. Orchid uncovers these exposures every day:

* Over-permissioned access: Agents get “god mode” so they don’t fail, and then that privilege becomes the default operating state.
* Untracked usage: Agents can execute sensitive workflows through tools where logs are partial, inconsistent, or not correlated back to a sponsor.
* Static credentials: Hardcoded tokens don’t just “live forever”, they become shared infrastructure across agents, pipelines, and environments.
* Regulatory blind spots: Auditors ask, “who approved access, who used it, and what data was touched?” Dark matter makes those answers slow, or impossible.
* Privilege drift: Agents accumulate access over time because removing permissions is scarier than granting them, until an attacker inherits the drift.

We believe addressing these blind spots aligns with Gartner’s observation that modern AI governance requires identity and access management to tightly converge with information governance. This ensures organizations can dynamically classify data sensitivity and monitor real-time agent behavior instead of relying solely on static credentials.

AI agents aren’t just users without badges. They’re [dark matter](https://139840798.fs1.hubspotusercontent-eu1.net/hubfs/139840798/Buyers%20Guide%20%E2%80%93%20Content.pdf) identities: powerful, invisible, and outside the reach of today’s IAM. And the uncomfortable part: even well-intentioned agents will exploit dark matter. They don’t understand your org chart or...