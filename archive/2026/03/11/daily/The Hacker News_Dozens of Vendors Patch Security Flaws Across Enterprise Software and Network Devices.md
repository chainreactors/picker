---
title: Dozens of Vendors Patch Security Flaws Across Enterprise Software and Network Devices
url: https://thehackernews.com/2026/03/dozens-of-vendors-patch-security-flaws.html
source: The Hacker News
date: 2026-03-11
fetch_date: 2026-03-12T04:09:07.137044
---

# Dozens of Vendors Patch Security Flaws Across Enterprise Software and Network Devices

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [Dozens of Vendors Patch Security Flaws Across Enterprise Software and Network Devices](https://thehackernews.com/2026/03/dozens-of-vendors-patch-security-flaws.html)

**Ravie Lakshmanan**Mar 11, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcrrEElPNhJ9Cn51FnZPkh9XKFRVQzKwXGWqMzaKySW388TL56lNUbySAgOs9nxMbwCHVmFwxE3UvCVt_H9MtWZfS2euZz9zF-Wrh0mnVf-3kefawk-MvoqjSZd3MOcKzHVgjYWnkWy9iE2Ns-6kauXtWE4K9LJHQdBStJVJHjGCRS4om2dZIHDv7rw3zh/s1700-e365/software-update.jpg)

SAP has [released](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/march-2026.html) security updates to address two critical security flaws that could be exploited to achieve arbitrary code execution on affected systems.

The vulnerabilities in question listed below -

* **CVE-2019-17571** (CVSS score: 9.8) - A code injection vulnerability in SAP Quotation Management Insurance application (FS-QUO)
* **CVE-2026-27685** (CVSS score: 9.1) - An insecure deserialization vulnerability in SAP NetWeaver Enterprise Portal Administration

"The application uses an outdated artifact of Apache Log4j 1.2.17 that is vulnerable to CVE-2019-17571," SAP security company Onapsis [said](https://onapsis.com/blog/sap-security-patch-day-march-2026/). "It allows an unprivileged attacker to execute arbitrary code remotely on the server, causing high impact on confidentiality, integrity, and availability of the application."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

CVE-2026-27685, on the other hand, stems from missing or insufficient validation during the deserialization of uploaded content, which could allow an attacker to upload untrusted or malicious content.

"Only the fact that an attacker requires high privileges for a successful exploit prevents the vulnerability from being tagged with a CVSS score of 10," Onapsis added.

The disclosure comes as Microsoft shipped patches for [84 vulnerabilities](https://thehackernews.com/2026/03/microsoft-patches-84-flaws-in-march.html) across products, including dozens of privilege escalation and remote code execution flaws.

On Tuesday, Adobe also announced patches for [80 vulnerabilities](https://helpx.adobe.com/security.html), four of which are critical flaws impacting Adobe Commerce and Magento Open Source that could result in privilege escalation and security feature bypass. Separately, it fixed five critical vulnerabilities in Adobe Illustrator that could pave the way for arbitrary code execution.

Elsewhere, Hewlett Packard Enterprise put out fixes for five shortcomings in Aruba Networking AOS-CX. The most severe of the flaws is CVE-2026-23813 (CVSS score: 9.8), an authentication bypass affecting the management interface.

"A vulnerability has been identified in the web-based management interface of AOS-CX switches that could potentially allow an unauthenticated remote actor to circumvent existing authentication controls," HPE [said](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05027en_us&docLocale=en_US). "In some cases, this could enable resetting the admin password."

"Exploitation of this Aruba vulnerability potentially gives attackers full control of AOS-CX network devices and the ability to compromise an entire system undetected," Ross Filipek, CISO at Corsica Technologies, said in a statement.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/cyber-comm-guide-d)

"A successful compromise could lead to the disruption of network communications or the erosion of the integrity of key business services. This flaw is a reminder that vulnerabilities in network devices are becoming more common in today's hyper-connected world. When attackers gain privileged access to these devices, it puts organizations at significant risk."

### Software Patches from Other Vendors

Security updates have also been released by other vendors over the past few weeks to rectify several vulnerabilities, including —

* [ABB](https://www.abb.com/global/en/company/about/cybersecurity/alerts-and-notifications)
* [Amazon Web Services](https://aws.amazon.com/security/security-bulletins/)
* [AMD](https://www.amd.com/en/resources/product-security.html#security)
* [Arm](https://developer.arm.com/Arm%20Security%20Center#sortCriteria=%40published%20descending&numberOfResults=48)
* [Atlassian](https://www.atlassian.com/trust/security/advisories)
* [Bosch](https://psirt.bosch.com/security-advisories/)
* [Broadcom](https://support.broadcom.com/web/ecx/search?searchString=cve&activeType=all&from=0&sortby=post_time&orderBy=desc&pageNo=1&aggregations=%5B%7B%22type%22%3A%22_type%22%2C%22filter%22%3A%5B%22notification_docs%22%5D%7D%5D&uid=d042dbba-f8c4-11ea-beba-0242ac12000b&resultsPerPage=50&exactPhrase=&withOneOrMore=&withoutTheWords=&pageSize=50&language=en&state=34&suCaseCreate=false) (including VMware)
* [Canon](https://psirt.canon/advisory-information/#id_2229656)
* [Cisco](https://tools.cisco.com/security/center/publicationListing.x)
* [Commvault](https://documentation.commvault.com/securityadvisories/)
* [Dassault Systèmes](https://www.3ds.com/trust-center/security/security-advisories)
* [Dell](https://www.dell.com/support/security/)
* [Devolutions](https://devolutions.net/security/advisories/)
* [Drupal](https://www.drupal.org/security)
* [Elastic](https://discuss.elastic.co/c/announcements/security-announcements/31)
* [F5](https://my.f5.com/manage/s/new-updated-articles#f-f5_document_type=Security%20Advisory&aq=%40f5_original_published_date%20%3E%3D%20now-7d)
* [Fortinet](https://www.fortiguard.com/psirt)
* [Fortra](https://www.fortra.com/security/advisories/product-security)
* [Foxit Software](https://www.foxit.com/support/security-bulletins.html)
* [GitLab](https://about.gitlab.com/releases/2026/02/25/patch-release-gitlab-18-9-1-released/)
* Google [Android](https://source.android.com/docs/security/bulletin/2026/2026-03-01) and [Pi...