---
title: Transparent Tribe Deploys New Rust Backdoor Using Private GitHub Repositories for C2
url: https://thehackernews.com/2026/09/transparent-tribe-deploys-new-rust.html
source: The Hacker News
date: 2026-09-18
fetch_date: 2026-09-19T07:02:43.297152
---

# Transparent Tribe Deploys New Rust Backdoor Using Private GitHub Repositories for C2

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

# [Transparent Tribe Deploys New Rust Backdoor Using Private GitHub Repositories for C2](https://thehackernews.com/2026/09/transparent-tribe-deploys-new-rust.html)

**Ravie Lakshmanan**Sep 18, 2026Malware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhBM0nXgCLpwEyXmAdxLO_GatYww1Cem0yuGGqhmMwCB5N8w-TeoMm7jV4SbH4hjfYmxctUjyPiSlR3Caj2cSu7L_1nxTzg5xtfJrxhq5y0elL7yh8J2S5lakpnTbck3XhMVB1iG3obibSh64E8z877YcECkeJBs_rrZARXefKDeYQJ9Nf2u8pnxD0gEnx/s1700-nu-rw-lo-l85-e365/rust-malware.jpg)

The Pakistan-aligned threat group tracked as Transparent Tribe (aka APT36 and Earth Karkaddan) has been attributed to a fresh set of cyber attacks targeting government and defense entities in India and Afghanistan.

The attacks, per Zscaler ThreatLabz, involve the use of previously undocumented tools called RUSTYSHADE, RUSTYMOVE, PSNATCH, and BASHNATCH. The activity has been codenamed **Operation RapidRust**.

"APT36 has maintained a high operational tempo and updated their tactics, techniques, and procedures (TTPs) in continued attacks targeting government and defense organizations in India and Afghanistan," [Sudeep Singh](https://sudeepvision.com/), senior manager of APT Research at Zscaler ThreatLabz, [said](https://www.zscaler.com/blogs/security-research/operation-rapidrust-apt36-deploys-rustyshade-rustymove-psnatch-and) in a technical report published this week.

The discovery comes a little over a month after Acronis Threat Research Unit (TRU) [tied](https://thehackernews.com/2026/08/new-patchcord-backdoor-targets-afghan.html) the long-running persistent threat group to another campaign aimed at Afghan telecom providers and South Asian critical infrastructure organizations using a backdoor called PATCHCORD.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

A notable aspect of the campaign is the threat actor's use of private GitHub repositories for command-and-control (C2) and the registration of typosquatted domains impersonating popular Indian news organizations like The Print and India Today to host malicious PowerShell scripts and payloads -

* theprints[.]org, which mimics The Print ("theprint[.]in")
* indiatodays[.]org, which mimics India Today ("indiatoday[.]in")

Among the four newly identified malware families, one is a backdoor, another is a lateral movement utility, while the remaining two are file-stealing programs designed for Windows and Linux systems.

RUSTYSHADE, as the name implies, is a Rust-based backdoor that makes use of attacker-controlled private GitHub repositories for encrypted C2 communications. It shares some level of functionality overlap with [GITSHELLPAD](https://thehackernews.com/2026/01/experts-detect-pakistan-linked-cyber.html), a Golang implant that was observed in September 2025 in connection with a campaign known as Gopher Strike.

Specifically, the malware parses and writes certain files in the private GitHub repository for bidirectional communication using the GitHub REST API. The names of the files are below -

* command.txt, for storing encrypted C2 commands
* results.txt, for storing encrypted command output
* info.txt, to store system reconnaissance data
* heartbeat.txt, for keepalive beaconing to confirm active infection
* screenshot.png, for encrypted desktop screenshot
* webcam\_photo.jpg, for encrypted webcam capture
* download.bin, for encrypted exfiltrated file contents

The commands allow RUSTYSHADE to take screenshots, capture a webcam photo, perform file operations, and run commands in the background.

As part of post-compromise activity, the threat actor has been observed fetching a file stealer from an attacker-controlled GitHub gist that comes in two variants for targeting both Windows and Linux environments -

* PSNATCH, a PowerShell stealer that recursively scans preconfigured directories for Microsoft Office documents, images, archives, media, executables, scripts, and databases that were modified within the last three months and exfiltrates them to a private repository named after the infected machine. The file collection is limited to 1 GB per file and 5 GB per execution.
* BASHNATCH, a bash script similar to PSNATCH that targets Linux systems

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/enterprise-ai-security-a)

Perhaps the most interesting of the lot is RUSTYMOVE, a lightweight 64-bit Windows USB propagation tool developed in Rust. Its main responsibility is to continuously monitor for external removable media using a PowerShell script and copy two pre-staged malicious files to the root directory of each detected external drive -

* DriverInstaller.zip, which contains RUSTYSHADE
* DocScanner-11-Aug-2026-5-37pm.pdf.LNK, which is suspected to contain a command to execute RUSTYSHADE after extraction

Post-compromise activity from APT36 operators involves system, user, and network reconnaissance, followed by the deployment of next-stage payloads. A significant portion of the actions took place between August 20 and September 1, 2026, with the C2 commands issued only between 4 a.m. and 11 a.m. UTC and only on weekdays.

"This campaign demonstrates that APT36 continues to target government and defense entities in India and Afghanistan while maintaining high operational tempo and evolving TTPs," Singh said.

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
[**Share on Reddit](#link_share)
[**S...