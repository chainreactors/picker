---
title: HOOK Android Trojan Adds Ransomware Overlays, Expands to 107 Remote Commands
url: https://thehackernews.com/2025/08/hook-android-trojan-adds-ransomware.html
source: The Hacker News
date: 2025-08-27
fetch_date: 2025-10-07T00:50:37.024524
---

# HOOK Android Trojan Adds Ransomware Overlays, Expands to 107 Remote Commands

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

# [HOOK Android Trojan Adds Ransomware Overlays, Expands to 107 Remote Commands](https://thehackernews.com/2025/08/hook-android-trojan-adds-ransomware.html)

**Aug 26, 2025**Ravie Lakshmanan

[![HOOK Android Trojan](data:image/png;base64... "HOOK Android Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjRQ9AfKzutLoED2HaIQb60XGXwY68DrgQavTYr-z2ltyzoAimYk8Asni72-_OF6MQMPAtsgc9lR7FQmqAEsIIyCeJmhDHGPAiMj-XU8ABQYPn1fWn_I3M1pLlXtO7cw701ZJPPtXl6fkpUf3YkUsILWgEtxqWxOpV_GHZtcIgTaaqxywhan_8M6L1Sr5se/s790-rw-e365/mobile-ransomware.jpg)

Cybersecurity researchers have discovered a new variant of an Android banking trojan called HOOK that features ransomware-style overlay screens to display extortion messages.

"A prominent characteristic of the latest variant is its capacity to deploy a full-screen ransomware overlay, which aims to coerce the victim into remitting a ransom payment," Zimperium zLabs researcher Vishnu Pratapagiri [said](https://zimperium.com/blog/hook-version-3-the-banking-trojan-with-the-most-advanced-capabilities). "This overlay presents an alarming '\*WARNING\*' message, alongside a wallet address and amount, both of which are dynamically retrieved from the command-and-control server."

The mobile security company said the overlay is remotely initiated when the command "ransome" is issued by the C2 server. The overlay can be dismissed by the attacker by sending the "delete\_ransome" command.

HOOK is [assessed](https://thehackernews.com/2023/09/hook-new-android-banking-trojan-that.html) to be an offshoot of the [ERMAC](https://thehackernews.com/2025/08/ermac-v30-banking-trojan-source-code.html) banking trojan, which, coincidentally, had its source code leaked on a publicly accessible directory over the internet.

Like other banking malware targeting Android, it's capable of displaying a fake overlay screen on top of financial apps to steal users' credentials and abuse Android accessibility services to automate fraud and commandeer devices remotely.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Other notable features include the ability to send SMS messages to specified phone numbers, stream the victim's screen, capture photos using the front-facing camera, and steal cookies and recovery phrases associated with cryptocurrency wallets.

The latest version, per Zimperium, signals a major step forward, supporting 107 remote commands, with 38 newly added ones. This includes serving transparent overlays to capture user gestures, fake NFC overlays to trick victims into sharing sensitive data, and deceptive prompts to gather lockscreen PIN or pattern.

[![HOOK Android Trojan](data:image/png;base64... "HOOK Android Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQYB6QiV5dpAdmILr9l2kou2MTun6khnGdk_OryNE1s6CaqJG_9-Ew7Fl2qILqQRkovBaxnzGA5TdiF19VUp0UFeVXFj1eI-kaqGyx_kFrT2zu-YwrOPDPQS-3EgMjuo7Qwpq0twIl-mnYzPsvs5GHvqstMqmSVi2sLZHLbC5soQ9OoboqiOUN7RWHy35x/s790-rw-e365/appsss.jpg)

The list of newly added commands is as follows -

* **ransome**, to show ransomware overlay on top of the device
* **delete\_ransome**, to remove the ransomware overlay
* **takenfc**, to display a fake NFC scanning screen using a fullscreen WebView overlay and read card data (it, however, does not include the necessary functionality to collect and send the data to the attacker)
* **unlock\_pin**, to display a fake device unlock screen to collect unlock pattern or PIN code and gain unauthorized access to the device
* **takencard**, to display a fake overlay to collect credit card information by mimicking a Google Pay interface
* **start\_record\_gesture**, to record user gestures by displaying a transparent full screen overlay

HOOK is believed to be distributed on a large scale, using phishing websites and bogus GitHub repositories to host and disseminate malicious APK files. Some of the other Android malware families distributed via GitHub include ERMAC and [Brokewell](https://thehackernews.com/2024/04/new-brokewell-android-malware-spread.html), indicating a broader adoption among threat actors.

"The evolution of HOOK illustrates how banking trojans are rapidly converging with spyware and ransomware tactics, blurring threat categories," Zimperium noted. "With continuous feature expansion and broad distribution, these families pose a growing risk to financial institutions, enterprises, and end users alike."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvSu4hlRXrUli3-kmDDH7thbd3BbP5mthEuWaRbr5w0wqX6QqG1oLfJ6Vwnqm-qa5bmoqJDd_kFHc9QPzacnLxUD6dWOKao4FXqYE2K0aX8Gae1pwUbO6j7ilL2B854FRyrPIt_yDjDPPJFG_wGEvTiUs0h6BD4VeYI80arQ-r-f3KbVQ0Z_k4v8ebvhvV/s790-rw-e365/code.png)

### Anatsa Continues to Evolve

The disclosure comes as Zscaler's ThreatLabs detailed an updated version of the Anatsa banking trojan that has now expanded its focus to target over 831 banking and cryptocurrency services worldwide, including those in Germany and South Korea, up from 650 reported previously.

One of the apps in question has been found to mimic a file manager app (package name: "com.synexa.fileops.fileedge\_organizerviewer"), which acts as a dropper to deliver Anatsa. Besides replacing dynamic code loading of remote Dalvik Executable (DEX) payloads with direct installation of the trojan, the malware uses corrupted archives to hide the DEX payload that's deployed during runtime.

Anatsa also requests permissions for Android's accessibility services, which it subsequently abuses to grant itself additional permissions that allow it to send and receive SMS messages, as well as draw content on top of other applications to display overlay windows.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

In all, the company said it identified 77 malicious apps from various adware, maskware, and malware families, such as Anatsa, [Joker](https://thehackernews.com/2022/07/several-new-play-store-apps-spotted.html), and Harly...