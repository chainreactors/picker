---
title: 3,500 Websites Hijacked to Secretly Mine Crypto Using Stealth JavaScript and WebSocket Tactics
url: https://thehackernews.com/2025/07/3500-websites-hijacked-to-secretly-mine.html
source: The Hacker News
date: 2025-07-22
fetch_date: 2025-10-06T23:53:55.251513
---

# 3,500 Websites Hijacked to Secretly Mine Crypto Using Stealth JavaScript and WebSocket Tactics

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

# [3,500 Websites Hijacked to Secretly Mine Crypto Using Stealth JavaScript and WebSocket Tactics](https://thehackernews.com/2025/07/3500-websites-hijacked-to-secretly-mine.html)

**Jul 21, 2025**Ravie LakshmananWeb Security / Cryptocurrency

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxP95NN1kBjfUMblpJmjAZQib7WECogHzGu2ds6_NHBi4IfexewVLmKOkpDmx1XCvkFoXrNfQqIjxwC9NddPsFjDFPhn-QHckUOiZwzzVWXXDBej4Iow-kdXofY0mLYKfmuy_MTr6rIYoqf68nirtw-nQ_R1wGyHaVgY6ylY-d95m6UZQX03zc8odYCHN6/s790-rw-e365/code.jpg)

A new attack campaign has compromised more than 3,500 websites worldwide with JavaScript cryptocurrency miners, marking the return of browser-based cryptojacking attacks once popularized by the likes of [CoinHive](https://thehackernews.com/2018/07/coinhive-shortlink-crypto-mining.html).

Although the service has since [shuttered](https://thehackernews.com/2019/02/cryptocurrency-mining-coinhive.html) after browser makers took steps to ban miner-related apps and add-ons, researchers from the c/side said they found evidence of a stealthy miner packed within obfuscated JavaScript that assesses the computational power of a device and spawns background Web Workers to execute mining tasks in parallel without raising any alarm.

More importantly, the activity has been found to leverage WebSockets to fetch mining tasks from an external server, so as to dynamically adjust the mining intensity based on the device capabilities and accordingly throttle resource consumption to maintain stealth.

"This was a stealth miner, designed to avoid detection by staying below the radar of both users and security tools," security researcher Himanshu Anand [said](https://cside.dev/blog/cryptojacking-is-dead-long-live-cryptojacking).

The net result of this approach is that users would unknowingly mine cryptocurrency while browsing the compromised website, turning their computers into covert crypto generation machines without their knowledge or consent. Exactly how the websites are breached to facilitate in-browser mining is currently not known.

Further dissection has determined that over 3,500 websites have been ensnared in the sprawling illicit crypto mining effort, with the domain hosting the JavaScript miner also linked to [Magecart credit card skimmers](https://thehackernews.com/2025/01/wordpress-skimmers-evade-detection-by.html) in the past, indicating attempts on the part of the attackers to diversify their payloads and revenue streams.

The use of the same domains to deliver both miner and credit/debit card exfiltration scripts indicates the ability of the threat actors to weaponize JavaScript and stage opportunistic attacks aimed at unsuspecting site visitors.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Attackers now prioritize stealth over brute-force resource theft, using obfuscation, WebSockets, and infrastructure reuse to stay hidden," c/side said. "The goal isn't to drain devices instantly, it is to persistently siphon resources over time, like a digital vampire."

The findings coincide with a [Magecart skimming campaign](https://cside.dev/blog/magecart-targeting-east-asian-e-commerce-websites-on-opencart) targeting East Asian e-commerce websites using the OpenCart content management system (CMS) to inject a fake payment form during checkout and collect financial information, including bank details, from victims. The captured information is then exfiltrated to the attacker's server.

In recent weeks, client-side and website-oriented attacks have been found to take different forms -

* Utilizing JavaScript embeds that [abuse](https://cside.dev/blog/weaponized-google-oauth-triggers-malicious-websocket) the callback parameter associated with a legitimate Google OAuth endpoint ("accounts.google[.]com/o/oauth2/revoke") to redirect to an obfuscated JavaScript payload that creates a malicious WebSocket connection to an attacker-controlled domain
* Using Google Tag Manager ([GTM](https://thehackernews.com/2025/02/hackers-exploit-google-tag-manager-to.html)) script directly [injected](https://blog.sucuri.net/2025/07/wordpress-redirect-malware-hidden-in-google-tag-manager-code.html) into the WordPress database (i.e., wp\_options and wp\_posts tables) in order to load remote JavaScript that redirects visitors to over 200 sites to spam domains
* Compromising a WordPress site's [wp-settings.php file](https://blog.sucuri.net/2025/07/stealthy-php-malware-uses-zip-archive-to-redirect-wordpress-visitors.html) to include a malicious PHP script directly from a ZIP archive that connects to a command-and-control (C2) server and ultimately leverages the site's search engine rankings to inject spammy content and boost their sketchy sites in search results
* Injecting malicious code into a [WordPress site theme's footer PHP script](https://blog.sucuri.net/2025/07/attackers-inject-code-into-wordpress-theme-to-redirect-visitors.html) to server browser redirects
* Using a fake WordPress plugin named after the [infected domain](https://blog.sucuri.net/2025/07/fake-spam-plugin-uses-victims-domain-name-to-evade-detection.html) to evade detection and spring into action only when search engine crawlers are detected in order to serve spam content designed to manipulate search engine results
* Distributing [backdoored versions](https://patchstack.com/articles/critical-malware-found-in-gravityforms-official-plugin-site/) of the WordPress plugin Gravity Forms (affecting only versions 2.9.11.1 and 2.9.12) through the official download page in a supply chain attack that contacts an external server to fetch additional payloads and adds an admin account that gives the attacker complete control of the website

"If installed, the malicious code modifications will block attempts to update the package and attempt to reach an external server to download additional payload," RocketGenius, the team behind Gravity Forms, [said](https://www.gravityforms.com/blog/security-incident-notice/).

"If it su...