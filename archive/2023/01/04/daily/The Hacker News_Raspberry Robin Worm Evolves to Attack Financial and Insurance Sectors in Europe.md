---
title: Raspberry Robin Worm Evolves to Attack Financial and Insurance Sectors in Europe
url: https://thehackernews.com/2023/01/raspberry-robin-worm-evolves-to-attack.html
source: The Hacker News
date: 2023-01-04
fetch_date: 2025-10-04T03:01:46.188487
---

# Raspberry Robin Worm Evolves to Attack Financial and Insurance Sectors in Europe

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

# [Raspberry Robin Worm Evolves to Attack Financial and Insurance Sectors in Europe](https://thehackernews.com/2023/01/raspberry-robin-worm-evolves-to-attack.html)

**Jan 03, 2023**Ravie LakshmananPost-Exploitation / Malware

[![Raspberry Robin Worm](data:image/png;base64... "Raspberry Robin Worm")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjW9zhUW8cTVWuNjWMZHahDUrmASlPD9hAvqcvxSuPrPswDgM76DeMsfUCOyDEBieGFrnwNeRZ1Gqa_au2_flTZ_VeXOcm-54CN902n19OhSM0n7LyFRj-5ir594YvudTeotj51I7kyqsudq0fp7XpBRhhSPkN-O_qX9ldUik0CGZrcXQwGkY0dnu-T/s790-rw-e365/hackers.png)

Financial and insurance sectors in Europe have been targeted by the **Raspberry Robin** worm, as the malware continues to evolve its post-exploitation capabilities while remaining under the radar.

"What is unique about the malware is that it is heavily obfuscated and highly complex to statically disassemble," Security Joes [said](https://www.securityjoes.com/post/raspberry-robin-detected-itw-targeting-insurance-financial-institutes-in-europe) in a new report published Monday.

The intrusions, observed against Spanish and Portuguese-speaking organizations, are notable for collecting more victim machine data than previously documented, with the malware now exhibiting sophisticated techniques to resist analysis.

Raspberry Robin, also called QNAP worm, is [being used](https://thehackernews.com/2022/12/raspberry-robin-worm-strikes-again.html) by several threat actors as a means to gain a foothold into target networks. Spread via infected USB drives and other methods, the framework has been recently put to use in attacks aimed at telecom and government sectors.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Microsoft is tracking the operators of Raspberry Robin under the moniker [DEV-0856](https://thehackernews.com/2022/10/raspberry-robin-operators-selling.html).

Security Joes' forensic investigation into one such attack has revealed the use of a 7-Zip file, which is downloaded from the victim's browser via social engineering and contains an MSI installer file designed to drop multiple modules.

[![Raspberry Robin Worm](data:image/png;base64... "Raspberry Robin Worm")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigpvQ2fu1hJSwe9LRQ7h2MFWTUGLKrSPQaFAOzzthlHl2AidcUPcBsQuKQdTwkpsfg37PGD5jfQ3EidaDhy93f8LHksrp9runWZHUwF7KjJi7CmYAOHYvtmzEnl-anxiG0yJRD_mEylmePgP9IuCjbqFnCJ_70WZWlOssriPVzB2LZ8ScZtyKl2bms/s790-rw-e365/hacking.png)

In another instance, a ZIP file is said to have been downloaded by the victim through a fraudulent ad hosted on a domain that's known to distribute adware.

The archive file, stored in a Discord server, contains encoded JavaScript code that, upon execution, drops a downloader that's protected with numerous layers of obfuscation and encryption to evade detection.

The shellcode downloader is primarily engineered to fetch additional executables, but it has also seen significant upgrades that enables it to profile its victims to deliver appropriate payloads, in some cases even resorting to a form of trickery by [serving fake malware](https://thehackernews.com/2022/12/raspberry-robin-worm-strikes-again.html).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This involves collecting the host's Universally Unique Identifier ([UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier)), processor name, attached display devices, and the number of minutes that have elapsed since system startup, along with the hostname and username information that was gathered by older versions of the malware.

The reconnaissance data is then encrypted using a hard-coded key and transmitted to a command-and-control (C2) server, which responds back with a Windows binary that's eventually executed on the machine.

"Not only did we discover a version of the malware that is several times more complex, but we also found that the C2 beaconing, which used to have a URL with a plaintext username and hostname, now has a robust RC4 encrypted payload," threat researcher Felipe Duarte said.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[Raspberry Robin](https://thehackernews.com/search/label/Raspberry%20Robin)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Ha...