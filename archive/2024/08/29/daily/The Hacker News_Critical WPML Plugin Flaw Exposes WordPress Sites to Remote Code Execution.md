---
title: Critical WPML Plugin Flaw Exposes WordPress Sites to Remote Code Execution
url: https://thehackernews.com/2024/08/critical-wpml-plugin-flaw-exposes.html
source: The Hacker News
date: 2024-08-29
fetch_date: 2025-10-06T18:10:02.454250
---

# Critical WPML Plugin Flaw Exposes WordPress Sites to Remote Code Execution

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

# [Critical WPML Plugin Flaw Exposes WordPress Sites to Remote Code Execution](https://thehackernews.com/2024/08/critical-wpml-plugin-flaw-exposes.html)

**Aug 28, 2024**Ravie LakshmananWordPress Security / Website Protection

[![WPML Plugin Flaw](data:image/png;base64... "WPML Plugin Flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1TdktyLZv9Not7fvAbH1YMEOa3_jfRPrj6fkxeFwFb1Ab2Qk0URwsIqzOH6SyneAULR4PqHVPlb4ftiP5CnR3Jy3CeXW-VYRaV5s5Hcw9IYpWG1EnBtRo3gnA4BrFE6YnVfMPZbckpNz5fz4JnDjK7JznjsETjn3Esw9ArRNgW14k4IrNEBCmMGhpuDEA/s790-rw-e365/wpml.png)

A critical security flaw has been disclosed in the WPML WordPress multilingual plugin that could allow authenticated users to execute arbitrary code remotely under certain circumstances.

The vulnerability, tracked as [CVE-2024-6386](https://www.wordfence.com/blog/2024/08/1000000-wordpress-sites-protected-against-unique-remote-code-execution-vulnerability-in-wpml-wordpress-plugin/) (CVSS score: 9.9), impacts all versions of the plugin before 4.6.13, which was released on August 20, 2024.

Arising due to missing input validation and sanitization, the issue makes it possible for authenticated attackers, with Contributor-level access and above, to execute code on the server.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

WPML is a popular plugin used for building multilingual WordPress sites. It has over one million active installations.

Security researcher stealthcopter, who discovered and reported CVE-2024-6386, said the problem lies in the plugin's handling of [shortcodes](https://wordpress.com/support/wordpress-editor/blocks/shortcode-block/) that are used to insert post content such as audio, images, and videos.

[![WPML Plugin Flaw](data:image/png;base64... "WPML Plugin Flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2gnSvU6gHJwjcno_csy6jzaeSMyRzQFDkUq2kEkWFIKbXOmMHFuggiiCwspGlhJH5_bosHBwHfBr_xnW6Y-h1CaCFOYRNjzln5iDIB0Fb3opxjmGvs8dxCrbzMJ5bTCe5tyYKE3jr_6SGuguz3E3j5afjpoxoQIrCJIQuBT19ShJM54eDZjSx2H0SWN0G/s790-rw-e365/EXPLIT.png)

"Specifically, the plugin uses Twig templates for rendering content in shortcodes but fails to properly sanitize input, leading to server-side template injection (SSTI)," the researcher [said](https://sec.stealthcopter.com/wpml-rce-via-twig-ssti/).

SSTI, as the name implies, [occurs](https://www.imperva.com/learn/application-security/server-side-template-injection-ssti/) when an attacker is able to use native template syntax to inject a malicious payload into a web template, which is then executed on the server. An attacker could then weaponize the shortcoming to execute arbitrary commands, effectively allowing them to take control of the site.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"This WPML release fixes a security vulnerability that could allow users with certain permissions to perform unauthorized actions," the plugin maintainers, OnTheGoSystems, [said](https://wpml.org/changelog/2024/08/wpml-4-6-13-and-woocommerce-multilingual-5-3-7-security-and-other-enhancements/). "This issue is unlikely to occur in real-world scenarios. It requires users to have editing permissions in WordPress, and the site must use a very specific setup."

Users of the plugin are recommended to apply the latest patches to mitigate against potential threats.

### Update

In a new post detailing the timeline of events, OnTheGoSystems said it has released WPML 4.6.13 to patch CVE-2024-6386 and WooCommerce Multilingual 5.3.7 to address a similar vulnerability that was reported by Patchstack.

It further emphasized that a successful attack requires a bad actor to have editing privileges on a WordPress site (i.e., a Contributor role and above) and that the issue has been fully resolved.

"That being said, the severity comes down to what types of users you have on your site," the company [said](https://wpml.org/announcements/2024/08/securing-wpml-with-the-help-of-our-trusted-partners-at-wordfence/). "If you and your team are the sole admins/writers/editors on the site, there's no one outside of you or your team that could exploit this vulnerability."

"On the other hand, if you're running a site with users that have Contributor-level access and you don’t know these persons personally, you might be more at risk."

*(The story was updated after publication to include additional details about the fix and its impact.)*

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

[content management system](https://thehackernews.com/search/label/content%20management%20system)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Open Source Security](https://thehackernews.com/search/label/Open%20Source%20Security)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[Web Development](https://thehackernews.com/search/label/Web%20Development)[WordPress](https://thehackernews.com/search/label/WordPress)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incide...