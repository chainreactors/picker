---
title: Apple Patches (almost) everything again. March 2026 edition., (Wed, Mar 25th)
url: https://isc.sans.edu/diary/rss/32830
source: SANS Internet Storm Center, InfoCON: green
date: 2026-03-25
fetch_date: 2026-03-26T04:32:02.563490
---

# Apple Patches (almost) everything again. March 2026 edition., (Wed, Mar 25th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Brad Duncan](/handler_list.html#brad-duncan "Brad Duncan")

Threat Level: [green](/infocon.html)

* [previous](/diary/32826)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

# [Apple Patches (almost) everything again. March 2026 edition.](/forums/diary/Apple%2BPatches%2Balmost%2Beverything%2Bagain%2BMarch%2B2026%2Bedition/32830/)

**Published**: 2026-03-25. **Last Updated**: 2026-03-25 21:29:57 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Apple%2BPatches%2Balmost%2Beverything%2Bagain%2BMarch%2B2026%2Bedition/32830/#comments)

Apple released the next version of its operating system, patching 85 different vulnerabilities across all of them. None of the vulnerabilities are currently being exploited. The last three macOS "generations" are covered, as are the last two versions of iOS/iPadOS. For tvOS, watchOS, and visionOS, only the current version received patches. This update also includes the recently released Background Security Improvements. Some older watchOS versions received updates, but these updates do not address any security issues.

| iOS 26.4 and iPadOS 26.4 | iOS 18.7.7 and iPadOS 18.7.7 | macOS Tahoe 26.4 | macOS Sequoia 15.7.5 | macOS Sonoma 14.8.5 | tvOS 26.4 | watchOS 26.4 | visionOS 26.4 | Safari 26.4 | Xcode 26.4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **CVE-2025-43376:** A remote attacker may be able to view leaked DNS queries with Private Relay turned on.  Affects WebKit | | | | | | | | | |
|  | x |  |  |  |  |  |  |  |  |
| **CVE-2025-43534:** A user with physical access to an iOS device may be able to bypass Activation Lock.  Affects iTunes Store | | | | | | | | | |
|  | x |  |  |  |  |  |  |  |  |
| **CVE-2026-20607:** An app may be able to access protected user data.  Affects libxpc | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-20631:** A user may be able to elevate privileges.  Affects PackageKit | | | | | | | | | |
|  |  | x |  |  |  |  |  |  |  |
| **CVE-2026-20632:** An app may be able to access sensitive user data.  Affects Music | | | | | | | | | |
|  |  | x |  |  |  |  |  |  |  |
| **CVE-2026-20633:** An app may be able to access user-sensitive data.  Affects Archive Utility | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-20637:** An app may be able to cause unexpected system termination.  Affects AppleKeyStore | | | | | | | | | |
|  | x |  | x | x |  |  |  |  |  |
| **CVE-2026-20639:** Processing a maliciously crafted string may lead to heap corruption.  Affects configd | | | | | | | | | |
|  |  |  | x | x |  |  |  |  |  |
| **CVE-2026-20643:** Processing maliciously crafted web content may bypass Same Origin Policy.  Affects WebKit | | | | | | | | | |
| x | x | x |  |  |  |  | x | x |  |
| **CVE-2026-20651:** An app may be able to access sensitive user data.  Affects Messages | | | | | | | | | |
|  |  |  | x |  |  |  |  |  |  |
| **CVE-2026-20657:** Parsing a maliciously crafted file may lead to an unexpected app termination.  Affects Vision | | | | | | | | | |
|  | x |  | x | x |  |  |  |  |  |
| **CVE-2026-20660:** A remote user may be able to write arbitrary files.  Affects CFNetwork | | | | | | | | | |
|  |  |  | x |  |  |  |  |  |  |
| **CVE-2026-20665:** Processing maliciously crafted web content may prevent Content Security Policy from being enforced.  Affects WebKit | | | | | | | | | |
| x | x | x |  |  | x | x | x | x |  |
| **CVE-2026-20668:** An app may be able to access sensitive user data.  Affects Focus | | | | | | | | | |
|  | x |  | x | x |  |  |  |  |  |
| **CVE-2026-20684:** An app may bypass Gatekeeper checks.  Affects AppleScript | | | | | | | | | |
|  |  | x |  |  |  |  |  |  |  |
| **CVE-2026-20687:** An app may be able to cause unexpected system termination or write kernel memory.  Affects Kernel | | | | | | | | | |
| x | x | x | x |  | x | x |  |  |  |
| **CVE-2026-20688:** An app may be able to break out of its sandbox.  Affects Printing | | | | | | | | | |
| x |  | x | x | x |  |  | x |  |  |
| **CVE-2026-20690:** Processing an audio stream in a maliciously crafted media file may terminate the process.  Affects CoreMedia | | | | | | | | | |
| x | x | x | x | x | x | x | x |  |  |
| **CVE-2026-20691:** A maliciously crafted webpage may be able to fingerprint the user.  Affects WebKit Sandboxing | | | | | | | | | |
| x |  | x |  |  |  | x | x | x |  |
| **CVE-2026-20692:** "Hide IP Address" and "Block All Remote Content" may not apply to all mail content.  Affects Mail | | | | | | | | | |
| x |  | x | x | x |  |  |  |  |  |
| **CVE-2026-20693:** An attacker with root privileges may be able to delete protected system files.  Affects PackageKit | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-20694:** An app may be able to access user-sensitive data.  Affects MigrationKit | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-20695:** An app may be able to determine kernel memory layout.  Affects Kernel | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-20697:** An app may be able to access sensitive user data.  Affects Spotlight | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-20698:** An app may be able to cause unexpected system termination or corrupt kernel memory.  Affects Kernel | | | | | | | | | |
| x |  | x |  |  | x | x | x |  |  |
| **CVE-2026-20699:** An app may be able to access user-sensitive data.  Affects AppleMobileFileIntegrity | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-20701:** An app may be able to connect to a network share without user consent.  Affects NetAuth | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28816:** An app may be able to delete files for which it does not have permission.  Affects Notes | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28817:** A sandboxed process may be able to circumvent sandbox restrictions.  Affects Printing | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28818:** An app may be able to access sensitive user data.  Affects Spotlight | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28820:** An app may be able to access sensitive user data.  Affects StorageKit | | | | | | | | | |
|  |  | x |  |  |  |  |  |  |  |
| **CVE-2026-28821:** An app may be able to gain elevated privileges.  Affects CoreServices | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28822:** An attacker may be able to cause unexpected app termination.  Affects Audio | | | | | | | | | |
| x |  | x | x | x | x | x | x |  |  |
| **CVE-2026-28823:** An app with root privileges may be able to delete protected system files.  Affects Admin Framework | | | | | | | | | |
|  |  | x |  |  |  |  |  |  |  |
| **CVE-2026-28824:** An app may be able to access sensitive user data.  Affects AppleMobileFileIntegrity | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28825:** An app may be able to modify protected parts of the file system.  Affects SMB | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28826:** A malicious app may be able to break out of its sandbox.  Affects NSColorPanel | | | | | | | | | |
|  |  | x |  |  |  |  |  |  |  |
| **CVE-2026-28827:** An app may be able to break out of its sandbox.  Affects NetFSFramework | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28828:** An app may be able to access sensitive user data.  Affects TCC | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28829:** An app may be able to modify protected parts of the file system.  Affects WebDAV | ...