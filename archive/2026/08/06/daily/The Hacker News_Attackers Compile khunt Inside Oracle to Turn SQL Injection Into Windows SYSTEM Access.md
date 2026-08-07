---
title: Attackers Compile khunt Inside Oracle to Turn SQL Injection Into Windows SYSTEM Access
url: https://thehackernews.com/2026/08/attackers-compile-khunt-inside-oracle.html
source: The Hacker News
date: 2026-08-06
fetch_date: 2026-08-07T04:30:25.798377
---

# Attackers Compile khunt Inside Oracle to Turn SQL Injection Into Windows SYSTEM Access

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

# [Attackers Compile khunt Inside Oracle to Turn SQL Injection Into Windows SYSTEM Access](https://thehackernews.com/2026/08/attackers-compile-khunt-inside-oracle.html)

**Swati Khandelwal**Aug 06, 2026Database Security / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWGMHYrRkDGf3XV_lOoUbE1UCSjvcN9x-XNpNGpX_f45JqZzd2FrxJ-metvu-U5VyDqH2PGNaY9MiSeShhH-YVN3O4ryN5lh4ICsuXtz0-DuCSAgnywXUifDOf_qZS81AtjRGNQWgs1QnL4Eu54icswla_ZK7qGoZqWDaVzPX46pmcTrvj_ec0yQwrt9k/s1700-e365/oracle-root.jpg)

Attackers broke into an organization's Oracle database through a SQL injection flaw in a public-facing web application, then installed a post-exploitation toolkit without writing an executable to disk. They fed Java source code to the database, let Oracle compile it into stored schema objects, and ran commands from inside the database engine.

Huntress, which tracks the toolkit as **khunt**, investigated after credential-theft detections fired on July 27, 2026, and traced the chain to SYSTEM-level code execution on the underlying Windows server.

The flaw sat in the application, where an autocomplete search field passed unvalidated input to the database over a Java Database Connectivity (JDBC) connection. The account behind that connection had enough privilege to create Java objects.

No Oracle patch closes either the application flaw or the account privilege behind it. Finding the toolkit means hunting: search the Oracle installation for object names beginning Khunt, and SQL logs for KHUNT%.

A Java class compiled into a database schema object is not a process, a binary, or a file on the filesystem, and endpoint detection and response products do not generally inspect Oracle's internals. As Huntress frames it, the database stops being something attackers query and becomes a beachhead they attack from.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

Oracle ships an embedded Java Virtual Machine, and the CREATE JAVA SOURCE statement lets a user hand it Java code that the database compiles and stores as a schema object. In a user's own schema, [Oracle's documentation](https://docs.oracle.com/en/database/oracle/oracle-database/26/sqlrf/CREATE-JAVA.html) puts the bar at a single system privilege, CREATE PROCEDURE. Spawning an operating-system process from that code runs through [Runtime.exec](https://docs.oracle.com/en/database/oracle/oracle-database/21/jjdev/Runtime-exe-secure-use.html), which needs its own file-execution permission, and Oracle says those are [issued only by privileged administrators](https://docs.oracle.com/en/database/oracle/oracle-database/19/jjdev/using-Runtime-exec.html).

Huntress does not say which grants the compromised account held, or whether the attackers had to add any. The chain succeeded, so it had enough for both.

The technique is at least two decades old. Marco Ivaldi's [raptor\_oraexec.sql](https://github.com/0xdea/exploits/blob/master/oracle/raptor_oraexec.sql), dated 2006, creates an Oracle source object with command-execution and file-read methods, then publishes them to SQL through PL/SQL wrappers. The khunt objects use the same basic architecture. "The use of the technique in the wild has rarely been documented," [Huntress said](https://www.huntress.com/blog/khunt-malware-sql-injection-oracle).

Six Java objects and several khunt\_\* PL/SQL wrappers made up the toolkit:

* KhuntCmd loaded cmd.exe and ran arbitrary operating-system commands passed in as SQL.
* KhuntHash read usernames and [password hashes](https://docs.oracle.com/en/database/oracle/oracle-database/19/dbseg/database-authentication-users1.html) from Oracle's internal user table and wrote them to a file.
* KhuntFS and KhuntFS2 listed, read, searched, and sized files.
* KhuntT confirmed the toolkit was reachable, and KhuntUnzip unpacked archives.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Running cmd.exe /c whoami through KhuntCmd returned SYSTEM. The attackers then used PowerShell and reg.exe to copy the SECURITY and SYSTEM registry hives into F:\Oracle, ran tasklist /svc into khunttasks.txt, and copied the SAM and SECURITY hives with esentutl.exe.

Huntress observed the files being staged locally, but did not establish that they were exfiltrated. The firm named no threat actor and traced the malicious requests to 178.162.151[.]229.

Those indicators are specific to this toolkit, so no search for Khunt or KHUNT% will surface the technique behind it. The fix is parameterized queries and input validation in the application, plus least privilege underneath: an account serving a public-facing app should not be able to author Java sources or run stored procedures it has no reason to touch.

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

[database security](https://thehackernews.com/search/label/database%20security), [endpoint security](https://thehackernews.com/search/label/endpoint%20security), [oracle](https://thehackernews.com/search/label/oracle), [privilege escalation](https://thehackernews.com/search/label/privilege%20escalation), [SQL Injection](https://thehackernews.com/search/label/SQL%20Injection), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security), [Windows Security](https://thehackernews.com/search/label/Windows%20Security)

⚡ Top Stories This Week

[![New Bit2Watt Attack Co...