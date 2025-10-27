---
title: Cisco Issues Patch for High-Severity VPN Hijacking Bug in Secure Client
url: https://thehackernews.com/2024/03/cisco-issues-patch-for-high-severity.html
source: The Hacker News
date: 2024-03-09
fetch_date: 2025-10-04T12:12:33.892393
---

# Cisco Issues Patch for High-Severity VPN Hijacking Bug in Secure Client

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

# [Cisco Issues Patch for High-Severity VPN Hijacking Bug in Secure Client](https://thehackernews.com/2024/03/cisco-issues-patch-for-high-severity.html)

**Mar 08, 2024**Ravie LakshmananNetwork Security / Vulnerability

[![VPN Hijacking Bug](data:image/png;base64... "VPN Hijacking Bug")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjaaAPOVxPO0YHuxnsfw5jiHI1LU3BX1FsRt7b03_3rrCMup0bIgwINorRpPhekZDYtnlkopOJoc4psihkW7Mm-AlPg1JV5Cee15it-mo3FolBqHB9Md7lrZkUqzo72LdjIdAkX_XqYRN5R0myNyl2kyN-JZCYkFaroL_r1geuT3iBZ594aHCixNZ9X9k4O/s790-rw-e365/cisco.jpg)

Cisco has released patches to address a high-severity security flaw impacting its Secure Client software that could be exploited by a threat actor to open a VPN session with that of a targeted user.

The networking equipment company described the vulnerability, tracked as CVE-2024-20337 (CVSS score: 8.2), as allowing an unauthenticated, remote attacker to conduct a carriage return line feed ([CRLF](https://owasp.org/www-community/vulnerabilities/CRLF_Injection)) injection attack against a user.

Arising as a result of insufficient validation of user-supplied input, a threat actor could leverage the flaw to trick a user into clicking on a specially crafted link while establishing a VPN session.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"A successful exploit could allow the attacker to execute arbitrary script code in the browser or access sensitive, browser-based information, including a valid SAML token," the company [said](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-secure-client-crlf-W43V4G7) in an advisory.

"The attacker could then use the token to establish a remote access VPN session with the privileges of the affected user. Individual hosts and services behind the VPN headend would still need additional credentials for successful access."

The vulnerability impacts Secure Client for Windows, Linux, and macOS, and has been addressed in the following versions -

* Earlier than 4.10.04065 (not vulnerable)
* 4.10.04065 and later (fixed in 4.10.08025)
* 5.0 (migrate to a fixed release)
* 5.1 (fixed in 5.1.2.42)

Amazon security researcher [Paulos Yibelo Mesfin](https://twitter.com/PaulosYibelo/status/1765502730464846310?t=Aadv) has been credited with discovering and reporting the flaw, telling The Hacker News that the shortcoming allows attackers to access local internal networks when a target visits a website under their control.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Cisco has also published fixes for CVE-2024-20338 (CVSS score: 7.3), another high-severity flaw in Secure Client for Linux that could permit an authenticated, local attacker to elevate privileges on an affected device. It has been resolved in version 5.1.2.42.

"An attacker could exploit this vulnerability by copying a malicious library file to a specific directory in the filesystem and persuading an administrator to restart a specific process," it [said](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-secure-privesc-sYxQO6ds). "A successful exploit could allow the attacker to execute arbitrary code on an affected device with root privileges."

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

[cyberattack](https://thehackernews.com/search/label/cyberattack)[network security](https://thehackernews.com/search/label/network%20security)[privilege escalation](https://thehackernews.com/search/label/privilege%20escalation)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware A...