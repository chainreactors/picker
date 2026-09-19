---
title: Microsoft Patches CVSS 10.0 Azure AI Foundry Flaw Enabling Unauthorized Privilege Escalation
url: https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html
source: The Hacker News
date: 2026-09-18
fetch_date: 2026-09-19T07:02:43.432817
---

# Microsoft Patches CVSS 10.0 Azure AI Foundry Flaw Enabling Unauthorized Privilege Escalation

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

# [Microsoft Patches CVSS 10.0 Azure AI Foundry Flaw Enabling Unauthorized Privilege Escalation](https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html)

**Ravie Lakshmanan**Sep 18, 2026Vulnerability / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiML2C2l_2QmIUPPt9Gs6K9nVdVk9WZWhJaeBQjf92a7R0O0ghnhNznkqPHwG1quCmfadrkibl0WJhLioNmbATDXGxPcy6EHuDVvUrcDF_q0m23IQD1CxL0DsMZT2ZnXCtOyGADMztIcBmgQzaAvNQR39JWnvbG085s4q4W01UQnH4g-Yj15_ZKrJXDaOpQ/s1700-nu-rw-lo-l85-e365/ms-azure.jpg)

Microsoft has released fixes for a maximum-severity security flaw in Azure AI Foundry that could be exploited to achieve privilege escalation. No customer action is required.

The vulnerability, tracked as **CVE-2026-85889**, carries a CVSS score of 10.0.

"Missing authentication for critical function in Azure AI Foundry allows an unauthorized attacker to elevate privileges over a network," Microsoft [said](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85889) in a Thursday advisory.

Azure AI Foundry, also called Microsoft Foundry, is an [enterprise platform](https://azure.microsoft.com/en-us/products/ai-foundry) designed to build, deploy, and manage generative artificial intelligence (AI) applications and agents.

The Windows maker credited security researcher Rémy Marot (@R\_Marot) for discovering and reporting the flaw. There is no evidence that the issue has been exploited in the wild.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Also patched by Microsoft in recent days are a number of other critical flaws -

* **[CVE-2026-85885](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85885)** (CVSS score: 9.9) - A command injection vulnerability in Microsoft 365 Copilot that could allow an authorized attacker to elevate privileges over a network
* **[CVE-2026-85878](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85878)** (CVSS score: 9.9) - An improper authorization in Azure Database for PostgreSQL that could allow an authorized attacker to elevate privileges over a network
* **[CVE-2026-87701](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-87701)** (CVSS score: 9.6) - An improper neutralization vulnerability in Azure Cosmos DB that could allow an authorized attacker to elevate privileges over a network

As is typically the case with cloud-based CVEs, Microsoft said the vulnerabilities have already been fully mitigated, and that they require no action for users to take.

Separately, Microsoft has shipped updates for two other vulnerabilities, one of which was originally disclosed last month.

* **[CVE-2026-62721](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62721)** (CVSS score: 7.8) - An insufficient granularity of access control in Windows User-Mode Power Service (UMPS) that could allow an authorized attacker to elevate privileges locally and gain SYSTEM privileges.
* **[CVE-2026-85921](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85921)** (CVSS score: 8.2) - A double free vulnerability in Windows Secure Kernel Mode that could allow an authorized attacker to elevate privileges locally and gain Virtual Trust Level 1 (VTL1) privileges.

Both flaws have been addressed as part of an [out-of-band update](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/09/kb5129194-windows-11-26h1-security-update) for Windows 11, version 26H1 -

* 2026-09 Cumulative Update for Windows 11, version 26H1 for arm64-based Systems (KB5129194) (28000.2956)
* 2026-09 Cumulative Update for Windows 11, version 26H1 for x64-based Systems (KB5129194) (28000.2956)

The disclosure comes as Microsoft patched a [record 974 vulnerabilities](https://thehackernews.com/2026/09/microsoft-patches-record-974-flaws.html) spanning its software portfolio earlier last week. Two of those defects impacting Windows Advanced Local Procedure Call (ALPC) and the Windows Update Stack have come under active exploitation.

According to reports from [Proofpoint](https://thehackernews.com/2026/09/four-spy-groups-used-same-chrome-and.html) and [Volexity](https://thehackernews.com/2026/09/china-linked-hackers-exploit-chrome.html), the ALPC vulnerability has been chained along with two Google Chrome flaws to develop an exploit kit called BlueMoon that has been weaponized by multiple espionage-aligned threat actors to deliver malicious payloads.

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

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [cyber espionage](https://thehackernews.com/search/label/cyber%20espionage), [Microsoft](https://thehackernews.com/search/label/Microsoft), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Windows](https://thehackernews.com/search/label/Windows)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers](https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems....