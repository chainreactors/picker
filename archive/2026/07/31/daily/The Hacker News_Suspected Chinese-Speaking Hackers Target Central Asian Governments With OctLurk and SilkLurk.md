---
title: Suspected Chinese-Speaking Hackers Target Central Asian Governments With OctLurk and SilkLurk
url: https://thehackernews.com/2026/08/suspected-chinese-speaking-hackers.html
source: The Hacker News
date: 2026-07-31
fetch_date: 2026-08-01T05:13:34.732142
---

# Suspected Chinese-Speaking Hackers Target Central Asian Governments With OctLurk and SilkLurk

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

![cybersecurity](data:image/svg+xml;base64...)

# [Suspected Chinese-Speaking Hackers Target Central Asian Governments With OctLurk and SilkLurk](https://thehackernews.com/2026/08/suspected-chinese-speaking-hackers.html)

**Ravie Lakshmanan**Jul 31, 2026Malware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmBagWdesuJqVgNAHPh7t75IGrajY_oJeL9HHI7r23AK7CuLUN22-GBwDCWJWTlIutBApsdhSGproqxtR6kV_Dg04FT2zc6vZXZCQed8Kx3bD-jw-VXkYfAHlJsNgcQOcqRFW8TTh1kyN34MisnGx3ImU9vejv_oNy4jN0sPNcPM7jclq7klrMmGrnROjk/s1700-e365/chinese-hackers.jpg)

A Chinese-speaking threat actor is suspected to be behind a fresh wave of cyber attacks targeting government organizations mainly located in Central Asia, including Afghanistan, Kyrgyzstan, Tajikistan, Uzbekistan, Kazakhstan, and the Syrian Arab Republic, since January 2025.

These targeted organizations operate across several sectors, such as healthcare, research, government offices, ministries of foreign affairs, logistics, law-enforcement agencies, urban planning and facilities management, and public educational establishments, per Kaspersky. The activity has not been linked to any known adversary or group.

The attacks are characterized by the use of two new obfuscated backdoors the Russian cybersecurity company is tracking as **OctLurk** and **SilkLurk**, as well as a specialized utility codenamed **LurkProxy** to proxy network traffic.

"OctLurk and SilkLurk can download and inject additional plugins to perform further malicious actions, including launching command shells, performing file system activity, synthesizing keyboard and mouse events, network scanning, credential dumping, keylogging, password theft from browsers, email collection, and remote access," researchers Saurabh Sharma and Yaroslav Kikel [said](https://securelist.com/octlurk-silklurk-backdoors-central-asia/120840/).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The initial access vector used in these attacks is currently unknown. However, Kaspersky analysis has found that OctLurk is injected into memory and deployed by means of a loader, with the attackers also checking internet connectivity to the domain "dns.ssentialserv[.]xyz" before executing a batch script responsible for launching LurkProxy. The tool then establishes contact with a remote server ("154.196.162[.]76") for command-and-control (C2).

Once run, OctoLurk first collects system information, encrypts it, and sends it to a hard-coded C2 server ("dns.multitoconference[.]com") over a stream socket connection. It's equipped to load plugins received from the server directly into memory to enable command execution, file operations, clipboard content gathering and modification, screenshot capture, and mouse movements.

The threat actors have been found to leverage the backdoor's command shell plugin to perform the following series of actions -

* Fingerprint the host and harvest extensive data about the compromised system.
* Run commands to export successful logon events for remote interactive logons and to query those events for specific users.
* Harvest password hashes from domain controllers using Impacket's "secretsdump.py" tool.
* Drop and execute a keylogger that masquerades as AnyDesk to sidestep detection.
* Decrypt and extract passwords from Google Chrome and Mozilla Firefox.
* Establish remote access to the victim machine using Pandora RC agent.
* Scan internal and public networks using [Fscan](https://github.com/shadow1ng/fscan) to identify services running on specific ports, such as Secure Shell (SSH) on port 22 and MySQL on port 3306, and then attempt to access these services using credentials from a password file named "pp.txt."
* Connect to an email server, authenticate with a username and password, and issue commands to collect or manipulate emails.

LurkProxy, for its part, can function as a reverse proxy in two distinct modes, either as a SOCKS5 proxy or a transparent proxy. At any given time, the malware can operate in only one mode to route network traffic through a target address.

The third tool in the threat actor's arsenal is SilkLurk, which is launched by means of a DLL that, in turn, is executed using a DLL side-loading sequence. The backdoor then creates a TCP socket and connects to a C2 server specified in its configuration, followed by collecting victim information and transmitting it to the server.

In response, the server sends a command that's to be executed on the infected endpoint. This can involve getting the system's local time, setting a sleep interval that determines the frequency at which the backdoor polls the C2 server, sending or updating backdoor configuration, and receiving and injecting additional plugins into memory.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The post-compromise activity linked to SilkLurk is below -

* Invoke "cmd.exe" to launch PowerShell and run commands to connect to shared network resources with administrative credentials, search and stage confidential documents, disconnect from the network shares, and use legitimate archiving tools like WinRAR and 7-Zip to archive the stolen data.
* Run "cmd.exe" to initiate a DLL side-loading chain to drop [PlugX](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html), a known backdoor used by Chinese hacking groups.

Kaspersky said it found infrastructure overlaps between the campaign and a prior set of attacks involving a C++-based implant codenamed [SilentRaid](https://thehackernews.com/2026/01/china-linked-uat-7290-targets-telecoms.html) (aka MystRodX and TrustFall).

"This overlap points to shared infrastructure across multiple OS-targeting campaigns, though it remains unclear whether these activities ran concurrently or at different times," Kaspersky said. "The emergence of the OctLurk and SilkLurk multi-plugin malware framework highlights how threat actors continuously refine their tactics to evade detection and maintain control over compromised networks."

"Both families operate primarily in memory, leaving only a minimalistic loader on disk that relies on machine-specific data (OctLurk uses the drive serial number, and SilkLurk uses the computer name) to decode payload locations and contents. This...