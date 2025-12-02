---
title: Tomiris Shifts to Public-Service Implants for Stealthier C2 in Attacks on Government Targets
url: https://thehackernews.com/2025/12/tomiris-shifts-to-public-service.html
source: The Hacker News
date: 2025-12-01
fetch_date: 2025-12-02T03:19:08.850462
---

# Tomiris Shifts to Public-Service Implants for Stealthier C2 in Attacks on Government Targets

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Tomiris Shifts to Public-Service Implants for Stealthier C2 in Attacks on Government Targets](https://thehackernews.com/2025/12/tomiris-shifts-to-public-service.html)

**Dec 01, 2025**Ravie LakshmananMalware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0Lxoj-jT0lWvAbKZzQ_8tBsiD8CE76EWRKAfG_TID9mVbmf8BoJx5N1fR3ztKD6Yb3B8bRlGyMEArCKaW939VXvJT1G-z2iIxJrjkl_0NBONbMDU3NL8L_vqDzJQWMRIehlO-GiASFU0hTzfxL7_uKhObMFcFHfwv8lRxgFKqNXk-a04Z5gj-Wxvo_nbM/s790-rw-e365/cyberattacks.jpg)

The threat actor known as **[Tomiris](https://thehackernews.com/2023/04/russian-hackers-tomiris-targeting.html)** has been attributed to attacks targeting foreign ministries, intergovernmental organizations, and government entities in Russia with an aim to establish remote access and deploy additional tools.

"These attacks highlight a notable shift in Tomiris's tactics, namely the increased use of implants that leverage public services (e.g., Telegram and Discord) as command-and-control (C2) servers," Kaspersky researchers Oleg Kupreev and Artem Ushkov [said](https://securelist.com/tomiris-new-tools/118143/) in an analysis. "This approach likely aims to blend malicious traffic with legitimate service activity to evade detection by security tools."

The cybersecurity company said more than 50% of the spear-phishing emails and decoy files used in the campaign used Russian names and contained Russian text, indicating that Russian-speaking users or entities were the primary focus. The spear-phishing emails have also targeted Turkmenistan, Kyrgyzstan, Tajikistan, and Uzbekistan using tailored content written in their respective national languages.

The attacks aimed at high-value political and diplomatic infrastructure have leveraged a combination of reverse shells, custom implants, and open-source C2 frameworks like Havoc and AdaptixC2 to facilitate post-exploitation.

Details of Tomiris [first emerged](https://thehackernews.com/2021/09/new-tomiris-backdoor-found-linked-to.html) in September 2021 when Kaspersky shed light on the inner workings of a backdoor of the same name, pinpointing its links with SUNSHUTTLE (aka GoldMax), a malware used by the Russian APT29 hackers behind the SolarWinds supply chain attack, and Kazuar, a .NET-based espionage backdoor used by Turla.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/rat-d)

Despite these overlaps, Tomiris is assessed to be a different threat actor that mainly focuses on intelligence gathering in Central Asia. Microsoft, in a report [published](https://thehackernews.com/2024/12/russia-linked-turla-exploits-pakistani.html) in December 2024, connected the Tomiris backdoor to a Kazakhstan-based threat actor it tracks as Storm-0473.

Subsequent reports from [Cisco Talos](https://thehackernews.com/2023/10/yorotrooper-researchers-warn-of.html), [Seqrite Labs](https://thehackernews.com/2025/02/silent-lynx-using-powershell-golang-and.html), [Group-IB](https://thehackernews.com/2025/08/shadowsilk-hits-36-government-targets.html), and [BI.ZONE](https://thehackernews.com/2025/10/new-cavalry-werewolf-attack-hits.html) have strengthened this hypothesis, with the analyses identifying overlaps with clusters referred to as Cavalry Werewolf, ShadowSilk, [Silent Lynx](https://thehackernews.com/2025/11/threatsday-bulletin-ai-tools-in-malware.html#silent-lynx-exploits-diplomacy-themes-to-breach-targets), SturgeonPhisher, and YoroTrooper.

The latest activity documented by Kaspersky begins with phishing emails containing malicious password-protected RAR files. The password to open the archive is included in the text of the email. Present within the file is an executable masquerading as a Microsoft Word document (\*.doc.exe) that, when launched, drops a C/C++ reverse shell that's responsible for gathering system information and contacting a C2 server to fetch AdaptixC2.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipvK5_v8U_avbvqmUtneSEDcW61oSspZv_cjpl0wbUxTr2qzcnxUkzeFVwBjw_ZrNyrIy_2LotARiYiTZnwNxaUCm6G2Li0NPTtOKNaj-c1O2a5Cw10ADUkHkZbbHZ8fMBun7shFgJT0pkNOOecJ9RvXbyrVzZMVyRw1qiMmuXlFzvE3TyiEisdwHT_3Xr/s790-rw-e365/tom.jpg)

The reverse shell also makes Windows Registry modifications to ensure persistence for the downloaded payload. Three different versions of the malware have been detected this year alone.

Alternatively, the RAR archives propagated via the emails have been found to deliver other malware families, which, in turn, trigger their own infection sequences -

* A Rust-based downloader that collects system information and sends it to a Discord webhook; creates Visual Basic Script (VBScript) and PowerShell script files; and launches the VBScript using cscript, which runs the PowerShell script to fetch a ZIP file containing an executable associated with Havoc.
* A Python-based reverse shell that uses Discord as C2 to receive commands, execute them, and exfiltrate the results back to the server; conducts reconnaissance; and downloads next-stage implants, including AdaptixC2 and a Python-based FileGrabber that harvests files matching jpg, .png, .pdf, .txt, .docx, and .doc. extensions.
* A Python-based backdoor dubbed Distopia that's based on the open-source [dystopia-c2](https://github.com/3ct0s/dystopia-c2) project and uses Discord as C2 to execute console commands and download additional payloads, including a Python-based reverse shell that uses Telegram for C2 to run commands on the host and send the output back to the server.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-insights-d)

Tomiris' malware arsenal also comprises a number of reverse shells and implants written in different programming languages -

* A C# reverse shell that employs Telegram to receive commands
* A Rust-based malware named JLORAT that can run commands and take screenshots
* A Rust-based reverse shell that uses PowerShell as the shell rather than "cmd.exe"
* A Go-based reverse shell that establish...