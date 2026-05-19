---
title: Ivanti, Fortinet, SAP, VMware, n8n Patch RCE, SQL Injection, Privilege Escalation Flaws
url: https://thehackernews.com/2026/05/ivanti-fortinet-sap-vmware-n8n-patch.html
source: The Hacker News
date: 2026-05-18
fetch_date: 2026-05-19T06:05:21.343995
---

# Ivanti, Fortinet, SAP, VMware, n8n Patch RCE, SQL Injection, Privilege Escalation Flaws

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [Ivanti, Fortinet, SAP, VMware, n8n Patch RCE, SQL Injection, Privilege Escalation Flaws](https://thehackernews.com/2026/05/ivanti-fortinet-sap-vmware-n8n-patch.html)

**Ravie Lakshmanan**May 18, 2026Vulnerability / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2iqd3uRuOdLaM83LyZC9GOeOLeP9BnBVQQQzF7LZUeBTXfGo6e6b9c7PSC0Tkt_vhN_FUFUiDwnLXXNmzpIubE5bI0rA7dRaDhuiV35uiNTcMab7o8E_1ehn3CzUUsfno-6fYECbYzGNS1dyNof1ihn-hf4QYjLn7ZD53y_byQigukme9w-LAeBKDWXAg/s1700-e365/patches.jpg)

Ivanti, Fortinet, n8n, SAP, and VMware have released security fixes for various vulnerabilities that could be exploited by bad actors to bypass authentication and execute arbitrary code.

Topping the list is a [critical flaw](https://www.ivanti.com/blog/may-2026-security-update) impacting Ivanti Xtraction (CVE-2026-8043, CVSS score: 9.6) that could be exploited to achieve information disclosure or client-side attacks.

"External control of a file name in Ivanti Xtraction before version 2026.2 allows a remote authenticated attacker to read sensitive files and write arbitrary HTML files to a web directory, leading to information disclosure and possible client-side attacks," Ivanti [said](https://hub.ivanti.com/s/article/Security-Advisory---Ivanti-Xtraction-CVE-2026-8043?language=en_US) in an advisory.

Fortinet published advisories for two critical shortcomings affecting FortiAuthenticator and FortiSandbox, FortiSandbox Cloud, and FortiSandbox PaaS that could result in code execution -

* **[CVE-2026-44277](https://www.fortiguard.com/psirt/FG-IR-26-128)** (CVSS score: 9.1) - An improper access control vulnerability in FortiAuthenticator that may allow an unauthenticated attacker to execute unauthorized code or commands via crafted requests. (Fixed in FortiAuthenticator versions 6.5.7, 6.6.9, and 8.0.3)
* **[CVE-2026-26083](https://www.fortiguard.com/psirt/FG-IR-26-136)** (CVSS score: 9.1) - A missing authorization vulnerability in FortiSandbox, FortiSandbox Cloud, and FortiSandbox PaaS WEB UI that may allow an unauthenticated attacker to execute unauthorized code or commands via HTTP requests. (Fixed in FortiSandbox versions 4.4.9 and 5.0.2, FortiSandbox Cloud version 5.0.6, and FortiSandbox PaaS versions 4.4.9. and 5.0.2)

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

SAP also [shipped](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/may-2026.html) fixes for two critical vulnerabilities -

* **[CVE-2026-34260](https://nvd.nist.gov/vuln/detail/CVE-2026-34260)** (CVSS score: 9.6) - An SQL injection vulnerability in SAP S/4HANA
* **[CVE-2026-34263](https://nvd.nist.gov/vuln/detail/CVE-2026-34263)** (CVSS score: 9.6) - A missing authentication check in the SAP Commerce cloud configuration

"The vulnerability is caused by an overly permissive security configuration with improper rule ordering, allowing an unauthenticated user to perform malicious configuration upload and code injection, resulting in arbitrary server-side code execution," Onapsis [said](https://onapsis.com/blog/sap-security-patch-day-may-2026/) about CVE-2026-34263.

On the other hand, CVE-2026-34260 could be exploited by an attacker to inject malicious SQL statements and potentially impact the confidentiality and availability of the application. However, since the affected code only allows read access to data, the vulnerability does not compromise the integrity of the application.

"It allows a low-privileged, authenticated attacker to inject malicious SQL code via user-controlled input, potentially exposing sensitive database information and crashing the application," Pathlock [said](https://pathlock.com/blog/security-alerts/sap-patch-day-may-2026/).

Patches have also been released by Broadcom for a high-severity flaw in VMware Fusion (CVE-2026-41702, CVSS score: 7.8) that could pave the way for local privilege escalation. The issue has been addressed in version 26H1.

"VMware Fusion contains a TOCTOU (Time-of-check Time-of-use) vulnerability that occurs during an operation performed by a SETUID binary," Broadcom [said](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/37454). "A malicious actor with local non-administrative user privileges may exploit this vulnerability to escalate privileges to root on the system where Fusion is installed."

Round off the list is a set of five critical vulnerabilities impacting n8n -

* **[CVE-2026-42231](https://github.com/n8n-io/n8n/security/advisories/GHSA-q5f4-99jv-pgg5)** (CVSS score: 9.4) - A vulnerability in the xml2js library used to parse XML request bodies in n8n's webhook handler that allows prototype pollution via a crafted XML payload, enabling an authenticated user with permission to create or modify workflows to achieve remote code execution on the n8n host. (Fixed in n8n versions 1.123.32, 2.17.4, and 2.18.1)
* **[CVE-2026-42232](https://github.com/n8n-io/n8n/security/advisories/GHSA-hqr4-h3xv-9m3r)** (CVSS score: 9.4) - An authenticated user with permission to create or modify workflows could achieve global prototype pollution via the XML Node, leading to remote code execution when combined with other nodes exploiting the prototype pollution. (Fixed in n8n versions 1.123.32, 2.17.4, and 2.18.1)
* **[CVE-2026-44791](https://github.com/n8n-io/n8n/security/advisories/GHSA-wrwr-h859-xh2r)** (CVSS score: 9.4) - A bypass for CVE-2026-42232 that could result in remote code execution on the n8n host. (Fixed in n8n versions 1.123.43, 2.20.7, and 2.22.1)
* **[CVE-2026-44789](https://github.com/n8n-io/n8n/security/advisories/GHSA-c8xv-5998-g76h)** (CVSS score: 9.4) - An authenticated user with permission to create or modify workflows could achieve global prototype pollution via an unvalidated pagination parameter in the HTTP Request node, leading to remote code execution on the n8n host. (Fixed in n8n versions 1.123.43, 2.20.7, and 2.22.1)...