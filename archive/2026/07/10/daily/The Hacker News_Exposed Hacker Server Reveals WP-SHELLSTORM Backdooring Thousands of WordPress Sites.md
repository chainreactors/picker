---
title: Exposed Hacker Server Reveals WP-SHELLSTORM Backdooring Thousands of WordPress Sites
url: https://thehackernews.com/2026/07/exposed-hacker-server-reveals-wp.html
source: The Hacker News
date: 2026-07-10
fetch_date: 2026-07-11T05:04:37.593817
---

# Exposed Hacker Server Reveals WP-SHELLSTORM Backdooring Thousands of WordPress Sites

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Exposed Hacker Server Reveals WP-SHELLSTORM Backdooring Thousands of WordPress Sites](https://thehackernews.com/2026/07/exposed-hacker-server-reveals-wp.html)

**Swati Khandelwal**Jul 10, 2026Cybercrime / Website Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgruetcUTsay2-ledgCIdCPKK_bPRiTzuXzYeUiLR3xuazZgHTmxO4Gz6PyyuwdFUVoHHOCbq5PksEMW18dSsdzCJddBMr8vQ3TQO3PIqXExF_17RGVfKRD8cPltNjh6eV1fgXM-pYYlwZnWaZcf7oo50CahUBY5AWt8-IS1K7KxhlL9GFLDcAk1ruwMSI/s1700-e365/hacker-server.jpg)

A cybercrime crew left one of its own servers wide open on the internet for three weeks, and it exposed the operation's inner workings: the hacking tools, the activity logs, and target lists naming more than 1.4 million websites.

Far fewer were actually broken into, but the exposed files showed researchers how a mass site-hacking operation runs from the inside.

The operation, now tracked as **WP-SHELLSTORM**, is what [SOCRadar](https://socradar.io/blog/wp-shellstorm-expose-1-4m-wordpress-sites/) calls a webshell access brokerage: a crew that breaks into sites at scale, plants a hidden backdoor (a "webshell") on each, and packages that access for resale.

The strongest activity hit WordPress sites running out-of-date plugins. If you run WordPress or Joomla, the two flaws that mattered most were in the Breeze caching plugin and Joomla's JCE editor; skip to the checklist below if that's you.

## A forgotten server

Two teams dug into the same exposed folder. SOCRadar's threat intelligence team spotted it on June 11, 2026, on a US-based rented server at 137.175.93[.]126 with no password on it at all. Inside was roughly 800MB across 434 files: webshells, exploit scripts, scan results, the operator's typed command history, and command-and-control settings.

[Ctrl-Alt-Intel](https://ctrlaltintel.com/research/Wordpress/) had analyzed the same directory too, having found it on Hunt.io's open-directory platform, and published on June 22, weeks before SOCRadar's own July 9 writeup. The exposure came down to a basic slip: the operator started a simple Python web server to move files around and left it running for 22 days.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The crew took publicly known bugs in website plugins, most of them in WordPress, and built automated scanners to fire those exploits at massive target lists pulled from FOFA, a Chinese search engine for internet-connected systems, similar to Shodan.

Where a site ran a vulnerable version, the exploit could upload a webshell: a small script that lets the attacker run commands on the server from anywhere, read files, steal passwords, and move deeper into the network.

The toolkit covered 27 known flaws, though a handful did most of the work. The biggest producer was a bug in the Breeze caching plugin (CVE-2026-3844), which the crew fired at more than 45,000 targets and, by its own count, backdoored over 17,000 of them.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhX6v2Ijtt8eT8SggY3Tr8iFOILJUsBZ0zdDZOtscX4GJWn1Q9ytZiMzFjTILVSdhXqbngQZoGYqHr5SQ5SfgCcEglXCEVrwKEjsv7Lt9rwYiiI5nfc6u1Qty1YQabQehJe10fi5FU5PftyVZwQuOJ3kKSlYfmQU1p5yb7zrbpl-U6Bf-vj5-x-DfO8DIQ/s1700-e365/actor.jpg)

That one comes with a catch: it only works when a non-default "Host Files Locally – Gravatars" setting is switched on, so most Breeze installs were never exposed.

## The numbers, in plain terms

The headline figure needs a caveat. The 1.4 million count is how many domains were on the target lists, not how many were broken into, and those lists spanned WordPress, Joomla, and other platforms. The single largest file was a list of 587,034 Joomla targets.

The number actually compromised was far smaller, and the two research teams measured it differently: Ctrl-Alt-Intel's deduplicated count found 25,195 sites with confirmed or validated compromise evidence, while SOCRadar, counting active webshells, put the live figure at 5,700-plus.

One flaw shows the gap plainly: a Joomla bug was fired at more than 560,000 targets but landed on only 77 of them.

Being on someone's scan list is not the same as being hacked. Keep that in mind whenever a report leads with a frightening target number.

## The tooling and an earlier campaign

The main backdoor, a file named down.php, was heavily obfuscated, four layers deep, and appears to be derived from an open-source Chinese webshell called BestShell. Once running, it could manage files, run commands, open reverse shells, scan the network, and check which security software the host was running.

For its own remote access, the crew used a SNOWLIGHT dropper to install VShell, a stealthy backdoor that disguises its process name as [kworker/0:2] to blend in with the kernel threads in a process list.

Those two tools have a history: in April 2025, [Sysdig](https://www.sysdig.com/blog/unc5174-chinese-threat-actor-vshell) linked this SNOWLIGHT-to-VShell chain to the suspected Chinese state group UNC5174, activity [THN covered at the time](https://thehackernews.com/2025/04/chinese-hackers-target-linux-systems.html). VShell itself, though, is a common tool in Chinese-speaking criminal circles, so its presence alone doesn't point to a state actor.

The server also held traces of an earlier, very different job. SOCRadar found that before the noisy WordPress spree, the same crew ran a quieter campaign in early May 2026 against corporate Java systems. It pulled 613 configuration files from 11 systems across nine companies in fintech, e-commerce, logistics, gaming, and electronics.

The haul included cloud login keys for AWS, Alibaba Cloud, Oracle, Tencent, and DigitalOcean, database passwords, and Alipay RSA private keys. It leaned on an old, well-known bug in Nacos, a configuration server ([CVE-2021-29441](https://nvd.nist.gov/vuln/detail/CVE-2021-29441)), that lets an attacker skip the login by faking a single web header.

SOCRadar read...