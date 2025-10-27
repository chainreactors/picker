---
title: Critical Security Flaw Found in LiteSpeed Cache Plugin for WordPress
url: https://thehackernews.com/2024/09/critical-security-flaw-found-in.html
source: The Hacker News
date: 2024-09-07
fetch_date: 2025-10-06T18:31:48.882109
---

# Critical Security Flaw Found in LiteSpeed Cache Plugin for WordPress

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

# [Critical Security Flaw Found in LiteSpeed Cache Plugin for WordPress](https://thehackernews.com/2024/09/critical-security-flaw-found-in.html)

**Sep 06, 2024**Ravie LakshmananWordPress / Webinar Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqQSpPMGyIKr93U-s5wnbjTCCdtaYQIRbD5OgwB7QOCXLBgt9dpooR4vyuZIb9DYfte4rkxeiG-WpkBUnZMgozRTLtXq0EqN_bBf_KLtEPCPDMmWIRa0FhQUz2D2szGP_yfBQM1pKQX6uqmY74U8wfKyU4D8oWVufd_DBKhV_TOpqesKZD6Za0_fCcrP8Q/s790-rw-e365/lightspeed.jpg)

Cybersecurity researchers have discovered yet another critical security flaw in the LiteSpeed Cache plugin for WordPress that could allow unauthenticated users to take control of arbitrary accounts.

The vulnerability, tracked as CVE-2024-44000 (CVSS score: 7.5), impacts versions before and including 6.4.1. It has been addressed in version 6.5.0.1.

"The plugin suffers from an unauthenticated account takeover vulnerability which allows any unauthenticated visitor to gain authentication access to any logged-in users and at worst can gain access to an Administrator level role after which malicious plugins could be uploaded and installed," Patchstack researcher Rafie Muhammad [said](https://patchstack.com/articles/critical-account-takeover-vulnerability-patched-in-litespeed-cache-plugin/).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The discovery follows an extensive security analysis of the plugin, which previously led to the identification of a critical privilege escalation flaw ([CVE-2024-28000](https://thehackernews.com/2024/08/critical-flaw-in-wordpress-litespeed.html), CVSS score: 9.8). LiteSpeed Cache is a popular caching plugin for the WordPress ecosystem with over 5 million active installations.

The new vulnerability stems from the fact that a debug log file named "/wp-content/debug.log" is publicly exposed, which makes it possible for unauthenticated attackers to view potentially sensitive information contained in the file.

This could also include user cookie information present within HTTP response headers, effectively allowing users to log in to a vulnerable site with any session that is actively valid.

The lower severity of the flaw is owing to the prerequisite that the debug feature must be enabled on a WordPress site for it to be successful. Alternatively, it could also affect sites that had activated the debug log feature at some point in the past, but have failed to remove the debug file.

It's important to note that this feature is disabled by default. The patch addresses the problem by moving the log file to a dedicated folder within the LiteSpeed plugin folder ("/wp-content/litespeed/debug/"), randomizing filenames, and dropping the option to log cookies in the file.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Users are advised to check their installations for the presence of the "/wp-content/debug.log" and take steps to purge them if the debugging feature has (or had) been enabled.

It's also recommended to set an .htaccess rule to deny direct access to the log files as malicious actors can still directly access the new log file if they know the new filename by means of a trial-and-error method.

"This vulnerability highlights the critical importance of ensuring the security of performing a debug log process, what data should not be logged, and how the debug log file is managed," Muhammad said.

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

[account takeover](https://thehackernews.com/search/label/account%20takeover)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data protection](https://thehackernews.com/search/label/data%20protection)[LiteSpeed](https://thehackernews.com/search/label/LiteSpeed)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[website security](https://thehackernews.com/search/label/website%20security)[WordPress](https://thehackernews.com/search/label/WordPress)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking...