---
title: Sekoia Honeypot Captures an Attack on GenAI Infrastructure
url: https://www.sekoia.com/blog/a-honeypots-tale-deconstructing-an-attack-on-genai-infrastructure
source: Over Security
date: 2026-10-19
fetch_date: 2026-10-20T06:53:36.206686
---

# Sekoia Honeypot Captures an Attack on GenAI Infrastructure

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

* Solutions
* Platform
* Partners
* Company
* Resources

[en](/blog/a-honeypots-tale-deconstructing-an-attack-on-genai-infrastructure)

[fr](/fr)

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

[en](/blog/a-honeypots-tale-deconstructing-an-attack-on-genai-infrastructure)

[fr](/fr)

Solutions

Tailored cybersecurity built for your specific challenges and industry

By Use Case

[SIEM replacement](/solutions/siem-replacement)[Stack integration](/solutions/cybersecurity-stack-integration)[Continuous threat detection](/solutions/real-time-threat-detection)[Automated incident response](/solutions/automated-incident-response)[Alert fatigue relief](/solutions/reduce-alert-fatigue)

By Vertical

[Healthcare](/solutions/healthcare)[Technology](/solutions/technology)[Energy & Utilities](/solutions/energy-utilities)[Government](/solutions/government)[Manufacturing](/solutions/manufacturing)[MSSP](/solutions/mssp)

Platform

Give your analysts their time back

UNIFIED Platform

[Autonomous SOC Platform](/platform)[Cyber Threat Intelligence](/platform/intelligence)

PLATFORM IntegrationS

[Integrations catalog](/integrations)

Products

[Sekoia Defend

SIEM](/platform/defend)[Sekoia Intelligence

CTI](/platform/intelligence)[Sekoia Digital Risk

DRP](/platform/digital-risk)[Sekoia Reveal

CAASM](/platform/reveal)[Sekoia Elevate

AI SOC agents](/platform/elevate)

See Sekoia in action

Curious about what our platform can do? Take a self-guided tour and explore the features that security teams rely on.

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)

Partners

Join a powerful ecosystem of cyber experts, continuous training, and shared success

Partners

[Our business partners](/our-business-partners)[Why become a partner?](/why-become-a-business-partner)[Partner portal](https://sekoia.introw.io/)

Services

[Training courses](/training-courses)[Sekoia university](https://training.sekoia.com/account/login/)

Join our business partner ecosystem

Grow your business alongside Sekoia. Join a thriving network of partners and unlock new revenue opportunities in cybersecurity.

[Become a partner](/become-a-partner)

Why Sekoia?

Our story, our world-class team, and our latest updates

About us

[About Sekoia](/about)[About TDR team](/about-threat-detection-research-team)[Customer reviews](/our-customers)[Join us](/join-us)

Newsroom

[Newsroom](/newsroom)[Brand kit](https://share.sekoia.com/s/MH3CJ6Q8o5BC6Q6)

Resources

Deepen your cyber knowledge with expert insights, reports, and real-world case studies

Blog

[Blog](/blog)

glossary

[Cyberglossary](/glossary)

Resource center

[Case studies](/resources-category/case-studies)[Solution briefs](/resources-category/solution-briefs)[Webinars](/resources-category/webinars)[Reports](/resources-category/reports)

[View all](/resources)

Stay ahead of cyber threats

Get the latest insights on threat intelligence, SOC best practices and Sekoia product updates delivered straight to your inbox.

[Subscribe](https://go.sekoia.com/Preference-center-EN.html)

Clear

Solutions

Platform

Integrations

Partners

Company

Newsroom

Blog

Glossary

Case studies

Solution briefs

Webinars

Reports

Others

Recommended

![]()

The new era of cybersecurity: AI-guided SOC and human-machine collaboration.

The new era of cybersecurity: AI-guided SOC and human-machine collaboration.✕

Show more

![](https://cdn.prod.website-files.com/69aaa27bc8027f082ae84b86/6ab62024f7d63abe309a94fd_search-placeholder.svg)![](https://cdn.prod.website-files.com/69aaa27bc8027f082ae84b86/6ab62024f7d63abe309a94fd_search-placeholder.svg)![](https://cdn.prod.website-files.com/69aaa27bc8027f082ae84b86/6ab62024f7d63abe309a94fd_search-placeholder.svg)![](https://cdn.prod.website-files.com/69aaa27bc8027f082ae84b86/6ab62024f7d63abe309a94fd_search-placeholder.svg)![](https://cdn.prod.website-files.com/69aaa27bc8027f082ae84b86/6ab62024f7d63abe309a94fd_search-placeholder.svg)![](https://cdn.prod.website-files.com/69aaa27bc8027f082ae84b86/6ab62024f7d63abe309a94fd_search-placeholder.svg)![](https://cdn.prod.website-files.com/69aaa27bc8027f082ae84b86/6ab62024f7d63abe309a94fd_search-placeholder.svg)

Recent

Recommended

[Home](/)[Blog](/blog)

A honeypot's tale: Deconstructing an attack on GenAI infrastructure

All categories & topics

[Threat Research & Intelligence](/category/threat-research-intelligence)

[Detection Engineering](/category/detection-engineering)

[SOC Insights & Other News](/category/soc-insights-other-news)

[Product News](/category/product-news)

[TDR Team](/category/tdr)

[AI](/category/ai-security)

[Cloud](/category/cloud-security)

[Integrations](/category/integrations)

[Compliance](/category/compliance)

[APT](/category/apt)

[Cybercrime](/category/cybercrime)

[Phishing](/category/phishing)

[Ransomware](/category/ransomware)

[Stealer](/category/stealer)

[ClickFix](/category/clickfix)

Summarize with AI

Share

Copied !

[Threat Research & Intelligence](/category/threat-research-intelligence)

[TDR Team](/category/tdr)

[Cybercrime](/category/cybercrime)

[AI](/category/ai-security)

19 min

October 19, 2026

By

[Jérémy Scion](/authors/jeremy-scion)

By

[TDR Team](/authors/threat-detection-research-team)

# A honeypot's tale: Deconstructing an attack on GenAI infrastructure

Sekoia's TDR team ran a decoy Flowise server to study attacks on GenAI platforms. One threat actor stole its credentials and tried to misuse its AI agent.

![Illustration of a cyberattack on generative AI infrastructure, showing a hooded attacker chained to connected systems, robotic hands, captured language models, SQL data, documents, canary tokens, vector databases, and gambling-themed targets.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6acf8f61fcffd41c1d7c8ef2_blog-a-honeypots-tale-deconstructing-an-attack-on-genai-infrastructure-img-cover%20(1).webp)

## Key takeaways

Attackers are increasingly hijacking GenAI orchestration platforms. Here's everything our TDR team discovered...

* Emergence of AI orchestration platforms as high-value targets: Platforms like Flowise hold central positions connecting LLMs to enterprise databases, credentials, and API tools, making them attractive targets for credential theft and resource exploitation.
* Weaponisation of LLMs for offensive analysis: The attacker attempted to turn the AI agent into an interactive offensive assistant, submitting real-world reconnaissance data (Nightingale/Redis infrastructure) to generate custom exploitation playbooks and target analysis.
* Threat actor profiling and context: Linguistic indicators and observed tradecraft suggest a Chinese-speaking threat actor targeting unregulated online gambling (iGaming) infrastructure. The activity focused on identifying exploitable vulnerabilities in regional deployments, particularly in Southeast Asia, and is more consistent with opportunistic cybercrime than with a bespoke APT operation.

> This post was originally distributed as a private FLINT report to our customers on 7 September 2026.

## Introduction

As part of a continuous vulnerability monitoring routine, Sekoia's [Threat Detection & Research (TDR) team](/about-threat-detection-research-team) deploys and operates honeypots in multiple locations worldwide to capture emerging exploitation trends.

Over the past few months, [GenAI](/glossary/generative-ai) orchestration platforms have become attractive targets because they concentrate API keys, enterprise data, and access to external tools. Recently reported campaigns1 show that attackers are increasingly hijacking these platforms to consume LLM resources, steal credentials, or abuse agent capabilities.

In this context, the Flowise orchestration solution represents an attractive target. It is affected by several recent critical vulnerabilities that enable remote code execution, notably through the unsaf...