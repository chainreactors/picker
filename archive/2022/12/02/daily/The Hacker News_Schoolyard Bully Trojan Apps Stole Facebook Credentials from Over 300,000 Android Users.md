---
title: Schoolyard Bully Trojan Apps Stole Facebook Credentials from Over 300,000 Android Users
url: https://thehackernews.com/2022/12/schoolyard-bully-trojan-apps-stole.html
source: The Hacker News
date: 2022-12-02
fetch_date: 2025-10-04T00:20:13.010843
---

# Schoolyard Bully Trojan Apps Stole Facebook Credentials from Over 300,000 Android Users

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

# [Schoolyard Bully Trojan Apps Stole Facebook Credentials from Over 300,000 Android Users](https://thehackernews.com/2022/12/schoolyard-bully-trojan-apps-stole.html)

**Dec 01, 2022**Ravie LakshmananMobile Threat Advisory

[![Facebook Hacking](data:image/png;base64... "Facebook Hacking")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSLDhHovi69bnM69vYuj0igdNu35msfVmpVRZ0jalgVmoiCFI5XhmmM15DJU9FY6sJtOukXGMZBWr8v-N-OAUkVyHD83iUg7A8f5BUttJBk_MBIh81-LHXlEINgCswOYYwe7Wvt_JaZbDxbpRL-YTLEgYUL6ERZp2U6USWGHdNTyOGI7YnOSsdFFuM/s790-rw-e365/apps.png)

More than 300,000 users across 71 countries have been victimized by a new Android threat campaign called the **Schoolyard Bully Trojan**.

Mainly designed to steal Facebook credentials, the malware is camouflaged as legitimate education-themed applications to lure unsuspecting users into downloading them.

The apps, which were available for download from the official Google Play Store, have now been taken down. That said, they still continue to be available on third-party app stores.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"This trojan uses JavaScript injection to steal the Facebook credentials," Zimperium researchers Nipun Gupta and Aazim Bill SE Yaswant said in a [report](https://www.zimperium.com/blog/schoolyard-bully-trojan-facebook-credential-stealer/) shared with The Hacker News.

It achieves this by launching Facebook's login page in a WebView, which also embeds within it malicious JavasCript code to exfiltrate the user's phone number, email address, and password to a configured command-and-control (C2) server.

[![Schoolyard Bully Trojan](data:image/png;base64... "Schoolyard Bully Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjRXtffhEYJ02S4cB0r1cWMTmZLdZ2Cw0KDODMOa3f8eKO4oNlPcKopxYEyrTxQY3Q63JNdoj06lF9jRNLf91fApBrhTf60uJdV9jfgzyEFWKN4YGxnpsN8notvmKZXINCwDLJGwmzMHHZSEs-fIv4wh-U_emfGsMILP49AipTXFwKZr7sdTYP_Qf7nw/s790-rw-e365/map.png)

The Schoolyard Bully Trojan further makes use of native libraries such as "libabc.so" so as to avoid detection by antivirus solutions.

While the malware singles out Vietnamese language applications, it has also been discovered in several other apps available in over 70 countries, underscoring the scale of the attacks.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The findings come more than a year after Zimperium unearthed similar activity aimed at compromising Facebook accounts through rogue Android apps as part of a campaign codenamed [FlyTrap](https://thehackernews.com/2021/08/beware-new-android-malware-hacks.html).

"Attackers can cause a lot of havoc by stealing Facebook passwords," Richard Melick, director of mobile threat intelligence at Zimperium, said. "If they can impersonate someone from their legitimate Facebook account, it becomes extremely easy to phish friends and other contacts into sending money or sensitive information."

"It's also very concerning how many people reuse the same passwords. If an attacker steals someone's Facebook password, there's a high probability that same email and password will work with banking or financial apps, corporate accounts and so much more."

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

[Android](https://thehackernews.com/search/label/Android)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)[Mobile app](https://thehackernews.com/search/label/Mobile%20app)

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

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a W...