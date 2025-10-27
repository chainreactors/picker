---
title: EastWind Attack Deploys PlugY and GrewApacha Backdoors Using Booby-Trapped LNK Files
url: https://thehackernews.com/2024/08/russian-government-hit-by-eastwind.html
source: The Hacker News
date: 2024-08-13
fetch_date: 2025-10-06T18:09:02.825167
---

# EastWind Attack Deploys PlugY and GrewApacha Backdoors Using Booby-Trapped LNK Files

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

# [EastWind Attack Deploys PlugY and GrewApacha Backdoors Using Booby-Trapped LNK Files](https://thehackernews.com/2024/08/russian-government-hit-by-eastwind.html)

**Aug 12, 2024**Ravie LakshmananCloud Security / Malware

[![Malicious LNK Files](data:image/png;base64... "Malicious LNK Files")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9Cb5W2uk9n6yF4-4U4dn5wsWhrPfn1iwGeBL5KushSPHbRdPwe-23V9SpWR41-kJ2OlAoF1Wlknv14aqlsiHCE6HHGJjULlSnzN7tDCds7QeriaDRe3eojJL9agzS64-HqPKKGJEQW9JaqAvZBZ6DQjztk-1X-Hi14-EKRatL_3iFSJm4LPSliiGFFkay/s790-rw-e365/russia.png)

The Russian government and IT organizations are the target of a new campaign that delivers a number of backdoors and trojans as part of a spear-phishing campaign codenamed **EastWind**.

The attack chains are characterized by the use of RAR archive attachments containing a Windows shortcut (LNK) file that, upon opening, activates the infection sequence, culminating in the deployment of malware such as GrewApacha, an updated version of the [CloudSorcerer](https://thehackernews.com/2024/07/new-apt-group-cloudsorcerer-targets.html) backdoor, and a previously undocumented implant dubbed PlugY.

PlugY is "downloaded through the CloudSorcerer backdoor, has an extensive set of commands and supports three different protocols for communicating with the command-and-control server," Russian cybersecurity company Kaspersky [said](https://securelist.ru/eastwind-apt-campaign/110020/).

The initial infection vector relies on a booby-trapped LNK file, which employs [DLL side-loading techniques](https://attack.mitre.org/techniques/T1574/002/) to launch a malicious DLL file that uses Dropbox as a communications mechanism to execute reconnaissance commands and download additional payloads.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Among the malware deployed using the DLL is GrewApacha, a known backdoor [previously](https://www.ptsecurity.com/ru-ru/research/pt-esc-threat-intelligence/apt31-new-attacks/) [linked](https://habr.com/ru/companies/solarsecurity/articles/723526/) to the China-linked [APT31](https://thehackernews.com/2023/08/chinas-apt31-suspected-in-attacks-on.html) group. Also launched using DLL side-loading, it uses an attacker-controlled GitHub profile as a [dead drop resolver](https://attack.mitre.org/techniques/T1102/001/) to store a Base64-encoded string of the actual C2 server.

CloudSorcerer, on the other hand, is a sophisticated cyber espionage tool used for stealth monitoring, data collection, and exfiltration via Microsoft Graph, Yandex Cloud, and Dropbox cloud infrastructure. Like in the case of GrewApacha, the updated variant leverages legitimate platforms like LiveJournal and Quora as an initial C2 server.

"As with previous versions of CloudSorcerer, profile biographies contain an encrypted authentication token to interact with the cloud service," Kaspersky said.

Furthermore, it utilizes an encryption-based protection mechanism that ensures the malware is detonated only on the victim's computer by using a unique key that's derived from the Windows [GetTickCount() function](https://learn.microsoft.com/en-us/windows/win32/api/sysinfoapi/nf-sysinfoapi-gettickcount) at runtime.

The third malware family observed in the attacks in PlugY, a fully-featured backdoor that connects to a management server using TCP, UDP, or named pipes, and comes with capabilities to execute shell commands, monitor device screen, log keystrokes, and capture clipboard content.

Kaspersky said a source code analysis of PlugX uncovered similarities with a known backdoor called [DRBControl](https://thehackernews.com/2022/10/chinese-hackers-targeting-online.html) (aka [Clambling](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)), which has been [attributed](https://www.securityjoes.com/post/apt27-turns-to-ransomware) to China-nexus threat clusters tracked as [APT27](https://thehackernews.com/2024/05/inside-operation-diplomatic-specter.html) and [APT41](https://thehackernews.com/2024/08/apt41-hackers-use-shadowpad-cobalt.html).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The attackers behind the EastWind campaign used popular network services as command servers - GitHub, Dropbox, Quora, as well as Russian LiveJournal and Yandex Disk," the company said.

The disclosure comes Kaspersky also detailed a watering hole attack that involves compromising a legitimate site related to gas supply in Russia to distribute a worm named CMoon that can harvest confidential and payment data, take screenshots, download additional malware, and launch distributed denial-of-service (DDoS) attacks against targets of interest.

The malware also collects files and data from various web browsers, cryptocurrency wallets, instant messaging apps, SSH clients, FTP software, video recording and streaming apps, authenticators, remote desktop tools, and VPNs.

"CMoon is a worm written in .NET, with wide functionality for data theft and remote control," it [said](https://securelist.ru/how-the-cmoon-worm-collects-data/109988/). "Immediately after installation, the executable file begins to monitor the connected USB drives. This allows you to steal files of potential interest to attackers from removable media, as well as copy a worm to them and infect other computers where the drive will be used."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on R...