---
title: Popular Android Apps Like Xiaomi, WPS Office Vulnerable to File Overwrite Flaw
url: https://thehackernews.com/2024/05/popular-android-apps-like-xiaomi-wps.html
source: The Hacker News
date: 2024-05-03
fetch_date: 2025-10-06T17:17:51.524304
---

# Popular Android Apps Like Xiaomi, WPS Office Vulnerable to File Overwrite Flaw

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

# [Popular Android Apps Like Xiaomi, WPS Office Vulnerable to File Overwrite Flaw](https://thehackernews.com/2024/05/popular-android-apps-like-xiaomi-wps.html)

**May 02, 2024**Ravie LakshmananVulnerability / Android

[![Android Security](data:image/png;base64... "Android Security")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigmE-bZrGVDm13EWFXWLMYr044v3vExYNhz7ZgWpDBfjhuzCNOZHmUduocbXO37wpVMnX6NV4mgprnIoIxSc_6G_Gh7QHnUIz8Y1c0KNUIpJjnE4t8Uxu29YGdGxxirPHtpQnpBKCPxv88gvYiqU8Y3QGaAVChksvgAXyxsV2j7JWC2GyUimABOp6lNet5/s790-rw-e365/apps.png)

Several popular Android applications available in Google Play Store are susceptible to a path traversal-affiliated vulnerability codenamed the **Dirty Stream** attack that could be exploited by a malicious app to overwrite arbitrary files in the vulnerable app's home directory.

"The implications of this vulnerability pattern include arbitrary code execution and token theft, depending on an application's implementation," Dimitrios Valsamaras of the Microsoft Threat Intelligence team [said](https://www.microsoft.com/en-us/security/blog/2024/05/01/dirty-stream-attack-discovering-and-mitigating-a-common-vulnerability-pattern-in-android-apps/) in a report published Wednesday.

Successful exploitation could allow an attacker to take full control of the application's behavior and leverage the stolen tokens to gain unauthorized access to the victim's online accounts and other data.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Two of the apps that were found vulnerable to the problem are as follows -

* Xiaomi File Manager (com.mi. Android.globalFileexplorer) - Over 1 billion installs
* WPS Office (cn.wps.moffice\_eng) - Over 500 million installs

While Android implements isolation by assigning each application its own dedicated data and memory space, it offers what's called a content provider to facilitate data and file sharing between apps in a secure manner. But implementation oversights could enable bypassing of read/write restrictions within an application's home directory.

"This content provider-based model provides a well-defined file-sharing mechanism, enabling a serving application to share its files with other applications in a secure manner with fine-grained control," Valsamaras said.

"However, we have frequently encountered cases where the consuming application doesn't validate the content of the file that it receives and, most concerning, it uses the filename provided by the serving application to cache the received file within the consuming application's internal data directory."

[![Android Security](data:image/png;base64... "Android Security")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghHbxigQ-FpuIoHAv5z-5I2uJUdShuw3AoKuHsoquDwKdCnNyq-FbIw6tjh0zJqbTYa3848gsvPhr5RSE-8qBn9cl7bjcTCpxwmSZjD-7mqZsWKMy3tZaqdyMKnZ8YsQ_WUp-GfVb-TTbeNH8bdEY_76KSk_Jl0S4GI_-eVSwYjTAOVnrVsgbvQK1h9K7N/s790-rw-e365/ms.png)

This pitfall can have serious consequences when a serving app declares a malicious version of the [FileProvider class](https://developer.android.com/reference/androidx/core/content/FileProvider) in order to enable file sharing between apps, and ultimately cause the consuming application to overwrite critical files in its private data space.

Put differently, the mechanism takes advantage of the fact that the consuming app blindly trusts the input to send arbitrary payloads with a specific filename by means of a custom, [explicit intent](https://developer.android.com/guide/components/intents-filters#Types) and without the user's knowledge or consent, leading to code execution.

As a result, this could permit an attacker to overwrite the target app's shared preferences file and make it communicate with a server under their control to exfiltrate sensitive information.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Another scenario involves apps that load native libraries from its own data directory (instead of "/data/app-lib"), in which case a rogue app could exploit the aforementioned weakness to overwrite a native library with malicious code that gets executed when the library is loaded.

Following responsible disclosure, both Xiaomi and WPS Office have rectified the issue as of February 2024. Microsoft, however, said the issue could be more prevalent, requiring that developers take steps to check their apps for similar issues.

Google has also published its own guidance on the matter, urging developers to properly handle the filename provided by the server application.

"When the client application writes the received file to storage, it should ignore the filename provided by the server application and instead use its own internally generated unique identifier as the filename," Google [said](https://developer.android.com/privacy-and-security/risks/untrustworthy-contentprovider-provided-filename). "If generating a unique filename is not practical, the client application should sanitize the provided filename."

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

[Android](https://thehackernews.com/search/label/Android)[app development](https://thehackernews.com/search/label/a...