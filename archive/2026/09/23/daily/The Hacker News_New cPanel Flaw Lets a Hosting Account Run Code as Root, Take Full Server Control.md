---
title: New cPanel Flaw Lets a Hosting Account Run Code as Root, Take Full Server Control
url: https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account_0272795595.html
source: The Hacker News
date: 2026-09-23
fetch_date: 2026-09-24T07:08:24.332005
---

# New cPanel Flaw Lets a Hosting Account Run Code as Root, Take Full Server Control

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

# [New cPanel Flaw Lets a Hosting Account Run Code as Root, Take Full Server Control](https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account_0272795595.html)

**Swati Khandelwal**Sep 23, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhT5quc0dmRWhh6WOC80Gx9QoHTMYyq5srnXBXjybOKZk_qoUn1Q2nKLE9MifqCEyRIha_NFvRsyr8Nx5EyxGIREXaTb5Fh59cz4Ln8yZj9Zv7piqM49wmm7rfmchW1cVlss1wn47qNypaYarZUVNHBO8rzXaYTvRMi9u1phgfXVd8OZx8_Vjxm34684BE/s1700-nu-rw-lo-l85-e365/cpanel-0day.jpg)

A flaw in cPanel's [CalDAV and CardDAV service](https://support.cpanel.net/hc/en-us/articles/43591715125271-Security-CVE-2026-87899-Vulnerability-in-cPanel-s-CalDAV-CardDAV-September-22-2026) lets anyone with a cPanel hosting account run code as root and take "full control of the server," the company said on September 22.

A [second bug](https://support.cpanel.net/hc/en-us/articles/43597969409943-Security-CVE-2026-87900-Vulnerability-in-WP-Toolkit-Database-Creation-September-22-2026) in the WP Toolkit plugin, used to install and manage WordPress sites, allows an account holder to change databases that belong to other accounts.

cPanel has released fixed versions for both, along with a fix for a [third flaw](https://support.cpanel.net/hc/en-us/articles/43502940099991-Security-CVE-2026-68490-Vulnerability-in-cPanel-s-CalDAV-CardDAV-Functionality-September-22-2026) in the same service, which stores each account's calendars and contacts. That third flaw lets a local user on the server read other accounts' calendar events and contacts, but not change them or gain root access.

cPanel lists no requirements for the root flaw other than having an account. On a shared server where a hosting provider sells accounts to the public, that means any customer could use it. So could anyone who gets hold of a customer's login.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The three flaws and the versions that fix them:

| Flaw | Where | What it allows, according to cPanel | Affected | Fixed in |
| --- | --- | --- | --- | --- |
| CVE-2026-87899 | CalDAV and CardDAV | A logged-in account holder can run code as root | cPanel & WHM version 120 and later | 11.134.0.57 or later   11.136.0.41 or later   11.138.0.8 or later   WP Squared 11.138.1.11 or later |
| CVE-2026-87900 | WP Toolkit | A logged-in cPanel user can change databases in other accounts | WP Toolkit 6.11.2-10794 and older | WP Toolkit 6.11.3 or later |
| CVE-2026-68490 | CalDAV and CardDAV | A local user can read other accounts' calendar events and contacts | cPanel & WHM version 120 and later | 11.134.0.57 or later   11.136.0.41 or later   11.138.0.8 or later   WP Squared 11.138.1.11 or later |

The WP Toolkit bug is in how the plugin handles commands that create databases. cPanel says only that a logged-in cPanel user could "perform database modifications in other accounts."

It does not say what changes are possible, whether data from other accounts can also be read, or whether the user needs access to WP Toolkit itself.

WP Toolkit is also available for Plesk, another hosting control panel from the same company, WebPros. cPanel has not said whether the Plesk version is affected.

None of the three advisories mentions exploitation or gives a way to check whether a server was attacked before it was updated. The flaws were not in CISA's Known Exploited Vulnerabilities catalog when The Hacker News checked on September 23.

cPanel credits all three flaws to Ali Mustafa, a researcher who goes by rz1027. Vendor advisories and CVE records credit him with at least seven cPanel and Plesk flaws disclosed since August 27, three of them shared with a researcher known as abed1526.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

They include a September 8 flaw in cPanel's [EmailTrack feature](https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account.html) that let an account with mail privileges run code as root, cPanel said at the time.

Plesk fixed two more on September 10, in how its Backup Manager [restores files](https://support.plesk.com/hc/en-us/articles/43248932867351-Vulnerability-in-Plesk-s-Backup-Manager-symlink-race-during-restore-allows-root-privilege-escalation) and how it [handles backup headers](https://support.plesk.com/hc/en-us/articles/43248841638551-Vulnerability-in-Plesk-s-Backup-Manager-unsigned-backup-header-allows-path-traversal). It said each could let a customer take over the whole server.

### How to Update

cPanel gives separate update instructions for cPanel & WHM and for WP Toolkit. WP Toolkit is installed as [its own package](https://support.cpanel.net/hc/en-us/articles/1500000253161-Updating-WP-Toolkit), wp-toolkit-cpanel, with its own update.

* **cPanel & WHM** (CVE-2026-87899 and CVE-2026-68490): follow [cPanel's update steps](https://support.cpanel.net/hc/en-us/articles/1500004959421-How-do-I-update-cPanel-WHM). In WHM, go to Home / cPanel / Upgrade to Latest Version, or run /usr/local/cpanel/scripts/upcp --force as root. The update also repairs calendar and contact permissions for existing accounts.
* **WP Toolkit** (CVE-2026-87900): update to version 6.11.3 or later with this command: bash <(curl https://wp-toolkit.plesk.com/cPanel/installer.sh || wget -O - https://wp-toolkit.plesk.com/cPanel/installer.sh) --version 6.11.3

The calendar flaws affect version 120 and later, but cPanel lists fixed builds only for the 134, 136, and 138 release lines and for WP Squared.

cPanel offers no temporary workaround for servers that cannot be updated yet. For WP Toolkit, only the manual command is given, and whether automatic updates will install 6.11.3 is not stated.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews)...