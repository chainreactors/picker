---
title: Synology Urges Patch for Critical Zero-Click RCE Flaw Affecting Millions of NAS Devices
url: https://thehackernews.com/2024/11/synology-urges-patch-for-critical-zero.html
source: The Hacker News
date: 2024-11-06
fetch_date: 2025-10-06T19:26:23.301741
---

# Synology Urges Patch for Critical Zero-Click RCE Flaw Affecting Millions of NAS Devices

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

# [Synology Urges Patch for Critical Zero-Click RCE Flaw Affecting Millions of NAS Devices](https://thehackernews.com/2024/11/synology-urges-patch-for-critical-zero.html)

**Nov 05, 2024**Ravie LakshmananVulnerability / Data Security

[![NAS Devices](data:image/png;base64... "NAS Devices")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfAfqQvxv4zNj1PXr5uS1l7qttu5bUegYweslW5DT1OGI4IwuoM7P160WL8TuSeC1k_555eTSSM9SZVMlymX4ovmTFuD-mLkGxiGJLEzDFN8_OQynIZy9qx__8gW8i3nFqh1DK4FjYExzJnxJE52P51_GcDNflDWPOy9ipMitX7nusqOeKIr0osK8x1kge/s790-rw-e365/nas-hacked.png)

Taiwanese network-attached storage (NAS) appliance maker Synology has addressed a critical security flaw impacting DiskStation and BeePhotos that could lead to remote code execution.

Tracked as CVE-2024-10443 and dubbed **RISK:STATION** by Midnight Blue, the zero-day flaw was demonstrated at the Pwn2Own Ireland 2024 hacking contest by security researcher Rick de Jager.

RISK:STATION is an "unauthenticated zero-click vulnerability allowing attackers to obtain root-level code execution on the popular Synology DiskStation and BeeStation NAS devices, affecting millions of devices," the Dutch company [said](https://www.midnightblue.nl/research/riskstation).

The zero-click nature of the vulnerability means it does not require any user interaction to trigger the exploitation, thereby allowing attackers to gain access to the devices to steal sensitive data and plant additional malware.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The flaw impacts the following versions -

* [BeePhotos for BeeStation OS 1.0](https://www.synology.com/en-global/security/advisory/Synology_SA_24_18) (Upgrade to 1.0.2-10026 or above)
* [BeePhotos for BeeStation OS 1.1](https://www.synology.com/en-global/security/advisory/Synology_SA_24_18) (Upgrade to 1.1.0-10053 or above)
* [Synology Photos 1.6 for DSM 7.2](https://www.synology.com/en-global/security/advisory/Synology_SA_24_19) (Upgrade to 1.6.2-0720 or above)
* [Synology Photos 1.7 for DSM 7.2](https://www.synology.com/en-global/security/advisory/Synology_SA_24_19) (Upgrade to 1.7.0-0795 or above)

Additional technical details about the vulnerability have been currently withheld so as to give customers sufficient time to apply the patches. Midnight Blue said there are between one and two million Synology devices that are currently simultaneously affected and exposed to the internet.

### QNAP Patches 3 Critical Bugs

The disclosure comes as QNAP resolved three critical flaws affecting QuRouter, SMB Service, and HBS 3 Hybrid Backup Sync, all of which were exploited during Pwn2Own -

* [CVE-2024-50389](https://www.qnap.com/en-in/security-advisory/qsa-24-45) - Fixed in QuRouter 2.4.5.032 and later
* [CVE-2024-50387](https://www.qnap.com/en-in/security-advisory/qsa-24-42) - Fixed in SMB Service 4.15.002 and SMB Service h4.15.002, and later
* [CVE-2024-50388](https://www.qnap.com/en-in/security-advisory/qsa-24-41) - Fixed in HBS 3 Hybrid Backup Sync 25.1.1.673 and later

While there is no evidence that any of the aforementioned vulnerabilities have been exploited in the wild, users are advised to apply the patches as soon as possible given that NAS devices have been high-value targets for [ransomware attacks](https://thehackernews.com/2022/09/qnap-warns-of-new-deadbolt-ransomware.html) in the past.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data security](https://thehackernews.com/search/label/data%20security)[NAS Device](https://thehackernews.com/search/label/NAS%20Device)[network security](https://thehackernews.com/search/label/network%20security)[ransomware](https://thehackernews.com/search/label/ransomware)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[zero-day](https://thehackernews.com/search/label/zero-day)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexi...