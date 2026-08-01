---
title: Chinese Hacker Commands DeepSeek via Telegram to Launch Autonomous Attacks
url: https://thehackernews.com/2026/07/chinese-hacker-commands-deepseek-via.html
source: The Hacker News
date: 2026-07-31
fetch_date: 2026-08-01T05:13:35.487384
---

# Chinese Hacker Commands DeepSeek via Telegram to Launch Autonomous Attacks

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

![cybersecurity](data:image/svg+xml;base64...)

# [Chinese Hacker Commands DeepSeek via Telegram to Launch Autonomous Attacks](https://thehackernews.com/2026/07/chinese-hacker-commands-deepseek-via.html)

**Swati Khandelwal**Jul 31, 2026Artificial Intelligence / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2dGysHIR6yJWx6hMxq6lAct7fi4YTury_WDkrcenDv-psd-fU7I8K3RbM6Blox_5OE3MQojew5bnPamtI_DPzdBX6fOk295hhQh6rBkA2f9a1sN7t7ZbSyU-kWdLoIb7XnseOHKPmLOGRb9wRRvmV0scVZ4rhMtxSmqOLZmZIUjtg_IHT4FBg5gzeX50/s1700-e365/deepseek-telegram.jpg)

Palo Alto Networks' Unit 42 says a Chinese-speaking threat actor used DeepSeek through the open-source Hermes Agent framework to launch attacks autonomously.

After an initial Telegram instruction, the agent found internet-facing systems and selected public exploits. The researchers recovered no further operator input in the session.

The operator, tracked through the aliases **knaithe** and **KnYuan**, launched exploitation attempts against more than 460 targets using autonomous and conventional workflows.

Unit 42 described seven exploit tracks. They span eight Common Vulnerabilities and Exposures (CVE) identifiers because the n8n chain combines two vulnerabilities. The DeepSeek-led attacks against Langflow and n8n failed because the exposed systems did not meet the exploits' configuration requirements.

In separate manual operations, Unit 42 reported data exfiltration from three organizations through the [NetScaler memory-overread flaw CVE-2026-3055](https://thehackernews.com/2026/03/citrix-netscaler-under-active-recon-for.html) and command execution on 11 Marimo instances through [CVE-2026-39987](https://thehackernews.com/2026/04/marimo-rce-flaw-cve-2026-39987.html). Yet it later says it could confirm only three successfully exploited targets across the entire operation. The report does not reconcile the two statements. The Hacker News has contacted Palo Alto Networks for clarification and will update the story with any response.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The agent checked versions, downloaded exploits, abandoned an unproductive path, and chose another vulnerability based on severity, deployment scale, and apparent exploitability. Organizations should patch exposed Langflow, n8n and Marimo systems, along with customer-managed NetScaler ADC or Gateway appliances configured as Security Assertion Markup Language (SAML) identity providers. They should also remove unnecessary public access to workflow and notebook interfaces.

Hermes Agent exposed the operation by starting python3 -m http.server 8888 from /home/worker. The unintended HTTP server made the actor's model configurations, application programming interface (API) keys, exploit scripts, target lists, shell history, and autonomous-session logs accessible, according to the [company's report](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/).

DeepSeek was the primary reasoning model inside [Hermes Agent](https://thehackernews.com/2026/07/hacker-runs-hermes-ai-agent-unattended.html), which supplied terminal access, reusable skills and unattended execution. Unit 42 found limited use of Claude Code and Qwen Code. It also found signs of Codex use in exploit-development directories, but could not verify actual use because the chat logs were not preserved.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEithPM9Z1AeYtLol9Y4JSjXa5e6aRwWZDKIJpUNjfe3uRVE9j5cEJNrSTmEKrk49PtPMXhEJZKONlUnuSXQMramQzAL1jbOd9YWlWCdE1VmykSXJoyKLkasBB9byLtAL4aKjP1PDyNASJy-4lzU5Z97J3PkvJA7Yufo1pzbpn8rgaI0IeYHWrkYCVuzT0Q/s1700-e365/telegram-ai.jpg)

The framework's own [documentation](https://github.com/NousResearch/hermes-agent) confirms that it can operate through Telegram, run commands, and schedule unattended tasks.

In a recovered May 2026 session, DeepSeek downloaded a public exploit for [the Langflow code-injection flaw](https://github.com/langflow-ai/langflow/security/advisories/GHSA-vwmf-pq79-vjvx) [CVE-2026-33017](https://thehackernews.com/2026/03/critical-langflow-flaw-cve-2026-33017.html), enumerated 84 instances through FOFA, and found one target running version 1.3.4. Langflow is an artificial intelligence (AI) agent and workflow builder. The attack stopped because the system had neither auto\_login enabled nor a usable public flow identifier.

The agent then surveyed 10 product families, searched GitHub for recent proof-of-concept repositories and selected n8n, the workflow automation platform. It obtained a chain combining the unauthenticated file-access flaw [CVE-2026-21858](https://thehackernews.com/2026/01/critical-n8n-vulnerability-cvss-100.html) with the expression-injection issue [CVE-2025-68613](https://thehackernews.com/2025/12/critical-n8n-flaw-cvss-99-enables.html). FOFA returned 25,209 n8n systems in China during the session.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

DeepSeek sampled about 100, probed roughly 40 and identified three running vulnerable versions. One target exposed three form endpoints, but all required authentication. More than 50 additional targets also lacked a usable public form, so no n8n system was compromised.

Langflow fixed CVE-2026-33017 in version 1.9.0. n8n fixed [CVE-2026-21858 in version 1.121.0](https://github.com/n8n-io/n8n/security/advisories/GHSA-v4pr-fm98-w9pg). It fixed [CVE-2025-68613 in versions 1.120.4, 1.121.1, and 1.122.0](https://www.cve.org/CVERecord?id=CVE-2025-68613). Version 1.121.1 is therefore the earliest release that addresses both flaws used in the attempted chain. Marimo fixed [CVE-2026-39987 in version 0.23.0](https://github.com/marimo-team/marimo/security/advisories/GHSA-2679-6mx9-h9xc).

Citrix says CVE-2026-3055 affects customer-managed NetScaler ADC and Gateway appliances configured as SAML identity providers. Administrators can check the appliance configuration for add authentication samlIdPProfile .\* and install the fixed builds listed in the company's [security bulletin](https://support.citrix.com/external/article/CTX696300/netscaler-adc-and-netscaler-gateway-secu.html).

Unit 42 assesses the operator to be based in Zhuhai, China. Public material is consistent with, but does not...