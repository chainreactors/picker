---
title: Apache OFBiz Update Fixes High-Severity Flaw Leading to Remote Code Execution
url: https://thehackernews.com/2024/09/apache-ofbiz-update-fixes-high-severity.html
source: The Hacker News
date: 2024-09-07
fetch_date: 2025-10-06T18:31:50.303744
---

# Apache OFBiz Update Fixes High-Severity Flaw Leading to Remote Code Execution

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

# [Apache OFBiz Update Fixes High-Severity Flaw Leading to Remote Code Execution](https://thehackernews.com/2024/09/apache-ofbiz-update-fixes-high-severity.html)

**Sep 06, 2024**Ravie LakshmananCybersecurity / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWHmqqU7IY8lGXVl0blicq17FHTd_BrWSZqgB9wacCMWtpTlzi-I5BAwGw1Cu1Vf7_RsKvZq1QLk941EluSbsuPPH-bgUZ7yCyd_mzGPEvuwSWsXoZNNPtRtEeajFQVdm7HrzZ386gHdpl9fN7oRj6TTr1UUVFiV3G_fLgazfaqGtHz46A4oLyCbeQzmu8/s790-rw-e365/apache.jpg)

A new security flaw has been [addressed](https://ofbiz.apache.org/security.html) in the Apache OFBiz open-source enterprise resource planning (ERP) system that, if successfully exploited, could lead to unauthenticated remote code execution on Linux and Windows.

The high-severity vulnerability, tracked as [CVE-2024-45195](https://nvd.nist.gov/vuln/detail/CVE-2024-45195) (CVSS score: 7.5), affects all versions of the software before 18.12.16.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"An attacker with no valid credentials exploit missing view authorization checks in the web application to execute arbitrary code on the server," Rapid7 security researcher Ryan Emmons [said](https://www.rapid7.com/blog/post/2024/09/05/cve-2024-45195-apache-ofbiz-unauthenticated-remote-code-execution-fixed/) in a new report.

It's worth noting that CVE-2024-45195 is a bypass for a [sequence of issues](https://thehackernews.com/2024/08/new-zero-day-flaw-in-apache-ofbiz-erp.html), CVE-2024-32113, CVE-2024-36104, and CVE-2024-38856, which were addressed by the project maintainers over the past few months.

Both CVE-2024-32113 and CVE-2024-38856 have since come under active exploitation in the wild, with the former leveraged to deploy the Mirai botnet malware.

Rapid7 said all three older shortcomings stem from the "ability to desynchronize the controller and view map state," a problem that was never fully remediated in any of the patches.

A consequence of the vulnerability is that it could be abused by attackers to execute code or SQL queries and achieve remote code execution sans authentication.

The latest patch put in place "validates that a view should permit anonymous access if a user is unauthenticated, rather than performing authorization checks purely based on the target controller."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Apache OFBiz version 18.12.16 also addresses a critical server-side request forgery (SSRF) vulnerability ([CVE-2024-45507](https://nvd.nist.gov/vuln/detail/CVE-2024-45507), CVSS score: 9.8) that could lead to unauthorized access and system compromise by taking advantage of a specially crafted URL.

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

[Apache OfBiz](https://thehackernews.com/search/label/Apache%20OfBiz)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[ERP Security](https://thehackernews.com/search/label/ERP%20Security)[linux](https://thehackernews.com/search/label/linux)[Open-Source](https://thehackernews.com/search/label/Open-Source)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[windows security](https://thehackernews.com/search/label/windows%20security)

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

[![Researchers Warn of Self-Spreading WhatsApp Malware Named SORVEPOTEL](data:image/svg+xml;base64... "Researchers Warn of Self-Spreading WhatsApp Malware...