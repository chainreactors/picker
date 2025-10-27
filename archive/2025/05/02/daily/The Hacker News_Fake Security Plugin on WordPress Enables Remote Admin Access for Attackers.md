---
title: Fake Security Plugin on WordPress Enables Remote Admin Access for Attackers
url: https://thehackernews.com/2025/05/fake-security-plugin-on-wordpress.html
source: The Hacker News
date: 2025-05-02
fetch_date: 2025-10-06T22:31:21.105426
---

# Fake Security Plugin on WordPress Enables Remote Admin Access for Attackers

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Fake Security Plugin on WordPress Enables Remote Admin Access for Attackers](https://thehackernews.com/2025/05/fake-security-plugin-on-wordpress.html)

**May 01, 2025**Ravie LakshmananMalware / Web Skimming

[![Fake Security Plugin on WordPress](data:image/png;base64... "Fake Security Plugin on WordPress")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNEV0nIK_bmQg_kdIYebdbkzbE50yAdC8QUFAJrjmDguTYi0mCl97sOj70N2CFFaPTB3aHpni7ZGBb7O2bDzHWWZUCG3MNxa-ZSMB3e0BSlki3iN7hrk4HLCWlzBzVVOtXieUpLC3q6uUTig56pi3WUCSrNLoZRq0z9ba12YuQlXkGGrx0k7h7Cd46ScCi/s790-rw-e365/wordpress.jpg)

Cybersecurity researchers have shed light on a new campaign targeting WordPress sites that disguises the malware as a security plugin.

The plugin, which goes by the name "WP-antymalwary-bot.php," comes with a variety of features to maintain access, hide itself from the admin dashboard, and execute remote code.

"Pinging functionality that can report back to a command-and-control (C&C) server is also included, as is code that helps spread malware into other directories and inject malicious JavaScript responsible for serving ads," Wordfence's Marco Wotschka [said](https://www.wordfence.com/blog/2025/04/interesting-wordpress-malware-disguised-as-legitimate-anti-malware-plugin/) in a report.

First discovered during a site cleanup effort in late January 2025, the malware has since been detected in the wild with new variants. Some of the other names used for the plugin are listed below -

* addons.php
* wpconsole.php
* wp-performance-booster.php
* scr.php

Once installed and activated, it provides threat actors administrator access to the dashboard and makes use of the REST API to facilitate remote code execution by injecting malicious PHP code into the site theme's header file or clearing the caches of popular caching plugins.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A new iteration of the malware includes notable changes to the manner code injections are handled, fetching JavaScript code hosted on another compromised domain to serve ads or spam.

The plugin is also complemented by a malicious wp-cron.php file, which recreates and reactivates the malware automatically upon the next site visit should it be removed from the plugins directory.

It's currently not clear how the sites are breached to deliver the malware or who is behind the campaign. However, the presence of Russian language comments and messages likely indicates that the threat actors are Russian-speaking.

The disclosure comes as Sucuri [detailed](https://blog.sucuri.net/2025/04/fake-font-domain-used-to-skim-credit-card-data.html) a web skimmer campaign that uses a fake fonts domain named "italicfonts[.]org" to display a fake payment form on checkout pages, steal entered information, and exfiltrate the data to the attacker's server.

Another "advanced, multi-stage carding attack" examined by the website security company involves targeting Magento e-commerce portals with JavaScript malware designed to harvest a wide range of sensitive information.

"This malware leveraged a fake GIF image file, local browser sessionStorage data, and tampered with the website traffic using a malicious reverse proxy server to facilitate the theft of credit card data, login details, cookies, and other sensitive data from the compromised website," security researcher Ben Martin [said](https://blog.sucuri.net/2025/04/fake-gif-leveraged-in-multi-stage-reverse-proxy-card-skimming-attack.html).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0-btc2zHmQ6jshBYmwln3ikkkaXH9syTeAvBYSlagHEquNYy9XGSqdRYQCbDeptkDsXd2wTu7X6vpuKIobxg6sDMDDo1KzR44RFcoHUDGnH4PIcQTNV5TyyoDHXAbTZSD2_zkxuKfd05Ho62qcK1LAdXNlOo41IagONoufWX8S0T5mdjhJVDwnkPFJqZz/s790-rw-e365/rr.png)

The GIF file, in reality, is a PHP script that acts as a reverse proxy by capturing incoming requests and using it to collect the necessary information when a site visitor lands on the checkout page.

Adversaries have also been observed injecting Google AdSense code into at least 17 WordPress sites in various places with the goal of delivering unwanted ads and generating revenue on either a per-click or per-impression basis.

"They're trying to use your site's resources to continue serving ads, and worse, they could be stealing your ad revenue if you're using AdSense yourself," security researcher Puja Srivastava [said](https://blog.sucuri.net/2025/04/ad-jacked-cybercriminals-inject-google-adsense-into-wordpress.html). "By injecting their own Google AdSense code, they get paid instead of you."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

That's not all. Deceptive CAPTCHA verifications served on compromised websites have been found to trick users into downloading and executing Node.js-based backdoors that gather system information, grant remote access, and deploy a Node.js remote access trojan (RAT), which is designed to tunnel malicious traffic through SOCKS5 proxies.

The activity has been attributed by Trustwave SpiderLabs to a traffic distribution system (TDS) called [Kongtuke](https://thehackernews.com/2025/02/crazy-evil-gang-targets-crypto-with.html) (aka 404 TDS, Chaya\_002, LandUpdate808, and [TAG-124](https://www.recordedfuture.com/blog/massive-hidden-infrastructure-enabling-big-game-hunting-at-scale)).

"The JS script which, was dropped in post-infection, is designed as a multi-functional backdoor capable of detailed system reconnaissance, executing remote commands, tunneling network traffic (SOCKS5 proxy), and maintaining covert, persistent access," security researcher Reegun Jayapaul [said](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/yet-another-nodejs-backdoor-yanb-a-modern-challenge/).

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackers...