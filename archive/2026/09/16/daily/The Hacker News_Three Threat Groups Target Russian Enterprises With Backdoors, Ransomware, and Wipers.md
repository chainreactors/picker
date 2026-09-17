---
title: Three Threat Groups Target Russian Enterprises With Backdoors, Ransomware, and Wipers
url: https://thehackernews.com/2026/09/three-threat-groups-target-russian.html
source: The Hacker News
date: 2026-09-16
fetch_date: 2026-09-17T06:59:40.478070
---

# Three Threat Groups Target Russian Enterprises With Backdoors, Ransomware, and Wipers

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

# [Three Threat Groups Target Russian Enterprises With Backdoors, Ransomware, and Wipers](https://thehackernews.com/2026/09/three-threat-groups-target-russian.html)

**Ravie Lakshmanan**Sep 16, 2026Malware / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMMZZrs8eh-baUC-73E9tejQYA0JZzWyoElUJGhCi0N4_f2EzmPPhQW3xY0kmNZv775T26ywu4czdta-vHaLp1gaI03eqho2SSe3riHMZP8hLTrU1ETnIv-k1ywOpnBFvbkyQJNZt7F4Xx4NndvvS8esTt1jzaCdeN9JZNkNB8sBU1vytibSRAjMsLZzc6/s1700-nu-rw-lo-l85-e365/russian-groups.jpg)

Enterprises in Russia have emerged as the target of three threat activity clusters tracked as **NightEagle**, **Hacking Cat**, and **Toy Ghouls**, according to multiple reports from Kaspersky.

The cybersecurity vendor said it has [identified attacks](https://securelist.com/tr/nighteagle-apt-ghostcontainer-and-tunneling/121323/) mounted by [NightEagle](https://thehackernews.com/2025/07/nighteagle-apt-exploits-microsoft.html) (aka APT-Q-95), a threat actor known to be active since at least 2023, that involve new techniques for persistence and lateral movement.

"In most incidents, the attackers used compromised valid credentials to gain access to corporate VPNs," Kaspersky said in an analysis published today. "VPN connections originated from IP addresses in the Russian segment linked to Cloudflare WARP tunnels, as well as from IP addresses associated with European virtual infrastructure providers."

The attacks, as highlighted in July 2025, involve the deployment of [GhostContainer](https://thehackernews.com/2025/07/hackers-exploit-apache-http-server-flaw.html#exchange-servers-targeted-by-ghostcontainer-backdoor), a known modular backdoor that grants the operators complete access to a victim's Microsoft Exchange Server, as well as run arbitrary code, perform file operations, and load additional modules.

To sidestep detection, the malware masquerades as a common server component to blend in with regular operations. It can also function as a traffic redirection or tunnel. Prior attacks involving the malware have targeted a government agency and a high-tech company located in Asia.

"It incorporates components from several open-source projects, including the Neo-reGeorg tunnel, an exploit for the CVE-2020-0688 vulnerability, and the GhostWebShell class from the ysoserial utility," Kaspersky explained. "All of these components are publicly available on GitHub."

The exact method used by the attackers to deliver GhostContainer to Microsoft Exchange servers is unknown, although it's believed to have involved the extraction of cryptographic keys used by the server from the ASP.NET configuration, followed by overwriting the VIEWSTATE framework parameter, and injecting a payload into it, causing the backdoor to be launched in memory.

To move laterally within the internal network, NightEagle has been observed downloading tunneling tools to redirect network traffic via RDP using [Microsoft dev tunnels](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/overview) and an open-source program called [rdp2tcp](https://github.com/V-E-O/rdp2tcp).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

"To obtain elevated privileges and move laterally through the network, NightEagle exploited various vulnerabilities in Active Directory," Kaspersky added. "The attackers used previously established tunnels to connect to internal infrastructure systems."

This includes the exploitation of [CVE-2019-0708](https://nvd.nist.gov/vuln/detail/cve-2019-0708) (aka [BlueKeep](https://support.microsoft.com/en-us/servicing/os/windows/2019/05/customer-guidance-for-cve-2019-0708-remote-desktop-services-remote-code-execution-vulnerability-may)) to create a local account on the system and add it to the Administrators and Remote Desktop Users groups. Furthermore, the attackers have attempted to impersonate the domain controller by means of a [DCSync attack](https://www.trellix.com/blogs/platform/impersonating-the-boss-how-attackers-drain-active-directory/).

The end goal is to establish persistence in the victim infrastructure, get password hashes for domain accounts, use long-lived Kerberos tickets to gain legitimate access to target resources, and ultimately break into domain controllers and the victim's entire Active Directory infrastructure.

### Pro-Ukrainian Hacking Cat Deploys Gorilla RAT and Monkey Ransomware

The second group to single out Russian enterprises is Hacking Cat, a pro-Ukrainian hacktivist entity with a history of conducting website defacements and data breaches since February 2024. In recent months, however, the group is said to have shifted tactics and pivoted to encryption and destructive attacks.

"Hacking Cat actively collaborates with other hacktivists such as Cyber Anarchy Squad and the Ukrainian Cyber Alliance, which can complicate the attribution of tools to specific attackers," Kaspersky [said](https://securelist.ru/tr/hacking-cat/117062/).

Attacks mounted by the group have weaponized vulnerabilities in Exchange servers (e.g., [CVE-2021-26855](https://nvd.nist.gov/vuln/detail/cve-2021-26855) and [CVE-2026-42897](https://nvd.nist.gov/vuln/detail/CVE-2026-42897)) to deliver a Go-based remote access trojan dubbed Gorilla RAT, which can tunnel traffic to allow the operator to access the victim's internal network.

Once launched, the malware establishes a connection with a remote server, registers the victim, and awaits further instructions that allow it to run arbitrary commands, enumerate processes, gather system information, upload/download files, and open or close a TCP tunnel.

Also delivered by the threat actor are multiple variants of a ransomware family dubbed Monkey that are written in Rust, .NET, C++, and Golang to target Windows, Linux, and VMware ESXi systems. The earliest Monkey ransomware artifact dates back to late summer 2025. The malware also takes steps to terminate unnecessary processes...