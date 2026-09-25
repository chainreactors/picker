---
title: Secrets Sprawl Is an Identity Problem That AI Just Made Impossible to Ignore
url: https://thehackernews.com/2026/09/secrets-sprawl-is-identity-problem-that.html
source: The Hacker News
date: 2026-09-24
fetch_date: 2026-09-25T06:53:34.154964
---

# Secrets Sprawl Is an Identity Problem That AI Just Made Impossible to Ignore

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Secrets Sprawl Is an Identity Problem That AI Just Made Impossible to Ignore](https://thehackernews.com/2026/09/secrets-sprawl-is-identity-problem-that.html)

**The Hacker News**Sep 24, 2026Artificial Intelligence / Application Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8mLbRmwaAgvJunom4dBxBYMz50LUutLJiS6Yz7RPCbZQO1aYXAqFWOga4dCKD3AoenZHxYLpPexLEQ2swJO67vy4xl2_uw1g08lRtETN3hTMLpvafmn5WD4VK2ilpuFaYAdMHHPBRG2yYsyDBins15huubgt2b6pDVnnhW92It8lKHBqOifOLTaNSwho/s1700-nu-rw-lo-l85-e365/keeper.png)

AI coding agents are changing how quickly developers can build and ship software as well as how quickly credentials can become exposed. According to [GitGuardian’s 2026 State of Secrets Sprawl Report](https://www.gitguardian.com/state-of-secrets-sprawl-report-2026), commits identified as AI-assisted are leaking secrets at approximately twice the rate of human-written ones. Most of the fastest-growing categories of leaked credentials are now connected to AI services, meaning the tools meant to advance development are also accelerating the exposure of the keys development relies on.

This isn’t a new vulnerability; what is new is AI changing the scale and pace at which those mistakes can happen. A coding agent can read an entire project, modify files, generate configurations and interact with external services in the time a developer might take to review a single pull request. The main issue isn’t that AI agents sometimes encounter secrets but that many of those secrets were never designed for an environment in which software can act autonomously. AI coding agents are contributing to secrets sprawl by hardcoding credentials into more files and spreading existing ones into more systems than security teams can track and rotate.

## How secrets sprawl has changed in the agentic AI era

Secrets sprawl occurs when credentials such as API keys, tokens and service account credentials accumulate across more systems than an organization can reliably inventory and rotate — hardcoded in source files, pasted into configurations and copied into tickets. Security teams have historically tried to control this sprawl by detecting exposed secrets retroactively; scanners watch repositories, pre-commit hooks catch what they can and security teams rotate credentials after an exposure is discovered. Those controls still matter, but AI agents expose the limitations of depending on detection alone. Agents can read local files, execute commands, call APIs, interact with Model Context Protocol (MCP) servers and modify configuration. Each additional capability creates another place where a credential may be required and another path through which that credential can spread.

This is why organizations should treat secrets sprawl in the agentic AI era as a Non-Human Identity (NHI) problem, not a model-behavior one. Every useful action an agent takes on another system has an identity behind it. When agents query a database, call an API and deploy to staging, some credential authorizes that action. Organizations cannot reliably predict every action an autonomous system will take, but they can control what the identity behind that system is allowed to access.

## How AI coding agents can expose secrets

What makes coding agents useful is also what creates new credential risks: agents need context. An agent that can’t read an entire project doesn’t provide much assistance, especially one that must be re-authorized for every operation. Below are several ways this plays out in practice, demonstrating why organizations should be more careful when granting AI coding agents access to credentials and secrets.

### Agents can access sensitive files in the project context

Developers often keep credentials in .env files and local configurations, left behind from a prior debugging session and never intended for source control. An AI coding agent with broad access to a project may be able to read those files along with the application code it was asked to analyze. To an AI agent, a configuration file containing a production API key is still part of the working environment, so unless access is explicitly limited, the credential may become available to the agent even if it is irrelevant to the task. This shifts security assumptions around developer workstations: Local plaintext credentials are no longer accessible only to the developer and the applications that explicitly reference them but are now also potentially available to software agents operating across the same environment.

### Agent and MCP configurations can contain hardcoded credentials

Setup instructions for agents and MCP servers routinely simplify how developers connect AI applications with databases, APIs and other external systems. Because many integrations require authentication, that simplification often means pasting the credential directly into a configuration file. Since that file never enters version control, it's easy to assume the credential is safe. However, the credential may still exist in plaintext on a developer machine, often in a location the agent has permissions to read.

### Secrets are duplicated across surfaces that teams may not scan

A secret rarely lives in one location; the same key ends up in an .env file, a CI/CD variable or even a Jira ticket while engineers troubleshoot a failed deployment. An AI coding agent connected to those systems introduces another vulnerability: since every copy of a secret authenticates, rotating the one in the repository leaves the rest working. This is why repository scanning alone cannot solve secrets sprawl. A large share of secret incidents can originate completely outside code repositories, with exposures in collaboration and ticketing tools, which is why rotating the copy found in a repository has minimal benefit if the same credential is valid elsewhere.

### Agent credentials are often over-permissioned

An agent needs enough access to perform its wor...