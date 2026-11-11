---
title: Binance Warns of iOS Sandbox Escape That Could Expose Crypto Wallet Keys, No Fix Confirmed
url: https://thehackernews.com/2026/11/binance-warns-of-ios-sandbox-escape.html
source: The Hacker News
date: 2026-11-10
fetch_date: 2026-11-11T08:35:39.989610
---

# Binance Warns of iOS Sandbox Escape That Could Expose Crypto Wallet Keys, No Fix Confirmed

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

# [Binance Warns of iOS Sandbox Escape That Could Expose Crypto Wallet Keys, No Fix Confirmed](https://thehackernews.com/2026/11/binance-warns-of-ios-sandbox-escape.html)

**Swati Khandelwal**Nov 10, 2026Vulnerability / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikVWFDhEAWo-q-_JsRneE91hAsf7Ho4XXGI51_q0V6XaCrBl7COWgs81b8KLYtdO0XaRMjP5JbJs80iC103U16Mr7GU05znwtx3CvvMnJMR1ywArpKJj4AdVd9HaLv0U65k59BBY706XjRtU8bx9q-fnLlozVb63XJ43QDKm3FbJUmrSwcB9TvwJpyP64/s1700-nu-rw-lo-l85-e365/ios-jail.jpg)

An iOS sandbox escape published on GitHub lets an app read other apps' files on iPhones running iOS 26 and 27. That puts seed phrases, private keys, and login credentials at risk of exposure to malicious apps, Binance warned today. Apple's updates for iOS 26 and 27, released yesterday, do not list a fix.

A researcher who goes by **forcequit**, in collaboration with **0xjohnny**,[released](https://x.com/forcequitOS/status/2119475139528020218) the escape, called **worse\_query**, on Sunday, a day before those updates came out. Neither the exchange nor the researcher reported any attacks or thefts involving it.

The exchange told users to delete apps installed from untrusted sources, such as sideloaded or manually signed apps, and to update iOS and all their apps. No fix for the escape has been confirmed.

For anyone who suspects a breach, the exchange's [security warning](https://x.com/binance/status/2120093246399430770) advises moving funds to a new wallet created on a clean device and resetting all active login sessions.

The researcher's [proof-of-concept code](https://github.com/forcequitOS/worse_query) can reach every app's data container on an iPhone, and some system folders on iOS 27. To use it, an app has to set up an App Group container.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

He says the code is for developers and "isn't useful by itself." Other developers have built apps on it that people can install.

One of them is WQ Files, a [file manager](https://github.com/kolbicz/WQFiles) that developer Christoph Kolbicz built on worse\_query. It reaches other apps' data without a jailbreak or a kernel exploit, and it can edit, delete and clear that data.

WQ Files installs via sideloading tools such as AltStore and SideStore, which automatically create the App Group it needs when used with an Apple ID. No one involved has said whether an app from the App Store could use worse\_query.

The three versions in the exchange's warning are the ones listed as tested in the WQ Files [release notes](https://github.com/kolbicz/WQFiles/releases/tag/v0.7). The researcher gives a wider range.

Of these sources, only Erosion's developers list iOS 27.2.1, which came out yesterday, and none lists iOS 26.7.3. They added 27.2.1 this week in a [README change](https://github.com/jailbreakdotparty/Erosion/commit/585a24a) with the note "pretty sure 27.2.1 is supported".

Yesterday's updates, iOS 27.2.1 and iOS 26.7.3, fixed two [iMessage flaws](https://thehackernews.com/2026/11/apple-patches-imessage-group-chat.html) and several Bluetooth bugs. The [security notes](https://support.apple.com/en-us/149715) for iOS 27.2.1 do not mention worse\_query or any sandbox issues, nor do the [iOS 26.7.3 notes](https://support.apple.com/en-us/149716). Apple does not disclose, discuss, or confirm security issues until it has investigated and a patch or release is available, the notes say.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

In a [reply on X](https://x.com/forcequitOS/status/2119493787932336551), the researcher wrote that he had not planned to release worse\_query early. He added that "Apple was stalling on responding to me and people started larping with it on here."

The exchange did not name any wallet app as exposed, and neither did the researcher nor the developers of the apps built on worse\_query.

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

[Apple](https://thehackernews.com/search/label/Apple), [cryptocurrency](https://thehackernews.com/search/label/cryptocurrency), [data security](https://thehackernews.com/search/label/data%20security), [mobile security](https://thehackernews.com/search/label/mobile%20security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Google Disrupts 1.3 Million-Device Android Botnet, Says TV Box Maker Sold Criminal Access](https://thehackernews.com/2026/11/google-disrupts-13-million-device.html)

[![The Hacker News](data:image/svg+xml;base64...)

Claude Code's “Don't Ask Again” File Exposes Passwords and Keys in 1,122 Public Copies on GitHub](https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html)

[![The Hacker News](data:image/svg+xml;base64...)

Hackers Target OpenSSH SSHole Flaw Within Hours of Disclosure, Gain Root on Honeypot](https://thehackernews.com/2026/11/hackers-exploited-openssh-sshole-flaw.html)

[![The Hacker News](data:image/svg+xml;base64...)

Microsoft Paint RCE Fix Now Available, but Windows Update Won't Deliver It](...