---
title: CISA Warns of Critical Vulnerabilities in 3 Industrial Control System Software
url: https://thehackernews.com/2022/11/cisa-warns-of-critical-vulnerabilities.html
source: The Hacker News
date: 2022-11-05
fetch_date: 2025-10-03T21:47:59.910056
---

# CISA Warns of Critical Vulnerabilities in 3 Industrial Control System Software

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

# [CISA Warns of Critical Vulnerabilities in 3 Industrial Control System Software](https://thehackernews.com/2022/11/cisa-warns-of-critical-vulnerabilities.html)

**Nov 04, 2022**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjy10jV7SOEGAAFdcoLSsEA8Ce0dwzClAZ4_jR22mCUD386h1vkI6AH0xPDWIeKSchusdOv88VG3fkas5xvmHpSGubQU0WNLyo7ebUofMo3GuVUFAYjdCQNZgHogvrVsMHtZIuPvu6l1hxXwNC9WPypc5KevLSI-FDOVsep7vAT-ug-wV-8IU2zy6GP/s790-rw-e365/ics.jpg)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has [published](https://www.cisa.gov/uscert/ncas/current-activity/2022/11/03/cisa-releases-three-industrial-control-systems-advisories) three Industrial Control Systems (ICS) advisories about multiple vulnerabilities in software from ETIC Telecom, Nokia, and Delta Industrial Automation.

Prominent among them is a set of three flaws affecting ETIC Telecom's Remote Access Server (RAS), which "could allow an attacker to obtain sensitive information and compromise the vulnerable device and other connected machines," CISA said.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

This includes CVE-2022-3703 (CVSS score: 9.0), a critical flaw that stems from the RAS web portal's inability to verify the authenticity of firmware, thereby making it possible to slip in a rogue package that grants backdoor access to the adversary.

Two other flaws relate to a directory traversal bug in the RAS API (CVE-2022-41607, CVSS score: 8.6) and a file upload issue (CVE-2022-40981, CVSS score: 8.3) that can be exploited to read arbitrary files and upload malicious files that can compromise the device.

Israeli industrial cybersecurity firm OTORIO has been credited with discovering and reporting the flaws. All versions of ETIC Telecom RAS 4.5.0 and prior are vulnerable, with the issues [addressed](https://www.etictelecom.com/en/softwares-download/) by the French company in version 4.7.3.

The second advisory from CISA concerns three flaws in Nokia's ASIK AirScale 5G Common System Module (CVE-2022-2482, CVE-2022-2483, and CVE-2022-2484), which could pave the way for arbitrary code execution and stoppage of secure boot functionality. All the flaws are rated 8.4 on the CVSS severity scale.

"Successful exploitation of these vulnerabilities could result in the execution of a malicious kernel, running of arbitrary malicious programs, or running of modified Nokia programs," CISA noted.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The Finnish telecom giant is said to have published mitigation instructions for the flaws that impact ASIK versions 474021A.101 and ASIK 474021A.102. The agency is recommending that users contact Nokia directly for further information.

Lastly, the cybersecurity authority has also warned of a path traversal vulnerability (CVE-2022-2969, CVSS score: 8.1) that affects Delta Industrial Automation's DIALink products and could be leveraged to plant malicious code on targeted appliances.

The shortcoming has been addressed in version 1.5.0.0 Beta 4, which CISA said can be obtained by reaching out to Delta Industrial Automation directly or via Delta field application engineering (FAEs).

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

[CISA](https://thehackernews.com/search/label/CISA)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

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

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](data:image/sv...