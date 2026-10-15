---
title: Fake AI Tools Put US Companies at Risk: Inside the Counterfeit Claude, ChatGPT, and Copilot Campaigns
url: https://any.run/cybersecurity-blog/fake-ai-tools-us-companies/
source: Over Security
date: 2026-10-14
fetch_date: 2026-10-15T06:45:15.646581
---

# Fake AI Tools Put US Companies at Risk: Inside the Counterfeit Claude, ChatGPT, and Copilot Campaigns

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* [Guides and tutorials](https://any.run/cybersecurity-blog/guides/)
* [Research](https://any.run/cybersecurity-blog/research/)
* Categories
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [SOC & MSSP Strategy](https://any.run/cybersecurity-blog/category/soc-mssp-strategy/)
  + [Customer Success Story](https://any.run/cybersecurity-blog/category/customer-success/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
* [Write for us](https://any.run/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/?register)
* [Register for free](https://app.any.run/?register)

* + Search

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* [Guides and tutorials](https://any.run/cybersecurity-blog/guides/)
* [Research](https://any.run/cybersecurity-blog/research/)
* Categories
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [SOC & MSSP Strategy](https://any.run/cybersecurity-blog/category/soc-mssp-strategy/)
  + [Customer Success Story](https://any.run/cybersecurity-blog/category/customer-success/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
* [Write for us](https://any.run/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/?register)
* [Register for free](https://app.any.run/?register)

* + Search

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* + Search

![Fake AI Tools Put US Companies at Risk: Inside Counterfeit Claude, ChatGPT, and Copilot](https://any.run/cybersecurity-blog/wp-content/uploads/2026/10/Fake-AI-scaled.png)

[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

# Fake AI Tools Put US Companies at Risk: Inside Counterfeit Claude, ChatGPT, and Copilot

October 14, 2026

[Add comment](#comments-23673)
2708 views
20 min read

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

Fake AI Tools Put US Companies at Risk: Inside Counterfeit Claude, ChatGPT, and Copilot

#### Recent posts

* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/10/Fake-AI-1024x497.png)

  #### Fake AI Tools Put US Companies at Risk: Inside Counterfeit Claude, ChatGPT, and Copilot

  2708
  0](https://any.run/cybersecurity-blog/fake-ai-tools-us-companies/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/10/cover-1024x497.png)

  #### What's Really Attacking Your Industry? Insights From 74K Sandbox Analyses

  3591
  0](https://any.run/cybersecurity-blog/threat-data-for-enterprises/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/10/Webinar-w-Elastic-1024x497.png)

  #### Making Threat Intelligence Work for SOC Teams: ANY.RUN & Elastic Webinar Insights

  11173
  0](https://any.run/cybersecurity-blog/ti-feeds-elastic-webinar/)

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

Fake AI Tools Put US Companies at Risk: Inside Counterfeit Claude, ChatGPT, and Copilot

[ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=fake-ai-tools-us-companies&utm_term=141026&utm_content=linktolanding) researchers tracked **fake AI tool campaigns** that impersonate Claude, ChatGPT, GitHub Copilot, Gemini, and other AI brands to plant infostealers, take over browser sessions, and phish business accounts. Between April 15 and October 5, 2026, **1,258 public sandbox analyses** were tied to these campaigns, and the USA was the second-largest source of submissions after India.

The attacks share one trait: the employee performs the decisive step. They paste an “install command,” run a convincing installer, or sign in to a fake window. That can put source code, cloud and AI API keys, active business sessions, ad accounts, and billing access at risk, turning a single user action into potential data exposure, account compromise, financial loss, or disruption to development and marketing operations.

Below, we break down five attack patterns, the numbers behind them, and the signals SOC teams can hunt for.

## Key Takeaways

* **Fake AI is a sustained campaign theme, not a one-off.** We linked 1,258 public sandbox analyses to fake-AI campaigns between April 15 and October 5, 2026, with more than 100 analyses every month from April to September, keeping employee and SOC exposure consistently high.
* **Claude and ChatGPT are the brands attackers wear most.** Together they account for 81% of those analyses: Claude 601 (48%) and OpenAI ChatGPT and Codex 418 (33%), making widely adopted AI brands a recurring path into corporate environments.
* **American organizations are squarely in scope.** The US ranks first for both the fake “Download Claude” campaign and the ChatGPT-themed chains. Across all fake AI activity analyzed, US submitters account for 69 of 422 country records in [Threat Intelligence Lookup](https://any.run/threat-intelligence-lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=fake-ai-tools-us-companies&utm_term=141026&utm_content=linktotilookuplanding), or 16%, ranking second overall after India.
* **The victim runs the attack.** At least 45% of the analyses belong to campaigns that tell the user to paste a command into the Run dialog, PowerShell, or Terminal, turning routine user actions into an execution path that can bypass traditional controls.
* **Trusted platforms carry the lures.** We saw lures on GitHub, GitLab Pages, Cloudflare Pages, Google Sites, claude.ai, and chatgpt.com, promoted through Google Ads and search results, making simple domain blocking less effective.

## Fake AI Threat Overview

Fake AI campaigns are effective because they blend into normal employee behavior. Searching for a new AI app, following setup instructions, opening a shared chat, or connecting a business account can all look routine, which gives attackers room to move past traditional email-focused defenses.

What makes these campaigns especially relevant for organizations is the type of access they can reach. Developers may expose source code, cloud credentials, or API keys, while marketing and business teams can hold access to advertising, billing, and other high-value accounts.

| Attribute | Details |
| --- | --- |
|  |  |
| --- | --- |
| Observed period | April 15–October 5, 2026 |
| Activity analyzed | 1,258 public sandbox analyses linked to fake AI-themed activity |
| Most impersonated brands | Claude, ChatGPT, Codex, GitHub Copilot, Gemini, Ollama, OpenClaw, Perplexity, and Manus |
| Primary delivery channels | Search results, Google Ads, shared AI chats and artifacts, fake download pages, and email invitations |
| Main user actions | Pasting commands into PowerShell or Terminal, running installers, or entering credentials into fake sign-in windows |
| Observed outcomes | Infostealer and RAT delivery, browser-session theft, credential phishing, and business-account co...