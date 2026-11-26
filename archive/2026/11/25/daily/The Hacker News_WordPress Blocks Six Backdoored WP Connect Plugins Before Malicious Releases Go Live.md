---
title: WordPress Blocks Six Backdoored WP Connect Plugins Before Malicious Releases Go Live
url: https://thehackernews.com/2026/11/wordpress-blocks-six-backdoored-wp.html
source: The Hacker News
date: 2026-11-25
fetch_date: 2026-11-26T10:15:12.994027
---

# WordPress Blocks Six Backdoored WP Connect Plugins Before Malicious Releases Go Live

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

# [WordPress Blocks Six Backdoored WP Connect Plugins Before Malicious Releases Go Live](https://thehackernews.com/2026/11/wordpress-blocks-six-backdoored-wp.html)

**Ravie Lakshmanan**Nov 25, 2026Web Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNbawIx8zYCfd7sCTbVfIzPFBtykkY65lf8EOswU62pIdZKTrx9ReB3mGnqYqujmW5eGzN_w8pEijAZMTpmOZ3fGB5zFyFaPo4ZhRQ8V0BkAmDCH3WoVqJ3kAfjDcw3_wRjhwphfyJxjF3_rDYiudb-cxt0pY3t8s-IRjNP1aEYHqtO5L1eZMkgBX6y2xD/s1700-nu-rw-lo-l85-e365/wp.jpg)

WordPress has removed six WordPress plugins developed by WP Connect after they were backdoored on November 22, 2026, to enable arbitrary code execution on sites that have them installed, following a suspected compromise of the developer's account.

The WordPress plugins team has proactively detected and blocked the threat before it could be officially released. Visiting each plugin listing now serves the message: "This plugin has been closed as of November 22, 2026, and is not available for download. This closure is permanent."

The names of the affected plugins and the malicious versions are listed below -

* [Air WP Sync – Airtable to WordPress](https://wordpress.org/plugins/air-wp-sync/) (2.9.1 – 2.9.4)
* [WP Sync for Notion – Notion to WordPress](https://wordpress.org/plugins/wp-sync-for-notion/) (1.7.4)
* [Add-on Brevo for Gravity Forms](https://wordpress.org/plugins/addon-gravityforms-sendinblue-free/) (2.6.3)
* [Add-On for Contact Form 7 to Airtable](https://wordpress.org/plugins/add-on-cf7-for-airtable/) (2.5.4)
* [Add-On for Contact Form 7 to Notion](https://wordpress.org/plugins/add-on-cf7-for-notion/) (1.6.4)
* [Orders Sync to Airtable for WooCommerce](https://wordpress.org/plugins/orders-sync-to-airtable-for-woocommerce/) (1.0.2)

These plugins have been collectively installed on more than 3,600 WordPress sites, according to WordPress security company Wordfence. The supply chain compromise is being tracked as CVE-2026-135202 (CVSS score: 9.8). It remains unpatched.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

"Each release silently loaded the same remote-control module, which phones home to an attacker-controlled server, executes any PHP code it is sent, and exposes a full command set for running shell commands, stealing password hashes, and planting webshells," security researcher Chloe Chamberland [said](https://www.wordfence.com/blog/2026/11/supply-chain-compromise-backdoors-six-wp-connect-plugins-blocked-by-wordpress-orgs-release-hold/).

Specifically, the plugins come with a backdoor module ("includes/airwp-online.php") that runs on every request, sends site information (site URL, PHP, WordPress, and OS versions, and the server user) to a hard-coded command-and-control server ("tascredit-pay[.]com"), and runs PHP code returned by the server via eval().

It can also perform the following actions -

* Accept queued commands that run shell commands
* Read, write, and delete arbitrary files
* Query arbitrary database tables
* Dump the users table including login, email address, and password hashes
* Drop a web shell into the uploads directory or to a path of the attacker's choosing
* Register an hourly WP-Cron hook that runs attacker-supplied code

As a result, an unauthenticated attacker in control of the site can execute arbitrary code on the server and take complete control, facilitating credential theft and persistence through web shells and cron hooks that outlast the plugin removal.

Because the malicious versions were never released and blocked due to [WordPress's new cooldown protections](https://thehackernews.com/2026/09/wordpress-adds-automated-plugin-reviews.html) as part of its Protect The Shire initiative, sites running these plugins are unlikely to be affected. However, it's essential that site owners check their websites to make sure that they are not running one of the compromised versions and remove them as soon as possible.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

"Unlike a typical vulnerability, this was not a coding mistake, and there is no patch: the malicious code was added deliberately and committed to each plugin's WordPress.org repository," Chamberland said. "Taken together, this strongly suggests that the developer's WordPress.org account was compromised and used to push the malicious releases, rather than that the vendor shipped this code intentionally."

The disclosure comes as URLscan.io revealed that an unspecified WordPress site had been infected by multiple cybercriminal campaigns, with attackers attempting to disable or remove scripts belonging to competing threat actors.

The site carried "thirteen separate [ClickFix](https://thehackernews.com/2026/11/romulus-clickfix-attacks-deliver-rat.html) injections from three distinct kits [LOM, ErrTraffic, and Macfinger], alongside seven further malicious loaders," it [said](https://urlscan.io/blog/2026/11/19/CompetingClickFixInjections/). "Several of the injections attempt to remove each other's code and overlays, and one injection disables another through a JavaScript naming collision. Five of the thirteen injections resolve their next-stage infrastructure from Polygon smart contracts, a technique known as [EtherHiding](https://thehackernews.com/2026/08/trojanized-npm-packages-decode-c2-ip.html)."

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
[**Share on Reddit](...