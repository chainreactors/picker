---
title: PHP Warns of Critical Security Flaws Affecting All Supported Versions, Fixes Coming November 19
url: https://thehackernews.com/2026/11/php-warns-of-critical-security-flaws.html
source: The Hacker News
date: 2026-11-19
fetch_date: 2026-11-20T09:23:13.870446
---

# PHP Warns of Critical Security Flaws Affecting All Supported Versions, Fixes Coming November 19

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

# [PHP Warns of Critical Security Flaws Affecting All Supported Versions, Fixes Coming November 19](https://thehackernews.com/2026/11/php-warns-of-critical-security-flaws.html)

**Ravie Lakshmanan**Nov 19, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj86YA0ZvPrdlouN6GvSZ5P_I5HCaYLm2PBs_JA74wUDgHl8anwcqEN5_Z0kTlAggf0906enJmrtUnN_6jn9kqD8KguG8nOeh1yGS6AAPo1-JHORLQ5nZcpmS5Ss7liuqghFsq8Bb4ooabK29UcCbZlwWGM6HtyRPs4Ty5zv5d4FC5So6tVFUOaEhUylIFU/s1700-nu-rw-lo-l85-e365/php-flaws.jpg)

The maintainers of the PHP programming language on Wednesday issued an advisory announcing an upcoming security release that addresses critical flaws.

The release is scheduled for November 19, 2026, between 2 and 2:30 p.m. UTC.

"These releases are part of PHP's regular four-week release cycle and will address security vulnerabilities affecting all supported PHP versions," the maintainers [said](https://www.php.net/archive/2026.php#2026-11-18-1). "The highest severity is CRITICAL."

However, the project also noted that issues rated critical require either non-default configuration or uncommon setups. It did not disclose any additional specifics.

**UPDATE:** [phpAfterShell Details Emerge — Critical PHP Bug Could Enable RCE](https://thehackernews.com/2026/11/php-fixes-7-critical-flaws-including.html)

The update is expected to include [CVE-2026-115560](https://thehackernews.com/2026/10/urgent-php-warns-of-another-unpatched.html), a remote code execution flaw that succeeds only if the following conditions are met -

* An application sets session.serialize\_handler to php\_binary or php\_serialize in its configuration, and its code switches the handler to php with ini\_set() before calling session\_start().
* Session upload progress is enabled, which is PHP's default.

As mitigations, users were urged to set session.upload\_progress.enabled=0 until the next regular bugfix release and restart the PHP worker for the setting to be applied.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

The development comes nearly a month after PHP released fixes for two critical vulnerabilities, CVE-2026-109618 and CVE-2026-109619, collectively tracked as PHP2Shell that enable unauthenticated remote code execution (RCE) via specially crafted HTTP requests.

The [shortcomings](https://thehackernews.com/2026/10/php2shell-exploitation-hits-government.html) have since come under [limited active exploitation](https://thehackernews.com/2026/10/php2shell-exploit-attempts-hit-millions.html), targeting publicly-accessible [Palo Alto Networks management interfaces](https://thehackernews.com/2026/10/attackers-exploit-php2shell-flaws-in.html) and [Check Point Security Gateways](https://thehackernews.com/2026/11/hackers-exploit-php2shell-flaws-in.html) to launch attacks against Active Directory and deliver backdoors.

In a report published on October 30, 2026, Hunt.io said it [identified](https://hunt.io/blog/php2shell-honeypot-shells-root-palo-alto-firewalls) 616 PHP2Shell-related files, spanning shared exploit kits, cloned proof-of-concepts (PoCs), custom heap exploits, scanners, and post-exploitation tooling, across multiple hosts, even as [participants in underground forums](https://www.catonetworks.com/blog/cato-ctrl-threat-intel-php2shell-in-the-underground-and-the-search-for-a-working-exploit/) have sought exploits, discussed prerequisites, and whether [circulating PoCs](https://www.catonetworks.com/blog/cato-ctrl-threat-research-php2shell-exploitation-attempts-in-the-wild/) worked.

"Exploit developers are unlikely to create a single universal exploit that works reliably across all affected PHP deployments," CrowdStrike [said](https://www.crowdstrike.com/en-us/blog/obstacles-to-weaponizing-php2shell-likely-constrain-exploitation/).

Last month, PHP also released patches to [address](https://thehackernews.com/2026/10/adobe-commerce-polyshell-attacks-breach.html) a critical flaw in Brotli (CVE-2026-111497 aka Node2Shell or Broccoli2Shell), an out-of-bounds write vulnerability in the decoder library that could result in arbitrary code execution.

Users are advised to apply the updates as soon as they become available.

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

[Application Security](https://thehackernews.com/search/label/Application%20Security), [cyber attacks](https://thehackernews.com/search/label/cyber%20attacks), [PHP](https://thehackernews.com/search/label/PHP), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Default 'admin:admin' Server Password Helps Researchers Hack Two Automakers, Unlock and Start Cars](https://thehackernews.com/2026/11/default-adminadmin-server-password.html)

[![The Hacker News](data:image/svg+xml;base64...)

PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE](https://thehackernews.com/2026/11/postgresql-patches-52-flaws-including.html)

[![The Hacker News](data:image/svg+xml;base64......