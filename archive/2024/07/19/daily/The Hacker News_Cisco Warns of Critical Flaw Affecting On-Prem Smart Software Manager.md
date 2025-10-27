---
title: Cisco Warns of Critical Flaw Affecting On-Prem Smart Software Manager
url: https://thehackernews.com/2024/07/cisco-warns-of-critical-flaw-affecting.html
source: The Hacker News
date: 2024-07-19
fetch_date: 2025-10-06T17:44:23.987356
---

# Cisco Warns of Critical Flaw Affecting On-Prem Smart Software Manager

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

# [Cisco Warns of Critical Flaw Affecting On-Prem Smart Software Manager](https://thehackernews.com/2024/07/cisco-warns-of-critical-flaw-affecting.html)

**Jul 18, 2024**Ravie Lakshmanan

[![Smart Software Manager](data:image/png;base64... "Smart Software Manager")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6kQGLCd5dG9hrwNd08NUuVNOMNbm-q3l7Vju6IN635OZMUPAWUcCj7tH9pgo8_dG2STGkQg5thiZ3xltY8lodlzvggKc8JS82rgKDR5lyLcm66Gy8TvvClLHHuAAFxoClYkCZmjaGK4AtvG12eifXqCidhHHH0TsybnrCgeeoTwYj0cWoYOAmXWrHh74V/s790-rw-e365/cisco.png)

Cisco has released patches to address a maximum-severity security flaw impacting Smart Software Manager On-Prem (Cisco SSM On-Prem) that could enable a remote, unauthenticated attacker to change the password of any users, including those belonging to administrative users.

The vulnerability, tracked as **CVE-2024-20419**, carries a CVSS score of 10.0.

"This vulnerability is due to improper implementation of the password-change process," the company [said](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cssm-auth-sLw3uhUy) in an advisory. "An attacker could exploit this vulnerability by sending crafted HTTP requests to an affected device. A successful exploit could allow an attacker to access the web UI or API with the privileges of the compromised user."

The shortcoming affects Cisco SSM On-Prem versions 8-202206 and earlier. It has been fixed in version 8-202212. It's worth noting that version 9 is not susceptible to the flaw.

Cisco said there are no workarounds that resolve the issue, and that it's not aware of any malicious exploitation in the wild. Security researcher Mohammed Adel has been credited with discovering and reporting the bug.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Also fixed by the networking equipment maker is another critical file write vulnerability in Secure Email Gateway (CVE-2024-20401, CVSS score: 9.8) that lets attackers add new users with root privileges and permanently crash the appliances using emails with malicious attachments.

"An attacker could exploit this vulnerability by sending an email that contains a crafted attachment through an affected device," it [noted](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-afw-bGG2UsjH). "A successful exploit could allow the attacker to replace any file on the underlying file system."

"The attacker could then perform any of the following actions: add users with root privileges, modify the device configuration, execute arbitrary code, or cause a permanent denial-of-service (DoS) condition on the affected device."

The flaw affects SEG devices if it is running a vulnerable release of Cisco AsyncOS and if the following prerequisites are met -

* The file analysis feature (part of Cisco Advanced Malware Protection) or the content filter feature is enabled and assigned to an incoming mail policy
* The Content Scanner Tools version is earlier than 23.3.0.4823

A patch for CVE-2024-20401 is available via Content Scanner Tools package versions 23.3.0.4823 and later, which is included by default in Cisco AsyncOS for Cisco Secure Email Software releases 15.5.1-055 and later.

### CISA Adds 3 Flaws to KEV Catalog

The disclosure comes as the U.S. Cybersecurity and Infrastructure Security Agency (CISA) [added](https://www.cisa.gov/news-events/alerts/2024/07/17/cisa-adds-three-known-exploited-vulnerabilities-catalog) three vulnerabilities to its Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog, based on evidence of active exploitation -

* **[CVE-2024-34102](https://nvd.nist.gov/vuln/detail/CVE-2024-34102)** (CVSS score: 9.8) - Adobe Commerce and Magento Open Source Improper Restriction of XML External Entity Reference (XXE) Vulnerability
* **[CVE-2024-28995](https://nvd.nist.gov/vuln/detail/CVE-2024-28995)** (CVSS score: 8.6) - SolarWinds Serv-U Path Traversal Vulnerability
* **[CVE-2022-22948](https://nvd.nist.gov/vuln/detail/CVE-2022-22948)** (CVSS score: 6.5) - VMware vCenter Server Incorrect Default File Permissions Vulnerability

CVE-2024-34102, which is also referred to as [CosmicSting](https://thehackernews.com/2024/06/over-110000-websites-affected-by.html), is a severe security flaw arising from improper handling of nested deserialization, allowing attackers to [achieve remote code execution](https://www.vicarius.io/vsociety/posts/cosmicsting-critical-unauthenticated-xxe-vulnerability-in-adobe-commerce-and-magento-cve-2024-34102). A proof-of-concept (PoC) exploit for the flaw was [released](https://www.assetnote.io/resources/research/why-nested-deserialization-is-harmful-magento-xxe-cve-2024-34102) by Assetnote late last month.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Reports about the exploitation of [CVE-2024-28995](https://thehackernews.com/2024/06/solarwinds-serv-u-vulnerability-under.html), a directory transversal vulnerability that could enable access to sensitive files on the host machine, were [detailed](https://censys.com/cve-2024-28995/) by GreyNoise, including attempts to read files such as /etc/passwd.

The abuse of CVE-2022-22948, on the other hand, has been [attributed](https://thehackernews.com/2024/06/chinese-cyber-espionage-group-exploits.html) by Google-owned Mandiant to a China-nexus cyber espionage group known as UNC3886, which has a history of leveraging zero-day flaws in Fortinet, Ivanti, and VMware appliances.

Federal agencies are required to apply mitigations per vendor instructions by August 7, 2024, to secure their networks against active threats.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we...