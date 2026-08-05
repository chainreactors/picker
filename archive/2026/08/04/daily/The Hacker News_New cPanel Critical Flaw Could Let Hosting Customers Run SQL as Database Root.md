---
title: New cPanel Critical Flaw Could Let Hosting Customers Run SQL as Database Root
url: https://thehackernews.com/2026/08/new-cpanel-critical-flaw-could-let.html
source: The Hacker News
date: 2026-08-04
fetch_date: 2026-08-05T04:59:46.038833
---

# New cPanel Critical Flaw Could Let Hosting Customers Run SQL as Database Root

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

![cybersecurity](data:image/svg+xml;base64...)

# [New cPanel Critical Flaw Could Let Hosting Customers Run SQL as Database Root](https://thehackernews.com/2026/08/new-cpanel-critical-flaw-could-let.html)

**Swati Khandelwal**Aug 04, 2026Vulnerability / Database Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2LFB09rf16kl1_PinOnHkAY4GiI38_azQ2t-EWYRicFndp5DX-5KSfwVVEJxwEKp07oouBfkFg71MxwilLY_M2i3clk82hs5-Xr-PgDj69JeYzTsPjp_8sdNZIminQFonHRq2GqWDXJuwGqpT4Na485_pILlvMSlBdSMqWYWqTHDrUC_9OdOW-kCdSeM/s1700-e365/cpanel.jpg)

cPanel has patched a flaw that let an authenticated hosting customer execute SQL in the database's root context, crossing the privilege boundary between a cPanel account and the server's administrative database identity. It shipped in a targeted security release that closes two other routes past account boundaries.

The database bug is tracked as **CVE-2026-58048** (CVSS 4.0 score: 9.4) and affects all supported versions of cPanel & WHM, along with WP Squared. Reaching it requires a valid cPanel account and access to the MySQL/MariaDB feature. From there, the vendor says the account holder could execute arbitrary database commands with full administrative privileges.

Depending on the operating system and database engine configuration, “this may extend to operating-system-level compromise.”

cPanel patched `CVE-2026-58048` in these builds:

* 11.110.0.137
* 11.118.0.71
* 11.126.0.78
* 11.134.0.48
* 11.136.0.32
* 138.1.6 for WP Squared

Servers that cannot update immediately can temporarily revoke the MySQL feature from cPanel users. That leaves existing databases running but prevents users from adding or removing databases. Administrators can update from WHM or use the [command documented by cPanel](https://support.cpanel.net/hc/en-us/articles/1500004959421-How-do-I-update-cPanel-WHM):

```
/usr/local/cpanel/scripts/upcp --force
```

[CISA's August 4 enrichment](https://github.com/cisagov/vulnrichment/blob/develop/2026/58xxx/CVE-2026-58048.json) recorded “Exploitation: none,” assessed the flaw as non-automatable, and rated its technical impact as total. That is a snapshot, and it says nothing about the days since.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

Under normal operation, cPanel [supports database-level privileges](https://support.cpanel.net/hc/en-us/articles/360051227374-What-MySQL-privileges-are-supported-by-cPanel) that do not require `SUPER` access or allow global modifications. `CVE-2026-58048` bypasses those limits by causing SQL to run in the database administrative context.

The failure sits in cPanel's database-renaming process. The [HackerOne CNA record](https://nvd.nist.gov/vuln/detail/CVE-2026-58048) says SQL mode is not preserved when a database is renamed, causing SQL to execute in root context. According to the company's [database documentation](https://docs.cpanel.net/cpanel/databases/mysql-databases/), the system creates a replacement database, moves the original data, recreates grants and stored code, and then removes the old database and its grants.

The [vendor advisory](https://support.cpanel.net/hc/en-us/articles/42285745783703-Security-CVE-2026-58048-Database-Privilege-Escalation) titles the issue a privilege escalation and does not use the words SQL injection. The CNA classifies the same defect as CWE-89, SQL injection. The two records describe one bug from different angles. The advisory and CVE record do not identify the injected input, the affected SQL mode or the exact payload. Nor does it say whether Team User sub-accounts, the role-limited logins an account owner can create, meet its description of an authenticated account holder if they hold database access.

A Critical rating is a severity measure. It does not say how many servers have somebody in a position to use the flaw, and here that population is set by who holds accounts on the box: a server whose accounts all belong to one company is a different proposition from one selling accounts to strangers. The line is not clean, since accounts can be phished or resold. And it narrows nothing about consequence, which CISA rated total.

## Two more in the same build

[`CVE-2026-58047`](https://support.cpanel.net/hc/en-us/articles/42285024734743-Security-CVE-2026-58047-HTTP-Request-Smuggling) (CVSS 4.0 score: 5.6) is an HTTP request-smuggling issue in `cpsrvd`, the daemon that serves the cPanel and WHM interfaces. Under limited conditions, an unauthenticated remote attacker may manipulate responses delivered to other users on the same server. The [CNA record](https://nvd.nist.gov/vuln/detail/CVE-2026-58047) says credentials could leak as a result.

Where patching has to wait, the workaround is to disable backend connection reuse by setting `cpsrvd_keepalives_disabled=1` in `/var/cpanel/cpanel.config` and restarting `cpsrvd`. cPanel says the workaround forces a new TCP and TLS connection for each request on ports 2083, 2087 and 2096, increasing latency and CPU use on busy servers. cPanel credits Vincent55 Yang with reporting both CVEs.

The third cPanel advisory covers [`GCVE-25-2026-07-45-3`](https://support.cpanel.net/hc/en-us/articles/42285884685207-Security-GCVE-25-2026-07-45-3-Exim-forward-Privilege-Escalation) in Exim. A local user's `.forward` file can trigger unsafe string expansion in the redirect router under certain pipe-transport configurations. Under cPanel's default configuration, the expansion and execution occur as the cPanel user, which the company says may allow privilege escalation from Team User sub-accounts.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

[Exim's advisory](https://www.exim.org/static/doc/security/EXIM-Security-2026-06-22.3/EXIM-Security-2026-06-22.3.txt) says exploitation requires a redirect router providing `.forward` handling, an accessible pipe transport, `force_command` enabled on that transport and execution as a privileged user. Exim 4.99.5 removes the vulnerable expansion.

Exim 4.99.5 also fixes [`GCVE-25-2026-07-45-1`](https://www.exim.org/static/doc/security/EXIM-Security-2026-06-22.1/EXIM-Security-2026-06-22.1.txt), a High-severity local directory traversal through queue-name command-line arguments. Exim says the flaw can access files outside the spool are...