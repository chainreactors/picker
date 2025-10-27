---
title: WordPress Admins Urged to Remove miniOrange Plugins Due to Critical Flaw
url: https://thehackernews.com/2024/03/wordpress-admins-urged-to-remove.html
source: The Hacker News
date: 2024-03-19
fetch_date: 2025-10-04T12:13:06.265380
---

# WordPress Admins Urged to Remove miniOrange Plugins Due to Critical Flaw

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

# [WordPress Admins Urged to Remove miniOrange Plugins Due to Critical Flaw](https://thehackernews.com/2024/03/wordpress-admins-urged-to-remove.html)

**Mar 18, 2024**Ravie LakshmananWebsite Security / Vulnerability

[![WordPress miniOrange Plugins](data:image/png;base64... "WordPress miniOrange Plugins")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjfvWGErVuRNDBhvqZZ5XnRdZBdZmn4SMXA6OmJfgiRqsOqSW1CvoHuc7ZpUvqGUxlxgP_t5w1n-CwZDGASSjpnaiP3TxF2O1a04-yBX8uFmOCp0rnJ1VuhwC_bGd7ODxDrwl5dotlJzVtRHeGth12ivF4TwXiVqZ20PweBuyK-iXURsE_DDv-aJPd4lgd9/s790-rw-e365/mini.jpg)

WordPress users of miniOrange's Malware Scanner and Web Application Firewall plugins are being urged to delete them from their websites following the discovery of a critical security flaw.

The flaw, tracked as **CVE-2024-2172**, is rated 9.8 out of a maximum of 10 on the CVSS scoring system and discovered by [Stiofan](https://wpgeodirectory.com/). It impacts the following versions of the two plugins -

* [Malware Scanner](https://wordpress.org/plugins/miniorange-malware-protection/) (versions <= 4.7.2)
* [Web Application Firewall](https://wordpress.org/plugins/web-application-firewall/) (versions <= 2.1.1)

It's worth noting that the plugins have been permanently closed by the maintainers as of March 7, 2024. While Malware Scanner has over 10,000 active installs, Web Application Firewall has more than 300 active installations.

"This vulnerability makes it possible for an unauthenticated attacker to grant themselves administrative privileges by updating the user password," Wordfence [reported](https://www.wordfence.com/blog/2024/03/critical-vulnerability-remains-unpatched-in-two-permanently-closed-miniorange-wordpress-plugins-1250-bounty-awarded/) last week.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The issue is the result of a missing capability check in the function mo\_wpns\_init() that enables an unauthenticated attacker to arbitrarily update any user's password and escalate their privileges to that of an administrator, potentially leading to a complete compromise of the site.

"Once an attacker has gained administrative user access to a WordPress site they can then manipulate anything on the targeted site as a normal administrator would," Wordfence said.

"This includes the ability to upload plugin and theme files, which can be malicious zip files containing backdoors, and modify posts and pages which can be leveraged to redirect site users to other malicious sites or inject spam content."

The development comes as the WordPress security company warned of a similar high-severity privilege escalation flaw in the RegistrationMagic plugin (CVE-2024-1991, CVSS score: 8.8) affecting all versions, including and prior to 5.3.0.0.

The issue, addressed on March 11, 2024, with the release of version 5.3.1.0, permits an authenticated attacker to grant themselves administrative privileges by updating the user role. The plugin has more than 10,000 active installations.

"This vulnerability allows authenticated threat actors with subscriber-level permissions or higher to elevate their privileges to that of a site administrator which could ultimately lead to complete site compromise," István Márton [said](https://www.wordfence.com/blog/2024/03/1313-bounty-awarded-for-privilege-escalation-vulnerability-patched-in-registrationmagic-wordpress-plugin/).

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[malware scanner](https://thehackernews.com/search/label/malware%20scanner)[privilege escalation](https://thehackernews.com/search/label/privilege%20escalation)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[Web Application Firewall](https://thehackernews.com/search/label/Web%20Application%20Firewall)[Wordfence](https://thehackernews.com/search/label/Wordfence)[WordPress](https://thehackernews.com/search/label/WordPress)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Li...