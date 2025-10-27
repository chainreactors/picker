---
title: HPE Issues Security Patch for StoreOnce Bug Allowing Remote Authentication Bypass
url: https://thehackernews.com/2025/06/hpe-issues-security-patch-for-storeonce.html
source: The Hacker News
date: 2025-06-05
fetch_date: 2025-10-06T22:56:09.835414
---

# HPE Issues Security Patch for StoreOnce Bug Allowing Remote Authentication Bypass

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

# [HPE Issues Security Patch for StoreOnce Bug Allowing Remote Authentication Bypass](https://thehackernews.com/2025/06/hpe-issues-security-patch-for-storeonce.html)

**Jun 04, 2025**The Hacker NewsVulnerability / DevOps

[![HPE Issues Security Patch](data:image/png;base64... "HPE Issues Security Patch")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitLc-FJawaJ7HfHyM-rMGEUKadlIfPWxHDmdrQoigXQ26Tl9S8vq9tqgL3qRyIYMs95mXObPeVRIrwEz3xo8sMIljVsUroE15qzKyvhyAzVqoc5oOHm4nfhxUot-ikxsWid7zTRTaMWQZs9Vjdl0lKSkegaGJL2HIO5vIiHe34kbC7DMHV4OckaFcuw_In/s790-rw-e365/hpe.jpg)

Hewlett Packard Enterprise (HPE) has released security updates to address as many as eight vulnerabilities in its StoreOnce data backup and deduplication solution that could result in an authentication bypass and remote code execution.

"These vulnerabilities could be remotely exploited to allow remote code execution, disclosure of information, server-side request forgery, authentication bypass, arbitrary file deletion, and directory traversal information disclosure vulnerabilities," HPE [said](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbst04847en_us&docLocale=en_US) in an advisory.

This includes a fix for a critical security flaw tracked as CVE-2025-37093, which is rated 9.8 on the CVSS scoring system. It has been described as an authentication bypass bug affecting all versions of the software prior to 4.3.11. The vulnerability, along with the rest, was reported to the vendor on October 31, 2024.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

According to the Zero Day Initiative (ZDI), which credited an anonymous researcher for discovering and reporting the shortcoming, said the problem is rooted in the implementation of the machineAccountCheck method.

"The issue results from improper implementation of an authentication algorithm," ZDI [said](https://www.zerodayinitiative.com/advisories/ZDI-25-316/). "An attacker can leverage this vulnerability to bypass authentication on the system."

Successful exploitation of CVE-2025-37093 could permit a remote attacker to bypass authentication on affected installations. What makes the vulnerability more severe is that it could be chained with the remaining flaws to achieve code execution, information disclosure, and [arbitrary file deletion](https://www.zerodayinitiative.com/advisories/ZDI-25-317/) in the context of root -

* CVE-2025-37089 - Remote Code Execution
* CVE-2025-37090 - Server-Side Request Forgery
* CVE-2025-37091 - Remote Code Execution
* CVE-2025-37092 - Remote Code Execution
* CVE-2025-37093 - Authentication Bypass
* CVE-2025-37094 - Directory Traversal Arbitrary File Deletion
* CVE-2025-37095 - Directory Traversal Information Disclosure
* CVE-2025-37096 - Remote Code Execution

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes as HPE also shipped patches to address multiple critical-severity flaws in [HPE Telco Service Orchestrator](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw04872en_us&docLocale=en_US) ([CVE-2025-31651](https://nvd.nist.gov/vuln/detail/cve-2025-31651), CVSS score: 9.8) and [OneView](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbgn04853en_us&docLocale=en_US) ([CVE-2024-38475](https://nvd.nist.gov/vuln/detail/cve-2024-38475), [CVE-2024-38476](https://nvd.nist.gov/vuln/detail/cve-2024-38476), CVSS scores: 9.8) to address previously disclosed weaknesses in Apache Tomcat and Apache HTTP Server.

While there are no reports of active exploitation, it's essential that users apply the latest updates for optimal protection.

Found this article interesting? This article is a contributed piece from one of our valued partners. Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

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

[Apache Tomcat](https://thehackernews.com/search/label/Apache%20Tomcat)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[DevOps](https://thehackernews.com/search/label/DevOps)[Directory Traversal](https://thehackernews.com/search/label/Directory%20Traversal)[Hewlett Packard Enterprise](https://thehackernews.com/search/label/Hewlett%20Packard%20Enterprise)[information disclosure](https://thehackernews.com/search/label/information%20disclosure)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[zero day](https://thehackernews.com/search/label/zero%20day)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious ...