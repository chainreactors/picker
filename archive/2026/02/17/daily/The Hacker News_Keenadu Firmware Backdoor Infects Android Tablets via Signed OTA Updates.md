---
title: Keenadu Firmware Backdoor Infects Android Tablets via Signed OTA Updates
url: https://thehackernews.com/2026/02/keenadu-firmware-backdoor-infects.html
source: The Hacker News
date: 2026-02-17
fetch_date: 2026-02-18T04:16:20.640007
---

# Keenadu Firmware Backdoor Infects Android Tablets via Signed OTA Updates

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
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Keenadu Firmware Backdoor Infects Android Tablets via Signed OTA Updates](https://thehackernews.com/2026/02/keenadu-firmware-backdoor-infects.html)

**Ravie Lakshmanan**Feb 17, 2026Malware / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8Wza_QsQzhfPQCPUG6GYFEMc6xpel-E8wWXPSZlSeSLIHLRkxcgj-XxdItkZjBJSg7CW26jOr0gtstF5MjAeAumhISRoOJatq0Bss2rNv4f35PVZcwrrxlvhXqBwjtqCt6mL06qZJJZWFNTmLdCBkuL74UCB3O8rN1mC2UOulCvFIs37CyUl9v00zx1OD/s1700-e365/android-firmware.jpg)

A new Android backdoor that's embedded deep into the device firmware can silently harvest data and remotely control its behavior, according to new findings from Kaspersky.

The Russian cybersecurity vendor said it discovered the backdoor, dubbed **Keenadu**, in the firmware of devices associated with various brands, including Alldocube, with the compromise occurring during the firmware build phase. Keenadu has been detected in Alldocube iPlay 50 mini Pro firmware dating back to August 18, 2023. In all cases, the backdoor is embedded within tablet firmware, and the firmware files carry valid digital signatures. The names of the other vendors were not disclosed.

"In several instances, the compromised firmware was delivered with an OTA update," security researcher Dmitry Kalinin [said](https://securelist.com/keenadu-android-backdoor/118913/) in an exhaustive analysis published today. "A copy of the backdoor is loaded into the address space of every app upon launch. The malware is a multi-stage loader granting its operators the unrestricted ability to control the victim's device remotely."

Some of the payloads retrieved by Keenadu allow it to hijack the search engine in the browser, monetize new app installs, and stealthily interact with ad elements. One of the payloads has been found embedded in several standalone apps distributed via third-party repositories, as well as official app marketplaces like Google Play and Xiaomi GetApps.

Telemetry data suggests that 13,715 users worldwide have encountered Keenadu or its modules, with the majority of the users attacked by the malware located in Russia, Japan, Germany, Brazil, and the Netherlands.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

Keenadu was [first disclosed](https://thehackernews.com/2026/01/threatsday-bulletin-ghostad-drain-macos.html#android-tablets-backdoored) by Kaspersky in late December 2025, describing it as a backdoor in libandroid\_runtime.so, a critical shared library in the Android operating system that's loaded during boot. Once it's active on an infected device, it's injected into the [Zygote](https://source.android.com/docs/core/runtime/zygote) process, a behavior also observed in another Android malware called [Triada](https://thehackernews.com/2025/04/triada-malware-preloaded-on-counterfeit.html).

The malware is invoked by means of a function call added to the libandroid\_runtime.so, following which it checks if it's running within system apps belonging either to Google services or to cellular carriers like Sprint or T-Mobile. If so, the execution is aborted. It also has a kill switch to terminate itself if it finds files with certain names in system directories.

"Next, the Trojan checks if it is running within the system\_server process," Kalinin said. "This process controls the entire system and possesses maximum privileges; it is launched by the Zygote process when it starts."

If this check is true, the malware proceeds to create an instance of the AKServer class. Otherwise, it creates an instance of the AKClient class. The AKServer component contains the core logic and command-and-control (C2) mechanism, while AKClient is injected into every app launched on the device and serves as the bridge for interacting with AKServer.

This client-server architecture enables AKServer to execute custom malicious payloads tailored to the specific app it has targeted. AKServer also exposed another interface that malicious modules downloaded within the contexts of other apps can use to grant or revoke permissions to/from an arbitrary app on the device, get the current location, and exfiltrate device information.

The AKServer component is also designed to run a series of checks that cause the malware to terminate if the interface language is Chinese and the device is located within a Chinese time zone, or if Google Play Store or Google Play Services are absent from the device. Once the necessary criteria are satisfied, the Trojan decrypts the C2 address and sends device metadata in encrypted format to the server.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8YVW7HkZXtJt1TbbItT0L7DCLS6CGGWFsfgNZNDjBs-Ocv0N2giEGXgWsoX8bGT9ryNLvUk1KvFJ06LUa8hSfaCLPS8lUpLkqZm-GiKzxupH7Os9KS7hB1fhX-vftEhA8ZXFaaKTpBHJsihx7mPxXXxJcq-xsWAvBgdcpVwFxYE4HrXYU9_pZWxyZIctY/s1700-e365/flaw.png)

In response, the server returns an encrypted JSON object containing details about the payloads. However, in what appears to be an attempt to complicate analysis and evade detection, an added check built into the backdoor prevents the C2 server from serving any payloads until 2.5 months have elapsed since the initial check-in.

"The attacker's server delivers information about the payloads as an object array," Kaspersky explained. "Each object contains a download link for the payload, its MD5 hash, target app package names, target process names, and other metadata. Notably, the attackers chose Amazon AWS as their CDN provider."

Some of the identified malicious modules are listed below -

* **Keenadu loader**, which targets popular online storefronts like Amazon, Shein, and Temu to deliver unspecified payloads. However, it's suspected that they make it possible to add items to the apps' shopping carts without the victim's knowledge.
* **Clicker loader**, which is injected into YouTube, Facebook, Google Digital Wellbeing, and Android Sy...