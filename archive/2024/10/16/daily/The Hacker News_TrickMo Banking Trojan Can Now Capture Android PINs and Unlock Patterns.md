---
title: TrickMo Banking Trojan Can Now Capture Android PINs and Unlock Patterns
url: https://thehackernews.com/2024/10/trickmo-banking-trojan-can-now-capture.html
source: The Hacker News
date: 2024-10-16
fetch_date: 2025-10-06T18:56:52.880890
---

# TrickMo Banking Trojan Can Now Capture Android PINs and Unlock Patterns

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

# [TrickMo Banking Trojan Can Now Capture Android PINs and Unlock Patterns](https://thehackernews.com/2024/10/trickmo-banking-trojan-can-now-capture.html)

**Oct 15, 2024**Ravie LakshmananMobile Security / Financial Fraud

[![Android PINs and Unlock Patterns](data:image/png;base64... "Android PINs and Unlock Patterns")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0n1Yh89X0-TDGq0zqxptIFr8OswFr1PPpmJPYeCgUAss59B_rB58R3S4UDg0z82-u9_FwmoaYqy-BT3pk59btzdNWgyxhI7Ltj5SiOkY3K9fy-lqVUegsY0p-MMjYWRjfi1pdDXfnCfC-XrKppUU9v98-nwnyXIc4nUYtKCL6Zd86oGUh2lvfTS2iAihA/s790-rw-e365/android.png)

New variants of an Android banking trojan called TrickMo have been found to harbor previously undocumented features to steal a device's unlock pattern or PIN.

"This new addition enables the threat actor to operate on the device even while it is locked," Zimperium security researcher Aazim Yaswant [said](https://www.zimperium.com/blog/expanding-the-investigation-deep-dive-into-latest-trickmo-samples/) in an analysis published last week.

First spotted in the wild in 2019, TrickMo is so named for its associations with the TrickBot cybercrime group and is capable of granting remote control over infected devices, as well as stealing SMS-based one-time passwords (OTPs) and displaying overlay screens to capture credentials by abusing Android's accessibility services.

Last month, Italian cybersecurity company Cleafy [disclosed](https://thehackernews.com/2024/09/trickmo-android-trojan-exploits.html) updated versions of the mobile malware with improved mechanisms to evade analysis and grant itself additional permissions to perform various malicious actions on the device, including carrying out unauthorized transactions.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Some of the [new variants](https://github.com/Zimperium/IOC/tree/master/2024-10-TrickMo) of the malware have also been equipped to harvest the device's unlock pattern or PIN by presenting to the victim a deceptive User Interface (UI) that mimics the device's actual unlock screen.

The UI is an HTML page that's hosted on an external website and displayed in full-screen mode, thus giving the impression that it's a legitimate unlock screen.

Should unsuspecting users enter their unlock pattern or PIN, the information, alongside a unique device identifier, is transmitted to an attacker-controlled server ("[android.ipgeo[.]at](https://urlscan.io/domain/android.ipgeo.at)") in the form of an [HTTP POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST) request.

Zimperium said the lack of adequate security protections for the C2 servers made it possible to gain insight into the kinds of data stored in them. This includes files with approximately 13,000 unique IP addresses, most of which are geolocated to Canada, the U.A.E., Turkey, and Germany.

[![TrickMo Banking Trojan](data:image/png;base64... "TrickMo Banking Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFbhW0a90yMLLANu4CoaQm40BM9cPQ4Bzi6COjVqiNHV-mFmOjNfWA9mpjwhUhrxjyjQayCU5NRNNA3fjRubVLrTHRmUMqX2z02KmB2yMSCkseI-xsRK5WewXJhJof8DJIV8LfiUh1h9mQxXpZZdhmdgkVNSEN4PU76NIGAStBKO_arvGkJ1WtMNv-JA6m/s790-rw-e365/apps.jpg)

"These stolen credentials are not only limited to banking information but also encompass those used to access corporate resources such as VPNs and internal websites," Yaswant said. "This underscores the critical importance of protecting mobile devices, as they can serve as a primary entry point for cyberattacks on organizations."

Another notable aspect is the broad targeting of TrickMo, gathering data from applications spanning multiple categories such as banking, enterprise, job and recruitment, e-commerce, trading, social media, streaming and entertainment, VPN, government, education, telecom, and healthcare.

The development comes amid the emergence of a new ErrorFather Android banking trojan campaign that employs a variant of [Cerberus](https://thehackernews.com/2023/01/android-users-beware-new-hook-malware.html) to conduct financial fraud.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The emergence of ErrorFather highlights the persistent danger of repurposed malware, as cybercriminals continue to exploit leaked source code years after the original Cerberus malware was discovered," Broadcom-owned Symantec [said](https://www.broadcom.com/support/security-center/protection-bulletin/errorfather-android-trojan).

According to [data](https://www.zscaler.com/blogs/security-research/new-threatlabz-report-mobile-remains-top-threat-vector-111-spyware-growth) from Zscaler ThreatLabz, financially motivated mobile attacks involving banking malware have witnessed a 29% jump during the period June 2023 to April 2024, when compared to the previous year.

India came out as the top target for mobile attacks during the time frame, experiencing 28% of all attacks, followed by the U.S., Canada, South Africa, the Netherlands, Mexico, Brazil, Nigeria, Singapore, and the Philippines.

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

[Android](https://thehackernews.com/search/label/Android)[banking Trojan](https://th...