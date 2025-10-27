---
title: Ivanti Endpoint Manager Flaw Actively Targeted, CISA Warns Agencies to Patch
url: https://thehackernews.com/2024/10/ivanti-endpoint-manager-flaw-actively.html
source: The Hacker News
date: 2024-10-04
fetch_date: 2025-10-06T18:54:54.243285
---

# Ivanti Endpoint Manager Flaw Actively Targeted, CISA Warns Agencies to Patch

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Ivanti Endpoint Manager Flaw Actively Targeted, CISA Warns Agencies to Patch](https://thehackernews.com/2024/10/ivanti-endpoint-manager-flaw-actively.html)

**Oct 03, 2024**Ravie LakshmananVulnerability / Endpoint Security

[![Ivanti Endpoint Manager](data:image/png;base64... "Ivanti Endpoint Manager")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmWWN8VTFXWw3fh58oD48h7VhRHQ1gzvqqBljobZRPiyMKaoRjRT0tFT9sXjy0TgQ7uZhLlrqd58GejjwIzqfjd41uUd_Oopqr2jwKm0kjblziaNofgYYkpZTkBT4Xd-59mhiO6BA76eD83kWUJaASzpT40XBBKhz0SIBW9FnuFblsAHCvESYdoO4G70jz/s790-rw-e365/ivanti.jpg)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday [added](https://www.cisa.gov/news-events/alerts/2024/10/02/cisa-adds-one-known-exploited-vulnerability-catalog) a security flaw impacting Ivanti Endpoint Manager (EPM) that the company patched in May to its Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog, based on evidence of active exploitation.

The vulnerability, tracked as **[CVE-2024-29824](https://nvd.nist.gov/vuln/detail/CVE-2024-29824)**, carries a CVSS score of 9.6 out of a maximum of 10.0, indicating critical severity.

"An unspecified SQL Injection vulnerability in Core server of Ivanti EPM 2022 SU5 and prior allows an unauthenticated attacker within the same network to execute arbitrary code," the software service provider [said](https://forums.ivanti.com/s/article/Security-Advisory-May-2024?language=en_US) in an advisory released on May 21, 2024.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Horizon3.ai, which [released](https://www.horizon3.ai/attack-research/attack-blogs/cve-2024-29824-deep-dive-ivanti-epm-sql-injection-remote-code-execution-vulnerability/) a proof-of-concept (PoC) exploit for the flaw in June, said the issue is rooted in a function called RecordGoodApp() within a DLL named PatchBiz.dll.

Specifically, it concerns how the function handles an SQL query statement, thereby allowing an attacker to gain remote code execution via xp\_cmdshell.

The exact specifics of how the shortcoming is being exploited in the wild remains unclear, but Ivanti has since updated the bulletin to state that it has "confirmed exploitation of CVE-2024-29824" and that a "limited number of customers" have been targeted.

With the latest development, as many as four different flaws in Ivanti appliances have come under active abuse within just a month's span, showing that they are a lucrative attack vector for threat actors -

* **[CVE-2024-8190](https://thehackernews.com/2024/09/ivanti-warns-of-active-exploitation-of.html)** (CVSS score: 7.2) - An operating system command injection vulnerability in Cloud Service Appliance (CSA)
* **[CVE-2024-8963](https://thehackernews.com/2024/09/critical-ivanti-cloud-appliance.html)** (CVSS score: 9.4) - A path traversal vulnerability in CSA
* **[CVE-2024-7593](https://thehackernews.com/2024/09/cisa-flags-critical-ivanti-vtm.html)** (CVSS score: 9.8) - An authentication bypass vulnerability Virtual Traffic Manager (vTM)

Federal agencies are mandated to update their instances to the latest version by October 23, 2024, to safeguard their networks against active threats.

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

[CISA](https://thehackernews.com/search/label/CISA)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[endpoint security](https://thehackernews.com/search/label/endpoint%20security)[Ivanti](https://thehackernews.com/search/label/Ivanti)[network security](https://thehackernews.com/search/label/network%20security)[sql injection](https://thehackernews.com/search/label/sql%20injection)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Comet AI Browser Into a Data Thief](https://thehackernews.com/2025/10/cometjacking-one-click-can-turn.html)

[![...