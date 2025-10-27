---
title: Four Critical Vulnerabilities Expose HPE Aruba Devices to RCE Attacks
url: https://thehackernews.com/2024/05/four-critical-vulnerabilities-expose.html
source: The Hacker News
date: 2024-05-04
fetch_date: 2025-10-06T17:17:41.167727
---

# Four Critical Vulnerabilities Expose HPE Aruba Devices to RCE Attacks

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

# [Four Critical Vulnerabilities Expose HPE Aruba Devices to RCE Attacks](https://thehackernews.com/2024/05/four-critical-vulnerabilities-expose.html)

**May 03, 2024**Ravie LakshmananVulnerability / Software Security

[![HPE Aruba Devices](data:image/png;base64... "HPE Aruba Devices")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJ_NiSACku3pJ34UhfJlL5i5pAXWTJEjWyhyphenhyphencR7-iJS3qoNhs71PrBYlOjixCXAZBW6pA_P-WrCwfgLqmmZdbbUYLaocUZDzPsA6s86pCmeoGlcgArUN1Q4NJmJbEVt2uS9m5hf2lZ1sfAIVBc_T3S7txOYzElo7uqAwlZAJ25R28xEM00pV6LzEaok1AW/s790-rw-e365/hpe.png)

HPE Aruba Networking (formerly Aruba Networks) has released security updates to address critical flaws impacting ArubaOS that could result in remote code execution (RCE) on affected systems.

Of the [10 security defects](https://www.arubanetworks.com/assets/alert/ARUBA-PSA-2024-004.txt), four are rated critical in severity -

* **CVE-2024-26304** (CVSS score: 9.8) - Unauthenticated Buffer Overflow Vulnerability in the L2/L3 Management Service Accessed via the PAPI Protocol

* **CVE-2024-26305** (CVSS score: 9.8) - Unauthenticated Buffer Overflow Vulnerability in the Utility Daemon Accessed via the PAPI Protocol

* **CVE-2024-33511** (CVSS score: 9.8) - Unauthenticated Buffer Overflow Vulnerability in the Automatic Reporting Service Accessed via the PAPI Protocol

* **CVE-2024-33512** (CVSS score: 9.8) - Unauthenticated Buffer Overflow Vulnerability in the Local User Authentication Database Accessed via the PAPI Protocol

A threat actor could exploit the aforementioned buffer overflow bugs by sending specially crafted packets destined to the Process Application Programming Interface (PAPI) UDP port (8211), thereby gaining the ability to execute arbitrary code as a privileged user on the underlying operating system.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The vulnerabilities, which impact Mobility Conductor (formerly Mobility Master), Mobility Controllers, and WLAN Gateways and SD-WAN Gateways managed by Aruba Central, are present in the following software versions -

* ArubaOS 10.5.1.0 and below
* ArubaOS 10.4.1.0 and below
* ArubaOS 8.11.2.1 and below, and
* ArubaOS 8.10.0.10 and below

They also impact the ArubaOS and SD-WAN software versions that have reached end of maintenance status -

* ArubaOS 10.3.x.x
* ArubaOS 8.9.x.x
* ArubaOS 8.8.x.x
* ArubaOS 8.7.x.x
* ArubaOS 8.6.x.x
* ArubaOS 6.5.4.x
* SD-WAN 8.7.0.0-2.3.0.x, and
* SD-WAN 8.6.0.4-2.2.x.x

A security researcher named Chancen has been credited with discovering and reporting seven of the 10 issues, including the four critical buffer overflow vulnerabilities.

Users are advised to apply the latest fixes to mitigate potential threats. As temporary workarounds for ArubaOS 8.x, the company is recommending that users enable the [Enhanced PAPI Security feature](https://www.arubanetworks.com/techdocs/ArubaOS_87_Web_Help/Content/arubaos-solutions/papi-enha-secu/enha-secu.htm) using a non-default key.

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

[ArubaOS](https://thehackernews.com/search/label/ArubaOS)[programming](https://thehackernews.com/search/label/programming)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[software security](https://thehackernews.com/search/label/software%20security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

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

[![Researchers Warn of Self-Spreading What...