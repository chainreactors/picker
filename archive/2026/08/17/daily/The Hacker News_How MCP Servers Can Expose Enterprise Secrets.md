---
title: How MCP Servers Can Expose Enterprise Secrets
url: https://thehackernews.com/2026/08/how-mcp-servers-can-expose-enterprise.html
source: The Hacker News
date: 2026-08-17
fetch_date: 2026-08-18T02:54:02.580576
---

# How MCP Servers Can Expose Enterprise Secrets

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [How MCP Servers Can Expose Enterprise Secrets](https://thehackernews.com/2026/08/how-mcp-servers-can-expose-enterprise.html)

**The Hacker News**Aug 17, 2026AI Security / Identity Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmy_mE0_W-wEeuppBUYhS19P_uTo6RifgrGEV5eLim_B6KkhI_BO5wSL930qS_NCD6aR7nL5mAizU4RAfinzkWhz-oq1wCnHszL6C25H0Sj_MahJIBsr7lw_wzJ7xZ4YF7-GVJJO0L1wxe8LQXv3rHuLV3vbuDUEQ9D7vXa6D4zK6ARD1aFmiQv4fka5Y/s1700-e365/keeper.png)

MCP servers can expose enterprise secrets through plaintext configuration files, over-permissioned access and prompt injection, often before security teams even know the server is running. As more organizations adopt AI agents into their systems, that exposure can silently become a major gap in MCP server security. The Model Context Protocol (MCP) allows AI agents to reach the tools and data, including internal documentation and cloud infrastructure, that form the foundation of enterprise systems. Behind that convenience, the MCP server connecting those tools and data to enterprise systems typically holds the keys to everything it touches: credentials, service account keys, API tokens and other secrets. Every organization should now question what secrets they are handing to AI and how well those secrets are protected once they reach an MCP server.

## What is Model Context Protocol (MCP)?

Model Context Protocol (MCP) is an open standard, originally introduced by Anthropic, that allows AI assistants to connect to external tools and data. Instead of being constrained to a model’s existing knowledge, an AI agent can use MCP to reach live systems, pulling a record from a database, opening a file or calling an API. What makes this work is the MCP server: a small program that sits between the AI and the system it wants to use, exposing the specific actions the AI agent is allowed to perform. With the MCP server serving as the middleman, this is where the greatest risk lies because, to act on a system, an MCP server requires that system’s credentials.

Agents no longer just produce answers; they take action by retrieving sensitive data and deciding which tools to call using Non-Human Identities (NHIs) like API keys and tokens. Because [MCP turns AI agents into active identities](https://www.keepersecurity.com/blog/2026/01/05/how-the-model-context-protocol-is-redefining-zero-trust-for-ai-agents/) operating across enterprise systems, a leaked secret doesn’t just expose data; it also grants an attacker the ability to act on it.

## Ways MCP servers may expose secrets

The convenience of MCP comes with a catch: The same server that allows an AI agent to do meaningful work is also a hub for credentials. Since MCP is innovative and moving fast, many servers are built and deployed without the security measures that should be expected for something holding production keys. Here are some of the most common ways secrets can end up exposed in MCP servers.

### Plaintext credentials in config files

MCP servers routinely store the tokens and keys they need in local configuration files and often in plaintext. In many setups, getting a server running means pasting in a configuration string that contains the credentials themselves. If that file is left on a disk, it’s very likely to be overlooked, copied between machines or committed to a Git repository by accident. Once an attacker reaches that server, everything it holds is readable.

### Credential sprawl across ungoverned servers

Without a central location to store secrets, every AI agent ends up managing its own. The same credentials — including API keys and tokens — get scattered across config files and environment variables, and duplicate copies pile up across development, staging and production. Because no one has a full inventory of these secrets, they rarely get rotated, leaving them valid and static indefinitely. Each scattered, long-lived secret can be stolen by an attacker, creating another potential entry point for a breach.

### Prompt injection

Not every leak requires an attacker to break in. Because AI agents read and act on the material they are given, an attacker may hide instructions within a document, support ticket or web page the agent accesses. As a result, the agent may follow those hidden directions, treating them as legitimate commands in what is referred to as prompt injection. Agents can be tricked into misusing their tools or handing over the secrets they were trusted to protect.

### Over-permissioning

To avoid running into authorization errors while building, developers often grant an MCP server broad permissions and move on. However, those generous scopes tend to ship to production if they are forgotten about. When least privilege isn’t enforced, an AI agent can reach far beyond what’s necessary for its task, meaning any single compromise exposes much more than it should have.

### Exposed-server risk

Anyone can publish an MCP server, which is a supply chain issue waiting to happen. Connecting to an untrusted one can turn against you, as [CVE-2025-6514](https://nvd.nist.gov/vuln/detail/CVE-2025-6514) demonstrated. In mcp-remote (an OAuth proxy downloaded over 400,000 times that runs on the client machine), a malicious server could trigger OS command injection, leading to remote code execution on the machine running the proxy and granting attackers access to steal its credentials.

## How to secure enterprise secrets on MCP servers

MCP changes where secrets live and who reaches them, but the measures for protecting them must be applied intentionally to this new AI layer. Here are several best practices that counter the exposure paths:

* **Stop hardcoding secrets and centralize them.** Pulling credentials out of config files, environment variables and source code and placing them into a single managed store is the solution for both plaintext exposure and credential sprawl. Instead of secrets sprawl across servers, AI agents retrieve what they nee...