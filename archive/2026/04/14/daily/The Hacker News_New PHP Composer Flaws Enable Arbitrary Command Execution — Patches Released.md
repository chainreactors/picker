---
title: New PHP Composer Flaws Enable Arbitrary Command Execution — Patches Released
url: https://thehackernews.com/2026/04/new-php-composer-flaws-enable-arbitrary.html
source: The Hacker News
date: 2026-04-14
fetch_date: 2026-04-15T04:44:11.990115
---

# New PHP Composer Flaws Enable Arbitrary Command Execution — Patches Released

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

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

# [New PHP Composer Flaws Enable Arbitrary Command Execution — Patches Released](https://thehackernews.com/2026/04/new-php-composer-flaws-enable-arbitrary.html)

**Ravie Lakshmanan**Apr 14, 2026Vulnerability / DevSecOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgP-RqcuX8QuBEwVkchLNSjyIAqQEuFwy0prqQ1gGqxpBFESQLuCzgGB7-cjYhJrbLhbTk_j8G4NedN06plhhqLd_Rpd01mTh8XcOHjvQ_UuJqfjTROZeh40WlSN_7gzRL4yVKX-Aj0ui2gOxo9l70b3Dy5R6srKjne-gQXIhL7fNAHYZ7rDm6-yWl4-_JD/s1700-e365/php-code.jpg)

Two high-severity security vulnerabilities have been [disclosed](https://blog.packagist.com/composer-2-9-6-perforce-driver-command-injection-vulnerabilities/) in Composer, a package manager for PHP, that, if successfully exploited, could result in arbitrary command execution.

The vulnerabilities have been described as command injection flaws affecting the Perforce VCS (version control software) driver. Details of the two flaws are below -

* **[CVE-2026-40176](https://github.com/composer/composer/security/advisories/GHSA-wg36-wvj6-r67p)** (CVSS score: 7.8) - An improper input validation vulnerability that could allow an attacker controlling a repository configuration in a malicious composer.json declaring a Perforce VCS repository to inject arbitrary commands, resulting in command execution in the context of the user running Composer.
* **[CVE-2026-40261](https://github.com/composer/composer/security/advisories/GHSA-gqw4-4w2p-838q)** (CVSS score: 8.8) - An improper input validation vulnerability stemming from inadequate [escaping](https://en.wikipedia.org/wiki/Escape_sequence) that could allow an attacker to inject arbitrary commands through a crafted source reference containing shell metacharacters.

In both cases, Composer would execute these injected commands even if Perforce VCS is not installed, the maintainers noted in an advisory.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

The vulnerabilities affect the following versions -

* >= 2.3, < 2.9.6 (Fixed in version 2.9.6)
* >= 2.0, < 2.2.27 (Fixed in version 2.2.27)

If immediate patching is not an option, it's advised to inspect composer.json files before running Composer and verify that Perforce-related fields contain valid values. It's also recommended to only use trusted Composer repositories, run Composer commands on projects from trusted sources, and avoid installing dependencies using the "--prefer-dist" or the "preferred-install: dist" configuration setting.

Composer said it scanned Packagist.org and did not find any evidence of the aforementioned vulnerabilities being exploited by threat actors by publishing packages with malicious Perforce information. A new release is expected to be shipped for Private Packagist Self-Hosted customers.

"As a precaution, publication of Perforce source metadata has been disabled on Packagist.org since Friday, April 10th, 2026," it said. "Composer installations should be updated immediately regardless."

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

[Command Injection](https://thehackernews.com/search/label/Command%20Injection), [Composer](https://thehackernews.com/search/label/Composer), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [DevSecOps](https://thehackernews.com/search/label/DevSecOps), [Open Source](https://thehackernews.com/search/label/Open%20Source), [Perforce](https://thehackernews.com/search/label/Perforce), [PHP](https://thehackernews.com/search/label/PHP), [Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![Microsoft Warns of WhatsApp-Delivered VBS Malware Hijacking Windows via UAC Bypass](data:image/svg+xml;base64... "Microsoft Warns of WhatsApp-Delivered VBS Malware Hijacking Windows via UAC Bypass")

Microsoft Warns of WhatsApp-Delivered VBS Malware Hijacking Windows via UAC Bypass](https://thehackernews.com/2026/04/microsoft-warns-of-whatsapp-delivered.html)

[![New Chrome Zero-Day CVE-2026-5281 Under Active Exploitation — Patch Released](data:image/svg+xml;base64... "New Chrome Zero-Day CVE-2026-5281 Under Active Exploitation — Patch Released")

New Chrome Zero-Day CVE-2026-5281 Under Active Exploitation — Patch Released](https://thehackernews.com/2026/04/new-chrome-zero-day-cve-2026-5281-under.html)

[![Apple Expands iOS 18.7.7 Update to More Devices to Block DarkSword Exploit](data:image/svg+xml;base64... "Apple Expands iOS 18.7.7 Update to More Devices to Block DarkSword Exploit")

Apple Expands iOS 18.7.7 Update to More Devices to Block DarkSword Exploit](https://thehackernews.com/2026/04/apple-expands-ios-1877-update-to-more.html)

[![Hackers Exploit CVE-2025-55182 to Breach 766 Next.js Hosts, Steal Credentials](data:image/svg+xml;base64... "Hackers Exploit CVE-2025-55182 to Breach 766 Next.js Hosts, Steal Credentials")

Hackers Exploit CVE-2025-55182 to Breach 766 Next.js Hosts, Steal Credentials](https://thehackernews.com/2026/04/hackers-exploit-cve-2025-55182-to.html)

[![New SparkCat Variant in iOS, Android Apps Steals Crypto Wallet Recovery Phrase Images](data:image/svg+xml;base64... "New SparkCat Variant in iOS, Android Apps Steals Crypto Wallet Recovery Phrase Images")

New SparkCat Variant in iOS, Android Apps Steals Crypto Wallet Recovery Phrase Images](https://thehackernews.com/2026/04/new-sparkcat-variant-in-ios-android.html)

[![Microsoft Details Cookie-Contro...