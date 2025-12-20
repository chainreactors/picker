---
title: New UEFI Flaw Enables Early-Boot DMA Attacks on ASRock, ASUS, GIGABYTE, MSI Motherboards
url: https://thehackernews.com/2025/12/new-uefi-flaw-enables-early-boot-dma.html
source: The Hacker News
date: 2025-12-19
fetch_date: 2025-12-20T03:15:37.370025
---

# New UEFI Flaw Enables Early-Boot DMA Attacks on ASRock, ASUS, GIGABYTE, MSI Motherboards

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

# [New UEFI Flaw Enables Early-Boot DMA Attacks on ASRock, ASUS, GIGABYTE, MSI Motherboards](https://thehackernews.com/2025/12/new-uefi-flaw-enables-early-boot-dma.html)

**Dec 19, 2025**Ravie LakshmananFirmware Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMb3AWaGGzuDhZZM0WBk_eEwbCg8zBxsM7-vESRDoizM7NngGTmZZuGjnl_ig_GzqAlVZVJF5r4bJH-1B7zQwrjKnSZuTPW0xsebT3dj_ygVTpS3aFfEwBKVh01Y7H-rJB-3netyZjaGV3vZ5Mg3Sh34mIMMD6NoowEsci4GrcDEeYIus7XPCu58Z_gZ9T/s790-rw-e365/motherboard.jpg)

Certain motherboard models from vendors like ASRock, ASUSTeK Computer, GIGABYTE, and MSI are affected by a security vulnerability that leaves them susceptible to early-boot direct memory access ([DMA](https://learn.microsoft.com/en-us/windows/security/hardware-security/kernel-dma-protection-for-thunderbolt)) attacks across architectures that implement a Unified Extensible Firmware Interface ([UEFI](https://uefi.org/home)) and input–output memory management unit ([IOMMU](https://en.wikipedia.org/wiki/Input%E2%80%93output_memory_management_unit)).

UEFI and IOMMU are designed to enforce a security foundation and prevent peripherals from performing unauthorized memory accesses, effectively ensuring that DMA-capable devices can manipulate or inspect system memory before the operating system is loaded.

The vulnerability, discovered by Nick Peterson and Mohamed Al-Sharifi of Riot Games in certain UEFI implementations, has to do with a discrepancy in the DMA protection status. While the firmware indicates that DMA protection is active, it fails to configure and enable the IOMMU during the critical boot phase.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/rat-d)

"This gap allows a malicious DMA-capable Peripheral Component Interconnect Express (PCIe) device with physical access to read or modify system memory before operating system-level safeguards are established," the CERT Coordination Center (CERT/CC) [said](https://kb.cert.org/vuls/id/382314) in an advisory.

"As a result, attackers could potentially access sensitive data in memory or influence the initial state of the system, thus undermining the integrity of the boot process."

Successful exploitation of the vulnerability could allow a physically present attacker to enable pre-boot code injection on affected systems running unpatched firmware and access or alter system memory via DMA transactions, much before the operating system kernel and its security features are loaded.

The vulnerabilities that enable a bypass of early-boot memory protection are listed below -

* **[CVE-2025-14304](https://www.cve.org/CVERecord?id=CVE-2025-14304)** (CVSS score: 7.0) - A protection mechanism failure vulnerability affecting ASRock, ASRock Rack, and ASRock Industrial motherboards using Intel 500, 600, 700, and 800 series chipsets
* **[CVE-2025-11901](https://www.cve.org/CVERecord?id=CVE-2025-11901)** (CVSS score: 7.0) - A protection mechanism failure vulnerability affecting ASUS motherboards using Intel Z490, W480, B460, H410, Z590, B560, H510, Z690, B660, W680, Z790, B760, and W790 series chipsets
* **[CVE-2025-14302](https://www.cve.org/CVERecord?id=CVE-2025-14302)** (CVSS score: 7.0) - A protection mechanism failure vulnerability affecting GIGABYTE motherboards using Intel Z890, W880, Q870, B860, H810, Z790, B760, Z690, Q670, B660, H610, W790 series chipsets, and AMD X870E, X870, B850, B840, X670, B650, A620, A620A, and TRX50 series chipsets (Fix for TRX50 planned for Q1 2026)
* **[CVE-2025-14303](https://www.cve.org/CVERecord?id=CVE-2025-14303)** (CVSS score: 7.0) - A protection mechanism failure vulnerability affecting MSI motherboards using Intel 600 and 700 series chipsets

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

With impacted vendors releasing firmware updates to correct the IOMMU initialization sequence and enforce DMA protections throughout the boot process, it's essential that end users and administrators apply them as soon as they are available to stay protected against the threat.

"In environments where physical access cannot be fully controlled or relied on, prompt patching and adherence to hardware security best practices are especially important," CERT/CC said. "Because the IOMMU also plays a foundational role in isolation and trust delegation in virtualized and cloud environments, this flaw highlights the importance of ensuring correct firmware configuration even on systems not typically used in data centers."

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
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[CERT/CC](https://thehackernews.com/search/label/CERT/CC)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Direct Memory Access](https://thehackernews.com/search/label/Direct%20Memory%20Access)[Firmware Security](https://thehackernews.com/search/label/Firmware%20Security)[hardware security](https://thehackernews.com/search/label/hardware%20security)[Motherboard](https://thehackernews.com/search/label/Motherboard)[UEFI](https://thehackernews.com/search/label/UEFI)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![Android Malware FvncBot, SeedSnatcher, and ClayRat Gain Stron...