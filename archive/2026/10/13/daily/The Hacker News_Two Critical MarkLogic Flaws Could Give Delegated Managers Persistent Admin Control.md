---
title: Two Critical MarkLogic Flaws Could Give Delegated Managers Persistent Admin Control
url: https://thehackernews.com/2026/10/two-critical-marklogic-flaws-could-give.html
source: The Hacker News
date: 2026-10-13
fetch_date: 2026-10-14T06:53:25.413283
---

# Two Critical MarkLogic Flaws Could Give Delegated Managers Persistent Admin Control

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Two Critical MarkLogic Flaws Could Give Delegated Managers Persistent Admin Control](https://thehackernews.com/2026/10/two-critical-marklogic-flaws-could-give.html)

**Swati Khandelwal**Oct 13, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvGRzVYOU1S12WE6ja5ZSrhInOGaNdwCGGwWch1oJn_SDtoy90ycGVjd-JeDjwSSH8XDzKlkoKsu_vlND1iW0aWJgEqf3Ti18goDI0yXeaLbF2DHrokj8Qdvm1kHEi8wqdm6_axRi17PVBqtlgFWLpZnv6Eufx_bFMkpWcnz6ymbQI4IDB7lgYi3QrZ7w/s1700-nu-rw-lo-l85-e365/amrk.jpg)

Two of 31 newly disclosed flaws in Progress Software's [MarkLogic Server](https://www.progress.com/marklogic/server) database could let an account given only some management privileges take administrator control of the server, the company says.

Progress published all 31 on October 12 and scored five of them critical. Fixes have been available since September 10, in [MarkLogic 11.3.7](https://docs.progress.com/bundle/marklogic-server-whats-new-11/page/topics/release-notes.html) and [MarkLogic 12.1.0](https://docs.progress.com/bundle/marklogic-server-whats-new-12/page/topics/release-notes.html).

Affected releases, and the release that fixes each:

* MarkLogic 11.x before 11.3.7: upgrade to 11.3.7
* MarkLogic 12.x before 12.1.0: upgrade to 12.1.0

MarkLogic 11.3 is the long-term support (LTS) line. The 12 line, which Progress calls an innovation release, has no patched 12.0 release. Its fix is 12.1.0, which also adds new features.

Installing the fixes for the 10 MarkLogic flaws Progress disclosed in August is not enough. Those fixes arrived in 11.3.6 and 12.0.3, and both releases are affected by the new flaws.

Progress's CVE records and its upgrade notes for the two releases do not say whether any of the 31 flaws has been used in attacks. None was in the U.S. Cybersecurity and Infrastructure Security Agency's [Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) when The Hacker News checked on October 13.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The same records and notes list no workaround for customers who cannot upgrade yet.

### What the Critical Flaws Allow

Progress scored three of the five critical flaws 9.9 out of 10 on the CVSS scale and the other two 9.6. For each one, the attacker must already have a privilege or a way to run code on the server, according to the company's CVE records.

Two of them involve forests. In MarkLogic, a [forest](https://docs.progress.com/bundle/marklogic-server-administrate-12/page/topics/forests/understanding-forests.html) is a collection of documents that is attached to a database.

| CVE | Score | What the Attacker Needs | What It Could Allow |
| --- | --- | --- | --- |
| [CVE-2026-85947](https://www.cve.org/CVERecord?id=CVE-2026-85947) | 9.9 | Forest-management privileges | Create a persistent administrator account, potentially giving complete administrative control of the server |
| [CVE-2026-85948](https://www.cve.org/CVERecord?id=CVE-2026-85948) | 9.9 | Manage-user-level privileges | Gain persistent administrative control, through an XQuery injection flaw in a deprecated Management API path |
| [CVE-2026-85955](https://www.cve.org/CVERecord?id=CVE-2026-85955) | 9.9 | Query-execution access and the `xdmp-eval-in` privilege | Run server-side code with elevated permissions |
| [CVE-2026-85956](https://www.cve.org/CVERecord?id=CVE-2026-85956) | 9.6 | Delegated database-administrator privileges | Back up or restore forests outside its own database, allowing access to or changes to what Progress calls "security-critical data" |
| [CVE-2026-9191](https://www.cve.org/CVERecord?id=CVE-2026-9191) | 9.6 | The ability to run code through certain REST and XDBC evaluation paths | Perform unauthorized actions or compromise an authenticated session |

The fix for CVE-2026-85947 shows which accounts are at issue. A "forest-scoped administrative grant" is no longer enough on its own to attach a forest to a database of the account's choosing, the upgrade notes say. They also tell customers to review delegated forest and database privilege assignments before upgrading, and to audit the roles that hold xdmp-eval-in.

Outside researchers reported four of the five through Bugcrowd. A researcher using the handle rexnets is credited with CVE-2026-85947, CVE-2026-85948, and CVE-2026-85956, and another using the handle WaltWhitehat is credited with CVE-2026-9191.

### Flaws That Depend on Configuration

Progress scored 24 of the remaining flaws high and two medium. The highest, CVE-2026-85954, at 8.6, could allow an attacker to gain more privileges than granted by passing values to certain XQuery functions.

Several of the others apply only where a named feature or platform is in use:

* **SAML:** In deployments that use SAML authentication, an unauthenticated remote attacker could make the server accept an assertion it should reject (CVE-2026-85962). On 11.x, the SAML parser could also process external DTDs or entities (CVE-2026-85957).
* **OAuth:** An attacker could use a token that the server should not accept (CVE-2026-85958). The fix adds issuer and audience checks for Ping Identity and other OAuth configurations.
* **Password-based Kerberos:** In certain configurations, an attacker positioned on the network could impersonate the Kerberos authentication service (CVE-2026-85972).
* **Cloud hosting:** An authenticated attacker could access internal cloud services and obtain cloud credentials on Azure (CVE-2026-85951) and on Linux-based cloud deployments (CVE-2026-85952).
* **Diagnostic logs:** Under certain configurations, the server could write security-sensitive information to diagnostic logs (CVE-2026-85949 and, on Azure, CVE-2026-85961). AWS secret keys and session tokens were written in plaintext when the affected IAM trace path was enabled, the upgrade notes say.
* **Amazon S3:** Connections to S3...