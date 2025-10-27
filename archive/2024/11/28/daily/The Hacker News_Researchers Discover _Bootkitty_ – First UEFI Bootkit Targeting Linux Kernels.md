---
title: Researchers Discover "Bootkitty" – First UEFI Bootkit Targeting Linux Kernels
url: https://thehackernews.com/2024/11/researchers-discover-bootkitty-first.html
source: The Hacker News
date: 2024-11-28
fetch_date: 2025-10-06T19:29:41.866748
---

# Researchers Discover "Bootkitty" – First UEFI Bootkit Targeting Linux Kernels

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

# [Researchers Discover "Bootkitty" – First UEFI Bootkit Targeting Linux Kernels](https://thehackernews.com/2024/11/researchers-discover-bootkitty-first.html)

**Nov 27, 2024**Ravie LakshmananLinux / Malware

[![UEFI Linux Bootkit](data:image/png;base64... "UEFI Linux Bootkit")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRd8EW3eHnsJX_aK9I-EQd8dIMobvH58H_5thb3hgzIjfJ-dolAAIbyhgGwUuLiILyES0LJZag8oKn8HK3UVX67O1d2V40U4CnwzPyJgK3dSfA6AqgsybZoCJS1LiAEEDKJeNmcg2xgBRgx_ycjD2PRvA7kMSo-ndVQ31tqA2EhrhCF1vZ6GH-d47mL7G-/s790-rw-e365/linux.png)

Cybersecurity researchers have shed light on what has been described as the first Unified Extensible Firmware Interface (UEFI) [bootkit](https://thehackernews.com/2023/06/nsa-releases-guide-to-combat-powerful.html) designed for Linux systems.

Dubbed **Bootkitty** by its creators who go by the name BlackCat, the [bootkit](https://www.sentinelone.com/cybersecurity-101/cybersecurity/bootkit/) is assessed to be a proof-of-concept (PoC) and there is no evidence that it has been put to use in real-world attacks. Also tracked as [IranuKit](https://humzak711.github.io/analyzing_IranuKit), it was [uploaded](https://www.virustotal.com/gui/file/f1f84819bdf395d42c36adb36ded0e7de338e2036e174716b5de71abc56f5d40) to the VirusTotal platform on November 5, 2024.

"The bootkit's main goal is to disable the kernel's signature verification feature and to preload two as yet unknown ELF binaries via the Linux init process (which is the first process executed by the Linux kernel during system startup)," ESET researchers Martin Smolár and Peter Strýček [said](https://www.welivesecurity.com/en/eset-research/bootkitty-analyzing-first-uefi-bootkit-linux/).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The development is significant as it heralds a shift in the cyber threat landscape where UEFI bootkits are no longer confined to [Windows systems alone](https://techcommunity.microsoft.com/blog/windows-itpro-blog/revoking-vulnerable-windows-boot-managers/4121735).

It's worth noting that Bootkitty is signed by a self-signed certificate, and therefore cannot be executed on systems with UEFI Secure Boot enabled unless an attacker-controlled certificate has been already installed.

[![UEFI Linux Bootkit](data:image/png;base64... "UEFI Linux Bootkit")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrTnxztqkMC9nZq0FMm1MSuKZCj71aQcdASTgnhUm5j5X64ICdWGoosqQK-dyKaegXBv7Ab1OkEBzK9yHd6KMsyWqNjclAqMDZN2qaJtUHC2mt1OXSDk0G28h05ejZkz0zMmxkZqCJE8UStuIrt79iwrAOZj9XCQrsudMteXP9qVngTsp3Kt6jjdy4B-Kt/s790-rw-e365/attack.png)

Regardless of the UEFI Secure Boot status, the bootkit is mainly engineered to boot the Linux kernel and patch, in memory, the function's response for integrity verification before GNU GRand Unified Bootloader ([GRUB](https://en.wikipedia.org/wiki/GNU_GRUB)) is executed.

Specifically, it proceeds to hook two functions from the UEFI authentication protocols if Secure Boot is enabled in such a way that UEFI integrity checks are bypassed. Subsequently, it also patches three different functions in the legitimate GRUB boot loader to sidestep other integrity verifications.

It's also designed to interfere with the normal functioning of the Linux kernel's decompression process to allow the malware to load malicious modules. Last but not least, it modifies the [LD\_PRELOAD](https://thehackernews.com/2022/10/new-cryptojacking-campaign-targeting.html) environment variable so that two unknown ELF shared objects ("/opt/injector.so" and "/init") are loaded when the init process starts.

The Slovakian cybersecurity company said its investigation into the bootkit also led to the discovery of a likely related unsigned kernel module codenamed BCDropper that's capable of deploying an ELF binary dubbed BCObserver that loads another as-yet-unknown kernel module after a system start.

The kernel module, also featuring BlackCat as the author's name, implements other rootkit-related functionalities like hiding files, processes, and opening ports. There is no evidence to suggest a connection to the ALPHV/BlackCat ransomware group at this stage.

"Whether a proof-of-concept or not, Bootkitty marks an interesting move forward in the UEFI threat landscape, breaking the belief about modern UEFI bootkits being Windows-exclusive threats," the researchers said, adding "it emphasizes the necessity of being prepared for potential future threats."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

### Bootkitty Exploits LogoFAIL

Firmware security company Binarly, in a follow-up analysis published on November 29, 2024, revealed that the prototype UEFI bootkit capable of infecting the Linux kernel is exploiting a vulnerability tied to [LogoFAIL](https://thehackernews.com/2023/12/logofail-uefi-vulnerabilities-expose.html) ([CVE-2023-40238](https://www.insyde.com/security-pledge/SA-2023053), CVSS score: 5.5) to enable the "execution of malicious shellcode through tampered BMP files in UEFI firmware."

[![UEFI Bootkit](data:image/png;base64... "UEFI Bootkit")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiuRVuaSF1Cn7hdkPlTQ9axuU1gr5A9lyWissONrjZ0f1N6Jx_HdpoWQwVbFUe5jxyn-XzfDtHXds9YXuoZAKcZ3eS7_8vAmhj5nep8gk6mAxuDBpoc119aUagwEYmzybYwuBtCBrrFUN_ACr4S5ijIy4mmC5PqAsdYTyBsLYsJDL34M2jNEHVayJFA0aAM/s790-rw-e365/image.png)

"The exploit uses embedded shellcode within a BMP image to bypass Secure Boot protections by injecting rogue certificates into the MokList variable," it [said](https://www.binarly.io/blog/logofail-exploited-to-deploy-bootkitty-the-first-uefi-bootkit-for-linux).

"Vulnerable devices include models from Acer, HP, Fujitsu, and Lenovo, with evidence suggesting the exploit may have been tailored for specific hardware configurations. While a patch from Insyde mitigates the vulnerability, unpatched devices remain at risk."

### Bootkitty Part of Research Project

ESET has [revealed](https://x.com/ESETresearch/status/186358...