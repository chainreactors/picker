---
title: Google Issues Patches for Critical Android Flaw That Could Allow RCE Without User Interaction
url: https://thehackernews.com/2026/11/google-patches-critical-android-flaw.html
source: The Hacker News
date: 2026-11-04
fetch_date: 2026-11-05T08:45:13.510045
---

# Google Issues Patches for Critical Android Flaw That Could Allow RCE Without User Interaction

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [Google Issues Patches for Critical Android Flaw That Could Allow RCE Without User Interaction](https://thehackernews.com/2026/11/google-patches-critical-android-flaw.html)

**Swati Khandelwal**Nov 04, 2026Vulnerability / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgm9fDI_lHL64S1r-eoB5-99WagZJBIjKDF-bEJ9egJw_EiLUomXSakGnV0vdq9Fqu2j6KVWM4upLmOwweDCKQ32f21W8CTsQHnoGMhFm-ISPNQEg1Jq5WbDujqLHVkGSEsox0Xd3Yc5Dd-v4-6rdzU4akd97y7cBhRYFO2ofmxpf3HYspJ6MkJs2RtfC4/s1700-nu-rw-lo-l85-e365/android-patch.jpg)

A critical Android flaw could allow an attacker to run code on a phone without any user action remotely, Google said in its [November security bulletin](https://source.android.com/docs/security/bulletin/2026/2026-11-01).

The flaw, **CVE-2026-58868**, affects Android 14 through 17. Phones get the fix with security patch level 2026-11-01 or later, which phone makers and carriers send on their own schedules.

As of November 4, Google's bulletin did not report any attacks exploiting its flaws. None of them was in the Known Exploited Vulnerabilities catalog, kept by the U.S. Cybersecurity and Infrastructure Security Agency, as of its November 3 update.

The flaw is a possible out-of-bounds write caused by a heap buffer overflow in the onOutputReceived function of the file FrameDecoder.cpp. Neither the bulletin nor the flaw's [CVE record](https://www.cve.org/CVERecord?id=CVE-2026-58868) says how an attacker would reach that code.

Google's Critical rating assumes that the protections built into Android and Google's services are turned off or bypassed.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Older versions, such as Android 12 and 13, are not listed as affected by the flaw. Google's records do not say whether they contain it.

### How to Check Your Phone

[Google's help page](https://support.google.com/android/answer/7680439) gives these steps:

1. Open the Settings app.
2. Tap About phone, or About tablet, then Android version.
3. Find the dates for the Android security update and the Google Play system update.

The Android security update date is the phone's security patch level. A date of 2026-11-01 or later covers CVE-2026-58868 and the other flaws in the Framework, System, and Android runtime components.

A date of 2026-11-05 or later covers every flaw in the November bulletin, including those in the kernel and in parts from Arm, Imagination Technologies, MediaTek, Unisoc and Qualcomm.

Google sets two dates so phone makers can ship a set of fixes common to all Android devices sooner. It encourages them to include every fix in the bulletin.

Phones running Android 10 or later may also receive some fixes through Google Play system updates. This month's list for those updates includes another Critical flaw, CVE-2026-58876.

CVE-2026-58868 is not on that list, so the date to check for it is the Android security update.

The bulletin gives no workaround for phones that cannot install the update yet.

### A Remote Denial-of-Service Flaw in Android's Text-Message Code

Another Critical flaw, CVE-2026-58882, could allow a remote denial-of-service attack with no user interaction, according to its [CVE record](https://www.cve.org/CVERecord?id=CVE-2026-58882). It is in decodeWapPdu, a function in Android's code for WAP Push messages that arrive via SMS.

On October 29, a researcher who publishes as Mark B posted a [write-up called "SMS of Death"](https://smsofdeath.com/) about a bug in the same function. Neither the bulletin nor the CVE record says whether CVE-2026-58882 is that bug.

One malformed WAP Push message crashes com.android.phone and ends any active call, including emergency calls, according to the write-up. In tests on several phone models, the crash happened every time.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

The attacker needs only the target's phone number, and the message never shows up in the inbox. The phone retries the message each time it starts, so it can crash on startup until the message is removed.

A proof-of-concept app that sends such a message from one phone to another is public. Phones running Android 12 and 13 run the same code but do not receive the fix that newer versions do, the researcher says.

### Other Critical Flaws

Google's November bulletin lists 216 vulnerabilities, 23 of them rated Critical. Two more Critical flaws could allow remote code execution: CVE-2026-58876 and CVE-2026-58936, both in Android's System component.

Six Critical flaws are in the kernel, two of them in Bluetooth code. The most severe kernel flaw could allow a remote attacker to gain elevated privileges without user interaction.

The 2026-11-05 patch level also fixes Critical flaws in MediaTek modem code and in a closed-source Qualcomm component. In its [November bulletin](https://www.mediatek.com/product-security-bulletin/November-2026), MediaTek describes its Critical modem flaws as out-of-bounds writes and says it is not aware of any active exploitation.

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

[Android](https://thehackernews.com/s...