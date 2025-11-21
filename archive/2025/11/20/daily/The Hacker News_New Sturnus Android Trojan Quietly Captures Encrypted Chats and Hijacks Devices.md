---
title: New Sturnus Android Trojan Quietly Captures Encrypted Chats and Hijacks Devices
url: https://thehackernews.com/2025/11/new-sturnus-android-trojan-quietly.html
source: The Hacker News
date: 2025-11-20
fetch_date: 2025-11-21T03:14:23.040204
---

# New Sturnus Android Trojan Quietly Captures Encrypted Chats and Hijacks Devices

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [New Sturnus Android Trojan Quietly Captures Encrypted Chats and Hijacks Devices](https://thehackernews.com/2025/11/new-sturnus-android-trojan-quietly.html)

**Nov 20, 2025**Ravie LakshmananMalware / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8I7UV4u8O03jdgw6jpt_ITLXyqrcwoVLRUr_84vWKRe9ctYFLOAhKGvO7poJq_5YZwb7-3a2NzF0smKc5U0KOj6dgRmw5o0jWI0xEtZMjZTZ8KByylPoes-8t_8sXq7wWEyJ_TQtjI81OS1hx-uAG5a3xVCgEd9sqr3JlCemLHuS9ui-ctH6KjH8-uQri/s790-rw-e365/android-malware.jpg)

Cybersecurity researchers have disclosed details of a new Android banking trojan called **Sturnus** that enables credential theft and full device takeover to conduct financial fraud.

"A key differentiator is its ability to bypass encrypted messaging," ThreatFabric [said](https://www.threatfabric.com/blogs/sturnus-banking-trojan-bypassing-whatsapp-telegram-and-signal) in a report shared with The Hacker News. "By capturing content directly from the device screen after decryption, Sturnus can monitor communications via WhatsApp, Telegram, and Signal."

Another notable feature is its ability to stage overlay attacks by serving fake login screens atop banking apps to capture victims' credentials. According to the Dutch mobile security company, Sturnus is privately operated and is currently assessed to be in the evaluation stage. Artifacts distributing the banking malware are listed below -

* Google Chrome ("com.klivkfbky.izaybebnx")
* Preemix Box ("com.uvxuthoq.noscjahae")

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

The malware has been designed to specifically single out financial institutions across Southern and Central Europe with region-specific overlays.

The name Sturnus is a nod to its use of a mixed communication pattern blending plaintext, AES, and RSA, with ThreatFabric likening it to the [European starling](https://www.allaboutbirds.org/guide/European_Starling/overview) (binomial name: Sturnus vulgaris), which [incorporates](https://www.allaboutbirds.org/guide/European_Starling/sounds) a variety of whistles and is known to be a vocal mimic.

The trojan, once launched, contacts a remote server over WebSocket and HTTP channels to register the device and receive encrypted payloads in return. It also establishes a WebSocket channel to allow the threat actors to interact with the compromised Android device during Virtual Network Computing (VNC) sessions.

Besides serving fake overlays for banking apps, Sturnus is also capable of abusing Android's [accessibility services](https://thehackernews.com/2025/03/new-android-trojan-crocodilus-abuses.html) to capture keystrokes and record user interface (UI) interactions. As soon as an overlay for a bank is served to the victim and the credentials are harvested, the overlay for that specific target is disabled so as not to arouse the user's suspicion.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjk_8XyE3zIgbBgGsBjZ9N2WjdWede0j7TM1O4RByHqtHLw8ORxQFfrJR4WxhwKaDI2CFeX0l4dT-o_WdliNMGsOgzaCJQuRppSwQpfooRZ_pRzJXuM8hQ0ogTsVhQN0uNXesKhinvx-tZZJSbhYcTjeGs9r701n_FiOzFe1gmzSK6X4yLWs1B0Kou8ylPw/s790-rw-e365/Sturnus.png)

Furthermore, it can display a full-screen overlay that blocks all visual feedback and mimics the Android operating system update screen to give the impression to the user that software updates are in progress, when, in reality, it allows malicious actions to be carried out in the background.

Some of the malware's other features include support for monitoring device activity, as well as leveraging accessibility services to gather chat contents from Signal, Telegram, and WhatsApp when they are opened by the victim, and send details about every visible interface element on the screen.

This allows the attackers to reconstruct the layout at their end and remotely issue actions related to clicks, text input, scrolling, app launches, permission confirmations, and even enable a black screen overlay. An alternate remote control mechanism packed into Sturnus uses the system's display-capture framework to mirror the device screen in real-time.

"Whenever the user navigates to settings screens that could disable its administrator status, the malware detects the attempt through accessibility monitoring, identifies relevant controls, and automatically navigates away from the page to interrupt the user," ThreatFabric said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

"Until its administrator rights are manually revoked, both ordinary uninstallation and removal through tools like ADB are blocked, giving the malware strong protection against cleanup attempts."

The extensive environment monitoring capabilities make it possible to collect sensor information, network conditions, hardware data, and an inventory of installed apps. This device profile serves as a continuous feedback loop, helping attackers adapt their tactics to sidestep detection.

"Although the spread remains limited at this stage, the combination of targeted geography and high-value application focus implies that the attackers are refining their tooling ahead of broader or more coordinated operations," ThreatFabric said.

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
[![Facebook Messenger](data:image/png;base64...