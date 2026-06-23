---
title: ShapedPlugin WordPress Pro Plugins Backdoored in Supply Chain Attack
url: https://thehackernews.com/2026/06/shapedplugin-wordpress-pro-plugins.html
source: The Hacker News
date: 2026-06-22
fetch_date: 2026-06-23T06:08:25.540740
---

# ShapedPlugin WordPress Pro Plugins Backdoored in Supply Chain Attack

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [ShapedPlugin WordPress Pro Plugins Backdoored in Supply Chain Attack](https://thehackernews.com/2026/06/shapedplugin-wordpress-pro-plugins.html)

**Ravie Lakshmanan**Jun 22, 2026Supply Chain Attack / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgd4DchiVkQLBMvGHgWrojoZUdyk2SwEhEj5q6cOYzKCUWF1Lz3Mxeizurg1O-SLVi2jg319ib4SJsSoVWixAkl5WLPu4rL1cMoYXUM6EziOVyt42ESt1zmMo_iLEfHx9XSAXpsDd1FEtRSgKk4AhDzA7DjJN8c__pUgogxTQgaGjsxM04WNiesgRnbEVHN/s1700-e365/wordpress-plugin.jpg)

Multiple WordPress plugins from [ShapedPlugin](https://shapedplugin.com/) were compromised in a supply chain attack after unknown threat actors managed to tamper with the official release channels and push backdoor code.

"Attackers compromised the vendor's build and distribution pipeline, injecting backdoor code into Pro plugin releases distributed through official licensed update channels," Wordfence [said](https://www.wordfence.com/blog/2026/06/psa-supply-chain-compromise-targets-shapedplugin-backdoored-pro-plugins-distributed-via-official-channels/) in an analysis published last week.

The incident affects the following plugins -

* Product Slider Pro for WooCommerce (versions before 3.5.4)
* Real Testimonials Pro (version 3.2.5)
* Smart Post Show Pro (versions before 4.0.2)

As mentioned above, it's worth emphasizing that the compromise only affects Pro plugin builds distributed through the vendor's Easy Digital Downloads (EDD) infrastructure via account.shapedplugin[.]com. The free versions of the plugins on WordPress.org are not impacted.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The supply chain compromise associated with Product Slider Pro for WooCommerce has been assigned the CVE identifier [CVE-2026-49777](https://www.cve.org/CVERecord?id=CVE-2026-49777), along with a CVSS score of 10.0, indicating maximum severity. [CVE-2026-10735](https://www.cve.org/CVERecord?id=CVE-2026-10735) (CVSS score: 9.8) is the CVE identifier for the entire incident.

The WordPress security company said the compromised versions of the plugins incorporate a loader that's triggered on every admin page, causing it to fetch a payload from a remote server ("194.76.217[.]28:2871"), install it, and activate it as a fake plugin.

Once it's activated, the malware reports the victim domain back to the server and erases itself to cover up the tracks and complicate incident response efforts. The counterfeit plugin, for its part, hides itself from the WordPress admin plugin list and is capable of capturing credentials in plaintext and two-factor authentication (2FA) codes.

It also establishes multiple persistence methods that enable arbitrary file writes via a custom REST endpoint when provided a specific authentication token, as well as drop a web shell with command execution features. Lastly, it makes use of a PHP file named "install-persistent.php," which is bundled as part of the plugin, to extract the below data -

* Full contents of wp-config.php, including database credentials, authentication keys, and debug settings
* All administrator accounts with registration dates
* Mail plugin credentials from WP Mail SMTP, Post SMTP, and Easy WP SMTP
* WooCommerce order data from the last 3 months with payment method breakdown

Once this information is displayed, the file is deleted. Evidence indicates that the attack could be a compromise of the build pipeline, as opposed to a direct poisoning of the packages.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

What's particularly dangerous about this attack is that it exposes site owners who purchased legitimate licenses and installed updates directly from the vendor's official update system to malware.

Upon being notified of the issue, ShapedPlugin has confirmed the incident, adding that it's reviewing the distribution and release processes to ensure the integrity of its products going forward. New versions of the impacted plugins are expected to be released pending comprehensive security reviews and validation tests.

Site owners who have installed the malicious versions are recommended to reset all passwords, revoke and regenerate 2FA secrets for all users, review administrator accounts for unauthorized additions, and check mail plugin configurations for modified SMTP credentials.

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

[Malware](https://thehackernews.com/search/label/Malware), [Supply Chain Attack](https://thehackernews.com/search/label/Supply%20Chain%20Attack), [Two-Factor Authentication](https://thehackernews.com/search/label/Two-Factor%20Authentication), [Web Shell](https://thehackernews.com/search/label/Web%20Shell), [WooCommerce](https://thehackernews.com/search/label/WooCommerce), [Wordfence](https://thehackernews.com/search/label/Wordfence), [WordPress](https://thehackernews.com/search/label/WordPress)

⚡ Top Stories This Week

[![Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now](data:image/svg+xml;base64... "Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now")

Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Pat...