---
title: ThreatsDay Bulletin: Pixel Zero-Click, Redis RCE, China C2s, RAT Ads, Crypto Scams & 15+ Stories
url: https://thehackernews.com/2026/01/threatsday-bulletin-pixel-zero-click.html
source: The Hacker News
date: 2026-01-22
fetch_date: 2026-01-23T03:33:36.151025
---

# ThreatsDay Bulletin: Pixel Zero-Click, Redis RCE, China C2s, RAT Ads, Crypto Scams & 15+ Stories

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

# [ThreatsDay Bulletin: Pixel Zero-Click, Redis RCE, China C2s, RAT Ads, Crypto Scams & 15+ Stories](https://thehackernews.com/2026/01/threatsday-bulletin-pixel-zero-click.html)

**Ravie Lakshmanan**Jan 22, 2026Cybersecurity / Hacking News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxksXhijxqjYwcb5PYwnxnKJNyjVua9KXaVRMA_0sM5ZHkPM3mJ7S8PrniWhDhPQxjS1IL-okMbEHzBHFXApE0fGUY_dOSBYGbXoD6mDeg2YLOyjqZthPP_wYdmLOfIEsMSOAoMyJiBoAcyAPxXHUGgBl6epepPYmX40YCIW42pue9MuAQi3C_yrv5S_c4/s1600-e365/threatsday.jpg)

Most of this week's threats didn't rely on new tricks. They relied on familiar systems behaving exactly as designed, just in the wrong hands. Ordinary files, routine services, and trusted workflows were enough to open doors without forcing them.

What stands out is how little friction attackers now need. Some activity focused on quiet reach and coverage, others on timing and reuse. The emphasis wasn't speed or spectacle, but control gained through scale, patience, and misplaced trust.

The stories below trace where that trust bent, not how it broke. Each item is a small signal of a larger shift, best seen when viewed together.

1. Spear-phishing delivers custom backdoor

   [Operation Nomad Leopard Targets Afghanistan](https://www.seqrite.com/blog/operation-nomad-leopard-targeted-spear-phishing-campaign-against-government-entities-in-afghanistan/)

   Government entities in Afghanistan have been at the receiving end of a spear-phishing campaign dubbed Operation Nomad Leopard that employs bogus administrative documents as decoys to distribute a backdoor named FALSECUB by means of a GitHub-hosted ISO image file. The campaign was first detected in late December 2025. "The ISO file contains three files," Seqrite Lab [said](https://www.seqrite.com/blog/operation-nomad-leopard-targeted-spear-phishing-campaign-against-government-entities-in-afghanistan/). "The LNK file, Doc.pdf.lnk, is responsible for displaying the PDF to the victim and executing the payload. The PDF file, doc.pdf, contains the government-themed lure." The final payload is a C++ executable that's capable of receiving commands from an external server. The activity has not been attributed to any specific country or known hacker group. "The campaign appears to be conducted by a regionally focused threat actor with a low-to-moderate sophistication level," the Indian cybersecurity company added.
2. DoS attacks hit UK services

   [U.K. Warns of Malicious Activity from Russia-Aligned Hacktivists](https://www.ncsc.gov.uk/news/pro-russia-hacktivist-activity-continues-to-target-uk-organisations)

   The U.K. government is warning of continued malicious activity from Russian-aligned hacktivist groups like [NoName057(16)](https://www.ncsc.gov.uk/news/pro-russia-hacktivist-activity-continues-to-target-uk-organisations) targeting critical infrastructure and local government organizations in the country with denial-of-service (DoS) attacks. The end goal of these attacks is to take websites offline and disable access to essential services. "Although DoS attacks are typically low in sophistication, a successful attack can disrupt entire systems, costing organisations significant time, money, and operational resilience by having to analyse, defend against, and recover from them," the U.K. National Cyber Security Centre (NCSC) [said](https://www.ncsc.gov.uk/news/ncsc-issues-warning-over-hacktivist-groups-disrupting-uk-organisations-online-services).
3. Trusted apps load malicious DLLs

   [New Stealer Campaign Uses DLL Side-Loading Trick](https://blog.virustotal.com/2026/01/malicious-infostealer-january-26.html)

   Google-owned VirusTotal has [disclosed](https://blog.virustotal.com/2026/01/malicious-infostealer-january-26.html) details of an information stealer campaign that relies on a trusted executable to trick the operating system into loading a malicious DLL ("CoreMessaging.dll") payload – a technique called [DLL side-loading](https://thehackernews.com/2026/01/hackers-use-linkedin-messages-to-spread.html) – leading to the execution of secondary-stage infostealers designed to exfiltrate sensitive data. Both the executable and the DLL are distributed via ZIP archives that mimic installers for legitimate applications like Malwarebytes (e.g., "malwarebytes-windows-github-io-6.98.5.zip") and other programs.
4. WSL abused without process spawn

   [Windows Subsystem for Linux Beacon Object File Released](https://specterops.io/blog/2026/01/16/one-wsl-bof-to-rule-them-all/)

   SpecterOps researcher Daniel Mayer has [released](https://github.com/MayerDaniel/the-one-wsl-bof) a beacon object file ([BOF](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/beacon-object-files_main.htm)) – a compiled C program designed to run within the memory of a post-exploitation agent like Cobalt Strike Beacon – that [interacts](https://specterops.io/blog/2026/01/16/one-wsl-bof-to-rule-them-all/) with the Windows Subsystem for Linux (WSL) by directly invoking the WSL COM service, avoiding process creation for "wsl.exe" entirely and allowing operators to list all installed WSL distributions and execute arbitrary commands on any WSL distribution that the BOF finds.
5. Ads push covert RAT installers

   [Malicious Ads for File Converters Lead to RATs](https://www.nextron-systems.com/2026/01/14/free-converter-software-convert-any-system-from-clean-to-infected-in-seconds/)

   Cybersecurity researchers have disclosed an active malicious campaign that uses advertisements placed on legitimate websites to lure users into downloading "converter" tools for converting images or documents. These services share a similar website template and go by names like Easy2Convert, ConvertyFile, Infinite Docs, and PowerDoc. Should a user end up attempt to download the program, they are redirected to another domain that actually hosts the C# dropper files. "In the foreground, these tools usually work as promised, so users do not become suspicious," Nextron Systems [said](https://www.nextron-systems.com/2026/01/14/free-converter-software-convert-any-system-from-clean-to-infected-in-seconds/). "In the background, however, they behave almost identically: they install persistent remote access trojans (RATs) that give the threat actor continuous access to the victim system." Specifically, the executable is designe...