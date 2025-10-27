---
title: Critical Flaw in Telerik Report Server Poses Remote Code Execution Risk
url: https://thehackernews.com/2024/07/critical-flaw-in-telerik-report-server.html
source: The Hacker News
date: 2024-07-27
fetch_date: 2025-10-06T17:46:36.271187
---

# Critical Flaw in Telerik Report Server Poses Remote Code Execution Risk

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

# [Critical Flaw in Telerik Report Server Poses Remote Code Execution Risk](https://thehackernews.com/2024/07/critical-flaw-in-telerik-report-server.html)

**Jul 26, 2024**Ravie LakshmananSoftware Security / Vulnerability

[![Telerik](data:image/png;base64... "Telerik")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEk5OJde2Bknocbc8Rmu6TJfhCVcS3BpI8I3ypFyGJx4kAPET9FVp7dlkFaC1dQ9qgcZgPlyzgatXR9VaT2oqhwKVkoocz6MuD5cS5QNMRpRL0hAoplG80rQAnElZyhNOXnqfcJCDVy_uU9oF3XyEzIZPyz7-g8qNuDK6AQMC5JxxTRFzPq1q1EG-YxPzL/s790-rw-e365/server.png)

Progress Software is urging users to update their Telerik Report Server instances following the discovery of a critical security flaw that could result in remote code execution.

The vulnerability, tracked as **CVE-2024-6327** (CVSS score: 9.9), impacts Report Server version 2024 Q2 (10.1.24.514) and earlier.

"In Progress Telerik Report Server versions prior to 2024 Q2 (10.1.24.709), a remote code execution attack is possible through an insecure deserialization vulnerability," the company [said](https://docs.telerik.com/report-server/knowledge-base/deserialization-vulnerability-cve-2024-6327) in an advisory.

[Deserialization flaws](https://cwe.mitre.org/data/definitions/502.html) occur when an application [reconstructs untrusted data](https://cloud.google.com/blog/topics/threat-intelligence/hunting-deserialization-exploits) that an attacker has control over without adequate validation in place, resulting in the execution of unauthorized commands.

Progress Software said the flaw has been addressed in version 10.1.24.709. As temporary mitigation, it's recommended to change the user for the Report Server Application Pool to one with limited permission.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Administrators can check if their servers are vulnerable to attacks by going through these steps -

* Go to the Report Server web UI and log in using an account with administrator rights
* Open the Configuration page (~/Configuration/Index).
* Select the About tab and the version number will be displayed in the pane on the right.

The disclosure comes nearly two months after the company patched another critical shortcoming in the same software ([CVE-2024-4358](https://thehackernews.com/2024/06/telerik-report-server-flaw-could-let.html), CVSS score: 9.8) that could be abused by a remote attacker to bypass authentication and create rogue administrator users.

On June 13, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) [added](https://www.cisa.gov/news-events/alerts/2024/06/13/cisa-adds-three-known-exploited-vulnerabilities-catalog) the flaw to its Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog, following reports of active exploitation in the wild.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Insecure Deserialization](https://thehackernews.com/search/label/Insecure%20Deserialization)[Progress Software](https://thehackernews.com/search/label/Progress%20Software)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[software security](https://thehackernews.com/search/label/software%20security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

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

[![Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day](data:image/svg+xml;base64... "Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day")

Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day](https://thehackernews.com/2025/10/scanning-activity-on-palo-alto-networks.html)

[![Researchers Warn of Self-Spreading WhatsApp Malware Named SORVEPOTEL](data:image/svg+xm...