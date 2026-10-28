---
title: Apple Patches for October 2026, (Mon, Oct 26th)
url: https://isc.sans.edu/diary/rss/33458
source: SANS Internet Storm Center, InfoCON: green
date: 2026-10-27
fetch_date: 2026-10-28T07:49:39.294893
---

# Apple Patches for October 2026, (Mon, Oct 26th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Brad Duncan](/handler_list.html#brad-duncan "Brad Duncan")

Threat Level: [green](/infocon.html)

* [previous](/diary/33454)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Apple Patches for October 2026](/forums/diary/Apple%2BPatches%2Bfor%2BOctober%2B2026/33458/)

**Published**: 2026-10-26. **Last Updated**: 2026-10-27 02:09:55 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Apple%2BPatches%2Bfor%2BOctober%2B2026/33458/#comments)

Apple today released patches for 304 vulnerabilties. This number is still in line with prior Apple updates, and comes just about a month after the last apple update.

Noteworthy Issue:

CVE-2026-86950: This is an already exploited vulnerability in CoreGraphics, and was patched originally a month ago. This month's update delivers the corresponding patches for iOS 18.

No new vulnerability is marked as already exploited.

Other Interesting issues:

CVE-2026-86990: A malicious app may access the camera without user permissions.
CVE-2026-28864: A local attacker may gain access to user's Keychain items.

Apple Patch volume (number of CVEs patched) over time:

![](https://isc.sans.edu/diaryimages/images/NTZy6.png)

| iOS 27.2 and iPadOS 27.2 | iOS 26.7.2 and iPadOS 26.7.2 | iOS 18.7.11 and iPadOS 18.7.11 | macOS Golden Gate 27.2 | macOS Tahoe 26.7.2 | macOS Sequoia 15.8.2 | tvOS 27.2 | watchOS 27.2 | visionOS 27.2 | Safari 27.2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **CVE-2022-26704:** An app may be able to gain elevated privileges.  Affects Spotlight | | | | | | | | | |
| x |  |  | x |  |  |  | x | x |  |
| **CVE-2026-112410:** A remote attacker may cause an unexpected process termination.  Affects Heimdal | | | | | | | | | |
|  |  |  | x | x | x |  |  |  |  |
| **CVE-2026-112413:** Processing a maliciously crafted file may lead to unexpected app termination.  Affects Model I/O | | | | | | | | | |
| x | x |  | x | x | x |  |  | x |  |
| **CVE-2026-112414:** Processing a maliciously crafted message may lead to a denial-of-service.  Affects Mail | | | | | | | | | |
| x | x |  | x | x | x |  |  | x |  |
| **CVE-2026-112415:** An app may be able to cause unexpected system termination or corrupt process memory.  Affects AppleAVD | | | | | | | | | |
| x | x |  | x | x | x |  |  | x |  |
| **CVE-2026-112416:** Processing a maliciously crafted video file may lead to unexpected app termination.  Affects AppleAVD | | | | | | | | | |
| x | x |  | x | x | x | x |  | x |  |
| **CVE-2026-112417:** Processing a maliciously crafted 3D model may lead to memory corruption.  Affects RealityKit | | | | | | | | | |
|  |  |  |  |  |  |  |  | x |  |
| **CVE-2026-112421:** An app may be able to modify protected parts of the file system.  Affects PackageKit | | | | | | | | | |
|  |  |  | x | x | x |  |  |  |  |
| **CVE-2026-112423:** Processing a maliciously crafted file may lead to a denial-of-service or potentially disclose memory contents.  Affects SceneKit | | | | | | | | | |
| x | x |  | x | x | x |  |  | x |  |
| **CVE-2026-112424:** An app may be able to cause unexpected system termination or read kernel memory.  Affects HFS | | | | | | | | | |
|  |  |  | x | x | x |  |  |  |  |
| **CVE-2026-112425:** Processing a 3D model may result in disclosure of process memory.  Affects SceneKit | | | | | | | | | |
| x | x |  | x | x | x | x |  | x |  |
| **CVE-2026-112427:** A remote attacker may be able to cause arbitrary code execution.  Affects Remote Management | | | | | | | | | |
|  |  |  | x |  |  |  |  |  |  |
| **CVE-2026-112428:** An app may bypass Gatekeeper checks.  Affects DesktopServices | | | | | | | | | |
|  |  |  | x | x | x |  |  |  |  |
| **CVE-2026-112429:** Processing a maliciously crafted file may disclose process memory.  Affects ColorSync | | | | | | | | | |
|  |  |  | x | x | x |  |  |  |  |
| **CVE-2026-112430:** An app may be able to gain root privileges.  Affects Security | | | | | | | | | |
|  |  |  | x | x | x |  |  |  |  |
| **CVE-2026-112432:** An app may be able to access sensitive user data.  Affects FontParser | | | | | | | | | |
| x |  |  | x |  |  | x | x | x |  |
| **CVE-2026-112434:** An app may be able to gain root privileges.  Affects Security | | | | | | | | | |
|  |  |  | x | x | x |  |  |  |  |
| **CVE-2026-112438:** An unprivileged attacker may be able to execute arbitrary code as root.  Affects Kernel | | | | | | | | | |
|  |  |  | x | x | x |  |  |  |  |
| **CVE-2026-112441:** An app may be able to access sensitive user data.  Affects Spotlight | | | | | | | | | |
|  |  |  | x | x | x |  |  |  |  |
| **CVE-2026-112442:** An app may be able to modify protected parts of the file system.  Affects PackageKit | | | | | | | | | |
|  |  |  | x | x | x |  |  |  |  |
| **CVE-2026-112443:** An app may be able to cause unexpected system termination or corrupt process memory.  Affects Wi-Fi | | | | | | | | | |
|  |  |  | x | x |  |  |  |  |  |
| **CVE-2026-112444:** An app may be able to bypass Gatekeeper checks.  Affects DesktopServices | | | | | | | | | |
|  |  |  | x | x |  |  |  |  |  |
| **CVE-2026-112446:** An app may be able to access sensitive user data.  Affects Accounts | | | | | | | | | |
| x |  |  | x |  |  | x | x | x |  |
| **CVE-2026-112447:** An app may be able to bypass Privacy preferences.  Affects Time Machine | | | | | | | | | |
|  |  |  | x | x | x |  |  |  |  |
| **CVE-2026-112449:** Processing a maliciously crafted 3D model may lead to memory corruption.  Affects Model I/O | | | | | | | | | |
| x | x |  | x | x | x |  |  | x |  |
| **CVE-2026-112451:** A remote attacker may be able to cause a denial-of-service or disclose process memory.  Affects smbx | | | | | | | | | |
|  |  |  | x | x | x |  |  |  |  |
| **CVE-2026-112453:** An app may be able to break out of its sandbox.  Affects System Settings | | | | | | | | | |
|  |  |  | x | x | x |  |  |  |  |
| **CVE-2026-112454:** Processing a maliciously crafted video file may lead to unexpected app termination or corrupt process memory.  Affects AppleAVD | | | | | | | | | |
| x |  |  | x |  |  | x | x | x |  |
| **CVE-2026-112455:** An app may be able to access sensitive user data.  Affects Shortcuts | | | | | | | | | |
| x | x |  | x | x | x | x | x | x |  |
| **CVE-2026-112456:** Processing a maliciously crafted file may lead to heap corruption.  Affects HFS | | | | | | | | | |
| x | x |  | x | x | x |  |  |  |  |
| **CVE-2026-112457:** An attacker on the local network may be able to cause unexpected system termination or corrupt process memory.  Affects Remote Management | | | | | | | | | |
|  |  |  | x | x | x |  |  |  |  |
| **CVE-2026-112459:** An app may be able to cause unexpected system termination or corrupt kernel memory.  Affects IOMobileFrameBuffer | | | | | | | | | |
| x |  |  | x |  |  | x | x |  |  |
| **CVE-2026-112461:** Processing a maliciously crafted 3D model may lead to memory corruption.  Affects Model I/O | | | | | | | | | |
| x | x |  | x | x | x |  |  | x |  |
| **CVE-2026-112462:** A malicious application may be able to bypass Privacy preferences.  Affects Control Center | | | | | | | | | |
|  |  |  | x | x | x |  |  |  |  |
| **CVE-2026-112464:** Processing a maliciously crafted file may lead to heap corruption.  Affects SceneKit | | | | | | | | | |
| x | x |  | x | x | x | x |  | x |  |
| **CVE-2026-112466:** An app may be able to cause unexpected system termination or read kernel memory.  Affects AVEVideoEncoder | | | | | | | | | |
| x | x |  | x | x | x | x | x | x |  |
| **CVE-2026-112467:** An app may be able to bypass network restrictions.  Affects App Store | | | | | | | | | |
|  |  |  | x | x |  |  |  |  |  |
| **CVE-2026-112468:** An app may be able to cause unexpected system termination or corrupt kernel memory.  Affects AVEVideoEncoder |...