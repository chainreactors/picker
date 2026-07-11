---
title: Study of 281 Free Android VPN Apps Finds Traffic Leaks, Unencrypted Data, and Tracking
url: https://thehackernews.com/2026/07/study-of-281-free-android-vpn-apps.html
source: The Hacker News
date: 2026-07-10
fetch_date: 2026-07-11T05:04:37.742209
---

# Study of 281 Free Android VPN Apps Finds Traffic Leaks, Unencrypted Data, and Tracking

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Study of 281 Free Android VPN Apps Finds Traffic Leaks, Unencrypted Data, and Tracking](https://thehackernews.com/2026/07/study-of-281-free-android-vpn-apps.html)

**Swati Khandelwal**Jul 10, 2026Mobile Security / Privacy

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGJR5fh4xv_X2JER6SMxM62unaK2pucigiJwiE69bCR9n3fgVMqlH2zWpTsmiy4d936R46czjNmkAjDpU7yZgPMl6KFp7phz3kQ9sO1XaE3JHMW0VCUtwN3_zOqOcUfKdbJTJjWjahA44NPMXMif0JqnO_kzJDfuHT0HJvtOlndAvheFqNrpviHXVQ_DIb/s1700-e365/android-vpn-security.jpg)

Researchers ran 281 of the most popular free VPN apps on the Google Play Store through a new testing system and found that many fail at the basics people install a VPN for, i.e., keeping their traffic private and secure.

The apps flagged with at least one problem have been installed more than 2.4 billion times.

The problems are basic, not sophisticated. 29 apps let user traffic leak outside the encrypted tunnel, including the DNS lookups that reveal which websites you visit. 61 apps send some data in plain text that anyone watching the traffic on that network can read.

Five of those send the app's configuration file in the clear, which lets an attacker on the network redirect the connection to a server they control.

The system, called **MVPNalyzer**, was presented at the NDSS security conference in February 2026 by researchers at the University of Michigan, the University of New Mexico, and IIT Delhi.

It is a mobile counterpart to the same lab's earlier VPNalyzer study of desktop VPN software, and the researchers describe it as the first framework built to systematically and repeatedly audit Android VPN apps.

A VPN wraps your traffic in an encrypted tunnel so your internet provider, or an eavesdropper on the network, cannot see what you are doing. The trade-off is that the VPN app now sees all of it. You are not removing the need to trust someone. You are moving that trust from your internet provider to whoever built the app.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The study asks whether these apps earn it. For many, they do not.

## The most serious flaw: tunnel hijacking

The worst finding involves those five apps that download their configuration file without encryption. That file tells the app which server to connect to. If it travels in plain text, an attacker on the same network, say a public Wi-Fi operator, can rewrite it in transit and point the app at a server they control.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgy0uf9Xbvzs8uQR1k4Eyza_1u_RG-6Nfa6k2EiqmB9TKLnO6g29yLWdKCJJ-SQeGvZRMV9nQMwQSYYF8uKJNaxRWcZJ4gIMpyJoQkUmhBbMBYaRA5N5AX0QLWPnwenRzt_ARKhTUpNyXcJkPVJwfRKhE3Y5NzsUEjkinDD64XrD2nQSHSSDB_u9B-s7s6d/s1700-e365/MVPNalyzer.jpg) |
| Architecture of the MVPNalyzer framework |

The user connects, sees the usual "connected" screen, and routes everything through the attacker. The researchers built this attack and confirmed it worked on phones under their control.

They flagged the issue for all five providers as a priority. Two responded, both promising to move the file to HTTPS. One said it would send the configuration files ["securely using HTTPS with proper certificate validation."](https://www.ndss-symposium.org/wp-content/uploads/2026-s1573-paper.pdf) The other three had not acknowledged it.

## Leaks, and apps that hide nothing

Of the 29, 24 leaked DNS traffic, exposing the sites users visited to the local network; those apps alone account for about 360 million installs. Six leaked full browsing traffic outside the tunnel, and four ran "tunnels" with no encryption at all, with some apps failing in more than one way.

Separately, 169 apps made no attempt to disguise their traffic as anything other than a VPN, so a network operator or government censor can spot and block them with basic tools. Nearly two-thirds of those apps advertise that they beat blocking or unlock restricted content. They make the promise and do nothing to keep it.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiaY3x8USOFkQVfHB6GVrC6nYVCkbo_NlWSKwSNcuXEwVV2FHshzGEOysqr38tE8OS888yC8146_ONZ0x6JPF2HBEnbUdzoNusx3LjOR-xPRjFn_wkNRPx7S60ouNDKW6K6PbvcQ8Tx4BLsl79RdxJw5ocBf4mkXvrwU9kM-YVYThhy42UmGkTND3sf8Ymm/s1700-e365/appss.jpg)

For someone in a country where using a VPN is itself risky, being easy to identify as a VPN user is the opposite of what they signed up for.

## Tracking, from the apps built to stop it

People often install VPNs to avoid being tracked. Many of these apps track anyway. 76 sent the device's Advertising ID, a unique code advertisers use to follow a person from one app to the next.

The study found that more than 80% of the apps, 246 of them, contacted known advertising and tracking servers. Many also sent details like the phone model, operating system version, and screen size.

On their own, those look harmless, but combined, they form a "fingerprint" that can single out one device. One app even sent the phone's exact GPS coordinates.

## Weak setups under the hood

The researchers also pulled apart the OpenVPN configuration files bundled with 108 of the apps, a separate check from the live-traffic tests above. Only one followed every security best practice the study measured.

About 89% relied on a single authentication method, either a password or a certificate, rather than combining the two. Nearly one in five used weak or outdated encryption, including the aging Blowfish cipher and triple DES. A few set the tunnel's data cipher to none, which switches off encryption entirely. Both of those old ciphers carry long-known weaknesses ([CVE-2016-6329](https://nvd.nist.gov/vuln/detail/CVE-2016-6329) and [CVE-2016-2183](https://nvd.nist.gov/vuln/detail/CVE-2016-2183)) that let an attacker recover data from long-running connections.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/...