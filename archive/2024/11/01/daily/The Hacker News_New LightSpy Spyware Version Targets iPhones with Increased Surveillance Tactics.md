---
title: New LightSpy Spyware Version Targets iPhones with Increased Surveillance Tactics
url: https://thehackernews.com/2024/10/new-lightspy-spyware-version-targets.html
source: The Hacker News
date: 2024-11-01
fetch_date: 2025-10-06T19:27:50.058839
---

# New LightSpy Spyware Version Targets iPhones with Increased Surveillance Tactics

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

# [New LightSpy Spyware Version Targets iPhones with Increased Surveillance Tactics](https://thehackernews.com/2024/10/new-lightspy-spyware-version-targets.html)

**Oct 31, 2024**Ravie LakshmananSpyware / Mobile Security

[![iPhone Spyware](data:image/png;base64... "iPhone Spyware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgr45tM1jfFriC6I8-fkNSoay8JCWhcJl0qFEa7qFLl1MbIxxVhv_Psr766umRFG3lvobhe0dmc7MaYAXVfPziAJVFAyIRJWunD-tmh617ltlj5ORyDeDV9XefWPMqmyzzdPaDGwHag1cn5tjAfUy_3_JAYxkTFDW-3GnU07Fn-WuS-aaTsusb6ghUUvIVC/s790-rw-e365/apple.png)

Cybersecurity researchers have discovered an improved version of an Apple iOS spyware called LightSpy that not only expands on its functionality, but also incorporates destructive capabilities to prevent the compromised device from booting up.

"While the iOS implant delivery method closely mirrors that of the macOS version, the post-exploitation and privilege escalation stages differ significantly due to platform differences," ThreatFabric [said](https://www.threatfabric.com/blogs/lightspy-implant-for-ios) in an analysis published this week.

LightSpy, first documented in 2020 as targeting users in Hong Kong, is a [modular implant](https://thehackernews.com/2024/06/lightspy-spywares-macos-variant-found.html) that employs a plugin-based architecture to augment its capabilities and allow it to capture a wide range of sensitive information from an infected device.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Attack chains distributing the malware leverage known security flaws in Apple iOS and macOS to trigger a WebKit exploit that drops a file with the extension ".PNG," but is actually a Mach-O binary responsible for retrieving next-stage payloads from a remote server by abusing a memory corruption flaw tracked as [CVE-2020-3837](https://nvd.nist.gov/vuln/detail/CVE-2020-3837).

This includes a component dubbed FrameworkLoader that, in turn, downloads LightSpy's Core module and its assorted plugins, which have gone up significantly from 12 to 28 in the latest version (7.9.0).

"After the Core starts up, it will perform an Internet connectivity check using Baidu.com domain, and then it will check the arguments that were passed from FrameworkLoader as the [command-and-control] data and working directory," the Dutch security company said.

"Using the working directory path /var/containers/Bundle/AppleAppLit/, the Core will create subfolders for logs, database, and exfiltrated data."

The plugins can capture a wide range of data, including Wi-Fi network information, screenshots, location, iCloud Keychain, sound recordings, photos, browser history, contacts, call history, and SMS messages, as well as gather information from apps like Files, LINE, Mail Master, Telegram, Tencent QQ, WeChat, and WhatsApp.

[![iPhone Spyware](data:image/png;base64... "iPhone Spyware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdAgn4tij3m9L591XMg77YUzLTt0r8yR2J7e1Pi21lgmq8__-wdcQMaUIBC-xxFY_LMzUQPcgJPgIxjm9h6z39XjL5xFHKaloqnIyZKbGZ8fDm-J1K0NSP9vIDo-wd5DcJgaKVBQRcdSE-lpFR4sZjZao6E2YC9XQmCU-z5O7Lli1YlsPnkaQnxP2PHHDp/s790-rw-e365/spyware.png)

Some of the newly added plugins also boast destructive features that can delete media files, SMS messages, Wi-Fi network configuration profiles, contacts, and browser history, and even freeze the device and prevent it from starting again. Furthermore, LightSpy plugins can generate fake push notifications containing a specific URL.

The exact distribution vehicle for the spyware is unclear, although it's believed to be orchestrated via [watering hole attacks](https://thehackernews.com/2020/03/iphone-iOS-spyware.html). The campaigns have not been attributed to a known threat actor or group to date.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

However, there is some evidence that the operators are likely based in China owing to the fact that the location plugin "recalculates location coordinates according to a system used exclusively in China." It's worth noting that Chinese map service providers follow a coordinate system called [GCJ-02](https://en.wikipedia.org/wiki/Restrictions_on_geographic_data_in_China#GCJ-02).

"The LightSpy iOS case highlights the importance of keeping systems up to date," ThreatFabric said. "The threat actors behind LightSpy closely monitor publications from security researchers, reusing newly disclosed exploits to deliver payloads and escalate privileges on affected devices."

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

[Apple](https://thehackernews.com/search/label/Apple)[Cyber Defense](https://thehackernews.com/search/label/Cyber%20Defense)[Cyber Threat](https://thehackernews.com/search/label/Cyber%20Threat)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Digital privacy](https://thehackernews.com/search/label/Digital%20privacy)[Malware](https://thehackernews.com/search/label/Malware)[mobile security](https://thehackernews.com/search/label/mobile%20security)[spyware](https://thehackernews.com/search/label/spyware)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:...