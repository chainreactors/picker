---
title: PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE
url: https://thehackernews.com/2026/11/postgresql-patches-52-flaws-including.html
source: The Hacker News
date: 2026-11-13
fetch_date: 2026-11-14T08:21:56.118491
---

# PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE](https://thehackernews.com/2026/11/postgresql-patches-52-flaws-including.html)

**Swati Khandelwal**Nov 13, 2026Vulnerability / Database Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhj8XOS7IKEt2ZhrwwdlDSpQ5hAyI46wHZpPkTQ3_hA6yUtMQpzaM50fm2v9x0O7NCt5z9vdrTsYM3iPOmu9fmmMTQDViu-rQjCfSxfCQhwZQazr4ZYayvEn5MQfUdTBVODtAay6RIaTqJGUj-HVzbtMqNPdNFiQHExhO9sitJX0GrvTx_EhWmslA-87ds/s1700-nu-rw-lo-l85-e365/postgresql.jpg)

A type confusion flaw in **PostgreSQL** lets a database user who can create objects run code on the server. Updates released yesterday fix it, along with 51 other security flaws. Full protection from this flaw also requires rebuilding any C-language extensions installed on the server.

The flaw, tracked as **CVE-2026-6460**, has a CVSS score of 8.8. Any code run this way has the rights of the operating system user that runs PostgreSQL. All versions before 18.7, 17.12, 16.16, 15.20, and 14.25 are affected.

The PostgreSQL Global Development Group, which publishes the database's releases, has not reported any attacks using the flaw. CISA's assessment in the CVE record also lists exploitation as none.

The flaw involves composite types, which are types built from named fields, each with its own data type. A field's type can be changed while older values of that type are still held in other parts of the server.

The server could then read an old value as if it had the new type. The fix, described in the project's [release notes](https://www.postgresql.org/docs/18/release-18-7.html), adds version checks so the server can detect a value that no longer matches its type.

Security researcher **Mehmet Ince** described a working exploit for the flaw, demonstrated on PostgreSQL 18.6, in a [technical writeup](https://mehmetince.net/part-3-6-how-i-ended-up-turning-a-22-year-old-postgresql-type-confusion-primitive-into-rce-cve-2026-6460/) published this week.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

His method is to prepare a query that holds a value, change the type of one of the value's fields, and then run the query. The writeup includes the SQL that crashes an unpatched server this way and a second step that leaks memory addresses. It does not include the SQL for the final step, which makes the server run a command.

He wrote that he could "trigger this crash as a lowest-privileged login role." The project's [security advisory](https://www.postgresql.org/support/security/CVE-2026-6460/) describes the attacker only as someone who can create objects, without saying which privileges that takes.

Red Hat, which ships PostgreSQL packages, says in its [CVE assessment](https://access.redhat.com/security/cve/cve-2026-6460) that an attacker needs a database login with the ability to create or modify objects. None of these sources says whether an account with only default privileges can go beyond the crash to run code.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-cI43j9xIo0t_DXuSQgASX5u0DldrswshP5xjfi-EiVQqAW_msXNeL23Po3dFsXY5xlUJ-PH6KTzFT93_NAXfXZFbuiMY8q-uQGj3lh_AsDWq5LAyGGHhpQQ-U89SZPqtgnIqRfMxkSbts2Fj3c4sCrZfaDjr8BuJnzV-bIYKVf95SO6_c1ezpmQfgk4/s1700-nu-rw-lo-l85-e365/poc.jpg)

Ince traces the root of the flaw to May 5, 2004, when PostgreSQL gained the ability to change a column's type. His technique for running code relies on a later change made on May 14, 2015.

He also adapted the exploit for managed PostgreSQL services and privately shared proofs of concept with their security teams in August. The providers he worked with include AWS (Aurora and RDS), Microsoft (Azure PostgreSQL), Google (AlloyDB), Supabase, Databricks, and Ubicloud. The writeup does not give each service's current patch status.

The project credits more than a dozen reporters for **CVE-2026-6460**, including the researcher, and credits him on five other flaws in the same release.

The project rates 32 of the 52 flaws at 8.8, the highest score in the release. Based on the scores in its [vulnerability index](https://www.postgresql.org/support/security/), only one flaw in the server requires neither a login nor any user action. That flaw, **CVE-2026-116322**, lets an unauthenticated client trigger a restart of PostgreSQL 18 servers.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

Several other fixes are in client tools. A crafted archive can make pg\_restore run code as the user running it. A compromised source server can make psql run code through the restore script in pg\_dump's tar output.

### What Administrators Should Do

1. Update the server to 18.7, 17.12, 16.16, 15.20, or 14.25, matching your major version.
2. Rebuild or update every C-language extension at the same time as the server. Extensions built against older releases still load, but they "may not be protected from the vulnerabilities fixed in this release," according to a [repository notice](https://yum.postgresql.org/news/extensions-require-minor-release/) from the project's RPM package maintainers. Some extensions will also need source-code changes.
3. Extensions rebuilt for the new releases can fail to load on older servers. Extension packages in the project's RPM repositories now require the new minor release.
4. If PostgreSQL runs outside its package's own service unit, for example under Patroni, restart it right after updating, a maintainer of the RPM packages says in a [packaging blog post](https://people.planetpostgresql.org/devrim/index.php?/archives/138-PostgreSQL-November-2026-minor-releases-update-the-server-and-extensions-together.html).
5. Update client tools such as pg\_dump, pg\_restore, reindexdb and vacuumdb on every machine that runs them.
6. Do not use the new composite\_type\_mismatch setting to turn off the checks. The project says doing so carries security risks.
7. The pro...