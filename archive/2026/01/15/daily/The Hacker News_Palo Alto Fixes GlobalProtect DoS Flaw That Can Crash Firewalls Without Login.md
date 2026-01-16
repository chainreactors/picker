---
title: Palo Alto Fixes GlobalProtect DoS Flaw That Can Crash Firewalls Without Login
url: https://thehackernews.com/2026/01/palo-alto-fixes-globalprotect-dos-flaw.html
source: The Hacker News
date: 2026-01-15
fetch_date: 2026-01-16T03:30:39.861274
---

# Palo Alto Fixes GlobalProtect DoS Flaw That Can Crash Firewalls Without Login

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [Palo Alto Fixes GlobalProtect DoS Flaw That Can Crash Firewalls Without Login](https://thehackernews.com/2026/01/palo-alto-fixes-globalprotect-dos-flaw.html)

**Jan 15, 2026**Ravie LakshmananNetwork Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYIgBhmpBELPnR-WkdX1gKhf8lt6aLh_vFl7l4w8GVDOFcvbF8Vwrvt0vTwAqX5q51ybv3o8qPzMre3pF1PwDCnX0aYUmKBKHusgttSMK07Pbh20nSIq4hqwA_1dumI3Jhop44Dxh1uUkCzg-9CRT7b3BrWLGfgAyVP9o65XkuRkUASszfh1ljMyr-aiDP/s790-rw-e365/paloalto.jpg)

Palo Alto Networks has released security updates for a high-severity security flaw impacting GlobalProtect Gateway and Portal, for which it said there exists a proof-of-concept (PoC) exploit.

The vulnerability, tracked as **CVE-2026-0227** (CVSS score: 7.7), has been described as a denial-of-service (DoS) condition impacting GlobalProtect PAN-OS software arising as a result of an improper check for exceptional conditions ([CWE-754](https://cwe.mitre.org/data/definitions/754))

"A vulnerability in Palo Alto Networks PAN-OS software enables an unauthenticated attacker to cause a denial-of-service (DoS) to the firewall," the company [said](https://security.paloaltonetworks.com/CVE-2026-0227) in an advisory released Wednesday. "Repeated attempts to trigger this issue result in the firewall entering into maintenance mode."

The issue, discovered and reported by an unnamed external researcher, affects the following versions -

* PAN-OS 12.1 < 12.1.3-h3, < 12.1.4
* PAN-OS 11.2 < 11.2.4-h15, < 11.2.7-h8, < 11.2.10-h2
* PAN-OS 11.1 < 11.1.4-h27, < 11.1.6-h23, < 11.1.10-h9, < 11.1.13
* PAN-OS 10.2 < 10.2.7-h32, < 10.2.10-h30, < 10.2.13-h18, < 10.2.16-h6, < 10.2.18-h1
* PAN-OS 10.1 < 10.1.14-h20
* Prisma Access 11.2 < 11.2.7-h8
* Prisma Access 10.2 < 10.2.10-h29

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

Palo Alto Networks also clarified that the vulnerability is applicable only to PAN-OS NGFW or Prisma Access configurations with an enabled GlobalProtect gateway or portal. The company's Cloud Next-Generation Firewall (NGFW) is not impacted. There are no workarounds to mitigate the flaw.

While there is no evidence that the vulnerability has been exploited in the wild, it's essential to keep the devices up-to-date, especially given that exposed GlobalProtect gateways have [witnessed](https://thehackernews.com/2025/10/scanning-activity-on-palo-alto-networks.html) repeated [scanning activity](https://thehackernews.com/2025/12/threatsday-bulletin-spyware-alerts.html#globalprotect-scans-spike) over the [past year](https://thehackernews.com/2025/12/cisco-warns-of-active-attacks.html).

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[denial of service](https://thehackernews.com/search/label/denial%20of%20service)[Firewall](https://thehackernews.com/search/label/Firewall)[network security](https://thehackernews.com/search/label/network%20security)[Palo Alto Networks](https://thehackernews.com/search/label/Palo%20Alto%20Networks)[PAN-OS](https://thehackernews.com/search/label/PAN-OS)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide](data:image/svg+xml;base64... "DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide")

DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide](https://thehackernews.com/2025/12/darkspectre-browser-extension-campaigns.html)

[![⚡ Weekly Recap: IoT Exploits, Wallet Breaches, Rogue Extensions, AI Abuse and More](data:image/svg+xml;base64... "⚡ Weekly Recap: IoT Exploits, Wallet Breaches, Rogue Extensions, AI Abuse and More")

⚡ Weekly Recap: IoT Exploits, Wallet Breaches, Rogue Extensions, AI Abuse and More](https://thehackernews.com/2026/01/weekly-recap-iot-exploits-wallet.html)

[![Kimwolf Android Botnet Infects Over 2 Million Devices via Exposed ADB and Proxy Networks](data:image/svg+xml;base64... "Kimwolf Android Botnet Infects Over 2 Million Devices via Exposed ADB and Proxy Networks")

Kimwolf Android Botnet Infects Over 2 Million Devices via Exposed ADB and Proxy Networks](https://thehackernews.com/2026/01/kimwolf-android-botnet-infects-over-2.html)

[![New n8n Vulnerability (9.9 CVSS) Lets Authenticated Users Execute System Commands](data:image/svg+xml;base64... "New n8n Vulnerability (9.9 CVSS) Lets Authenticated Users Execute System Commands")

New n8n Vulnerability (9.9 CVSS) Lets Authenticated Users Execute System Commands](https://thehackernews.com/2026/01/new-n8n-vulnerability-99-cvss-lets.html)

[![Fake Booking Emails Redirect Hotel Staff to Fake BSoD Pages Delivering DCRat](data:image/svg+xml;base64... "Fake Booking Emails Redirect Hotel Staff to Fake BSoD Pages Delivering DCRat")

Fake Booking Emails Redirect Hotel Staff to Fake BSoD Pages Delivering DCRat](https://thehackernews.com/2026/01/fake-booking-emails-redirect-hotel.html)

[![Two Chrome Extensions Caught Stealing ChatGP...