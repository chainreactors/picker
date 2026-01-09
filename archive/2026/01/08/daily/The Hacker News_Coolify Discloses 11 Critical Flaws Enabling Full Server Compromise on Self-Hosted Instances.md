---
title: Coolify Discloses 11 Critical Flaws Enabling Full Server Compromise on Self-Hosted Instances
url: https://thehackernews.com/2026/01/coolify-discloses-11-critical-flaws.html
source: The Hacker News
date: 2026-01-08
fetch_date: 2026-01-09T03:32:02.909840
---

# Coolify Discloses 11 Critical Flaws Enabling Full Server Compromise on Self-Hosted Instances

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [Coolify Discloses 11 Critical Flaws Enabling Full Server Compromise on Self-Hosted Instances](https://thehackernews.com/2026/01/coolify-discloses-11-critical-flaws.html)

**Jan 08, 2026**Ravie LakshmananVulnerability / Container Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgiTPlT13VFHh6Gnrmg0ozwHRlYaVFKySt-BBjowr5Az7KwqG4PXVrH9n_1YTLZpuJHf02fu1TJBTeHKLnDJ3UTzhZR_8ldCYcHRoSoUaqhmj1vrBqDGn3StC_LYhVzLI5S-iFELOqLhnet3zlgB91h5KehCfvyoQ9IQc_MZt_bE-Y3SJ0fvVUAkLVqx6zw/s790-rw-e365/coolify.jpg)

Cybersecurity researchers have disclosed details of multiple critical-severity security flaws affecting [Coolify](https://github.com/coollabsio/coolify), an open-source, self-hosting platform, that could result in authentication bypass and remote code execution.

The list of vulnerabilities is as follows -

* **[CVE-2025-66209](https://github.com/coollabsio/coolify/security/advisories/GHSA-vm5p-43qh-7pmq)** (CVSS score: 10.0) - A command injection vulnerability in the database backup functionality allows any authenticated user with database backup permissions to execute arbitrary commands on the host server, resulting in container escape and full server compromise
* **[CVE-2025-66210](https://github.com/coollabsio/coolify/security/advisories/GHSA-q33h-22xm-4cgh)** (CVSS score: 10.0) - An authenticated command injection vulnerability in the database import functionality allows attackers to execute arbitrary commands on managed servers, leading to full infrastructure compromise
* **[CVE-2025-66211](https://github.com/coollabsio/coolify/security/advisories/GHSA-24mp-fc9q-c884)** (CVSS score: 10.0) - A command injection vulnerability in the PostgreSQL init script management allows authenticated users with database permissions to execute arbitrary commands as root on the server
* **[CVE-2025-66212](https://github.com/coollabsio/coolify/security/advisories/GHSA-q7rg-2j7p-83gp)** (CVSS score: 10.0) - An authenticated command injection vulnerability in the Dynamic Proxy Configuration functionality allows users with server management permissions to execute arbitrary commands as root on managed servers
* **[CVE-2025-66213](https://github.com/coollabsio/coolify/security/advisories/GHSA-cj2c-9jx8-j427)** (CVSS score: 10.0) - An authenticated command injection vulnerability in the File Storage Directory Mount functionality allows users with application/service management permissions to execute arbitrary commands as root on managed servers
* **[CVE-2025-64419](https://github.com/coollabsio/coolify/security/advisories/GHSA-234r-xrrg-m8f3)** (CVSS score: 9.7) - A command injection vulnerability via docker-compose.yaml that enables attackers to execute arbitrary system commands as root on the Coolify instance
* **[CVE-2025-64420](https://github.com/coollabsio/coolify/security/advisories/GHSA-qwxj-qch7-whpc)** (CVSS score: 10.0) - An information disclosure vulnerability that allows low-privileged users to view the private key of the root user on the Coolify instance, allowing them to gain unauthorized access to the server via SSH and authenticate as the root user using the key
* **[CVE-2025-64424](https://github.com/coollabsio/coolify/security/advisories/GHSA-qx24-jhwj-8w6x)** (CVSS score: 9.4) - A command injection vulnerability was found in the git source input fields of a resource, allowing a low-privileged user (member) to execute system commands as root on the Coolify instance
* **[CVE-2025-59156](https://github.com/coollabsio/coolify/security/advisories/GHSA-h5xw-7xvp-xrxr)** (CVSS score: 9.4) - An operating system command injection vulnerability that allows a low-privileged user to inject arbitrary Docker Compose directives and achieve root-level command execution on the underlying host
* **[CVE-2025-59157](https://github.com/coollabsio/coolify/security/advisories/GHSA-5cg9-38qj-8mc3)** (CVSS score: 10.0) - An operating system command injection vulnerability that allows a regular user to inject arbitrary shell commands that execute on the underlying server by using the Git Repository field during deployment
* **[CVE-2025-59158](https://github.com/coollabsio/coolify/security/advisories/GHSA-h52r-jxv9-9vhf)** (CVSS score: 9.4) - An improper encoding or escaping of the data that allows an authenticated user with low privileges to conduct a stored cross-site scripting (XSS) attack during project creation that's automatically executed in the browser context when an administrator later attempts to delete the project or its associated resource

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

The following versions are impacted by the shortcomings -

* **CVE-2025-66209, CVE-2025-66210, CVE-2025-66211** - <= 4.0.0-beta.448 (Fixed in >= 4.0.0-beta.451)
* **CVE-2025-66212, CVE-2025-66213** - <= 4.0.0-beta.450 (Fixed in >= 4.0.0-beta.451)
* **CVE-2025-64419** - < 4.0.0-beta.436 (Fixed in >= 4.0.0-beta.445)
* **CVE-2025-64420, CVE-2025-64424** - <= 4.0.0-beta.434 (Fix status unclear)
* **CVE-2025-59156, CVE-2025-59157, CVE-2025-59158** - <= 4.0.0-beta.420.6 (Fixed in 4.0.0-beta.420.7)

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgBs7zEKLRZNnbqqKYhi8c3jphr6G5XMUspu7_NpjLylqOFqV7JrT3mXgvuxp9o4fMGrqL7aWzvO40-l4nMSx0Y8VALwKg8vV4VHisTKo355kO37s6_e4gfoV1t2o_DId9KcVKd2ckxY29vsjHSby3byVQzP1xJhiGLLXI4tErGp5HoTbQXRPGCWod1Kvgz/s790-rw-e365/Coolify.png) |
| Source: Censys |

According to [data](https://censys.com/advisory/cve-2025-64424-cve-2025-64420-cve-2025-64419) from attack surface management platform Censys, there are about [52,890 exposed Coolify hosts](https://platform.censys.io/search?q=host.services.endpoints.http.headers%3A%28key%3D%22Set-Cookie%22+and+value%3A%22coolify_session%22%29+or+host.services.endpoints.http.html_title%3A%22coolify%22+or+host.services.endpoints.http.favicons.hash_md5%3D%22e34e6be15d327d4a85c9fad467bc3f67%22) as of January 8, 2026, with most of them located in Germany (15,000), the U...