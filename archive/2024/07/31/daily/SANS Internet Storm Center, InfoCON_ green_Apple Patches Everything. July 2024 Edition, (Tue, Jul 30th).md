---
title: Apple Patches Everything. July 2024 Edition, (Tue, Jul 30th)
url: https://isc.sans.edu/diary/rss/31128
source: SANS Internet Storm Center, InfoCON: green
date: 2024-07-31
fetch_date: 2025-10-06T17:46:56.143353
---

# Apple Patches Everything. July 2024 Edition, (Tue, Jul 30th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31122)
* [next](/diary/31132)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Apple Patches Everything. July 2024 Edition](/forums/diary/Apple%2BPatches%2BEverything%2BJuly%2B2024%2BEdition/31128/)

**Published**: 2024-07-30. **Last Updated**: 2024-07-30 17:01:22 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Apple%2BPatches%2BEverything%2BJuly%2B2024%2BEdition/31128/#comments)

Yesterday, Apple released patches across all of its operating systems. A standalone patch for Safari was released to address WebKit problems in older macOS versions. Apple does not provide CVSS scores or severity ratings. The ratings below are based on my reading of the impact. However, the information isn’t always sufficient to accurately assign a rating.

One vulnerability, CVE-2024-23296, which can be used to bypass kernel protections via RTKit, is already being exploited. Apple patched this issue for newer operating systems in March, but it now releasing the patch for older macOS and iOS versions.

According to my count, these updates address 64 different vulnerabilities.

| Safari 17.5 | iOS 17.5 and iPadOS 17.5 | iOS 16.7.8 and iPadOS 16.7.8 | macOS Sonoma 14.5 | macOS Ventura 13.6.7 | macOS Monterey 12.7.5 | watchOS 10.5 | tvOS 17.5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **CVE-2024-27844 [moderate]**  Safari  The issue was addressed with improved checks.  A website's permission dialog may persist after navigation away from the site | | | | | | | |
| x |  |  | x |  |  |  |  |
| **CVE-2024-27834 [moderate]**  WebKit  The issue was addressed with improved checks.  An attacker with arbitrary read and write capability may be able to bypass Pointer Authentication | | | | | | | |
| x | x | x | x |  |  | x | x |
| **CVE-2024-27838 [moderate]**  WebKit  The issue was addressed by adding additional logic.  A maliciously crafted webpage may be able to fingerprint the user | | | | | | | |
| x | x | x | x |  |  | x | x |
| **CVE-2024-27808 [critical]**  WebKit  The issue was addressed with improved memory handling.  Processing web content may lead to arbitrary code execution | | | | | | | |
| x | x |  | x |  |  | x | x |
| **CVE-2024-27850 [moderate]**  WebKit  This issue was addressed with improvements to the noise injection algorithm.  A maliciously crafted webpage may be able to fingerprint the user | | | | | | | |
| x | x |  | x |  |  |  |  |
| **CVE-2024-27833 [critical]**  WebKit  An integer overflow was addressed with improved input validation.  Processing maliciously crafted web content may lead to arbitrary code execution | | | | | | | |
| x | x | x |  |  |  |  | x |
| **CVE-2024-27851 [critical]**  WebKit  The issue was addressed with improved bounds checks.  Processing maliciously crafted web content may lead to arbitrary code execution | | | | | | | |
| x | x |  | x |  |  | x | x |
| **CVE-2024-27830 [moderate]**  WebKit Canvas  This issue was addressed through improved state management.  A maliciously crafted webpage may be able to fingerprint the user | | | | | | | |
| x | x |  | x |  |  | x | x |
| **CVE-2024-27820 [critical]**  WebKit Web Inspector  The issue was addressed with improved memory handling.  Processing web content may lead to arbitrary code execution | | | | | | | |
| x | x | x | x |  |  | x | x |
| **CVE-2024-27826 [moderate]**  Apple Neural Engine  The issue was addressed with improved memory handling.  A local attackermay be able to cause unexpected system shutdown | | | | | | | |
|  | x |  | x |  |  | x | x |
| **CVE-2024-27804 [moderate]**  AppleAVD  The issue was addressed with improved memory handling.  An app may be able to cause unexpected system termination | | | | | | | |
|  | x |  | x |  |  | x | x |
| **CVE-2024-27816 [moderate]**  RemoteViewServices  A logic issue was addressed with improved checks.  An attacker may be able to access user data | | | | | | | |
|  | x |  | x |  |  | x | x |
| **CVE-2024-27841 [important]**  AVEVideoEncoder  The issue was addressed with improved memory handling.  An app may be able to disclose kernel memory | | | | | | | |
|  | x |  | x |  |  |  |  |
| **CVE-2024-27805 [moderate]**  Core Data  An issue was addressed with improved validation of environment variables.  An app may be able to access sensitive user data | | | | | | | |
|  | x | x | x | x | x | x | x |
| **CVE-2024-27817 [important]**  CoreMedia  The issue was addressed with improved checks.  An app may be able to execute arbitrary code with kernel privileges | | | | | | | |
|  | x | x | x | x | x |  | x |
| **CVE-2024-27831 [moderate]**  CoreMedia  An out-of-bounds write issue was addressed with improved input validation.  Processing a file may lead to unexpected app termination or arbitrary code execution | | | | | | | |
|  | x | x | x | x | x |  | x |
| **CVE-2024-27832 [moderate]**  Disk Images  The issue was addressed with improved checks.  An app may be able to elevate privileges | | | | | | | |
|  | x |  | x |  |  | x | x |
| **CVE-2024-27839 [moderate]**  Find My  A privacy issue was addressed by moving sensitive data to a more secure location.  A malicious application may be able to determine a user's current location | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2024-27801 [moderate]**  Foundation  The issue was addressed with improved checks.  An app may be able to elevate privileges | | | | | | | |
|  | x |  | x |  |  | x | x |
| **CVE-2024-27836 [critical]**  ImageIO  The issue was addressed with improved checks.  Processing a maliciously crafted image may lead to arbitrary code execution | | | | | | | |
|  | x |  | x |  |  |  |  |
| **CVE-2024-27828 [important]**  IOSurface  The issue was addressed with improved memory handling.  An app may be able to execute arbitrary code with kernel privileges | | | | | | | |
|  | x |  |  |  |  | x | x |
| **CVE-2024-27818 [moderate]**  Kernel  The issue was addressed with improved memory handling.  An attacker may be able to cause unexpected app termination or arbitrary code execution | | | | | | | |
|  | x | x | x |  |  |  |  |
| **CVE-2024-27840 [moderate]**  Kernel  The issue was addressed with improved memory handling.  An attacker that has already achieved kernel code execution may be able to bypass kernel memory protections | | | | | | | |
|  | x | x |  | x | x | x | x |
| **CVE-2024-27815 [important]**  Kernel  An out-of-bounds write issue was addressed with improved input validation.  An app may be able to execute arbitrary code with kernel privileges | | | | | | | |
|  | x |  | x |  |  | x | x |
| **CVE-2024-27823 [moderate]**  Kernel  A race condition was addressed with improved locking.  An attacker in a privileged network position may be able to spoof network packets | | | | | | | |
|  | x | x | x | x | x | x | x |
| **CVE-2024-27811 [moderate]**  libiconv  The issue was addressed with improved checks.  An app may be able to elevate privileges | | | | | | | |
|  | x |  | x |  |  | x | x |
| **CVE-2023-42893 [moderate]**  Libsystem  A permissions issue was addressed by removing vulnerable code and adding additional checks.  An app may be able to access protected user data | | | | | | | |
|  | x |  | x |  |  |  |  |
| **CVE-2024-23251 [moderate]**  Mail  An authentication issue was addressed with improved state management.  An attacker with physical access may be able to leak Mail account credentials | | | | | | | |
|  | x | x | x |  |  | x |  |
| **CVE-2024-23282 [moderate]**  Mail  The issue was addressed with improved checks.  A maliciously crafted ema...