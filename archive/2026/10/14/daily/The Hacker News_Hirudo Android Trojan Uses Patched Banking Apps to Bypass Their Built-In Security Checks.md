---
title: Hirudo Android Trojan Uses Patched Banking Apps to Bypass Their Built-In Security Checks
url: https://thehackernews.com/2026/10/hirudo-android-trojan-uses-patched.html
source: The Hacker News
date: 2026-10-14
fetch_date: 2026-10-15T06:45:39.576321
---

# Hirudo Android Trojan Uses Patched Banking Apps to Bypass Their Built-In Security Checks

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Hirudo Android Trojan Uses Patched Banking Apps to Bypass Their Built-In Security Checks](https://thehackernews.com/2026/10/hirudo-android-trojan-uses-patched.html)

**Ravie Lakshmanan**Oct 14, 2026Malware / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj010OXrg2ZBrxwqSnpzd8SrIDY_dYOMtdnzIpG7YnCjv1QB58_HylDTkfFmXtZYci90doRcSrPdFfYLowM_S5t2RpD6UkCoWveJrKajQS-7d3sDtyI22FYN0TKy-pQpzWScUB_ROhXRNzZi9dzhgg02kH3WVtdGPNWYBLKv8qZgsa9kREW1SvZ2LTF2AWV/s1700-nu-rw-lo-l85-e365/android-banking.jpg)

Cybersecurity researchers have disclosed details of a new Android banking trojan called **Hirudo** that works by replacing legitimate banking apps with purpose-built patched versions designed to bypass security checks from inside the app itself, marking a new escalation in financial fraud.

Dutch mobile security company ThreatFabric said it identified replacements for eight Indonesian banking apps, while credential targeting in the malware spans Indonesia, China, India, Mexico, Morocco and Thailand.

"The operation combines credential theft, device takeover, screen and camera capture, and SMS theft, in combination with a fairly mature backend," Eward Driehuis, vice president of fraud engineering at ThreatFabric, [said](https://www.threatfabric.com/blogs/hirudo-from-fake-updates-to-patched-banking-apps) in a statement shared with The Hacker News.

Hirudo facilitates on-device credential theft and live remote control. The malware is delivered by shopping, adult video, and entertainment dropper apps that carry the trojan as a separate installation package, which is then served as an in-app update.

Some of the dropper apps are listed below -

* Shopora (com.agbbh.kjdrttt)
* 1V1 X (com.onev.vip)
* KoiShort (com.koishort.app)
* ZoyaTV (com.zoyatv.app)

"The lure is functional, loading real content in a WebView, a storefront, a video catalogue or short dramas, so the experience looks legitimate," ThreatFabric explained. "Behind that content the dropper runs a fixed startup routine: it collects promotion-tracking data, fetches its campaign configuration, and checks whether the payload, the Hirudo RAT, is already installed with its accessibility service and notification access enabled."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

If it's not present, it displays a fake in-app update prompt to trigger the installation of the malware. It's worth emphasizing that Hirudo is installed as a second app and must be granted its own permissions before it can carry out the malicious activities.

As observed in the case of [StreamRat](https://thehackernews.com/2026/09/meta-ads-push-streamrat-android-trojan.html), the malware implements an anti-detection technique based on blocking Internet access by configuring a deliberately non-functional VPN connection prior to the payload installation. This is seen as an attempt to prevent other apps and services, like Google Play Protect, from carrying out cloud-based checks of the payload.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgbdYja-91DB_iOWcCA5eksVFfGuM034qTpOe336soH_rW6opGFqwhyphenhyphenLPMZ2hdWyKWAaa5P3K90jaeCf63_WuDZ3aanIjX7O4CQmxHCLM-lQC1tFGovrZjwGSBcz4dy7zjuILCIbcVzf7EaTb9Yvgr9kFJnjX_qktwWKlomn5DR_c3B88UUT9E7v4P3w7Ab/s1700-nu-rw-lo-l85-e365/1.png)

"However, Play Protect also provides offline detection for known potentially harmful applications, meaning that the mechanism does not completely disable its protection," ThreatFabric noted last month. "We therefore assess that the technique is more likely intended to reduce the effectiveness of online reputation and code-analysis mechanisms rather than bypass Play Protect entirely."

Depending on the nature of the lure app used, the dropper is also designed to serve bogus screens to capture payment PINs, serve fake screens requesting login credentials for banks and wallet apps, display fake lock screen pattern and PIN overlays, and facilitate total remote control of the device.

While all this behavior is par for the course when it comes to Android banking trojans, it's their attempts to replace the target banking app with a tampered copy that stand out. Specifically, the purpose-built replacements embed a hooking engine to blind signature, accessibility, screen-capture, and Play Integrity checks from within the app. The replacement targets eight Indonesian apps.

"For these, the RAT detects the installed banking app through accessibility, checks its signing certificate against a stored reference, [and] then shows a fake 'update' prompt," ThreatFabric explained. "It opens Android's uninstaller for the genuine app without waiting for the user to tap, and downloads the bank-specific replacement in parallel."

While the need for having to remove the app before installing its near-identical malicious copy is a "real constraint," the mechanism offers the ability to bypass the banking app's own security checks by returning responses fed by the attacker beforehand.

This involves returning the genuine app signing certificate, returning an empty list when querying for enabled accessibility services, and stripping the [FLAG\_SECURE flag](https://thehackernews.com/2025/12/android-malware-fvncbot-seedsnatcher.html) so that the app's screens can be viewed and recorded remotely.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpx6oglh2QPl9YWWjVZeANIArF-2mcjt5SoOZy1lVOY4Sa_yJLeRKvmH2O4qUmWRJOOzy6Viqy6hfTGJiosI_HHAtGARLDI96Z4xi8sy2QV_scqNwbZuItdaC86U5Zr3w4_CQpHJSHVRt3Iw5cdF1yMgsxdGb6ndg4vClzCu3ie38j5LxnR_dCGFt2-Hil/s1700-nu-rw-lo-l85-e365/2.png)

"Key-attestation certificates are re-signed with a bundled keybox, and Play Integrity requests are relayed over plain HTTP to an operator-controlled server, which returns a verdict for the app to accept," the mobile security company said.

"Two details are worth underlining for...