---
title: Apple Patches Everything, Again, (Tue, Nov 4th)
url: https://isc.sans.edu/diary/rss/32448
source: SANS Internet Storm Center, InfoCON: green
date: 2025-11-04
fetch_date: 2025-11-05T03:12:37.978438
---

# Apple Patches Everything, Again, (Tue, Nov 4th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32444)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Apple Patches Everything, Again](/forums/diary/Apple%2BPatches%2BEverything%2BAgain/32448/)

**Published**: 2025-11-04. **Last Updated**: 2025-11-04 12:10:29 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Apple%2BPatches%2BEverything%2BAgain/32448/#comments)

Apple released its expected set of operating system upgrades. This is a minor feature upgrade that also includes fixes for 110 different vulnerabilities. As usual for Apple, many of the vulnerabilities affect multiple operating systems. None of the vulnerabilities is marked as already exploited. Apple only offers very sparse vulnerability descriptions. Here are some vulnerabilities that may be worth watching:

CVE-2025-43338, CVE-2025-43372: A memory corruption vulnerability in ImageIO. ImageIO is responsible for rendering images, and vulnerabilities like this have been exploited in the past for remote code execution. CVE-2025-43400, a vulnerability affecting FontParser, could have a similar impact.

CVE-2025-43431: A memory corruption issue in WebKit. This could be used to execute code via Safari.

| iOS 26.1 and iPadOS 26.1 | macOS Tahoe 26.1 | macOS Sequoia 15.7.2 | macOS Sonoma 14.8.2 | tvOS 26.1 | watchOS 26.1 | visionOS 26.1 | Safari 26.1 | Xcode 26.1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **CVE-2025-31199:** An app may be able to access sensitive user data.  Affects Spotlight | | | | | | | | |
|  |  |  | x |  |  |  |  |  |
| **CVE-2025-43292:** An app may be able to access sensitive user data.  Affects CoreMedia | | | | | | | | |
|  |  | x |  |  |  |  |  |  |
| **CVE-2025-43294:** An app may be able to access sensitive user data.  Affects MallocStackLogging | | | | | | | | |
| x |  |  |  | x | x |  |  |  |
| **CVE-2025-43322:** An app may be able to access user-sensitive data.  Affects Admin Framework | | | | | | | | |
|  | x | x | x |  |  |  |  |  |
| **CVE-2025-43334:** An app may be able to access user-sensitive data.  Affects sudo | | | | | | | | |
|  | x | x | x |  |  |  |  |  |
| **CVE-2025-43335:** An app may be able to access user-sensitive data.  Affects Security | | | | | | | | |
|  | x | x | x |  |  |  |  |  |
| **CVE-2025-43336:** An app with root privileges may be able to access private information.  Affects SoftwareUpdate | | | | | | | | |
|  | x | x | x |  |  |  |  |  |
| **CVE-2025-43337:** An app may be able to access sensitive user data.  Affects AppleMobileFileIntegrity | | | | | | | | |
|  |  | x |  |  |  |  |  |  |
| **CVE-2025-43338:** Processing a maliciously crafted media file may lead to unexpected app termination or corrupt process memory.  Affects ImageIO | | | | | | | | |
|  |  |  | x |  |  |  |  |  |
| **CVE-2025-43348:** An app may bypass Gatekeeper checks.  Affects Finder | | | | | | | | |
|  | x | x | x |  |  |  |  |  |
| **CVE-2025-43350:** An attacker may be able to view restricted content from the lock screen.  Affects Control Center | | | | | | | | |
| x |  |  |  |  |  |  |  |  |
| **CVE-2025-43351:** An app may be able to access protected user data.  Affects StorageKit | | | | | | | | |
|  | x |  |  |  |  |  |  |  |
| **CVE-2025-43361:** A malicious app may be able to read kernel memory.  Affects Audio | | | | | | | | |
|  |  | x | x |  |  |  |  |  |
| **CVE-2025-43364:** An app may be able to break out of its sandbox.  Affects NetFSFramework | | | | | | | | |
|  | x |  |  |  |  |  |  |  |
| **CVE-2025-43372:** Processing a maliciously crafted media file may lead to unexpected app termination or corrupt process memory.  Affects ImageIO | | | | | | | | |
|  |  |  | x |  |  |  |  |  |
| **CVE-2025-43373:** An app may be able to cause unexpected system termination or corrupt kernel memory.  Affects Wi-Fi | | | | | | | | |
|  | x | x | x |  |  |  |  |  |
| **CVE-2025-43377:** An app may be able to cause a denial-of-service.  Affects Model I/O | | | | | | | | |
|  | x | x |  |  |  |  |  |  |
| **CVE-2025-43378:** An app may be able to access sensitive user data.  Affects AppleMobileFileIntegrity | | | | | | | | |
|  | x | x |  |  |  |  |  |  |
| **CVE-2025-43379:** An app may be able to access protected user data.  Affects AppleMobileFileIntegrity | | | | | | | | |
| x | x | x | x | x | x | x |  |  |
| **CVE-2025-43380:** Parsing a file may lead to an unexpected app termination.  Affects sips | | | | | | | | |
|  | x | x | x |  |  |  |  |  |
| **CVE-2025-43381:** A malicious app may be able to delete protected user data.  Affects CoreServicesUIAgent | | | | | | | | |
|  | x |  |  |  |  |  |  |  |
| **CVE-2025-43382:** An app may be able to access sensitive user data.  Affects AppleMobileFileIntegrity | | | | | | | | |
|  | x | x | x |  |  |  |  |  |
| **CVE-2025-43383:** Processing a maliciously crafted media file may lead to unexpected app termination or corrupt process memory.  Affects Model I/O | | | | | | | | |
| x | x |  |  | x |  | x |  |  |
| **CVE-2025-43384:** Processing a maliciously crafted media file may lead to unexpected app termination or corrupt process memory.  Affects Model I/O | | | | | | | | |
|  |  | x |  |  |  |  |  |  |
| **CVE-2025-43387:** A malicious app may be able to gain root privileges.  Affects DiskArbitration | | | | | | | | |
|  | x | x |  |  |  |  |  |  |
| **CVE-2025-43389:** An app may be able to access sensitive user data.  Affects Notes | | | | | | | | |
| x | x | x | x |  |  | x |  |  |
| **CVE-2025-43390:** An app may be able to access user-sensitive data.  Affects AppleMobileFileIntegrity | | | | | | | | |
|  | x | x |  |  |  |  |  |  |
| **CVE-2025-43391:** An app may be able to access sensitive user data.  Affects Photos | | | | | | | | |
| x | x | x | x |  |  |  |  |  |
| **CVE-2025-43392:** A website may exfiltrate image data cross-origin.  Affects WebKit Canvas | | | | | | | | |
| x | x |  |  | x | x | x | x |  |
| **CVE-2025-43393:** An app may be able to break out of its sandbox.  Affects quarantine | | | | | | | | |
|  | x |  |  |  |  |  |  |  |
| **CVE-2025-43394:** An app may be able to access protected user data.  Affects bootp | | | | | | | | |
|  | x | x | x |  |  |  |  |  |
| **CVE-2025-43395:** An app may be able to access protected user data.  Affects configd | | | | | | | | |
|  | x | x | x |  |  |  |  |  |
| **CVE-2025-43396:** A sandboxed app may be able to access sensitive user data.  Affects Installer | | | | | | | | |
|  | x | x | x |  |  |  |  |  |
| **CVE-2025-43397:** An app may be able to cause a denial-of-service.  Affects SoftwareUpdate | | | | | | | | |
|  | x | x | x |  |  |  |  |  |
| **CVE-2025-43398:** An app may be able to cause unexpected system termination.  Affects Kernel | | | | | | | | |
| x | x | x | x | x | x | x |  |  |
| **CVE-2025-43399:** An app may be able to access protected user data.  Affects Siri | | | | | | | | |
|  | x | x |  |  |  |  |  |  |
| **CVE-2025-43400:** Processing a maliciously crafted font may lead to unexpected app termination or corrupt process memory.  Affects FontParser | | | | | | | | |
|  |  |  |  | x | x |  |  |  |
| **CVE-2025-43401:** A remote attacker may be able to cause a denial-of-service.  Affects CoreAnimation | | | | | | | | |
|  | x | x | x |  |  |  |  |  |
| **CVE-2025-43402:** An app may be able to cause unexpected system termination or corrupt process memory.  Affects WindowServer | | | | | | | | |
|  | x |  |  |  |  |  |  |  |
| **CVE-2025-43404:** An app may be able to access sensitive user data.  Affects Sandbox | | | | | | | | |
|  | x |  |  |...