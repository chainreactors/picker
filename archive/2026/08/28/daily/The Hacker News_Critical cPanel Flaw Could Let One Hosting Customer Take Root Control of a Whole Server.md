---
title: Critical cPanel Flaw Could Let One Hosting Customer Take Root Control of a Whole Server
url: https://thehackernews.com/2026/08/critical-cpanel-flaw-could-let-one.html
source: The Hacker News
date: 2026-08-28
fetch_date: 2026-08-29T08:33:13.218659
---

# Critical cPanel Flaw Could Let One Hosting Customer Take Root Control of a Whole Server

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Critical cPanel Flaw Could Let One Hosting Customer Take Root Control of a Whole Server](https://thehackernews.com/2026/08/critical-cpanel-flaw-could-let-one.html)

**Swati Khandelwal**Aug 28, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtKp2lGcxPfp8ymA88FIBXB0Bn9fcUSaU_UIl1pfAjDSC2usRwUE73vhQEeP6jar9U9k10yotgyYl_tIk6dQA-MFIr2bJ3LN_azGt9kDU6hpW448HgmBuJbc6TWSo1vfpmhoK0J3_5rhF6VIpWd7NYf0G1YSYHdqKubWgQwa1yU6KRAL-bnDGd8HmCmPk/s1700-e365/cpanel-root.jpg)

cPanel has released patches for a security flaw affecting domain parking and addon domain functionality in cPanel and WebHost Manager (WHM), which could allow code execution as the root user.

The vulnerability, assigned the CVE identifier **CVE-2026-65643**, impacts all supported versions of cPanel & WHM.

cPanel described the issue as a critical security vulnerability and said that an authenticated account holder who can add parked or addon domains can create arbitrary files on the server.

"Successful exploitation leads to code execution as the root user, giving an attacker full control of the server," cPanel said in a notification to customers.

cPanel has released the following patched versions -

* 11.110.0.141 or later
* 11.134.0.53 or later
* 11.136.0.37 or later
* 11.138.0.2 or later
* 11.138.1.7 or later (WP Squared)

The notification names WP Squared in its patched list and does not mention DNSOnly.

cPanel patched [three separate flaws in July](https://thehackernews.com/2026/08/new-cpanel-critical-flaw-could-let.html), and the fixed builds named in those advisories included the 11.118 and 11.126 branches. The August 27 list covers the 110, 134, 136, and 138 branches, and the company has not said whether 11.118 and 11.126 remain supported.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

cPanel said in its July [advisory about the Exim flaw](https://support.cpanel.net/hc/en-us/articles/42285884685207-Security-GCVE-25-2026-07-45-3-Exim-forward-Privilege-Escalation) that it may allow privilege escalation from Team User sub-accounts. The August 27 notification does not specify whether a Team User sub-account with permission to the parked and addon domains is in scope.

Servers configured for automatic daily updates receive the patched build automatically, according to the [advisory published on August 27](https://support.cpanel.net/hc/en-us/articles/42959571221527-Security-CVE-2026-65643-Vulnerability-in-cPanel-s-Domain-Parking-Functionality-August-27-2026).

Administrators can apply it immediately by logging in to the server as root and running /scripts/upcp --force. The update can also be installed from WHM under Home > cPanel > Upgrade to Latest Version, and the installed build can then be verified under Server Configuration > Update Preferences.

Servers running an end-of-life version have to upgrade to a supported version to receive the fix.

The customer notification carries no CVSS score, and The Hacker News confirmed via the CVE Program's record store on August 28, 2026, that no record has been published for CVE-2026-65643. Records for CVE-2026-58048 and CVE-2026-58047, two cPanel flaws disclosed on July 31, were both present at the time of the check.

cPanel has not said whether the flaw has been exploited, and it is absent from the U.S. Cybersecurity and Infrastructure Security Agency's (CISA) Known Exploited Vulnerabilities (KEV) catalog as of the version released on August 27, 2026. The catalog already carries two flaws in a cPanel plugin.

CISA added CVE-2026-48172, a privilege escalation issue in the LiteSpeed cPanel plugin, on May 26, 2026, and noted that it can be exploited by any cPanel user account to execute arbitrary scripts with root privileges.

It added CVE-2026-54420, a symlink-following flaw in the same plugin, on June 15, 2026, for shared hosting servers running CloudLinux or CageFS where a user has FTP or web shell access.

The catalog also lists CVE-2026-41940, the [authentication bypass patched in April](https://thehackernews.com/2026/04/critical-cpanel-authentication.html), with known use in ransomware campaigns.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The customer notification provides no interim mitigation and no way to verify whether a server has already been compromised.

cPanel carried a command to grep the Apache error log for signs of exploitation in [its Phusion Passenger advisory](https://support.cpanel.net/hc/en-us/articles/42694659893143-Security-Privilege-Escalation-via-Phusion-Passenger-s-Watchdog-API), published on August 14, 2026.

cPanel said that the issue does not affect default installations and applies only to servers where an affected Passenger package has been installed.

Plesk, which WebPros develops alongside cPanel, updated its own [advisory for the same flaw](https://support.plesk.com/hc/en-us/articles/42694125241751-Vulnerability-Privilege-Escalation-via-Phusion-Passenger-s-Watchdog-API) on August 14, 2026, with a five-item checklist for spotting a prior compromise that begins with unexpected entries in /etc/ld.so.preload.

"Patching closes the vulnerability going forward, but it does not undo anything an attacker may have already done," Plesk said.

Phusion, which develops Passenger, shipped a fix in [Passenger 6.2.0](https://blog.phusion.nl/passenger-6-2-0/)  on August 18, 2026, for a Watchdog API flaw that does not have a CVE identifier.

"We have seen exploitation of this vulnerability in the wild at a shared hosting provider," Phusion said.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
*...