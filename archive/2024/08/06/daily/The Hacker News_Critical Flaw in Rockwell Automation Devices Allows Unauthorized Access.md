---
title: Critical Flaw in Rockwell Automation Devices Allows Unauthorized Access
url: https://thehackernews.com/2024/08/critical-flaw-in-rockwell-automation.html
source: The Hacker News
date: 2024-08-06
fetch_date: 2025-10-06T18:06:22.457482
---

# Critical Flaw in Rockwell Automation Devices Allows Unauthorized Access

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

# [Critical Flaw in Rockwell Automation Devices Allows Unauthorized Access](https://thehackernews.com/2024/08/critical-flaw-in-rockwell-automation.html)

**Aug 05, 2024**Ravie LakshmananNetwork Security / Vulnerability

[![Rockwell Automation](data:image/png;base64... "Rockwell Automation")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzBxWR-N8RKouruXd91MW-8Th8N7whDQ4qrhX4o0cRpdOYtkgST2VKhB0QclGZsKPZF68oJI-Uc9-4S-qZaCrZ80JREEjFMCbv8cPb9ZbZbxcBdscNSBgXuzAjnUxF868f3NpMUfbyym7b7tgpKeMzdqGDHXxid7T_haXAguGOwuEsR3JSdKm6oPE9BtmF/s790-rw-e365/card.png)

A high-severity security bypass vulnerability has been disclosed in Rockwell Automation ControlLogix 1756 devices that could be exploited to execute common industrial protocol ([CIP](https://thehackernews.com/2023/07/rockwell-automation-controllogix-bugs.html)) programming and configuration commands.

The flaw, which is assigned the CVE identifier **CVE-2024-6242**, carries a CVSS v3.1 score of 8.4.

"A vulnerability exists in the affected products that allows a threat actor to bypass the Trusted Slot feature in a ControlLogix controller," the U.S. Cybersecurity and Infrastructure Security Agency (CISA) [said](https://www.cisa.gov/news-events/ics-advisories/icsa-24-214-09) in an advisory.

"If exploited on any affected module in a 1756 chassis, a threat actor could potentially execute CIP commands that modify user projects and/or device configuration on a Logix controller in the chassis."

Operational technology security company Claroty, which discovered and reported the vulnerability, said it developed a technique that made it possible to bypass the trusted slot feature and send malicious commands to the programming logic controller (PLC) CPU.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The trusted slot feature "enforces security policies and allows the controller to deny communication via untrusted paths on the [local chassis](https://literature.rockwellautomation.com/idc/groups/literature/documents/um/enet-um003_-en-p.pdf)," security researcher Sharon Brizinov [said](https://claroty.com/team82/research/bypassing-rockwell-automation-logix-controllers-local-chassis-security-protection).

"The vulnerability we found, before it was fixed, allowed an attacker to jump between local backplane slots within a 1756 chassis using CIP routing, traversing the security boundary meant to protect the CPU from untrusted cards."

While a successful exploit requires network access to the device, an attacker could take advantage of the flaw to send elevated commands, including downloading arbitrary logic to the PLC CPU, even if the attacker is located behind an untrusted network card.

Following responsible disclosure, the shortcoming has been [addressed](https://www.rockwellautomation.com/en-us/trust-center/security-advisories/advisory.SD1682.html) in the following versions -

* ControlLogix 5580 (1756-L8z) - Update to versions V32.016, V33.015, V34.014, V35.011, and later.
* GuardLogix 5580 (1756-L8zS) - Update to versions V32.016, V33.015, V34.014, V35.011 and later.
* 1756-EN4TR - Update to versions V5.001 and later.
* 1756-EN2T Series D, 1756-EN2F Series C, 1756-EN2TR Series C, 1756-EN3TR Series B, and 1756-EN2TP Series A - Update to version V12.001 and later

"This vulnerability had the potential to expose critical control systems to unauthorized access over the CIP protocol that originated from untrusted chassis slots," Brizinov said.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[industrial control system](https://thehackernews.com/search/label/industrial%20control%20system)[network security](https://thehackernews.com/search/label/network%20security)[Operational Technology](https://thehackernews.com/search/label/Operational%20Technology)[scada](https://thehackernews.com/search/label/scada)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perpl...