---
title: TWINLOOT Abuses SharePoint and Teams to Steal Credentials and Move Across Networks
url: https://thehackernews.com/2026/08/twinloot-abuses-sharepoint-and-teams-to.html
source: The Hacker News
date: 2026-08-18
fetch_date: 2026-08-19T03:00:29.089266
---

# TWINLOOT Abuses SharePoint and Teams to Steal Credentials and Move Across Networks

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

# [TWINLOOT Abuses SharePoint and Teams to Steal Credentials and Move Across Networks](https://thehackernews.com/2026/08/twinloot-abuses-sharepoint-and-teams-to.html)

**Ravie Lakshmanan**Aug 18, 2026Endpoint Security / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIrQ96TUVfZUEVto7SlNlTp_8P2270tmrpifBbd-F8vo3gQz3Na40YH60oRh2dEazLOZInJzCGa66bxl9t85Usl30eG_Db_yjMWup2eOM3BmaPhILk_Ihs-yo6AdB-DWG99L7OXK9bdD8Jygu2imWU71-Ap3bPtYLOgqu-vO2Zbr5egp6A5HNcXDSaa0o2/s1700-e365/windows-malware.jpg)

Cybersecurity researchers have disclosed details of a previously undocumented Python implant framework dubbed **TWINLOOT**.

"TWINLOOT is a modular, PyArmor-hardened Python implant designed to operate its entire command-and-control infrastructure inside trusted Microsoft services," Ontinue [said](https://www.ontinue.com/resource/python-implant-hiding-its-entire-c2-inside-microsoft-365-azure/) in a technical report shared with The Hacker News. "Tasking flows through SharePoint Online file dead-drops via the Microsoft Graph API. Interactive operator access routes through WebRTC DataChannels relayed by Microsoft Teams [TURN](https://learn.microsoft.com/en-us/openspecs/office_protocols/ms-turn/bf1e2a02-4f6e-4975-b83c-74018546b387) servers."

Traffic to and from the Graph API is driven by means of a headless instance of the victim's own Edge browser, thereby making it virtually indistinguishable from legitimate network activity. The implant is equipped to harvest Windows credentials using pixel-perfect fake lock screens, offer a reverse SOCKS5 pivot into victim networks, execute arbitrary commands, and establish persistence on the host.

Ontinue's Cyber Defense Center said it discovered the implant during its investigation into an ongoing campaign in July 2026. A defining aspect of the malware is its use of multiple command-and-control (C2) channels, all of which make use of Microsoft services -

* SharePoint Online (Graph API) for tasking
* Teams TURN relays for interactive access
* Victim's Edge browser for ferrying Graph traffic

The initial access vector is assessed to be a social engineering attack via Microsoft Teams, in which the threat actor masquerading as IT support persuaded a target to run a PowerShell command that's responsible for downloading an archive file containing the Python runtime and a 39 MB compiled payload ("bootstrap-fat.pyc"), which serves as a loader for TWINLOOT.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Describing the threat actor as knowledgeable in offensive tradecraft and Microsoft's cloud architecture, Ontinue said the Python framework is the first such tool to combine Microsoft 365 dead drop C2, Teams TURN relay abuse, and headless browser transport under a single umbrella.

TWINLOOT runs two parallel channels from the victim machine: One is a SharePoint dead drop that authenticates to an attacker's Azure tenant and polls a SharePoint drive for commands every 15 seconds, allowing the operator to receive instructions, run them, and exfiltrate data back to the server.

The second channel makes use of a reverse SOCKS5 tunnel to enable interactive access and lateral movement. "It runs over either a direct TLS/WebSocket connection to the attacker's server or through the Teams TURN WebRTC relay," Ontinue said.

"The operator gets a SOCKS5 listener on their own machine (127.0.0.1:1080), and proxies traffic through it into the victim's internal network. Those connections exit from pythonw.exe on the victim host to internal targets on ports like 445 (SMB), 3389 (RDP), 5985 (WinRM), and 1433 (MSSQL). To the victim's internal network, it looks like the compromised host is making normal lateral connections."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgqr4Hxv6gPC21WpV8-IsKUNfO-t0jFH40JmoZ5ujHO4eNotOFrPZjMxT4XyaDgbt_fNQ_ffGFnI5JxTUPGIwkBPp6vcFXfwonppT1Kx8FKK5hnCEkdtfbSjsf0sTervDYFcy_gm3OJmmyoO2p98g6TPNMnMMXdJcUIrJVjEI3FayYgYDhqbZs7-0Z73pPA/s1700-e365/chain.jpg)

To enable lateral movement, the operator captures the victim's password via bogus lock screen prompts and exfiltrates it over the SharePoint channel. The fake screen is rendered when the "credz\_waiting" command is issued by the threat actor.

It's worth noting that the entered password is not validated against Windows authentication to check if the victim has entered the right system password. Regardless of what is provided, the victim is displayed an error message "The password is incorrect. Try again," likely causing them to input the correct password the second time.

Once the credential is entered, the fake lock screen is automatically closed. Every password captured by the screen is encrypted and uploaded to the SharePoint drive. These credentials are then abused through the SOCKS5 tunnel to pivot to the next host using Remote Desktop Protocol (RDP) or WinRM.

This is not the first time bad actors have leveraged a TURN-based mechanism to communicate with the threat actor. In June 2026, Broadcom-owned Symantec and Carbon Black detailed DragonForce ransomware's use of a Go-based remote access trojan (RAT) called [Backdoor.Turn](https://thehackernews.com/2026/06/dragonforce-hackers-abuse-microsoft.html) to conceal command-and-control (C2) traffic inside Microsoft Teams relay infrastructure.

Although the overall modus operandi is the same, the manner in which they are implemented is different in both tools: Backdoor.Turn uses a QUIC session through the relay. TWINLOOT, on the other hand, uses WebRTC DataChannels via aiortc.

Then, late last month, another new Rust-based RAT dubbed [msaRAT](https://blog.talosintelligence.com/chaos-msarat-living-off-the-browser-to-build-covert-c2-channel/) was observed using the same TURN method, but against Twilio instead of Teams. Attributed to the [Chaos ransomware group](https://thehackernews.com/2025/07/chaos-raas-emerges-after-blacksuit.html), the mal...