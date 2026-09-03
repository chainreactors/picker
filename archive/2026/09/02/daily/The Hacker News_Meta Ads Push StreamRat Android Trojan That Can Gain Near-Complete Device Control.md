---
title: Meta Ads Push StreamRat Android Trojan That Can Gain Near-Complete Device Control
url: https://thehackernews.com/2026/09/meta-ads-push-streamrat-android-trojan.html
source: The Hacker News
date: 2026-09-02
fetch_date: 2026-09-03T07:02:42.217220
---

# Meta Ads Push StreamRat Android Trojan That Can Gain Near-Complete Device Control

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Meta Ads Push StreamRat Android Trojan That Can Gain Near-Complete Device Control](https://thehackernews.com/2026/09/meta-ads-push-streamrat-android-trojan.html)

**The Hacker News**Sep 02, 2026Malvertising / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNhCfat7BT6m53utL9Z1iMKYQv6B3QwsQdxZBzkmr1WsJpDDdFGZgHjaLuHSXMBBJSyfxtyR750K33X3GzZwYkHac_3mpIITheSY4lh8LMK-ufnQ9htwhkmfv2MRKfZKtYdROU7VuO0HMmK7BQ7FlttrQiToqHq9zffChgBIOJT8yLL5vT7JY43_FDK-A/s1700-nu-rw-lo-l85-e365/android-trojan.jpg)

Cybersecurity researchers have disclosed details of a new Android banking trojan called **StreamRat** that was promoted to Spanish-speaking users through a fake television-streaming campaign on Meta and can give operators near-complete control of infected devices.

ThreatFabric said the campaign's advertisement focused on Spain and reached an estimated 570,950 Meta accounts in the European Union that saw it at least once, with totals for infected devices and confirmed victims remaining unreported.

Device takeover requires the victim to grant a succession of controls after sideloading the Android Package (APK). Users should stop the installation when a streaming app requests system controls unrelated to streaming.

"There is little doubt that StreamRat is a new and technically sophisticated threat, developed by individuals with prior experience in the Android malware ecosystem," ThreatFabric said in its [StreamRat analysis](https://www.threatfabric.com/blogs/from-meta-ads-to-full-device-takeover-uncovering-streamrat).

ThreatFabric did not attribute the campaign to a named threat actor. Once Accessibility access is enabled, operators can capture keystrokes, display credential-stealing overlays, inspect the visible interface, and control the device remotely.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The campaign begins when the social-media lure directs an Android user to a specially crafted website. The site checks the visitor's operating system. It displays its download button to Android devices.

The visitor can then download a file named app.apk. The victim launches the APK. The dropper asks to become the device's default Home application, which returns the victim to its interface whenever the Home button is pressed.

Before fetching the final payload, the dropper requests permission to establish a VPN connection. Once approved, the VPN routes device traffic into a nonfunctional interface while excluding the dropper itself.

The dropper's main page downloads the StreamRat payload to the public Downloads directory as update\_{timestamp}.apk. The dropper next asks for permission to install applications from unknown sources.

After approval, it installs the payload through Android's package installation mechanism. StreamRat launches. The payload requests Accessibility access. After the user grants that permission, the malware connects to its command-and-control (C2) server.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8gW3PVosURQnp7IhueCfsOnLr5kV6JItfHtHsVFvyymmrdjN5wCKTbsVlHoxPBHOQuMRO66XOjjBXgVamzHxAQtRkLXX7q1xGIlYYrkOJTtNSo04lrvfEGAqDM8rvI24WI0zayU3INToErOvfFgcJ51Ic2CBYYhnrUKz3egL2xJbXdjkq14j8hFuuBhs/s1700-nu-rw-lo-l85-e365/strea%2C.png)

The VPN interface forwards no routed traffic, causing other applications to lose internet connectivity during installation. The dropper shuts down the VPN after the payload executes, allowing StreamRat to communicate with its C2 server.

ThreatFabric assessed that the interruption may reduce online reputation and code-analysis checks. Google Play Protect retains offline detection for known potentially harmful applications, limiting the technique's effect on the service.

For a visible screen capture, StreamRat invokes Android's MediaProjection application programming interface (API), which displays a consent dialog and is typically identified by a screen-sharing indicator.

The malware can use Accessibility to interact with the consent dialog after the victim has granted that permission. A second mode uses the Accessibility takeScreenshot() method to capture the screen outside the MediaProjection indicator.

ThreatFabric said StreamRat was also promoted through TikTok. The report's TikTok-specific public evidence consisted of landing-page code that can identify TikTok as the referring application. It supplied no TikTok ad record or reach figure.

The same banners were likely displayed on Facebook and Instagram, while the primary Meta placement remained undetermined.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

Applicability is tied to the installation behavior and the requested permissions, as no Android version range was published.

The company shared the following indicators of compromise (IoCs) -

* **SHA-256** - e0714788b4e2518b0d9d4cbf18c7217bb97718e01689d77338f1cc4a230fcb6c
* **Package** - io.base.one887
* **Application** - StrεαmTV Pro
* **SHA-256** - ba83cc3c9535690191018edf73ca5c6001609df9919462796aa2e551f142e4d3
* **Package** - io.meat.hint
* **Application** - Sistema de vídeo
* **C2 IP** - 45.147.28[.]59
* **C2 IP** - 193.32.2[.]245

The Meta campaign began on June 11, 2026. It ended on July 3, 2026. The campaign was identified in late July 2026. The findings were published on September 2, 2026.

The StreamRat payload came from a GitHub account that ThreatFabric linked to an [earlier Mirax campaign](https://thehackernews.com/2026/04/mirax-android-rat-turns-devices-into.html). The dropper closely resembled the one used in that operation.

"The droppers are hosted using GitHub releases, with different backup links and daily package updates," Cleafy said in its [Mirax report](https://www.cleafy.com/cleafy-labs/mirax-a-new-android-rat-turning-infected-devices-into-potential-residential-proxy-nodes).

Found this article interesting? This article is a...