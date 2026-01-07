---
title: Unpatched Firmware Flaw Exposes TOTOLINK EX200 to Full Remote Device Takeover
url: https://thehackernews.com/2026/01/unpatched-firmware-flaw-exposes.html
source: The Hacker News
date: 2026-01-06
fetch_date: 2026-01-07T03:30:45.185603
---

# Unpatched Firmware Flaw Exposes TOTOLINK EX200 to Full Remote Device Takeover

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

# [Unpatched Firmware Flaw Exposes TOTOLINK EX200 to Full Remote Device Takeover](https://thehackernews.com/2026/01/unpatched-firmware-flaw-exposes.html)

**Jan 06, 2026**Ravie LakshmananIoT Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyTFwLjAZvcGODxR0B7hv5Irv_LIjhCSSiF42fD71qFULdTLWFdJzYSWaMPwXThxT7CocXe9IdvNCU6-9F5fwrHyNMN9AjbhpOLxOzUXDFYHO0Uaypv6wTJ9O4vOmbC_OfBTwBvvXFHAQfTWg4Q_dM5aelJtqTPy7HkRl2E8q1D9bx6hoa1PKMkUkxTqsw/s790-rw-e365/totolink.jpg)

The CERT Coordination Center (CERT/CC) has disclosed details of an unpatched security flaw impacting TOTOLINK EX200 wireless range extender that could allow a remote authenticated attacker to gain full control of the device.

The flaw, **CVE-2025-65606** (CVSS score: N/A), has been characterized as a flaw in the firmware-upload error-handling logic, which could cause the device to inadvertently start an unauthenticated root-level telnet service. CERT/CC credited Leandro Kogan for discovering and reporting the issue.

"An authenticated attacker can trigger an error condition in the firmware-upload handler that causes the device to start an unauthenticated root telnet service, granting full system access," CERT/CC [said](https://kb.cert.org/vuls/id/295169).

Successful exploitation of the flaw requires an attacker to be already authenticated to the web management interface to access the firmware-upload functionality.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

CERT/CC said the firmware-upload handler enters an "abnormal error state" when certain malformed firmware files are processed, causing the device to launch a telnet service with root privileges and without requiring any authentication.

This unintended remote administration interface could be exploited by the attacker to hijack susceptible devices, leading to configuration manipulation, arbitrary command execution, or persistence.

According to CERT/CC, TOTOLINK has not released any patches to address the flaw, and the product is said to be no longer actively maintained. TOTOLINK's web page for EX200 shows that the firmware for the product was [last updated](https://www.totolink.net/home/menu/detail/menu_listtpl/download/id/144/ids/36.html) in February 2023.

In the absence of a fix, users of the appliance are advised to restrict administrative access to trusted networks, prevent unauthorized users from accessing the management interface, monitor for anomalous activity, and upgrade to a supported model.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[firmware](https://thehackernews.com/search/label/firmware)[iot security](https://thehackernews.com/search/label/iot%20security)[network security](https://thehackernews.com/search/label/network%20security)[privilege escalation](https://thehackernews.com/search/label/privilege%20escalation)[router security](https://thehackernews.com/search/label/router%20security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide](data:image/svg+xml;base64... "DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide")

DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide](https://thehackernews.com/2025/12/darkspectre-browser-extension-campaigns.html)

[![CSA Issues Alert on Critical SmarterMail Bug Allowing Remote Code Execution](data:image/svg+xml;base64... "CSA Issues Alert on Critical SmarterMail Bug Allowing Remote Code Execution")

CSA Issues Alert on Critical SmarterMail Bug Allowing Remote Code Execution](https://thehackernews.com/2025/12/csa-issues-alert-on-critical.html)

[![⚡ Weekly Recap: MongoDB Attacks, Wallet Breaches, Android Spyware, Insider Crime and More](data:image/svg+xml;base64... "⚡ Weekly Recap: MongoDB Attacks, Wallet Breaches, Android Spyware, Insider Crime and More")

⚡ Weekly Recap: MongoDB Attacks, Wallet Breaches, Android Spyware, Insider Crime and More](https://thehackernews.com/2025/12/weekly-recap-mongodb-attacks-wallet.html)

[![MongoDB Vulnerability CVE-2025-14847 Under Active Exploitation Worldwide](data:image/svg+xml;base64... "MongoDB Vulnerability CVE-2025-14847 Under Active Exploitation Worldwide")

MongoDB Vulnerability CVE-2025-14847 Under Active Exploitation Worldwide](https://thehackernews.com/2025/12/mongodb-vulnerability-cve-2025-14847.html)

[![Trust Wallet Chrome Extension Breach Caused $7 Million Crypto Loss via Malicious Code](data:image/svg+xml;base64... "Trust Wallet Chrome Extension Breach Caused $7 Million Crypto Loss via Malicious Code")

Trust Wallet Chrome Extension Breach Caused $7 Million Crypto Loss via Malicious Code](https://thehackernews.com/2025/12/trust-wallet-chrome-extension-bug.html)

[![Critical LangChain Core Vulnerability Exposes Secrets via Serialization Injection](data:image/svg+xml;base64... "Critical LangChain Core Vulnerability Exposes Secrets via Serialization Injection")

Critical LangChain Core Vulnerability Exposes Secrets via Serialization I...