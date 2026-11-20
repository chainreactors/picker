---
title: phpAfterShell Explained: How Hackers Could Turn a PHP Session Flaw Into Code Execution
url: https://thehackernews.com/2026/11/phpaftershell-explained-how-hackers.html
source: The Hacker News
date: 2026-11-19
fetch_date: 2026-11-20T09:23:12.801849
---

# phpAfterShell Explained: How Hackers Could Turn a PHP Session Flaw Into Code Execution

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

# [phpAfterShell Explained: How Hackers Could Turn a PHP Session Flaw Into Code Execution](https://thehackernews.com/2026/11/phpaftershell-explained-how-hackers.html)

**Swati Khandelwal**Nov 19, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiEEFyvreIQgAheXoKRJxLcNgyzFh0rlydmiMfaOBIlmM7zGPc_71mCSG6zWGlpFcRQg59gVUw6NbpmFiNKIcDB3AqVA5eKpjYExWhMu-uBD_W5xu1wiYRtX5MklAgxeuHOBJOI8H9LmaIoXv7IrvFMVHvVhor06lj_ljcIDjIDAPYJ8w01X-BTA51EpOU/s1700-nu-rw-lo-l85-e365/php-after-shell.jpg)

PHP's default file-based session storage can be made to return objects an attacker chose, by cutting off a session write at the right moment. When combined with a second weakness, such as a suitable gadget chain in the app, those objects can allow the attacker to run code on the server.

Today's PHP releases fix the flaw, called **[phpAfterShell](https://thehackernews.com/2026/11/php-fixes-7-critical-flaws-including.html)**.

The flaw is tracked as **CVE-2026-126714** and rated 9.2 out of 10 on the CVSS 4.0 scale by PHP's maintainers. Depthfirst, a security company, says it found the flaw and reported it to the maintainers.

The October 21 PHP releases, which fixed two critical flaws known as [PHP2Shell](https://thehackernews.com/2026/10/php-issues-emergency-patches-for-two.html), do not contain this fix. Servers updated then remain affected until they install today's releases. Neither the maintainers nor the company reports any attacks using phpAfterShell.

### Who Is Affected and What to Do

These releases are affected, according to the maintainers' [security advisory](https://github.com/php/php-src/security/advisories/GHSA-fm2m-fjf5-v3cp):

| Branch | Affected releases | Fixed release |
| --- | --- | --- |
| PHP 8.2 | Before 8.2.36 | 8.2.36 |
| PHP 8.3 | Before 8.3.37 | 8.3.37 |
| PHP 8.4 | Before 8.4.28 | 8.4.28 |
| PHP 8.5 | Before 8.5.13 | 8.5.13 |

PHP 8.6.0, also released today, includes the fix.

The flaw is in the files session handler, which PHP uses by default. Sessions kept in Redis, a database, or another store are outside this defect, though each store's handling of a cut-off update needs its own check.

Whether an attacker needs to log in depends on how the app exposes its session handling.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

On the path the company tested, the attacker uses upload progress, a PHP feature that records the progress of a file upload in the user's session. Where the feature is on, a multipart form upload that carries its field makes PHP write to the session before the app's own code runs. The app does not need an upload page, only any page that opens the session later.

PHP 8.1 and older are end-of-life. The official end-of-life mitigation branches for 7.4, 8.0, and 8.1 are not affected, but older unpatched builds of those versions are, according to the company.

The company's [remediation guidance](https://depthfirst.com/phpaftershell) sets out these steps:

1. Install the fixed release for your branch, as listed above. If you run PHP 8.1 or older, move to a supported branch.
2. Rebuild any container images and redeploy.
3. Check that the PHP version serving web requests is the new one.

If you cannot update yet and your app does not use upload progress, set **session.upload\_progress.enabled = 0** in **php.ini** or the server's PHP settings, then restart the PHP workers. Also limit the untrusted data your app stores in sessions.

Switching the feature off is not a full fix. It closes the upload path, but apps that put attacker-controlled data into sessions in other ways remain affected, the maintainers say.

The maintainers listed the same setting on October 21 as a temporary measure for one of the PHP2Shell flaws. Servers that have kept it off since then still need the update.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgLoqqEe0XW2nWCPLMM5qy5ng0qt6xWov0xxceCfMNzji1DLUEs6eK4emFE5HXp0HTfS2NxSqeUAja5Sb-1OtBTEcTmnDOiQrb8hkoXqR5vMftJ9nDvcFbQlK7rGGqcmMpYAhf2wqWByFnB4h-fkaGKwYJvR_vAuGxV6-5fZJDl4v_6IcI8APkFF7fen90/s1700-nu-rw-lo-l85-e365/phpaftershell.gif)

Moving sessions to a store that replaces records in one step also avoids this defect. The update is still the recommended fix for sites that keep the files handler.

Linux distribution packages may include the fix without changing the PHP version number, according to the company, so the version number alone may not indicate whether a server is fixed.

Once installed, the fixed releases empty the session file before each write and stop the write if that step fails. A cut-off write can still lose session data, but it can no longer leave old data behind for an attacker to use.

The updates also switch upload progress off by default. The Hacker News compared PHP's source code for the October 21 releases and today's. The built-in setting is on in 8.2.35, 8.3.36, 8.4.27 and 8.5.12, and off in 8.2.36, 8.3.37, 8.4.28, 8.5.13 and 8.6.0.

The [release notes](https://www.php.net/ChangeLog-8.php) do not mention or explain the change. The sample php.ini files still show the old setting in a commented-out line. A php.ini file, distribution package, or hosting panel that switches the setting on will keep it on.

Where nothing else sets it, apps that rely on upload progress will need it switched back on after the update.

The same releases also fix [other PHP security flaws](https://thehackernews.com/2026/11/php-fixes-7-critical-flaws-including.html).

### How the Attack Works

The attack starts with the session write that upload progress makes before the app's code runs, Depthfirst's researchers say in their [technical analysis](https://depthfirst.com/research/phpaftershell).

A PHP session file stores each value as a name followed by serialized data. Length fields in that data tell PHP where each string ends, and nothing in the file marks a write as finished.

[![](data:image/png;base64...