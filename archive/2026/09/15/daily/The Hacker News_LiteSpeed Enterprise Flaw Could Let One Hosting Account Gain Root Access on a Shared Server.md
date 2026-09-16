---
title: LiteSpeed Enterprise Flaw Could Let One Hosting Account Gain Root Access on a Shared Server
url: https://thehackernews.com/2026/09/litespeed-enterprise-flaw-could-let-one.html
source: The Hacker News
date: 2026-09-15
fetch_date: 2026-09-16T07:06:15.083847
---

# LiteSpeed Enterprise Flaw Could Let One Hosting Account Gain Root Access on a Shared Server

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

# [LiteSpeed Enterprise Flaw Could Let One Hosting Account Gain Root Access on a Shared Server](https://thehackernews.com/2026/09/litespeed-enterprise-flaw-could-let-one.html)

**Swati Khandelwal**Sep 15, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjRVzSne-2lfRX57xj9CbnkpX1fjEWXYoPN0tDsXwgBwaE_LVqYBKtWbO1nudNLKp89aR90EeszJUqsNvZN4ZLzU1i7hm89ihV-lK1mIKiNXl6GWAWkn6uz7WlRVfIdJrS7Nfn6x-1Cclf6oTs3RxVNWxQSVBsvhzDjMBnmU3l3oERVu3b5hqag5mSeKoU/s1700-nu-rw-lo-l85-e365/litespeed.jpg)

A critical vulnerability in **LiteSpeed Web Server Enterprise** could let a low-privilege website user gain root access on a shared-hosting server, cPanel warned in an [advisory published on September 14](https://support.cpanel.net/hc/en-us/articles/43483286674583-Security-LiteSpeed-Enterprise-security-advisory-September-14-2026).

On such servers, many customers' sites run on a single machine, and an attacker with one of those hosting accounts could exploit the flaw to access or alter other sites and the server itself, according to the advisory.

cPanel said it had received notice of the flaw, which affects versions before 6.3.7, and urged administrators to update to that release, which LiteSpeed [published on September 11](https://store.litespeedtech.com/store/index.php?rp=/announcements/895/LiteSpeed-Web-Server-v6.3.7-Now-Available.html).

The flaw can bypass the controls that keep hosting accounts apart, including [CageFS](https://docs.cloudlinux.com/cloudlinuxos/cloudlinux_os_components/#cagefs), cPanel said. CageFS is a CloudLinux tool that gives each hosting account a restricted view of the file system, so it cannot see other accounts or the server's configuration files.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Neither cPanel's advisory nor LiteSpeed's release notes describe how the flaw works. LiteSpeed's announcement of 6.3.7 called it a release with "Security improvements, bug fixes, and more!" Its [changelog](https://docs.litespeedtech.com/lsws/changelog/) lists three security changes but does not mention a privilege-escalation flaw, and neither company has said publicly which change fixes it.

The advisory carries no CVE identifier or severity score, and a check of published CVE records on September 15 found none for the flaw. The advisory also does not say whether the flaw has been exploited.

Both cPanel and LiteSpeed give the same command to install 6.3.7 now: /usr/local/lsws/admin/misc/lsup.sh -f -v 6.3.7

The manual update matters because 6.3.7 may not arrive on its own: LiteSpeed said there "may be some delay" before the release reaches auto-update.

As of September 15, LiteSpeed's [download page](https://www.litespeedtech.com/products/litespeed-web-server/download) still listed 6.3.6 as the stable release, alongside a July pre-release build of 6.4.0 (RC1) whose changelog does not list the three security changes. cPanel's advisory does not say whether the 6.4.0 release candidates are affected.

LiteSpeed's [update documentation](https://docs.litespeedtech.com/lsws/updates/) says that forcing a specific version with this command stops the server from following its stable update tier, and that administrators can resume automatic stable updates afterward by running touch /usr/local/lsws/autoupdate/follow\_stable.

Neither cPanel's advisory nor LiteSpeed's release notes offer a workaround for servers that cannot update at once, or indicators for checking whether a server has already been attacked. The advisory names only the Enterprise edition and does not address OpenLiteSpeed, LiteSpeed's open-source server, for which LiteSpeed had released no matching update as of September 15.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

It is the third time since May that a flaw in LiteSpeed software on cPanel servers has been reported to grant a hosting account root access, but the first in the web server itself.

In May and June, LiteSpeed disclosed two such flaws in its user-end cPanel plugin, [CVE-2026-48172](https://blog.litespeedtech.com/2026/05/21/security-update-for-litespeed-cpanel-plugin/) and [CVE-2026-54420](https://blog.litespeedtech.com/2026/06/01/security-update-for-litespeed-cpanel-plugin-2/), said both were being actively exploited, and fixed both in the plugin. CISA later added both to its Known Exploited Vulnerabilities catalog, as The Hacker News reported in [May](https://thehackernews.com/2026/05/litespeed-cpanel-plugin-cve-2026-48172.html) and [June](https://thehackernews.com/2026/06/cisa-flags-litespeed-cpanel-plugin-flaw.html).

The Hacker News has contacted LiteSpeed, cPanel, and CloudLinux with questions about the flaw.

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

[privilege escalation](https://thehackernews.com/search/label/privilege%20escalation), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

OpenAI Agents Linked to RubyGems Campaign Th...