---
title: New cPanel Flaw Lets a Hosting Account With Mail Privileges Run Code as Root
url: https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account.html
source: The Hacker News
date: 2026-09-09
fetch_date: 2026-09-10T06:52:41.688349
---

# New cPanel Flaw Lets a Hosting Account With Mail Privileges Run Code as Root

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [New cPanel Flaw Lets a Hosting Account With Mail Privileges Run Code as Root](https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account.html)

**Swati Khandelwal**Sep 09, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgM_YdNiqGpEWkDm5hEkF-RhZ94vv84sJmONomdRsksJ65GwI388Va-uVIzXWhwZtHmBTF3oze2l4Sscj2zpTsn6lqdPWPKAeL1iP6SSyzvNBOA4dLAKxfSmfThhmQgIc_1AYGWG9dbrCLFg_dk4m8pCHxFcJBRnThru8PtB7UJqUy3VjW15-vQlRvuwpc/s1700-nu-rw-lo-l85-e365/cpanel-bug.jpg)

cPanel has patched a flaw that it says lets a single hosting account take control of an entire server. An authenticated account holder with mail-related privileges can create files of their choosing on the server through EmailTrack and, from there, run code as the root user.

cPanel published the [advisory on September 8](https://support.cpanel.net/hc/en-us/articles/43187903921559-Security-CVE-2026-67401-SQL-Injection-Vulnerability-in-cPanel-s-EmailTrack-Functionality-September-8-2026) and says every supported version of cPanel and WHM is affected.

The flaw is tracked as **CVE-2026-67401**. cPanel's advisory calls it an SQL injection issue in EmailTrack, but does not say which cPanel feature or privilege an account needs. cPanel's developer documentation lists an EmailTrack module that tracks email statistics, and the advisory does not say whether that is the affected code.

cPanel is web hosting control panel software. A customer manages one hosting account via cPanel, while the provider manages the entire machine via WHM as the root user.

Attackers exploited [a different cPanel flaw in April](https://thehackernews.com/2026/04/critical-cpanel-authentication.html). Taking over the panel is not the same as breaking into one customer's website, the security company Hadrian said at the time, because WHM gives an attacker root administrative access to the server.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

An attacker with that access can read every hosting account on the machine, change files and databases, create hidden accounts, install malware, steal credentials, and move into customer networks.

cPanel named these fixed builds:

| Release line | Fixed build |
| --- | --- |
| 11.110 | 11.110.0.143 |
| 11.134 | 11.134.0.55 |
| 11.136 | 11.136.0.39 |
| 11.138 | 11.138.0.4 |
| WP Squared | 11.138.1.9 |

A server can be updated from WHM under Home / cPanel / Upgrade to Latest Version. On the command line, [cPanel's instructions](https://support.cpanel.net/hc/en-us/articles/1500004959421-How-do-I-update-cPanel-WHM) are to log in as root and run /usr/local/cpanel/scripts/upcp --force.

The advisory does not explain how an SQL injection problem leads to file creation and then to root access.

The advisory also offers nothing to do in the meantime for servers that cannot update straight away. cPanel gave a step like that in its [July 30 advisory](https://support.cpanel.net/hc/en-us/articles/42285745783703-Security-CVE-2026-58048-Database-Privilege-Escalation) for a database flaw, where administrators who could not upgrade were told they could temporarily remove the MySQL feature from cPanel users.

The patched list covers the 110, 134, 136 and 138 release lines. cPanel patched the 11.118 and 11.126 lines in its July advisories, has not listed them since, and has not said whether they are still supported.

For the August flaw, the CVE record lists every version from 11.112.0.0 up to, but not including, 11.134.0.53 in the affected range and lists no fixed build in lines 118 or 126.

cPanel also does not say whether installing the patched build helps a server that was attacked before the update, or how an administrator would check.

The advisory carries no severity score. cPanel's recent CVEs are assigned through HackerOne, and the scores have been arriving in the CVE record rather than in the advisory.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/enterprise-ai-security-a)

The record for the August flaw was published on September 1, five days after that advisory. It scores that flaw 8.7 out of 10 on the CVSS scale, indicating high severity. No record had been published for CVE-2026-67401 when The Hacker News checked the CVE Program's record store on September 9.

No public exploit code or report of exploitation appeared in searches on September 9, and CVE-2026-67401 is absent from CISA's [Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) in the version released on September 8.

Neither check rules out exploitation. That April flaw, an authentication bypass that needed no account at all, is in the same catalog with known use in ransomware campaigns.

Two other cPanel flaws disclosed since the end of July also start from an ordinary hosting account. A July 30 advisory covered a database flaw that could let an account with access to the database feature run database commands with full administrative privileges. cPanel described an [August 27 flaw in domain parking](https://thehackernews.com/2026/08/critical-cpanel-flaw-could-let-one.html) that ended the same way as this one: code execution as root.

Repositories that present themselves as working exploits for those two flaws were online when The Hacker News checked on September 9.

cPanel credits Ali Mustafa (rz1027) and abed1526 with reporting this one. The CVE record for the August flaw credits the same name, Ali Mustafa.

Neither cPanel's advisories nor that record ties the two flaws to the same code. The records classify them differently: eval injection for the August flaw and SQL injection for this one, according to cPanel's own title.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin....