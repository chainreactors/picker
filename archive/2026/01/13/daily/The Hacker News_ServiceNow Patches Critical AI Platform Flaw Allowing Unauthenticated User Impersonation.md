---
title: ServiceNow Patches Critical AI Platform Flaw Allowing Unauthenticated User Impersonation
url: https://thehackernews.com/2026/01/servicenow-patches-critical-ai-platform.html
source: The Hacker News
date: 2026-01-13
fetch_date: 2026-01-14T03:36:14.748341
---

# ServiceNow Patches Critical AI Platform Flaw Allowing Unauthenticated User Impersonation

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [ServiceNow Patches Critical AI Platform Flaw Allowing Unauthenticated User Impersonation](https://thehackernews.com/2026/01/servicenow-patches-critical-ai-platform.html)

**Jan 13, 2026**Ravie LakshmananVulnerability / SaaS Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxZu-BM7xxcFqhj3Vi07lWWCcD8kJgOH3JTQ4oV6Q3Ngd6GmylXsA52gk2aqSCIfEEHxsmev5EbQPxMr4fWFMLFrvwj1U8VKilr46bj6oN01nCbN08tV9bkft9WpFgSZHVXd_-jrbSTTvlpKrPpvqazA_Cwoh8XUjLKK0SC-r1Plq-2KCpdlDgTHBg1e4H/s790-rw-e365/SERVICENOW-AI.jpg)

ServiceNow has disclosed details of a now-patched critical security flaw impacting its ServiceNow artificial intelligence (AI) Platform that could enable an unauthenticated user to impersonate another user and perform arbitrary actions as that user.

The vulnerability, tracked as **[CVE-2025-12420](https://www.cve.org/CVERecord?id=CVE-2025-12420)**, carries a CVSS score of 9.3 out of 10.0. It has been codenamed **BodySnatcher** by AppOmni.

"This issue [...] could enable an unauthenticated user to impersonate another user and perform the operations that the impersonated user is entitled to perform," the company [said](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2587329) in an advisory released Monday.

The shortcoming was addressed by ServiceNow on October 30, 2025, by deploying a security update to the majority of hosted instances, with the company also sharing the patches with ServiceNow partners and self-hosted customers.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

The following versions include a fix for CVE-2025-12420 -

* Now Assist AI Agents (sn\_aia) - 5.1.18 or later and 5.2.19 or later
* Virtual Agent API (sn\_va\_as\_service) - 3.15.2 or later and 4.0.4 or later

ServiceNow credited Aaron Costello, chief of SaaS Security Research at AppOmni, with discovering and reporting the flaw in October 2025. While there is no evidence that the vulnerability has been exploited in the wild, users are advised to apply an appropriate security update as soon as possible to mitigate potential threats.

"BodySnatcher is the most severe AI-driven vulnerability uncovered to date: Attackers could have effectively 'remote controlled' an organization's AI, weaponizing the very tools meant to simplify the enterprise," Costello told The Hacker News.

In a separate report, AppOmni said the Virtual Agent integration flaw allows unauthenticated attackers to impersonate any ServiceNow user using only an email address, bypassing multi-factor authentication (MFA) and single sign-on (SSO) protections. Successful exploitation could allow a threat actor to impersonate an administrator and execute an AI agent to subvert security controls and create backdoor accounts with elevated privileges.

"By chaining a hardcoded, platform-wide secret with account-linking logic that trusts a simple email address, an attacker can bypass multi-factor authentication (MFA), single sign-on (SSO), and other access controls," Costello [added](https://appomni.com/ao-labs/bodysnatcher-agentic-ai-security-vulnerability-in-servicenow/). "And it's the most severe AI-driven security vulnerability uncovered to date. With these weaknesses linked together, the attacker can remotely drive privileged agentic workflows as any user."

The disclosure comes nearly two months after AppOmni [revealed](https://thehackernews.com/2025/11/servicenow-ai-agents-can-be-tricked.html) that malicious actors can exploit default configurations in ServiceNow's Now Assist generative AI platform and leverage its agentic capabilities to conduct second-order prompt injection attacks.

The issue could then be weaponized to execute unauthorized actions, enabling attackers to copy and exfiltrate sensitive corporate data, modify records, and escalate privileges.

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

[Access Control](https://thehackernews.com/search/label/Access%20Control)[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Identity Security](https://thehackernews.com/search/label/Identity%20Security)[SaaS Security](https://thehackernews.com/search/label/SaaS%20Security)[ServiceNow](https://thehackernews.com/search/label/ServiceNow)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide](data:image/svg+xml;base64... "DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide")

DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide](https://thehackernews.com/2025/12/darkspectre-browser-extension-campaigns.html)

[![⚡ Weekly Recap: IoT Exploits, Wallet Breaches, Rogue Extensions, AI Abuse and More](data:image/svg+xml;base64... "⚡ Weekly Recap: IoT Exploits, Wallet Breaches, Rogue Extensions, AI Abuse and More")

⚡ Weekly Recap: IoT Exploits, Wallet Breaches, Rogue Extensions, AI Abuse and More](https://thehackernews.com/2026/01/weekly-recap-iot-exploits-wallet.html)

[![Kimwolf Android Bot...