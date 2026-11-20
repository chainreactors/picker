---
title: Drupal Patches Critical Installer Flaw That Could Give Unauthenticated Attackers Control of Sites
url: https://thehackernews.com/2026/11/drupal-patches-critical-installer-flaw.html
source: The Hacker News
date: 2026-11-19
fetch_date: 2026-11-20T09:23:13.217727
---

# Drupal Patches Critical Installer Flaw That Could Give Unauthenticated Attackers Control of Sites

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

# [Drupal Patches Critical Installer Flaw That Could Give Unauthenticated Attackers Control of Sites](https://thehackernews.com/2026/11/drupal-patches-critical-installer-flaw.html)

**Swati Khandelwal**Nov 19, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4kxIzi1B-GPdS7pbaOI823BHxteL-8FbODKnAoDkr8tGhhjGYuRU9KIEAvOQ6kBZFQPCly3BIhQo6vkjxJy13zL7CxlRXsez_G_otFVaja2H5ObmzNMMilbewaweqqO5Paa0H49yaZdWB09xAIqeo7YLG0uyd05qjdbh2aLIRZd73_jwVGH26YexA3l8/s1700-nu-rw-lo-l85-e365/drupal-flaws.jpg)

Under specific conditions, a critical vulnerability in Drupal core can allow an attacker without login credentials to use the built-in installer to attempt to reinstall a site.

That can lead to a site takeover or remote code execution, and the project rates the vulnerable configurations as uncommon. Fixed releases for all supported branches shipped yesterday.

The Drupal Security Team disclosed the flaw, tracked as CVE-2026-132165, yesterday and rated it critical, 18 out of 25 on the project's risk scale.

The installer ships in every copy of Drupal core as the file /core/install.php and stays on the site after installation. Core's default .htaccess rules do not block requests to it, so blocking it is left to each site.

No attacks are reported in the [security advisory](https://www.drupal.org/sa-core-2026-017), which rates exploitation as complex and records an existing proof-of-concept exploit. Some exploit paths are blocked where the web server cannot write to or change permissions on settings.php.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

The team had told site owners in an [advance notice](https://www.drupal.org/psa-2026-11-16) earlier this week to set aside time for the update, warning that exploits may be developed within hours or days.

Every release below 10.6.22 is affected, along with Drupal 11 releases from 11.0.0 before 11.3.22 and from 11.4.0 before 11.4.13.

### What to Do Now

The fixed versions, detailed in the project's [release notes](https://www.drupal.org/project/drupal/releases/11.4.13), are:

* Drupal 11.4.x: update to 11.4.13
* Drupal 11.3.x: update to 11.3.22
* Drupal 10.6.x: update to 10.6.22

The team recommends blocking the installer even after updating. Sites that cannot update yet should follow the project's [installer guidance](https://www.drupal.org/docs/administering-a-drupal-site/security-in-drupal/securing-the-installer-installphp), updated yesterday, which describes three options: a deny rule in the web server configuration, an .htaccess rule, or removing the file and keeping it removed with Composer scripts.

Sites that use the Drupal Steward protection service are already protected from known attack vectors, according to the team, and should still update in case new vectors emerge.

Drupal 11.2.x and earlier, 10.5.x and earlier, and Drupal 8 and 9 are end-of-life and get no fix. The 11.3.x branch and Drupal 10 lose security coverage altogether in December under the project's [support schedule](https://www.drupal.org/psa-2026-11-02).

In the week of November 8, 154,485 of the 528,430 sites reporting usage data to drupal.org, about 29 percent, were running end-of-life branches.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

The flaw was found by Anthropic's OSS Scanner, an automated service the AI company launched on October 8 to look for vulnerabilities in open-source projects that opt in. Findings go to maintainers without human review, each with a reproducer and, where available, a candidate patch, according to its [launch announcement](https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source).

Drupal's security team said on November 2 that a surge of security reports, which it attributes to AI tools, is more than it can sustain at its current funding, and that it is cutting security coverage for core minor versions from 12 months to 8 starting in 2027.

This is the second critical remote code execution flaw fixed in Drupal core in two months, after the [Field UI flaw](https://thehackernews.com/2026/10/drupal-patches-critical-core-rce-flaw.html) patched on October 14, which also had at least one exploit path that needed no login.

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

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [Content Management Systems](https://thehackernews.com/search/label/Content%20Management%20Systems), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Default 'admin:admin' Server Password Helps Researchers Hack Two Automakers, Unlock and Start Cars](https://thehackernews.com/2026/11/default-adminadmin-server-password.html)

[![The Hacker News](data:image/svg+xml;base64...)

PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE](https...