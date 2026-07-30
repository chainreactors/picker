---
title: Apple Patches Everything (July 2026), (Wed, Jul 29th)
url: https://isc.sans.edu/diary/rss/33196
source: SANS Internet Storm Center, InfoCON: green
date: 2026-07-29
fetch_date: 2026-07-30T04:52:27.252318
---

# Apple Patches Everything (July 2026), (Wed, Jul 29th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/33192)
* [next](/diary/33198)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Apple Patches Everything (July 2026)](/forums/diary/Apple%2BPatches%2BEverything%2BJuly%2B2026/33196/)

**Published**: 2026-07-29. **Last Updated**: 2026-07-29 07:32:37 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Apple%2BPatches%2BEverything%2BJuly%2B2026/33196/#comments)

I am a bit late with this summary, but this week Apple released updates to all its operating systems and Safari. The Safari update, as usual, targets macOS prior to macOS 26. macOS updates covered the two older versions (14 and 15), while other operating system patches only covered the current 26 versions.

A total of 187 vulnerabilities are addressed in this update. Many cover multiple operating systems. Apple did not label any of the vulnerabilities as already being exploited.

Three vulnerabilities that caught my interest are CVE-2026-28849, CVE-2026-28900, and CVE-2026-28914. These issues appear to be the vulnerability described in https://mysk.blog/2026/07/23/macos-overwrite-app-executables/ earlier this week. But I have not seen a confirmation that this is the same issue.

Other than that, the vulnerabilities are "more of the usual". A lot of DoS and privilege-escalation/sandbox-escape issues, and the usual WebKit issues. In June, Apple announced that it may publish occasional "security update only" releases. This release does not contain any significant new functionality but is also meant as a "prep release" for iOS/macOS 27, as it makes some adjustments to Spotlight to get the system ready for the new major OS releases coming in the fall.

| iOS 26.6 and iPadOS 26.6 | macOS Tahoe 26.6 | macOS Sequoia 15.7.8 | macOS Sonoma 14.8.8 | tvOS 26.6 | watchOS 26.6 | visionOS 26.6 | Safari 26.6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **CVE-2025-43325:** An app may be able to access sensitive user data.  Affects Icons | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-20672:** An app may be able to access sensitive user data.  Affects LaunchServices | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-23918:** A remote attacker may be able to cause a denial-of-service.  Affects apache | | | | | | | |
|  | x | x | x |  |  |  |  |
| **CVE-2026-28849:** A maliciously crafted ZIP archive may bypass Gatekeeper checks.  Affects BOM | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-28896:** An attacker may be able to cause unexpected system termination or read kernel memory.  Affects ppp | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-28900:** A maliciously crafted ZIP archive may bypass Gatekeeper checks.  Affects libarchive | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-28911:** A malicious app may be able to corrupt memory of a system process.  Affects Metal | | | | | | | |
|  | x |  | x |  |  |  |  |
| **CVE-2026-28912:** A user may be able to elevate privileges.  Affects PackageKit | | | | | | | |
|  | x | x |  |  |  |  |  |
| **CVE-2026-28914:** A maliciously crafted ZIP archive may bypass Gatekeeper checks.  Affects zip | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-28926:** An app may be able to elevate privileges.  Affects Disk Images | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-28928:** An app may be able to cause unexpected system termination.  Affects Apple Neural Engine | | | | | | | |
| x | x |  |  | x | x |  |  |
| **CVE-2026-28931:** Connecting to a malicious NFS server may lead to kernel memory corruption.  Affects Kernel | | | | | | | |
| x | x |  |  | x | x |  |  |
| **CVE-2026-28932:** An app may be able to cause a denial of service.  Affects xar | | | | | | | |
|  | x | x | x |  |  |  |  |
| **CVE-2026-28936:** Processing a maliciously crafted file may lead to unexpected app termination.  Affects CoreServices | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-28945:** An app may be able to bypass network restrictions.  Affects Disk Images | | | | | | | |
|  | x | x | x |  |  |  |  |
| **CVE-2026-28961:** An attacker with physical access to a locked device may be able to view sensitive user information.  Affects Network Extensions | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-28973:** A malicious app may be able to break out of its sandbox.  Affects libc | | | | | | | |
| x | x | x | x |  | x |  |  |
| **CVE-2026-28981:** Processing a maliciously crafted image may lead to arbitrary code execution.  Affects HFS | | | | | | | |
|  | x | x | x |  |  |  |  |
| **CVE-2026-28982:** A remote user may be able to cause unexpected system termination or corrupt kernel memory.  Affects Kernel | | | | | | | |
|  | x | x | x |  |  |  |  |
| **CVE-2026-28983:** A remote attacker may be able to cause a denial of service.  Affects LaunchServices | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-39868:** An app may be able to cause unexpected system termination or corrupt kernel memory.  Affects Kernel | | | | | | | |
|  |  | x | x | x | x | x |  |
| **CVE-2026-39873:** Connecting to a malicious SMB server may lead to unexpected system termination.  Affects SMB | | | | | | | |
|  | x | x | x |  |  |  |  |
| **CVE-2026-39874:** A malicious app may be able to gain root privileges.  Affects Remote Management | | | | | | | |
|  | x | x | x |  |  |  |  |
| **CVE-2026-39875:** A malicious app may be able to gain root privileges.  Affects CUPS | | | | | | | |
|  | x | x | x |  |  |  |  |
| **CVE-2026-39877:** An app may be able to disclose kernel memory.  Affects IOSkywalkFamily | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-43661:** Processing a maliciously crafted image may corrupt process memory.  Affects ImageIO | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-43665:** A local attacker may be able to determine the legacy VNC password configured for Screen Sharing.  Affects Screen Sharing Server | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-43672:** A malicious application may be able to bypass Privacy preferences.  Affects Assets | | | | | | | |
|  | x | x | x |  |  |  |  |
| **CVE-2026-43673:** Processing a maliciously crafted audio file may corrupt process memory.  Affects CoreAudio | | | | | | | |
| x | x | x | x | x | x | x |  |
| **CVE-2026-43676:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebKit | | | | | | | |
|  |  |  |  |  | x | x |  |
| **CVE-2026-43681:** A local user may be able to read kernel memory.  Affects AppleRAID | | | | | | | |
|  | x | x | x |  |  |  |  |
| **CVE-2026-43682:** A remote user may be able to cause unexpected system termination or corrupt kernel memory.  Affects HFS | | | | | | | |
|  | x | x | x |  |  |  |  |
| **CVE-2026-43693:** An app may be able to gain root privileges.  Affects Core Services | | | | | | | |
|  | x | x | x |  |  |  |  |
| **CVE-2026-43694:** An app may be able to cause unexpected system termination or write kernel memory.  Affects quarantine | | | | | | | |
|  | x | x | x |  |  |  |  |
| **CVE-2026-43698:** An app may be able to gain root privileges.  Affects CUPS | | | | | | | |
|  | x | x | x |  |  |  |  |
| **CVE-2026-43699:** Processing maliciously crafted web content may lead to an unexpected process crash.  Affects WebKit | | | | | | | |
|  |  |  |  | x | x | x |  |
| **CVE-2026-43700:** Processing maliciously crafted web content may disclose sensitive user information.  Affects WebKit | | | | | | | |
|  |  |  |  | x | x | x |  |
| **CVE-2026-43701:** A malicious website may be able to process restricted web content outside the sandbox.  Affects WebKit | | | | | | | |
|  |  |  |  | x | x | x |  |
| **CVE-2026-437...