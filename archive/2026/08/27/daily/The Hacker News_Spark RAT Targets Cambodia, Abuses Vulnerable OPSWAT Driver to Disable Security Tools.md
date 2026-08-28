---
title: Spark RAT Targets Cambodia, Abuses Vulnerable OPSWAT Driver to Disable Security Tools
url: https://thehackernews.com/2026/08/spark-rat-targets-cambodia-abuses.html
source: The Hacker News
date: 2026-08-27
fetch_date: 2026-08-28T13:37:59.278476
---

# Spark RAT Targets Cambodia, Abuses Vulnerable OPSWAT Driver to Disable Security Tools

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Spark RAT Targets Cambodia, Abuses Vulnerable OPSWAT Driver to Disable Security Tools](https://thehackernews.com/2026/08/spark-rat-targets-cambodia-abuses.html)

**Ravie Lakshmanan**Aug 27, 2026Malware / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvqqkrFYi_Np3w-hHvDbFZqWnf1qCrkS6zwJARAyiKX99YdH2w37pqvD-Zy1HPAYdbJbFu3Tztap9lcuv-lkq8wd9elTkfK0NWN5a9J8218OE9btcQHMdyM93GiuYLuj5mC_TPFBXnVZkUEckgARKceSsJKRqHDeW-U_tsDcPscO3-s2Oid28OEZTz7cIw/s1700-e365/combo-malware.jpg)

Individuals and organizations in Cambodia have emerged as the target of a new campaign that delivers an open-source remote access trojan (RAT) called **Spark RAT**.

"The samples employ diverse lure themes, suggesting an effort to appeal to a broad range of potential victims. These include government notices, public health materials, real estate-related content, and other topics," Acronis Threat Research Unit (TRU) researchers Darrel Virtusio and Subhajeet Singha [said](https://www.acronis.com/en/tru/posts/cambodia-focused-cluster-uses-multi-stage-infection-chain-with-localized-lures/) in an analysis published Wednesday.

The multi-stage attack is notable for employing the bring your own vulnerable driver (BYOVD) technique to load a legitimate-but-vulnerable driver associated with OPSWAT AppRemover ("ardrv.sys") to escalate privileges and neutralize security software.

Attack chains likely make use of targeting phishing emails to distribute compressed archives containing an Inno Setup executable and trick recipients into running it using wide-ranging lures, including Cambodian government notices, public health announcements, dental examination records, real estate documents, and promotional offers.

Acronis said it discovered a number of malicious artifacts between late June through early August 2026, although it's unclear if the campaign remains ongoing.

The Inno Setup installer is designed to trigger a DLL side-loading chain using a signed Tencent executable, which then delivers interim payloads responsible for deploying the vulnerable "ardrv.sys" and then launching the [Spark RAT](https://thehackernews.com/2025/04/pakistan-linked-hackers-expand-targets.html) payload. Spark RAT is an [open-source, Go-based cross-platform RAT](https://github.com/XZB-1248/Spark) that enables remote control of compromised devices.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The DLL loader also carries out a timing-based anti-sandbox check to detect environments that shorten or manipulate sleep delays, and proceeds to terminate execution if the elapsed time falls outside the expected range. Furthermore, it reviews running processes for those related to Huorong Internet Security ("HipsTray.exe"), a Chinese endpoint security program.

If the process is present, the loader attempts to weaken the privileges of the security product. In the next stage, it decrypts shellcode concealed within a PNG file present in the archive to run a second stager, which verifies if it is running with SYSTEM privileges.

"Based on these checks, the payload selects one of two execution modes," Acronis said. "If it is already running as SYSTEM, it proceeds directly to inject mode, bypassing the persistence setup and executing the next stage. Otherwise, it enters setup mode, where it establishes persistence first, then executes the next stage."

The inject mode works by parsing and decrypting shellcode embedded in another PNG file from the archive, and then injecting it into "vssvc.exe" and executing it within the context of the target process. To ensure the injected payload remains running, it monitors the "vssvc.exe" instance and re-injects the shellcode if the process terminates or restarts with a new PID.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcrOx7Sj6PKmU776mowTYVkjLownLbqAW8e9CT_bsAHluExOWeDF9YPDgn84LA85gLnSnuWxU6ABezWJBPRprsH6wdg10HuEIYo7UAPSScGRjxvgzypxi5z9FHg3W1wkYp-jYJRVfQIZfkAWp5SRLXda8-plH-iFzxzJLEKmBVoBHCeV6ecdS1G4u-tkrE/s1700-e365/nui.jpg)

In the setup mode, the malware reads and decrypts the shellcode from the same file, after which it checks for a list of hard-coded processes associated with Qihoo 360. If none of them are found, it sets up a Windows service-based persistence mechanism to launch the binary that sideloads the DLL to relaunch the entire cycle all over again. After establishing persistence on the host, it injects the shellcode into "vssvc.exe" like before.

The payload performs the following sequence of actions -

* Attempt to patch AMSI and ETW related functionality
* Setup persistence using a scheduled task
* Install the ardrv.sys driver that's vulnerable to CVE-2026-36425 to terminate security-related processes such as Microsoft Defender, Huorong Internet Security, and Tencent PC Manager
* Read and decrypt another embedded payload from a third PNG file to perform user-mode termination of hard-coded security processes

Simultaneously, a fourth PNG-based payload file is processed to extract and decrypt shellcode that's injected into "ctfmon.exe," ultimately leading to the execution of Spark RAT.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Interestingly, the BYOVD routine references a number of other drivers, including those part of [TrueSight](https://thehackernews.com/2025/02/2500-truesightsys-driver-variants.html) and [Zemana Anti-Malware SDK](https://thehackernews.com/2025/09/silver-fox-exploits-microsoft-signed.html), both of which have been put to use by the [Silver Fox](https://thehackernews.com/2026/07/silverfox-targets-japanese-manufacturer.html) threat actor prior to dropping Winos 4.0 (aka ValleyRAT). In addition, the [targeting](https://thehackernews.com/2024/11/new-winos-40-malware-infects-gamers.html) of [Huorong security processes](https://thehackernews.com/2025/02/silver-fox-apt-uses-winos-40-malware-in.html) has been [repeatedly obs...