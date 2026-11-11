---
title: Apple Patches iMessage Group Chat Privacy Flaws and Bluetooth Pairing Vulnerabilities
url: https://thehackernews.com/2026/11/apple-patches-imessage-group-chat.html
source: The Hacker News
date: 2026-11-10
fetch_date: 2026-11-11T08:35:40.217316
---

# Apple Patches iMessage Group Chat Privacy Flaws and Bluetooth Pairing Vulnerabilities

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [Apple Patches iMessage Group Chat Privacy Flaws and Bluetooth Pairing Vulnerabilities](https://thehackernews.com/2026/11/apple-patches-imessage-group-chat.html)

**Swati Khandelwal**Nov 10, 2026Vulnerability / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUM6RGvSNUqube0TIXYpzHhs7uSvT0k28f2Q8s-GVOexnCI4T5mzFMUs3Lz4_aS6gNuS71DSTvtfOO-tfVFXvVu82pBmj5gO5_jO5g1ndVQQX8xjBY8A_IDAVNkO7oE1s5FRyEsxXQ_HEM_5_KI4g9VWN8BLgCmQTS1DaFt6lRlfgEJMsxyC5bxQW1qhM/s1700-nu-rw-lo-l85-e365/apple-patch.jpg)

An iMessage flaw could let a remote attacker join a group chat and receive its messages, Apple said yesterday, and it released updates to fix it. The updates also fix a separate iMessage flaw that could let someone added to a group access messages sent before they joined.

As of today, other updates released yesterday for the iPhone XS, XS Max and XR, the iPad (7th generation) and some Apple Watch models do not list either fix.

The company's notes also do not say whether either flaw has been exploited, what an attacker would need, whether group members would see someone who joined this way, or whether every member must update to be protected.

The updates that fix the iMessage flaws also fix a flaw in Google's Brotli compression library. The notes do not mention any attacks using that flaw. The U.S. Cybersecurity and Infrastructure Security Agency (CISA) added it to its Known Exploited Vulnerabilities catalog on October 27.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The flaw that could let a remote attacker join a group chat is tracked as CVE-2026-113961. It is an authorization issue that the updates fix through improved validation. The flaw involving earlier messages is CVE-2026-113960.

### Which Updates Carry the Fixes

Each operating system version got its own update. The [security advisory](https://support.apple.com/en-us/149715) for iOS and iPadOS 27.2.1 describes all three flaws. The [security releases list](https://support.apple.com/en-us/100100) links to the notes for every update.

The [iOS 18.7.12 notes](https://support.apple.com/en-us/149717) and the [watchOS 26.6.1 notes](https://support.apple.com/en-us/149723) list other security fixes but not the iMessage or Brotli fixes.

The company does not say whether devices on those versions are affected by the three flaws. Its notes also offer no workaround for anyone who cannot update right away.

The Brotli flaw, CVE-2026-111497, is an out-of-bounds write in the library's decoder that could let malicious input corrupt memory. CISA's [catalog entry](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-111497) for the [Brotli decoder flaw](https://thehackernews.com/2026/10/brotli-decoder-flaw-behind-nodejs-rce.html) names Google's Brotli as the affected product and says different products could use the component.

All nine updates fix Bluetooth and AirPlay flaws. Two could allow a malicious Bluetooth device, or an attacker within Bluetooth range, to pair with a device without user interaction. The notes do not say what a paired device could then do.

Two others could let an attacker bypass the limit on pairing code attempts, one from Bluetooth range and one from the same network. Another could let an attacker in Bluetooth range corrupt process memory.

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

[Apple](https://thehackernews.com/search/label/Apple), [mobile security](https://thehackernews.com/search/label/mobile%20security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Google Disrupts 1.3 Million-Device Android Botnet, Says TV Box Maker Sold Criminal Access](https://thehackernews.com/2026/11/google-disrupts-13-million-device.html)

[![The Hacker News](data:image/svg+xml;base64...)

Claude Code's “Don't Ask Again” File Exposes Passwords and Keys in 1,122 Public Copies on GitHub](https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html)

[![The Hacker News](data:image/svg+xml;base64...)

Hackers Target OpenSSH SSHole Flaw Within Hours of Disclosure, Gain Root on Honeypot](https://thehackernews.com/2026/11/hackers-exploited-openssh-sshole-flaw.html)

[![The Hacker News](data:image/svg+xml;base64...)

Microsoft Paint RCE Fix Now Available, but Windows Update Won't Deliver It](https://thehackernews.com/2026/11/microsoft-paint-rce-fix-now-available.html)

[![The Hacker News](data:image/svg+xml;base64...)

Hackers Hide Linux Backdoor in Control Web Panel Server to Execute Commands Without Logs](https://thehackernews.com/2026/11/hackers-hide-linux-backdoor-in-control.html)

[![The Hacker News](data:image/svg+xml;base64...)

OpenSSH Issues Emergency Fix for Flaw Letting Long Passwords Bypass SSH Auth on Alpine Linux](https://thehackernews.com/2026/11/openssh-issues-emergency-fix-for-flaw.html)

[![The Hacker News](data:image/svg+xml;base64...)

OpenAI AI Pipeline Generates 948 Linux Root Escalation Exploits in 30-Hour Run](https://thehackernews.com/20...