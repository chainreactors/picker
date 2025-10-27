---
title: SAP Patches Critical NetWeaver (CVSS Up to 10.0) and High-Severity S/4HANA Flaws
url: https://thehackernews.com/2025/09/sap-patches-critical-netweaver-cvss-up.html
source: The Hacker News
date: 2025-09-11
fetch_date: 2025-10-02T20:00:59.284380
---

# SAP Patches Critical NetWeaver (CVSS Up to 10.0) and High-Severity S/4HANA Flaws

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

# [SAP Patches Critical NetWeaver (CVSS Up to 10.0) and High-Severity S/4HANA Flaws](https://thehackernews.com/2025/09/sap-patches-critical-netweaver-cvss-up.html)

**Sep 10, 2025**Ravie LakshmananSoftware Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgGa_oGwjyfDok9cHEwG_Q40d6-OSNfEaW5LstAMBMLw8X_hyBKxBa_U8x8jQUOGGtKtCi-7J4Ac3F0OZlw71REn2r-BNSA6mL3DqJTaxDYoxpn-mayJQmr18zouPsoQEvdOXF-JDQKuuj-dtFxI4cJQraAYIWbBUuyI8gtf6YXQJJ3pVhoQe1KnTAxtAgq/s790-rw-e365/sap-update.jpg)

SAP on Tuesday [released](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/september-2025.html) security updates to address multiple security flaws, including three critical vulnerabilities in SAP Netweaver that could result in code execution and the upload arbitrary files.

The vulnerabilities are listed below -

* **[CVE-2025-42944](https://www.cve.org/CVERecord?id=CVE-2025-42944)** (CVSS score: 10.0) - A deserialization vulnerability in SAP NetWeaver that could allow an unauthenticated attacker to submit a malicious payload to an open port through the [RMI-P4 module](https://help.sap.com/docs/SAP_NETWEAVER_731/c591e2679e104fcdb8dc8e77771ff524/48295738a14558d8e10000000a421937.html?locale=en-US), resulting in operating system command execution
* **[CVE-2025-42922](https://www.cve.org/CVERecord?id=CVE-2025-42922)** (CVSS score: 9.9) - An insecure file operations vulnerability in SAP NetWeaver AS Java that could allow an attacker authenticated as a non-administrative user to upload an arbitrary file
* **[CVE-2025-42958](https://www.cve.org/CVERecord?id=CVE-2025-42958)** (CVSS score: 9.1) - A missing authentication check vulnerability in the SAP NetWeaver application on IBM i-series that could allow highly privileged unauthorized users to read, modify, or delete sensitive information, as well as access administrative or privileged functionalities

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"[CVE-2025-42944] allows an unauthenticated attacker to execute arbitrary OS commands by submitting a malicious payload to an open port," Onapsis [said](https://onapsis.com/blog/sap-security-notes-september-2025-patch-day/). "A successful exploit can lead to full compromise of the application. As a temporary workaround, customers should add P4 port filtering at the ICM level to prevent unknown hosts from connecting to the P4 port."

Also addressed by SAP is a high-severity missing input validation bug in SAP S/4HANA ([CVE-2025-42916](https://www.cve.org/CVERecord?id=CVE-2025-42916), CVSS score: 8.1) that could permit an attacker with high privilege access to ABAP reports to delete the content of arbitrary database tables, should the tables not be protected by an authorization group.

The patches arrive days after SecurityBridge and Pathlock [disclosed](https://thehackernews.com/2025/09/sap-s4hana-critical-vulnerability-cve.html) that a critical security defect in SAP S/4HANA that was fixed by the company last month (CVE-2025-42957, CVSS score: 9.9) has come under active exploitation in the wild.

While there is no evidence that the newly disclosed issues have been weaponized by bad actors, it's essential that users move to apply the necessary updates as soon as possible for optimal protection.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[NetWeaver](https://thehackernews.com/search/label/NetWeaver)[S/4HANA](https://thehackernews.com/search/label/S/4HANA)[SAP](https://thehackernews.com/search/label/SAP)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked Plug...