---
title: WHMCS SQL Injection Could Expose Customer Data and Admin Password Hashes without Login
url: https://thehackernews.com/2026/11/whmcs-sql-injection-flaw-could-expose.html
source: The Hacker News
date: 2026-11-24
fetch_date: 2026-11-25T10:48:30.037025
---

# WHMCS SQL Injection Could Expose Customer Data and Admin Password Hashes without Login

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [WHMCS SQL Injection Could Expose Customer Data and Admin Password Hashes without Login](https://thehackernews.com/2026/11/whmcs-sql-injection-flaw-could-expose.html)

**Swati Khandelwal**Nov 24, 2026Web Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgK7wXAof6nH7PDC5-3qxXZJgJvZODTjQcrWFOjO8jeb9yGkK6bUkzm27MzMy5n0S_Xywsj0npu_F0FmQ4JcKxPXNEoezLrpKoSStaYK4Ww46QUuzySTeQnnzcIXs_NADunlqeyuMIl5Wm5PKWc3c0JyNmYPxfbInIWx2tfosieI_QS_e4PX-JILlLH-1U/s1700-nu-rw-lo-l85-e365/hosting.jpg)

A flaw in **WHMCS**'s shopping cart, the billing and automation platform many web hosting companies use to run their businesses, could allow anyone on the internet to retrieve customer records and administrator password hashes from an installation's database. No login is needed.

The company disclosed the **SQL injection** yesterday along with two other flaws that need a logged-in client, and released fixed versions. It has not reported attacks using any of the three.

Because no login is needed, the flaw, tracked as **CVE-2026-82981** (CVSS score: 8.7), is within reach of anyone who can load the shopping cart of a vulnerable installation over the internet.

The records an attacker could pull include clients' personal and support information as well as admin accounts with their hashed passwords, according to the company's advisory. A stolen hash is not a working password, but it gives attackers something to try to crack offline.

The 9.0.10 and 8.13.8 updates shipped yesterday, and the [release notes](https://docs.whmcs.com/releases/9-0/9-0-release-notes/) list them as maintenance releases. For the 9.1 series, the [security advisory](https://help.whmcs.com/m/125386/l/2151347-cve-2026-82981-whmcs-security-update-2026-11-23) names 9.1.2 as the fix, but that build had not yet appeared on the company's 9.1 release notes page at publication time.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

Fixes are available only for supported versions, so installations on the 8.0 to 8.12 series must upgrade to a fixed release.

Installing the updates falls to self-hosted administrators, since WHMCS Cloud installations are updated automatically, according to the company's [updating documentation](https://docs.whmcs.com/9-0/system/updates/updating-whmcs/).

The second SQL injection, **CVE-2026-82979** (CVSS score: 7.1), sits in the Client Area and needs a logged-in client that holds the View & Manage Contacts permission. That client could read other customers' personal, billing, and support information, as well as the same admin records and password hashes, the [second advisory](https://help.whmcs.com/m/125386/l/2151340-cve-2026-82979-whmcs-security-update-2026-11-23) says.

The third flaw, **CVE-2026-93700**, lies in how email campaigns process client-supplied data. A logged-in client could use it to read sensitive configuration files on the server, including database credentials, and to run code on the server, its advisory says.

It carries the highest score of the three, 9.0, though its [CVE record](https://www.secure.com/cve/cve-2026-93700) uses the older CVSS 3.1 scale while the other two use CVSS 4.0. That record's vector indicates that some user interaction is required, and the company has not said what else exploitation entails.

All three flaws were reported by a single researcher who uses the handle **alakazamspooon**.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

For the email-campaign flaw, updating is not the whole job. The [email-campaign advisory](https://help.whmcs.com/m/125386/l/2151351-cve-2026-93700-whmcs-security-update-2026-11-23) also tells administrators to:

1. Delete every planned or ongoing campaign under Utilities > Email Campaigns, using Delete in each campaign's Manage Campaign menu.
2. Clear the template cache under Utilities > System > System Cleanup, using Empty Template Cache.
3. Update to a fixed release.

The advisory does not explain why existing campaigns must go, leaving open the question of whether updating alone is enough.

This is at least the third round of WHMCS security fixes this year. The company patched an authorization flaw in the Client Area on May 12, described in its [May advisory](https://help.whmcs.com/m/125386/l/2073908), and an unauthenticated remote code execution flaw on September 3, described in its [September advisory](https://help.whmcs.com/m/125386/l/2118034-cve-2026-67399-whmcs-security-update-2026-09-03).

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

[data security](https://thehackernews.com/search/label/data%20security), [Patch Management](https://thehackernews.com/search/label/Patch%20Management), [SQL Injection](https://thehackernews.com/search/label/SQL%20Injection), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Hosting](https://thehackernews.com/search/label/Web%20Hosting), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

WhatsApp Patches 3 Security Flaws, Including Android Bug Suspected of Use i...