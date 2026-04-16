---
title: April Patch Tuesday Fixes Critical Flaws Across SAP, Adobe, Microsoft, Fortinet, and More
url: https://thehackernews.com/2026/04/april-patch-tuesday-fixes-critical.html
source: The Hacker News
date: 2026-04-15
fetch_date: 2026-04-16T04:54:24.503898
---

# April Patch Tuesday Fixes Critical Flaws Across SAP, Adobe, Microsoft, Fortinet, and More

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

# [April Patch Tuesday Fixes Critical Flaws Across SAP, Adobe, Microsoft, Fortinet, and More](https://thehackernews.com/2026/04/april-patch-tuesday-fixes-critical.html)

**Ravie Lakshmanan**Apr 15, 2026Vulnerability / Data Breach

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-FBwJYevQ8Ner9ypyp5-H1XIPfa5guhQXC-W4llTZuBI072vjCoxKh9PUexQBZGJIeuZXoBAKboz9xz5Gzd0p1SiT5UME0wd0lTTOS6EIh3nJ6vsAeMzGmT0P38ry2ySiLc-je0e0YAZAPDYmhw3jSfqbExcsQW5nL8syaClAcSfZziU-KPneawQFfo6p/s1700-e365/patches.jpg)

A number of critical vulnerabilities impacting products from Adobe, Fortinet, Microsoft, and SAP have taken center stage in April's Patch Tuesday releases.

Topping the list is an SQL injection vulnerability impacting SAP Business Planning and Consolidation and SAP Business Warehouse ([CVE-2026-27681](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/april-2026.html), CVSS score: 9.9) that could result in the execution of arbitrary database commands.

"The vulnerable ABAP program allows a low-privileged user to upload a file with arbitrary SQL statements that will then be executed," Onapsis [said](https://onapsis.com/blog/sap-security-notes-april-2026-patch-day/) in an advisory.

In a potential attack scenario, a bad actor could abuse the affected upload-related functionality to run malicious SQL against BW/BPC data stores, extract sensitive data, and delete or corrupt database content.

"Manipulated planning figures, broken reports, or deleted consolidation data can undermine close processes, executive reporting, and operational planning," Pathlock [said](https://pathlock.com/blog/security-alerts/sap-patch-day-april-2026-critical-sql-injection-authorization-flaws/). "In the wrong hands, this issue also creates a credible path to both stealthy data theft and overt business disruption."

Another security vulnerability that deserves a mention is a critical-severity remote code execution in Adobe Acrobat Reader ([CVE-2026-34621](https://thehackernews.com/2026/04/adobe-patches-actively-exploited.html), CVSS score: 8.6) that has come under active exploitation in the wild.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

That said, there are many unknowns at this stage. It is not clear how many people have been affected by the hacking campaign. Nor is there any information about who is behind the activity, who is being targeted, and what their motives could be.

Also [patched](https://helpx.adobe.com/security/security-bulletin.html) by Adobe are [five critical flaws in ColdFusion versions 2025 and 2023](https://helpx.adobe.com/security/products/coldfusion/apsb26-38.html) that, if successfully exploited, could lead to arbitrary code execution, application denial-of-service, arbitrary file system read, and security feature bypass.

The vulnerabilities are listed below -

* **CVE-2026-34619** (CVSS score: 7.7) - A path traversal vulnerability leading to security feature bypass
* **CVE-2026-27304** (CVSS score: 9.3) - An improper input validation vulnerability leading to arbitrary code execution
* **CVE-2026-27305** (CVSS score: 8.6) - A path traversal vulnerability leading to arbitrary file system read
* **CVE-2026-27282** (CVSS score: 7.5) - An improper input validation vulnerability leading to security feature bypass
* **CVE-2026-27306** (CVSS score: 8.4) - An improper input validation vulnerability leading to arbitrary code execution

Fixes have also been released for two critical FortiSandbox vulnerabilities that could result in authentication bypass and code execution -

* **[CVE-2026-39813](https://fortiguard.fortinet.com/psirt/FG-IR-26-112)** (CVSS score: 9.1) - A path traversal vulnerability in FortiSandbox JRPC API that could allow an unauthenticated attacker to bypass authentication via specially crafted HTTP requests. (Fixed in versions 4.4.9 and 5.0.6)
* **[CVE-2026-39808](https://fortiguard.fortinet.com/psirt/FG-IR-26-100)** (CVSS score: 9.1) - An operating system command injection vulnerability in FortiSandbox that could allow an unauthenticated attacker to execute unauthorized code or commands via crafted HTTP requests. (Fixed in version 4.4.9)

The development comes as Microsoft [addressed](https://thehackernews.com/2026/04/microsoft-issues-patches-for-sharepoint.html) a staggering 169 security defects, including a spoofing vulnerability impacting Microsoft SharePoint Server (CVE-2026-32201, CVSS score: 6.5) that could allow an attacker to view sensitive information. The company said it's being actively exploited, although there are no insights into the in-the-wild exploitation associated with the bug.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

"SharePoint services, especially those used as internal document stores, can be a treasure trove for threat actors looking to steal data, especially data that may be leveraged to force ransom payments using double extortion techniques by threatening to release the stolen data if payment is not made," Kev Breen, senior director of threat research at Immersive, said.

"A secondary concern is that threat actors with access to SharePoint services could deploy weaponised documents or replace legitimate documents with infected versions that would allow them to spread to other hosts or victims moving laterally across the organization."

## Software Patches from Other Vendors

In addition to Microsoft, security updates have also been released by other vendors over the past several weeks to rectify several vulnerabilities, including —

* [ABB](https://www.abb.com/global/en/company/about/cybersecurity/alerts-and-notifications)
* [Amazon Web Services](https://aws.amazon.com/security/security-bulletins/)
* [AMD](https://www.amd.com/en/resources/product-security.html#security)
* [Apple](https://support.apple.com/en-us/HT201222)
* [ASUS](https://www.asus.com/security-advisory/)
* [AVEVA](https://www.aveva.com/en/support-and-success/cyber-security-updates/)
* [Broadcom](https://support.broadcom.com/web/ecx/security-advisory) (including VMware)
* [Canon](https://psirt.canon/advisory-information/#id_2229656)
* [Cisco](https://tools.cisco.com/security/center/publicationListing.x)
* [Citrix](https://support.citrix.com/support-home/to...