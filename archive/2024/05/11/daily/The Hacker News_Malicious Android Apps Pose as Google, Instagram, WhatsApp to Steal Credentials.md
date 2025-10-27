---
title: Malicious Android Apps Pose as Google, Instagram, WhatsApp to Steal Credentials
url: https://thehackernews.com/2024/05/malicious-android-apps-pose-as-google.html
source: The Hacker News
date: 2024-05-11
fetch_date: 2025-10-06T17:19:09.720861
---

# Malicious Android Apps Pose as Google, Instagram, WhatsApp to Steal Credentials

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

# [Malicious Android Apps Pose as Google, Instagram, WhatsApp to Steal Credentials](https://thehackernews.com/2024/05/malicious-android-apps-pose-as-google.html)

**May 10, 2024**Ravie LakshmananCybercrime / Banking Fraud

[![Malicious Android Apps](data:image/png;base64... "Malicious Android Apps")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgu7hyphenhyphennU2IYjiz-ihf3HI2sV7T0y8bp02Lny2zKl22QLmn60deJC7JrSYqlkAEihse0cDSvFoTKVWehDNwJHrR4xoMZOMSFkDUTBuDWNqQ6tbDT5Z7hZ784vbqPeKYUv9W9NFIV32gq8n_72bAOq0NcSHKiEtrKHmePuoQcgVdyRddlABJ3R4Q0upkj8NZG/s790-rw-e365/apps.png)

Malicious Android apps masquerading as Google, Instagram, Snapchat, WhatsApp, and X (formerly Twitter) have been observed to steal users' credentials from compromised devices.

"This malware uses famous Android app icons to mislead users and trick victims into installing the malicious app on their devices," the SonicWall Capture Labs threat research team [said](https://blog.sonicwall.com/en-us/2024/04/android-remote-access-trojan-equipped-to-harvest-credentials/) in a recent report.

The distribution vector for the campaign is currently unclear. However, once the app is installed on the users' phones, it requests them to grant it permissions to the accessibility services and the [device administrator API](https://developers.google.com/android/work/device-admin-deprecation), a now-deprecated feature that provides device administration features at the system level.

Obtaining these permissions allows the rogue app to gain control over the device, making it possible to carry out arbitrary actions ranging from data theft to malware deployment without the victims' knowledge.

The malware is designed to establish connections with a command-and-control (C2) server to receive commands for execution, allowing it to access contact lists, SMS messages, call logs, the list of installed apps; send SMS messages; open phishing pages on the web browser, and toggle the camera flashlight.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The phishing URLs mimic the login pages of well-known services like Facebook, GitHub, Instagram, LinkedIn, Microsoft, Netflix, PayPal, Proton Mail, Snapchat, Tumblr, X, WordPress, and Yahoo.

A Google spokesperson confirmed to The Hacker News that [Google Play Protect](https://developers.google.com/android/play-protect), Android's built-in malware defense, automatically protects users from apps containing known versions of this malware.

The development comes as Cyfirma and Broadcom-owned Symantec [warned](https://www.cyfirma.com/research/new-pakistan-based-cyber-espionage-groups-year-long-campaign-targeting-indian-defense-forces-with-android-malware/) of a social engineering campaign that employs WhatsApp as a delivery vector to propagate a new Android malware by posing as a defense-related application.

"Upon successful delivery, the application would install itself under the guise of a Contacts application," Symantec [said](https://www.broadcom.com/support/security-center/protection-bulletin/android-malware-used-in-targeted-attack-against-indian-defense-forces). "Upon execution, the app would request permissions for SMS, Contacts, Storage, and Telephone and subsequently remove itself from view."

It also follows the [discovery](https://www.broadcom.com/support/security-center/protection-bulletin/coper-actors-abuse-livechat-cdn-in-ongoing-fake-chrome-tactic) of malware campaigns distributing Android banking trojans like [Coper](https://thehackernews.com/2024/04/vultur-android-banking-trojan-returns.html), which is capable of harvesting sensitive information and displaying fake window overlays, deceiving users into unknowingly surrendering their credentials.

[![Malicious Android Apps](data:image/png;base64... "Malicious Android Apps")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwcESXGxq398-wVpyGpXHKp8sEfnuFZAFix15kcXM9_yO0vvjhzscwovmAMvipgbTOFjdwOTGNR78ri-UIKLuhYJw3AiYNoXOpfSd54lUaoQplKBd7WwfFO_6BcufNGJX8Z8NRfIkLE7t7AbH5DTWxVQQ5AcsHsWVQQ8GMVB6wBv6bs3hH3wlF1h6sl5Rm/s790-rw-e365/insta.png)

Last week, Finland's National Cyber Security Centre (NCSC-FI) [revealed](https://www.kyberturvallisuuskeskus.fi/fi/ajankohtaista/kyberturvallisuuskeskuksen-viikkokatsaus-182024) that smishing messages are being used to direct users to Android malware that steals banking data.

The attack chain leverages a technique called telephone-oriented attack delivery (TOAD), wherein the SMS messages urge the recipients to call a number in connection with a debt collection claim.

Once the call is made, the scammer on the other end informs the victim that the message is fraudulent and that they should install an antivirus app on their phone for protection.

They also instruct the caller to click on a link sent in a second text message to install the purported security software, but in reality, is malware engineered to steal online banking account credentials and ultimately perform unauthorized fund transfers.

While the exact Android malware strain used in the attack was not identified by NCSC-FI, it's suspected to be [Vultr](https://thehackernews.com/2024/04/vultur-android-banking-trojan-returns.html), which was detailed by NCC Group early last month as leveraging a virtually identical process to infiltrate devices.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Android-based malware such as Tambir and Dwphon have also been detected in the wild in recent months with various device gathering features, with the latter targeting mobile phones by Chinese handset makers and primarily intended for the Russian market.

"Dwphon comes as a component of the system update application and exhibits many characteristics of pre-installed Android malware," Kaspersky [said](https://securelist.com/crimeware-report-android-malware/112121/).

"The exact infection path is unclear, but there is an assumption that the infected application was incorporated into the firmware as...