---
title: PlayPraetor Android Trojan Infects 11,000+ Devices via Fake Google Play Pages and Meta Ads
url: https://thehackernews.com/2025/08/playpraetor-android-trojan-infects.html
source: The Hacker News
date: 2025-08-05
fetch_date: 2025-10-07T00:51:19.427995
---

# PlayPraetor Android Trojan Infects 11,000+ Devices via Fake Google Play Pages and Meta Ads

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

# [PlayPraetor Android Trojan Infects 11,000+ Devices via Fake Google Play Pages and Meta Ads](https://thehackernews.com/2025/08/playpraetor-android-trojan-infects.html)

**Aug 04, 2025**Ravie LakshmananMobile Security / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiK-E-fRl0HHtvl1C4GC5486zoKtrNUEeFwzh-AmTRCiIGguKsW8xw3jxKuUQtHW5nCnVW0cese1eZ6q8LZV-0NtEH-eQuIWRu7t7n6NTvv1pNZsS35Hm2F3fFhKEsk2keCDVvvH83lMrQmmoTK1R5ACNWvidwXZLMiV5IFmX0vP4KMVd3Vbmc8YtsLCjYf/s790-rw-e365/android-malware.jpg)

Cybersecurity researchers have discovered a nascent Android remote access trojan (RAT) called **PlayPraetor** that has infected more than 11,000 devices, primarily across Portugal, Spain, France, Morocco, Peru, and Hong Kong.

"The botnet's rapid growth, which now exceeds 2,000 new infections per week, is driven by aggressive campaigns focusing on Spanish and French speakers, indicating a strategic shift away from its previous common victim base," Cleafy researchers Simone Mattia, Alessandro Strino, and Federico Valentini [said](https://www.cleafy.com/cleafy-labs/playpraetors-evolving-threat-how-chinese-speaking-actors-globally-scale-an-android-rat) in an analysis of the malware.

PlayPraetor, managed by a Chinese command-and-control (C2) panel, doesn't significantly deviate from other Android trojans in that it abuses accessibility services to gain remote control and can serve fake overlay login screens atop nearly 200 banking apps and cryptocurrency wallets in an attempt to hijack victim accounts.

PlayPraetor was [first documented](https://www.ctm360.com/reports/playpraetor-trojan-report) by CTM360 in March 2025, detailing the operation's use of thousands of fraudulent Google Play Store download pages to perpetrate an interconnected large-scale scam campaign that can harvest banking credentials, monitor clipboard activity, and log keystrokes.

"The links to the impersonated Play Store pages are distributed through Meta Ads and SMS messages to effectively reach a wide audience," the Bahrain-based company noted at the time. "These deceptive ads and messages trick users to click on the links, leading them to the fraudulent domains hosting the malicious APKs."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Assessed to be a globally coordinated operation, PlayPraetor [comes](https://www.ctm360.com/reports/play-masquerading-party-report) in five different variants that install deceptive Progressive Web Apps (PWAs), WebView-based apps (Phish), exploit accessibility services for persistent and C2 (Phantom), facilitate invite code-based phishing and trick users into purchasing counterfeit products (Veil), and grant full remote control via EagleSpy and SpyNote (RAT).

The Phantom variant of PlayPraetor, per the Italian fraud prevention company, is capable of on-device fraud ([ODF](https://thehackernews.com/2022/05/latest-mobile-malware-report-suggests.html)) and is dominated by two principal affiliate operators who control about 60% of the botnet (roughly 4,500 compromised devices) and appear to center their efforts around Portuguese-speaking targets.

"Its core functionality relies on abusing Android's accessibility services to gain extensive, real-time control over a compromised device," Cleafy said. "This allows an operator to perform fraudulent actions directly on the victim's device."

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7Sg8eLkSRWiJsgOfgDTG6itvXuujY9oMUGfMoJKMsW5J5O7hyphenhyphensKnYhx6zxO2ecP_g6cX6UOfC7c5MpgOpq1aIXI4x_wbNm8GQrVfeG0_rs1xwlK-zG5njRxEAy52KOZwJRSlU2qG9YKD-Bikj2JPxEC4_igrUyY5ixLEOg7-FWZ9Vge-VwTlDk06sTShZ/s790-rw-e365/ctm.jpg) |
| Image Source: CTM360 |

Once installed, the malware beacons out to the C2 server via HTTP/HTTPS and makes use of a WebSocket connection to create a bidirectional channel to issue commands. It also sets up a Real-Time Messaging Protocol (RTMP) connection to initiate a video livestream of the infected device's screen.

The evolving nature of the supported commands indicates that PlayPraetor is being actively developed by its operators, allowing for comprehensive data theft. In recent weeks, attacks distributing the malware have increasingly targeted Spanish- and Arabic-speaking victims, signaling a broader expansion of the malware-as-a-service (MaaS) offering.

The C2 panel, for its part, is not only used to actively interact with compromised devices in real-time, but also enable the creation of bespoke malware delivery pages that mimic Google Play Store on both desktop and mobile devices.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj3b-XAGpzf38vPEiz2CaxoiLeHe8SPjCvVu1_HMqLmYsSydalnr20sUp828t4ys4F-dASWT48c7dotx6uGT7snMU_6qmHGjux0QdeR8x8ra1tFtVtWxIfr8QesxrYt3jhyphenhyphenefn7iYTiFYVO0nVQsMmtTuTXdOrxccgG-HZ9U_NUp95heP4D7w-Fa7-Y260Q/s790-rw-e365/malware.png)

"The campaign's success is built upon a well-established operational methodology, leveraging a multi-affiliate MaaS model," Cleafy said. "This structure allows for broad and highly targeted campaigns."

PlayPraetor is the latest malware originating from Chinese-speaking threat actors with an aim to conduct financial fraud, a trend exemplified by the emergence of [ToxicPanda](https://thehackernews.com/2025/02/new-tgtoxic-banking-trojan-variant.html) and [SuperCard X](https://thehackernews.com/2025/06/new-android-malware-surge-hits-devices.html) over the past year.

### ToxicPanda Evolves

According to data from Bitsight, ToxicPanda has compromised around 3,000 Android devices in Portugal, followed by Spain, Greece, Morocco and Peru. Campaigns distributing the malware have leveraged TAG-1241, a traffic distribution system (TDS), for malware distribution using [ClickFix](https://thehackernews.com/2025/03/microsoft-warns-of-clickfix-phishing.html) and fake Google Chrome update lures.

[![CIS Build Kits](data:image/png;base64...)]...