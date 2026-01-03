---
title: Transparent Tribe Launches New RAT Attacks Against Indian Government and Academia
url: https://thehackernews.com/2026/01/transparent-tribe-launches-new-rat.html
source: The Hacker News
date: 2026-01-02
fetch_date: 2026-01-03T03:23:08.728889
---

# Transparent Tribe Launches New RAT Attacks Against Indian Government and Academia

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [Transparent Tribe Launches New RAT Attacks Against Indian Government and Academia](https://thehackernews.com/2026/01/transparent-tribe-launches-new-rat.html)

**Jan 02, 2026**Ravie LakshmananCyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjaFyRmyuVgO_C0sj1T6dS6xOHtQzLfUUckXuj31BDmfIdvD6xMza5hxryu06NflKvAWIOrqiIl5qZRQRuiTXiRoGkzSSCmfffHmkoW6w1yu7wWkXbk3YnnPQojFwLfDhnCvmjU063dxagQoIPFtiyxLoBP-V36reDJ7__kmAZQ5UD4Ybva-cvjDryruo2W/s790-rw-e365/india.jpg)

The threat actor known as Transparent Tribe has been attributed to a fresh set of attacks targeting Indian governmental, academic, and strategic entities with a remote access trojan (RAT) that grants them persistent control over compromised hosts.

"The campaign employs deceptive delivery techniques, including a weaponized Windows shortcut (LNK) file masquerading as a legitimate PDF document and embedded with full PDF content to evade user suspicion," CYFIRMA [said](https://www.cyfirma.com/research/apt36-multi-stage-lnk-malware-campaign-targeting-indian-government-entities/) in a technical report.

Transparent Tribe, also called APT36, is a hacking group that's known for mounting cyber espionage campaigns against Indian organizations. Assessed to be of Indian origin, the state-sponsored adversary has been active since at least 2013.

The threat actor boasts of an ever-evolving arsenal of RATs to realize its goals. Some of the trojans put to use by Transparent Tribe in recent years include [CapraRAT](https://thehackernews.com/2023/09/transparent-tribe-uses-fake-youtube.html), [Crimson RAT](https://thehackernews.com/2023/04/pakistan-based-transparent-tribe.html), [ElizaRAT](https://thehackernews.com/2024/11/icepeony-and-transparent-tribe-target.html), and [DeskRAT](https://thehackernews.com/2025/10/apt36-targets-indian-government-with.html).

The latest set of attacks began with a spear-phishing email containing a ZIP archive with a LNK file disguised as a PDF. Opening the file triggers the execution of a remote HTML Application (HTA) script using "mshta.exe" that decrypts and loads the final RAT payload directly in memory. In tandem, the HTA downloads and opens a decoy PDF document so as not to arouse users' suspicion.

"After decoding logic is established, the HTA leverages ActiveX objects, particularly WScript.Shell, to interact with the Windows environment," CYFIRMA noted. "This behavior demonstrates environment profiling and runtime manipulation, ensuring compatibility with the target system and increasing execution reliability techniques commonly observed in malware abusing 'mshta.exe.'"

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

A noteworthy aspect of the malware is its ability to adapt its persistence method based on the antivirus solutions installed on the infected machine -

* If Kapsersky is detected, it creates a working directory under "C:\Users\Public\core\," writes an obfuscated HTA payload to disk, and establishes persistence by dropping a LNK file in the Windows Startup folder that, in turn, launches the HTA script using "mshta.exe"
* If Quick Heal is detected, it establishes persistence by creating a batch file and a malicious LNK file in the Windows Startup folder, writing the HTA payload to disk, and then calling it using the batch script
* If Avast, AVG, or Avira are detected, it works by directly copying the payload into the Startup directory and executing it
* If no recognized antivirus solution is detected, it falls back to a combination of batch file execution, registry based persistence, and payload deployment prior to launching the batch script

The second HTA file includes a DLL named "iinneldc.dll" that functions as a fully-featured RAT, supporting remote system control, file management, data exfiltration, screenshot capture, clipboard manipulation, and process control.

"APT36 (Transparent Tribe) remains a highly persistent and strategically driven cyber-espionage threat, with a sustained focus on intelligence collection targeting Indian government entities, educational institutions, and other strategically relevant sectors," the cybersecurity company said.

In recent weeks, APT36 has also been linked to another campaign that leverages a malicious shortcut file disguised as a government advisory PDF ("NCERT-Whatsapp-Advisory.pdf.lnk") to deliver a .NET-based loader, which then drops additional executables and malicious DLLs to establish remote command execution, system reconnaissance, and long-term access.

The shortcut is designed to execute an obfuscated command using cmd.exe to retrieve an MSI installer ("nikmights.msi") from a remote server ("aeroclubofindia.co[.]in"), which is responsible for initiating a series of actions -

* Extract and display a decoy PDF document to the victim
* Decode and write DLL files to "C:\ProgramData\PcDirvs\pdf.dll" and "C:\ProgramData\PcDirvs\wininet.dll"
* Drop "PcDirvs.exe" to the same the same location and execute it after a delay of 10 seconds
* Establish persistence by creating "PcDirvs.hta" that contains Visual Basic Script to make Registry modifications to launch "PcDirvs.exe" every time after system startup

It's worth pointing out that the lure PDF displayed is a [legitimate advisory](https://web.archive.org/web/20240808195321/https%3A//pkcert.gov.pk/advisory/24-12.pdf) issued by the National Cyber Emergency Response Team of Pakistan (PKCERT) in 2024 about a fraudulent WhatsApp message campaign targeting government entities in Pakistan with a malicious WinRAR file that infects systems with malware.

The DLL "wininet.dll" connects to a hard-coded command-and-control (C2) infrastructure hosted at dns.wmiprovider[.]com. It was registered in mid-April 2025. The C2 associated with the activity is currently inactive, but the Windows Registry-based persistence ensures that the threat can be resurrected at any time in the future.

"The DLL implements multiple HTTP GET–based endpoints to establish comm...