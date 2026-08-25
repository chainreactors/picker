---
title: Operation QUICSILVER Targets Myanmar Government and IT with QUICAgent Backdoor
url: https://thehackernews.com/2026/08/operation-quicsilver-targets-myanmar.html
source: The Hacker News
date: 2026-08-24
fetch_date: 2026-08-25T03:00:41.317695
---

# Operation QUICSILVER Targets Myanmar Government and IT with QUICAgent Backdoor

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

# [Operation QUICSILVER Targets Myanmar Government and IT with QUICAgent Backdoor](https://thehackernews.com/2026/08/operation-quicsilver-targets-myanmar.html)

**Ravie Lakshmanan**Aug 24, 2026Cyber Espionage / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhAU29lFKKhJ4-37mroz3wn9p8YejZSqMG70AcTu4Z_FLB6hhof-kGO8-6KOfJcE5TXPvrziWpqDpLu_Mi64u8ilPMtdicwexovYdtmVQhhFOTlAeEamKEccbGQf4Y15ufNQRggwtyzLJy32qocItBHu4FX7FLYDYbnjBXuYMtflnNB4ttrzIdynMPcquxs/s1700-e365/silver.jpg)

Cybersecurity researchers have flagged a cyber espionage campaign targeting Myanmar that uses graduation ceremony invitation lures to deliver a Go backdoor called QUICAgent.

The campaign, codenamed **[Operation QUICSILVER](https://www.seqrite.com/blog/operation-quicsilver-china-nexus-actor-targets-myanmar-diplomats-via-vhd-delivered-go-backdoor/)**, has been found to target government and information technology sectors, per Seqrite Labs. The activity is assessed to be the work of a China-nexus threat actor with moderate confidence.

It was first observed in April 2026, when the attack was observed delivering a file named "HolidayNotice.pdf.exe" along with a lure that was a fabricated Belgian–Myanmar public holiday calendar. Two subsequent artifacts, each detected in June and July 2026, make use of a Virtual Hard Disk (VHD) file that activates the infection chain.

Present within the VHD file is a Windows Shortcut (LNK) that mimics a PDF document. Opening the document displays a decoy PDF to the victim, an official graduation ceremony invitation that's written in Burmese and purports to be from the Information Technology and Cyber Security Department (ITCSD), which operates under Myanmar's Ministry of Transport and Communications.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The "announcement" serves as a distraction while the shortcut file stealthily launches "ftp.exe," a legitimate Microsoft-signed Windows binary, and abuses its "-s" option to run commands stored in a local script file.

"While the decoy is presented on the victim's screen, the script searches for two document files, header.doc and body.doc, stored inside the hidden \_rels directory," security researchers Priya Patel and Kartik Jivani said. "It then combines these two files using the native Windows copy /b command to reconstruct the next-stage payload."

The payload is a Golang-based implant dubbed QUICAgent that performs sandbox evasion techniques before connecting to a command-and-control (C2) server. Specifically, it incorporates a random delay of 100-600 milliseconds and executes 1,000 iterations of SHA-256 hashing operations to exhaust automated sandbox execution time limits.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJS0-Sem-0d5mmYgY-QmpxlorRSZUtS5jR5uCWA2XkuRE7uRWOE7RTurJ-6kiFx3Oy_zrCfLPjSKkAsejCNRQeJ5AKm33Sqv7Iekwi6kZOjNXF7nxkiJIVZhyST4KWKTHe3tb9Briw6qOUS2vvmtLAAcDj6TJgZY6jVApmEMpKvWYvKsSbrgCz9umJIa58/s1700-e365/seq.jpg)

The backend C2 server address is retrieved dynamically by sending an HTTP GET request to two Cloudflare Workers domains. Once the C2 address is obtained ("104.64.211[.]22"), it suffixes port 443 to the domain and constructs the final destination. The malware uses QUIC over UDP port 443 to communicate with the C2 server.

The initial beacon to the server also includes basic information about the compromised host. The beacon is transmitted every five seconds, with each infected machine assigned a unique X-Agent-ID to identify the victim. QUICAgent is fairly basic in that it supports five commands to execute commands, transfer files, browse directories, and modify the beacon interval.

Persistence is achieved by setting up an LNK file in the current user's Windows Startup folder so that it's automatically executed the next time the user logs in to the system.

"The campaign uses a multi-stage infection chain that begins with a malicious LNK file, abuses ftp.exe as a LOLBAS to execute the next stage, reconstructs the payload from two fake document files, and finally deploys a custom Go-based backdoor that we have named QUICAgent," the Indian cybersecurity company said.

The disclosure comes as the China-linked Mustang Panda actor has been observed using an updated version of a known backdoor called [COOLCLIENT](https://thehackernews.com/2026/01/mustang-panda-deploys-updated.html) that can deploy a signed kernel-mode driver ("Msagent.sys"), similar to the kernel-mode enhancements identified in [TONESHELL](https://thehackernews.com/2025/12/mustang-panda-uses-signed-kernel-driver.html). The backdoor is assessed to be deployed via PlugX using DLL sideloading, a technique extensively abused by the hacking group.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

COOLCLIENT supports such a wide array of capabilities as keylogging, clipboard theft, credential harvesting, file management, system reconnaissance, and plugin-based extensions. It was first detected in the wild in 2022.

"The driver enhances the malware's stealth by hiding the COOLCLIENT process, protecting related files and registry entries, and preventing them from being inspected or modified," Kaspersky [said](https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/), adding it detected the updated variant and its accompanying driver in intrusions across Myanmar, Mongolia, Pakistan, and Russia.

"While the overall execution flow remains consistent with previously documented COOLCLIENT variants, this sample introduces a previously undocumented kernel-mode driver that significantly expands the malware's stealth capabilities."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/...