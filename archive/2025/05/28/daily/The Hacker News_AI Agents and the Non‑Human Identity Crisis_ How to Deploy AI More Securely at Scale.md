---
title: AI Agents and the Non‑Human Identity Crisis: How to Deploy AI More Securely at Scale
url: https://thehackernews.com/2025/05/ai-agents-and-nonhuman-identity-crisis.html
source: The Hacker News
date: 2025-05-28
fetch_date: 2025-10-06T22:31:22.142885
---

# AI Agents and the Non‑Human Identity Crisis: How to Deploy AI More Securely at Scale

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

# [AI Agents and the Non‑Human Identity Crisis: How to Deploy AI More Securely at Scale](https://thehackernews.com/2025/05/ai-agents-and-nonhuman-identity-crisis.html)

**May 27, 2025**The Hacker NewsArtificial Intelligence / Cloud Identity

[![AI Agents and the Non‑Human Identity](data:image/png;base64... "AI Agents and the Non‑Human Identity")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEij8ENlnoIG0eIXFU1XLnE5qw7jAaXdHCDpbs9-Q8vLv1SveNF2briZgiv1pb5R1MfVlMwCgT9Y6eKRmaSEXlYjhTI6diHtdVYZ-gICjNbxAoxrKy7FS0K44YY-IIl1ssjVP3-6g9JLOhCDHcEi92P5ILc-q3jrnsurypGC3YP0eUkcXlYID-fMv6OgDwM/s790-rw-e365/main.png)

Artificial intelligence is driving a massive shift in enterprise productivity, from GitHub Copilot's code completions to chatbots that mine internal knowledge bases for instant answers. Each new agent must authenticate to other services, quietly swelling the population of non‑human identities (NHIs) across corporate clouds.

That population is already overwhelming the enterprise: many companies now juggle at least **45 machine identities for every human user**. Service accounts, CI/CD bots, containers, and AI agents all need secrets, most commonly in the form of API keys, tokens, or certificates, to connect securely to other systems to do their work. [GitGuardian's State of Secrets Sprawl 2025 report](https://www.gitguardian.com/state-of-secrets-sprawl-report-2025) reveals the cost of this sprawl: over **23.7 million secrets** surfaced on public GitHub in 2024 alone. And instead of making the situation better, repositories with Copilot enabled the leak of secrets **40 percent more often**.

## **NHIs Are Not People**

Unlike human beings logging into systems, NHIs rarely have any policies to mandate rotation of credentials, tightly scope permissions, or decommission unused accounts. Left unmanaged, they weave a dense, opaque web of high‑risk connections that attackers can exploit long after anyone remembers those secrets exist.

The adoption of AI, especially large language models and [retrieval-augmented generation (RAG)](https://blog.gitguardian.com/before-you-deploy-that-llm-nhi/), has dramatically increased the speed and volume at which this risk-inducing sprawl can occur.

Consider an internal support chatbot powered by an LLM. When asked how to connect to a development environment, the bot might retrieve a Confluence page containing valid credentials. The chatbot can unwittingly expose secrets to anyone who asks the right question, and the logs can easily leak this info to whoever has access. Worse yet, in this scenario, the LLM is telling your developers to use this plaintext credential. The security issues can stack up quickly.

The situation is not hopeless, though. In fact, if proper governance models are implemented around NHIs and secrets management, then developers can actually innovate and deploy faster.

**Five Actionable Controls to Reduce AI‑Related NHI Risk**

Organizations looking to control the risks of AI-driven NHIs should focus on these five actionable practices:

1. **Audit and Clean Up Data Sources**
2. **Centralize Your Existing NHIs Management**
3. **Prevent Secrets Leaks In LLM Deployments**
4. **Improve Logging Security**
5. **Restrict AI Data Access**

Let's take a closer look at each one of these areas.

## **Audit and Clean Up Data Sources**

The first LLMs were bound only to the specific data sets they were trained on, making them novelties with limited capabilities. [Retrieval-augmented generation (RAG)](https://blog.gitguardian.com/before-you-deploy-that-llm-nhi/) engineering changed this by allowing LLM to access additional data sources as needed. Unfortunately, if there are secrets present in these sources, the related identities are now at risk of being abused.

Data sources, including project management platform Jira, communication platforms like Slack, and knowledgebases such as Confluence, weren't built with AI or secrets in mind. If someone adds a plaintext API key, there are no safeguards to alert them that this is dangerous. A chatbot can easily become a secrets-leaking engine with the right prompting.

The only surefire way to prevent your LLM from leaking those internal secrets is to eliminate the secrets present or at least revoke any access they carry. An invalid credential carries no immediate risk from an attacker. Ideally, you can remove these instances of any secret altogether before your AI can ever retrieve it. Fortunately, there are tools and platforms, like GitGuardian, that can make this process as painless as possible.

## **Centralize Your Existing NHIs Management**

The quote "If you can not measure it, you can not improve it" is most often attributed to Lord Kelvin. This holds very true for non-human identity governance. Without taking stock of all the service accounts, bots, agents, and pipelines you currently have, there is little hope that you can apply effective rules and scopes around new NHIs associated with your agentic AI.

The one thing all those types of non-human identities have in common is that they all have a secret. No matter how you define NHI, we all define authentication mechanisms the same way: the secret. When we focus our inventories through this lens, we can collapse our focus to the proper storage and management of secrets, which is far from a new concern.

There are plenty of tools that can make this achievable, like HashiCorp Vault, CyberArk, or AWS Secrets Manager. Once they are all centrally managed and accounted for, then we can move from a world of long-lived credentials towards one where rotation is automated and enforced by policy.

### Prevent Secrets Leaks In LLM Deployments

Model Context Protocol (MCP) servers are the new standard for how agentic AI is accessing services and data sources. Previously, if you wanted to configure an AI system to access a resource, you would need to wire it together yourself, figuring it out as you go. MCP introduced the protocol that AI can connect to the service provider with a standardized ...