---
title: Researchers Uncover Flaws in Windows Smart App Control and SmartScreen
url: https://thehackernews.com/2024/08/researchers-uncover-flaws-in-windows.html
source: The Hacker News
date: 2024-08-06
fetch_date: 2025-10-06T18:06:15.826754
---

# Researchers Uncover Flaws in Windows Smart App Control and SmartScreen

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

# [Researchers Uncover Flaws in Windows Smart App Control and SmartScreen](https://thehackernews.com/2024/08/researchers-uncover-flaws-in-windows.html)

**Aug 05, 2024**Ravie LakshmananThreat Intelligence / Vulnerability

[![Smart App Control and SmartScreen](data:image/png;base64... "Smart App Control and SmartScreen")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXiN_wHw29eVvLZ_BeHWja7GnNOg3w8h1EoqpDHCIJtz7pDb5LfYw5KOCe6E6bSwDhFY8hTq0JOtbwxJA-Ux1mLGOYeJptc5XgRR2Vp2CL8o-DYoCrg2fX4B1X1Cx2lLfmauI-fL65mQQtMlN6LuUwxzV6Nya2KBeClK3aN_8FwPtpB-Y37oBqgRiN-h7P/s790-rw-e365/main.gif)

Cybersecurity researchers have uncovered design weaknesses in Microsoft's Windows Smart App Control and SmartScreen that could enable threat actors to gain initial access to target environments without raising any warnings.

Smart App Control ([SAC](https://support.microsoft.com/en-us/topic/what-is-smart-app-control-285ea03d-fa88-4d56-882e-6698afdb7003)) is a cloud-powered security feature [introduced](https://thehackernews.com/2024/05/windows-11-to-deprecate-ntlm-add-ai.html) by Microsoft in Windows 11 to block malicious, untrusted, and potentially unwanted apps from being run on the system. In cases where the service is unable to make a prediction about the app, it checks if it's signed or has a valid signature so as to be executed.

SmartScreen, which was released alongside Windows 10, is a similar security feature that determines whether a site or a downloaded app is potentially malicious. It also leverages a reputation-based approach for URL and app protection.

"Microsoft Defender SmartScreen evaluates a website's URLs to determine if they're known to distribute or host unsafe content," Redmond [notes](https://learn.microsoft.com/en-us/windows/security/operating-system-security/virus-and-threat-protection/microsoft-defender-smartscreen/) in its documentation.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"It also provides reputation checks for apps, checking downloaded programs and the digital signature used to sign a file. If a URL, a file, an app, or a certificate has an established reputation, users don't see any warnings. If there's no reputation, the item is marked as a higher risk and presents a warning to the user."

It's also worth mentioning that when SAC is enabled, it replaces and disables Defender SmartScreen.

"Smart App Control and SmartScreen have a number of fundamental design weaknesses that can allow for initial access with no security warnings and minimal user interaction," Elastic Security Labs [said](https://www.elastic.co/security-labs/dismantling-smart-app-control) in a report shared with The Hacker News.

One of the easiest ways to bypass these protections is get the app signed with a legitimate Extended Validation (EV) certificate, a technique already exploited by malicious actors to distribute malware, as recently evidenced in the case of [HotPage](https://thehackernews.com/2024/07/alert-hotpage-adware-disguised-as-ad.html).

[![Smart App Control and SmartScreen](data:image/png;base64... "Smart App Control and SmartScreen")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0GiVpNbi0_Fzv8fv5ugFm824cfmHBnnDVFgkm8g4WDJepJS5vVLhVocZ4ce6oeZImMqiWgXF5w5LV-O60TtaJGQj4PUJJmWNYc6b1Ojatyp500tLKL-ktKiK-P7WAieYcAYs0mdnQ_i3PXsSpuwXAo-V90ID20FsMBEpUgRSZhYPOmonAtWPXW0fdzKTt/s790-rw-e365/demo.gif)

Some of the other methods that can be used for detection evasion are listed below -

* Reputation Hijacking, which involves identifying and repurposing apps with a good reputation to bypass the system (e.g., [JamPlus](https://github.com/jamplus/jamplus) or a known AutoHotkey interpreter)

* Reputation Seeding, which involves using an seemingly-innocuous attacker-controlled binary to trigger the malicious behavior due to a vulnerability in an application, or after a certain time has elapsed.

* Reputation Tampering, which involves altering certain sections of a legitimate binary (e.g., calculator) to inject shellcode without losing its overall reputation

* LNK Stomping, which involves exploiting a bug in the way Windows shortcut (LNK) files are handled to remove the mark-of-the-web ([MotW](https://thehackernews.com/2022/06/researchers-warn-of-unpatched-dogwalk.html)) tag and get around SAC protections owing to the fact that SAC blocks files with the label.

"It involves crafting LNK files that have non-standard target paths or internal structures," the researchers said. "When clicked, these LNK files are modified by explorer.exe with the canonical formatting. This modification leads to removal of the MotW label before security checks are performed."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Elastic Security Labs said it found in-the-wild exploits leveraging LNK stomping as early as February 2018, citing [artifacts](https://www.virustotal.com/gui/file/11dadc71018027c7e005a70c306532e5ea7abdc389964cbc85cf3b79f97f6b44/details) submitted to VirusTotal, suggesting that threat actors have been aware of the bypass for years.

"Reputation-based protection systems are a powerful layer for blocking commodity malware," the company said. "However, like any protection technique, they have weaknesses that can be bypassed with some care. Security teams should scrutinize downloads carefully in their detection stack and not rely solely on OS-native security features for protection in this area."

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
[**Shar...