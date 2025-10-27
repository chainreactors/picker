---
title: Samsung Galaxy Store App Found Vulnerable to Sneaky App Installs and Fraud
url: https://thehackernews.com/2023/01/samsung-galaxy-store-app-found.html
source: The Hacker News
date: 2023-01-24
fetch_date: 2025-10-04T04:40:50.876584
---

# Samsung Galaxy Store App Found Vulnerable to Sneaky App Installs and Fraud

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

# [Samsung Galaxy Store App Found Vulnerable to Sneaky App Installs and Fraud](https://thehackernews.com/2023/01/samsung-galaxy-store-app-found.html)

**Jan 23, 2023**Ravie LakshmananMobile Hacking / App Security

[![Samsung Galaxy Store App](data:image/png;base64... "Samsung Galaxy Store App")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEji98eYw9apF-u-Jg2Wbzo1bUhYD2KGTOc9gnywEsiO_ORnHTF-YQE0OOQf2Cprc5nHA1S2-8s_aRlR5gFZlnrpZLj4GU7YRsNaJsl1uych-kV2Hl21KZxiIGsV6z4c8emKueWgVJMH_fEL2EVXx0lr7nYlBeVxH-ATUM1FiZDMRc-WHua7aWr1rGCx/s790-rw-e365/samsung-galay-store.jpg)

Two security flaws have been disclosed in Samsung's Galaxy Store app for Android that could be exploited by a local attacker to stealthily install arbitrary apps or direct prospective victims to fraudulent landing pages on the web.

The issues, tracked as **CVE-2023-21433 and CVE-2023-21434**, were [discovered](https://research.nccgroup.com/2023/01/20/technical-advisory-multiple-vulnerabilities-in-the-galaxy-app-store-cve-2023-21433-cve-2023-21434/) by NCC Group and notified to the South Korean chaebol in November and December 2022. Samsung [classified](https://security.samsungmobile.com/serviceWeb.smsb) the bugs as moderate risk and released fixes in version 4.5.49.8 shipped earlier this month.

Samsung Galaxy Store, previously known as Samsung Apps and Galaxy Apps, is a dedicated app store used for Android devices manufactured by Samsung. It was launched in September 2009.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The first of the two vulnerabilities is CVE-2023-21433, which could enable an already installed rogue Android app on a Samsung device to install any application available on the Galaxy Store.

Samsung described it as a case of improper access control that it said has been patched with proper permissions to prevent unauthorized access.

It's worth noting here that the shortcoming only impacts Samsung devices that are running Android 12 and before, and does not affect those that are on the latest version (Android 13).

The second vulnerability, CVE-2023-21434, relates to an instance of improper input validation that occurs when limiting the list of domains that could be launched as a [WebView](https://developer.android.com/reference/android/webkit/WebView) from within the app, effectively enabling a threat actor to bypass the filter and browse to a domain under their control.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Either tapping a malicious hyperlink in Google Chrome or a pre-installed rogue application on a Samsung device can bypass Samsung's URL filter and launch a webview to an attacker controlled domain," NCC Group researcher Ken Gannon said.

The update comes as Samsung rolled out security updates for the month of January 2023 to [remediate several flaws](https://security.samsungmobile.com/securityUpdate.smsb), some of which could be exploited to modify carrier network parameters, control BLE advertising without permission, and achieve arbitrary code execution.

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

[App Store](https://thehackernews.com/search/label/App%20Store)[Malware](https://thehackernews.com/search/label/Malware)[mobile hacking](https://thehackernews.com/search/label/mobile%20hacking)[NCC Group](https://thehackernews.com/search/label/NCC%20Group)[Samsung](https://thehackernews.com/search/label/Samsung)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html)

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](data:image/svg+xml;base64... "Fortra GoAnywhere CVSS 10 F...