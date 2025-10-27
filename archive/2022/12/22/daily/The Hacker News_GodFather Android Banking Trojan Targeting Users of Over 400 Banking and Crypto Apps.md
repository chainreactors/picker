---
title: GodFather Android Banking Trojan Targeting Users of Over 400 Banking and Crypto Apps
url: https://thehackernews.com/2022/12/godfather-android-banking-trojan.html
source: The Hacker News
date: 2022-12-22
fetch_date: 2025-10-04T02:15:36.218135
---

# GodFather Android Banking Trojan Targeting Users of Over 400 Banking and Crypto Apps

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

# [GodFather Android Banking Trojan Targeting Users of Over 400 Banking and Crypto Apps](https://thehackernews.com/2022/12/godfather-android-banking-trojan.html)

**Dec 21, 2022**Ravie LakshmananMobile Security / Banking Trojan

[![Android Banking Trojan](data:image/png;base64... "Android Banking Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnYNn2FN7jMHXjd_GnHx18yKz5kd9TRrFPVh7fGP656itjnKjadp0uQLIz8lPdfSeyK5a0Rgwr40kZCvqBxDhz2Wg6LSy05E5LhDV5CNBsblISh83K6-EeUnIxsJCwetI-moZIHBTXo3H97iWywjCXhSCG7LAfwQtvbtgeNvjc2fDrgMvltkFDHih0/s790-rw-e365/gibbb.png)

An Android banking trojan known as **GodFather** is being used to target users of more than 400 banking and cryptocurrency apps spanning across 16 countries.

This includes 215 banks, 94 crypto wallet providers, and 110 crypto exchange platforms serving users in the U.S., Turkey, Spain, Italy, Canada, and Canada, among others, Singapore-headquartered Group-IB [said](https://blog.group-ib.com/godfather-trojan) in a report shared with The Hacker News.

The malware, like [many](https://thehackernews.com/2022/10/hackers-using-vishing-tactics-to-trick.html) [financial](https://thehackernews.com/2022/11/these-two-google-play-store-apps.html) [trojans](https://thehackernews.com/2022/11/this-android-file-manager-app-infected.html) targeting the Android ecosystem, attempts to steal user credentials by generating convincing overlay screens (aka web fakes) that are served atop target applications.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

First detected by Group-IB in June 2021 and [publicly disclosed](https://twitter.com/ThreatFabric/status/1505932079401480198) by ThreatFabric in March 2022, GodFather also packs in native backdoor features that allows it to abuse Android's Accessibility APIs to record videos, log keystrokes, capture screenshots, and harvest SMS and call logs.

[![Android Banking Trojan](data:image/png;base64... "Android Banking Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjFCdMUO8WNv8PmAois5XmkjboTGhCcakwxjiaXSw139VZ9y_psTcLfW9EAkMyCNBiOc59REGpvZF6X0Hc6JZlYuM_FQru3lCW9iDo_DJpcRi6QtboYbQaUa6XizR5rUJ1sd-GOvmjipzLzr9iA7vYi_xB2-cfwPTHa-JK4GXM88kdE4L3nijVbusN/s790-rw-e365/gib-2.png)

Group-IB's analysis of the malware has revealed it to be a successor of [Anubis](https://www.threatfabric.com/blogs/anubis_2_malware_and_afterlife.html), another banking trojan that had its source code leaked in an underground forum in January 2019. It's also said to be distributed to other threat actors through the malware-as-a-service (MaaS) model.

The similarities between the two malware families extend to the method of receiving the command-and-control (C2) address, implementation of C2 commands, and the web fake, proxy and screen capture modules. However, audio recording and location tracking features have been removed.

"Interestingly, GodFather spares users in post-Soviet countries," Group-IB said. "If the potential victim's system preferences include one of the languages in that region, the Trojan shuts down. This could suggest that GodFather's developers are Russian speakers."

What makes GodFather stand out is the fact that it retrieves its command-and-control (C2) server address by decrypting actor-controlled Telegram channel descriptions that are encoded using the [Blowfish cipher](https://en.wikipedia.org/wiki/Blowfish_%28cipher%29).

[![Android Banking Trojan](data:image/png;base64... "Android Banking Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhD9Qjuk7M5k3XsUUAKI-eAzVMxf3EUsNJ_GOqOX5zrrMtxFvjAi48o1d53qDDhZSzpIf_0rRaH9DkBgtH3cqLt7jGI9fQIFdeZ7pmK6WMZoVF5j_-VhYGz4bBksC84Sglyk472bkIg_UgQvT8mx-An7-gMQpMqOne7hfaEOIxMz72vzWeyFMe4m76S/s790-rw-e365/gib.png)

The exact modus operandi employed to infect user devices is not known, although an examination of the threat actor's command-and-control (C2) infrastructure reveals trojanized dropper apps as one potential distribution vector.

This is based on a C2 address that's linked to an app named Currency Converter Plus (com.plus.currencyconverter) that was hosted on the Google Play Store as of June 2022. The application in question is no longer available for download.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Another artifact examined by Group-IB impersonates the legitimate [Google Play Protect](https://developers.google.com/android/play-protect) service that, upon being launched, creates an [ongoing notification](https://developer.android.com/reference/android/app/Notification.Builder.html#setOngoing(boolean)) and hides its icon from the list of installed applications.

The findings come as Cyble [discovered](https://blog.cyble.com/2022/12/20/godfather-malware-returns-targeting-banking-users/) a number of GodFather samples masquerading as the MYT Müzik app aimed at users in Turkey.

"[Google Play Protect](https://support.google.com/googleplay/answer/2812853) checks Android devices with Google Play Services for potentially harmful apps from other sources," a Google spokesperson told The Hacker News. "Users are protected by Google Play Protect, which blocks these identified malicious apps on Android devices."

GodFather is not the only Android malware based on Anubis. Earlier this July, ThreatFabric revealed that a modified version of Anubis known as [Falcon](https://twitter.com/threatfabric/status/1547194667598594050) targeted Russian users by impersonating the state-owned VTB Bank.

"The emergence of GodFather underscores the ability of threat actors to edit and update their tools to maintain their effectiveness in spite of efforts by malware detection and prevention providers to update their products," Group-IB researcher Artem Grischenko said.

"With a tool like GodFather, threat actors are limited only by their ability to create convincing web fakes for a particular application. Sometimes, the sequel really can be better than the original."

Found this article interest...