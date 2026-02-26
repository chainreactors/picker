---
title: Claude Code Flaws Allow Remote Code Execution and API Key Exfiltration
url: https://thehackernews.com/2026/02/claude-code-flaws-allow-remote-code.html
source: The Hacker News
date: 2026-02-25
fetch_date: 2026-02-26T04:12:08.081317
---

# Claude Code Flaws Allow Remote Code Execution and API Key Exfiltration

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Claude Code Flaws Allow Remote Code Execution and API Key Exfiltration](https://thehackernews.com/2026/02/claude-code-flaws-allow-remote-code.html)

**Ravie Lakshmanan**Feb 25, 2026Artificial Intelligence / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhp3ch5lk3LqPFl0TutlBSasJaFa2bNjNdXbIePoE8y76HOmsErmRwXcYUungmePyAK_J_zclibjngwBoTNEB2whRW3-ZAjwKSu1B0VwHyHS_qtKqeivbIdC4HFmSef-lcxWkLXnMs_4HVgmiTNNQSE6UeNt4Ci6lkQaZZlrcwrEy1s4wAVb93CJup8e6r7/s1700-e365/claudecode.jpg)

Cybersecurity researchers have [disclosed](https://blog.checkpoint.com/research/check-point-researchers-expose-critical-claude-code-flaws/) multiple security vulnerabilities in Anthropic's Claude Code, an artificial intelligence (AI)-powered coding assistant, that could result in remote code execution and theft of API credentials.

"The vulnerabilities exploit various configuration mechanisms, including Hooks, Model Context Protocol (MCP) servers, and environment variables – executing arbitrary shell commands and exfiltrating Anthropic API keys when users clone and open untrusted repositories," Check Point Research [said](https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/) in a report shared with The Hacker News.

The identified shortcomings fall under three broad categories -

* **[No CVE](https://github.com/anthropics/claude-code/security/advisories/GHSA-ph6w-f82w-28w6)** (CVSS score: 8.7) - A code injection vulnerability stemming from a user consent bypass when starting Claude Code in a new directory that could result in arbitrary code execution without additional confirmation via untrusted [project hooks](https://code.claude.com/docs/en/hooks-guide) defined in .claude/settings.json. (Fixed in version 1.0.87 in September 2025)
* **[CVE-2025-59536](https://github.com/anthropics/claude-code/security/advisories/GHSA-4fgq-fpq9-mr3g)** (CVSS score: 8.7) - A code injection vulnerability that allows execution of arbitrary shell commands automatically upon tool initialization when a user starts Claude Code in an untrusted directory. (Fixed in version 1.0.111 in October 2025)
* **[CVE-2026-21852](https://github.com/anthropics/claude-code/security/advisories/GHSA-jh7p-qr78-84p7)** (CVSS score: 5.3) - An information disclosure vulnerability in Claude Code's project-load flow that allows a malicious repository to exfiltrate data, including Anthropic API keys. (Fixed in version 2.0.65 in January 2026)

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

"If a user started Claude Code in an attacker-controller repository, and the repository included a settings file that set ANTHROPIC\_BASE\_URL to an attacker-controlled endpoint, Claude Code would issue API requests before showing the trust prompt, including potentially leaking the user's API keys," Anthropic said in an advisory for CVE-2026-21852.

In other words, simply opening a crafted repository is enough to exfiltrate a developer's active API key, redirect authenticated API traffic to external infrastructure, and capture credentials. This, in turn, can permit the attacker to burrow deeper into the victim's AI infrastructure.

This could potentially involve accessing shared project files, modifying/deleting cloud-stored data, uploading malicious content, and even generating unexpected API costs.

Successful exploitation of the first vulnerability could trigger stealthy execution on a developer's machine without any additional interaction beyond launching the project.

CVE-2025-59536 also achieves a similar goal, the main difference being that repository-defined configurations defined through .mcp.json and claude/settings.json file could be exploited by an attacker to override explicit user approval prior to interacting with external tools and services through the Model Context Protocol (MCP). This is achieved by setting the "[enableAllProjectMcpServers](https://code.claude.com/docs/en/settings)" option to true.

"As AI-powered tools gain the ability to execute commands, initialize external integrations, and initiate network communication autonomously, configuration files effectively become part of the execution layer," Check Point said. "What was once considered operational context now directly influences system behavior."

"This fundamentally alters the threat model. The risk is no longer limited to running untrusted code – it now extends to opening untrusted projects. In AI-driven development environments, the supply chain begins not only with source code, but with the automation layers surrounding it."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Anthropic](https://thehackernews.com/search/label/Anthropic), [API Security](https://thehackernews.com/search/label/API%20Security), [artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Code Injection](https://thehackernews.com/search/label/Code%20Injection), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [infor...