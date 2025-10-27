---
title: New Android Trojan "BlankBot" Targets Turkish Users' Financial Data
url: https://thehackernews.com/2024/08/new-android-trojan-blankbot-targets.html
source: The Hacker News
date: 2024-08-06
fetch_date: 2025-10-06T18:06:24.594248
---

# New Android Trojan "BlankBot" Targets Turkish Users' Financial Data

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

# [New Android Trojan "BlankBot" Targets Turkish Users' Financial Data](https://thehackernews.com/2024/08/new-android-trojan-blankbot-targets.html)

**Aug 05, 2024**Ravie LakshmananMobile Security / Financial Security

[![Android Trojan](data:image/png;base64... "Android Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjyXNU7iyswUzrdKBOu4F8poERd5FcDJwbCH2bV6UKJhVtvpaTqdgg4efREVrJnmOmUecS1yU2JqpKxLq-ab2okl4m8YLAMCWOEky57fbjHshwgaLTu3JlZ8haHrPqym0-8TDYzX5ZQPxvnBhIiEVadl_rY4uHsv74VsPjHUQv5G99mD4uJHaiKYxhnBeI/s790-rw-e365/android.png)

Cybersecurity researchers have discovered a new Android banking trojan called BlankBot targeting Turkish users with an aim to steal financial information.

"BlankBot features a range of malicious capabilities, which include customer injections, keylogging, screen recording and it communicates with a control server over a WebSocket connection," Intel 471 [said](https://intel471.com/blog/blankbot-a-new-android-banking-trojan-with-screen-recording-keylogging-and-remote-control-capabilities) in an analysis published last week.

Discovered on July 24, 2024, BlankBot is said to be undergoing active development, with the malware abusing Android's accessibility services permissions to obtain full control over the infected devices.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The names of some of the malicious APK files containing BlankBot are listed below -

* app-release.apk (com.abcdefg.w568b)
* app-release.apk (com.abcdef.w568b)
* app-release-signed (14).apk (com.whatsapp.chma14)
* app.apk (com.whatsapp.chma14p)
* app.apk (com.whatsapp.w568bp)
* showcuu.apk (com.whatsapp.w568b)

Like the recently resurfaced [Mandrake](https://thehackernews.com/2024/07/new-mandrake-spyware-found-in-google.html) Android trojan, BlankBot implements a session-based package installer to circumvent the restricted settings feature introduced in Android 13 to block sideloaded applications from directly requesting dangerous permissions.

"The bot asks the victim to allow installing applications from the third-party sources, then it retrieves the Android package kit (APK) file stored inside the application assets directory with no encryption and proceeds with the package installation process," Intel 471 said.

The malware comes with a wide range of features to perform screen recording, keylogging, and inject overlays based on specific commands received from a remote server to harvest bank account credentials, payment data, and even the pattern used to unlock the device.

BlankBot is also capable of intercepting SMS messages, uninstalling arbitrary applications, and gathering data such as contact lists and installed apps. It further makes use of the accessibility services API to prevent the user from accessing device settings or launching antivirus apps.

"BlankBot is a new Android banking trojan still under development, as evidenced by the multiple code variants observed in different applications," the cybersecurity company said. "Regardless, the malware can perform malicious actions once it infects an Android device."

A Google spokesperson told The Hacker News that the company has not found any apps containing the malware on the Google Play Store.

“Android users are automatically protected against known versions of this malware by [Google Play Protect](https://support.google.com/googleplay/answer/2812853?hl=en), which is on by default on Android devices with Google Play Services,” the tech giant said. “Google Play Protect warns users and blocks apps that contain this malware, even when those apps come from sources outside of Play.”

The disclosure comes as Google outlined the various steps it's taking to combat threat actors' use of cell-site simulators like Stingrays to inject SMS messages directly into Android phones, a fraud technique referred to as SMS Blaster fraud.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"This method to inject messages entirely bypasses the carrier network, thus bypassing all the sophisticated network-based anti-spam and anti-fraud filters," Google [said](https://security.googleblog.com/2024/08/keeping-your-android-device-safe-from.html). "SMS Blasters expose a fake LTE or 5G network which executes a single function: downgrading the user's connection to a legacy 2G protocol."

The mitigation measures include a user option to [disable 2G](https://thehackernews.com/2023/08/new-android-14-security-feature-it.html) at the modem level and turn off [null ciphers](https://source.android.com/docs/whatsnew/android-14-release#disable-null-ciphers), the latter of which is an essential configuration for a False Base Station in order to inject an SMS payload.

Earlier this May, Google also [said](https://thehackernews.com/2024/05/android-15-introduces-new-features-to.html) it's stepping up cellular security by alerting users if their cellular network connection is unencrypted and if criminals are using cell-site simulators to snoop on users or send them SMS-based fraud messages.

*(The story was updated after publication to include a response from Google.)*

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

SHA...