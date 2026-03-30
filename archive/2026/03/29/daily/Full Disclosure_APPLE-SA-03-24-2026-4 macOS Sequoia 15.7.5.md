---
title: APPLE-SA-03-24-2026-4 macOS Sequoia 15.7.5
url: https://seclists.org/fulldisclosure/2026/Mar/19
source: Full Disclosure
date: 2026-03-29
fetch_date: 2026-03-30T04:46:58.465658
---

# APPLE-SA-03-24-2026-4 macOS Sequoia 15.7.5

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-03-24-2026-4 macOS Sequoia 15.7.5

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 24 Mar 2026 17:02:26 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-03-24-2026-4 macOS Sequoia 15.7.5

macOS Sequoia 15.7.5 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/126795.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

802.1X
Available for: macOS Sequoia
Impact: An attacker in a privileged network position may be able to
intercept network traffic
Description: An authentication issue was addressed with improved state
management.
CVE-2026-28865: Héloïse Gollier and Mathy Vanhoef (KU Leuven)

Accounts
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2026-28877: Rosyna Keller of Totally Not Malicious Software

apache
Available for: macOS Sequoia
Impact: Multiple issues in Apache
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-55753
CVE-2025-58098
CVE-2025-59775
CVE-2025-65082
CVE-2025-66200

AppleKeyStore
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: A use after free issue was addressed with improved memory
management.
CVE-2026-20637: Johnny Franks (zeroxjf), an anonymous researcher

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2026-28824: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: An app may be able to access user-sensitive data
Description: A downgrade issue affecting Intel-based Mac computers was
addressed with additional code-signing restrictions.
CVE-2026-20699: Mickey Jin (@patch1t)

Audio
Available for: macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2026-28879: Justin Cohen of Google

Audio
Available for: macOS Sequoia
Impact: An attacker may be able to cause unexpected app termination
Description: A type confusion issue was addressed with improved memory
handling.
CVE-2026-28822: Jex Amro

Calling Framework
Available for: macOS Sequoia
Impact: A remote attacker may be able to cause a denial-of-service
Description: A denial-of-service issue was addressed with improved input
validation.
CVE-2026-28894: an anonymous researcher

CFNetwork
Available for: macOS Sequoia
Impact: A remote user may be able to write arbitrary files
Description: A path handling issue was addressed with improved logic.
CVE-2026-20660: Amy (amys.website)

Clipboard
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved validation of
symlinks.
CVE-2026-28866: Cristian Dinca (icmd.tech)

configd
Available for: macOS Sequoia
Impact: Processing a maliciously crafted string may lead to heap
corruption
Description: An integer overflow was addressed with improved input
validation.
CVE-2026-20639: @cloudlldb of @pixiepointsec

CoreMedia
Available for: macOS Sequoia
Impact: Processing an audio stream in a maliciously crafted media file
may terminate the process
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2026-20690: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

CoreServices
Available for: macOS Sequoia
Impact: An app may be able to gain elevated privileges
Description: A validation issue existed in the entitlement verification.
This issue was addressed with improved validation of the process
entitlement.
CVE-2026-28821: YingQi Shi (@Mas0nShi) of DBAppSecurity's WeBin lab

CoreServices
Available for: macOS Sequoia
Impact: An app may be able to break out of its sandbox
Description: A permissions issue was addressed with additional sandbox
restrictions.
CVE-2026-28838: an anonymous researcher

CoreUtils
Available for: macOS Sequoia
Impact: A user in a privileged network position may be able to cause a
denial-of-service
Description: A null pointer dereference was addressed with improved
input validation.
CVE-2026-28886: Etienne Charron (Renault) and Victoria Martini (Renault)

CUPS
Available for: macOS Sequoia
Impact: An app may be able to gain root privileges
Description: A race condition was addressed with improved state
handling.
CVE-2026-28888: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs

curl
Available for: macOS Sequoia
Impact: An issue existed in curl which may result in unintentionally
sending sensitive information via an incorrect connection
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-14524

DesktopServices
Available for: macOS Sequoia
Impact: An app may be able to access user-sensitive data
Description: This issue was addressed with improved handling of
symlinks.
CVE-2026-20633: Mickey Jin (@patch1t)

DeviceLink
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2026-28876: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs

Diagnostics
Available for: macOS Sequoia
Impact: An app may be able to modify protected parts of the file system
Description: A permissions issue was addressed by removing the
vulnerable code.
CVE-2026-28892: 风沐云烟 (@binary_fmyy) and Minghao Lin (@Y1nKoc)

File System
Available for: macOS Sequoia
Impact: An app may be able to disclose kernel memory
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2026-28832: DARKNAVY (@DarkNavyOrg)

Focus
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A logging issue was addressed with improved data redaction.
CVE-2026-20668: Kirin (@Pwnrin)

GPU Drivers
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: A race condition was addressed with improved state
handling.
CVE-2026-28834: an anonymous researcher

iCloud
Available for: macOS Sequoia
Impact: An app may be able to enumerate a user's installed apps
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-28880: Zhongcheng Li from IES Red Team

ImageIO
Available for: macOS Sequoia
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-6...