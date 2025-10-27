---
title: Apple Updates (almost) Everything: Patch Overview, (Tue, Jan 24th)
url: https://isc.sans.edu/diary/rss/29472
source: SANS Internet Storm Center, InfoCON: green
date: 2023-01-25
fetch_date: 2025-10-04T04:45:33.505709
---

# Apple Updates (almost) Everything: Patch Overview, (Tue, Jan 24th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29470)
* [next](/diary/29480)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [Apple Updates (almost) Everything: Patch Overview](/forums/diary/Apple%2BUpdates%2Balmost%2BEverything%2BPatch%2BOverview/29472/)

**Published**: 2023-01-24. **Last Updated**: 2023-01-24 15:07:10 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Apple%2BUpdates%2Balmost%2BEverything%2BPatch%2BOverview/29472/#comments)

Apple yesterday released its usually set of updates across its entire portfolio of operating systems. Some issues of note:

* The update includes a patch for CVE-2022-42856 for iOS 12.5. This will help users of older Apple devices going back to the iPhone 5s. More recent operating systems received this patch in December.
* tvOS is missing. I expect a tvOS update soon to address some of the vulnerabilities.
* I do not see updates for git. Git last week patched some vulnerabilities; likely too late to be included in this update.

| Safari 16.3 | iOS 12.5.7 | macOS Monterey 12.6.3 | macOS Big Sur 11.7.3 | watchOS 9.3 | iOS 15.7.3 and iPadOS 15.7.3 | iOS 16.3 and iPadOS 16.3 | macOS Ventura 13.2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **CVE-2023-23496 [critical]**  WebKit  The issue was addressed with improved checks.  Processing maliciously crafted web content may lead to arbitrary code execution | | | | | | | |
| x |  |  |  | x |  | x | x |
| **CVE-2023-23518 [critical]**  WebKit  The issue was addressed with improved memory handling.  Processing maliciously crafted web content may lead to arbitrary code execution | | | | | | | |
| x |  | x | x | x |  | x | x |
| **CVE-2023-23517 [critical]**  WebKit  The issue was addressed with improved memory handling.  Processing maliciously crafted web content may lead to arbitrary code execution | | | | | | | |
| x |  | x | x | x |  | x | x |
| **CVE-2022-42856 [critical] \*\*\* EXPLOITED \*\*\***  WebKit  A type confusion issue was addressed with improved state handling.   Processing maliciously crafted web content may lead to arbitrary code execution. Apple is aware of a report that this issue may have been actively exploited against versions of iOS released before iOS 15.1. | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2023-23499 [important]**  AppleMobileFileIntegrity  This issue was addressed by enabling hardened runtime.  An app may be able to access user-sensitive data | | | | | | | |
|  |  | x | x | x |  | x | x |
| **CVE-2022-42915 [other]**  curl  Multiple issues were addressed by updating to curl version 7.86.0.  Multiple issues in curl | | | | | | | |
|  |  | x |  |  |  |  | x |
| **CVE-2022-42916 [other]**  curl  Multiple issues were addressed by updating to curl version 7.86.0.  Multiple issues in curl | | | | | | | |
|  |  | x |  |  |  |  | x |
| **CVE-2022-32221 [other]**  curl  Multiple issues were addressed by updating to curl version 7.86.0.  Multiple issues in curl | | | | | | | |
|  |  | x |  |  |  |  | x |
| **CVE-2022-35260 [other]**  curl  Multiple issues were addressed by updating to curl version 7.86.0.  Multiple issues in curl | | | | | | | |
|  |  | x |  |  |  |  | x |
| **CVE-2022-35252 [other]**  curl  Multiple issues were addressed by updating to curl version 7.85.0.  Multiple issues in curl | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2023-23513 [critical]**  dcerpc  A buffer overflow issue was addressed with improved memory handling.  Mounting a maliciously crafted Samba network share may lead to arbitrary code execution | | | | | | | |
|  |  | x | x |  |  |  | x |
| **CVE-2023-23493 [other]**  DiskArbitration  A logic issue was addressed with improved state management.  An encrypted volume may be unmounted and remounted by a different user without prompting for the password | | | | | | | |
|  |  | x |  |  |  |  | x |
| **CVE-2022-32915 [important]**  DriverKit  A type confusion issue was addressed with improved checks.  An app may be able to execute arbitrary code with kernel privileges | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2023-23507 [important]**  Intel Graphics Driver  The issue was addressed with improved bounds checks.  An app may be able to execute arbitrary code with kernel privileges | | | | | | | |
|  |  | x |  |  |  |  | x |
| **CVE-2023-23504 [important]**  Kernel  The issue was addressed with improved memory handling.  An app may be able to execute arbitrary code with kernel privileges | | | | | | | |
|  |  | x |  | x | x | x | x |
| **CVE-2023-23502 [other]**  Kernel  An information disclosure issue was addressed by removing the vulnerable code.  An app may be able to determine kernel memory layout | | | | | | | |
|  |  | x |  | x |  | x | x |
| **CVE-2023-23497 [important]**  PackageKit  A logic issue was addressed with improved state management.  An app may be able to gain root privileges | | | | | | | |
|  |  | x | x |  |  |  | x |
| **CVE-2023-23505 [other]**  Screen Time  A privacy issue was addressed with improved private data redaction for log entries.  An app may be able to access information about a user’s contacts | | | | | | | |
|  |  | x | x | x | x | x | x |
| **CVE-2023-23511 [important]**  Weather  The issue was addressed with improved memory handling.  An app may be able to bypass Privacy preferences | | | | | | | |
|  |  | x |  | x |  | x | x |
| **CVE-2023-23508 [important]**  Windows Installer  The issue was addressed with improved memory handling.  An app may be able to bypass Privacy preferences | | | | | | | |
|  |  | x | x |  |  |  | x |
| **CVE-2023-23519 [other]**  ImageIO  A memory corruption issue was addressed with improved state management.  Processing an image may lead to a denial-of-service | | | | | | | |
|  |  |  |  | x |  | x | x |
| **CVE-2023-23500 [important]**  Kernel  The issue was addressed with improved memory handling.  An app may be able to leak sensitive kernel state | | | | | | | |
|  |  |  |  | x | x | x | x |
| **CVE-2023-23503 [important]**  Maps  A logic issue was addressed with improved state management.  An app may be able to bypass Privacy preferences | | | | | | | |
|  |  |  |  | x | x | x | x |
| **CVE-2023-23512 [other]**  Safari  The issue was addressed with improved handling of caches.  Visiting a website may lead to an app denial-of-service | | | | | | | |
|  |  |  |  | x |  | x | x |
| **CVE-2023-23498 [other]**  Mail Drafts  A logic issue was addressed with improved state management.  The quoted original message may be selected from the wrong email when forwarding an email from an Exchange account | | | | | | | |
|  |  |  |  |  | x | x | x |
| **CVE-2023-23506 [important]**  libxpc  A permissions issue was addressed with improved validation.  An app may be able to access user-sensitive data | | | | | | | |
|  |  |  |  |  |  |  | x |
| **CVE-2023-23510 [other]**  Safari  A permissions issue was addressed with improved validation.  An app may be able to access a user’s Safari history | | | | | | | |
|  |  |  |  |  |  |  | x |
| **CVE-2022-3705 [other]**  Vim  A use after free issue was addressed with improved memory management.  Multiple issues in Vim | | | | | | | |
|  |  |  |  |  |  |  | x |
| **CVE-2023-23501 [important]**  Wi-Fi  The issue was addressed with improved memory handling.  An app may be able to disclose kernel memory | | | | | | | |
|  |  |  |  |  |  |  | x |

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [ipados](/tag.html?tag=ipados) [apple](/tag.html?tag=apple) [io...