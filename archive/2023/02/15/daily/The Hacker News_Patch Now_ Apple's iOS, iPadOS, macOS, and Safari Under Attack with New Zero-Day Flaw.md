---
title: Patch Now: Apple's iOS, iPadOS, macOS, and Safari Under Attack with New Zero-Day Flaw
url: https://thehackernews.com/2023/02/patch-now-apples-ios-ipados-macos-and.html
source: The Hacker News
date: 2023-02-15
fetch_date: 2025-10-04T06:43:02.703342
---

# Patch Now: Apple's iOS, iPadOS, macOS, and Safari Under Attack with New Zero-Day Flaw

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

# [Patch Now: Apple's iOS, iPadOS, macOS, and Safari Under Attack with New Zero-Day Flaw](https://thehackernews.com/2023/02/patch-now-apples-ios-ipados-macos-and.html)

**Feb 14, 2023**Ravie LakshmananDevice Security / Zero Day

[![Apple Zero-Day Flaw](data:image/png;base64... "Apple Zero-Day Flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhwLdHZcIgISVVe_p8sRJD55e2RHR8YhadA9x6ssYx0eC4eRUBser6oxe1WDZL81TA9ZxPlmqDzoe6fKj0vNn0Ag5otjIH60CBIe1qlr8MueqAK-LkOLZ_YaWIB8UAp9Vm9lFI2eXdko8QXlG6joMeS7B_qLdt4Ci5L-dsqRTu1cfJvbsPu2pxDbQ6n/s790-rw-e365/apple.png)

Apple on Monday rolled out security updates for [iOS, iPadOS](https://support.apple.com/en-us/HT213635), [macOS](https://support.apple.com/en-us/HT213633), and [Safari](https://support.apple.com/en-us/HT213638) to address a zero-day flaw that it said has been actively exploited in the wild.

Tracked as **CVE-2023-23529**, the issue relates to a type confusion bug in the WebKit browser engine that could be activated when processing maliciously crafted web content, culminating in arbitrary code execution.

The iPhone maker said the bug was addressed with improved checks, adding it's "aware of a report that this issue may have been actively exploited." An anonymous researcher has been credited with reporting the flaw.

It's not immediately clear as to how the vulnerability is being exploited in real-world attacks, but it's the second actively abused type confusion flaw in WebKit to be patched by Apple after [CVE-2022-42856](https://thehackernews.com/2022/12/new-actively-exploited-zero-day.html) in as many months, which was closed in December 2022.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

WebKit flaws are also notable for the fact that they impact every third-party web browser that's available for iOS and iPadOS owing to Apple's restrictions that require browser vendors to use the same rendering framework.

Also addressed by the company is a use-after-free issue in the Kernel (CVE-2023-23514) that could permit a rogue app to execute arbitrary code with the highest privileges.

Credited with reporting the issue are Xinru Chi of Pangu Lab and Ned Williamson of Google Project Zero. Apple said it resolved the vulnerability with improved memory management.

Separately, the latest macOS update also plugs a privacy defect in Shortcuts that a malware-laced app can take advantage of to "observe unprotected user data." The problem, Apple noted, was fixed with improved handling of temporary files.

Users are advised to update to iOS 16.3.1, iPadOS 16.3.1, macOS Ventura 13.2.1, and Safari 16.3.1 to mitigate potential risks. The updates are available for the following devices -

* iPhone 8 and later, iPad Pro (all models), iPad Air 3rd generation and later, iPad 5th generation and later, and iPad mini 5th generation and later
* Macs running macOS Ventura, macOS Big Sur, and macOS Monterey

Apple remediated a total of 10 zero-days spanning its software in 2022, nine of which were disclosed as actively exploited by threat actors. Four of those flaws were discovered in WebKit.

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

[Apple](https://thehackernews.com/search/label/Apple)[iOS](https://thehackernews.com/search/label/iOS)[iPadOS](https://thehackernews.com/search/label/iPadOS)[MacOS](https://thehackernews.com/search/label/MacOS)[Safari](https://thehackernews.com/search/label/Safari)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[zero-day](https://thehackernews.com/search/label/zero-day)

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

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0...