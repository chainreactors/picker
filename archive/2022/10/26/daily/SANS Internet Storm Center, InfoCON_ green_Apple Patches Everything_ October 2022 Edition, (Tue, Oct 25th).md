---
title: Apple Patches Everything: October 2022 Edition, (Tue, Oct 25th)
url: https://isc.sans.edu/diary/rss/29182
source: SANS Internet Storm Center, InfoCON: green
date: 2022-10-26
fetch_date: 2025-10-03T20:57:21.018875
---

# Apple Patches Everything: October 2022 Edition, (Tue, Oct 25th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29180)
* [next](/diary/29188)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [Apple Patches Everything: October 2022 Edition](/forums/diary/Apple%2BPatches%2BEverything%2BOctober%2B2022%2BEdition/29182/)

**Published**: 2022-10-25. **Last Updated**: 2022-10-25 00:22:44 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Apple%2BPatches%2BEverything%2BOctober%2B2022%2BEdition/29182/#comments)

A quick summary of Apple's pretty massive patch day today. With the release of a new version of macOS, and updates for all operating systems Apple publishes, we got a total of 106 vulnerabilities. As before with Apple, the rating (critical/important) is our own and not based on a CVSS score, as Apple publishes non. I typically rate privilege escalation, like flaws, as important and code execution flaws as critical. Let me know if you disagree with the rating. "other" just means that I didn't get around to rate the particular issue or that it affects multiple vulnerabilities.

One of the critical issues, CVE-2022-42827, may have been actively exploited, according to reports received by Apple. This issue affects iPadOS and iOS.

| Safari | iOS and iPadOS | MacOS Monterey (12.x) | MacOS BigSur (10.x) | macOS Ventura (13.x) | TVOS | WatchOS |
| --- | --- | --- | --- | --- | --- | --- |
| **WebKit Bugzilla [important]** WebKit  A logic issue was addressed with improved state management.  Processing maliciously crafted web content may disclose sensitive user information | | | | | | | |
| x | x |  |  | x | x | x |
| **CVE-2022-42825 [important]** AppleMobileFileIntegrity  This issue was addressed by removing additional entitlements.  An app may be able to modify protected parts of the file system | | | | | | | |
|  | x | x | x | x | x | x |
| **CVE-2022-32940 [important]** AVEVideoEncoder  The issue was addressed with improved bounds checks.  An app may be able to execute arbitrary code with kernel privileges | | | | | | | |
|  | x |  |  | x | x | x |
| **CVE-2022-42813 [critical]** CFNetwork  A certificate validation issue existed in the handling of WKWebView. This issue was addressed with improved validation.  Processing a maliciously crafted certificate may lead to arbitrary code execution | | | | | | | |
|  | x |  |  | x | x | x |
| **CVE-2022-32946 [important]** Core Bluetooth  This issue was addressed with improved entitlements.  An app may be able to record audio using a pair of connected AirPods | | | | | | | |
|  | x |  |  |  |  |  |
| **CVE-2022-32947 [important]** GPU Drivers  The issue was addressed with improved memory handling.  An app may be able to execute arbitrary code with kernel privileges | | | | | | | |
|  | x |  |  | x |  | x |
| **CVE-2022-42820 [important]** IOHIDFamily  A memory corruption issue was addressed with improved state management.  An app may cause unexpected app termination or arbitrary code execution | | | | | | | |
|  | x |  |  | x |  |  |
| **CVE-2022-42806 [important]** IOKit  A race condition was addressed with improved locking.  An app may be able to execute arbitrary code with kernel privileges | | | | | | | |
|  | x |  |  | x |  |  |
| **CVE-2022-32924 [important]** Kernel  The issue was addressed with improved memory handling.  An app may be able to execute arbitrary code with kernel privileges | | | | | | | |
|  | x |  |  | x | x | x |
| **CVE-2022-42808 [critical]** Kernel  An out-of-bounds write issue was addressed with improved bounds checking.  A remote user may be able to cause kernel code execution | | | | | | | |
|  | x |  |  | x | x | x |
| **CVE-2022-42827 [critical]** Kernel  An out-of-bounds write issue was addressed with improved bounds checking.  An application may be able to execute arbitrary code with kernel privileges.  **Apple is aware of a report that this issue may have been actively exploited.** | | | | | | | |
|  | x |  |  |  |  |  |
| **CVE-2022-42829 [important]** ppp  A use after free issue was addressed with improved memory management.  An app with root privileges may be able to execute arbitrary code with kernel privileges | | | | | | | |
|  | x |  |  | x |  |  |
| **CVE-2022-42830 [important]** ppp  The issue was addressed with improved memory handling.  An app with root privileges may be able to execute arbitrary code with kernel privileges | | | | | | | |
|  | x |  |  | x |  |  |
| **CVE-2022-42831 [important]** ppp  A race condition was addressed with improved locking.  An app with root privileges may be able to execute arbitrary code with kernel privileges | | | | | | | |
|  | x |  |  | x |  |  |
| **CVE-2022-42832 [important]** ppp  A race condition was addressed with improved locking.  An app with root privileges may be able to execute arbitrary code with kernel privileges | | | | | | | |
|  | x |  |  | x |  |  |
| **CVE-2022-42811 [important]** Sandbox  An access issue was addressed with additional sandbox restrictions.  An app may be able to access user-sensitive data | | | | | | | |
|  | x |  |  | x | x | x |
| **CVE-2022-32938 [important]** Shortcuts  A parsing issue in the handling of directory paths was addressed with improved path validation.  A shortcut may be able to check the existence of an arbitrary path on the file system | | | | | | | |
|  | x |  |  | x |  |  |
| **CVE-2022-28739 [critical]** Ruby  A memory corruption issue was addressed by updating Ruby to version 2.6.10.  A remote user may be able to cause unexpected app termination or arbitrary code execution | | | | | | | |
|  |  | x | x | x |  |  |
| **CVE-2022-32862 [important]** Sandbox  This issue was addressed with improved data protection.  An app with root privileges may be able to access private information | | | | | | | |
|  |  | x | x | x |  |  |
| **CVE-2022-42795 [critical]** Accelerate Framework  A memory consumption issue was addressed with improved memory handling.  Processing a maliciously crafted image may lead to arbitrary code execution | | | | | | | |
|  |  |  |  | x |  |  |
| **CVE-2022-32858 [important]** Apple Neural Engine  The issue was addressed with improved memory handling.  An app may be able to leak sensitive kernel state | | | | | | | |
|  |  |  |  | x |  |  |
| **CVE-2022-32898 [important]** Apple Neural Engine  The issue was addressed with improved memory handling.  An app may be able to execute arbitrary code with kernel privileges | | | | | | | |
|  |  |  |  | x |  |  |
| **CVE-2022-32899 [important]** Apple Neural Engine  The issue was addressed with improved memory handling.  An app may be able to execute arbitrary code with kernel privileges | | | | | | | |
|  |  |  |  | x |  |  |
| **CVE-2022-32827 [important]** AppleAVD  A memory corruption issue was addressed with improved state management.  An app may be able to cause a denial-of-service | | | | | | | |
|  |  |  |  | x |  |  |
| **CVE-2022-42789 [important]** AppleMobileFileIntegrity  An issue in code signature validation was addressed with improved checks.  An app may be able to access user-sensitive data | | | | | | | |
|  |  |  |  | x |  |  |
| **CVE-2022-32902 [important]** ATS  A logic issue was addressed with improved state management.  An app may be able to bypass Privacy preferences | | | | | | | |
|  |  |  |  | x |  |  |
| **CVE-2022-32904 [important]** ATS  An access issue was addressed with additional sandbox restrictions.  An app may be able to access user-sensitive data | | | | | | | |
|  |  |  |  | x |  |  |
| **CVE-2022-32890 [moderate]** ATS  A logic issue was addressed with improved checks.  A ...