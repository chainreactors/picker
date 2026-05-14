---
title: Android Adds Intrusion Logging for Sophisticated Spyware Forensics
url: https://thehackernews.com/2026/05/android-adds-intrusion-logging-for.html
source: The Hacker News
date: 2026-05-13
fetch_date: 2026-05-14T05:47:24.007767
---

# Android Adds Intrusion Logging for Sophisticated Spyware Forensics

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [Android Adds Intrusion Logging for Sophisticated Spyware Forensics](https://thehackernews.com/2026/05/android-adds-intrusion-logging-for.html)

**Ravie Lakshmanan**May 13, 2026Encryption / Spyware

[![Android Adds Intrusion Logging](data:image/png;base64... "Android Adds Intrusion Logging")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBNoTD0wrxHsoNUfZVLT2ImOUNC-2Md_wih6gTim-zbqkCzgGfXbtvlDgDMWeczo9RzINqu7qqk_3XK0KHSdbpLMPbR9xg_pLpjtoxugUt3B5-G9pL9wBCMI80Rx-Aw9eNxH-XXE2XpQHDtqaGDeXe3P4mGDvPgmDiqom8B2Xdfz7irCpOZVvhP9jsqudo/s1700-e365/adnroid-Intrusion-Logging.jpg)

Google on Tuesday [unveiled](https://blog.google/security/whats-new-in-android-security-privacy-2026/) a new opt-in Android feature called **Intrusion Logging** for storing forensic logs to better analyze sophisticated spyware attacks.

Intrusion Logging, available as part of [Advanced Protection Mode](https://support.google.com/android/answer/16339980), enables "persistent and privacy-preserving forensics logging to allow for investigation of devices in the event of a suspected compromise," the company said.

The feature, it added, was developed in partnership with Amnesty International and Reporters Without Borders. According to a [help document](https://support.google.com/android/answer/16927813) shared by Google, it logs device and network activities on a daily basis, including information about device behavior and the various applications that run on it.

The kinds of activities recorded are listed below -

* App activity (e.g., when an app process starts)
* App installations, updates, and uninstalls
* Network connections like starting and stopping Wi-Fi, Bluetooth, DNS lookups, and IP addresses
* File transfers to or from the device over USB
* Changes to system certificates
* When the device is locked or unlocked

Google also noted that the log data is end-to-end encrypted by the device and stored on Google servers. The encryption keys are secured by Google Account password and screen lock credentials, meaning the logs cannot be accessed by any third-party, including Google itself, apart from the device owner.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

"By storing the data on a secure server, even malware installed on the smartphone cannot access, delete, or manipulate it," Reporters Without Borders [said](https://www.reporter-ohne-grenzen.de/en/artikel/blog/4242/new-protection-feature-against-sophisticated-spyware-advanced-protection-mode-for-android). "End-to-end encryption also ensures that neither Google nor state actors can access the data. The Intrusion Logging function in particular enables detection and forensic analysis of even highly sophisticated and previously difficult-to-detect attacks."

The encrypted logs are stored for a period of 12 months, after which they are automatically wiped. Once Intrusion Logging is enabled, a user cannot delete the logs before the 12-month expiration window, even if the account is closed or the feature is turned off. Users have the option to download the logs offline, should they prefer to keep them for longer periods.

That said, Google has emphasized that once the logs are downloaded and decrypted, users are responsible for their security. "In certain legal or regulatory environments, you may be required by law to provide access to your decrypted data or your security credentials," it pointed out.

Another thing to keep in mind when enabling the feature is that it also records network events generated during Chrome Incognito browsing, such as DNS lookups and IP connections, as it operates at the system level and does not distinguish between the browsing modes. In other words, anybody with access to the decrypted logs can glean what websites were visited, but cannot infer specific pages on those sites.

The motivation behind Intrusion Logging is that a high-risk individual, who suspects they may have been targeted by advanced surveillance tools because of who they are and what they do, can share the activity log with trusted security experts for detailed examination.

The logs can be downloaded by navigating to the Settings app, and then tapping Security & privacy -> Advanced Protection -> Intrusion Logging -> Access logs. The feature is currently rolling out to all devices running the Android 16 December update and newer.

"With Intrusion Logging, Google is the first major vendor to proactively address the challenge of detecting advanced attacks on devices," Donncha Ó Cearbhaill, head of Security Lab at Amnesty International, [said](https://securitylab.amnesty.org/latest/2026/05/android-intrusion-logging-as-a-new-source-of-data-for-consensual-forensic-analysis/) in a statement. "By making more consensual forensic data available for researchers, we can make life more difficult for attackers and help civil society seek accountability when their devices are unlawfully targeted by spyware and mobile data extraction tools."

### Other Privacy and Security Features Coming to Android

Besides Intrusion Logging, Google has announced a raft of privacy and security improvements, including verified financial calls, a new phone call spoofing protection feature to combat attacks where scammers impersonate banks to trick users into revealing sensitive data or transferring funds.

When users receive a call that appears to be from a participating bank, Android asks the installed online banking app to confirm if they are actually attempting to reach the customer. If the app confirms no such is being made, the call is automatically ended by the system.

"Your bank or financial institution may also designate numbers as inbound-only, meaning they never use them to call customers," Google said. "Incoming calls from these numbers will be ended directly." The feature is expected to go live on Android 11+ devices with Revolut, Itaú, and Nubank in the coming weeks, before expanding to more banks later this year.

[![Cybersecurity](data:image/png;ba...