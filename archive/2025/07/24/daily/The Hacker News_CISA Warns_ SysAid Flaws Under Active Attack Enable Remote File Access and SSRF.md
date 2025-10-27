---
title: CISA Warns: SysAid Flaws Under Active Attack Enable Remote File Access and SSRF
url: https://thehackernews.com/2025/07/cisa-warns-sysaid-flaws-under-active.html
source: The Hacker News
date: 2025-07-24
fetch_date: 2025-10-06T23:56:09.167639
---

# CISA Warns: SysAid Flaws Under Active Attack Enable Remote File Access and SSRF

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

# [CISA Warns: SysAid Flaws Under Active Attack Enable Remote File Access and SSRF](https://thehackernews.com/2025/07/cisa-warns-sysaid-flaws-under-active.html)

**Jul 23, 2025**Ravie LakshmananVulnerability / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFEwQgrE7qAtgq6C1g6hUPYJ3hP_GfXMu8oycJUGPxE8nGAT5nPcoOHXqTk31Oznhh4kkNt0J1diP_RmOXynKOjIub0ZoNOS0DiQ7hB4UE7RWhR4BxBUT57DfLELkc9Tv656RCY4uG9hqc8ZUckT0Rbc2-pgTr7Nh0rCbIrs1F9HRxSOhRrBwHmf6T-moe/s790-rw-e365/sysaid.jpg)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) [added](https://www.cisa.gov/news-events/alerts/2025/07/22/cisa-adds-four-known-exploited-vulnerabilities-catalog) two security flaws impacting SysAid IT support software to its Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog, based on evidence of active exploitation.

The vulnerabilities in question are listed below -

* **[CVE-2025-2775](https://www.cve.org/CVERecord?id=CVE-2025-2775)** (CVSS score: 9.3) - An improper restriction of XML external entity (XXE) reference vulnerability in the Checkin processing functionality, allowing for administrator account takeover and file read primitives
* **[CVE-2025-2776](https://www.cve.org/CVERecord?id=CVE-2025-2776)** (CVSS score: 9.3) - An improper restriction of XML external entity (XXE) reference vulnerability in the Server URL processing functionality, allowing for administrator account takeover and file read primitives

Both shortcomings were [disclosed](https://thehackernews.com/2025/05/sysaid-patches-4-critical-flaws.html) by watchTowr Labs researchers Sina Kheirkhah and Jake Knott back in May, alongside [CVE-2025-2777](https://www.cve.org/CVERecord?id=CVE-2025-2777) (CVSS score: 9.3), a pre-authenticated XXE within the /lshw endpoint.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The three vulnerabilities were addressed by SysAid in the on-premise version 24.4.60 build 16 released in early March 2025.

The cybersecurity firm noted that the vulnerabilities could allow attackers to inject unsafe XML entities into the web application, resulting in a Server-Side Request Forgery (SSRF) attack, and in some cases, remote code execution when chained with [CVE-2024-36394](https://www.cve.org/CVERecord?id=CVE-2024-36394), a command injection flaw revealed by CyberArk last June.

It's currently not known how CVE-2025-2775 and CVE-2025-2776 are being exploited in real-world attacks. Nor is any information available regarding the identity of the threat actors, their end goals, or the scale of these efforts.

To safeguard against the active threat, Federal Civilian Executive Branch (FCEB) agencies are required to apply the necessary fixes by August 12, 2025.

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

[CISA](https://thehackernews.com/search/label/CISA)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Server-Side Request Forgery](https://thehackernews.com/search/label/Server-Side%20Request%20Forgery)[software security](https://thehackernews.com/search/label/software%20security)[SysAid](https://thehackernews.com/search/label/SysAid)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[WatchTowr Labs](https://thehackernews.com/search/label/WatchTowr%20Labs)[XML External Entity](https://thehackernews.com/search/label/XML%20External%20Entity)

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

[![⚡ Weekly Recap: Oracle 0-Day, BitLocker Bypass, VMScape, WhatsApp Worm and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Oracle 0-Day, BitLocker B...