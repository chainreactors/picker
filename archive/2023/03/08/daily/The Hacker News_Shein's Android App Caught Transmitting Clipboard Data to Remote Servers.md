---
title: Shein's Android App Caught Transmitting Clipboard Data to Remote Servers
url: https://thehackernews.com/2023/03/sheins-android-app-caught-transmitting.html
source: The Hacker News
date: 2023-03-08
fetch_date: 2025-10-04T08:58:03.947151
---

# Shein's Android App Caught Transmitting Clipboard Data to Remote Servers

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

# [Shein's Android App Caught Transmitting Clipboard Data to Remote Servers](https://thehackernews.com/2023/03/sheins-android-app-caught-transmitting.html)

**Mar 07, 2023**Ravie LakshmananPrivacy / Data Breach

[![Shein Android](data:image/png;base64... "Shein Android")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqFSyAjx7LzBBQ0D-0qOlJBRJbVTRHJMcMAkXOIAbMn3XfqfNvCsK0s2qiGVy7I7ZEZEqwONvYZztL4xnarkx9mDzPK09mLvwkPhaEpMO4TJAIPbJWF4jXLd93-d2WLo1w0au3ck49bgR5n20W5vJhfZUqf8fbD_CQNlRf8QMRyuunbxK0fHaljijn/s790-rw-e365/shein.png)

An older version of Shein's [Android application](https://play.google.com/store/apps/details?id=com.zzkko&hl=en&gl=US) suffered from a bug that periodically captured and transmitted clipboard contents to a remote server.

The Microsoft 365 Defender Research Team said it [discovered](https://www.virustotal.com/gui/file/ff07dc6e237acd19cb33e35c60cb2ae52c460aac76bc27116d8de76abec66c51/details) the problem in [version 7.9.2](https://www.appbrain.com/app/shein-fashion-shopping-online/com.zzkko) of the app that was released on December 16, 2021. The issue has since been addressed as of May 2022.

Shein, originally named ZZKKO, is a Chinese online fast fashion retailer based in Singapore. The app, which is currently at version 9.0.0, has over 100 million downloads on the Google Play Store.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The tech giant [said](https://www.microsoft.com/en-us/security/blog/2023/03/06/protecting-android-clipboard-content-from-unintended-exposure/) it's not "specifically aware of any malicious intent behind the behavior," but noted that the function isn't necessary to perform tasks on the app.

[![Shein Android App](data:image/png;base64... "Shein Android App")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguB45UQRbUCWr0xnnm3Sxlk6c-iZvlAghDWr3V7B3e-5-fpqf11DZTldlePfuhMAbfIgVVfam79QyjodMAAkgOQRA5qCdLci3hB5J-lk7VwoRvCCqA2WPC-HYc0-wVN-eaox3cUneG8vNpE7edHrVcybHiDImTghr6xcpk9qdoTOQpsUpQ8m1TfM-z/s790-rw-e365/app.png)

It further pointed out that launching the application after copying any content to the device clipboard automatically triggered an HTTP POST request containing the data to the server "api-service[.]shein[.]com."

To mitigate such privacy risks, Google has further made improvements to Android in recent years, including [displaying toast messages](https://developer.android.com/about/versions/12/behavior-changes-all#clipboard-access-notifications) when an app accesses the clipboard and [barring apps](https://developer.android.com/about/versions/10/privacy/changes#clipboard-data) from getting the data unless it is actively running in the foreground.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Considering mobile users often use the clipboard to copy and paste sensitive information, like passwords or payment information, clipboard contents can be an attractive target for cyberattacks," researchers Dimitrios Valsamaras and Michael Peck said.

"Leveraging clipboards can enable attackers to collect target information and exfiltrate useful data."

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

[Android](https://thehackernews.com/search/label/Android)[data security](https://thehackernews.com/search/label/data%20security)[Google](https://thehackernews.com/search/label/Google)[Microsoft](https://thehackernews.com/search/label/Microsoft)[Privacy](https://thehackernews.com/search/label/Privacy)[Shopping App](https://thehackernews.com/search/label/Shopping%20App)

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

[![Fortra GoAnywhere CVSS 10 ...