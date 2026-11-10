---
title: Bitter Hackers Deploy New PapRAT Backdoor in Cyberespionage Campaign Targeting South Asia
url: https://thehackernews.com/2026/11/bitter-hackers-deploy-new-paprat.html
source: The Hacker News
date: 2026-11-09
fetch_date: 2026-11-10T09:03:25.512239
---

# Bitter Hackers Deploy New PapRAT Backdoor in Cyberespionage Campaign Targeting South Asia

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [Bitter Hackers Deploy New PapRAT Backdoor in Cyberespionage Campaign Targeting South Asia](https://thehackernews.com/2026/11/bitter-hackers-deploy-new-paprat.html)

**Ravie Lakshmanan**Nov 09, 2026Cyber Espionage / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQwQpjbb2oT57o807l7YmQ31V2RbyxqqO4hENkKlfikKKH-LeqSUiYz5AaPCCFWml-l_RaN1JMiwbJa9lJe7z7Ijzdk66icRP70eETLZ7lLomkSa3JjezoxbRNeDEkTv0K-26dSzHKxAjc7xyLA9RbIiERPLqyRu5QzfyrPeyIA4dfLzMil5wDkYN9n4sG/s1700-nu-rw-lo-l85-e365/command.jpg)

The South Asian cyber espionage group known as **[Bitter](https://thehackernews.com/2025/06/bitter-hacker-group-expands-cyber.html)** (aka APT-C-08, APT-Q-37, Hazy Tiger, Orange Yali, T-APT-17, and TA397) has been observed targeting South Asian organizations with a previously unreported remote access trojan called PapRAT.

"PapRAT has both C++ and Rust implementations," Fortinet FortiGuard Labs researcher Cara Lin [said](https://www.fortinet.com/blog/threat-research/bitter-expands-its-arsenal-with-paprat). "Its capabilities include command execution, file uploads and downloads, file deletion, directory and drive enumeration, and screenshot capture. The Rust variant adds PowerShell execution and other commands."

The campaign is notable for making use of three different infection chains -

* A Windows Shortcut (LNK) file that abuses the native "ftp.exe" utility to run scripts and create scheduled tasks designed to maintain contact with a command-and-control (C2) server.
* A VHDX disk image containing a LNK file that launches a lure Microsoft Excel spreadsheet, while running an MSI installer in the background to deploy PapRAT.
* A URL shortcut (URL) file that fetches a LNK file via WebDAV, which then leads to an MSI installer that deploys PapRAT.

The living-off-the-land (LotL) approach is designed to execute commands from a remote server ("goodnfortunes[.]com"), allowing it to collect directory and task lists, directory information from Desktop, Documents, and Downloads, installed antivirus product data, and mounted drives.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The harvested reconnaissance information is saved as "abc.pdf" and exfiltrated back to the C2 server via a curl command, after which the staged file is deleted from the host.

A second version of the script has been found to retrieve a file called "talk.log" from "techtalkhelp[.]com." The payload contains a Base64-encoded script to obtain additional instructions from the same server and execute them as PowerShell commands.

"This staging model gives the attacker operational flexibility, while the commands are updated server-side without pushing a new binary, avoiding PE drops and process injection that some security appliances could easily detect," Fortinet said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhWMY-HXWglo0k2-giGMVmQpfMkCWZagxy4RIuM34OU91TLTjTxyMOnrk-wvhwGVFqolNYJrsMC2xRbI1FIMD7332uh0E9a7QUGCrLaGSyvZdoo6mDzyyMRTndh2zzYsJbfDU0spon79FEmCglrMiJkpI6iRUPLexoyXbs48DKWjmhbgZe8bYEgT6FMYiIo/s1700-nu-rw-lo-l85-e365/red.png)

The PapRAT malware delivered via the MSI installer in the second attack chain is designed for remote control. It supports eight commands -

* MSG, for remote shell
* FDD, for directory listing
* DEL, for file deletion
* RUN, for arbitrary file execution
* GDR, for drive enumeration
* SS1, for screenshot capture
* UPP, for uploading local files to the C2 server ("rivingtonclarks[.]com")
* DWW, for downloading files from the C2 server

A Rust version of the malware incorporates three more commands -

* MS2, for PowerShell command execution
* SLP, for sleeping and polling resumption
* BYE, for process termination

A notable aspect of the third attack chain is that it combines the salient aspects of the first two sequences by using a script to download an MSI installer via curl. Like before, the MSI installer serves as a conduit for PapRAT, which then proceeds to drop [WmRAT](https://thehackernews.com/2024/12/bitter-apt-targets-turkish-defense.html), a malware previously identified as used by Bitter.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

The findings indicate that the threat actor continues to refine its custom arsenal to establish and maintain access to targeted systems.

"These changes underscore the importance of monitoring malicious behavior across scripting tools, scheduled tasks, and installer activity alongside detecting known malware signatures," Fortinet said. "Organizations should treat unexpected LNK files, URL shortcuts, disk images, and MSI packages with caution, particularly when delivered through unsolicited messages."

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

[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack), [cyber espionage](https://thehackernews.com/search/label/cyber%20espionage), [Malware](https://thehackernews.com/search/label/Malware), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+...