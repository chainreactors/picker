---
title: MuddyWater Deploys UDPGangster Backdoor in Targeted Turkey-Israel-Azerbaijan Campaign
url: https://thehackernews.com/2025/12/muddywater-deploys-udpgangster-backdoor.html
source: The Hacker News
date: 2025-12-08
fetch_date: 2025-12-09T03:18:22.162795
---

# MuddyWater Deploys UDPGangster Backdoor in Targeted Turkey-Israel-Azerbaijan Campaign

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

# [MuddyWater Deploys UDPGangster Backdoor in Targeted Turkey-Israel-Azerbaijan Campaign](https://thehackernews.com/2025/12/muddywater-deploys-udpgangster-backdoor.html)

**Dec 08, 2025**Ravie LakshmananNetwork Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYXNboyf2GnxrecT0sKYR0MhunHsxtjogBIhtsNVobnT6Y5JxVFfrYcy4cGoABHSNBKDJTe4fEbi3I9uJ7Rl_HNToAsi6MiMLq53MreR2Eo25VrjlEIxyFz7wbmA2ZXkP-xkTlsEmtA5MTFl1sf_zMOoACofqqbq5pqDA4R0ssFb8b6sEmmaHDoGJ7pEvS/s790-rw-e365/cyberattack.jpg)

The Iranian hacking group known as [MuddyWater](https://thehackernews.com/2025/10/iran-linked-muddywater-targets-100.html) has been observed leveraging a new backdoor dubbed **UDPGangster** that uses the User Datagram Protocol (UDP) for command-and-control (C2) purposes.

The cyber espionage activity targeted users in Turkey, Israel, and Azerbaijan, according to a report from Fortinet FortiGuard Labs.

"This malware enables remote control of compromised systems by allowing attackers to execute commands, exfiltrate files, and deploy additional payloads – all communicated through UDP channels designed to evade traditional network defenses," security researcher Cara Lin [said](https://www.fortinet.com/blog/threat-research/udpgangster-campaigns-target-multiple-countries).

The attack chain involves using spear-phishing tactics to distribute booby-trapped Microsoft Word documents that trigger the execution of a malicious payload once macros are enabled. Some of the phishing messages impersonate the Turkish Republic of Northern Cyprus Ministry of Foreign Affairs and purport to invite recipients to an online seminar titled "Presidential Elections and Results."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/filefix-d)

Attached along with the emails are a ZIP file ("seminer.zip") and a Word document ("seminer.doc"). The ZIP file also contains the same Word file, opening which users are asked to enable macros to stealthily execute embedded VBA code.

For its part, the VBA script in the dropper file is equipped to conceal any sign of malicious activity by displaying a Hebrew-language decoy image from Israeli telecommunications provider Bezeq about supposed disconnection periods in the first week of November 2025 across various cities in the country.

"The macro uses the Document\_Open() event to automatically execute, decoding Base64-encoded data from a hidden form field (UserForm1.bodf90.Text) and writing the decoded content to C:\Users\Public\ui.txt," Lin explained. "It then executes this file using the Windows API CreateProcessA, launching the UDPGangster payload."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_KfUT6nWjitHPvWL7GclfPLgjy544_tfjkYTdzbBiGVKX3379JEWIV3SXicsJatdHdzmZAzhKUU9o9m1lEeCtrVbs20QEcjiAycjV14Gnz2RPx_9zNZprli5sMQimqaODDMMvuA-TqZXi8bswwfAX5npWECUxP41HiG4wWBGrw0uOtvFJZNPRhfdCoUgm/s790-rw-e365/vba-executing.png)

UDPGangster establishes persistence through Windows Registry modifications and boasts of various anti-analysis checks to resist efforts made by security researchers to take it apart. This includes -

* Verifying if the process is being debugged
* Analyzing CPU configurations for sandboxes or virtual machines
* Determining if the system has less than 2048 MB of RAM
* Retrieving network adapter information to validate if the MAC address prefix matches a list of known virtual machine vendors
* Validating if the computer is part of the default Windows workgroup rather than a joined domain
* Examining running processes for tools like VBoxService.exe, VBoxTray.exe, vmware.exe, and vmtoolsd.exe
* Running Registry scans to searches for matches to known virtualization vendor identifiers, such as VBox, VMBox, QEMU, VIRTUAL, VIRTUALBOX, VMWARE, and Xen
* Searching for known sandboxing or debugging tools, and
* Ascertaining whether the file is running in an analysis environment

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

It's only after these checks are satisfied does UDPGangster proceed to gather system information and connects to an external server ("157.20.182[.]75") over UDP port 1269 to exfiltrate collected data, run commands using "cmd.exe," transmit files, update C2 server, and drop and execute additional payloads.

"UDPGangster uses macro-based droppers for initial access and incorporates extensive anti-analysis routines to evade detection," Lin said. "Users and organizations should remain cautious of unsolicited documents, particularly those requesting macro activation."

The development comes days after ESET attributed the threat actor to attacks spanning academia, engineering, local government, manufacturing, technology, transportation, and utilities sectors in Israel that delivered another backdoor referred to as [MuddyViper](https://thehackernews.com/2025/12/iran-linked-hackers-hits-israeli_2.html).

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

[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[digital forensics](https://thehackernews.com/search/label/digital%20forensics)[Incident r...