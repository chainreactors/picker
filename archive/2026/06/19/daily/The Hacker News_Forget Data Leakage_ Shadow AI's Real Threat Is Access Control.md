---
title: Forget Data Leakage: Shadow AI's Real Threat Is Access Control
url: https://thehackernews.com/2026/06/forget-data-leakage-shadow-ais-real.html
source: The Hacker News
date: 2026-06-19
fetch_date: 2026-06-20T06:14:43.146962
---

# Forget Data Leakage: Shadow AI's Real Threat Is Access Control

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Forget Data Leakage: Shadow AI's Real Threat Is Access Control](https://thehackernews.com/2026/06/forget-data-leakage-shadow-ais-real.html)

**The Hacker News**Jun 19, 2026Agentic AI / SaaS Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6R48ZeaNtIzMVc6atNjuxbNYFUfiFCJ_cE1qE_85yGOOavsX0ijvQGdv9QZ2-4Lky8mTOPhrNIydUvLS2DtGkkFXYJFRTT99Vbb03s3Rtk9pTariHdQ2on2RGxiAsMQnySj7AJfxUtBxO1aJTupjkQvDvt5jp1klznY9_WHckqm64F-BbCtCR2UoJ968/s1700-e365/tines-main.jpg)

The first wave of enterprise AI concern was straightforward. It was simply employees pasting sensitive data into public AI tools. Security teams responded with usage policies, domain blocks, and data loss prevention rules. That response made sense at the time.

It doesn't fit the problem anymore.

Shadow AI has shifted from a data leakage concern to an access control problem. The threat isn't about what employees type into AI tools. It's about which AI agents are running inside the organization, what enterprise systems they're connected to, and what actions they're authorized,or not, to take.

## **From passive tools to active actors**

Employees and business units are building AI agents at a pace most security teams can't keep track of. Custom assistants, coding agents, workflow automations, and agentic applications are being created across departments with some in sanctioned platforms, but many through browser extensions, SaaS-native features, developer tools, MCP servers, endpoint-based agents, and custom scripts. Many start as quick experiments. Some become embedded in critical business processes within days.

The risk profile of these agents is fundamentally different from traditional shadow IT. An unsanctioned SaaS application is a destination for data. An AI agent is an actor that can call APIs, use stored credentials, retrieve records, modify configurations, trigger downstream workflows, and take actions in production systems, often without a human explicitly authorizing each step.

An employee pasting a customer record into a public AI tool is a data leakage incident. A custom AI agent connected to Salesforce, Snowflake, GitHub, Gong, and Slack is an access control incident waiting to happen. It could expose data, but it could also perform read, write, and delete actions on that data. It may also run on service accounts with permissions nobody audited and stay active six months after the employee who built it changed roles or left the company. [New research from Token Security and the Cloud Security Alliance](https://www.token.security/lp/autonomous-but-not-controlled-ai-security-data-report-csa?utm_source=thehackernews&utm_medium=3rdparty&utm_campaign=thehackernews&utm_content=june-19) maps exactly how widespread this exposure has become.

## **Why existing controls don't reach it**

Most enterprise security controls were designed for human identities and deterministic workloads. IAM policies, DLP rules, and network monitoring assume predictable behavior and defined access paths. AI agents break those assumptions.

An agent tasked with resolving a failed deployment might read logs, query monitoring systems, modify infrastructure configurations, open tickets, trigger automation pipelines, and notify engineering teams, all in sequence, all using the same inherited credentials. To avoid breaking workflows, developers grant broad permissions upfront. Those permissions accumulate. Agents inherit creator-level privileges, temporary access becomes permanent, and security and identity teams lose visibility into what those identities are actually doing.

Blocking public AI domains doesn't reach any of this. By the time an agent has credentials to enterprise systems, the boundary has already been crossed. [Automated remediation of non-human identities](https://www.token.security/product/nhi-automation-and-remediation?utm_source=thehackernews&utm_medium=3rdparty&utm_campaign=thehackernews&utm_content=june-19) is where that gap gets closed.

## **What a real shadow AI inventory looks like**

Discovering shadow AI requires looking across the environments where agents actually live, such as AI platforms, SaaS apps with built-in automation, cloud accounts, developer tools, endpoints, and identity providers. Here are six questions to define whether security teams have real control.

1. Where are agents being created or installed? This includes obvious AI platforms but also coding assistants, SaaS-native agent features, local developer tools, and internal applications that have quietly added AI capabilities.
2. Who owns each agent, and who can use it? Without ownership, there's no accountability. An agent built for a three-person finance team that gets shared across the organization carries a very different risk profile than one scoped to a single user.
3. What resources and services is the agent connected to? An agent can appear harmless at the platform level while holding connections to sensitive databases or production systems through credentials that were granted informally and never reviewed.
4. What identities and secrets does it use? Agents authenticate through service accounts, API keys, OAuth tokens, cloud IAM roles, and long-lived secrets. Each credential type carries different risks.
5. What is the agent’s intent and what has it actually done? Configuration alone doesn't show whether an agent is reading data, writing records, or accessing systems outside its intended scope. Understanding intent and behavioral context is required to prioritize response.
6. Is the agent still active? Token Security's Agentic Pulse data found that 65.4% of agentic chatbots have never been used since creation, but their credentials remain active. Dormant agents with live access are a persistent and underappreciated exposure.

## **The maturity curve to ensure agentic AI security**

Most organizations are at the beginning of this and have little to no agent inventory. The next step is to gain partial visibility to know...