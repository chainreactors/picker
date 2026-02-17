---
title: New ZeroDayRAT Mobile Spyware Enables Real-Time Surveillance and Data Theft
url: https://thehackernews.com/2026/02/new-zerodayrat-mobile-spyware-enables.html
source: The Hacker News
date: 2026-02-16
fetch_date: 2026-02-17T04:21:51.896204
---

# New ZeroDayRAT Mobile Spyware Enables Real-Time Surveillance and Data Theft

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

# [New ZeroDayRAT Mobile Spyware Enables Real-Time Surveillance and Data Theft](https://thehackernews.com/2026/02/new-zerodayrat-mobile-spyware-enables.html)

**Ravie Lakshmanan**Feb 16, 2026Spyware / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgUKaEDCa0YvJa9oAIavVh9Rz9NN1Cj0XVy8fKroTXMBQp7rYGL14oiZ14iCTMk0ToBg1wWx-iTClSpoZ_wg4hSAgPvFyatlGddSFgnaqdREUK24NW6xdnVgajR703vH_UpbjnLC4_NdFy1RC4pETcSTaxekLpAXNfz0n8ME7s9nyIco15DjjTiZwm7Tkhs/s1700-e365/android-spyware.jpg)

Cybersecurity researchers have disclosed details of a new mobile spyware platform dubbed **ZeroDayRAT** that's being advertised on Telegram as a way to grab sensitive data and facilitate real-time surveillance on Android and iOS devices.

"The developer runs dedicated channels for sales, customer support, and regular updates, giving buyers a single point of access to a fully operational spyware panel," Daniel Kelley, security researcher at iVerify, [said](https://iverify.io/blog/breaking-down-zerodayrat---new-spyware-targeting-android-and-ios). "The platform goes beyond typical data collection into real-time surveillance and direct financial theft."

ZeroDayRAT is designed to support Android versions 5 through 16 and iOS versions up to 26. It's assessed that the malware is distributed via social engineering or fake app marketplaces. The malicious binaries are generated through a builder that's provided to buyers along with an online panel that they can set up on their own server.

Once the malware infects a device, the operator gets to see all the details, including model, location, operating system, battery status, SIM, carrier details, app usage, notifications, and a preview of recent SMS messages, through a self-hosted panel. This information allows the threat actor to profile the victim and glean more about who they talk to and the apps they use the most.

The panel also extracts their current GPS coordinates and plots them on Google Maps, along with the history of all locations they have been to over time, effectively turning it into spyware.

"One of the more problematic panels is the accounts tab," Kelley added. "Every account registered on the device is enumerated: Google, WhatsApp, Instagram, Facebook, Telegram, Amazon, Flipkart, PhonePe, Paytm, Spotify, and more, each with its associated username or email."

Some of the other capabilities of ZeroDayRAT include logging keystrokes, gathering SMS messages -- including one-time passwords (OTPs) to defeat two-factor authentication, as well as allowing hands-on operations, such as activating real-time surveillance via live camera streaming and a microphone feed that allows the adversary to remotely monitor a victim.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

To enable financial theft, the malware incorporates a stealer component that scans for wallet apps like MetaMask, Trust Wallet, Binance, and Coinbase, and substitutes wallet addresses copied to the clipboard to [reroute transactions](https://thehackernews.com/2025/03/new-massjacker-malware-targets-piracy.html) to a wallet under the attacker's control.

There also exists a bank stealer module to target online mobile wallet platforms like Apple Pay, Google Pay, PayPal, along with PhonePe, an Indian digital payments application that allows instant money transfers with the Unified Payments Interface ([UPI](https://www.npci.org.in/product/upi)), a protocol to facilitate inter-bank peer-to-peer and person-to-merchant transactions.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOY5mGpQ1aNJ9CFpw4IccarzwtVo5z8qdBg6iv6FQZOQYtoj5oFPwnNWfS2kB6VOiuhNrTs_Sv7kO0jNynxkXr7rHQ_eM70V1wWWO3Ar-gokKRRsfj5O6C6Nwmh1bBx4vGejfG2wkyfdHf9iJjmoo2vcViULXZpftp2kij1UDLITrmt3_jH1y0kPiBVmdh/s1700-e365/android-2.jpg)

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjU_S8esvq_PqhtUQ4TFncd3xVyWZy-azRnPc2bkfgJ0-VGSUbX1J2zMBWCZJuAu1pMEFCmfibK6srn1GC8q5nvBfH-lwIhGXhdObxEw4b5i_N8nx3m4s9S2S5BsK0RVy8BzfpolE4o5DQ8HPDxtu2DADMR3La5L0WNJ_wN-wRXimTuTrUayzjX_GdC5E00/s1700-e365/android-1.jpg)

"Taken together, this is a complete mobile compromise toolkit, the kind that used to require nation-state investment or bespoke exploit development, now sold on Telegram," Kelley said. "A single buyer gets full access to a target's location, messages, finances, camera, microphone, and keystrokes from a browser tab. Cross-platform support and active development make it a growing threat to both individuals and organizations."

The ZeroDayRAT malware is similar to numerous others that have targeted mobile device users, either via phishing or by infiltrating official app marketplaces. Over the past few years, bad actors have [repeatedly](https://thehackernews.com/2021/09/beware-this-android-trojan-stole.html) managed to [find various ways](https://thehackernews.com/2025/07/mobile-security-alert-352-iconads-fraud.html) to bypass [security protections](https://thehackernews.com/2025/07/cybercriminals-use-fake-apps-to-steal.html) put in place by Apple and Google to trick users into installing malicious apps.

Attacks targeting Apple's iOS have typically leveraged an [enterprise provisioning capability](https://developer.apple.com/documentation/devicemanagement/installing-profiles-on-devices) that allows organizations to install apps without the need for publishing them to the App Store. By marketing tools that combine spyware, surveillance, and information-stealing capabilities, they further lower the barrier of entry for less skilled hackers. They also highlight the evolving sophistication and persistence of mobile-focused cyber threats.

News of the commercial spyware platform coincides with the emergence of various mobile malware and scam campaigns that have come to light in recent weeks -

* An [Android remote access trojan (RAT) campaign](https://www.bitdefender.c...