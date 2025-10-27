---
title: CHILLYHELL macOS Backdoor and ZynorRAT RAT Threaten macOS, Windows, and Linux Systems
url: https://thehackernews.com/2025/09/chillyhell-macos-backdoor-and-zynorrat.html
source: The Hacker News
date: 2025-09-11
fetch_date: 2025-10-02T20:00:48.811821
---

# CHILLYHELL macOS Backdoor and ZynorRAT RAT Threaten macOS, Windows, and Linux Systems

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

# [CHILLYHELL macOS Backdoor and ZynorRAT RAT Threaten macOS, Windows, and Linux Systems](https://thehackernews.com/2025/09/chillyhell-macos-backdoor-and-zynorrat.html)

**Sep 10, 2025**Ravie LakshmananThreat Intelligence / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMM3XRawiIkYgH3z6CTwTS7PLhKcxGN-Zw35fC5FXnQSEAu34H6CEE6Zy6D6Rqqw9A9qo13GjeKJnsMCL8jQwCCOlosXX4R0_7R3lfsY6QB1_tyto8qnLYG7aIE5cOXDmxv4nWoQr14vKrevE_U07mzKT38kclMs1JVmAgenWz-ToY1My_MOqZHo0_Pkj2/s790-rw-e365/windows-mac-linux.jpg)

Cybersecurity researchers have discovered two new malware families, including a modular Apple macOS backdoor called **CHILLYHELL** and a Go-based remote access trojan (RAT) named **ZynorRAT** that can target both Windows and Linux systems.

According to an [analysis](https://www.jamf.com/blog/chillyhell-a-modular-macos-backdoor/) from Jamf Threat Labs, ChillyHell is written in C++ and is developed for Intel architectures.

CHILLYHELL is the name assigned to a malware that's attributed to an [uncategorized threat cluster](https://cloud.google.com/blog/topics/threat-intelligence/how-mandiant-tracks-uncategorized-threat-actors) dubbed UNC4487. The hacking group is assessed to have been active since at least October 2022.

According to threat intelligence [shared](https://medium.com/%40thatsiemguy/mandiant-fusion-available-in-google-secops-e-c11bbbbf2cf1) by Google Mandiant, UNC4487 is a suspected espionage actor that has been observed compromising the websites of Ukrainian government entities to redirect and socially engineer targets to execute [Matanbuchus](https://thehackernews.com/2025/07/hackers-leverage-microsoft-teams-to.html) or CHILLYHELL malware.

The Apple device management company said it discovered a new CHILLYHELL sample uploaded to the VirusTotal malware scanning platform on May 2, 2025. The artifact, notarized by Apple back in 2021, is said to have been publicly hosted on Dropbox since then. Apple has since revoked the developer certificates linked to the malware.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Once executed, the malware extensively profiles the compromised host and establishes persistence using three different methods, following which it initializes command-and-control (C2) communication with a hard-coded server (93.88.75[.]252 or 148.72.172[.]53) over HTTP or DNS, and enters into a command loop to receive further instructions from its operators.

To set up persistence, CHILLYHELL either installs itself as a [LaunchAgent](https://thehackernews.com/2024/01/experts-warn-of-macos-backdoor-hidden.html) or a system LaunchDaemon. As a backup mechanism, it alters the user's shell profile (.zshrc, .bash\_profile, or .profile) to inject a launch command into the configuration file.

A noteworthy tactic adopted by the malware is its use of timestomping to modify the timestamps of created artifacts to avoid raising red flags.

"If it does not have sufficient permission to update the timestamps by means of a direct system call, it will fall back to using shell commands touch -c -a -t and touch -c -m -t respectively, each with a formatted string representing a date from the past as an argument included at the end of the command," Jamf researchers Ferdous Saljooki and Maggie Zirnhelt said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhg1HkPXcZXakBUt_nVBHq9hiNuA-kYtvqyRq3o2ayq9uEzvGlLYIkVUFEnPNIKIk9y3YZO_GcPAAxD50l_3rofEdVJRRkvPartFqlLcHbxvaGbRelIIKryemec9xcpASkQ2ivnBXCOa4Xyg5ptbuN6nRG1VmxdWVx27txMTBmFMGkYMwjzFak-a-ilrwUG/s790-rw-e365/applet.jpg)

CHILLYHELL supports a wide range of commands that allow it to launch a reverse shell to the C2 IP address, download a new version of the malware, fetch additional payloads, run a module named ModuleSUBF to enumerate user accounts from "/etc/passwd" and conduct brute-force attacks using a pre-defined password list retrieved from the C2 server.

"Between its multiple persistence mechanisms, ability to communicate over different protocols and modular structure, ChillyHell is extraordinarily flexible," Jamf said. "Capabilities such as timestomping and password cracking make this sample an unusual find in the current macOS threat landscape."

"Notably, ChillyHell was notarized and serves as an important reminder that not all malicious code comes unsigned."

The findings dovetail with the discovery of ZynorRAT, a RAT that uses a Telegram bot called @lraterrorsbot (aka lrat) to commandeer infected Windows and Linux hosts. Evidence shows that the malware was first submitted to VirusTotal on July 8, 2025. It does not share any overlaps with other known malware families.

Compiled with Go, the Linux version supports a wide range of functions to enable file exfiltration, system enumeration, screenshot capture, persistence through systemd services, and arbitrary command execution -

* /fs\_list, to enumerate directories
* /fs\_get, to exfiltrate files from the host
* /metrics, to perform system profiling
* /proc\_list, to run the "ps" Linux command
* /proc\_kill, to kill a specific process by passing the PID as input
* /capture\_display, to take screenshots
* /persist, to establish persistence

ZynorRAT's Windows version is near-identical to its Linux counterpart, while still resorting to Linux-based persistence mechanisms. This likely indicates that development of the Windows variant is a work in progress.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Its main purpose is to serve as a collection, exfiltration, and remote access tool, which is centrally managed through a Telegram bot," Sysdig researcher Alessandra Rizzo [said](https://www.sysdig.com/blog/zynorrat-technical-analysis-reverse-engineering-a-novel-turkish-go-based-rat). "Telegram serves as the main C2 infrastructure through which the malware receives further commands once deployed on a victim machine."

Further analysis of screenshots l...