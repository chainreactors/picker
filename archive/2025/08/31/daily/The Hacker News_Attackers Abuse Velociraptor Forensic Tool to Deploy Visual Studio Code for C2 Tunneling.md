---
title: Attackers Abuse Velociraptor Forensic Tool to Deploy Visual Studio Code for C2 Tunneling
url: https://thehackernews.com/2025/08/attackers-abuse-velociraptor-forensic.html
source: The Hacker News
date: 2025-08-31
fetch_date: 2025-10-07T00:18:02.082862
---

# Attackers Abuse Velociraptor Forensic Tool to Deploy Visual Studio Code for C2 Tunneling

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

# [Attackers Abuse Velociraptor Forensic Tool to Deploy Visual Studio Code for C2 Tunneling](https://thehackernews.com/2025/08/attackers-abuse-velociraptor-forensic.html)

**Aug 30, 2025**Ravie LakshmananMalware / Endpoint Security

[![Velociraptor Forensic Tool](data:image/png;base64... "Velociraptor Forensic Tool")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgONCKk3MmknRD6PZPrgDLx0brdZZM5s6yE2fH6mmplcIFUYlM6wAlTcDhGFGzDHLWUuuQQkscEunm-2N6iindn4Up48vWIS1YAAAFe8_YG25xDqgmMwnmZoYzwaTFPeWWaG0vEDx-UYNoNMkYEkBsCXeLOvX_hYraMY1gh47-vU1ZH_b4hixAted3ss6kw/s790-rw-e365/win-malware.jpg)

Cybersecurity researchers have called attention to a cyber attack in which unknown threat actors deployed an open-source endpoint monitoring and digital forensic tool called [Velociraptor](https://www.rapid7.com/products/velociraptor/), illustrating ongoing abuse of legitimate software for malicious purposes.

"In this incident, the threat actor used the tool to download and execute Visual Studio Code with the likely intention of [creating a tunnel](https://thehackernews.com/2024/12/hackers-weaponize-visual-studio-code.html) to an attacker-controlled command-and-control (C2) server," the Sophos Counter Threat Unit Research Team [said](https://news.sophos.com/en-us/2025/08/26/velociraptor-incident-response-tool-abused-for-remote-access/) in a report published this week.

While threat actors are known to adopt living-off-the-land (LotL) techniques or take advantage of legitimate remote monitoring and management (RMM) tools in their attacks, the use of Velociraptor signals a tactical evolution, where incident response programs are being used to obtain a foothold and minimize the need for having to deploy their own malware.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Further analysis of the incident has revealed that the attackers used the Windows msiexec utility to download an MSI installer from a Cloudflare Workers domain, which serves as a staging ground for other tools used by them, including a Cloudflare tunneling tool and a remote administration utility known as Radmin.

The MSI file is designed to install Velociraptor, which then establishes contact with another Cloudflare Workers domain. The access is then leveraged to download Visual Studio Code from the same staging server using an encoded PowerShell command and execute the source code editor with the tunnel option enabled in order to allow both remote access and remote code execution.

The threat actors have also been observed utilizing the msiexec Windows utility again to download additional payloads from the workers[.]dev folder.

"Organizations should monitor for and investigate unauthorized use of Velociraptor and treat observations of this tradecraft as a precursor to ransomware," Sophos said. "Implementing an endpoint detection and response system, monitoring for unexpected tools and suspicious behaviors, and following best practices for securing systems and generating backups can mitigate the ransomware threat."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5PE2vlVm6GJ_VAoFaU0pdujXDhIBcI2z-5Kezi65ZCLIGkdyPDiMM2rnLgBH8FAjIoE7UWfSN8uZy9LbAygVR6Sh4nSdECHcg6al0KQd7LfzRghhJjGTvrxnUoGvNFN23uoTWuUGV-ThzpueeaaQVRE4IIkfe3Offvnha5ItH9Sh_qQHEwBgyMv9TzuMN/s790-rw-e365/win.jpg)

The disclosure comes as cybersecurity firms [Hunters](https://www.hunters.security/en/blog/microsoft-teams-phishing-fake-it-helpdesk) and [Permiso](https://permiso.io/blog/sliding-into-your-dms-abusing-microsoft-teams-for-malware-delivery) detailed a malicious campaign that has leveraged Microsoft Teams for initial access, reflecting a growing pattern of threat actors [weaponizing](https://thehackernews.com/2024/11/veildrive-attack-exploits-microsoft.html) the platform's trusted and deeply embedded role in enterprise-focused communications for malware deployment.

These attacks begin with the threat actors using newly created or compromised tenants to send direct messages or initiate calls to targets, impersonating IT help desk teams or other trusted contacts to install remote access software like AnyDesk, DWAgent, or Quick Assist, and seize control of victim systems to deliver malware.

While [similar techniques](https://thehackernews.com/2025/06/former-black-basta-members-use.html) involving remote access tools have been linked to ransomware groups like Black Basta since mid-2024, these newer campaigns forgo the preliminary email bombing step and ultimately make use of the remote access to deliver a PowerShell payload with capabilities commonly associated with credential theft, persistence, and remote code execution.

"The lures used to initiate engagement are tailored to appear routine and unremarkable, typically framed as IT assistance related to Teams performance, system maintenance, or general technical support," Permiso researcher Isuf Deliu said. "These scenarios are designed to blend into the background of everyday corporate communication, making them less likely to trigger suspicion."

It's worth noting that similar tactics have been employed to propagate malware families like [DarkGate](https://thehackernews.com/2024/12/attackers-exploit-microsoft-teams-and.html) and [Matanbuchus](https://thehackernews.com/2025/07/hackers-leverage-microsoft-teams-to.html) malware over the past year.

The attacks also serve a Windows credential prompt to trick users into entering their passwords under the guise of a benign system configuration request, which are then harvested and saved to a text file on the system.

"Microsoft Teams phishing isn't a fringe technique anymore — it's an active, evolving threat that bypasses traditional email defenses and exploits trust in collaboration tools," security researchers Alon Klayman and Tomer Kachlon said.

"By monitoring audit logs like ChatCreated and MessageSent, enriching signals with contextual data, and training users to spot IT/help desk impersonations, SOC teams can clo...