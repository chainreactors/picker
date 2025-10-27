---
title: Critical SQL Injection Flaws Expose Gentoo Soko to Remote Code Execution
url: https://thehackernews.com/2023/06/critical-sql-injection-flaws-expose.html
source: The Hacker News
date: 2023-06-29
fetch_date: 2025-10-04T11:49:14.243008
---

# Critical SQL Injection Flaws Expose Gentoo Soko to Remote Code Execution

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

# [Critical SQL Injection Flaws Expose Gentoo Soko to Remote Code Execution](https://thehackernews.com/2023/06/critical-sql-injection-flaws-expose.html)

**Jun 28, 2023**Ravie LakshmananEndpoint Security / RCE

[![SQL Injection](data:image/png;base64... "SQL Injection")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_5FwxT59xLEmYq0iYorfCgET04nACWzI3qXth_6WzHuR8pILvAri8DccvJ3H4t2QMHRQzphjWNrZK0rQcJZi52xZc86hU_jrc0Ob3K5dF76oHeYtx1u-lt_HH4_ZnqBeKlNhdpHMc11-DldU9iIE3lu4HeMiXof-a6cen8yMzVjb5cPQDg_p2GMUS_O8/s790-rw-e365/sql.jpg)

Multiple SQL injection vulnerabilities have been disclosed in Gentoo Soko that could lead to remote code execution (RCE) on vulnerable systems.

"These SQL injections happened despite the use of an Object-Relational Mapping (ORM) library and prepared statements," SonarSource researcher Thomas Chauchefoin [said](https://www.sonarsource.com/blog/why-orms-and-prepared-statements-cant-always-win/), adding they could result in RCE on Soko because of a "misconfiguration of the database."

The [two](https://github.com/gentoo/soko/security/advisories/GHSA-gc2x-86p3-mxg2) [issues](https://github.com/gentoo/soko/security/advisories/GHSA-45jr-w89p-c843), which were discovered in the search feature of Soko, have been collectively tracked as CVE-2023-28424 (CVSS score: 9.1). They were addressed within 24 hours of responsible disclosure on March 17, 2023.

Soko is a Go software module that powers [packages.gentoo.org](https://packages.gentoo.org/), offering users an easy way to search through different Portage packages that are available for Gentoo Linux distribution.

But the shortcomings identified in the service meant that it could have been possible for a malicious actor to [inject specially crafted code](https://capec.mitre.org/data/definitions/66.html), resulting in the exposure of sensitive information.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The SQL injections were exploitable and had the ability to disclose the PostgreSQL server's version and execute arbitrary commands on the system," SonarSource said.

The development comes months after SonarSource [uncovered](https://www.sonarsource.com/blog/odoo-get-your-content-type-right-or-else/) a cross-site scripting (XSS) flaw in an open-source business suite called Odoo that could be exploited to impersonate any victim on a vulnerable Odoo instance as well as exfiltrate valuable data.

Earlier this year, security weaknesses were also disclosed in open-source software such as [Pretalx](https://www.sonarsource.com/blog/pretalx-vulnerabilities-how-to-get-accepted-at-every-conference/) and [OpenEMR](https://www.sonarsource.com/blog/openemr-remote-code-execution-in-your-healthcare-system/) that could pave the way for remote attackers to execute arbitrary code.

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

[Gentoo Linux](https://thehackernews.com/search/label/Gentoo%20Linux)[linux](https://thehackernews.com/search/label/linux)[sql injection](https://thehackernews.com/search/label/sql%20injection)

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

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](data:image/svg+xml;base64... "Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure")

Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](https://thehackernews.com/2025/09/fortra-goanywhere-cvss-10-flaw.html)

[![Cisco ASA Firewall Zero-Day Exploits Deploy RayInitiator and LINE VIPER Malware](data:image/svg+xml;base64... "Cisco ASA Firewall Zero-Day Exploits Deploy RayInitiator and LINE VIPER Ma...