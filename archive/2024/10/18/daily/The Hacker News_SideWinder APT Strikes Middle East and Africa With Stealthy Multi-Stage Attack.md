---
title: SideWinder APT Strikes Middle East and Africa With Stealthy Multi-Stage Attack
url: https://thehackernews.com/2024/10/sidewinder-apt-strikes-middle-east-and.html
source: The Hacker News
date: 2024-10-18
fetch_date: 2025-10-06T18:57:56.951861
---

# SideWinder APT Strikes Middle East and Africa With Stealthy Multi-Stage Attack

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

# [SideWinder APT Strikes Middle East and Africa With Stealthy Multi-Stage Attack](https://thehackernews.com/2024/10/sidewinder-apt-strikes-middle-east-and.html)

**Oct 17, 2024**Ravie LakshmananMalware / Cyber Espionage

[![Multi-Stage Attack](data:image/png;base64... "Multi-Stage Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjH8YrO9GkMl8Phskru9hKt9GP36m5JiUEC4pkLq3pL-LdfFiEtijYNwj5tZOTL1vlyqw2l8VGqqP8XGtUKMbooJ4bQi-2BwbL5PtHsT7pdO0y69L1F055DMZYyty6-9g03GbX1CHQ8Fbuu7AmH3gKr_pHDQWYeuAINkI_bugBFPwP2JodO7wrkn8Lb63zQ/s790-rw-e365/hackers.png)

An advanced persistent threat (APT) actor with suspected ties to India has sprung forth with a flurry of attacks against high-profile entities and strategic infrastructures in the Middle East and Africa.

The activity has been attributed to a group tracked as [SideWinder](https://thehackernews.com/2024/07/new-sidewinder-cyber-attacks-target.html), which is also known as APT-C-17, Baby Elephant, Hardcore Nationalist, Leafperforator, Rattlesnake, Razor Tiger, and T-APT-04.

"The group may be perceived as a low-skilled actor due to the use of public exploits, malicious LNK files and scripts as infection vectors, and the use of public RATs, but their true capabilities only become apparent when you carefully examine the details of their operations," Kaspersky researchers Giampaolo Dedola and Vasily Berdnikov [said](https://securelist.com/sidewinder-apt/114089/).

Targets of the attacks include government and military entities, logistics, infrastructure and telecommunications companies, financial institutions, universities, and oil trading companies located in Bangladesh, Djibouti, Jordan, Malaysia, the Maldives, Myanmar, Nepal, Pakistan, Saudi Arabia, Sri Lanka, Turkey, and the U.A.E.

SideWinder has also been observed setting its sights on diplomatic entities in Afghanistan, France, China, India, Indonesia, and Morocco.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The most significant aspect of the recent campaign is the use of a multi-stage infection chain to deliver a previously unknown post-exploitation toolkit called StealerBot.

It all commences with a spear-phishing email with an attachment – either a ZIP archive containing a Windows shortcut (LNK) file or a Microsoft Office document – that, in turn, executes a series of intermediate JavaScript and .NET downloaders to ultimately deploy the StealerBot malware.

The documents rely on the tried-and-tested technique of remote template injection to download an RTF file that is stored on an adversary-controlled remote server. The RTF file, for its part, triggers an exploit for [CVE-2017-11882](https://thehackernews.com/2023/12/hackers-exploiting-old-ms-excel.html), to execute JavaScript code that's responsible for running additional JavaScript code hosted on mofa-gov-sa.direct888[.]net.

On the other hand, the LNK file employs the [mshta.exe](https://redcanary.com/threat-detection-report/techniques/mshta/) utility, a Windows-native binary designed to execute Microsoft HTML Application (HTA) files, to run the same JavaScript code hosted on a malicious website controlled by the attacker.

The JavaScript malware serves to extract an embedded Base64-encoded string, a .NET library named "App.dll" that collects system information and functions as a downloader for a second .NET payload from a server ("ModuleInstaller.dll").

ModuleInstaller is also a downloader, but one that's equipped to maintain persistence on the host, execute a backdoor loader module, and retrieve next-stage components. But in an interesting twist, the manner in which they are run is determined by what endpoint security solution is installed on the host.

"The Backdoor loader module has been observed since 2020," the researchers said, pointing out its ability to evade detection and avoid running in sandboxed environments. "It has remained almost the same over the years."

[![Multi-Stage Attack](data:image/png;base64... "Multi-Stage Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwZxtdR8upaXr-4x-NRgWFYdMMG3Su9gcUYG7nKdl57XP0Ne7irvYlPyOxmGJSMh44JgwLtWViLywDb671ccg-6Y5WkiHCUfcPi5Totdk05gKsLZXVyJiG84fVCXUnKttlUl9K4LyKDx3ZufbU-vs9xasNmnR2Btx4xxH6QVQ1Kppa-uwErRfyz6DIKglj/s790-rw-e365/SideWinder.png)

"It was recently updated by the attacker, but the main difference is that old variants are configured to load the encrypted file using a specific filename embedded in the program, and the latest variants were designed to enumerate all the files in the current directory and load those without an extension."

The end goal of the attacks is to drop StealerBot via the Backdoor loader module. Described as a .NET-based "advanced modular implant," it is specifically geared to facilitate espionage activities by fetching several plugins to -

* Install additional malware using a C++ downloader
* Capture screenshots
* Log keystrokes
* Steal passwords from browsers
* Intercept RDP credentials
* Steal files
* Start reverse shell
* Phish Windows credentials, and
* Escalate privileges bypassing User Account Control (UAC)

"The implant consists of different modules loaded by the main 'Orchestrator,' which is responsible for communicating with the [command-and-control] and executing and managing the plugins," the researchers said. "The Orchestrator is usually loaded by the backdoor loader module."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Kaspersky said it detected two installer components – named InstallerPayload and InstallerPayload\_NET – that don't feature as part of the attack chain, but are used to install StealerBot to likely update to a new version or infect another user.

The expansion of SideWinder's geographic reach and its use of a new sophisticated toolkit comes as cybersecurity company Cyfirma detailed new infrastructure running the [Mythic post-exploitation framework](https://securelist.com/loki-agent-for-mythic/113596/) and linked to [Transparen...