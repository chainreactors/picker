---
title: Critical WordPress Anti-Spam Plugin Flaws Expose 200,000+ Sites to Remote Attacks
url: https://thehackernews.com/2024/11/critical-wordpress-anti-spam-plugin.html
source: The Hacker News
date: 2024-11-27
fetch_date: 2025-10-06T19:28:43.404003
---

# Critical WordPress Anti-Spam Plugin Flaws Expose 200,000+ Sites to Remote Attacks

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

# [Critical WordPress Anti-Spam Plugin Flaws Expose 200,000+ Sites to Remote Attacks](https://thehackernews.com/2024/11/critical-wordpress-anti-spam-plugin.html)

**Nov 26, 2024**Ravie LakshmananVulnerability / Website Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgBq63hh3kO_bENYYcgiz4X7yiRISaxrwuXuoMB_SzGTLPgdWCgmaomPXmd_21D9RbO_mBI693ST63F4T2eLaVl53R_g758zgj0Ilo56bV18BMpzOzPxDJcTdMlib8pHGt3Wft3ogn0wJe3VOB4K-w9sXzHTLEZO7HmNSZHWz51HB1hLyVlCbVu7Sr5jKm/s790-rw-e365/wordpress.png)

Two critical security flaws impacting the Spam protection, Anti-Spam, and FireWall plugin for WordPress could allow an unauthenticated attacker to install and enable malicious plugins on susceptible sites and potentially achieve remote code execution.

The vulnerabilities, tracked as **CVE-2024-10542** and **CVE-2024-10781**, carry a CVSS score of 9.8 out of a maximum of 10.0. They were addressed in versions 6.44 and 6.45 released this month.

Installed on over 200,000 WordPress sites, CleanTalk's Spam protection,f Anti-Spam, FireWall plugin is [advertised](https://wordpress.org/plugins/cleantalk-spam-protect/) as a "universal anti-spam plugin" that blocks spam comments, registrations, surveys, and more.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

According to Wordfence, both vulnerabilities concern an authorization bypass issue that could allow a malicious actor to install and activate arbitrary plugins. This could then pave the way for remote code execution if the activated plugin is vulnerable of its own.

The plugin is "vulnerable to unauthorized Arbitrary Plugin Installation due to a missing empty value check on the 'api\_key' value in the 'perform' function in all versions up to, and including, 6.44," security researcher István Márton [said](https://www.wordfence.com/blog/2024/11/200000-wordpress-sites-affected-by-unauthenticated-critical-vulnerabilities-in-anti-spam-by-cleantalk-wordpress-plugin/), referring to CVE-2024-10781.

On the other hand, CVE-2024-10542 stems from an authorization bypass via reverse DNS spoofing on the checkWithoutToken() function.

Regardless of the bypass method, successful exploitation of the two shortcomings could allow an attacker to install, activate, deactivate, or even uninstall plugins.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Users of the plugin are advised to ensure that their sites are updated to the latest patched version to safeguard against potential threats.

The development comes as Sucuri has warned of [multiple](https://blog.sucuri.net/2024/10/indonesian-gambling-redirect-hiding-in-plain-sight.html) [campaigns](https://blog.sucuri.net/2024/11/simple-include-statement-hides-casino-spam.html) that are leveraging compromised WordPress sites to inject malicious code responsible for [redirecting site visitors](https://blog.sucuri.net/2024/10/rogue-ads-redirect-visitors.html) to other sites via bogus ads, [skimming login credentials](https://blog.sucuri.net/2024/11/malware-steals-account-credentials.html), as well as [dropping malware](https://blog.sucuri.net/2024/11/php-reinfector-and-backdoor-malware-target-wordpress-sites.html) that captures admin passwords, redirects to [VexTrio Viper scam sites](https://thehackernews.com/2024/01/vextrio-uber-of-cybercrime-brokering.html), and executes arbitrary PHP code on the server.

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

[Anti-Spam](https://thehackernews.com/search/label/Anti-Spam)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Firewall](https://thehackernews.com/search/label/Firewall)[Patch Management](https://thehackernews.com/search/label/Patch%20Management)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[WordPress](https://thehackernews.com/search/label/WordPress)[WordPress plugin](https://thehackernews.com/search/label/WordPress%20plugin)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Th...