---
title: WordPress Issues Patch for Critical Flaw That Can Enable Code Execution on Some Servers
url: https://thehackernews.com/2026/09/wordpress-issues-patch-for-critical.html
source: The Hacker News
date: 2026-09-22
fetch_date: 2026-09-23T06:54:52.486917
---

# WordPress Issues Patch for Critical Flaw That Can Enable Code Execution on Some Servers

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

# [WordPress Issues Patch for Critical Flaw That Can Enable Code Execution on Some Servers](https://thehackernews.com/2026/09/wordpress-issues-patch-for-critical.html)

**Swati Khandelwal**Sep 22, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgcFso-nJC2Re_gThOMTjPhyphenhyphenaOti1Mpn2_nb6NYGitzjVHTtvHN_q4oKg_FGa4IrTt81BAuA4qWzeJJZkxdV7F0-iSBR3ZwSUmqfBhvBX2ArxLTZqYjbtCPhu2Gw7PLSmOS5kOGQ9f0I46xPwhp5VCflFSN8YEm-z8VXdk1XRJwCvbqbljSZqorD4MpbQc/s1700-nu-rw-lo-l85-e365/wp-update.jpg)

WordPress has fixed a critical flaw in its core software that lets an attacker with no account make a site load a PHP file from outside its theme folders.

On some servers, that can go further, allowing the attacker to run their own code. The fix shipped on September 22 in WordPress 7.1.2, with fixes for every branch the project still supports, back to 4.7, and WordPress is telling site owners to [update now](https://wordpress.org/news/2026/09/wordpress-7-1-2-release/).

WordPress rates the flaw as critical, assigns it a CVSS score of 9.2, and assigns it [CVE-2026-87902](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp). Reaching it requires no account and no action from a logged-in user.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Every version from 4.7.0 through 7.1.1 is affected. That includes 7.1.1, from WordPress's [September 17 security release](https://thehackernews.com/2026/09/new-wordpress-click2shell-flaw-forces.html), so a site updated less than a week ago still needs this one. It is a separate flaw from the ones that the release fixed.

The release to update to depends on the branch you run:

| Branch you run | Update to |
| --- | --- |
| 7.1.x | 7.1.2 |
| 7.0.x | 7.0.6 |
| 6.9.x | 6.9.9 |
| 6.8.x | 6.8.10 |
| 6.7.x | 6.7.9 |
| 6.6.x | 6.6.9 |

WordPress backported the fix to every older branch it still supports as a courtesy, down to 4.7.37. The full list is in the [release notes](https://wordpress.org/documentation/wordpress-version/version-7-1-2/).

Sites with automatic background updates enabled will start the update automatically. Others can update from the dashboard under Updates, or download the release from WordPress.org. WordPress does not offer a separate workaround, so updating is the fix.

Loading a local PHP file runs whatever that file already does. Turning that into code of the attacker's choosing requires a second condition: the server must already have a PHP file that does something useful when loaded. That is the "some servers" in WordPress's description, and it is why the flaw does not mean full code execution on every affected site.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

The flaw is in how WordPress chooses the template file for a page. One of the file names it builds comes from part of the web address, and on affected versions WordPress did not run that value through its own check for ../ traversal steps, the check the neighboring code already used.

Because the name is built as page-{value}.php, a working attack also needs the active theme to have a top-level folder whose name starts with page-, and the target file has to end in .php. Some themes, including older default WordPress themes, ship a folder that fits, while the current default themes do not.

Security vendor Patchstack, in [its own analysis](https://patchstack.com/articles/wordpress-7-1-2-security-release-unauthenticated-lfi-to-rce/), says two checks tell a site owner how exposed they are: whether the active theme has a top-level folder whose name begins with page-, and whether PHP is running with a setting called register\_argc\_argv turned on, which a known code-execution technique depends on.

Neither is a fix, the company says, but both show how close a site is to the worst case. That setting is off by default on PHP 8.5 and on by default on older PHP versions.

WordPress credited **Robert Ressl** with finding the flaw, which he disclosed privately through its HackerOne program in July. Ressl published a detailed [write-up](https://ressl.ch/blog/cve-2026-87902-wordpress/) when the fix shipped, along with a proof-of-concept and a self-contained test lab. His demonstrated attack ran code with the privileges of the web-server account, not full control of the server, and he tested it against WordPress 7.0.2 in isolated local labs, not the patched release or any live site.

Ressl says operators who cannot update immediately can reduce the route to code execution by turning *register\_argc\_argv* off for web requests and removing unused PEAR components, though neither repairs the underlying flaw.

As of September 22, there were no reports of the flaw being used in attacks, and it had no entry in the U.S. CISA Known Exploited Vulnerabilities catalog.

WordPress and Ressl were contacted for comment.

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

[Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security), [WordPress](https:...