---
title: VolkLocker Ransomware Exposed by Hard-Coded Master Key Allowing Free Decryption
url: https://thehackernews.com/2025/12/volklocker-ransomware-exposed-by-hard.html
source: The Hacker News
date: 2025-12-15
fetch_date: 2025-12-16T03:24:40.694676
---

# VolkLocker Ransomware Exposed by Hard-Coded Master Key Allowing Free Decryption

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [VolkLocker Ransomware Exposed by Hard-Coded Master Key Allowing Free Decryption](https://thehackernews.com/2025/12/volklocker-ransomware-exposed-by-hard.html)

**Dec 15, 2025**Ravie LakshmananRansomware / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZP3WUgrypoDpL5dUk1TlTjzyLA_HKMjawrIv9xe9Aq6_K1u7ikP5Y7ehR-VuYhvQkb5ZHaKrz2WH_uXqmB5YaQm_t4byXd8uFCIMAqYcx15Zog3Wwt4JLdtlvCwm3nPMFI9eBNdni-5Ac7XjIrJ8JjN1D5MFRIer-S1XyPlIpw1s9ybXB_Lgt4UwJ_UJW/s790-rw-e365/ransomware-key.jpg)

The pro-Russian hacktivist group known as **[CyberVolk](https://thehackernews.com/2024/12/thn-recap-top-cybersecurity-threats.html#:~:text=CyberVolk%2C%20a%20Pro%2DRussian%20Hacktivist%20Collective%20Originating%20from%20India)** (aka GLORIAMIST) has resurfaced with a new ransomware-as-a-service (RaaS) offering called VolkLocker that suffers from implementation lapses in test artifacts, allowing users to decrypt files without paying an extortion fee.

According to SentinelOne, VolkLocker (aka CyberVolk 2.x) emerged in August 2025 and is capable of targeting both Windows and Linux systems. It's written in Golang.

"Operators building new VolkLocker payloads must provide a bitcoin address, Telegram bot token ID, Telegram chat ID, encryption deadline, desired file extension, and self-destruct options," security researcher Jim Walter [said](https://www.sentinelone.com/labs/cybervolk-a-deep-dive-into-the-hacktivists-tools-and-ransomware-fueling-pro-russian-cyber-attacks/) in a report published last week.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/windows-stealer-alert-d)

Once launched, the ransomware attempts to escalate privileges, performs reconnaissance and system enumeration, including checking local MAC address prefixes against known virtualization vendors like Oracle and VMware. In the next stage, it lists all available drives and determines the files to be encrypted based on the embedded configuration.

VolkLocker uses AES-256 in Galois/Counter Mode ([GCM](https://en.wikipedia.org/wiki/Galois/Counter_Mode)) for encryption through Golang's "crypto/rand" package. Every encrypted file is assigned a custom extension such as .locked or .cvolk.

However, an analysis of the test samples has uncovered a fatal flaw where the locker's master keys are not only hard-coded in the binaries, but are also used to encrypt all files on a victim system. More importantly, the master key is also written to a plaintext file in the %TEMP% folder ("C:\Users\AppData\Local\Temp\system\_backup.key").

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHr6cN2xeL8afXaNLmvcacJBpXaA7O3h8K-3514Ru7z2zBgYmb5P6Evp9Ia5ynODDr2z7EupDAy8-uCfzFJDrLoXqrQST67gvVH3F99s93C17IhvRWnwkCwV_IAuwOVJKPO_pVKKa80Xrea7JrwU2qIvbjht7U86owunhYUHpT37UuK1k3gE8Hj5cbg-9u/s790-rw-e365/cyber.jpg)

Since this backup key file is never deleted, the design blunder enables self-recovery. That said, VolkLocker has all the hallmarks typically associated with a ransomware strain. It makes Windows Registry modifications to thwart recovery and analysis, deletes volume shadow copies, and terminates processes associated with Microsoft Defender Antivirus and other common analysis tools.

However, where it stands out is in the use of an enforcement timer, which wipes the content of user folders, viz. Documents, Desktop, Downloads, and Pictures, if victims fail to pay within 48 hours or enter the wrong decryption key three times.

CyberVolk's RaaS operations are managed through Telegram, costing prospective customers between $800 and $1,100 for either a Windows or Linux version, or between $1,600 and $2,200 for both operating systems. VolkLocker payloads come with built-in Telegram automation for command-and-control, allowing users to message victims, initiate file decryption, list active victims, and get system information.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

As of November 2025, the threat actors have advertised a remote access trojan and keylogger, both priced at $500 each, indicating a broadening of their monetization strategy.

CyberVolk launched its own RaaS in June 2024. Known for conducting distributed denial-of-service (DDoS) and ransomware attacks on public and government entities to support Russian government interests, it's [believed to be of Indian origin](https://threatmon.io/cybervolk-ransomware-technical-malware-analysis/).

"Despite repeated Telegram account bans and channel removals throughout 2025, CyberVolk has reestablished its operations and expanded its service offerings," Walter said. "Defenders should see CyberVolk's adoption of Telegram-based automation as a reflection of broader trends among politically-motivated threat actors. These groups continue to lower barriers for ransomware deployment while operating on platforms that provide convenient infrastructure for criminal services."

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

[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Data Recovery](https://thehackernews.com/search/label/Data%20Recovery)[encryption](https://...