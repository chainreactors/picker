---
title: Apple Updates Everything (including Studio Display), (Mon, Mar 27th)
url: https://isc.sans.edu/diary/rss/29682
source: SANS Internet Storm Center, InfoCON: green
date: 2023-03-28
fetch_date: 2025-10-04T10:55:25.355112
---

# Apple Updates Everything (including Studio Display), (Mon, Mar 27th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29678)
* [next](/diary/29688)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Apple Updates Everything (including Studio Display)](/forums/diary/Apple%2BUpdates%2BEverything%2Bincluding%2BStudio%2BDisplay/29682/)

**Published**: 2023-03-27. **Last Updated**: 2023-03-27 21:01:22 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Apple%2BUpdates%2BEverything%2Bincluding%2BStudio%2BDisplay/29682/#comments)

Apple today released updates for all of its operating systems. The updates also apply for some of the older versions of iOS and macOS. For iOS/iPadOS 15, Apple now patched an already exploited vulnerability (CVE-2023-23529). Current operating systems received a patch for this vulnerability mid January.

Noteworthy is also that this is the first time, as far as I can recall, that we got a security update for the Studio Display firmware. Firmware updates were released before for the studio display, but they fixed non-security bugs.

| Studio Display Firmware Update 16.4 | Safari 16.4 | iOS 15.7.4 and iPadOS 15.7.4 | iOS 16.4 and iPadOS 16.4 | watchOS 9.4 | tvOS 16.4 | macOS Big Sur 11.7.5 | macOS Monterey 12.6.4 | macOS Ventura 13.3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **CVE-2023-27965 [important]**  Display  A memory corruption issue was addressed with improved state management.  An app may be able to execute arbitrary code with kernel privileges | | | | | | | | |
| x |  |  |  |  |  |  |  | x |
| **CVE-2023-27932 [moderate]**  WebKit  This issue was addressed with improved state management.  Processing maliciously crafted web content may bypass Same Origin Policy | | | | | | | | |
|  | x |  | x | x | x |  |  | x |
| **CVE-2023-27954 [moderate]**  WebKit  The issue was addressed by removing origin information.  A website may be able to track sensitive user information | | | | | | | | |
|  | x | x | x | x | x |  |  | x |
| **CVE-2023-23541 [moderate]**  Accessibility  A privacy issue was addressed with improved private data redaction for log entries.  An app may be able to access information about a user?s contacts | | | | | | | | |
|  |  | x | x |  |  |  |  |  |
| **CVE-2023-27961 [moderate]**  Calendar  Multiple validation issues were addressed with improved input sanitization.  Importing a maliciously crafted calendar invitation may exfiltrate user information | | | | | | | | |
|  |  | x | x | x |  | x | x | x |
| **CVE-2023-23543 [moderate]**  Camera  The issue was addressed with additional restrictions on the observability of app states.  A sandboxed app may be able to determine which app is currently using the camera | | | | | | | | |
|  |  | x | x |  |  |  |  | x |
| **CVE-2023-27936 [important]**  CommCenter  An out-of-bounds write issue was addressed with improved input validation.  An app may be able to cause unexpected system termination or write kernel memory | | | | | | | | |
|  |  | x |  |  |  | x | x | x |
| **CVE-2023-23537 [important]**  Find My  A privacy issue was addressed with improved private data redaction for log entries.  An app may be able to read sensitive location information | | | | | | | | |
|  |  | x | x | x |  | x |  | x |
| **CVE-2023-27956 [important]**  FontParser  The issue was addressed with improved memory handling.  Processing a maliciously crafted image may result in disclosure of process memory | | | | | | | |
|  |  | x | x | x | x |  |  | x |
| **CVE-2023-27928 [moderate]**  Identity Services  A privacy issue was addressed with improved private data redaction for log entries.  An app may be able to access information about a user?s contacts | | | | | | | | |
|  |  | x | x | x | x | x |  | x |
| **CVE-2023-27946 [moderate]**  ImageIO  An out-of-bounds read was addressed with improved bounds checking.  Processing a maliciously crafted file may lead to unexpected app termination or arbitrary code execution | | | | | | | | |
|  |  | x |  |  |  | x | x | x |
| **CVE-2023-23535 [important]**  ImageIO  The issue was addressed with improved memory handling.  Processing a maliciously crafted image may result in disclosure of process memory | | | | | | | | |
|  |  | x | x | x | x | x |  | x |
| **CVE-2023-27941 [important]**  Kernel  An out-of-bounds read issue existed that led to the disclosure of kernel memory. This was addressed with improved input validation.  An app may be able to disclose kernel memory | | | | | | | | |
|  |  | x |  |  |  |  |  | x |
| **CVE-2023-27969 [important]**  Kernel  A use after free issue was addressed with improved memory management.  An app may be able to execute arbitrary code with kernel privileges | | | | | | | | |
|  |  | x | x | x | x |  |  | x |
| **CVE-2023-27949 [moderate]**  Model I/O  An out-of-bounds read was addressed with improved input validation.  Processing a maliciously crafted file may lead to unexpected app termination or arbitrary code execution | | | | | | | | |
|  |  | x |  |  |  |  | x | x |
| **CVE-2023-28182 [moderate]**  NetworkExtension  The issue was addressed with improved authentication.  A user in a privileged network position may be able to spoof a VPN server that is configured with EAP-only authentication on a device | | | | | | | | |
|  |  | x | x |  |  | x | x | x |
| **CVE-2023-27963 [moderate]**  Shortcuts  The issue was addressed with additional permissions checks.  A shortcut may be able to use sensitive data with certain actions without prompting the user | | | | | | | | |
|  |  | x | x | x |  |  | x | x |
| **CVE-2023-23529 [critical] \*\*\* EXPLOITED \*\*\***  WebKit  A type confusion issue was addressed with improved checks.  Processing maliciously crafted web content may lead to arbitrary code execution. Apple is aware of a report that this issue may have been actively exploited. | | | | | | | | |
|  |  | x |  |  |  |  |  |  |
| **CVE-2023-23540 [important]**  Apple Neural Engine  The issue was addressed with improved memory handling.  An app may be able to execute arbitrary code with kernel privileges | | | | | | | | |
|  |  |  | x |  |  | x | x |  |
| **CVE-2023-27959 [important]**  Apple Neural Engine  The issue was addressed with improved memory handling.  An app may be able to execute arbitrary code with kernel privileges | | | | | | | | |
|  |  |  | x |  |  |  |  |  |
| **CVE-2023-27970 [important]**  Apple Neural Engine  An out-of-bounds write issue was addressed with improved bounds checking.  An app may be able to execute arbitrary code with kernel privileges | | | | | | | | |
|  |  |  | x |  |  |  |  |  |
| **CVE-2023-23532 [important]**  Apple Neural Engine  This issue was addressed with improved checks.  An app may be able to break out of its sandbox | | | | | | | | |
|  |  |  | x |  |  |  |  | x |
| **CVE-2023-23527 [moderate]**  AppleMobileFileIntegrity  The issue was addressed with improved checks.  A user may gain access to protected parts of the file system | | | | | | | | |
|  |  |  | x | x | x | x | x | x |
| **CVE-2023-27931 [important]**  TCC  This issue was addressed by removing the vulnerable code.  An app may be able to access user-sensitive data | | | | | | | | |
|  |  |  | x | x | x |  |  | x |
| **CVE-2023-23494 [moderate]**  CarPlay  A buffer overflow was addressed with improved bounds checking.  A user in a privileged network position may be able to cause a denial-of-service | | | | | | | | |
|  |  |  | x |  |  |  |  |  |
| **CVE-2023-27955 [moderate]**  ColorSync  The issue was addressed with improved checks.  An app may be able to read arbitrary files | | | | | | | | |
|  |  |  | x |...