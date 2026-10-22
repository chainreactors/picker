---
title: PHP2Shell: Two Unpatched Critical PHP RCE Flaws (CVSS 9.2) Trigger Emergency Security Alert
url: https://thehackernews.com/2026/10/php2shell-two-unpatched-critical-php.html
source: The Hacker News
date: 2026-10-21
fetch_date: 2026-10-22T06:46:44.119239
---

# PHP2Shell: Two Unpatched Critical PHP RCE Flaws (CVSS 9.2) Trigger Emergency Security Alert

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [PHP2Shell: Two Unpatched Critical PHP RCE Flaws (CVSS 9.2) Trigger Emergency Security Alert](https://thehackernews.com/2026/10/php2shell-two-unpatched-critical-php.html)

**Swati Khandelwal**Oct 21, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcxq1wmaSTaMiFJnrulXjwGrIIkIHBR3Q9Yv6Lky3rAie6XPOnFmXOVckMgVzGn9yvodrbkt6kV623Ofg8Iw-1MTDRoCVzXPiikivnZ5R7OynIF5-QC0DAiwXq8q2MRS3PZaz9NpjhJUqa-QWi1AQJ2XnJ-nvUNEvG3f1E0UpU5slUwzguAI-cESkZ5Xc/s1700-nu-rw-lo-l85-e365/php2shell.jpg)

*This story is developing and was written before PHP's scheduled 14:00 UTC release on October 21. Once the release is out, the affected and fixed versions below are confirmed by the official advisory.*

PHP will ship an out-of-cycle security release at 14:00 UTC today, October 21, for two critical vulnerabilities that its security team has rated 9.2 on the CVSS v4.0 scale but has not described.

[⚡ UPDATE — PHP Issues Emergency Patches for Two Critical PHP2Shell RCE Flaws as Exploit Attempts Emerge](https://thehackernews.com/2026/10/php-issues-emergency-patches-for-two.html)

Security researchers at watchTowr say the two flaws allow remote code execution. Only the four supported PHP branches, 8.2 through 8.5, can receive the fix, and no exploitation has been reported so far.

The [advance notice](https://www.php.net/archive/2026.php#2026-10-20-1) followed a leak. On October 20, a [post on HN](https://news.ycombinator.com/item?id=50167754) said two PHP remote code execution flaws, rated CVSS 10.0 and affecting versions from PHP 5 onward, would be disclosed on Thursday, October 22. The poster said they had "no evidence beyond 'source: trust me, bro'".

watchTowr then posted on X that the leaked information was real, that the two flaws were under embargo, that everyone had been supposed to wait until Thursday, and that it could not share more for now.

PHP published its [notice](https://news-web.php.net/php.announce/509) that evening, at 19:33 UTC, with the release set for Wednesday, a day before the date watchTowr gave. The notice says PHP may release earlier "should details of either vulnerability become public, or should evidence of active exploitation appear in the wild."

The leak carried the flaws' existence, a score, a date, and two CVE identifiers, not how the flaws work. The CVSS 10.0 figure is the leak's. PHP's rating is 9.2 on version 4.0 of the scale.

The identifiers researchers are using, **CVE-2026-109618** and **CVE-2026-109619**, were also listed in the leaked post. PHP's notice names neither. The claim that every version since PHP 5 is affected is unconfirmed too: watchTowr's own [FAQ](https://watchtowr.com/intelligence/php-cve-2026-109618-faq/) on the flaws says that scope "has not been confirmed by an official vendor advisory" and that no configuration or feature requirement has been described.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

PHP says "Full details, affected versions, and the fixed versions will be published with the release." Researchers have started calling the pair php2shell. The name is theirs, not PHP's.

Whatever the affected range turns out to be, PHP issues fixes only for its [four supported branches](https://www.php.net/supported-versions.php), and records each branch's changes in its [changelog](https://www.php.net/ChangeLog-8.php). Versions 8.2 and 8.3 receive only security fixes, and 8.4 and 8.5 are in active support. Ahead of the release, several trackers, including Alpine Linux's and security researcher Kevin Beaumont, expect the fixes to ship as PHP 8.5.12, 8.4.27, 8.3.36, and 8.2.35, the next point release of each branch, though PHP has not confirmed the numbers.

Anything older, including 8.1, 8.0, 7.x, and 5.x, is end of life and gets no PHP fix. If the flaws reach those branches, installations on them will have no vendor patch.

PHP branches that can receive today's fix

| Branch | Current release (September 24) | PHP support status |
| --- | --- | --- |
| 8.5 | 8.5.11 | Active support until December 31, 2027 |
| 8.4 | 8.4.26 | Active support until December 31, 2026 |
| 8.3 | 8.3.35 | Security fixes only until December 31, 2027 |
| 8.2 | 8.2.34 | Security fixes only until December 31, 2026 |

Security company Mallory [counted](https://mallory.ai/blog/php-rce-rapid-response) about 884,000 internet-facing hosts whose HTTP banner reported a PHP version of 8.1 or older to the Shodan search engine on October 20, 59% of the roughly 1.5 million hosts that reported any version. The count covers banners, not confirmed affected systems, and a further 740,000 hosts reported PHP without a version.

PHP has published no workaround. Until the release lands, the preparation comes down to six steps, most of them drawn from a rapid-response post from [Huntress](https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities), with CERT-EU's isolation advice added.

1. Inventory every PHP install, including PHP bundled in vendor appliances, Windows software, and control panels such as cPanel and Plesk.
2. Be ready to upgrade at 14:00 UTC. Patch internet-facing systems first, and check your Linux distribution and hosting provider for backported packages.
3. On an end-of-life branch, upgrade, take the system off the internet, or put it behind a VPN or a web application firewall until you can.
4. Where patching cannot be done at once, [CERT-EU](https://cert.europa.eu/publications/security-advisories/2026-018/) advises that you "consider isolating internet-facing applications from public networks until a fix is available."
5. Watch what PHP starts. Alert on php-fpm, php-cgi, httpd, or apache2 launching shells, interpreters, or download tools. On Linux servers without endpoint detection, Florian Roth's [process-watcher](https://github.com/Neo23x0/process-watcher/blob/main/emerging-threats/php-rce-october-26/README.md) logs every program a PHP process starts...