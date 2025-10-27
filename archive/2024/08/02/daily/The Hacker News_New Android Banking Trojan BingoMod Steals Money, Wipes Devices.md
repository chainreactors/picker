---
title: New Android Banking Trojan BingoMod Steals Money, Wipes Devices
url: https://thehackernews.com/2024/08/new-android-banking-trojan-bingomod.html
source: The Hacker News
date: 2024-08-02
fetch_date: 2025-10-06T18:07:30.082800
---

# New Android Banking Trojan BingoMod Steals Money, Wipes Devices

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

# [New Android Banking Trojan BingoMod Steals Money, Wipes Devices](https://thehackernews.com/2024/08/new-android-banking-trojan-bingomod.html)

**Aug 01, 2024**Ravie LakshmananBanking Trojan / Cyber Fraud

[![Android Banking Trojan](data:image/png;base64... "Android Banking Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4aWKfJLWV9AOViLHLcGQL06kJTWjVn-qAWKWmh3MqnZE5DwQaElj3xTk4n11WaR5jeAeTZTUxlvCID5goZgaNN8VmyXHUi4bfzEquem6fTX31rXWLMrTM7RatunGBIRJyV4pqQboRxAegWHq8sLl7wUkfNSzxAA6nQ6VHWxhUGtCj_8xmas_PW9ceRISl/s790-rw-e365/android.gif)

Cybersecurity researchers have uncovered a new Android remote access trojan (RAT) called **BingoMod** that not only performs fraudulent money transfers from the compromised devices but also wipes them in an attempt to erase traces of the malware.

Italian cybersecurity firm Cleafy, which discovered the RAT towards the end of May 2024, said the malware is under active development. It attributed the Android trojan to a likely Romanian-speaking threat actor owing to the presence of Romanian language comments in the source code associated with early versions.

"BingoMod belongs to the modern RAT generation of mobile malware, as its remote access capabilities allow threat actors (TAs) to conduct Account Takeover (ATO) directly from the infected device, thus exploiting the on-device fraud (ODF) technique," researchers Alessandro Strino and Simone Mattia [said](https://www.cleafy.com/cleafy-labs/bingomod-the-new-android-rat-that-steals-money-and-wipes-data).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It's worth mentioning here that this technique has been observed in other Android banking trojans, such as [Medusa](https://thehackernews.com/2024/06/new-medusa-android-trojan-targets.html) (aka TangleBot), [Copybara](https://thehackernews.com/2024/03/new-banking-trojan-chavecloak-targets.html), and [TeaBot](https://thehackernews.com/2024/02/anatsa-android-trojan-bypasses-google.html) (aka Anatsa).

BingoMod, like [BRATA](https://thehackernews.com/2022/01/mobile-banking-trojan-brata-gains-new.html), also stands out for employing a self-destruction mechanism that's designed to remove any evidence of the fraudulent transfer on the infected device so as to hinder forensic analysis. While this functionality is limited to the device's external storage, it's suspected that the remote access features could be used to initiate a complete factory reset.

[![Android Banking Trojan](data:image/png;base64... "Android Banking Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhbCRlpR-N0i2pucaqUQzpdVjIQOQNnrfCKAiHtOWfvinBSQMHKvlt1MRIIz77ca5IONkbgZCGSUBt55bzXQwEi2M4WR0FgeOM8lSQe2Ik_KPHDKP2NXubpruPKHOnDdyHOuaqAfd6QszHWe95K8ojZwnGUuCdJcFxCWqvwdA7UxHffs3Uuuq26YR4Ko3Se/s790-rw-e365/cc.png)

Some of the identified apps masquerade as antivirus tools and an update for Google Chrome. Once installed via smishing tactics, the app prompts the user to grant it accessibility services permissions, using it to initiate malicious actions.

This includes executing the main payload and locking out the user from the main screen to collect device information, which is then exfiltrated to an attacker-controlled server. It also abuses the accessibility services API to steal sensitive information displayed on the screen (e.g., credentials and bank account balances) and give itself permission to intercept SMS messages.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXIsnD4_mUFvOG1WDAcHhYSJ7lEcqP7uhH4sT3_hrq5YqijlkLyhDo2YN1VvxEnh9T0yefLfG8q6uRprE1GL1fYDZNJY7h3Uk8M7HgbdUwMwW5EH9fj3GpVbpDSugDLVx1KUkBtdvVBY1VFy1hyCcJpYIeKYQUnX8GMddQQBX2RgNlA-Ms40YkxJ9TmiqE/s790-rw-e365/image.png)

To initiate money transfers directly from compromised devices, BingoMod establishes a socket-based connection with the command-and-control infrastructure (C2) to receive as many as 40 commands remotely to take screenshots using Android's [Media Projection API](https://developer.android.com/media/grow/media-projection) and interact with the device in real-time.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This also means that the ODF technique relies on a live operator to perform a money transfer of up to €15,000 (~$16,100) per transaction as opposed to leveraging an Automated Transfer System ([ATS](https://thehackernews.com/2023/05/hackers-targeting-italian-corporate.html)) to carry out financial fraud at scale.

Another crucial aspect is the threat actor's emphasis on evading detection using code obfuscation techniques and the ability to uninstall arbitrary apps from the compromised device, indicating that the malware authors are prioritizing simplicity over advanced features.

"In addition to real-time screen control, the malware shows phishing capabilities through Overlay Attacks and fake notifications," the researchers said. "Unusually, overlay attacks are not triggered when specific target apps are opened but are initiated directly by the malware operator."

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

[Android security](https://thehackernews.com/search/label/Android%20security)[bankin...