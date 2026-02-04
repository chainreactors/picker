---
title: Notepad++ Hosting Breach Attributed to China-Linked Lotus Blossom Hacking Group
url: https://thehackernews.com/2026/02/notepad-hosting-breach-attributed-to.html
source: The Hacker News
date: 2026-02-03
fetch_date: 2026-02-04T04:08:17.982202
---

# Notepad++ Hosting Breach Attributed to China-Linked Lotus Blossom Hacking Group

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

# [Notepad++ Hosting Breach Attributed to China-Linked Lotus Blossom Hacking Group](https://thehackernews.com/2026/02/notepad-hosting-breach-attributed-to.html)

**Ravie Lakshmanan**Feb 03, 2026Malware / Open Source

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzMhF4Q5Le-vJfovBcsvDHI-V4XTT-ZlCDveT5a3ibTH_5_USxu3yKbxTyY86_7HfbI0Lfcvl9zXpIWost8jehkxJ83EEkTpJNxySNjlntsGoxQtgJompW0iNQdpylvHAc5GkY-7L8X4iebatDHQUhMYFspiAKemuy_iPqtjz3NCwLXzIRC4xFOeiq6Ea5/s1700-e365/notepad.jpg)

A China-linked threat actor known as **[Lotus Blossom](https://thehackernews.com/2025/03/chinese-apt-lotus-panda-targets.html)** has been attributed with medium confidence to the recently discovered compromise of the infrastructure hosting Notepad++.

The attack enabled the state-sponsored hacking group to deliver a previously undocumented backdoor codenamed **Chrysalis** to users of the open-source editor, according to [new findings](https://www.rapid7.com/blog/post/tr-chrysalis-backdoor-dive-into-lotus-blossoms-toolkit/) from Rapid7.

The development comes shortly after Notepad++ maintainer Don Ho [said](https://thehackernews.com/2026/02/notepad-official-update-mechanism.html) that a compromise at the hosting provider level allowed threat actors to hijack update traffic starting June 2025 and selectively redirect such requests from certain users to malicious servers to serve a tampered update by exploiting insufficient update verification controls that existed in older versions of the utility.

The weakness was plugged in December 2025 with the release of version 8.8.9. It has since emerged that the hosting provider for the software was breached to perform targeted traffic redirections until December 2, 2025, when the attacker's access was terminated. Notepad++ has since migrated to a new hosting provider with stronger security and rotated all credentials.

Rapid7's analysis of the incident has uncovered no evidence or artifacts to suggest that the site's plugin or updater-related mechanisms were exploited to distribute malware.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

"The only confirmed behavior is that execution of 'notepad++.exe' and subsequently 'GUP.exe' preceded the execution of a suspicious process 'update.exe' which was downloaded from 95.179.213.0," security researcher Ivan Feigl said.

"Update.exe" is a Nullsoft Scriptable Install System (NSIS) installer that contains multiple files -

* An NSIS installation script
* BluetoothService.exe, a renamed version of Bitdefender Submission Wizard that's used for DLL side-loading (a technique widely used by Chinese hacking groups)
* BluetoothService, encrypted shellcode (aka Chrysalis)
* log.dll, a malicious DLL that's sideloaded to decrypt and execute the shellcode

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPFDC1u4uG7GBbZnUfAO_wuRYBmWiATszeCrZCdOtqwbWjBVYK0ASltl1fKxznz8Dzy1_ohyAlnd-zCWgVqYd0tl7kbsSxvhvmdvaM8nCN8B6guSeuQ3xAVWk0Y8KjYYpVa7kA97uKggUGbfKK_c4AAMP3Qr2Zr9S8Rwd-cB68CsCQ_4sYz-LiDuaKJpxF/s1700-e365/dll.jpg)

Chrysalis is a bespoke, feature-rich implant that gathers system information and contacts an external server ("api.skycloudcenter[.]com") to likely receive additional commands for execution on the infected host.

The command-and-control (C2) server is currently offline. However, a deeper examination of the obfuscated artifact has revealed that it's capable of processing incoming HTTP responses to spawn an interactive shell, create processes, perform file operations, upload/download files, and uninstall itself.

"Overall, the sample looks like something that has been actively developed over time," Rapid7 said, adding it also identified a file named "conf.c" that's designed to retrieve a Cobalt Strike beacon by means of a custom loader that embeds [Metasploit block API](https://github.com/rapid7/metasploit-framework/blob/master/external/source/shellcode/windows/x86/src/block/block_api.asm) shellcode.

One such loader, "ConsoleApplication2.exe" is noteworthy for its use of [Microsoft Warbird](https://websec.net/blog/a-deep-dive-into-microsoft-warbird-mss-kernel-mode-dynamic-packer-68ee2c87b251081f55ec8c31), an undocumented internal code protection and obfuscation framework, to execute shellcode. The threat actor has been found to copy and modify an already existing proof-of-concept (PoC) [published](https://cirosec.de/en/news/abusing-microsoft-warbird-for-shellcode-execution/) by German cybersecurity company Cirosec in September 2024.

Rapid7's attribution of Chrysalis to Lotus Blossom (aka Billbug, Bronze Elgin, Lotus Panda, Raspberry Typhoon, Spring Dragon, and Thrip) based on similarities with prior campaigns undertaken by the threat actor, including one [documented](https://thehackernews.com/2025/04/lotus-panda-hacks-se-asian-governments.html) by Broadcom-owned Symantec in April 2025 that involved the use of legitimate executables from Trend Micro and Bitdefender to sideload malicious DLLs.

"While the group continues to rely on proven techniques like DLL side-loading and service persistence, their multi-layered shellcode loader and integration of undocumented system calls (NtQuerySystemInformation) mark a clear shift toward more resilient and stealth tradecraft," the company said.

"What stands out is the mix of tools: the deployment of custom malware (Chrysalis) alongside commodity frameworks like Metasploit and Cobalt Strike, together with the rapid adaptation of public research (specifically the abuse of Microsoft Warbird). This demonstrates that Billbug is actively updating its playbook to stay ahead of modern detection."

## Kaspersky Observes 3 Infection Chains

Kaspersky, in its own breakdown of the Notepad++ incident, said it observed three different infection chains that were designed to target about a dozen machines belonging to individuals located in Vietnam, El Salvador, and Australia, a government organization located in the Philippines, a financi...