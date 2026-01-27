---
title: Konni Hackers Deploy AI-Generated PowerShell Backdoor Against Blockchain Developers
url: https://thehackernews.com/2026/01/konni-hackers-deploy-ai-generated.html
source: The Hacker News
date: 2026-01-26
fetch_date: 2026-01-27T03:39:24.721909
---

# Konni Hackers Deploy AI-Generated PowerShell Backdoor Against Blockchain Developers

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

# [Konni Hackers Deploy AI-Generated PowerShell Backdoor Against Blockchain Developers](https://thehackernews.com/2026/01/konni-hackers-deploy-ai-generated.html)

**Ravie Lakshmanan**Jan 26, 2026Malware / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZjxGlZLamF04EJ6k6LroD__iJijKDR-um0kxbhfPls3rVFqj3SNIZweWeNb_S0WqzDo5EwSfg6iTiVddPJJg48dQKaUkw2RYxMeYVC-NcfGDxMbGHR79_V6nSAawHyjJgDrTlEtRFheK3q6sDqJIgZwvGDYtaKf-KintMeOaelZyqgjl_0-qNSNO4gS6W/s1700-e365/hackers-ps.jpg)

The North Korean threat actor known as **Konni** has been observed using PowerShell malware generated using artificial intelligence (AI) tools to target developers and engineering teams in the blockchain sector.

The phishing campaign has targeted Japan, Australia, and India, highlighting the adversary's expansion of the targeting scope beyond [South Korea](https://thehackernews.com/2022/01/north-korean-hackers-return-with.html), [Russia](https://thehackernews.com/2023/11/konni-group-using-russian-language.html), [Ukraine](https://thehackernews.com/2025/05/north-korean-konni-apt-targets-ukraine.html), and [European nations](https://thehackernews.com/2022/07/north-korean-hackers-using-malicious.html), Check Point Research [said](https://research.checkpoint.com/2026/konni-targets-developers-with-ai-malware/) in a technical report published last week.

Active since at least 2014, Konni is primarily known for its targeting of organizations and individuals in South Korea. It's also tracked as Earth Imp, Opal Sleet, Osmium, TA406, and Vedalia.

In November 2025, the Genians Security Center (GSC) [detailed](https://thehackernews.com/2025/11/konni-hackers-turn-googles-find-hub.html) the hacking group's targeting of Android devices by exploiting Google's asset tracking service, Find Hub, to remotely reset victim devices and erase personal data from them, signaling a new escalation of their tradecraft.

As recently as this month, Konni has been observed distributing spear-phishing emails containing malicious links that are disguised as harmless advertising URLs associated with Google and Naver's advertising platforms to bypass security filters and deliver a remote access trojan codenamed EndRAT.

The campaign has been codenamed Operation Poseidon by the GSC, with the attacks impersonating North Korean human rights organizations and financial institutions in South Korea. The attacks are also characterized by the use of improperly secured WordPress websites to distribute malware and for command-and-control (C2) infrastructure.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

The email messages have been found to masquerade as financial notices, such as transaction confirmations or wire transfer requests, to trick recipients into downloading ZIP archives hosted on WordPress sites. The ZIP file comes with a Windows shortcut (LNK) that's designed to execute an AutoIt script disguised as a PDF document. The AutoIt script is a known Konni malware called EndRAT (aka EndClient RAT).

"This attack is analyzed as a case that effectively bypassed email security filtering and user vigilance through a spear-phishing attack vector that exploited the ad click redirection mechanism used within the Google advertising ecosystem," the South Korean security outfit [said](https://www.genians.co.kr/en/blog/threat_intelligence/spear-phishing).

"It was confirmed that the attacker utilized the redirection URL structure of a domain used for legitimate ad click tracking (ad.doubleclick[.]net) to incrementally direct users to external infrastructure where actual malicious files were hosted."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhnz1C9aJNeXEv7nEO1O0USi0vRt-wWYELBO30HykMrCqRYmIKDsBzaaP-mSBnth56QH7LYsISEKiObkNq4oKxEjE91k9VubJRDk_sD-oA-uXNRIl3_anw5zl9CcfDF1tpd_4nFfXds559pMuJvj3Y2XYkHDZLuvUXuj9fhW16qRvxdC9El7sq_ErYku3Oi/s1700-e365/cp.jpg)

The latest campaign documented by Check Point leverages ZIP files mimicking project requirements-themed documents and hosted on Discord's content delivery network (CDN) to unleash a multi-stage attack chain that performs the following sequence of actions. The exact initial access vector used in the attacks is unknown.

* The ZIP archive contains a PDF decoy and an LNK file
* The shortcut file launches an embedded PowerShell loader which extracts two additional files, a Microsoft Word lure document and a CAB archive, and displays as the Word document as a distraction mechanism
* The shortcut file extracts the contents of the CAB archive, which contains a PowerShell Backdoor, two batch scripts, and an executable used for User Account Control (UAC) bypass
* The first batch script is used to prepare the environment, establish persistence using a scheduled task, stage the backdoor and execute it, following which it deletes itself from disk to reduce forensic visibility
* The PowerShell backdoor carries out a string of anti-analysis and sandbox-evasion checks, and then proceeds to profile the system and attempts to elevate privileges using the [FodHelper UAC bypass](https://thehackernews.com/2023/08/new-nodestealer-targeting-facebook.html) technique
* The backdoor performs cleanup of the previously dropped UAC bypass executable, configures Microsoft Defender exclusion for "C:\ProgramData," and runs the second batch script to replace the previously created scheduled task with a new one that's capable of running with elevated privileges
* The backdoor proceeds to drop SimpleHelp, a legitimate Remote Monitoring and Management (RMM) tool for persistent remote access, and communicates with a C2 server that's safeguarded by an encryption gate intended to block non-browser traffic to periodically send host metadata and execute PowerShell code returned by the server

The cybersecurity company said there are indications that the PowerShell backdoor was created with the assistance of an AI tool, citing its modular structure, human-readable documentation, and the presence of source code comments like "# <– your permanent project UUID."

"Instead of focusing on individual end-users, the campaign goal seems to be to establish a foothold in development environments, where compromise can provide broader downstream access across multiple projects and services," Check Point said. "The introduct...