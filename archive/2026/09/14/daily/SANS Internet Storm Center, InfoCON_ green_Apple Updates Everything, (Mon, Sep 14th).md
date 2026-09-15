---
title: Apple Updates Everything, (Mon, Sep 14th)
url: https://isc.sans.edu/diary/rss/33336
source: SANS Internet Storm Center, InfoCON: green
date: 2026-09-14
fetch_date: 2026-09-15T07:03:05.990732
---

# Apple Updates Everything, (Mon, Sep 14th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/33332)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Apple Updates Everything](/forums/diary/Apple%2BUpdates%2BEverything/33336/)

**Published**: 2026-09-14. **Last Updated**: 2026-09-14 18:33:44 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Apple%2BUpdates%2BEverything/33336/#comments)

Today, Apple released its annual update across all its operating systems. With that, Apple not only released new features but also patched 261 different vulnerabilities. This is the most vulnerabilities Apple has ever patched, but the increase is not as significant as other vendors' "post-AI" patch releases.

In addition to the major "27" version, Apple also released bug-fix-only releases for the 26 branch of its operating systems and for 15 (Sequioa) for macOS. None of the vulnerabilities is labeled as being exploited. Apple does not note a severity to individual vulnerabilities.

There are some reports about difficulties downloading iOS 27. Users instead see 26.7 downloaded, but iOS 27 may actually be installed. Also note that some security-relevant applications, such as Little Snitch, have recently released updates that must be applied before upgrading to macOS 27. The Objective-See utility BlockBlock released version 2.5.2 to improve macOS 27 compatiblity.

![](https://isc.sans.edu/diaryimages/images/Screenshot%202026-09-14%20at%202_23_35%E2%80%AFPM.png)
Figure: Number of patches for each update over the last 2 years.

| iOS 27 and iPadOS 27 | iOS 26.7 and iPadOS 26.7 | macOS Golden Gate 27 | macOS Tahoe 26.7 | macOS Sequoia 15.8 | tvOS 27 | watchOS 27 | visionOS 27 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **CVE-2022-3437:** A user in a privileged network position may be able to leak sensitive user information.  Affects Heimdal | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-20683:** An app may be able to use the Sign In With Apple authentication flow to access the user's Apple Account.  Affects Apple Account | | | | | | | |
| x |  | x | x | x |  |  | x |
| **CVE-2026-28899:** An app may bypass Gatekeeper checks.  Affects WebDAV | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-28930:** An app may be able to access protected user data.  Affects Spotlight | | | | | | | |
|  |  |  |  | x |  |  |  |
| **CVE-2026-28934:** Mounting a malicious disk image may cause unexpected system termination.  Affects HFS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-28935:** An app may be able to cause unexpected system termination or corrupt kernel memory.  Affects Kernel | | | | | | | |
|  |  |  |  | x | x | x | x |
| **CVE-2026-28937:** An app may be able to access sensitive user data.  Affects Terminal | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-28966:** Processing a maliciously crafted file may lead to unexpected app termination.  Affects RealityKit | | | | | | | |
| x | x | x | x | x | x |  | x |
| **CVE-2026-28968:** An app may be able to cause unexpected system termination or corrupt kernel memory.  Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-28969:** An app may be able to cause unexpected system termination.  Affects IOKit | | | | | | | |
| x |  | x | x | x | x | x | x |
| **CVE-2026-34979:** An attacker in a privileged network position may be able to cause a denial-of-service.  Affects CUPS | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-43661:** Processing a maliciously crafted image may corrupt process memory.  Affects ImageIO | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2026-43664:** An app may be able to access sensitive user data.  Affects Accessibility | | | | | | | |
| x | x | x | x | x | x | x |  |
| **CVE-2026-43674:** An attacker with physical access to an unlocked device may be able to view Wi-Fi passwords without authentication.  Affects Wi-Fi3 | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2026-43677:** Connecting to a malicious WebDAV server may lead to unexpected app termination.  Affects WebDAV | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43683:** An app may be able to cause unexpected process termination or disclose process memory.  Affects CoreDrag | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43684:** An app may be able to cause unexpected system termination or corrupt kernel memory.  Affects Kernel | | | | | | | |
|  | x | x |  | x |  |  |  |
| **CVE-2026-43686:** Connecting to a malicious NFS server may lead to kernel memory corruption.  Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-43687:** Connecting to a malicious NFS server may disclose kernel memory.  Affects Kernel | | | | | | | |
| x | x | x | x |  | x | x | x |
| **CVE-2026-43688:** Processing a maliciously crafted file may lead to unexpected app termination.  Affects Filters | | | | | | | |
| x |  | x |  |  |  |  |  |
| **CVE-2026-43689:** A malicious app may be able to gain root privileges.  Affects Kernel | | | | | | | |
| x | x | x |  |  |  |  | x |
| **CVE-2026-43690:** A local user may be able to read kernel memory.  Affects SMB | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43691:** An app may be able to gain root privileges.  Affects CUPS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43692:** A remote user may cause an unexpected app termination or arbitrary code execution.  Affects CUPS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43695:** An app may be able to access sensitive user data.  Affects NetworkExtension | | | | | | | |
| x |  | x | x | x | x | x | x |
| **CVE-2026-43696:** An app may be able to capture Touch Bar content without authorization.  Affects Touch Bar | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-43697:** Processing a maliciously crafted 3D file may lead to an out-of-bounds read.  Affects SceneKit | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43698:** An app may be able to gain root privileges.  Affects CUPS | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-43702:** Processing a maliciously crafted video file may lead to unexpected app termination or corrupt process memory.  Affects CoreMedia Video Toolbox | | | | | | | |
|  | x |  | x | x |  |  |  |
| **CVE-2026-43715:** Processing maliciously crafted web content may lead to memory corruption.  Affects WebKit | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2026-43719:** Mounting a maliciously crafted SMB network share may lead to system termination.  Affects SMB | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43737:** An app may be able to access motion data from headphones without user consent.  Affects CoreMotion | | | | | | | |
| x | x | x | x | x | x | x |  |
| **CVE-2026-43738:** Processing a maliciously crafted asset catalog may result in disclosure of process memory.  Affects CoreUI | | | | | | | |
| x |  | x |  |  |  |  |  |
| **CVE-2026-43741:** An app may be able to access protected user data.  Affects Messages | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43743:** An app may be able to cause unexpected system termination.  Affects IOGPUFamily | | | | | | | |
|  | x |  | x |  |  |  |  |
| **CVE-2026-43760:** An app may be able to access user-sensitive data.  Affects Screen Sharing Server | | | | | | | |
|  |  |  | x |  |  |  |  |
| **CVE-2026-43763:** An app may be able to read files outside of its sandbox.  Affects ATS | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2026-43785:** An app may be able to modify a file it only had permission to read.  Affects File Bookmark | | | | | | | |
| x |  | x | x | x | x |  | x |
| **CVE-2026-43786:** An app may be able to gain ...