---
title: Six New U-Boot Flaws Could Let Malicious Images Crash Devices or Run Code at Boot
url: https://thehackernews.com/2026/07/six-new-u-boot-flaws-could-let.html
source: The Hacker News
date: 2026-07-10
fetch_date: 2026-07-11T05:04:36.772219
---

# Six New U-Boot Flaws Could Let Malicious Images Crash Devices or Run Code at Boot

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

# [Six New U-Boot Flaws Could Let Malicious Images Crash Devices or Run Code at Boot](https://thehackernews.com/2026/07/six-new-u-boot-flaws-could-let.html)

**Swati Khandelwal**Jul 10, 2026Firmware Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEihuE5rUYRadx5Q2auJjv9dVeFNIP8XSwSTaH0PDwGLUA54MXlPy3AyI532a8OnhXadtWnCCH30qvUKW9C3rCOu1LPld1or5_lXwNhRVqbohHNInDzNd1f9E77Sox5yB-ir7H69LmlYRKnoqnFASOMFa2TIK2RfTThJvu_oofIXHCpiRbXGXWy-bquBWsw/s1700-e365/bootloader.gif)

Researchers at firmware security firm Binarly have found six new flaws in U-Boot, the small program that starts up hardware as varied as home routers, smart cameras, and the management chips inside data-center servers.

Four of the bugs can crash a device. The other two could let an attacker who slips a malicious image in front of the bootloader run their own code, before the device has confirmed that the software is genuine.

That last part is the point. A bootloader runs before the operating system, so a flaw here can undermine everything that loads after it. All six bugs are reached while U-Boot is still reading an untrusted image, before it has checked the signature.

## What Binarly found

U-Boot can bundle a kernel, device tree, ramdisk, and other boot components into one package, a FIT (Flattened Image Tree), and it checks that package's digital signature before handing over control.

Binarly went looking for weak spots in that check and found six. Most of the vulnerable code has been in U-Boot since v2013.07, [Binarly says](https://www.binarly.io/blog/unfit-to-boot-breaking-u-boots-fit-signature-verification), across more than 50 stable releases, and it also lives in the many vendor firmwares built on top of U-Boot.

The bugs are tracked as Binarly advisories [BRLY-2026-037 through BRLY-2026-042](https://www.binarly.io/advisories). No CVE identifiers have been assigned yet. They fall into two groups: two that could run code, and four that only crash.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The two are BRLY-2026-037 and BRLY-2026-038, and both trace to one unchecked value. U-Boot calls fdt\_get\_name, a lookup in the device-tree parsing library it borrows, and on a malformed image, that lookup returns a null pointer and a negative length. U-Boot uses both without checking either.

One bug follows the null pointer into a memory copy that, on devices where address zero is mapped, becomes a stack buffer overflow. The other feeds the negative length into pointer arithmetic that walks backward until it overwrites a saved return address. In the right memory layout, either one can hand control to code the attacker-supplied.

The other four only crash the bootloader. BRLY-2026-039 and BRLY-2026-041 read past the end of the image by trusting a size or offset that the attacker controls. BRLY-2026-040 dereferences a null pointer that an older image format hands back unchecked. BRLY-2026-042 exhausts the stack, set off by a deeply nested image that drives an early validation step to call itself until it runs out.

Binarly published a proof-of-concept image and reproduction steps for each flaw and demonstrated them against standard U-Boot builds. No exploitation in real attacks has been reported.

Of the six, the two memory-corruption bugs are the ones to prioritize: a crash can knock a device offline, but code execution at boot could subvert its entire chain of trust.

## How bad it gets

In the worst case, recovering a device that will not boot means physical access and reflashing its memory chip with a clean image. Code execution is worse. Code that runs this early sits below the operating system, where ordinary security tools may not see it.

The catch for an attacker is delivery: these bugs only bite once a malicious image reaches the boot path, which usually takes physical access or a privileged foothold. That foothold is not always local.

In [earlier work](https://thehackernews.com/2025/09/two-new-supermicro-bmc-bugs-allow.html) on Supermicro's server management controllers, the same Binarly researcher showed that an attacker with remote access to the management interface could abuse the device's own update process to flash a malicious image, without touching the hardware.

## What to do

There is no stable release with the fix yet, so vendors and maintainers of U-Boot-based products should not wait: pull the upstream fixes now, following the commit links in each Binarly advisory, and track them by advisory ID, since no CVEs exist.

U-Boot merged the six patches in June, but the July release (v2026.07) had already frozen in April, so it shipped without them; the next release, v2026.10, is not due until October.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBxLQDy7VdLze43eMmpRllTXaPKPfB_veNUxQlqIu3-68GBJtegkhDGCqtaiSymOQviROdxln1FSd4zdMp5Jv9jeF1xQxLPc9uo9H7zW2nWHNax0wT0Y8JRj-zyUfbaCLqhxSfQT2sCfhWMBPL6UVgsh5RYVNVxwus_mW_BY9Ptwz3z7iF0_LWOnte-gqg/s1600/sy-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

Everyone else runs a device someone else built on U-Boot. For them, the fix has to arrive as a firmware update from the product vendor. That is what to watch for.

This exact check has failed before. The same signature logic was hit months earlier by [CVE-2026-33243](https://github.com/u-boot/u-boot/commit/2092322b31cc8b1f8c9e2e238d1043ae0637b241), which U-Boot patched in April; the related barebox bootloader, which uses the same image tooling, was hit too.

In that bug, a property meant only to list what the signature covers was not itself signed, so a tampered image could swap in parts that were never verified. The helper behind the two worst bugs here, fdt\_get\_name, comes from libfdt, the flattened-device-tree library U-Boot shares with the Linux kernel, barebox, and others. The same unchecked-return mistake can surface anywhere that code is used.

[LogoFAIL](https://theh...