---
title: Researcher Uncovers Critical Flaws in Multiple Versions of Ivanti Endpoint Manager
url: https://thehackernews.com/2025/01/researcher-uncovers-critical-flaws-in.html
source: The Hacker News
date: 2025-01-17
fetch_date: 2025-10-06T20:14:15.389837
---

# Researcher Uncovers Critical Flaws in Multiple Versions of Ivanti Endpoint Manager

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

# [Researcher Uncovers Critical Flaws in Multiple Versions of Ivanti Endpoint Manager](https://thehackernews.com/2025/01/researcher-uncovers-critical-flaws-in.html)

**Jan 16, 2025**Ravie LakshmananVulnerability / Endpoint Security

[![Ivanti Endpoint Manager](data:image/png;base64... "Ivanti Endpoint Manager")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhz0hv9aK59OTGDE2ojyNLspgKbBNn9Oas4TKgYowgQxB4LlCKTo8wQD0Ha8P6insH1O2DG_wmvnbP5sv9tykvNg4djzyLJFgQUDRrsyRbxnoOyID9e-sMV0olAs7zqsJr0vmv_LUElNmcBEYL4hyluh7MGdFa_qINdUA3oI9Uvdr7vxbcKLZ0GLEtjxYK7/s790-rw-e365/ivanti.jpg)

Ivanti has [rolled out](https://www.ivanti.com/blog/january-security-update) security updates to address several security flaws impacting Avalanche, Application Control Engine, and Endpoint Manager (EPM), including four critical bugs that could lead to information disclosure.

All the four critical security flaws, rated 9.8 out of 10.0 on the CVSS scale, are rooted in EPM, and concern instances of absolute path traversal that allow a remote unauthenticated attacker to leak sensitive information. The flaws are listed below -

* CVE-2024-10811
* CVE-2024-13161
* CVE-2024-13160, and
* CVE-2024-13159

The shortcomings affect EPM versions 2024 November security update and prior, and 2022 SU6 November security update and prior. They have been addressed in EPM 2024 January-2025 Security Update and EPM 2022 SU6 January-2025 Security Update.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Horizon3.ai security researcher Zach Hanley has been credited with discovering and reporting all four vulnerabilities in question.

Also patched by Ivanti are multiple high-severity bugs in Avalanche versions prior to 6.4.7 and Application Control Engine before version 10.14.4.0 that could permit an attacker to bypass authentication, leak sensitive information, and get around the application blocking functionality.

The company said it has no evidence that any of the flaws are being exploited in the wild, and that it has intensified its internal scanning and testing procedures to promptly flag and address security issues.

The development comes as SAP released fixes to resolve two critical vulnerabilities in its NetWeaver ABAP Server and ABAP Platform (CVE-2025-0070 and CVE-2025-0066, CVSS scores: 9.9) that allows an authenticated attacker to exploit improper authentication checks in order to escalate privileges and access restricted information due to weak access controls.

"SAP strongly recommends that the customer visits the [Support Portal](https://support.sap.com/en/my-support/knowledge-base/security-notes-news.html) and applies patches on priority to protect their SAP landscape," the company [said](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/january-2025.html) in its January 2025 bulletin.

### Horizon3.ai Releases Technical Details

A little over a month after patches were shipped for the aforementioned flaws, San Francisco-headquartered Horizon3.ai has released additional technical specifics, describing them as "credential coercion" bugs that could allow an unauthenticated attacker to compromise the servers.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi39-MlHBEvOqrfmYzC3-WRujZ_oEFkZhUHUV7IspxcHDQ7TO4XK847kmBGegISwFKdtnblSZQR_jDjCayM8I8d2M5LZkcXdoeYEjyzw-V24p0xqvIuPfVnSvWHpUDw1T3JR-hQtKbAbbsFDwUBlGzEL0RWfnsZbhl-WMttr0yI0cRznl8IdKYC2meaTdhi/s790-rw-e365/ad.png)

The weaknesses discovered could permit an attacker to "coerce the Ivanti EPM machine account credential to be used in relay attacks, potentially allowing for server compromise," Hanley [said](https://www.horizon3.ai/attack-research/attack-blogs/ivanti-endpoint-manager-multiple-credential-coercion-vulnerabilities/), adding they reside in a DLL named "WSVulnerabilityCore.dll" that exposes various APIs related to vulnerability management for endpoints management by the EPM server.

* CVE-2024-13159 - Credential Coercion Vulnerability in GetHashForWildcardRecursive
* CVE-2024-13160 - Credential Coercion Vulnerability in GetHashForWildcard
* CVE-2024-13161 - Credential Coercion Vulnerability in GetHashForSingleFile
* CVE-2024-10811 - Credential Coercion Vulnerability in GetHashForFile

A proof-of-concept (PoC) exploit has also been publicly [made available](https://github.com/horizon3ai/Ivanti-EPM-Coercion-Vulnerabilities) by the company, making it imperative that users move quickly to apply the patches, if not already.

*(The story was updated after publication on February 20, 2025, to include information about the release of a PoC.)*

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

[Application Security](https://thehackernews.com/search/label/Application%20Security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[endpoint security](https://thehackernews.com/search/label/endpoint%20security)[Ivanti](https://thehackernews.com/search/label/Ivanti)[network security](https://thehackernews.com/search/label/network%20security)[SAP](https://thehackernews.com/search/label/SAP)[Software Patches](https://thehackernews.com/search/label/Software%20Patches)[Vulnerability](https://thehackern...