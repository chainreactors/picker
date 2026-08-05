---
title: Fake Adobe and Zoom Updates Install ScreenConnect for Persistent Remote Access
url: https://thehackernews.com/2026/08/fake-adobe-and-zoom-updates-install.html
source: The Hacker News
date: 2026-08-04
fetch_date: 2026-08-05T04:59:29.990196
---

# Fake Adobe and Zoom Updates Install ScreenConnect for Persistent Remote Access

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

# [Fake Adobe and Zoom Updates Install ScreenConnect for Persistent Remote Access](https://thehackernews.com/2026/08/fake-adobe-and-zoom-updates-install.html)

**Ravie Lakshmanan**Aug 04, 2026Threat Intelligence / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi35nnI5-o_HtA0Eunk4tOFM1lg12NrqY7HrDNBbee-kPWR-BHHxXQtd-Tj3b7FrMlTOcWNC63XgVV9n0FEoD-G4ydCpmBv2g1PjvS-lzopLbMnODHbNL2bGMJ6nOYXST9M83vc9IYZaUOjkUqaa4Xo-LaAOtXu3bRhYAcVIUwxgDNMifc6xWI27VVca_B4/s1700-e365/screenconnect.jpg)

Cybersecurity researchers have disclosed details of an active, multi-wave campaign that employs social engineering lures themed around Adobe and Zoom software updates, business document reviews, and system maintenance utilities to stealthily deploy Remote Monitoring and Management (RMM) programs like ConnectWise ScreenConnect.

The campaign has been codenamed **SMOKE#SCREEN** by Securonix Threat Research.

"The campaign relies on a toolkit of VBScript droppers, batch file loaders, compiled .NET executables and an HTML phishing page, all ultimately pointing to a live WsgiDAV-based staging server at 207.174.0[.]143:8080," researchers Shikha Sangwan, Akshay Gaikwad, and Aaron Beardslee said in a [report](https://www.securonix.com/blog/smoke-screen-screenconnect-rmm-abuse-cloudflare-tunnels/) shared with The Hacker News.

Successful attacks culminate with a ScreenConnect agent installed and beaconing to one of three attacker-controlled relay servers, providing the attackers with persistent remote access to compromised systems. The activity has not been attributed to any known threat actor or group.

The findings add to the growing abuse of legitimate RMM tools by threat actors, as it allows them to bypass security controls and take advantage of their prevalence in enterprise environments to blend in with authorized IT tooling without the need for deploying a purpose-built remote access trojan.

Securonix said its investigation commenced following the discovery of a live WsgiDAV server that served two purposes: stage malicious payloads and maintain command-and-control (C2) over existing infected machines through a ScreenConnect relay on port 8041.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

An analysis of the ScreenConnect relay configuration strings embedded in the MSI and EXE payloads has uncovered three distinct C2 clusters, each associated with software update, document review, and document viewer decoy binaries.

The initial access vector is assessed to be spear-phishing, with the emails serving as a conduit for an obfuscated Visual Basic Script (aka VBScript) dropper that first performs a series of environment and anti-analysis checks to ensure safe execution. It also enumerates running processes, and aborts if any of the following executables are running -

* Wireshark (wireshark.exe)
* Process Monitor (procmon.exe)
* Oracle VM VirtualBox (vboxservice.exe)
* Broadcom VMware Tools (vmtoolsd.exe)
* Citrix XenServer (xenservice.exe)
* Fiddler Classic (fiddler.exe)

If the environment checks pass, the script proceeds to decrypt a PowerShell command that fetches a C# payload from "207.189.11[.]170" and executes it. Alternatively, attacks have been observed using business-themed lures to trick recipients into running a VBScript that ultimately leads to ScreenConnect installation.

A third sample linked to the activity is delivered as a compressed archive, from which a batch script is run to disable Windows Antimalware Scan Interface (AMSI), escalate privileges by means of a User Account Control (UAC) prompt, turn off SmartScreen protections via Registry modifications, and then remove the Zone.Identifier alternate data stream (ADS) from the downloaded MSI file before running it.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_EY8skrKXmsu5XkbZKEbH2BmMz-YnJF2Moj0NrrjnCclyeRJt_3f4pyTW8zPm7UhrGBx7XtffP89NZxjRbG7XhvJOHrbc0JuvgsTcu31YLZV5pPyw544o6nYaKQkalcrVn1xy3rcJDRMq4oyJy3YOhfzYmW4n7KhbFSY2eeuL_Msd90mUIZVDKZgZ5Lbr/s1700-e365/ZOOM.png)

"The actor's delivery strategy has also rotated across multiple trusted hosting services," Securonix said. "An early phishing page ('zoom-update.html') delivers its payload via a Dropbox shared link, bypassing domain reputation filters since Dropbox is an allow-listed platform in most corporate environments."

"A compiled .NET loader ('MemoryLoader.cs') references a Cloudflare Quick Tunnel (subscription-magnetic-recommended-meat.trycloudflare.com), a service designed for temporary local server exposure that is rarely monitored. The staging server itself runs cloudflared.exe, confirming that the actor uses the Cloudflare binary directly on their infrastructure to generate these ephemeral tunnels."

Irrespective of the phishing lure used, all attack paths lead to the same destination: the installation of ScreenConnect client, which connects to a configured relay server and allows the operator to open a remote desktop session with the victim's machine.

"What makes this campaign particularly notable for defenders is the observable arc of the actor's tradecraft," Securonix said. "From cautious XOR-encrypted VBScript droppers to aggressive nine-step Defender destruction sequences and then, most recently, a pivot back to stealth with anti-EDR timing and self-contained encrypted bundles, the campaign reads like a real-time arms race between attacker and defender."

To counter the threat, organizations are recommended to restrict execution of untrusted MSI files, monitor when processes attempt to tamper with security products, audit legitimate use of RMM tools, check for suspicious PowerShell and "cmd.exe" processes, and enforce strict UAC settings to prevent standard users from bypassing UAC prompts for administrative tasks.

### Fake Xeno Roblox Cheats Deliver Java Stealer Malware

The disclosure comes as Bitdefender [warned](https://www.bitdefender.com/en-us/blog/labs/fake-xeno-roblox-discord-executor) of a separate campaign in which fake Xeno Executor installers promoted via gaming forums and Discord communities are used to initiate a multi-stage Java infection chain that drops an information stealer capable of credential theft, as well as ste...