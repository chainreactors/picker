---
title: Gh0st RAT Trojan Targets Chinese Windows Users via Fake Chrome Site
url: https://thehackernews.com/2024/07/gh0st-rat-trojan-targets-chinese.html
source: The Hacker News
date: 2024-07-30
fetch_date: 2025-10-06T17:59:08.966688
---

# Gh0st RAT Trojan Targets Chinese Windows Users via Fake Chrome Site

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

# [Gh0st RAT Trojan Targets Chinese Windows Users via Fake Chrome Site](https://thehackernews.com/2024/07/gh0st-rat-trojan-targets-chinese.html)

**Jul 29, 2024**Ravie LakshmananCybersecurity / Cyber Espionage

[![Gh0st RAT Trojan](data:image/png;base64... "Gh0st RAT Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjM1Wxw1hsNYSIpz3tvigMAvgNAar9L_kre1q_wzh3FpbhfzM7SpqmEOtJGefuzjidGf5LdfSMWpAXnQKGefKhJHprlf_BtnfKaZv3wTRdZb6f1jKIv_-bpJcqW4pCplqnxR3qwmm-erlV8Elw_5hfCKvP8c980mSDcneg6SW9v1MMcH9f-aa0ucsN-2Z9H/s790-rw-e365/chrome.png)

The remote access trojan known as Gh0st RAT has been observed being delivered by an "evasive dropper" called Gh0stGambit as part of a [drive-by download scheme](https://thehackernews.com/2024/07/fakebat-loader-malware-spreads-widely.html) targeting Chinese-speaking Windows users.

These infections stem from a fake website ("chrome-web[.]com") serving malicious installer packages masquerading as Google's Chrome browser, indicating that users searching for the software on the web are being singled out.

Gh0st RAT is a [long-standing malware](https://thehackernews.com/2024/06/new-cross-platform-malware-noodle-rat.html) that has been observed in the wild since 2008, manifesting in the form of different variants over the years in campaigns primarily orchestrated by China-nexus cyberespionage groups.

Some iterations of the trojan have also been [previously deployed](https://thehackernews.com/2023/10/microsoft-warns-of-cyber-attacks.html) by infiltrating poorly-secured MS SQL server instances, using it as a conduit to install the Hidden open-source rootkit.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

According to cybersecurity firm eSentire, which [discovered](https://www.esentire.com/blog/a-dropper-for-deploying-gh0st-rat) the latest activity, the targeting of Chinese-speaking users is based on "the use of Chinese-language web lures and Chinese applications targeted for data theft and defense evasion by the malware."

The MSI installer downloaded from the phony website contains two files, a legitimate Chrome setup executable and a malicious installer ("WindowsProgram.msi"), the latter of which is used to launch shellcode that's responsible for loading Gh0stGambit.

The dropper, in turn, checks for the presence of security software (e.g., 360 Safe Guard and Microsoft Defender Antivirus) before establishing contact with a command-and-control (C2) server in order to retrieve Gh0st RAT.

"Gh0st RAT is written in C++ and has many features, including terminating processes, removing files, capturing audio and screenshots, remote command execution, keylogging, data exfiltration, hiding registry, files, and directories via the rootkit capabilities, and many more," eSentire said.

It's also capable of dropping Mimikatz, enabling RDP on the compromised hosts, accessing account identifiers associated with Tencent QQ, clearing Windows event logs, and erasing data from 360 Secure Browser, QQ Browser, and Sogou Explorer.

The Canadian company said the artifact shares overlaps with a Gh0st RAT variant tracked by the AhnLab Security Intelligence Center (ASEC) under the moniker [HiddenGh0st](https://thehackernews.com/2023/10/microsoft-warns-of-cyber-attacks.html).

"Gh0st RAT has seen widespread use and modification by APT and criminal groups over the past several years," eSentire said. "The recent findings highlight the distribution of this threat via drive-by downloads, deceiving users into downloading a malicious Chrome installer from a deceptive website."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The continued success of drive-by downloads reinforces the need for ongoing security training and awareness programs."

The development comes as Broadcom-owned Symantec said it observed an increase in phishing campaigns likely leveraging Large Language Models (LLMs) to generate malicious PowerShell and HTML code used to download several loaders and stealers.

The emails contained "code used to download various payloads, including [Rhadamanthys](https://thehackernews.com/2023/12/rhadamanthys-malware-swiss-army-knife.html), [NetSupport RAT](https://thehackernews.com/2023/11/netsupport-rat-infections-on-rise.html), [CleanUpLoader](https://thehackernews.com/2024/06/oyster-backdoor-spreading-via.html) (Broomstick, Oyster), [ModiLoader](https://thehackernews.com/2023/03/stealthy-dbatloader-malware-loader.html) (DBatLoader), [LokiBot](https://thehackernews.com/2023/07/cybercriminals-exploit-microsoft-word.html), and [Dunihi](https://thehackernews.com/2022/06/google-blocks-dozens-of-malicious.html) (H-Worm)," security researchers Nguyen Hoang Giang and Yi Helen Zhang [said](https://symantec-enterprise-blogs.security.com/threat-intelligence/malware-ai-llm). "Analysis of the scripts used to deliver malware in these attacks suggests they were generated using LLMs."

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

[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data theft](https://thehackernews.com/search/label/data%20theft)[Ma...