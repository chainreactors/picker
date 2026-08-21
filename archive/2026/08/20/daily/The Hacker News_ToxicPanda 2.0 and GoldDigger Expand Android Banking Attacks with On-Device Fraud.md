---
title: ToxicPanda 2.0 and GoldDigger Expand Android Banking Attacks with On-Device Fraud
url: https://thehackernews.com/2026/08/toxicpanda-20-and-golddigger-expand.html
source: The Hacker News
date: 2026-08-20
fetch_date: 2026-08-21T03:05:10.083241
---

# ToxicPanda 2.0 and GoldDigger Expand Android Banking Attacks with On-Device Fraud

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [ToxicPanda 2.0 and GoldDigger Expand Android Banking Attacks with On-Device Fraud](https://thehackernews.com/2026/08/toxicpanda-20-and-golddigger-expand.html)

**Ravie Lakshmanan**Aug 20, 2026Malware / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhq19iWDNnvPUAAC2_MJN09g-1SHoPWQv82zvmQGTvrniDXm9BUWK73QrKCNCgxk0uGp6MrKF8cDQrigQCI3CW1G8V8GNltJ0GRc-yBjt69zPem4YW_b0XCZwsIFhWiOoul7eIhEOjb_F0X9A9B_DOmQNbCWHF6AzqDro4U0XjH_CgtJ_J0MVZjDPmyDL1p/s1700-e365/android-banking-malware.jpg)

Cybersecurity researchers have shed light on an updated version of [ToxicPanda](https://thehackernews.com/2025/02/new-tgtoxic-banking-trojan-variant.html) (aka TgToxic) that comes with "significant enhancements," including a set of 167 remote commands and expands its targeting footprint globally.

Zimperium zLabs, in a [Wednesday report](https://zimperium.com/blog/the-toxicpanda-never-sleeps-toxicpanda-2.0-prepares-its-next-strike-on-mobile), said the Android malware also features a PIN harvesting workflow targeting more than 140 banking and cryptocurrency applications. ToxicPanda is known to be active in the wild since at least July 2022.

"By abusing the Android accessibility service, threat actors can steal every UI element on the screen, alongside an overlay-based credential theft mechanism targeting 349 financial institutions [across 16 countries], compared to the previous version, which targeted only 16 banking applications, the latest iteration demonstrates a significant expansion in targeting scope and capabilities," security researcher Vishnu Pratapagiri said.

The new version also fleshes out some of the [previously unimplemented commands](https://thehackernews.com/2024/11/new-android-banking-malware-toxicpanda.html), siphons lock screen credentials using a fake overlay, and introduces an automated click-based mechanism to abuse [Android Wireless Debugging](https://developer.android.com/tools/adb#connect-to-a-device-over-wi-fi) via Android Debug Bridge (ADB) to facilitate privilege escalation and shell-level access on compromised devices. It achieves this by using the accessibility services to enable Developer Options and turn on Wireless debugging.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

ToxicPanda 2.0 connects to its command-and-control (C2) server by sending an initial HTTPS request to establish a bidirectional WebSocket communication channel to receive commands and exchange data. Like in the case of the [newly-discovered Manic](https://thehackernews.com/2026/08/manic-android-malware-exfiltrates-data.html), the Android malware can display full-screen "system update" overlays to conceal its background actions and deploy an invisible transparent overlay to capture touch and harvest PIN codes.

Other newly added functionalities include a prompt to trick the victim into granting Device Administrator privileges, overwriting the device's local lock screen PIN or password with an attacker-defined value, and profiling the infected device to determine the OEM vendor and take appropriate steps to exempt the malware from battery optimization policies using accessibility services and ensure uninterrupted background execution.

"The updated campaign also reveals a shift in distribution methods, with ToxicPanda 2.0 samples being delivered through Amazon AWS-hosted buckets, indicating the attackers are leveraging cloud infrastructure for malware delivery," Zimperium said.

### New GoldDigger Campaign Targets South Africa, U.K.

The third Android banking trojan to come under the security radar is [GoldDigger](https://thehackernews.com/2024/02/chinese-hackers-using-deepfakes-in.html), which was first documented by Group-IB in October 2023 as capable of carrying out on-device fraud. It's attributed to GoldFactory, a Chinese-speaking threat actor linked to other banking malware families targeting both Android and iOS, such as GoldPickaxe, GoldDiggerPlus, and GoldKefu.

According to IBM Trusteer, GoldDigger makes use of a sophisticated packer called "dpt-shell" to obfuscate its code and resources in an attempt to resist analysis. The packer also implements a bevy of evasion techniques: encrypting its native logic; detecting if Frida is attached to the process and, if so, crashing it; preventing external debuggers from attaching by marking itself as being traced using the PTRACE system call.

The current GoldDigger campaign mainly impersonates airline companies and shopping retailers, resulting in a "massive infection" in South Africa and the U.K. Victims who end up installing these apps are asked to grant accessibility services permissions, which the malware abuses for fraudulent actions.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

"GoldDigger can inject input to the banking app to mimic user interaction, such as entering text, clicking buttons, and performing gestures," security researcher Shahar Tavor Lusky [said](https://www.ibm.com/think/security/golddigger-android-malware-analysis). In doing so, GoldDigger initiates fraudulent transactions from the victim's banking app to the attacker."

GoldDigger can also give the operator real-time access to the victim's screen, capture credentials entered on banking apps using fake overlays, and run a targeted app within a virtual environment, giving the attacker full visibility into its runtime behavior and real-time interception of credentials and sensitive data.

For C2, the malware establishes a WebSocket connection to receive commands that allow it to request accessibility and location permissions; capture input from any app using the accessibility services; collect contacts and SMS messages; record audio and video and stream it using the RTMP protocol to the C2 server, open specific URLs; and open specific apps (e.g., Google Play Store and Settings).

To stay safe against these threats, it's advised to review installed applications ...