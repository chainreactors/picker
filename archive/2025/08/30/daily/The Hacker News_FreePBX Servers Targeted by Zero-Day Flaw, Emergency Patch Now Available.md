---
title: FreePBX Servers Targeted by Zero-Day Flaw, Emergency Patch Now Available
url: https://thehackernews.com/2025/08/freepbx-servers-targeted-by-zero-day.html
source: The Hacker News
date: 2025-08-30
fetch_date: 2025-10-07T00:50:25.651610
---

# FreePBX Servers Targeted by Zero-Day Flaw, Emergency Patch Now Available

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

# [FreePBX Servers Targeted by Zero-Day Flaw, Emergency Patch Now Available](https://thehackernews.com/2025/08/freepbx-servers-targeted-by-zero-day.html)

**Aug 29, 2025**Ravie LakshmananZero-Day / Vulnerability

[![FreePBX Servers Targeted by Zero-Day](data:image/png;base64... "FreePBX Servers Targeted by Zero-Day")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_JAqQ7frur0oVPE5CX27CFAfNZq8Oh8faWB9xBEFJPzoZOI2GWZgfTeWaC2uld54fcFXqCmQBI6cbcuhVW4wPSxCwXezy3SO1KfqQ-ZRZnyRxPp9Vkoi35RDVl4qXl7oMQKbknp629ihfrf9SfqgVLB16UUJYEbIDXkLqS3W0L4LnpBAc54NP3CXqeadd/s790-rw-e365/zeroday.jpg)

The Sangoma FreePBX Security Team has issued an advisory warning about an actively exploited FreePBX zero-day vulnerability that impacts systems with an administrator control panel (ACP) exposed to the public internet.

[FreePBX](https://thehackernews.com/2020/11/premium-rate-phone-fraudsters-hack-voip.html) is an open-source private branch exchange (PBX) platform widely used by businesses, call centers, and service providers to manage voice communications. It's built on top of [Asterisk](https://www.asterisk.org/asteriskexchange/freepbx/), an open-source communication server.

The vulnerability, assigned the CVE identifier **CVE-2025-57819**, carries a CVSS score of 10.0, indicating maximum severity.

"Insufficiently sanitized user-supplied data allows unauthenticated access to FreePBX Administrator, leading to arbitrary database manipulation and remote code execution," the project maintainers [said](https://github.com/FreePBX/security-reporting/security/advisories/GHSA-m42g-xg4c-5f3h) in an advisory.

The issue impacts the following versions -

* FreePBX 15 prior to 15.0.66
* FreePBX 16 prior to 16.0.89, and
* FreePBX 17 prior to 17.0.3

Sangoma said an unauthorized user began accessing multiple FreePBX version 16 and 17 systems connected to the internet starting on or before August 21, 2025, specifically those that have inadequate IP filtering or access control lists (ACLs), by taking advantage of a sanitization issue in the processing of user-supplied input to the commercial "endpoint" module.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The initial access obtained using this method was then combined with other steps to potentially gain root-level access on the target hosts, it added.

In light of active exploitation, users are [advised](https://community.freepbx.org/t/security-advisory-please-lock-down-your-administrator-access/107203) to upgrade to the latest supported versions of FreePBX and restrict public access to the administrator control panel. Users are also advised to scan their environments for the following indicators of compromise (IoCs) -

* File "/etc/freepbx.conf" recently modified or missing
* Presence of the file "/var/www/html/.clean.sh" (this file should not exist on normal systems)
* Suspicious POST requests to "modular.php" in Apache web server logs dating back to at least August 21, 2025
* Phone calls placed to extension 9998 in Asterisk call logs and CDRs are unusual (unless previously configured)
* Suspicious "ampuser" user in the ampusers database table or other unknown users

"We are seeing active exploitation of FreePBX in the wild with activity traced back as far as August 21 and backdoors being dropped post-compromise," watchTowr CEO Benjamin Harris said in a statement shared with The Hacker News.

"While it's early, FreePBX (and other PBX platforms) have long been a favorite hunting ground for ransomware gangs, initial access brokers and fraud groups abusing premium billing. If you use FreePBX with an endpoint module, assume compromise. Disconnect systems immediately. Delays will only increase the blast radius."

### CVE-2025-57819 Added to CISA KEV Catalog

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Friday [added](https://www.cisa.gov/news-events/alerts/2025/08/29/cisa-adds-one-known-exploited-vulnerability-catalog) CVE-2025-57819 to its Known Exploited Vulnerabilities (KEV) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by September 19, 2025.

"Sangoma FreePBX contains an authentication bypass vulnerability due to insufficiently sanitized user-supplied data allows unauthenticated access to FreePBX Administrator leading to arbitrary database manipulation and remote code execution," the agency [said](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).

### Technical Details of CVE-2025-57819 Released

In an analysis released on September 10, 2025, watchTowr Labs said the vulnerability has been used as a conduit to serve web shells and a bash cleanup script ("/var/www/html/.clean.sh") designed to erase evidence after backdoor access.

The cybersecurity company also noted that CVE-2025-57819 stems from the fact that it allows access to certain files ending with ".php" directly without the need for authentication (e.g., "/admin/ajax.php") and combine it with a post-auth SQL Injection in the FreePBX endpoint module.

"The custom FreePBX class loader allows you to include any file ending with the .php extension from the admin/modules location," it [noted](https://labs.watchtowr.com/you-already-have-our-personal-data-take-our-phone-calls-too-freepbx-cve-2025-57819/). "The official patch focuses narrowly on fixing the SQL Injection in the endpoint module. But the bigger issue – this 'authentication bypass' quirk that lets you include .php files pre-auth – sits in the core FreePBX code untouched."

watchTowr said this behavior on fully patched systems exposes a "juicy" attack surface that allows bad actors to directly hit certain module .php files without logging in.

As a next step, the SQL injection could be transformed into a full-blown remote code execution scenario by inserting a malicious row into a table called "cron\_jobs" by specifying the command to be executed. In all, an attacker can issue an HTTP request as below to achieve code execution -

```
GET /admin/ajax.php?module=Fr...