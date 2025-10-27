---
title: New Banshee Stealer Targets 100+ Browser Extensions on Apple macOS Systems
url: https://thehackernews.com/2024/08/new-banshee-stealer-targets-100-browser.html
source: The Hacker News
date: 2024-08-17
fetch_date: 2025-10-06T18:08:13.708230
---

# New Banshee Stealer Targets 100+ Browser Extensions on Apple macOS Systems

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

# [New Banshee Stealer Targets 100+ Browser Extensions on Apple macOS Systems](https://thehackernews.com/2024/08/new-banshee-stealer-targets-100-browser.html)

**Aug 16, 2024**Ravie LakshmananMalware / Browser Security

[![Apple macOS Systems](data:image/png;base64... "Apple macOS Systems")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivjqFHfqc4pfiBp0vczEDJWxK8q0M63zcwHcw1_TQRz8tM3LXZ643nnWBY86agywHZ6BMguKtlfs9xYu5TlwX9-GvgPOfIjzST5yxrEaO2Z6IKhI5ih0VdKEq-Q9hxjhEW3a2hpwI9AGoYEAT587WFFczmdIq3hHn80sQJ2EMynzH9CYn_Z4ybrt5cwpSQ/s790-rw-e365/chat.png)

Cybersecurity researchers have uncovered new stealer malware that's designed to specifically target Apple macOS systems.

Dubbed Banshee Stealer, it's offered for sale in the cybercrime underground for a steep price of $3,000 a month and works across both x86\_64 and ARM64 architectures.

"Banshee Stealer targets a wide range of browsers, cryptocurrency wallets, and around 100 browser extensions, making it a highly versatile and dangerous threat," Elastic Security Labs [said](https://www.elastic.co/security-labs/beyond-the-wail) in a Thursday report.

The web browsers and crypto wallets targeted by the malware comprise Safari, Google Chrome, Mozilla Firefox, Brave, Microsoft Edge, Vivaldi, Yandex, Opera, OperaGX, Exodus, Electrum, Coinomi, Guarda, Wasabi Wallet, Atomic, and Ledger.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It's also equipped to harvest system information and data from iCloud Keychain passwords and Notes, as well as incorporate a slew of anti-analysis and anti-debugging measures to determine if it's running in a virtual environment in an attempt to evade detection.

Furthermore, it makes use of the [CFLocaleCopyPreferredLanguages](https://developer.apple.com/documentation/corefoundation/1542887-cflocalecopypreferredlanguages) API to avoid infecting systems where Russian is the primary language.

Like other macOS malware strains such as [Cuckoo](https://www.kandji.io/blog/update-cuckoo-malware-evolves) and [MacStealer](https://thehackernews.com/2024/05/new-cuckoo-persistent-macos-spyware.html), Banshee Stealer also leverages osascript to display a fake password prompt to trick users into entering their system passwords for privilege escalation.

Among the other notable features include the ability to collect data from various files matching .txt, .docx, .rtf, .doc, .wallet, .keys, and .key extensions from the Desktop and Documents folders. The gathered data is then exfiltrated in a ZIP archive format to a remote server ("45.142.122[.]92/send/").

"As macOS increasingly becomes a prime target for cybercriminals, Banshee Stealer underscores the rising observance of macOS-specific malware," Elastic said.

The disclosure comes as Hunt.io and Kandji [detailed](https://www.kandji.io/blog/infostealer-swiftui-opendirectory-api-capture-verify-passwords) another macOS stealer strain that leverages SwiftUI and Apple's Open Directory APIs for capturing and verifying passwords entered by the user in a bogus prompt displayed in order to complete the installation process.

"It begins by running a Swift-based dropper that displays a fake password prompt to deceive users," Broadcom-owned Symantec [said](https://www.broadcom.com/support/security-center/protection-bulletin/new-macos-malware-uses-swiftui-and-opendirectory-api-for-credential-theft). "After capturing credentials, the malware verifies them using the OpenDirectory API and subsequently downloads and executes [malicious scripts](https://hunt.io/blog/macos-malware-impersonates-the-unarchiver-app-to-steal-user-data) from a command-and-control server."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhwEDJkAknZ5L8kmZsXnY0Hev9aCEfpwLc2_6rZ8a-u6s2NtKF7SpwZglfluW8aGWRrIVNBlXgve78PmpNlBt7AsqYSRxZVtCFIdpSf7lfacQI-9pKVEN-JHTgKVcjGiVoxuQUh6v8_cMQll5sqXC3nL0I4LATZFS8YOKtXmGRxqJa9KqUgpaVcJasa7UD0/s790-rw-e365/data.png)

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This development also follows the [continued emergence](https://blog.barracuda.com/2024/08/14/phishing-advanced-infostealer-data-exfiltration) of new Windows-based stealers such as [Flame Stealer](https://www.broadcom.com/support/security-center/protection-bulletin/flame-stealer-malware), even as [fake sites](https://www.broadcom.com/support/security-center/protection-bulletin/sora-ai-themed-branding-used-to-distribute-malware) masquerading as OpenAI's text-to-video artificial intelligence (AI) tool, [Sora](https://openai.com/index/sora/), are being used to propagate [Braodo Stealer](https://thehackernews.com/2024/07/microsoft-defender-flaw-exploited-to.html).

Separately, Israeli users are being [targeted](https://www.broadcom.com/support/security-center/protection-bulletin/rhadamanthys-stealer-targeting-users-in-israel) with phishing emails containing RAR archive attachments that impersonate Calcalist and Mako to deliver [Rhadamanthys Stealer](https://thehackernews.com/2023/12/rhadamanthys-malware-swiss-army-knife.html).

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

[browser security](https://thehackernews.com/search/label/...