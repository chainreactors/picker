---
title: Backdoored Smart Slider 3 Pro Update Distributed via Compromised Nextend Servers
url: https://thehackernews.com/2026/04/backdoored-smart-slider-3-pro-update.html
source: The Hacker News
date: 2026-04-10
fetch_date: 2026-04-11T04:22:57.257846
---

# Backdoored Smart Slider 3 Pro Update Distributed via Compromised Nextend Servers

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

# [Backdoored Smart Slider 3 Pro Update Distributed via Compromised Nextend Servers](https://thehackernews.com/2026/04/backdoored-smart-slider-3-pro-update.html)

**Ravie Lakshmanan**Apr 10, 2026Malware / Website Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPUQqw4JQlrmSih69TSpC28TmE2G1rOMs1k_jrdeQbXFFNV6nPvlVQh9oMIwtOLiVJVUxYZFZ0RDiXmLDOPXpF-pbaStwjml7hxE-OITfsVlk2wA-nKUOpcn9R7FjQe03OInZdN2p8GmkFXAvYBbDeU_IDX1wuQ4iqc46lM6SraDPXhbEcCt-LNL0YTck/s1700-e365/slider.jpg)

Unknown threat actors have hijacked the update system for the Smart Slider 3 Pro plugin for WordPress and Joomla to push a poisoned version containing a backdoor.

The incident impacts Smart Slider 3 Pro version 3.5.1.35 for WordPress, per WordPress security company Patchstack. Smart Slider 3 is a popular WordPress slider plugin with more than 800,000 active installations across its free and Pro editions.

"An unauthorized party gained access to Nextend’s update infrastructure and distributed a fully attacker-authored build through the official update channel," the company [said](https://patchstack.com/articles/critical-supply-chain-compromise-in-smart-slider-3-pro-full-malware-analysis/). "Any site that updated to 3.5.1.35 between its release on April 7, 2026, and its detection approximately 6 hours later received a fully weaponized remote access toolkit."

Nextend, which maintains the plugin, [said](https://wordpress.org/support/topic/smart-slider-3-pro-update/#post-18873519) an unauthorized party gained unauthorized access to its update system and pushed a malicious version (3.5.1.35 Pro) that remained accessible for approximately six hours, before it was detected and pulled.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

The trojanized update includes the ability to create rogue administrator accounts, as well as drop backdoors that execute system commands remotely via HTTP headers and run arbitrary PHP code via hidden request parameters. According to Patchstack, the malware comes with the following capabilities -

* Achieve pre-authenticated remote code execution via custom HTTP headers like X-Cache-Status and X-Cache-Key, the latter of which contains the code that's passed to "shell\_exec()."
* A backdoor that supports dual execution modes, enabling the attacker to execute arbitrary PHP code and operating system commands on the server.
* Create a hidden administrator account (e.g., "wpsvc\_a3f1") for persistent access and make it invisible to legitimate administrators by tampering with the "pre\_user\_query" and "views\_users" filters.
* Use three custom WordPress options that are set with the "autoload" setting disabled to reduce their visibility in option dumps: \_wpc\_ak (a secret authentication key), \_wpc\_uid (user ID of the hidden administrator account), and \_wpc\_uinfo (Base64-encoded JSON containing the plaintext username, password, and email of the rogue account).
* Install persistence in three locations for redundancy: create a [must-use plugin](https://thehackernews.com/2025/07/hackers-deploy-stealth-backdoor-in.html) with the filename "object-cache-helper.php" to make it look like a legitimate caching component, append the backdoor component to the active theme's "functions.php" file, and drop a file named "class-wp-locale-helper.php" in the WordPress "wp-includes" directory.
* Exfiltrate data containing site URL, secret backdoor key, hostname, Smart Slider 3 version, WordPress version, and PHP version, WordPress admin email address, WordPress database name, plaintext username and password of the administrator account, and a list of all installed persistence methods to the command-and-control (C2) domain "wpjs1[.]com."

"The malware operates in several stages, each designed to ensure deep, persistent, and redundant access to the compromised site," Patchstack said.

"The sophistication of the payload is notable: rather than a simple webshell, the attacker deployed a multi-layered persistence toolkit with several independent, redundant re-entry points, user concealment, resilient command execution with fallback chains, and automatic C2 registration with full credential exfiltration.

It's worth noting that the free version of the WordPress plugin is not affected. To contain the issue, Nextend shut down its update servers, removed the malicious version, and launched a full investigation into the incident.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

Users who have the trojanized version installed are advised to update to version 3.5.1.36. In addition, users who have installed the rogue version are recommended to perform the [following cleanup steps](https://smartslider.helpscoutdocs.com/article/2144-wordpress-security-advisory-smart-slider-3-pro-3-5-1-35-compromise) -

* Check for any suspicious or unknown admin accounts and remove them.
* Remove Smart Slider 3 Pro version 3.5.1.35 if installed.
* Reinstall a clean version of the plugin.
* Remove all persistence files that allow the backdoor to persist on the site.
* Delete malicious WordPress options from the "wp\_options" table: \_wpc\_ak, \_wpc\_uid, \_wpc\_uinfo, \_perf\_toolkit\_source, and wp\_page\_for\_privacy\_policy\_cache.
* Clean up the "wp-config.php" file, including removing "define('WP\_CACHE\_SALT', '<token>');" if it exists.
* Remove the line "# WPCacheSalt <token>" from the ".htaccess" file located in the WordPress root folder.
* Reset the administrator and WordPress database user passwords.
* Change FTP/SSH and hosting account credentials.
* Review the website and logs for any unauthorized changes and unusual POST requests.
* Enable two-factor authentication (2FA) for admins and disable PHP execution in the uploads folder.

"This incident is a textbook supply chain compromise, the kind that renders traditional perimeter defenses irrelevant," Patchstack said. "Generic firewall rules, nonce verification,role-based access controls,none of them apply when the malicious code is delivered through the trusted update channel. The plugin is the malware."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), ...