---
title: Hackers Deploy Stealth Backdoor in WordPress Mu-Plugins to Maintain Admin Access
url: https://thehackernews.com/2025/07/hackers-deploy-stealth-backdoor-in.html
source: The Hacker News
date: 2025-07-25
fetch_date: 2025-10-06T23:53:55.066723
---

# Hackers Deploy Stealth Backdoor in WordPress Mu-Plugins to Maintain Admin Access

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

# [Hackers Deploy Stealth Backdoor in WordPress Mu-Plugins to Maintain Admin Access](https://thehackernews.com/2025/07/hackers-deploy-stealth-backdoor-in.html)

**Jul 24, 2025**Ravie LakshmananCybersecurity / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi32X_LS5gqdsd_K9A_mm4w6k0aHQK1bd0RJHLt2kRkNQDSE7V8qwPEaQc1nTuYek34jHjaKqxY6IYtwV7FzxK5Z6HYlPBTx2UMjTxXJG0ZIHIyWAv_mJ9BA2xRHRw8lvmh3zyeIUWLuMVkxNAYoJ4_AhNvUTlD3SNhJEtmEEWegNJR3OPV0UJzX2w7zqvH/s790-rw-e365/WordPress.jpg)

Cybersecurity researchers have uncovered a new stealthy backdoor concealed within the "mu-plugins" directory in WordPress sites to grant threat actors persistent access and allow them to perform arbitrary actions.

Must-use plugins (aka mu-plugins) are [special plugins](https://developer.wordpress.org/advanced-administration/plugins/mu-plugins/) that are automatically activated on all WordPress sites in the installation. They are located in the "wp-content/mu-plugins" directory by default.

What makes them an [attractive option for attackers](https://thehackernews.com/2025/03/hackers-exploit-wordpress-mu-plugins-to.html) is that mu-plugins do not show in the default list of plugins on the Plugins page of wp-admin and cannot be disabled except by removing the plugin file from the must-use directory.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

As a result, a piece of malware that leverages this technique allows it to function quietly, without raising any red flags.

In the infection spotted by web security company Sucuri, the PHP script in the mu-plugins directory ("wp-index.php") serves as a loader to fetch a next-stage payload and save it in the WordPress database within the [wp\_options table](https://codex.wordpress.org/Database_Description#Table:_wp_options) under \_hdra\_core.

The remote payload is retrieved from a URL that's obfuscated using [ROT13](https://en.wikipedia.org/wiki/ROT13), a simple substitution cipher that replaces a letter with the 13th letter after it (i.e., A becomes N, B becomes O, C becomes P, and so forth).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhsoXcKMroM0WlXTIWEff1xSltVFSzR6xxvjD-yDK_6zgX3A1vNKAmp2fXL7vc3r1CBmkZsevYnI55SarrgdzYHW8XkWv-KhE6joPMuEkGIbVuXhrMyVr0_veMMbkKbmAyZSA-zd3Hn3uePiEgEf1X5c_LB4eNQsX8VDSpbvIdu6R-_zhS7GNZex6iUIjLH/s790-rw-e365/bot.png)

"The fetched content is then temporarily written to disk and executed," security researcher Puja Srivastava [said](https://blog.sucuri.net/2025/07/uncovering-a-stealthy-wordpress-backdoor-in-mu-plugins.html). "This backdoor gives the attacker persistent access to the site and the ability to run any PHP code remotely.

Specifically, it injects a hidden file manager into the theme directory as "pricing-table-3.php," permitting threat actors to browse, upload, or delete files. It also creates an administrator user named "officialwp" and then downloads a malicious plugin ("wp-bot-protect.php") and activates it.

Besides reinstating the infection in the event of deletion, the malware incorporates the ability to change the passwords of common administrator usernames, such as "admin," "root," and "wpsupport," to a default password set by the attacker. This also extends to its own "officialwp" user.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

In doing so, the threat actors can enjoy persistent access to the sites and perform malicious actions, while effectively locking out other administrators. This can range from data theft to injecting code that can serve malware to site visitors or redirect them to other scammy sites.

"The attackers gain full administrator access and a persistent backdoor, allowing them to do anything on the site, from installing more malware to defacing it," Srivastava said. "The remote command execution and content injection features mean the attackers can change the malware's behavior."

To mitigate against these threats, it's essential that site owners update WordPress, themes, and plugins periodically, secure accounts using two-factor authentication, and regularly audit all sections of the site, including theme and plugin files.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[PHP](https://thehackernews.com/search/label/PHP)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Sucuri](https://thehackernews.com/search/label/Sucuri)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[web security](https://thehackernews.com/search/label/web%20security)[website defacement](https://thehackernews.com/search/label/website%20defacement)[WordPress](https://thehackernews.com/search/label/WordPress)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Co...