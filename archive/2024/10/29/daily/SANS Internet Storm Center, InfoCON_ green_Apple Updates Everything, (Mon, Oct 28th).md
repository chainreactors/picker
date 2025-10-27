---
title: Apple Updates Everything, (Mon, Oct 28th)
url: https://isc.sans.edu/diary/rss/31390
source: SANS Internet Storm Center, InfoCON: green
date: 2024-10-29
fetch_date: 2025-10-06T18:55:16.355527
---

# Apple Updates Everything, (Mon, Oct 28th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31388)
* [next](/diary/31398)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Apple Updates Everything](/forums/diary/Apple%2BUpdates%2BEverything/31390/)

**Published**: 2024-10-28. **Last Updated**: 2024-10-28 20:34:12 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Apple%2BUpdates%2BEverything/31390/#comments)

Today, Apple released updates for all of its operating systems. These updates include new AI features. For iOS 18 users, the only upgrade path is iOS 18.1, which includes the AI features. Same for users of macOS 15 Sequoia. For older operating systems versions (iOS 17, macOS 13, and 14), patches are made available, addressing only the security issues.

None of the vulnerabilities is marked as already exploited. The update fixes several lock screen bypass issues and cross-application/sandbox escape issues. Overall, I didn't spot a "mast patch now" issue. Many of the lock screen bypass issues can often be eliminated.

Apple patched a total of 67 vulnerabilities.

Breakdown of vulnerabilities by operating system:

| Operating System | # of Vulns. Patched |
| --- | --- |
| macOS Sequoia 15.1 | 49 |
| macOS Sonoma 14.7.1 | 39 |
| macOS Ventura 13.7.1 | 36 |
| iOS 18.1 and iPadOS 18.1 | 27 |
| visionOS 2.1 | 19 |
| iOS 17.7.1 and iPadOS 17.7.1 | 16 |
| watchOS 11.1 | 15 |
| tvOS 18.1 | 13 |

Detailed Breackdown of vulnerabilities:

| iOS 18.1 and iPadOS 18.1 | iOS 17.7.1 and iPadOS 17.7.1 | macOS Sequoia 15.1 | macOS Sonoma 14.7.1 | macOS Ventura 13.7.1 | watchOS 11.1 | tvOS 18.1 | visionOS 2.1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **CVE-2024-40851:** An attacker with physical access may be able to access contact photos from the lock screen.  Affects Siri | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2024-40855:** A sandboxed app may be able to access sensitive user data.  Affects DiskArbitration | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2024-40858:** An app may be able to access Contacts without user consent.  Affects Photos | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2024-40867:** A remote attacker may be able to break out of Web Content sandbox.  Affects iTunes | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2024-40867:** A remote attacker may be able to break out of Web Content sandbox.  Affects iTunes | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2024-44122:** An application may be able to break out of its sandbox.  Affects LaunchServices | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2024-44126:** Processing a maliciously crafted file may lead to heap corruption.  Affects ARKit | | | | | | | |
|  |  |  |  | x |  |  |  |
| **CVE-2024-44137:** An attacker with physical access may be able to share items from the lock screen.  Affects Screen Capture | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2024-44144:** Processing a maliciously crafted file may lead to unexpected app termination.  Affects SceneKit | | | | | | | |
|  | x |  | x |  |  |  |  |
| **CVE-2024-44155:** Maliciously crafted web content may violate iframe sandboxing policy.  Affects Safari | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2024-44156:** An app may be able to bypass Privacy preferences.  Affects PackageKit | | | | | | | |
|  |  |  | x |  |  |  |  |
| **CVE-2024-44159:** An app may be able to bypass Privacy preferences.  Affects PackageKit | | | | | | | |
|  |  | x |  | x |  |  |  |
| **CVE-2024-44175:** An app may be able to access sensitive user data.  Affects Kernel | | | | | | | |
|  |  |  | x |  |  |  |  |
| **CVE-2024-44194:** An app may be able to access sensitive user data.  Affects Siri | | | | | | | |
| x |  | x |  |  | x |  | x |
| **CVE-2024-44195:** An app may be able to read arbitrary files.  Affects Quick Look | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2024-44196:** An app may be able to modify protected parts of the file system.  Affects PackageKit | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2024-44197:** A malicious app may be able to cause a denial-of-service.  Affects IOGPUFamily | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2024-44211:** An app may be able to access user-sensitive data.  Affects Sandbox | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2024-44213:** An attacker in a privileged network position may be able to leak sensitive user information.  Affects CUPS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2024-44215:** Processing an image may result in disclosure of process memory.  Affects ImageIO | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2024-44216:** An app may be able to access user-sensitive data.  Affects Installer | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2024-44218:** Processing a maliciously crafted file may lead to heap corruption.  Affects SceneKit | | | | | | | |
| x | x | x | x |  |  |  |  |
| **CVE-2024-44222:** An app may be able to read sensitive location information.  Affects Maps | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2024-44223:** An attacker with physical access to a Mac may be able to view protected content from the Login Window.  Affects Login Window | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2024-44229:** Private browsing may leak some browsing history.  Affects Safari Private Browsing | | | | | | | |
| x |  | x |  |  |  |  | x |
| **CVE-2024-44231:** A person with physical access to a Mac may be able to bypass Login Window during a software update.  Affects Login Window | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2024-44235:** An attacker may be able to view restricted content from the lock screen.  Affects Spotlight | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2024-44237:** Processing a maliciously crafted file may lead to unexpected app termination.  Affects sips | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2024-44239:** An app may be able to leak sensitive kernel state.  Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2024-44244:** Processing maliciously crafted web content may lead to an unexpected process crash.  Affects WebKit | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2024-44251:** An attacker may be able to view restricted content from the lock screen.  Affects Spotlight | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2024-44252:** Restoring a maliciously crafted backup file may lead to modification of protected system files.  Affects MobileBackup | | | | | | | |
| x | x |  |  |  |  | x | x |
| **CVE-2024-44253:** An app may be able to modify protected parts of the file system.  Affects PackageKit | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2024-44254:** An app may be able to access sensitive user data.  Affects Shortcuts | | | | | | | |
| x |  | x | x | x | x |  |  |
| **CVE-2024-44255:** A malicious app may be able to run arbitrary shortcuts without user consent.  Affects App Support | | | | | | | |
| x |  | x | x | x | x | x | x |
| **CVE-2024-44256:** An app may be able to break out of its sandbox.  Affects Messages | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2024-44257:** An app may be able to access sensitive user data.  Affects WindowServer | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2024-44258:** Restoring a maliciously crafted backup file may lead to modification of protected system files.  Affects Managed Configuration | | | | | | | |
| x | x |  |  |  |  | x | x |
| **CVE-2024-44259:** An attacker may be able to misuse a trust relationship to download malicious c...