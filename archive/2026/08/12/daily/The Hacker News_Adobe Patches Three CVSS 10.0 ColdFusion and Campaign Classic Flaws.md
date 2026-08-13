---
title: Adobe Patches Three CVSS 10.0 ColdFusion and Campaign Classic Flaws
url: https://thehackernews.com/2026/08/adobe-patches-three-cvss-100-coldfusion.html
source: The Hacker News
date: 2026-08-12
fetch_date: 2026-08-13T04:05:21.030244
---

# Adobe Patches Three CVSS 10.0 ColdFusion and Campaign Classic Flaws

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

# [Adobe Patches Three CVSS 10.0 ColdFusion and Campaign Classic Flaws](https://thehackernews.com/2026/08/adobe-patches-three-cvss-100-coldfusion.html)

**Ravie Lakshmanan**Aug 12, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj36vXq6xqWIDA09DIFwTp0gAZyTEpTdUoOrczmHr0NAOmxBDBySv4K6oEmzSup0sZylULeZlzf2unPADh99H5kx8-oktejFUPTM2t5aM6WrdTy99m6Qs12z4A58UYbqU2LhZRa20yY9FGy8FFB-pMvUFsA3MolrrA4nYOWVf9IS42Y0vUn3sMtu0BCty3g/s1700-e365/adobe-cve.jpg)

Adobe has [shipped updates](https://helpx.adobe.com/security.html) to address multiple critical security vulnerabilities impacting ColdFusion, Commerce, and Campaign Classic that, if successfully exploited, could result in arbitrary code execution and privilege escalation.

The most severe of the flaws are listed below -

* **[CVE-2026-48362](https://helpx.adobe.com/security/products/coldfusion/apsb26-90.html)** (CVSS score: 10.0) - An operating system command injection vulnerability in ColdFusion that could lead to arbitrary code execution (Fixed in 2025.0.12 and 2023.0.23)
* **[CVE-2026-48273](https://helpx.adobe.com/security/products/coldfusion/apsb26-90.html)** (CVSS score: 9.9) - An eval injection vulnerability in ColdFusion that could lead to arbitrary code execution (Fixed in 2025.0.12 and 2023.0.23)
* **[CVE-2026-71384](https://helpx.adobe.com/security/products/coldfusion/apsb26-90.html)** (CVSS score: 9.6) - An incorrect authorization vulnerability in ColdFusion that could lead to an application denial-of-service (Fixed in 2025.0.12 and 2023.0.23)
* **[CVE-2026-71362](https://helpx.adobe.com/security/products/magento/apsb26-92.html)** (CVSS score: 9.1) - An incorrect authorization vulnerability in Commerce that could lead to privilege escalation
* **[CVE-2026-71398](https://helpx.adobe.com/security/products/campaign/apsb26-123.html)** (CVSS score: 10.0) - An incorrect authorization vulnerability in Campaign Classic that could lead to arbitrary code execution (Fixed in ACC v7 7.4.4 build 9400)
* **[CVE-2026-27302](https://helpx.adobe.com/security/products/campaign/apsb26-123.html)** (CVSS score: 10.0) - An incorrect authorization vulnerability in Campaign Classic that could lead to arbitrary code execution (Fixed in ACC v7 7.4.4 build 9400)
* **[CVE-2026-48381](https://helpx.adobe.com/security/products/campaign/apsb26-123.html)** (CVSS score: 9.0) - An SQL injection vulnerability in Campaign Classic that could lead to arbitrary code execution (Fixed in ACC v7 7.4.4 build 9400)

The updates for ColdFusion and Campaign Classic have a [Priority 1 rating](https://helpx.adobe.com/security/severity-ratings.html), which refers to vulnerabilities that have a higher risk of being targeted by malicious cyber attacks.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

It's worth noting that the Campaign Classic updates only apply to fully on-premise deployments and to the on-premise components of hybrid deployments. Adobe-hosted instances have already been remediated and require no customer action.

Although there is no evidence of these flaws being exploited in the wild, administrators are recommended to install the update as soon as possible, preferably within 72 hours.

The disclosure comes less than two weeks after Adobe [released](https://thehackernews.com/2026/08/adobe-campaign-classic-cvss-100-flaw.html) patches for a maximum-severity security flaw in Campaign Classic (CVE-2026-48449, CVSS score: 10.0) that could result in arbitrary code execution.

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

[Adobe](https://thehackernews.com/search/label/Adobe), [Application Security](https://thehackernews.com/search/label/Application%20Security), [Code Execution](https://thehackernews.com/search/label/Code%20Execution), [denial of service](https://thehackernews.com/search/label/denial%20of%20service), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [Patch Management](https://thehackernews.com/search/label/Patch%20Management), [privilege escalation](https://thehackernews.com/search/label/privilege%20escalation), [SQL Injection](https://thehackernews.com/search/label/SQL%20Injection), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database](data:image/svg+xml;base64... "Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database")

Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database](https://thehackernews.com/2026/07/azure-cosmos-db-flaw-exposed-platform.html)

[![Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations](data:image/svg+xml;base64... "Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations")

Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations](https://thehackernews.com/2026/07/anthropic-says-claude-mistook-open.html)

[![Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw](data:image/svg+xml;base64... "Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw")

Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw](https://thehackernews.com/2026/07/researchers-report-84...