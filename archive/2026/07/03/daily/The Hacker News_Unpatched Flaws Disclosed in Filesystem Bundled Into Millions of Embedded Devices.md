---
title: Unpatched Flaws Disclosed in Filesystem Bundled Into Millions of Embedded Devices
url: https://thehackernews.com/2026/07/unpatched-flaws-disclosed-in-filesystem.html
source: The Hacker News
date: 2026-07-03
fetch_date: 2026-07-04T05:49:52.083320
---

# Unpatched Flaws Disclosed in Filesystem Bundled Into Millions of Embedded Devices

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Unpatched Flaws Disclosed in Filesystem Bundled Into Millions of Embedded Devices](https://thehackernews.com/2026/07/unpatched-flaws-disclosed-in-filesystem.html)

**Swati Khandelwal**Jul 03, 2026Vulnerability / IoT Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJGo3ti2B3O-v3XpxdiFLMhvMVB_Ee5mmTlis-Qls6K8auWLQtPb4DSLL4snqvuZSxEvYXbGVBiUvRH1wBiw53ovRi-KTpdb0WqPwkZMkA_eHTSkTQVPkexu02-I2u7wc7PKESGKFZxlKRjR1SAkgOK50kIfpqZ9wcEjZCYBWIh6u_L82tXa8WfgUIhmA/s1700-e365/fatfs.jpg)

Security firm runZero has disclosed seven vulnerabilities in [FatFs](https://elm-chan.org/fsw/ff/), a small filesystem library that lets a device read and write the FAT and exFAT formats used on USB drives and SD cards.

The flaws matter because FatFs is nearly everywhere. It ships inside the firmware that runs security cameras, drones, industrial controllers, hardware crypto wallets, and other devices built on real-time operating systems.

On the worst-affected systems, an attacker who gets a booby-trapped USB drive, SD card, or update file onto a device can corrupt its memory and run their own code.

Many embedded devices lack the memory protections found on phones and desktops, which is why runZero [says](https://www.runzero.com/blog/fatfs-bugs/) "any physical access leads to a jailbreak." A public kiosk, a camera with an SD slot, an ATM, or a voting machine with a USB port should not hand over full control after a moment of physical access, but here it can.

All seven bugs work the same basic way. The device tries to read a storage volume or firmware image that has been deliberately malformed, and FatFs mishandles the bad data. runZero rated the set CVSS Medium to High, with no Criticals.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The headline bug is [CVE-2026-6682](https://www.cve.org/CVERecord?id=CVE-2026-6682) (CVSS 7.6), an integer overflow in the code that mounts a FAT32 volume. Bad math can produce a false file size, which later code treats as a real read length. On real hardware, that can become memory corruption and code execution.

Here are all seven, worst first by runZero's ranking:

* **CVE-2026-6682 (7.6, High):** FAT32 mount integer overflow leading to memory corruption and possible code execution. Reachable through some firmware updates, not just physical media.
* **CVE-2026-6687 (7.6, High):** an exFAT volume-label field overflows a small buffer, giving an attacker a clean memory-corruption foothold.
* **CVE-2026-6688 (7.6, High):** long filenames overflow the wrapper code many projects put around FatFs, such as a strcpy of fno.fname into a fixed buffer. Hard to fix inside FatFs alone.
* **CVE-2026-6685 (6.1, Medium):** a math wrap in cache handling on fragmented volumes that can silently corrupt data.
* **CVE-2026-6683 (4.6, Medium):** an exFAT divide-by-zero that crashes the device. In an update flow, it can brick hardware. Also reachable through some firmware updates.
* **CVE-2026-6686 (4.6, Medium):** a file extended past its end can leak leftover data from previously deleted files.
* **CVE-2026-6684 (4.6, Medium):** a malformed GPT partition table (the disk's map) can hang the device during mount. It is the only one of the seven fixed upstream, in FatFs R0.16.

Here is the hard part. FatFs is maintained by one developer in a small corner of the internet, and runZero says it tried repeatedly to reach the maintainer and looped in Japan's JPCERT/CC coordination center, with no response.

By runZero's account, there is no upstream fix for the memory-corruption bugs, no security mailing list, and no way for the many products that bundle FatFs to learn they are affected. Updating helps with the GPT hang, since the current release blocks it, but the rest fall to downstream vendors to patch on their own.

runZero names affected platforms, including Espressif ESP-IDF, STMicroelectronics STM32Cube, Zephyr, MicroPython, ArduPilot, RT-Thread, Mbed, Samsung TizenRT, and the SWUpdate updater. That pushes the problem downstream into consumer IoT, industrial gear, drones, and crypto wallets.

As of runZero's July 1 disclosure, no attacks using these bugs had been reported, and none have surfaced since. But the exploit material is already public: runZero shipped proof-of-concept disk images, a test harness, and a working QEMU-based exploit example in a [companion repository](https://github.com/runZeroInc/vulns-2026-fatfs-chance).

If you build firmware that touches FAT or exFAT media, the advice is direct. Find the copy of FatFs in your product, audit the wrapper code around it, look hard at how you handle filenames and file sizes, and plan to patch.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhr7HGzx4ULDSqwnN820pPGxlPxqqVxKgIrI5II1iWdspOL6yHZsdB5lWoXU3LmhIU4dtnph89fLZ0CxrQSs-ufs6Mo4eD-d-Cpx-DsV1G15eC-phLACF7hyaKSIH1zIdj3AuD7lHSHnVelmKVMoVV-_zvtJuodsSIDKu6uSRfU6fZBkO-2PERqKSfIn6dA/s728-e100/sygnia-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

If you run affected devices, treat physical ports and update channels as an attack surface: limit who can plug in media, and watch for vendor firmware updates.

## Why this keeps happening

runZero first audited FatFs by hand in 2017 and found little worth reporting. Returning in March 2026, the team pointed an off-the-shelf setup at the same code: Visual Studio Code, GitHub Copilot in "auto" mode, and a few plain prompts.

The LLM built a fuzzer, a tool that feeds malformed data into code until something breaks. That surfaced bugs the manual audit had missed and helped confirm they were exploitable.

That fits a growing pattern. In late 2024, Google's Big Sleep agent [found a real, exploitable memory bug in SQLite](https://thehackernews.com/2024/11/googles-ai-tool-big-sleep-finds-zero.html) that ordinary fuzzing had missed.

Just last month, an autonomous AI agent [surfaced 21 memory-safety bugs in FFmpeg](https://thehackernew...