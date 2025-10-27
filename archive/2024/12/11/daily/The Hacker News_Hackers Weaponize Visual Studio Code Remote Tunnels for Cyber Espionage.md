---
title: Hackers Weaponize Visual Studio Code Remote Tunnels for Cyber Espionage
url: https://thehackernews.com/2024/12/hackers-weaponize-visual-studio-code.html
source: The Hacker News
date: 2024-12-11
fetch_date: 2025-10-06T19:42:44.629128
---

# Hackers Weaponize Visual Studio Code Remote Tunnels for Cyber Espionage

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

# [Hackers Weaponize Visual Studio Code Remote Tunnels for Cyber Espionage](https://thehackernews.com/2024/12/hackers-weaponize-visual-studio-code.html)

**Dec 10, 2024**Ravie LakshmananCyber Espionage / Hacking News

[![Visual Studio Code Remote Tunnels](data:image/png;base64... "Visual Studio Code Remote Tunnels")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmvx6hHNMpftMJkujVD-BWERfWb5DSC5ab9xWaRGg5RXf5ruo2LOd0b2TpOipYjce0bW6b6PgysenLOdmAHM6tHXaLaS0B4_s8SabqZacBI633q6i05Csuqc8QwqCigmeEXnIeu2m1fMtK5WJ4dKvDkJtAuLP88EmcMB3GwckaWBmKc2mW8jnmUxIZa6g-/s790-rw-e365/chinese-hackers.png)

A suspected China-nexus cyber espionage group has been attributed to an attacks targeting large business-to-business IT service providers in Southern Europe as part of a campaign codenamed **Operation Digital Eye**.

The intrusions took place from late June to mid-July 2024, cybersecurity companies SentinelOne SentinelLabs and Tinexta Cyber said in a joint report shared with The Hacker News, adding the activities were detected and neutralized before they could progress to the data exfiltration phase.

"The intrusions could have enabled the adversaries to establish strategic footholds and compromise downstream entities," security researchers Aleksandar Milenkoski and Luigi Martire [said](https://www.sentinelone.com/labs/operation-digital-eye-chinese-apt-compromises-critical-digital-infrastructure-via-visual-studio-code-tunnels).

"The threat actors abused Visual Studio Code and Microsoft Azure infrastructure for C2 [command-and-control] purposes, attempting to evade detection by making malicious activities appear legitimate."

It's currently not known which China-linked hacking group is behind the attacks, an aspect complicated by the widespread toolset and infrastructure sharing among threat actors aligned with the East Asian nation.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Central to Operation Digital Eye is the weaponization of Microsoft Visual Studio Code [Remote Tunnels](https://code.visualstudio.com/docs/remote/tunnels) for C2, a legitimate feature that enables remote access to endpoints, granting attackers the ability to execute arbitrary commands and manipulate files.

Part of why government-backed hackers use such public cloud infrastructure is so that their activity blends into the typical traffic seen by network defenders. Furthermore, such activities employ legitimate executables that are not blocked by application controls and firewall rules.

Attack chains observed by the companies entail the use of [SQL injection](https://en.wikipedia.org/wiki/SQL_injection) as an initial access vector to breach internet-facing applications and database servers. The code injection is accomplished by means of a legitimate penetration testing tool called [SQLmap](https://thehackernews.com/2023/12/new-hacker-group-gambleforce-tageting.html) that automates the process of detecting and exploiting SQL injection flaws.

A successful attack is followed by the deployment of a PHP-based web shell dubbed PHPsert that enables the threat actors to maintain a foothold and establish persistent remote access. Subsequent steps include reconnaissance, credential harvesting, and lateral movement to other systems in the network using Remote Desktop Protocol (RDP) and pass-the-hash techniques.

"For the pass-the-hash attacks, they used a custom modified version of Mimikatz," the researchers said. The tool "enables the execution of processes within a user's security context by leveraging a compromised NTLM password hash, bypassing the need for the user's actual password."

[![Visual Studio Code Remote Tunnels](data:image/png;base64... "Visual Studio Code Remote Tunnels")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhl9658YMONJ7f2xuPOH60aUEbOZoOvTNSVDGX3qqSdHqq3yMScF1_nMjP_dT8A0IhshHgu2FOYmpdzBfCl4K9K_N9Z80k4MRolDcONZDa2MsEBEyOuy7dEZQT7Zv8L8NRliYgwVwhGt_MY5hJQ-oKllBRqdWXNUboWcWMcrMW1J2GD0o6vdImxbx0hoRRT/s790-rw-e365/malware.png)

Substantial source code overlaps suggest that the bespoke tool originates from the same source as the ones observed exclusively in suspected Chinese cyber espionage activities, such as [Operation Soft Cell and Operation Tainted Love](https://thehackernews.com/2023/03/operation-soft-cell-chinese-hackers.html). These custom Mimikatz modifications, which also include shared code-signing certificates and the use of unique custom error messages or obfuscation techniques, have been collectively titled mimCN.

"The long-term evolution and versioning of mimCN samples, along with notable features such as instructions left for a separate team of operators, suggest the involvement of a shared vendor or digital quartermaster responsible for the active maintenance and provisioning of tooling," the researchers pointed out.

"This function within the Chinese APT ecosystem, corroborated by the [I-Soon leak](https://thehackernews.com/2024/03/two-chinese-apt-groups-ramp-up-cyber.html), likely plays a key role in facilitating China-nexus cyber espionage operations."

Also of note is the reliance on SSH and Visual Studio Code Remote Tunnels for remote command execution, with the attackers using GitHub accounts for [authenticating and connecting to the tunnel](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/security) in order to access the compromised endpoint through the browser-based version of Visual Studio Code ("vscode[.]dev").

That said, it's not known if the threat actors utilized freshly self-registered or already compromised GitHub accounts to authenticate to the tunnels.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Besides mimCN, some of the other aspects that point to China are the presence of simplified Chinese comments in PHPsert, the [use of infrastructure](https://thehackernews.com/2023/12/researchers-unmask-sandman-apts-hidden.html) provided by Romanian hosting service provider M247, and the use of Visual St...