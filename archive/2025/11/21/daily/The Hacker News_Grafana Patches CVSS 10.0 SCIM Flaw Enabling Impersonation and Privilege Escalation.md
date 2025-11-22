---
title: Grafana Patches CVSS 10.0 SCIM Flaw Enabling Impersonation and Privilege Escalation
url: https://thehackernews.com/2025/11/grafana-patches-cvss-100-scim-flaw.html
source: The Hacker News
date: 2025-11-21
fetch_date: 2025-11-22T03:08:59.435914
---

# Grafana Patches CVSS 10.0 SCIM Flaw Enabling Impersonation and Privilege Escalation

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Grafana Patches CVSS 10.0 SCIM Flaw Enabling Impersonation and Privilege Escalation](https://thehackernews.com/2025/11/grafana-patches-cvss-100-scim-flaw.html)

**Nov 21, 2025**Ravie LakshmananVulnerability / Threat Mitigation

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSd96MdjXbbJYSzwIs4CNhCrhOSN5Avm0c3kgMEQVlWBzUPXLbXKs_Kyjk_LhSeKQLjJRbzxyl7SCv62tvd2GEHySWOO__C_f5h2u-5md5Nycx87_WmNUx0CSZ7FCNVEI8LEavtyCoV7cHBFDbdNDaGMrX65oRX0pR17RJcKGIA8PofZ5YhsMrhQV1xpAt/s790-rw-e365/grafana.jpg)

Grafana has released security updates to address a maximum severity security flaw that could allow privilege escalation or user impersonation under certain configurations.

The vulnerability, tracked as **CVE-2025-41115**, carries a CVSS score of 10.0. It resides in the System for Cross-domain Identity Management ([SCIM](https://grafana.com/docs/grafana/latest/setup-grafana/configure-access/configure-scim-provisioning/)) component that allows automated user provisioning and management. First [introduced](https://grafana.com/blog/2025/05/14/introducing-scim-provisioning-in-grafana-enterprise-grade-user-management-made-simple/) in April 2025, it's currently in public preview.

"In Grafana versions 12.x where SCIM provisioning is enabled and configured, a vulnerability in user identity handling allows a malicious or compromised SCIM client to provision a user with a numeric externalId, which in turn could allow for overriding internal user IDs and lead to impersonation or privilege escalation," Grafana's Vardan Torosyan [said](https://grafana.com/blog/2025/11/19/grafana-enterprise-security-update-critical-severity-security-fix-for-cve-2025-41115/).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

That said, successful exploitation hinges on both conditions being met -

* enableSCIM feature flag is set to true
* user\_sync\_enabled config option in the [auth.scim] block is set to true

The shortcoming affects Grafana Enterprise versions from 12.0.0 to 12.2.1. It has been addressed in the following versions of the software -

* Grafana Enterprise 12.0.6+security-01
* Grafana Enterprise 12.1.3+security-01
* Grafana Enterprise 12.2.1+security-01
* Grafana Enterprise 12.3.0

"Grafana maps the SCIM externalId directly to the internal user.uid; therefore, numeric values (e.g. '1') may be interpreted as internal numeric user IDs," Torosyan said. "In specific cases this could allow the newly provisioned user to be treated as an existing internal account, such as the Admin, leading to potential impersonation or privilege escalation."

The analytics and observability platform said the vulnerability was discovered internally on November 4, 2025, during an audit and testing. Given the severity of the issue, users are advised to apply the patches as soon as possible to mitigate potential risks.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Identity Management](https://thehackernews.com/search/label/Identity%20Management)[Patch Management](https://thehackernews.com/search/label/Patch%20Management)[Threat Mitigation](https://thehackernews.com/search/label/Threat%20Mitigation)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/wiz-aws-ai-security)

Trending News

[![⚡ Weekly Recap: Hyper-V Malware, Malicious AI Bots, RDP Exploits, WhatsApp Lockdown and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Hyper-V Malware, Malicious AI Bots, RDP Exploits, WhatsApp Lockdown and More")

⚡ Weekly Recap: Hyper-V Malware, Malicious AI Bots, RDP Exploits, WhatsApp Lockdown and More](https://thehackernews.com/2025/11/weekly-recap-hyper-v-malware-malicious.html)

[![Microsoft Uncovers 'Whisper Leak' Attack That Identifies AI Chat Topics in Encrypted Traffic](data:image/svg+xml;base64... "Microsoft Uncovers 'Whisper Leak' Attack That Identifies AI Chat Topics in Encrypted Traffic")

Microsoft Uncovers 'Whisper Leak' Attack That Identifies AI Chat Topics in Encrypted Traffic](https://thehackernews.com/2025/11/microsoft-uncovers-whisper-leak-attack.html)

[![WhatsApp Malware 'Maverick' Hijacks Browser Sessions to Target Brazil's Biggest Banks](data:image/svg+xml;base64... "WhatsApp Malware 'Maverick' Hijacks Browser Sessions to Target Brazil's Biggest Banks")

WhatsApp Malware 'Maverick' Hijacks Browser Sessions to Target Brazil's Biggest Banks](https://thehackernews.com/2025/11/whatsapp-malware-maverick-hijacks.html)

[![Microsoft Fixes 63 Security Flaws, Including a Windows Kernel Zero-Day Under Active Attack](data:image/svg+xml;base64... "Microsoft Fixes 63 Security Flaws, Including a Windows Kernel Zero-Day Under Active Attack")

Microsoft Fixes 63 Security Flaws, Including a Windows Kernel Zero-Day Under Active Attack](https://thehackernews.com/2025/11/microsoft-fixes-63-security-flaws.html)

[![Amazon Uncovers Attacks Exploited Cisco ISE and Citrix NetScaler as Zero-Day Flaws](data:image/svg+xml;base64... "Amazon Uncovers Attacks Exploited Cisco ISE and Citrix NetScaler as Zero-Day Flaws")

Amazon Uncovers Attacks Exploited Cisco ISE and Citrix N...