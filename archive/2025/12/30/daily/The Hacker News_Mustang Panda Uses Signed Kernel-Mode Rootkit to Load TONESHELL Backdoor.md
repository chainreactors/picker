---
title: Mustang Panda Uses Signed Kernel-Mode Rootkit to Load TONESHELL Backdoor
url: https://thehackernews.com/2025/12/mustang-panda-uses-signed-kernel-driver.html
source: The Hacker News
date: 2025-12-30
fetch_date: 2025-12-31T03:25:32.569536
---

# Mustang Panda Uses Signed Kernel-Mode Rootkit to Load TONESHELL Backdoor

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

# [Mustang Panda Uses Signed Kernel-Mode Rootkit to Load TONESHELL Backdoor](https://thehackernews.com/2025/12/mustang-panda-uses-signed-kernel-driver.html)

**Dec 30, 2026**Ravie LakshmananMalware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjecDtf2H25Vece2raxEXtqLjCcgahGUR7FG5NIKWeyx6uIvaFtMlBZUrxC3Yz7RKWiVsbXyllunwBYTBEHgct6q99xvKtNR3U9SvdxMOnfbiU4UN8UgO_CLq5yowN3ZwYvw0oI5Hv7K8A14kLHv4EJaLZzowPdhSNBCE86fJF8G30qcTYYmBWCY4mMSEoh/s790-rw-e365/rootkit.jpg)

The Chinese hacking group known as **[Mustang Panda](https://thehackernews.com/2025/08/unc6384-deploys-plugx-via-captive.html)** has leveraged a previously undocumented kernel-mode rootkit driver to deliver a new variant of backdoor dubbed TONESHELL in a cyber attack detected in mid-2025 targeting an unspecified entity in Asia.

The findings come from Kaspersky, which observed the new backdoor variant in cyber espionage campaigns mounted by the hacking group targeting government organizations in Southeast and East Asia, primarily Myanmar and Thailand.

"The driver file is signed with an old, stolen, or leaked digital certificate and registers as a [minifilter driver](https://learn.microsoft.com/en-us/Windows-hardware/drivers/ifs/about-file-system-filter-drivers) on infected machines," the Russian cybersecurity company [said](https://securelist.com/honeymyte-kernel-mode-rootkit/118590/). "Its end-goal is to inject a backdoor trojan into the system processes and provide protection for malicious files, user-mode processes, and registry keys."

The final payload deployed as part of the attack is TONESHELL, an implant with reverse shell and downloader capabilities to fetch next-stage malware onto compromised hosts. The use of TONESHELL has been attributed to Mustang Panda since at least late 2022.

As recently as September 2025, the threat actor was [linked](https://thehackernews.com/2025/09/mustang-panda-deploys-snakedisk-usb.html) to attacks targeting Thai entities with TONESHELL and a USB worm named TONEDISK (aka WispRider) that uses removable devices as a distribution vector for a backdoor referred to as Yokai.

The command-and-control (C2) infrastructure used for TONESHELL is said to have been erected in September 2024, although there are indications that the campaign itself did not commence until February 2025. The exact initial access pathway used in the attack is not clear. It's suspected that the attackers abused previously compromised machines to deploy the malicious driver.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ransomware_dragon_d)

The driver file ("ProjectConfiguration.sys") is signed with a digital certificate from Guangzhou Kingteller Technology Co., Ltd, a Chinese company that's involved in the distribution and provisioning of automated teller machines (ATMs). The certificate was valid from August 2012 to 2015.

Given that there are other unrelated malicious artifacts signed with the same digital certificate, it's assessed that the threat actors likely leveraged a leaked or stolen certificate to realize their goals. The malicious driver comes fitted with two user-mode shellcodes that are embedded into the .data section of the binary. They are executed as separate user-mode threads.

"The rootkit functionality protects both the driver's own module and the user-mode processes into which the backdoor code is injected, preventing access by any process on the system," Kaspersky said.

The driver has the following set of features -

* Resolve required kernel APIs dynamically at runtime by using a hashing algorithm to match the required API addresses
* Monitor file-delete and file-rename operations to prevent itself from being removed or renamed
* Deny attempts to create or open Registry keys that match against a protected list by setting up a RegistryCallback routine and ensuring that it operates at an [altitude](https://thehackernews.com/2023/08/hackers-can-exploit-windows-container.html) of 330024 or higher
* Interfere with the altitude assigned to WdFilter.sys, a Microsoft Defender driver, and change it to zero (it has a [default value of 328010](https://learn.microsoft.com/en-us/windows-hardware/drivers/ifs/allocated-altitudes)), thereby preventing it from being loaded into the I/O stack
* Intercept process-related operations and deny access if the action targets any process that's on a list of protected process IDs when they are running
* Remove rootkit protection for those processes once execution completes

"Microsoft designates the 320000–329999 altitude range for the FSFilter Anti-Virus Load Order Group," Kaspersky explained. "The malware's chosen altitude exceeds this range. Since filters with lower altitudes sit deeper in the I/O stack, the malicious driver intercepts file operations before legitimate low-altitude filters like antivirus components, allowing it to circumvent security checks."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKN4awKzPDmYQ_bNaCV6tFkOPrdvpij6eti2vJkqYzC-7oY6YOehFbzIqmcIcm-L1YzHMSj3ZgKhodP_8g04AgVSex06dcpcWs6LE_p0VnNkdtx22vnkI_IevH8jt7S7gMVmNe0Zndf0wefCBEu2REPK-a3TFPqBbI2DldY7M5g5ReFqxcHyyJYFVVYI3B/s2600/kas.png)

The driver is ultimately designed to drop two user-mode payloads, one of which spawns an "svchost.exe" process and injects a small delay-inducing shellcode. The second payload is the TONESHELL backdoor that's injected into that same "svchost.exe" process.

Once launched, the backdoor establishes contact with a C2 server ("avocadomechanism[.]com" or "potherbreference[.]com") over TCP on port 443, using the communication channel to receive commands that allow it to -

* Create temporary file for incoming data (0x1)
* Download file (0x2 / 0x3)
* Cancel download (0x4)
* Establish remote shell via pipe (0x7)
* Receive operator command (0x8)
* Terminate shell (0x9)
* Upload file (0xA / 0xB)
* Cancel upload (0xC), and
* Close connection (0xD)

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.u...