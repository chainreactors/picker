---
title: 11 Old Microsoft-Signed Linux UEFI Shims Could Let Attackers Bypass Secure Boot
url: https://thehackernews.com/2026/07/11-old-microsoft-signed-linux-uefi.html
source: The Hacker News
date: 2026-07-14
fetch_date: 2026-07-15T04:49:59.698503
---

# 11 Old Microsoft-Signed Linux UEFI Shims Could Let Attackers Bypass Secure Boot

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

# [11 Old Microsoft-Signed Linux UEFI Shims Could Let Attackers Bypass Secure Boot](https://thehackernews.com/2026/07/11-old-microsoft-signed-linux-uefi.html)

**Ravie Lakshmanan**Jul 14, 2026Endpoint Security / Linux

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzgVI5ZeWhnWkl-lXmJYMLjAOXmxw21Y3sgxeF9rrOS_JqjQ7k_yyV_2KU_ELhmsm3nA3qNV0farc_31WCAhPPZRq7iIrYm90R_24lvc1f68Gv-yZPsM3bwDiUuCaCBAzq-S8ymLrrD7dx349vEjlR0eID2LXm5SO3Ocq1sG8sWkhAEG9RWX07avTOu3dW/s1700-e365/shim.gif)

Cybersecurity researchers have discovered 11 old, Microsoft-signed, Unified Extensible Firmware Interface (UEFI) applications that could be abused to bypass Secure Boot on most systems using the modern firmware standard.

"An attacker exploiting one of these vulnerable applications can execute untrusted code during system boot, enabling deployment of malicious UEFI bootkits or other malware," ESET researcher Martin Smolár [said](https://www.welivesecurity.com/en/eset-research/forgotten-uefi-shims-undermining-secure-boot/) in a report published today.

The UEFI shim bootloaders expose any UEFI-based machine that trusts Microsoft's "[Microsoft Corporation UEFI CA 2011](https://support.microsoft.com/en-US/servicing/os/secure-boot/2025/06/windows-secure-boot-certificate-expiration-and-ca-updates)" third-party UEFI certificate authority (CA) certificate, irrespective of the installed operating system. The certificate is used to sign third-party boot components intended to run under Secure Boot. It expired as of June 27, 2026, and has been replaced by Microsoft UEFI CA 2023 and Microsoft Option ROM UEFI CA 2023.

The shim is a lightweight, open-source UEFI bootloader that acts as an intermediary between a computer's motherboard firmware and the Linux operating system. Its primary purpose is to allow Linux distributions to boot when Secure Boot is enabled. It's worth noting that the shim itself is signed with a key trusted by the firmware, mostly a Microsoft signature, as its certificates come pre-installed on UEFI-based devices.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The sequence proceeds like this: the UEFI firmware loads the shim and validates its signature against the Microsoft CA stored in the firmware. The shim then validates the second-stage bootloader (in most cases, GRUB 2) against its own embedded vendor certificate. GRUB 2 finally validates the kernel using the same vendor certificate.

The Slovak cybersecurity company said the outdated-but-trusted shims can be exploited to execute arbitrary code when the system boots up, allowing bad actors to deploy UEFI bootkits like Bootkitty, HybridPetya, or BlackLotus even when Secure Boot protections are enabled.

The UEFI bootloaders of the open-source shim project, mainly from version 0.9 and earlier, have since been revoked by Microsoft as part of its [June 2026 Patch Tuesday](https://thehackernews.com/2026/06/microsoft-patches-record-206-flaws.html) update following responsible disclosure earlier this February. The list of the impacted shim bootloaders is below -

* Spyrus WTGCreator from UEFI shim loader (0.7 or lower)
* RedHat RedHat Enterprise Linux (7.2) from UEFI shim loader (0.9)
* RedHat CentOS (7.2) from UEFI shim loader (0.9)
* Baramundi software baramundi Management Suite (up to 2024R1) from UEFI shim loader (0.8)
* WhiteCanyon/Blancco WipeDrive (8.0.0 through 8.1.3) from UEFI shim loader (0.7)
* Finland's Matriculation Examination Board Abitti 1 (1.0) from UEFI shim loader (0.8)
* NTC IT ROSA, LLC ROSA Linux (R10, R9) from UEFI shim loader (0.9)
* Oracle America, Inc. OracleLinux (7.2) from UEFI shim loader (0.9)
* PC-Doctor, Inc. PC Doctor Service Center (15, 16) from UEFI shim loader (0.9)
* OpenSuse OpenSuse UEFI Shim loader (0.9)
* OpenSuse OpenSuse Shim (2.1) from UEFI Shim loader (0.9)

A consequence of this loophole is that an attacker could exploit these susceptible shim bootloaders to bypass newer security mechanisms by making use of the bring your own vulnerable driver (BYOVD) attack technique to run arbitrary code during the early boot phase, even before the operating system is initialized.

Linux systems also come with a security feature called a Machine Owner Key (MOK) allowlist that lets users authorize unsigned drivers to be loaded while UEFI Secure Boot is active. Although a MOK denylist was introduced in shim version 0.9 as a way to revoke old signing certificates associated with a vulnerable UEFI binary and re-sign patched versions.

In this context, an attacker could replace the victim's up-to-date shim with an older Microsoft-signed UEFI shim and bypass MOK denylist enforcement by taking advantage of the fact that the allowlist still trusts the old certificate. This, in turn, could allow an attacker's shim to load vulnerable binaries without restriction and obtain arbitrary code execution.

That's not all. The attack also subverts Secure Boot Advanced Targeting (SBAT), which is designed to revoke vulnerable boot components as opposed to maintaining a huge blocklist of individual cryptographic hashes corresponding to each file. Put differently, the mechanism is used to update the minimum acceptable generation whenever a vulnerability is discovered in a boot chain component. If an attempted boot uses an older, vulnerable version, the system blocks it and throws an error.

The CERT Coordination Center (CERT/CC), in an advisory issued last month, said the vendor-specific bootloaders have not been updated to address vulnerabilities in the upstream project after they became publicly known and fixed.

"As a result, vulnerable bootloaders remained signed and trusted by Secure Boot systems because they had not been revoked through the Microsoft-signed DBX revocation list," it [noted](https://www.kb.cert.org/vuls/id/616257). "This created a long-term supply chain exposure in which outdated and vulnerable boot components could still be executed on fully patched ...