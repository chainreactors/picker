---
title: Critical Splunk Enterprise Flaw Lets Attackers Run Code Without Authentication
url: https://thehackernews.com/2026/06/critical-splunk-enterprise-flaw-lets.html
source: The Hacker News
date: 2026-06-13
fetch_date: 2026-06-14T06:28:23.301223
---

# Critical Splunk Enterprise Flaw Lets Attackers Run Code Without Authentication

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Critical Splunk Enterprise Flaw Lets Attackers Run Code Without Authentication](https://thehackernews.com/2026/06/critical-splunk-enterprise-flaw-lets.html)

**Ravie Lakshmanan**Jun 13, 2026Vulnerability / Enterprise Software

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7NRzSRKbGdsTj1TIWcks4nX5u6n1U2vl5hxJ8KKFZ-JCAKlMQPXQNHA1i0otd63wcKJoZbeEc3oVa9o4uYNTRkRyZaJsJVGV7JUmlqjY5mQkrOXFQJXmUT1kOIZPU6CRdlwx6X7lyi7Iffz7gUIC-nYc2N1dzmiuo2hyphenhyphenPURZ3nKdQcsbLACKidjOeTbRh/s1700-e365/splunk.jpg)

Splunk has released security updates to address a critical security flaw in Splunk Enterprise that could be exploited to conduct unauthenticated file operations and even remote code execution.

The vulnerability, tracked as **CVE-2026-20253**, is rated 9.8 on the CVSS scoring system.

"In Splunk Enterprise versions below 10.2.4 and 10.0.7, an unauthenticated user could create or truncate arbitrary files through a PostgreSQL sidecar service endpoint," Splunk [said](https://advisory.splunk.com/advisories/SVD-2026-0603) in an alert this week.

"The vulnerability exists because the PostgreSQL sidecar service endpoint lacks authentication controls, allowing any network-reachable user to invoke file operations without credentials."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The issue has been addressed in the following versions -

* Splunk Enterprise 10.0.0 to 10.0.6 - Fixed in 10.0.7
* Splunk Enterprise 10.2.0 to 10.2.3 - Fixed in 10.2.4
* Splunk Enterprise 10.4 - Not affected

Splunk, which is part of Cisco, said Splunk Cloud is not impacted by the vulnerability as Postgres sidecars are not used in the product.

### What the Flaw is All About

On Friday, watchTowr Labs [released](https://labs.watchtowr.com/why-use-app-level-auth-when-every-database-has-auth-splunk-enterprise-cve-2026-20253-pre-auth-rce/) additional technical details of CVE-2026-20253, stating it could be exploited to achieve pre-authenticated remote code execution on susceptible systems through the "/v1/postgres/recovery/backup" and "/v1/postgres/recovery/restore" endpoints.

The attack chain works as follows -

* Connect to an attacker-controlled database and dump its contents into an arbitrary file using the /backup endpoint
* Load the dump of the attacker-controlled database into the local PostgreSQL instance using the /restore endpoint by including a "passfile" argument that specifies the path to a "[.pgpass](https://www.postgresql.org/docs/current/libpq-pgpass.html)" file ("/opt/splunk/var/packages/data/postgres/.pgpass") containing the password for the "postgres\_admin" user
* SQL queries defined in the database dump will get executed by Splunk's PostgreSQL instance

An attacker could weaponize this weakness to [define a new function](https://www.postgresql.org/docs/current/sql-createfunction.html) that uses [lo\_export](https://www.postgresql.org/docs/current/lo-funcs.html) - a function used to extract a BLOB from the database and save it as a file on the file system - to write attacker-controlled content to a file, following which the function gets executed during the restoration process.

"At this point, we can authenticate, restore attacker-controlled SQL, and interact with the local database," security researchers Piotr Bazydlo and Yordan Ganchev said. "Once we could restore attacker-controlled SQL into the local PostgreSQL instance, we quickly put together a database dump template that gave us a controlled file write."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

Armed with an arbitrary file write primitive on the Splunk file system, an attacker could escalate further to remote code execution by overwriting a Python script that Splunk frequently executes (e.g., "/opt/splunk/etc/apps/splunk\_secure\_gateway/bin/ssg\_enable\_modular\_input.py") to include the malicious payload.

The entire sequence of actions is below -

* Create a database and configure it such that a user can authenticate without a password and grant it sufficient permissions to invoke functions like lo\_export
* Use the /backup endpoint to drop a dump of the remote database onto the Splunk file system
* Use the /restore endpoint to load the malicious database dump, trigger execution of the malicious function during the restore process, and write an attacker-controlled Python script to the Splunk file system

Although there is no evidence of the flaw being exploited in the wild, the availability of the exploit specifics can be enough to drive threat actors to trigger opportunistic attempts. It's essential that users move quickly to apply the fixes to stay protected.

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

[cisco](https://thehackernews.com/search/label/cisco), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Enterprise Software](https://thehackernews.com/search/label/Enterprise%20Software), [PostgreSQL](https://thehackernews.com/search/label/PostgreSQL), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [Splunk](https://thehackernews.com/search/label/Splunk), [Vulnerab...