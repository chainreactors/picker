---
title: Cybercriminals Use Fake Apps to Steal Data and Blackmail Users Across Asia’s Mobile Networks
url: https://thehackernews.com/2025/07/cybercriminals-use-fake-apps-to-steal.html
source: The Hacker News
date: 2025-07-30
fetch_date: 2025-10-06T23:57:43.925431
---

# Cybercriminals Use Fake Apps to Steal Data and Blackmail Users Across Asia’s Mobile Networks

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

# [Cybercriminals Use Fake Apps to Steal Data and Blackmail Users Across Asia's Mobile Networks](https://thehackernews.com/2025/07/cybercriminals-use-fake-apps-to-steal.html)

**Jul 29, 2025**Ravie LakshmananMalware / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQuckNU07ZmlLXVVfT7d1Akb3lDZVlgaPp_7QHm0yctmAp_Xv8g6NdB7k8EczY8MvtyZpDzWuG59tlOY2R_eHwdhII1gDKwRo8PUymse-pBBJ05b_cVp7ZQXtS9-C5jM9R9Rg4TJ1NJU9JGfjlmgxUtphGohTTY7By3Y7TyrCusBbXlfL7QkPBSG2A5A2F/s790-rw-e365/appsss.jpg)

Cybersecurity researchers have discovered a new, large-scale mobile malware campaign that's targeting Android and iOS platforms with fake dating, social networking, cloud storage, and car service apps to steal sensitive personal data.

The cross-platform threat has been codenamed SarangTrap by Zimperium zLabs. Users in South Korea appear to be the primary focus.

"This extensive campaign involved over 250 malicious Android applications and more than 80 malicious domains, all disguised as legitimate dating and social media applications," security researcher Rajat Goyal [said](https://zimperium.com/blog/the-dark-side-of-romance-sarangtrap-extortion-campaign).

The bogus domains, which impersonate legitimate app store listing pages, are used as a lure to trick users into installing these apps, resulting in the exfiltration of contact lists and images, all while keeping up an illusion of legitimacy.

Once installed, the Android apps also prompt the victim to enter an invitation code, after which it's validated against a command-and-control (C2) server. The app then proceeds to request sensitive permissions that allow it access to SMS messages, contact lists, and files under the pretext of offering the advertised functionality.

Coupling the activation of the malicious behavior to an invitation code is, by turns, clever and sneaky as it allows the malware to evade dynamic analyses and antivirus scans and silently hoover data.

The iOS version of the campaign has been found to entice users into installing a deceptive mobile configuration profile on their device, and then use the configuration to facilitate the app installation to capture contacts, photos, and the photo library.

The campaign is said to be in active development, with new variants of the malware samples limiting themselves to collecting contacts, images, and device information to an external server. There is also evidence that the threat actors behind the activity have resorted to blackmailing victims with threats to share personal videos with family members.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5gwCwlwVhUQgdM5I0pI0JAS0E990bdKsbKb3wxs8apz5SLn6sMQEhUk2oHd7gxZPnqBF1qIlFz5fAbPj3wVLhsHI1hFXMUxYyYJqjAwlPNpQxAio3djgEXRzPBwBZEa7aCErT27Y1FVXAXPNV7swaWkJBZJhp_JQY3w54p3ldXHibQe_NCW7pLBUhpc3z/s790-rw-e365/apps.jpg)

"This unsettling story is not an isolated incident; it highlights the psychological manipulation and social engineering tactics that these campaigns employ to take advantage of emotional vulnerability," Goyal said.

"Victims are enticed into installing malware with the promise of companionship, only to discover that they are caught in a cycle of surveillance, extortion, and humiliation."

The disclosure comes in the wake of another campaign that has set up 607 Chinese-language domains to distribute malicious application files (APKs) posing as the Telegram messaging app via a QR code embedded on the site and execute remote commands in real-time to enable data theft, surveillance, and control over the device using the [MediaPlayer API](https://developer.android.com/reference/android/media/MediaPlayer).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The APK was signed with a [v1 signature scheme](https://source.android.com/docs/security/features/apksigning), making it vulnerable to the [Janus vulnerability](https://thehackernews.com/2017/12/android-malware-signature.html) on Android 5.0 – 8.0," BforeAI [said](https://bfore.ai/report/malicious-telegram-apk-campaign-advisory/). "This [vulnerability](https://www.trendmicro.com/en_us/research/17/l/janus-android-app-signature-bypass-allows-attackers-modify-legitimate-apps.html) allows attackers to craft deceptive applications."

"After crafting the malicious application, it is then repackaged using its original v1 signature. This modification goes undetected, allowing the compromised app to be installed without causing suspicion. In essence, it enables attackers to make an app more dangerous, redistribute it as an APK, and trick users (especially on older devices) into installing it while completely bypassing security checks."

Mimicking trusted and popular online platforms has been a successful compromise vector, as evidenced by Android campaigns that are targeting Indian bank customers and Bengali-speaking users, particularly people from Bangladesh living in Saudi Arabia, Malaysia, and the United Arab Emirates, with malicious apps posing as financial services distributed via phishing sites and Facebook pages.

The applications are designed to deceive users into entering their personal information as part of a supposed account creation process, as well as capture data provided by them in the fake transaction interfaces engineered to simulate mobile money transfers, bill payments, and bank transfers. In reality, no actual transaction is carried out.

"While the attack techniques are not new, the campaign's cultural targeting and sustained activity reflect how cybercriminals continue to adapt their strategies to reach specific communities," McAfee Labs researcher Dexter Shin [said](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/fake-android-money-transfer-app-targeting-bengali-speaking-users/).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-WLRBCY_CkFsTsHopb40X3fUNctXvXYYDcNdZ4RoZyT7EikKa9BWTjSYbhR49_h2_q9mfgXgo-qnBwg5W8DXM7J5tmXAdxmALhj2xk...