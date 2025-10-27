---
title: Enigma, Vector, and TgToxic: The New Threats to Cryptocurrency Users
url: https://thehackernews.com/2023/02/enigma-vector-and-tgtoxic-new-threats.html
source: The Hacker News
date: 2023-02-12
fetch_date: 2025-10-04T06:26:47.716178
---

# Enigma, Vector, and TgToxic: The New Threats to Cryptocurrency Users

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

# [Enigma, Vector, and TgToxic: The New Threats to Cryptocurrency Users](https://thehackernews.com/2023/02/enigma-vector-and-tgtoxic-new-threats.html)

**Feb 11, 2023**Ravie LakshmananCryptocurrency / Malware

[![Cryptocurrency Users](data:image/png;base64... "Cryptocurrency Users")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjkWk7PNtmq9jxlkiTO3rQch1-vFz3uRGZ9hYFRMkrbE8UMeccqPar0o9uC7kybfRTKBi6LzR3LPMWmy-on-v_nPbXERSTUIRsw9XCa6PMomLGy7HpPashBfmXtBTNmSxWohYsI0nmp1P_4M1kjfOowoDjt_shn4E7-Hlxaj-64ASRixw_yWgOlVAur/s790-rw-e365/HACKING.png)

Suspected Russian threat actors have been targeting Eastern European users in the crypto industry with fake job opportunities as bait to install information-stealing malware on compromised hosts.

The attackers "use several highly obfuscated and under-development custom loaders in order to infect those involved in the cryptocurrency industry with Enigma stealer," Trend Micro researchers Aliakbar Zahravi and Peter Girnus [said](https://www.trendmicro.com/en_us/research/23/b/enigma-stealer-targets-cryptocurrency-industry-with-fake-jobs.html) in a report this week.

Enigma is said to be an altered version of Stealerium, an open source C#-based malware that acts as a stealer, clipper, and keylogger.

The intricate infection journey starts with a rogue RAR archive file that's distributed via phishing or social media platforms. It contains two documents, one of which is a .TXT file that includes a set of sample interview questions related to cryptocurrency.

The second file is a Microsoft Word document that, while serving as a decoy, is tasked with launching the first-stage Enigma loader, which, in turn, downloads and executes an obfuscated secondary-stage payload through Telegram.

"To download the next stage payload, the malware first sends a request to the attacker-controlled Telegram channel [...] to obtain the file path," the researchers said. "This approach allows the attacker to continuously update and eliminates reliance on fixed file names."

The second-stage downloader, which is executed with elevated privileges, is designed to disable Microsoft Defender and install a third-stage by deploying a legitimately signed kernel mode Intel driver that's vulnerable to CVE-2015-2291 in a [technique](https://www.rapid7.com/blog/post/2021/12/13/driver-based-attacks-past-and-present/) [called](https://www.eset.com/int/about/newsroom/press-releases/research/esets-research-into-bring-your-own-vulnerable-driver-details-attacks-on-drivers-in-windows-core/) [Bring Your Own Vulnerable Driver](https://www.aon.com/cyber-solutions/aon_cyber_labs/yours-truly-signed-av-driver-weaponizing-an-antivirus-driver/) ([BYOVD](https://attack.mitre.org/techniques/T1068/)).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It's worth noting that the U.S. Cybersecurity and Infrastructure Security Agency (CISA) has [added](https://thehackernews.com/2023/02/cisa-warns-of-active-attacks-exploiting.html) the vulnerability to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation in the wild.

The third-stage payload ultimately paves the way for downloading Enigma Stealer from an actor-controlled Telegram channel. The malware, like other stealers, comes with features to harvest sensitive information, record keystrokes, and capture screenshots, all of which is exfiltrated back by means of Telegram.

[![Cryptocurrency Users](data:image/png;base64... "Cryptocurrency Users")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdTbYoD6ZNzcbH1cykOh_73kXl1WAS46naHQmGJ3hIncPLGQUCcwmkRAMmjj_kfNXgQ9bxrKJrD8YKaF-kXbcWn5Mgf-S5F1GSHUCm83-8yPsQWknI45ILXHYyyr_VgP9EOK-SjHe3wIii1Hg9C7p2CxVAmLpMwIUkbPpDQKuFr7bDgs12GytTZcpC/s790-rw-e365/map.png)

Bogus job offers are a tried-and-tested tactic employed by [North Korea-backed](https://thehackernews.com/2022/08/north-korea-hackers-spotted-targeting.html) [Lazarus Group](https://thehackernews.com/2022/09/north-koreas-lazarus-hackers-targeting.html) in its attacks targeting the crypto sector. The adoption of this modus operandi by Russian threat actors "demonstrates a persistent and lucrative attack vector."

The findings come as Uptycs [released](https://www.uptycs.com/blog/understanding-stealerium-malware-and-its-evasion-techniques) details of an attack campaign that leverages the Stealerium malware to siphon personal data, including credentials for cryptocurrency wallets such as Armory, Atomic Wallet, Coinomi, Electrum, Exodus, Guarda, Jaxx Liberty, and Zcash, among others.

[![Uptycs](data:image/png;base64... "Uptycs")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjclSeMUSajDolJ5YgMmWRheykSIfrKo5PgE1Mzo0SQkRyHsgTr7kf1QMeZrPuZ-ojVqmkznrTyd5cqiH3H0qIB9YxmPLgblh0T72kGTQLs724psgVRAKYvFZBn3tt5rItWyarZFRYwbEYP-MpILMnG9A_1Lpvd-RQaY7Z7r8QR6Iubb2XaE2gH7A10/s790-rw-e365/malware.png)

Joining Enigma Stealer and Stealerium in targeting cryptocurrency wallets is yet another malware dubbed [Vector Stealer](https://blog.cyble.com/2023/02/01/vector-stealer-a-gateway-for-rdp-hijacking/) that also comes with capabilities to steal .RDP files, enabling the threat actors to carry out RDP hijacking for remote access, Cyble said in a technical write-up.

Attack chains documented by the cybersecurity firms show that the malware families are delivered through Microsoft Office attachments containing malicious macros, suggesting that miscreants are still relying on the method despite [Microsoft's attempts to close the loophole](https://thehackernews.com/2023/02/post-macro-world-sees-rise-in-microsoft.html).

A similar method has also been put to use to deploy a Monero crypto miner against the backdrop of a cryptojacking and phishing campaign aimed at Spanish users, according to [Fortinet FortiGuard Labs](https://www.fortinet.com/blog/threat-research/malicious-code-cryptojacks-device-to-mine-for-monero-crypto).

[![Monero crypto miner](data:image/png;base64... "Monero crypto miner")](https://blogger.googleuser...