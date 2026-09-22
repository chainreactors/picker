---
title: TASK#STOMP PowerShell Backdoor Steals Documents, Wi-Fi Passwords, and Clipboard Data
url: https://thehackernews.com/2026/09/taskstomp-powershell-backdoor-steals.html
source: The Hacker News
date: 2026-09-21
fetch_date: 2026-09-22T07:05:19.849393
---

# TASK#STOMP PowerShell Backdoor Steals Documents, Wi-Fi Passwords, and Clipboard Data

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [TASK#STOMP PowerShell Backdoor Steals Documents, Wi-Fi Passwords, and Clipboard Data](https://thehackernews.com/2026/09/taskstomp-powershell-backdoor-steals.html)

**Ravie Lakshmanan**Sep 21, 2026Endpoint Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhC3vJ8DX6852JxHepz1kGmunH3ZXsStcK4LINkLBCrzS8ZacBhqL-7epmGuzSNGI-jpF4GtkM-FXUsrv3croTLimjG_SBbw-rpO8NBIHf6Wvr6BMmYYSDKxEPQI-nrSFYrc9vmojcKn50LRFbc1t3h8qFA8dE_pZ3kMvelRpBFVFe2ZmCVJhPCWlMxYZpO/s1700-nu-rw-lo-l85-e365/stomp.jpg)

Cybersecurity researchers have disclosed details of a new campaign dubbed **TASK#STOMP** that delivers a PowerShell backdoor designed to harvest sensitive data from compromised hosts.

The backdoor "automatically harvests and exfiltrates business documents, watches the filesystem for new files in real time, steals Wi-Fi passwords and clipboard contents, takes screenshots, and accepts arbitrary remote commands through two redundant, token-authenticated C2 servers," Securonix researchers Akshay Gaikwad and Aaron Beardslee [said](https://www.securonix.com/blog/task-stomp-powershell-backdoor-document-theft-remote-access) in a report shared with The Hacker News.

The starting point of the infection chain is the use of "wscript.exe" to execute an encoded Visual Basic Script (VBScript) file staged on the victim's desktop ("95c9050t66.vbs"). The exact initial access pathway used to deliver the payload is unclear, although it's possible that it may have been via email-based phishing or social engineering.

By giving it a completely random file name, it's suspected that the intention may have been to evade file name-based detection mechanisms. The VBScript functions as the orchestrator for establishing persistence on the host using scheduled tasks and launching subsequent stages.

The tasks are given the names Local Credential Manager, Network Audio Service, Windows Display Manager, and Device Credential Handler so as to blend in with regular operating system activity and avoid raising any red flags.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The VBScript installer also sets up a backup persistence method that uses the Windows Startup folder to launch another script payload ("msdiag.vbs") every time the user logs in to the system. In the next phase, the malware executes PowerShell commands to forcibly terminate previously running instances and ensure there exists only one active session

These strategies, paired with deliberate timestamp modification (aka timestomping), hidden execution, and cleanup behavior, suggest a deliberate effort to get around superficial administrative reviews and complicate forensic analysis. The use of redundant persistence methods guarantees continued execution even if one of them fails or is detected and removed.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgM9hgW4fwVdFVj1eL4YUdUjv4Q0kboJTir3FjxPCBV2ftB5uzIiWCF9ne_OX-xG4HlGVLCXVOq-jVaCQobiEEM1VJ64UjJEV4kc4Y6AJEd4vVIma7aA0PaD3nhqOWfJ5BHUJNeSgLarLspcLEXnI7LfRadG6HTL59FZaUzxknewwq8KdsfLmJdmqwh8R1W/s1700-nu-rw-lo-l85-e365/flow.png)

The next phase involves running a pair of hidden PowerShell commands -

* sys\_loader.ps1, which decodes "diag\_pack.dat" and initiates the document-stealing, surveillance, and remote-access payload to steal system metadata, business documents, Wi-Fi passwords, and clipboard content, monitor for newly modified files, take screenshots, and execute arbitrary PowerShell commands win\_conn.ps1, which decodes "win\_conn\_cfg.dat" and sets up a secondary, persistent C2 channel with command execution and collection capabilities

"Running the modules as separate processes provides functional separation and operational redundancy: failure or termination of one branch does not immediately remove the other," Securonix said.

Both the modules communicate with the same C2 infrastructure ("corecloudfileshare[.]xyz" or "attachmentsharingdrive[.]xyz"). Interestingly, the two components incorporate a mutual-watchdog relationship in which "diag\_pack.dat" checks if "win\_conn.ps1" is running, and restart it if not, and vice versa.

The end goal of the attack is to provide a pathway for continuous document collection, credential and clipboard theft, screenshot capture, redundant C2 communications, and arbitrary code execution, while leveraging an array of techniques to fly under the radar.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

In the final stage, the VBScript orchestrator opens Google Chrome in a maximized window and opens a specific URL from "irantenders[.]com," which hosts a searchable database of all tenders and contracts issued by government departments and local authorities in Iran. The purpose behind this user-facing web action is unknown.

Also launched is a batch script ("purge.bat") that invokes a two-second delay and likely performs a clean-up to erase traces of the malicious activity. That said, what this batch script does is unknown as its contents have not been recovered.

"Threat actors routinely abuse Windows Script Host, PowerShell, Task Scheduler, and the .NET toolchain to blend malicious execution with legitimate administrative activity," the researchers said.

"TASK#STOMP demonstrates this approach through a VBS-controlled framework that installs multiple persistence anchors and delegates follow-on functionality to PowerShell and dynamically compiled C# code. By relying almost entirely on native Windows components, the operation reduces its dependence on conventional executable payloads and makes individual events more difficult to distinguish from benign system activity."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://...