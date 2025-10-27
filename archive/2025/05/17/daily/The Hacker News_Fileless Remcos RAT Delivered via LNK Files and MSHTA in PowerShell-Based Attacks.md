---
title: Fileless Remcos RAT Delivered via LNK Files and MSHTA in PowerShell-Based Attacks
url: https://thehackernews.com/2025/05/fileless-remcos-rat-delivered-via-lnk.html
source: The Hacker News
date: 2025-05-17
fetch_date: 2025-10-06T22:33:21.518663
---

# Fileless Remcos RAT Delivered via LNK Files and MSHTA in PowerShell-Based Attacks

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

# [Fileless Remcos RAT Delivered via LNK Files and MSHTA in PowerShell-Based Attacks](https://thehackernews.com/2025/05/fileless-remcos-rat-delivered-via-lnk.html)

**May 16, 2025**Ravie LakshmananMalware / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzGHsDLl3RTam2U9Thl2vwK-XIlhOsWQbikgokcEv7oQ5KNW0egmmqcP99OWGemGvztR0a7FTQ6s1SXRS8KE4GL8okOarjSi5RC_agvctpRAddEzNwGcghUhyphenhyphen5GNj1b6x4lMuVi1KQU4i2FNcnVXWEN95iBSRoDwdIgi38AU-1w6aw8dlP5K2W0JNlb7bB/s790-rw-e365/powershell.jpg)

Cybersecurity researchers have shed light on a new malware campaign that makes use of a PowerShell-based shellcode loader to deploy a remote access trojan called Remcos RAT.

"Threat actors delivered malicious LNK files embedded within ZIP archives, often disguised as Office documents," Qualys security researcher Akshay Thorve [said](https://blog.qualys.com/vulnerabilities-threat-research/2025/05/15/fileless-execution-powershell-based-shellcode-loader-executes-remcos-rat) in a technical report. "The attack chain leverages [mshta.exe](https://redcanary.com/threat-detection-report/techniques/mshta/) for proxy execution during the initial stage."

The latest wave of attacks, as detailed by Qualys, employs tax-related lures to entice users into opening a malicious ZIP archive containing a Windows shortcut (LNK) file, which, in turn, makes use of mshta.exe, a legitimate Microsoft tool used to run HTML Applications (HTA).

The binary is used to execute an obfuscated HTA file named "xlab22.hta" hosted on a remote server, which incorporates Visual Basic Script code to download a PowerShell script, a decoy PDF, and another HTA file similar to xlab22.hta called "311.hta." The HTA file is also configured to make Windows Registry modifications to ensure that "311.hta" is automatically launched upon system startup.

Once the PowerShell script is executed, it decodes and reconstructs a shellcode loader that ultimately proceeds to launch the Remcos RAT payload entirely in memory.

Remcos RAT is a well-known malware that offers threat actors full control over compromised systems, making it an ideal tool for cyber espionage and data theft. A 32-bit binary compiled using Visual Studio C++ 8, it features a modular structure and can gather system metadata, log keystrokes, capture screenshots, monitor clipboard data, and retrieve a list of all installed programs and running processes.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In addition, it establishes a TLS connection to a command-and-control (C2) server at "readysteaurants[.]com," maintaining a persistent channel for data exfiltration and control.

This is not the first time fileless versions of Remcos RAT have been spotted in the wild. In November 2024, Fortinet FortiGuard Labs [detailed](https://thehackernews.com/2024/11/cybercriminals-use-excel-exploit-to.html) a phishing campaign that filelessly deployed the malware by making use of order-themed lures.

What makes the attack method attractive to threat actors is that it allows them to operate undetected by many traditional security solutions as the malicious code runs directly in the computer's memory, leaving very few traces on the disk.

"The rise of PowerShell-based attacks like the new Remcos RAT variant demonstrates how threat actors are evolving to evade traditional security measures," J Stephen Kowski, Field CTO at SlashNext, said.

"This fileless malware operates directly in memory, using LNK files and MSHTA.exe to execute obfuscated PowerShell scripts that can bypass conventional defenses. Advanced email security that can detect and block malicious LNK attachments before they reach users is crucial, as is real-time scanning of PowerShell commands for suspicious behaviors."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhBtjBkvx9HQ3Qh67OYiF7PIcunKa3ciy_7oUe-DD5Q-Fm4EKBw8QD1nxZ1hvKytxK60-tyxY93zv-KgUsmebkS3Dzc30s50oNLyyOOmIqh6lGxerLNgTlB0F82LF4AiVDxKx37_6krDJmg5mTfYlBaPz8-v1BTyPWj6S0sQeOuFRS5Y8ZG6CS9BHvQErwZ/s790-rw-e365/flow.jpg)

The disclosure comes as [Palo Alto Networks Unit 42](https://unit42.paloaltonetworks.com/malicious-payloads-as-bitmap-resources-hide-net-malware/) and [Threatray](https://www.threatray.com/blog/a-net-multi-stage-malware-delivery-system) detailed a new .NET loader that's used to detonate a wide range of commodity information stealers and RATS like Agent Tesla, NovaStealer, Remcos RAT, VIPKeylogger, XLoader, and XWorm.

The loader features three stages that work in tandem to deploy the final-stage payload: A .NET executable that embeds the second and third stages in encrypted form, a .NET DLL that decrypts and loads the next stage, and a .NET DLL that manages the deployment of the main malware.

"While earlier versions embedded the second stage as a hardcoded string, more recent versions use a bitmap resource," Threatray said. "The first stage extracts and decrypts this data, then executes it in memory to launch the second stage."

Unit 42 described the use of bitmap resources to conceal malicious payloads a a steganography technique that can bypass traditional security mechanisms and evade detection.

The findings also coincide with the emergence of several phishing and social engineering campaigns that are engineered for credential theft and malware delivery -

* Use of trojanized versions of the KeePass password management software – codenamed [KeeLoader](https://labs.withsecure.com/publications/keepass-trojanised-in-advanced-malware-campaign) – to drop a Cobalt Strike beacon and steal sensitive KeePass database data, including administrative credentials. The malicious installers are hosted on KeePass typosquat domains that are served via Bing ads.
* Use of [ClickFix lures](https://thehackernews.com/2025/03/microsoft-warns-of-clickfix-phishing.html) and [URLs embedded within PDF documents](https://www.forcepoint.com/blog/x-labs/unmasking-lumma-stealer-campaign) and a series...