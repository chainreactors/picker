---
title: WordPress Adds Automated Plugin Reviews to Block High-Risk Updates Before Distribution
url: https://thehackernews.com/2026/09/wordpress-adds-automated-plugin-reviews.html
source: The Hacker News
date: 2026-09-14
fetch_date: 2026-09-15T07:03:15.868270
---

# WordPress Adds Automated Plugin Reviews to Block High-Risk Updates Before Distribution

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

# [WordPress Adds Automated Plugin Reviews to Block High-Risk Updates Before Distribution](https://thehackernews.com/2026/09/wordpress-adds-automated-plugin-reviews.html)

**Ravie Lakshmanan**Sep 14, 2026Web Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6NRxf0-3Ca12cwdQVS-bicsxwk-06KQZJaLMbd2d217NkuO82Bld3P_E96WP8OEqZXSjDoLtW0JfnRYkQSyl0BlQDNkQoBOf7x-Q5wOmpc59Z4v1ycux0YWShQpPIyvYmMmIRJ0c5Zv_38VFrhwtdcdoxycqIm0b5Df7AeYjbr-8KCJlbujHVhmpvdtrk/s1700-nu-rw-lo-l85-e365/wordpress-auto.jpg)

WordPress has announced it's launching an automated security review for every release of a plugin before it's distributed through the WordPress.org update API so as to analyze it for potential security issues and ensure there are no risks involved.

"New plugins are reviewed before they enter the directory, but updates ship continuously after that," David Perez, WordPress Official Plugin Repository Team Co-Lead, [said](https://make.wordpress.org/plugins/2026/09/09/automated-security-review-for-plugin-releases/). "A plugin can be secure today and introduce a vulnerability, or malicious code, in a future release."

WordPress said the lack of a "consistent review step" between the commit of a release and the release of a plugin to downstream users meant that it could open the door for malicious attacks.

The content management system (CMS) platform noted that its automated review detected a backdoor committed to a release of a plugin with about 20,000 active installations on July 28, 2026. Because the release was within a cooldown window, the compromised version of the plugin never ended up getting distributed through the WordPress.org update API.

The plugin was closed for downloads 26 minutes after the Plugins Team was alerted to the update by WordPress security company Wordfence. WordPress did not disclose the name of the plugin.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Since June 5, 2026, every WordPress plugin and theme goes through a [cooldown period](https://wordpress.org/news/2026/06/pts/) before being distributed through auto-updates as part of a new security initiative called Protect The Shire. The idea is to introduce some friction to the process so that malicious updates do not reach end users immediately. The cooldown period is currently at six hours, [down from 24 hours](https://wp-content.co/protect-the-shire-initiatives-cooldown-period-reduced-to-six-hours-developers-call-out-lack-of-notice/) when it was first introduced.

The latest effort aims to close another critical security gap: a high-risk score for a plugin or theme release should automatically halt distribution without involvement from the Plugins Team. The entire process goes through the following steps -

* During the cooldown period, the changes in each release are analyzed in WordPress.org by artificial intelligence (AI) models along with Jetpack Scan.
* Results are cross-verified and combined into a security score: A higher score translates to a potentially higher risk.
* Releases with a high risk score are blocked automatically once the review completes, while those below that threshold will continue the normal process.
* Plugin committers receive an email with the findings. Emails are only sent in scenarios where a plugin is blocked.

That said, it's worth noting that a high risk score does not necessarily indicate malicious intent, as the score also takes into account inadvertently introduced security flaws just as it flags intentional malware.

In a follow-up comment, Perez elaborated that the security review "looks for the same vulnerability classes any security audit looks for," urging developers to follow [WordPress Coding Standards](https://github.com/WordPress/WordPress-Coding-Standards/) and PHP\_CodeSniffer ([PHPCS](https://github.com/squizlabs/PHP_CodeSniffer)) rules to validate their code and ensure code quality. Developers publishing WooCommerce extensions are recommended to use the Quality Insights Toolkit ([QIT](https://qit.woo.com/)) testing platform.

Other patterns that could also drive the risk score up are below -

* REST, AJAX or admin-post endpoints without a capability check (a nonce alone is not authorization)
* Queries built without $wpdb->prepare()
* File paths, uploads, deletions or includes built from request data
* unserialize() on request data or on a remote response
* Options, user meta or settings written from endpoints reachable by subscribers or unauthenticated users
* Code fetched or evaluated at runtime, and obfuscated or packed code

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

Once a release is blocked, the only way for the developer to get the restrictions removed is to review the findings, fix the issues, and publish a new release. Should the new release score below the high-risk threshold, it continues through the normal cooldown process.

"If a finding looks incorrect, authors can contact the Plugins Team," Perez said. "Please understand that the team handles a high volume of reviews, so publishing a fixed release is almost always faster than waiting for a manual review of an appeal."

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
[![Facebook Messenger]...