---
title: Trend Micro Apex Central RCE Flaw Scores 9.8 CVSS in On-Prem Windows Versions
url: https://thehackernews.com/2026/01/trend-micro-apex-central-rce-flaw.html
source: The Hacker News
date: 2026-01-09
fetch_date: 2026-01-10T03:33:07.332540
---

# Trend Micro Apex Central RCE Flaw Scores 9.8 CVSS in On-Prem Windows Versions

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

# [Trend Micro Apex Central RCE Flaw Scores 9.8 CVSS in On-Prem Windows Versions](https://thehackernews.com/2026/01/trend-micro-apex-central-rce-flaw.html)

**Jan 09, 2026**Ravie LakshmananVulnerability / Endpoint Security

[![Trend Micro Apex Central](data:image/png;base64... "Trend Micro Apex Central")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0g-pVmmuKjF27CaQySVEJl4oMN20t271uPWVmcHbp8d_gF6yHehH-MvQAsQJ6H6-S9POiKFiUQUfjBIpbgQ8pP8ERTQK-tVtNAhrhTE8qWaNW8wAnE26o8eDpZrWHzsLdktcyS9Wrei5cx2FYVhnbJkUuWss7SSP2khMfwODaOWBxXnR5OsUvsZlBuToN/s790-rw-e365/trendmicro.jpg)

Trend Micro has [released](https://success.trendmicro.com/en-US/solution/KA-0022071) security updates to address multiple security vulnerabilities impacting on-premise versions of Apex Central for Windows, including a critical bug that could result in arbitrary code execution.

The vulnerability, tracked as **CVE-2025-69258**, carries a CVSS score of 9.8 out of a maximum of 10.0. The vulnerability has been described as a case of remote code execution affecting LoadLibraryEX.

"A LoadLibraryEX vulnerability in Trend Micro Apex Central could allow an unauthenticated remote attacker to load an attacker-controlled DLL into a key executable, leading to execution of attacker-supplied code under the context of SYSTEM on affected installations," the cybersecurity company said.

Also patched by Trend Micro are two other flaws -

* **CVE-2025-69259** (CVSS score: 7.5) - A message unchecked NULL return value vulnerability in Trend Micro Apex Central could allow a remote, unauthenticated attacker to create a denial-of-service condition on affected installations
* **CVE-2025-69260** (CVSS score: 7.5) - A message out-of-bounds read vulnerability in Trend Micro Apex Central could allow a remote, unauthenticated attacker to create a denial-of-service condition on affected installations

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

Tenable, which is credited with identifying and reporting all three flaws in August 2025, [said](https://www.tenable.com/security/research/tra-2026-01) an attacker can exploit CVE-2025-69258 by sending a message "0x0a8d" ("SC\_INSTALL\_HANDLER\_REQUEST") to the MsgReceiver.exe component, causing a DLL under their control to be loaded into the binary, resulting in code execution with elevated privileges.

Similarly, CVE-2025-69259 and CVE-2025-69260 can also be triggered by sending a specially crafted message "0x1b5b" ("SC\_CMD\_CGI\_LOG\_REQUEST") to the MsgReceiver.exe process, which listens on the default TCP port 20001.

The issues impact Apex Central on-premise versions below Build 7190. Trend Micro noted that successful exploitation hinges on an attacker already having physical or remote access to a vulnerable endpoint.

"In addition to timely application of patches and updated solutions, customers are also advised to review remote access to critical systems and ensure policies and perimeter security are up-to-date," it added.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[denial of service](https://thehackernews.com/search/label/denial%20of%20service)[endpoint security](https://thehackernews.com/search/label/endpoint%20security)[network security](https://thehackernews.com/search/label/network%20security)[Patch Management](https://thehackernews.com/search/label/Patch%20Management)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Trend Micro](https://thehackernews.com/search/label/Trend%20Micro)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide](data:image/svg+xml;base64... "DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide")

DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide](https://thehackernews.com/2025/12/darkspectre-browser-extension-campaigns.html)

[![⚡ Weekly Recap: IoT Exploits, Wallet Breaches, Rogue Extensions, AI Abuse and More](data:image/svg+xml;base64... "⚡ Weekly Recap: IoT Exploits, Wallet Breaches, Rogue Extensions, AI Abuse and More")

⚡ Weekly Recap: IoT Exploits, Wallet Breaches, Rogue Extensions, AI Abuse and More](https://thehackernews.com/2026/01/weekly-recap-iot-exploits-wallet.html)

[![Kimwolf Android Botnet Infects Over 2 Million Devices via Exposed ADB and Proxy Networks](data:image/svg+xml;base64... "Kimwolf Android Botnet Infects Over 2 Million Devices via Exposed ADB and Proxy Networks")

Kimwolf Android Botnet Infects Over 2 Million Devices via Exposed ADB and Proxy Networks](https://thehackernews.com/2026/01/kimwolf-android-botnet-infects-over-2.html)

[![New n8n Vulnerability (9.9 CVSS) Lets Authenticated Users Execute System Commands](data:image/svg+xml;base64... "New n8n Vulnerability (9.9 CVSS) Lets Authenticated Users Execute System Commands")

New n8n Vulnerability (9.9 CVSS) Lets Authenticated Users Execute System Commands](https://thehackernews.com/2026/01/new-n8n-vulnerability-99-cvss-lets.html)

[![Fake Booking Emails Redirect Hotel St...