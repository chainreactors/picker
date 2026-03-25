---
title: Hackers Use Fake Resumes to Steal Enterprise Credentials and Deploy Crypto Miner
url: https://thehackernews.com/2026/03/hackers-use-fake-resumes-to-steal.html
source: The Hacker News
date: 2026-03-24
fetch_date: 2026-03-25T04:18:08.974066
---

# Hackers Use Fake Resumes to Steal Enterprise Credentials and Deploy Crypto Miner

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [Hackers Use Fake Resumes to Steal Enterprise Credentials and Deploy Crypto Miner](https://thehackernews.com/2026/03/hackers-use-fake-resumes-to-steal.html)

**Ravie Lakshmanan**Mar 24, 2026Malware / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbL1vWsuHhVXpRJ6YeAB7bUhrZmz7Ba3LRQ7MsrXsIVCXfxCMUs4nedbI26D5FpMqQ0uL6APhIlu12GJdDMWZ9AbGiz7qu5gUinMjsmh6yxiuqZvUzSrzj7Iy-Ax4UoCl1BZAGb6kRE_XPaTbmKHK6zTvsRWWeNcrhh4toMR5Fi2o4et0H938i6UPN1r8M/s1700-e365/malware-resume.jpg)

An ongoing phishing campaign is targeting French-speaking corporate environments with fake resumes that lead to the deployment of cryptocurrency miners and information stealers.

"The campaign uses highly obfuscated VBScript files disguised as resume/CV documents, delivered through phishing emails," Securonix researchers Shikha Sangwan, Akshay Gaikwad, and Aaron Beardslee [said](https://www.securonix.com/blog/faux-elevate-threat-actors-crypto-miners-and-infostealers/) in a report shared with The Hacker News.

"Once executed, the malware deploys a multi-purpose toolkit that combines credential theft, data exfiltration, and Monero cryptocurrency mining for maximum monetization."

The activity has been codenamed **FAUX#ELEVATE** by the cybersecurity company. The campaign is noteworthy for the abuse of legitimate services and infrastructure, such as Dropbox for staging payloads, Moroccan WordPress sites for hosting command-and-control (C2) configuration, and mail[.]ru SMTP infrastructure for exfiltrating stolen browser credentials and desktop files.

This is an example of a living-off-the-land-style attack that raises the bar on how attackers can trick defense mechanisms and sneak their way into the target's system without attracting much attention.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

The initial dropper file is a Visual Basic Script (VBScript) that, upon opening, displays a bogus French-language error message, fooling message recipients into thinking that the file is corrupted. However, what happens behind the scenes is that the heavily obfuscated script runs a series of checks to evade sandboxes and enters into a persistent User Account Control (UAC) loop that prompts users to run it with administrator privileges.

Notably, out of the script's 224,471 lines, only 266 lines contain actual executable code. The rest of the script is filled with junk comments featuring random English sentences, inflating the size of the file to 9.7MB.

"The malware also uses a domain-join gate using [WMI](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page) [Windows Management Instrumentation], ensuring that payloads are only delivered on enterprise machines, and standalone home systems are excluded entirely," the researchers said.

As soon as the dropper obtains administrative privileges, it wastes no time disabling security controls and covering up its tracks by configuring Microsoft Defender exclusion paths for all primary drive letters (from C to I), disabling UAC via a Windows Registry change, and deleting itself.

The dropper is also responsible for fetching two separate password-protected 7-Zip archives hosted on Dropbox -

* gmail2.7z, which contains various executables to steal data and mine cryptocurrency
* gmail\_ma.7z, which contains utilities for persistence and cleanup

Among the tools used to facilitate credential theft is a component that leverages the [ChromElevator](https://thehackernews.com/2025/10/stealit-malware-abuses-nodejs-single.html) project to extract sensitive data from Chromium-based browsers by getting around app-bound encryption ([ABE](https://thehackernews.com/2024/08/google-chrome-adds-app-bound-encryption.html)) protections. Some of the other tools include -

* mozilla.vbs, a VBScript malware for stealing Mozilla Firefox profile and credentials
* walls.vbs, a VBScript payload for desktop file exfiltration
* mservice.exe, an XMRig cryptocurrency miner that's launched after retrieving the mining configuration from a compromised Moroccan WordPress site
* WinRing0x64.sys, a legitimate Windows kernel driver that's used to unlock the CPU's full mining potential
* RuntimeHost.exe, a persistent Trojan component that modifies Windows Firewall rules and periodically communicates with a C2 server

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ciso-risk-comm-cert-dr-d)

The sole browser data is exfiltrated using two separate mail[.]ru sender accounts ("olga.aitsaid@mail.ru" and "3pw5nd9neeyn@mail.ru") that share the same password over SMTP to another email address operated by the threat actor ("vladimirprolitovitch@duck.com").

Once credential theft and exfiltration activities are complete, the attack chain initiates an aggressive cleanup of all dropped tools in a bid to minimize forensic footprint, leaving behind only the miner and trojan artifacts./p>

"The FAUX#ELEVATE campaign demonstrates a well-organized, multi-stage attack operation that combines several noteworthy techniques into a single infection chain," Securonix said.

"What makes this campaign particularly dangerous for enterprise security teams is the speed of execution, the full infection chain completes in approximately 25 seconds from initial VBS execution to credential exfiltration, and the selective targeting of domain-joined machines, which ensures that every compromised host provides maximum value through corporate credential theft and persistent resource hijacking."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_sh...