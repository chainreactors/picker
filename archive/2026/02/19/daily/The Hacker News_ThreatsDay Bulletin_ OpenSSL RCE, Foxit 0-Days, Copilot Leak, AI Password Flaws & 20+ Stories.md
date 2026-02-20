---
title: ThreatsDay Bulletin: OpenSSL RCE, Foxit 0-Days, Copilot Leak, AI Password Flaws & 20+ Stories
url: https://thehackernews.com/2026/02/threatsday-bulletin-openssl-rce-foxit-0.html
source: The Hacker News
date: 2026-02-19
fetch_date: 2026-02-20T04:08:01.783332
---

# ThreatsDay Bulletin: OpenSSL RCE, Foxit 0-Days, Copilot Leak, AI Password Flaws & 20+ Stories

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [ThreatsDay Bulletin: OpenSSL RCE, Foxit 0-Days, Copilot Leak, AI Password Flaws & 20+ Stories](https://thehackernews.com/2026/02/threatsday-bulletin-openssl-rce-foxit-0.html)

**Ravie Lakshmanan**Feb 19, 2026Cybersecurity / Hacking News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDev4RfdUfQ-WwS6a7aV2qVZ6Ftgydw2v8Q-0QDbcmjjnfwjMGcDNG5xV_Za_CJ8nyVFFzuMHVZ5wpspAJV48qF6WLVKQ3UhDZEh7r5rJXkM8IekmUtu1Q_ZroATC7mX6ThW14oaVvTuhyPeRT5v4mJNuZX_ZLSuuAb3aZQYlHRrVKkBzLPb4phQuxN2YS/s1700-e365/threatsday-feb.jpg)

The cyber threat space doesn’t pause, and this week makes that clear. New risks, new tactics, and new security gaps are showing up across platforms, tools, and industries — often all at the same time.

Some developments are headline-level. Others sit in the background but carry long-term impact. Together, they shape how defenders need to think about exposure, response, and preparedness right now.

This edition of ThreatsDay Bulletin brings those signals into one place. Scan through the roundup for quick, clear updates on what’s unfolding across the cybersecurity and hacking landscape.

1. Privacy model hardening

   [Google Showcases New Privacy and Security Features in Android 17](https://android-developers.googleblog.com/2026/02/the-first-beta-of-android-17.html)

   Google [announced](https://developer.android.com/about/versions/17/behavior-changes-17) the first beta version of [Android 17](https://android-developers.googleblog.com/2026/02/the-first-beta-of-android-17.html), with two privacy and security enhancements: the deprecation of Cleartext Traffic Attribute and support for HPKE Hybrid Cryptography to enable secure communication using a combination of public key and symmetric encryption (AEAD). "If your app targets (Android 17) or higher and relies on [usesCleartextTraffic](https://developer.android.com/guide/topics/manifest/application-element#usesCleartextTraffic)='true' without a corresponding Network Security Configuration, it will default to disallowing cleartext traffic," Google said. "You are encouraged to migrate to [Network Security Configuration files](https://developer.android.com/training/articles/security-config) for granular control."
2. RaaS expands cross-platform reach

   [LockBit 5.0 Ransomware Analyzed](https://www.acronis.com/en/tru/posts/lockbit-strikes-with-new-50-version-targeting-windows-linux-and-esxi-systems/)

   A new analysis of the LockBit 5.0 ransomware has revealed that the Windows version packs in various defense evasion and anti-analysis techniques, including packing, DLL unhooking, process hollowing, patching Event Tracing for Windows (ETW) functions, and log clearing. "What's notable among the multiple systems support is its proclaimed capability to 'work on all versions of Proxmox,'" Acronis [said](https://www.acronis.com/en/tru/posts/lockbit-strikes-with-new-50-version-targeting-windows-linux-and-esxi-systems/). "Proxmox is an open-source virtualization platform and is being adopted by enterprises as an alternative to commercial hypervisors, which makes it another prime target of ransomware attacks." The latest version also introduces dedicated builds tailored for enterprise environments, highlighting the continued evolution of ransomware-as-a-service (RaaS) operations.
3. Mac users lured via nested obfuscation

   [ClickFix Continues to Evolve](https://www.intego.com/mac-security-blog/matryoshka-clickfix-macos-stealer/)

   Cybersecurity researchers have detailed a new evolution of the [ClickFix](https://thehackernews.com/2026/02/microsoft-discloses-dns-based-clickfix.html) social engineering tactic targeting macOS users. "Dubbed Matryoshka due to its nested obfuscation layers, this variant uses a fake installation/fix flow to trick victims into executing a malicious Terminal command," Intego [said](https://www.intego.com/mac-security-blog/matryoshka-clickfix-macos-stealer/). "While the ClickFix tactic is not new, this campaign introduces stronger evasion techniques — including an in-memory, compressed wrapper and API-gated network communications — designed to hinder static analysis and automated sandboxes." The campaign primarily targets users attempting to visit software review sites, leveraging typosquatting in the URL name to redirect them to fake sites and activate the infection chain.
4. Loader pipeline drives rapid domain takeover

   [ClickFix Delivers Matanbuchus 3.0 and AstarionRAT](https://www.huntress.com/blog/clickfix-matanbuchus-astarionrat-analysis)

   Another new [ClickFix](https://thehackernews.com/2026/02/microsoft-discloses-dns-based-clickfix.html) campaign detected in February 2026 has been observed delivering a malware-as-a-service (MaaS) loader known as [Matanbuchus 3.0](https://thehackernews.com/2025/07/hackers-leverage-microsoft-teams-to.html). Huntress, which [dissected](https://www.huntress.com/blog/clickfix-matanbuchus-astarionrat-analysis) the attack chain, said the ultimate objective of the intrusion was to deploy ransomware or exfiltrate data based on the fact that the threat actor rapidly progressed from initial access to lateral movement to domain controllers via PsExec, rogue account creation, and Microsoft Defender exclusion staging. The attack also led to the deployment of a custom implant dubbed AstarionRAT that supports 24 commands to facilitate credential theft, SOCKS5 proxy, port scanning, reflective code loading, and shell execution. According to data from the cybersecurity company, [ClickFix fueled 53% of all malware loader activity](https://www.huntress.com/press-release/huntress-cyber-threat-report-exposes-the-playbook-for-organized-cybercrime) in 2025.
5. Typosquat chain targets macOS credentials

   [Fake Homebrew Typosquats Deliver Cuckoo Stealer](https://hunt.io/blog/fake-homebrew-clickfix-cuckoo-stealer-macos)

   In yet another ClickFix campaign, threat actors are relying on the "reliable trick" to host malicious instructions on f...