---
title: Apple Patches Everything, (Mon, May 11th)
url: https://isc.sans.edu/diary/rss/32976
source: SANS Internet Storm Center, InfoCON: green
date: 2026-05-11
fetch_date: 2026-05-12T05:39:16.961957
---

# Apple Patches Everything, (Mon, May 11th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32974)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Apple Patches Everything](/forums/diary/Apple%2BPatches%2BEverything/32976/)

**Published**: 2026-05-11. **Last Updated**: 2026-05-11 22:19:13 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Apple%2BPatches%2BEverything/32976/#comments)

Apple today released its typical feature update across it's operating systems (iOS, iPadOS, macOS, tvOS, watchOS, vision OS). With this update, Apple patched 84 different vulnerabilities. Updates are available for the "26" series of operating systems, as well as for the previous "18" version of iOS/iPadOS, and two versions back for macOS (version 14 and 15).

None of the vulnerabilities has been exploited. The number of addressed vulnerabilities is about average compared to similar Apple updates.

![](https://isc.sans.edu/diaryimages/images/Screenshot%202026-05-11%20at%203_17_51%E2%80%AFPM.png)

Figure: Number of Vulnerabilities patched for each security update. Last one in red at the end.

| iOS 26.5 and iPadOS 26.5 | iOS 18.7.9 and iPadOS 18.7.9 | macOS Tahoe 26.5 | macOS Sequoia 15.7.7 | macOS Sonoma 14.8.7 | tvOS 26.5 | watchOS 26.5 | visionOS 26.5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **CVE-2025-43524:** An app may be able to break out of its sandbox.  Affects Icons | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2026-28819:** An app may be able to execute arbitrary code with kernel privileges.  Affects Wi-Fi | | | | | | | |
|  | x | x | x | x |  |  |  |
| **CVE-2026-28840:** An app may be able to gain root privileges.  Affects PackageKit | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2026-28846:** A remote attacker may be able to cause unexpected app termination.  Affects SceneKit | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-28848:** A remote attacker may be able to cause unexpected system termination.  Affects SMB | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-28870:** An app may be able to access sensitive user data.  Affects GeoServices | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2026-28872:** A remote attacker may be able to cause a denial-of-service.  Affects Calendar | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2026-28873:** An app may be able to circumvent App Privacy Report logging.  Affects Privacy | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2026-28877:** An app may be able to access sensitive user data.  Affects Accounts | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2026-28878:** An app may be able to enumerate a user's installed apps.  Affects Crash Reporter | | | | | | | |
|  |  |  | x |  |  |  |  |
| **CVE-2026-28882:** An app may be able to enumerate a user's installed apps.  Affects libxpc | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2026-28883:** Processing maliciously crafted web content may lead to an unexpected process crash.  Affects WebKit | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-28894:** A remote attacker may be able to cause a denial-of-service.  Affects Calling Framework | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2026-28897:** A local user may be able to cause unexpected system termination or read kernel memory.  Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-28901:** Processing maliciously crafted web content may lead to an unexpected process crash.  Affects WebKit | | | | | | | |
|  |  |  |  |  |  |  | x |
| **CVE-2026-28906:** An attacker may be able to track users through their IP address.  Affects Networking | | | | | | | |
| x | x | x | x | x |  |  | x |
| **CVE-2026-28907:** Processing maliciously crafted web content may prevent Content Security Policy from being enforced.  Affects WebKit | | | | | | | |
| x | x | x |  |  | x | x | x |
| **CVE-2026-28908:** An app may be able to modify protected parts of the file system.  Affects Kernel | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-28913:** Processing maliciously crafted web content may lead to an unexpected process crash.  Affects WebKit | | | | | | | |
| x |  | x |  |  | x | x |  |
| **CVE-2026-28914:** A maliciously crafted ZIP archive may bypass Gatekeeper checks.  Affects zip | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-28915:** An app may be able to gain root privileges.  Affects CUPS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-28917:** Processing maliciously crafted web content may lead to an unexpected process crash.  Affects WebKit | | | | | | | |
| x | x | x |  |  | x | x | x |
| **CVE-2026-28918:** Parsing a maliciously crafted file may lead to an unexpected app termination.  Affects CoreSymbolication | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-28919:** An app may be able to gain root privileges.  Affects StorageKit | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-28920:** Visiting a maliciously crafted website may leak sensitive data.  Affects zlib | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-28922:** An app may be able to access private information.  Affects CoreMedia | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-28923:** A malicious app may be able to break out of its sandbox.  Affects GPU Drivers | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-28924:** An app may be able to access Contacts without user consent.  Affects Sync Services | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-28925:** An app may be able to cause unexpected system termination or write kernel memory.  Affects HFS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-28929:** Replying to an email could display remote images in Mail in Lockdown Mode.  Affects Mail Drafts | | | | | | | |
|  | x | x | x | x |  |  |  |
| **CVE-2026-28930:** An app may be able to access protected user data.  Affects Spotlight | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-28936:** Processing a maliciously crafted file may lead to unexpected app termination.  Affects CoreServices | | | | | | | |
| x | x | x |  | x |  |  | x |
| **CVE-2026-28940:** Processing a maliciously crafted image may corrupt process memory.  Affects Model I/O | | | | | | | |
| x | x | x | x |  | x |  | x |
| **CVE-2026-28941:** Processing a maliciously crafted file may lead to a denial-of-service or potentially disclose memory contents.  Affects Model I/O | | | | | | | |
|  | x | x | x |  |  |  |  |
| **CVE-2026-28942:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebKit | | | | | | | |
| x |  | x |  |  | x | x |  |
| **CVE-2026-28943:** An app may be able to determine kernel memory layout.  Affects IOHIDFamily | | | | | | | |
| x | x | x | x | x | x | x |  |
| **CVE-2026-28944:** Processing maliciously crafted web content may lead to an unexpected process crash.  Affects WebRTC | | | | | | | |
| x |  | x |  |  |  |  | x |
| **CVE-2026-28947:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebKit | | | | | | | |
|  |  |  |  |  |  |  | x |
| **CVE-2026-28951:** An app may be able to gain root privileges.  Affects Kernel | | | | | | | |
| x | x | x | x | x |  |  |  |
| **CVE-2026-28952:** An app may be able to cause unexpected system termination.  Affects Kernel | | | | | | | |
|  | x | x | x | x |  |  |  |
| **CVE-2026-28953:** Processing maliciously crafted web content may lead to an unexpected process crash.  Affects WebKit | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2026-28954:** A maliciously crafted disk image may bypass Gatekeeper checks.  Affects Kernel | | | | | | | |
|  | x | x | x | x |  |  | ...