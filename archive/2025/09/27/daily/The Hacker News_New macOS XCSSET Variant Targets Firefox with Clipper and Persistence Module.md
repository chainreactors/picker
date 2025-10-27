---
title: New macOS XCSSET Variant Targets Firefox with Clipper and Persistence Module
url: https://thehackernews.com/2025/09/new-macos-xcsset-variant-targets.html
source: The Hacker News
date: 2025-09-27
fetch_date: 2025-10-02T20:48:19.605353
---

# New macOS XCSSET Variant Targets Firefox with Clipper and Persistence Module

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

# [New macOS XCSSET Variant Targets Firefox with Clipper and Persistence Module](https://thehackernews.com/2025/09/new-macos-xcsset-variant-targets.html)

**Sep 26, 2025**Ravie LakshmananMalware / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1NQZ1_CMdaFHeJjrt-6LSIVEQ7v4DE1j8qVuoGeZ5jZbnLtLKNP0529bksz1qw4VpBFjyvOYj7bw26VzjQ1_IkJOWN1tjHBx6surinXOv5J3BklKlyKMWF48RbwB6MV0AlgaVqOVhLxbMp2oFqivLoeM1zOuw3azsY0TuQsXikV55FPhUwPNs1QiJcZN8/s790-rw-e365/macos-firefox.jpg)

Cybersecurity researchers have discovered an updated version of a known Apple macOS malware called **XCSSET** that has been observed in limited attacks.

"This new variant of XCSSET brings key changes related to browser targeting, clipboard hijacking, and persistence mechanisms," the Microsoft Threat Intelligence team [said](https://www.microsoft.com/en-us/security/blog/2025/09/25/xcsset-evolves-again-analyzing-the-latest-updates-to-xcssets-inventory/) in a Thursday report.

"It employs sophisticated encryption and obfuscation techniques, uses run-only compiled AppleScripts for stealthy execution, and expands its data exfiltration capabilities to include Firefox browser data. It also adds another persistence mechanism through LaunchDaemon entries."

XCSSET is the name assigned to a sophisticated modular malware that's designed to infect Xcode projects used by software developers and unleash its malicious capabilities when it's being built. Exactly how the malware is distributed remains unclear, but it's suspected that the propagation relies on the Xcode project files being shared among developers building apps for macOS.

Earlier this March, Microsoft [uncovered](https://thehackernews.com/2025/02/microsoft-uncovers-new-xcsset-macos.html) several enhancements to the malware, highlighting its improved error handling and the use of three different persistence techniques to siphon sensitive data from compromised hosts.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The latest variant of XCSSET has been found to incorporate a clipper sub-module that monitors clipboard content for specific regular expression (aka regex) patterns matching various cryptocurrency wallets. In the event of a match, the malware proceeds to substitute the wallet address in the clipboard with an attacker-controlled one to reroute transactions.

The Windows maker also noted that the new iteration introduces changes to the fourth stage of the infection chain, particularly where an AppleScript application is used to run a shell command to fetch the final-stage AppleScript that's responsible for collecting system information and launching various sub-modules using a boot() function.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibuPI2_RwhllnqZDUPUX4gGyS3feqfpBxs9oeBfalsXo5bl79ya-FXpcbXM4ReJ4YpZ1Zzg0HcmgilWEyWrCrh-Gi-aTeRWSPKyEwPJQ3H6yaQX7qtEMxhG2QjJso56HOgyeayhnjEjCFTCa_xAjM-d57Gm6Jh05AoHUOucY4MYO7ZztYIWsHGefzLGXeT/s2600/macos-malware.jpg)

Notably, the modifications include extra checks for the Mozilla Firefox browser and an altered logic to determine the presence of the Telegram messaging app. Also observed are changes to the various modules, as well as new modules that did not exist in previous versions -

* vexyeqj, the information module previously called seizecj, and which downloads a module called bnk that's run using osascript. The script defines functions for data validation, encryption, decryption, fetching additional data from command-and-control (C2) server, and logging. It also includes the clipper functionality.
* neq\_cdyd\_ilvcmwx, a module similar to txzx\_vostfdi that exfiltrates files to the C2 server
* xmyyeqjx, a module to set up LaunchDaemon-based persistence
* jey, the module previously called jez, and which is used to set up Git-based persistence
* iewmilh\_cdyd, a module to steal data from Firefox using a modified version of a publicly available tool named [HackBrowserData](https://github.com/moonD4rk/HackBrowserData/tree/main)

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

To mitigate the threat posed by XCSSET, users are recommended to ensure that they keep their system up-to-date, inspect Xcode projects downloaded or cloned from repositories or other sources, and exercise caution when it comes to copying and pasting sensitive data from the clipboard.

Sherrod DeGrippo, Director of Threat Intelligence Strategy at Microsoft, told The Hacker News that the modules regularly undergo small name changes as the malware evolves, despite its functionality remaining consistent.

"What stands out in this variant is its ability to intercept and tamper with clipboard content tied to digital wallets," DeGrippo said. "This isn't passive reconnaissance; it’s a threat that will undermine trust in something as basic as what you copy and paste.

"The latest XCSSET evolution shows how even developer tools can be weaponized. With tactics like clipboard hijacking, expanded browser targeting, and stealth persistence, threat actors continue to raise the level of sophistication defenders need to guard against."

*(The story was updated after publication to include a response from Microsoft.)*

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
[**Share on WhatsApp](#link_share...