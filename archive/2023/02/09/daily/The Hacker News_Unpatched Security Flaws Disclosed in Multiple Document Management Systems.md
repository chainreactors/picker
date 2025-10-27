---
title: Unpatched Security Flaws Disclosed in Multiple Document Management Systems
url: https://thehackernews.com/2023/02/unpatched-security-flaws-disclosed-in.html
source: The Hacker News
date: 2023-02-09
fetch_date: 2025-10-04T06:10:11.720591
---

# Unpatched Security Flaws Disclosed in Multiple Document Management Systems

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

# [Unpatched Security Flaws Disclosed in Multiple Document Management Systems](https://thehackernews.com/2023/02/unpatched-security-flaws-disclosed-in.html)

**Feb 08, 2023**Ravie LakshmananVulnerability Management

[![Document Management Systems](data:image/png;base64... "Document Management Systems")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9T3JRZ5PUDi1Oj0T1gsvJYsb_ApAnqIYkWBDdPK1AJdWQ5hUWZMJDTOgtajWRBs178tx8zViXxoxxhsFGJDg4H3kLRHNvcfBr82hUbQQ2H7W5T_6yx2DZjD_BhV5cvjV1Ws0tHGvTFvEPz_9kQwo_S7c6mG4_3rrzD8XHedJohA0WvqyhpYNjtY4G/s790-rw-e365/docs.png)

Multiple unpatched security flaws have been disclosed in open source and freemium Document Management System (DMS) offerings from four vendors LogicalDOC, Mayan, ONLYOFFICE, and OpenKM.

Cybersecurity firm Rapid7 said the eight vulnerabilities offer a mechanism through which "an attacker can convince a human operator to save a malicious document on the platform and, once the document is indexed and triggered by the user, giving the attacker multiple paths to control the organization."

The list of eight cross-site scripting ([XSS](https://owasp.org/www-community/attacks/xss/)) flaws, discovered by Rapid7 researcher Matthew Kienow, is as follows -

* **CVE-2022-47412** - ONLYOFFICE Workspace Search Stored XSS
* **CVE-2022-47413 and CVE-2022-47414** - OpenKM Document and Application XSS
* **CVE-2022-47415, CVE-2022-47416, CVE-2022-47417, and CVE-2022-47418** - LogicalDOC Multiple Stored XSS
* **CVE-2022-47419** - Mayan EDMS Tag Stored XSS

Stored XSS, also known as persistent XSS, occurs when a malicious script is injected directly into a vulnerable web application (e.g., via a comment field), causing the rogue code to be activated upon each visit to the application.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A threat actor can exploit the aforementioned flaws by providing a decoy document, granting the interloper the ability to further their control over the compromised network,

"A typical attack pattern would be to steal the session cookie that a locally-logged in administrator is authenticated with, and reuse that session cookie to impersonate that user to create a new privileged account," Tod Beardsley, director of research at Rapid7, [said](https://www.rapid7.com/blog/post/2023/02/07/multiple-dms-xss-cve-2022-47412-through-cve-20222-47419/).

In an alternative scenario, the attacker could abuse the identity of the victim to inject arbitrary commands and gain stealthy access to the stored documents.

The cybersecurity firm noted that the flaws were reported to the respective vendors on December 1, 2022, and continue to remain unfixed despite coordinating the disclosures with CERT Coordination Center (CERT/CC).

Users of the affected DMS are advised to proceed with caution when importing documents from unknown or untrusted sources as well as limit the creation of anonymous, untrusted users and restrict certain features such as chats and tagging to known users.

**Update:** ONLYOFFICE has confirmed to THN that its document management software has been updated to [version 7.3.3](https://github.com/ONLYOFFICE/DocumentServer/blob/master/CHANGELOG.md#733) on March 15, 2023, addressing CVE-2022-47412 described in this article.

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

[Cross site scripting](https://thehackernews.com/search/label/Cross%20site%20scripting)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html)

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](data:image/svg+xml;base6...