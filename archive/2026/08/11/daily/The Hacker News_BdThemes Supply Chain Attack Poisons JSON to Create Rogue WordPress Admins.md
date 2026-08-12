---
title: BdThemes Supply Chain Attack Poisons JSON to Create Rogue WordPress Admins
url: https://thehackernews.com/2026/08/bdthemes-supply-chain-attack-poisons.html
source: The Hacker News
date: 2026-08-11
fetch_date: 2026-08-12T04:02:50.702552
---

# BdThemes Supply Chain Attack Poisons JSON to Create Rogue WordPress Admins

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

![cybersecurity](data:image/svg+xml;base64...)

# [BdThemes Supply Chain Attack Poisons JSON to Create Rogue WordPress Admins](https://thehackernews.com/2026/08/bdthemes-supply-chain-attack-poisons.html)

**Ravie Lakshmanan**Aug 11, 2026Supply Chain Attack / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh96gU64z_xM5LiLI39IXPndJ1felnUkfQmWxQ2sGfE9r_yYK6AKPLV3x6uVWeZxZoEsJwy0h7OUHILX1sAbwc6MYHpIeeTvCVeH52TnCInqqjjRPW4-Sx7gPPq4abN7ltCnClrjRhDDqyON8UBxcKFjoyubm7CeEgaZos3j4OCLJdRozfEOrDX1rPsnSoF/s1700-e365/wordpress.jpg)

Cybersecurity researchers have warned of a supply chain compromise impacting WordPress plugin vendor BdThemes, prompting the content management systems (CMS) platform's plugins team to temporarily disable their downloads.

"Unlike traditional software supply chain attacks, zero source code files were modified within the official WordPress.org repository," Wordfence researcher Paolo Tresso [said](https://www.wordfence.com/blog/2026/08/psa-supply-chain-compromise-in-bdthemes-ecosystem-via-poisoned-api-response/). "Instead, threat actors poisoned a static remote JSON data stream fetched by an administrative promotional banner component."

The list of affected plugins is below -

* Element Pack Addons for Elementor – Elementor Widgets, Elementor Templates, Elementor Addons [bdthemes-element-pack-lite] - 100,000+ active installs
* Live Copy Paste for Elementor – Cross Domain Copy Paste & Page Duplicator [live-copy-paste] - 6,000+ active installs
* Pixel Gallery Addons for Elementor – Easy Grid, Creative Gallery, Drag and Drop Grid, Custom Grid Layout, Portfolio Gallery [pixel-gallery] - N/A
* Prime Slider Addons for Elementor – Widgets, Templates & Elementor Addons [bdthemes-prime-slider-lite] - N/A
* Smart Admin Assistant – Dashboard and Site Enhancements [smart-admin-assistant] - N/A
* Ultimate Post Kit Addons for Elementor [ultimate-post-kit] - N/A
* Ultimate Store Kit – Addon For WooCommerce, EDD and Elementor [ultimate-store-kit] - 6,000+ active installs

Users visiting the listings for each of the aforementioned plugins on the WordPress plugins directory are displayed the message that they have been closed as of either August 7 or 8, 2026, and are not available for download pending a "full review."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The issue, per the WordPress security company, is rooted in an internal component called Biggopti that's shipped along with the plugins. The system is designed to pull promotional banners from their API server and render them in the WordPress admin dashboard by fetching relevant JSON files from a DigitalOcean Spaces bucket.

The library has been found vulnerable to a cross-site scripting (XSS) flaw in the JSON response parsing code via the "display\_id" parameter from the Sigmative API due to insufficient client-side escaping. As a result, an attacker who can compromise the API can inject arbitrary web scripts in pages that get executed every time a user accesses those pages.

Because the script runs on every "wp-admin" page load, the injected code gets activated silently in the browser of any logged-in administrator. The vulnerability is rated 5.4 on the CVSS scoring system, indicating medium severity.

The change is said to have been first introduced on March 1, 2026, in "bdthemes-prime-slider-lite" before being applied to others. The attack is notable because it's entirely driven via the API and requires no plugin updates or files to be modified on disk.

"Rogue actors obtained write access to that bucket, replacing the legitimate JSON responses with crafted payloads to exploit that vulnerability," Wordfence said. "The XSS fires inside every logged-in admin's browser, silently, on every wp-admin page load. From there, the injected script creates rogue administrator accounts, uploads a web shell plugin, and phones home to a command-and-control (C2) server."

The main payload is delivered to the plugins using the "api-data-all-records" API endpoint. A JavaScript file named "w2.js," the payload performs the following actions -

* Contacts the C2 server ("ia-cdn[.]com/fz/c") with the victim website's origin to fetch targeting instructions. The execution is aborted if the C2 server returns a "skip" or "done" status.
* Creates a new rogue administrator via the WordPress REST API.
* Downloads a fake plugin ZIP from the C2 server and installs it via the standard plugin upload form, resulting in the deployment of a PHP web shell ("emer-run.php").
* Invokes the web shell to install two persistence modules into the Must-Use plugins ("[mu-plugins](https://thehackernews.com/2025/03/hackers-exploit-wordpress-mu-plugins-to.html)") directory: one is a "magic-login backdoor" that allows unauthenticated administrative entry via a URL parameter (?\_wplogin=<token>)by targeting the site's longest-registered administrator and the other is an anti-analysis stealth module that hooks into WordPress database queries to conceal the presence of the rogue user accounts from the administrative user list and display the total user count by excluding them.

An alternate payload ("x.js") found hosted on the plugin developer's infrastructure is served to victims using the "api-data-records" API endpoint. It's designed to generate "deterministic" administrative credentials that are mathematically derived from the victim website's hostname.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

"This algorithm produces predictable usernames (bd\_ followed by a 6-character base36 hash) and passwords (Bd@26! followed by the hash and x), pairing them with an @wordpress.org email address," Wordfence said. "Because the credentials are deterministic, threat actors do not need to store compromised site lists centrally, and incident responders can compute the exact username and password to hunt for on suspected domains."

The generated credentials are then leveraged to create a malicious administrator user, and the results of the attack are then exfiltrated back to the C2 server.

The C2 server used in the campaign is assessed to be related to two other software supply chain attacks involving [Advanced Responsive Video Embedder](https://www.wordfence.com/blog/2026/07/wordfence-prism-de...