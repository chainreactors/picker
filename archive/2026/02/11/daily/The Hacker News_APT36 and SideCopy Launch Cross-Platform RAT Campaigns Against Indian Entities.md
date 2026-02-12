---
title: APT36 and SideCopy Launch Cross-Platform RAT Campaigns Against Indian Entities
url: https://thehackernews.com/2026/02/apt36-and-sidecopy-launch-cross.html
source: The Hacker News
date: 2026-02-11
fetch_date: 2026-02-12T04:23:18.393596
---

# APT36 and SideCopy Launch Cross-Platform RAT Campaigns Against Indian Entities

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [APT36 and SideCopy Launch Cross-Platform RAT Campaigns Against Indian Entities](https://thehackernews.com/2026/02/apt36-and-sidecopy-launch-cross.html)

**Ravie Lakshmanan**Feb 11, 2026Cyber Espionage / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbazpuuwU1rJbldu2fNhcDhnmgmpygU-Ci4lvjJXXo3TlmbV06oWZJ-FEJjMtQnkzg9-cBOt9h8aCA5d2EuO3gRaDlbzzc1w4cZRsdDUY1YwMTXv9f3ebp4CrZ-0jIar70HO_pyuhzHdClzTo85wpHJF8wiabXv8ko9fxQbp5WFmWdVwvtqqAkh5mk2_hv/s1700-e365/india.jpg)

Indian defense sector and government-aligned organizations have been targeted by multiple campaigns that are designed to compromise Windows and Linux environments with remote access trojans capable of stealing sensitive data and ensuring continued access to infected machines.

The campaigns are characterized by the use of malware families like [Geta RAT](https://thehackernews.com/2025/04/pakistan-linked-hackers-expand-targets.html), [Ares RAT](https://thehackernews.com/2025/07/tag-140-deploys-drat-v2-rat-targeting.html), and [DeskRAT](https://thehackernews.com/2025/10/apt36-targets-indian-government-with.html), which are often attributed to Pakistan-aligned threat clusters tracked as SideCopy and APT36 (aka Transparent Tribe). SideCopy, active since at least 2019, is assessed to operate as a subdivision of Transparent Tribe.

"Taken together, these campaigns reinforce a familiar but evolving narrative," Aditya K. Sood, vice president of Security Engineering and AI Strategy at Aryaka, [said](https://www.aryaka.com/blog/espionage-without-noise-apt36-enduring-campaigns/). "Transparent Tribe and SideCopy are not reinventing espionage – they are refining it."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

"By expanding cross-platform coverage, leaning into memory-resident techniques, and experimenting with new delivery vectors, this ecosystem continues to operate below the noise floor while maintaining strategic focus."

Common to all the campaigns is the use of phishing emails containing malicious attachments or embedded download links that lead prospective targets to attacker-controlled infrastructure. These initial access mechanisms serve as a conduit for Windows shortcuts (LNK), ELF binaries, and PowerPoint Add-In files that, when opened, launch a multi-stage process to drop the trojans.

The malware families are designed to provide persistent remote access, enable system reconnaissance, collect data, execute commands, and facilitate long-term post-compromise operations across both Windows and Linux environments.

One of the attack chains is as follows: a malicious LNK file invokes "mshta.exe" to execute an HTML Application (HTA) file hosted on compromised legitimate domains. The HTA payload contains JavaScript to decrypt an embedded DLL payload, which, in turn, processes an embedded data blob to write a decoy PDF to disk, connects to a hard-coded command-and-control (C2) server, and displays the saved decoy file.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheRJn0G58-h5eLeFY81az1SoeN0DlVv75lan2-3xrQvGEcyYQImr8lxqR0Fv4BF41I7MzUff2h79hpdC8wVtUPc9CMRwxRw9GqNXcz5s7OF3apNxWioLgWHExzKwUbsqdIvNLqj60SY-VioBAyNCIedXBWBXApsHzgOD1viry_J_1HQSuPFOE2t7PFFgXz/s1700-e365/xml.jpg)

After the lure document is displayed, the malware checks for installed security products and adapts its persistence method accordingly prior to deploying Geta RAT on the compromised host. It's worth noting this attack chain was detailed by [CYFIRMA](https://thehackernews.com/2026/01/transparent-tribe-launches-new-rat.html) and Seqrite Labs researcher [Sathwik Ram Prakki](https://x.com/PrakkiSathwik/status/2007457956636590184) in late December 2025.

Geta RAT supports various commands to collect system information, enumerate running processes, terminate a specified process, list installed apps, gather credentials, retrieve and replace clipboard contents with attacker-supplied data, capture screenshots, perform file operations, run arbitrary shell commands, and harvest data from connected USB devices.

Running parallel to this Windows-focused campaign is a Linux variant that employs a Go binary as a starting point to drop a Python-based Ares RAT by means of a shell script downloaded from an external server. Like Geta RAT, Ares RAT can also run a wide range of commands to harvest sensitive data and run Python scripts or commands issued by the threat actor.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

Aryaka said it also observed another campaign where the Golang malware, DeskRAT, is delivered via a rogue PowerPoint Add-In file that runs embedded macro to establish outbound communication with a remote server to fetch the malware. APT36's use of DeskRAT was [documented](https://thehackernews.com/2025/10/apt36-targets-indian-government-with.html) by Sekoia and QiAnXin XLab in October 2025.

"These campaigns demonstrate a well-resourced, espionage-focused threat actor deliberately targeting Indian defense, government, and strategic sectors through defense-themed lures, impersonated official documents, and regionally trusted infrastructure," the company said. "The activity extends beyond defense to policy, research, critical infrastructure, and defense-adjacent organizations operating within the same trusted ecosystem."

"The deployment of DeskRAT, alongside Geta RAT and Ares RAT, underscores an evolving toolkit optimized for stealth, persistence, and long-term access."

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

*...