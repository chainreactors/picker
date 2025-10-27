---
title: Storm-2603 Deploys DNS-Controlled Backdoor in Warlock and LockBit Ransomware Attacks
url: https://thehackernews.com/2025/08/storm-2603-exploits-sharepoint-flaws-to.html
source: The Hacker News
date: 2025-08-02
fetch_date: 2025-10-07T00:52:24.571189
---

# Storm-2603 Deploys DNS-Controlled Backdoor in Warlock and LockBit Ransomware Attacks

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

# [Storm-2603 Deploys DNS-Controlled Backdoor in Warlock and LockBit Ransomware Attacks](https://thehackernews.com/2025/08/storm-2603-exploits-sharepoint-flaws-to.html)

**Aug 01, 2025**Ravie LakshmananThreat Intelligence / Ransomware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiP-Fw_YsyZX4C8fumIuzFLB0jEWxAAUkclAnSxKozJU7n8YyDJ_bFZ7ElnemeXj_t4dJHyIBtOY2JhStCTVxAY01dqammhjppPs-mI8j6AFFKj5nMdyhsop0mDkm5iqc6_IlJWLh7jbkHL3Czj_umM8S5hd-Lvu5ZNp8mv7ZscjQ6o-TNvUvxLFCWRJ_G5/s790-rw-e365/ransomware-sharepoint.jpg)

The threat actor linked to the exploitation of the recently disclosed security flaws in Microsoft SharePoint Server is using a bespoke command-and-control (C2) framework called **AK47 C2** (also spelled ak47c2) in its operations.

The framework includes at least two different types of clients, HTTP-based and Domain Name System ([DNS](https://www.cloudflare.com/learning/dns/what-is-dns/))-based, which have been dubbed AK47HTTP and AK47DNS, respectively, by Check Point Research.

The activity has been attributed to [Storm-2603](https://thehackernews.com/2025/07/storm-2603-exploits-sharepoint-flaws-to.html), which, according to Microsoft, is a suspected China-based threat actor that has leveraged the [SharePoint flaws](https://thehackernews.com/2025/07/microsoft-links-ongoing-sharepoint.html) – CVE-2025-49706 and CVE-2025-49704 (aka ToolShell) – to deploy Warlock (aka X2anylock) ransomware.

A previously unreported threat cluster, evidence gathered following an analysis of VirusTotal artifacts shows that the group may have been active since at least March 2025, deploying ransomware families like [LockBit Black](https://www.security.com/threat-intelligence/lockbit-ransomware-attack-techniques) and Warlock together – something that's not observed commonly among established e-crime groups.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Based on VirusTotal data, Storm-2603 likely targeted some organizations in Latin America throughout the first half of 2025, in parallel to attacking organizations in APAC," Check Point [said](https://research.checkpoint.com/2025/before-toolshell-exploring-storm-2603s-previous-ransomware-operations/).

The attack tools used by the threat actor includes legitimate open-source and Windows utilities like masscan, WinPcap, SharpHostInfo, nxc, and PsExec, as well as a custom backdoor ("dnsclient.exe") that uses DNS for command-and-control with the domain "update.updatemicfosoft[.]com."

The backdoor is part of the AK47 C2 framework, alongside AK47HTTP, that's employed to gather host information and parse DNS or HTTP responses from the server and execute them on the infected machine via "cmd.exe." The initial access pathway used in these attacks are unknown.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWlTGmJPG0RaFeLHGgaXUcP3z2Kph-PiTIvBFL1T49iIn9j20HrelrzbMeBSEJzAsPktfgMU9mMpstEogXx8enAKzI45uVdR4539OmZBr1czD-sb12y9pwDXV_U9MuP-vOfupCHScOWGbPyuc-73fg2bJUDALK7WbeqOjkxZN4kjJwV5B9J5S4DuyWHvwg/s790-rw-e365/cp.jpg)

A point worth mentioning here is that the aforementioned infrastructure was also flagged by Microsoft as used by the threat actor as a C2 server to establish communication with the "spinstall0.aspx" web shell. In addition to the open-source tools, Storm-2603 has been found to distribute three additional payloads -

* 7z.exe and 7z.dll, the legitimate 7-Zip binary that's used to sideload a malicious DLL, which delivers Warlock
* bbb.msi, an installer that uses clink\_x86.exe to sideload "clink\_dll\_x86.dll," which leads to LockBit Black deployment

Check Point said it also discovered another MSI artifact uploaded to VirusTotal in April 2025 that's used to launch Warlock and LockBit ransomware, and also drop a custom antivirus killer executable ("VMToolsEng.exe") that employs the bring your own vulnerable driver ([BYOVD](https://thehackernews.com/2024/11/researchers-uncover-malware-using-byovd.html)) technique to [terminate security software](https://thehackernews.com/2025/03/medusa-ransomware-uses-malicious-driver.html) using ServiceMouse.sys, a third-party driver provided by Chinese security vendor Antiy Labs.

Ultimately, Storm-2603's exact motivations remain unclear at this stage, making it harder to determine if it's espionage-focused or driven by profit motives. However, it bears noting that there have been [instances](https://thehackernews.com/2025/02/hackers-exploited-pan-os-flaw-to-deploy.html) where nation-state actors from China, Iran, and North Korea have deployed ransomware on the side.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"We tend to assess it is a financially motivated actor, but with this, we can't also exclude the option that this is a dual motivation actor, both espionage and financially motivated," Sergey Shykevich, Threat Intelligence Group Manager at Check Point, told The Hacker News.

"Storm-2603 leverages BYOVD techniques to disable endpoint defenses and DLL hijacking to deploy multiple ransomware families – blurring the lines between APT and criminal ransomware operations," Check Point added. "The group also uses open-source tools like PsExec and masscan, signaling a hybrid approach seen increasingly in sophisticated attacks."

### More Details About Storm-2603 Emerge

Palo Alto Networks Unit 42, which is tracking Storm-2603 under the moniker CL-CRI-1040, said it has also observed the threat activity cluster using AK47 C2 prior to the exploitation of ToolShell flaws in Microsoft SharePoint Server.

"CL-CRI-1040 was formerly associated with a LockBit 3.0-affiliate and has recently been operating a double-extortion data leak site known as Warlock," the company [said](https://unit42.paloaltonetworks.com/ak47-activity-linked-to-sharepoint-vulnerabilities/).

Describing AK47 C2 as a multi-protocol supporting backdoor, Unit 42 said the tool comes with capabilities to execute arbitrary ...