---
title: Anatsa Android Banking Trojan Hits 90,000 Users with Fake PDF App on Google Play
url: https://thehackernews.com/2025/07/anatsa-android-banking-trojan-hits.html
source: The Hacker News
date: 2025-07-09
fetch_date: 2025-10-07T00:03:30.779967
---

# Anatsa Android Banking Trojan Hits 90,000 Users with Fake PDF App on Google Play

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

# [Anatsa Android Banking Trojan Hits 90,000 Users with Fake PDF App on Google Play](https://thehackernews.com/2025/07/anatsa-android-banking-trojan-hits.html)

**Jul 08, 2025**Ravie LakshmananMalware / Mobile Security

[![Anatsa Android Banking Trojan](data:image/png;base64... "Anatsa Android Banking Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgeKwQ5Peq0EKLk5x_73E6IeIE4Eb5Ps_Ba7WcagkLfMjYrVK-dbxdp-tFCNntZMEFEAJOxRtwEFmVapyAm0fk4q2zYHJokHuTlpjrmZ9pltK4BVTa9uFedvJquW3i4GRoAU45ouiBtS7qUxjDL6LwGdD7B-04HxkGGtixOEkljW1Nn4iwZbLviNm6dGC8M/s790-rw-e365/pdf-malware.jpg)

Cybersecurity researchers have discovered an Android banking malware campaign that has leveraged a trojan named Anatsa to target users in North America using malicious apps published on Google's official app marketplace.

The malware, disguised as a "PDF Update" to a document viewer app, has been caught serving a deceptive overlay when users attempt to access their banking application, claiming the service has been temporarily suspended as part of scheduled maintenance.

"This marks at least the third instance of Anatsa focusing its operations on mobile banking customers in the United States and Canada," Dutch mobile security company ThreatFabric [said](https://www.threatfabric.com/blogs/anatsa-targets-north-america-uses-proven-mobile-campaign-process) in a report shared with The Hacker News. "As with previous campaigns, Anatsa is being distributed via the official Google Play Store."

Anatsa, also referred to as TeaBot and Toddler, has been [known](https://thehackernews.com/2023/06/anatsa-banking-trojan-targeting-users.html) to be active since at least 2020, typically delivered to victims via dropper apps.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Early last year, Anatsa was [found](https://thehackernews.com/2024/02/anatsa-android-trojan-bypasses-google.html) to have targeted Android device users in Slovakia, Slovenia, and Czechia by first uploading benign apps masquerading as PDF readers and phone cleaners to the Play Store and then introducing malicious code a week after release.

Like other Android banking trojans, Anatsa is capable of providing its operators with features designed to steal credentials through overlay and keylogging attacks, and conduct Device-Takeover Fraud (DTO) to initiate fraudulent transactions from victim's devices.

ThreatFabric said Anatsa campaigns follow a predictable, but well-oiled, process that involves establishing a developer profile on the app store and then publishing a legitimate app that works as advertised.

"Once the application gains a substantial user base – often in the thousands or tens of thousands of downloads – an update is deployed, embedding malicious code into the app," the company said. "This embedded code downloads and installs Anatsa on the device as a separate application."

The malware then receives a dynamic list of targeted financial and banking institutions from an external server, enabling the attackers to perform credential theft for account takeover, keylogging, or fully automated transactions using DTO.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVsq-rRoaBrc4qvVaEv4adGgoVB848xlMA_k9lJSA79byi6PYTAzo7Qe_5DQq1YZFnLkZOxmzSaib-WCOBQlbnm820sOemMKItozTzA51erBfX90QdBofVv7kIcCANp7YEd73gh11seF1giX9WGrtxA2-KLyTwD2KuZ2PMeLDq9y8rntgY8l9yARUim2HV/s790-rw-e365/play-apps.jpg)

A crucial factor that allows Anatsa to evade detection as well as maintain a high success rate is its cyclical nature where the attacks are interspersed by periods of no activity.

The newly discovered app targeting North American audiences exemplifies this calculated multi-stage strategy to deliver the banking trojan after several weeks after it began to attract thousands of downloads.

It masquerades as an app called "Document Viewer - File Reader" (APK package name: "com.stellarastra.maintainer.astracontrol\_managerreadercleaner") and is published by a developer named "Hybrid Cars Simulator, Drift & Racing." Both the app and the associated developer account are no longer accessible on the Play Store.

Statistics from Sensor Tower [show](https://app.sensortower.com/overview/com.stellarastra.maintainer.astracontrol_managerreadercleaner?country=US) that the app was first published on May 7, 2025, reaching the fourth spot in the "Top Free - Tools" category on June 29, 2025. It's estimated to have been downloaded around 90,000 times.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"This dropper followed Anatsa's established modus operandi: initially launched as a legitimate app, it was transformed into a malicious one approximately six weeks after release," ThreatFabric said. "The distribution window for this campaign was short yet impactful, running from 24 to 30 June."

The Anatsa variant, per the company, is also configured to target a broader set of banking apps in the United States, reflective of the malware's increasing focus on exploiting financial entities in the region.

Another clever feature incorporated into the malware is its ability to display a fake maintenance notice when trying to access the target banking application. This tactic not only conceals the malicious activity occurring within the app, but also prevents customers from contacting the bank's support team, thereby delaying detection of financial fraud.

"The latest operation not only broadened its reach but also relied on well-established tactics aimed at financial institutions in the region," ThreatFabric said. "Organizations in the financial sector are encouraged to review the provided intelligence and assess any potential risks or impacts on their customers and systems."

### Update

Following the publication of the story, Google shared the below statement with The Hacker News -

*All of these identified malicious apps have been removed from Google Play. Users are automatically protected by Google Play ...