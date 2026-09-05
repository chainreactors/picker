---
title: PostgreSQL Fixes 12-Year-Old Logical Decoding Flaw Enabling Replication-Role Code Execution
url: https://thehackernews.com/2026/09/postgresql-fixes-12-year-old-logical.html
source: The Hacker News
date: 2026-09-04
fetch_date: 2026-09-05T06:30:36.018033
---

# PostgreSQL Fixes 12-Year-Old Logical Decoding Flaw Enabling Replication-Role Code Execution

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

# [PostgreSQL Fixes 12-Year-Old Logical Decoding Flaw Enabling Replication-Role Code Execution](https://thehackernews.com/2026/09/postgresql-fixes-12-year-old-logical.html)

**Swati Khandelwal**Sep 04, 2026Vulnerability / Database Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2Gb4Wd-HSxdrPbdtUFxmldzzEkPEZcW1NkT7tV9-EfTAjDENSExJBWmOey_IJ5UKjszQfCNGkVoBtuxya00rFMrh_lJUAuS66Gr3kvU8GgFjMr7DF-7Ux1rUqwz-aDhum8HkVjxNKQTc6DXHG203CPXwg9sOMcA7nfsq6A81C9cJhb3HUu9GZDIj7FZY/s1700-nu-rw-lo-l85-e365/PostgreSQL.jpg)

PostgreSQL has released updates to address a security flaw that allows an account with the REPLICATION attribute to run arbitrary code as the operating-system user running the database server.

The flaw, tracked as **CVE-2026-6471** (CVSS score: 7.2), has been present since logical decoding was introduced in PostgreSQL 9.4 in 2014. Versions before PostgreSQL 18.6, 17.11, 16.15, 15.19, and 14.24 are affected.

Exploitation requires an account carrying the REPLICATION attribute and a server running with wal\_level = logical. Backup tools, standby servers, change data capture (CDC) pipelines, and monitoring systems routinely hold that attribute.

The fix, shipped on August 13, adds a server parameter called output\_plugin\_libraries that lists which libraries may be loaded as logical decoding output plugins, defaulting to 'pgoutput, test\_decoding'.

Installations using any other output plugin, wal2json, and decoderbufs

among them, will have logical decoding refused after updating until an administrator adds the library to that list and reloads the server configuration.

"Previously, a replication user could select any loadable library for logical decoding, allowing exploits of various sorts. To allow locking this down without breaking setups that worked before, introduce a whitelist of allowed output plugins," the PostgreSQL Global Development Group said in the [18.6 release notes](https://www.postgresql.org/docs/release/18.6/).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The PostgreSQL Project credited Vladimir Tokarev and Yu Kunpeng with reporting the problem.

Tokarev detailed it in [a September 1 write-up](https://www.cyera.com/research/postgreshell-the-database-powering-much-of-the-internet-had-an-open-door-for-12-years) for data security firm Cyera Research, which names the flaw **PostGREShell**.

The plugin name supplied in a CREATE\_REPLICATION\_SLOT command is passed directly to the function that loads the library, Cyera said.

PostgreSQL's existing restriction on plugin paths, which confines non-superusers to a single administrator-controlled directory, is never called on the replication path. The replication protocol's parser accepts almost any character inside a double-quoted plugin name, including path separators and ../ traversal, so a full filesystem path reaches the loader as typed.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_uHL_ZX6Is55FpTKxgjxDByemE-RHNXuYO35tnsrCo6de9LMynGNsvZ7dTyUD0oIIZdYOSBmIip1LJOYjF3CrlsRSwo0_a1NbmBup00SXxiUlxoslIivxfT1awlSctBWdmA4S_vYlalhI53nqcldW0nrD3QXQ2T87Xa1PzDdLJ041mwS8QzzzT4YqJe8/s1700-nu-rw-lo-l85-e365/db-1.png)

On Windows, the server resolves a network path over Server Message Block (SMB) and fetches the library from a machine the attacker controls, writing nothing to the target, Cyera said.

On Linux and macOS, the same result requires enabling Network File System (NFS) automounting. Everywhere else the attacker needs an existing way to write a file to the server's disk. Code loaded this way runs inside the database backend process as the postgres operating-system user.

Cyera's test plugin then wrote the role catalog directly to make the replication account a PostgreSQL superuser. It also set up three persistence mechanisms that survive a server restart.

Cyera describes the REPLICATION attribute as a low-privilege backup credential, but PostgreSQL scored the flaw with Privileges Required set to High, a rating reproduced in [SUSE's own assessment](https://www.suse.com/security/cve/CVE-2026-6471.html).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgf4P5leG3QrY8D8d_1Fe2MbNc8DumdZG9zEReOrL6rXiMVYHtP_KL7GEt_4fCfz6ZPev_0BRwH4uCcafgU-pG4WDf75EeWf863GbcrQUf5FAeSlSHC9wqPnOSHXgOIa4MWJuemRNjrR9jjb6kW-JTI1rt2bLBUAsVtz2k6aMUnp02StENSIq85XT60GVY/s1700-nu-rw-lo-l85-e365/db-2.png)

PostgreSQL rejected applying its existing LOAD restriction to the replication path.

"REPLICATION users were not previously subject to restrictions on output plugin paths, so they were able to bypass LOAD-time protections during logical decoding. Unfortunately, adding the standard LOAD restrictions now would retroactively require all third-party output plugins to be installed under the $libdir/plugins directory," Jacob Champion, who wrote the fix, said in [the commit message](https://git.postgresql.org/pg/commitdiff/226e49cbed592eaf7a08320efecb814b7492972e).

Failed loads appear in the server log as ERROR: library "..." may not be used as an output plugin, with a hint naming the setting, according to [the parameter's documentation](https://www.postgresql.org/docs/current/runtime-config-replication.html).

Administrators are advised to take the following steps -

1. Run SELECT DISTINCT plugin FROM pg\_replication\_slots WHERE plugin IS NOT NULL; before updating to identify the output plugins in use, which will only show plugins successfully used at some point.
2. Update to 18.6, 17.11, 16.15, 15.19, or 14.24, or to the equivalent distribution package.
3. Add any non-default plugin to output\_plugin\_libraries and reload the configuration with pg\_ctl reload or SELECT pg\_reload\_conf(). A restart is not required.
4. Set the new cluster's output\_plugin\_libraries before running pg\_upgrade --check when migrating from version 17 or later, as the check fails if the list does no...