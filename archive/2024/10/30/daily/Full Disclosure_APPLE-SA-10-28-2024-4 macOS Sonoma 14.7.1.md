---
title: APPLE-SA-10-28-2024-4 macOS Sonoma 14.7.1
url: https://seclists.org/fulldisclosure/2024/Oct/12
source: Full Disclosure
date: 2024-10-30
fetch_date: 2025-10-06T18:56:16.231446
---

# APPLE-SA-10-28-2024-4 macOS Sonoma 14.7.1

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

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-10-28-2024-4 macOS Sonoma 14.7.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 28 Oct 2024 16:17:35 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-10-28-2024-4 macOS Sonoma 14.7.1

macOS Sonoma 14.7.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121570.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

App Support
Available for: macOS Sonoma
Impact: A malicious app may be able to run arbitrary shortcuts without
user consent
Description: A path handling issue was addressed with improved logic.
CVE-2024-44255: an anonymous researcher

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: A sandboxed process may be able to circumvent sandbox
restrictions
Description: A logic issue was addressed with improved validation.
CVE-2024-44270: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: An app may be able to modify protected parts of the file system
Description: A downgrade issue affecting Intel-based Mac computers was
addressed with additional code-signing restrictions.
CVE-2024-44280: Mickey Jin (@patch1t)

Assets
Available for: macOS Sonoma
Impact: A malicious app with root privileges may be able to modify the
contents of system files
Description: This issue was addressed by removing the vulnerable code.
CVE-2024-44260: Mickey Jin (@patch1t)

CoreMedia Playback
Available for: macOS Sonoma
Impact: A malicious app may be able to access private information
Description: This issue was addressed with improved handling of
symlinks.
CVE-2024-44273: pattern-f (@pattern_F_), Hikerell of Loadshine Lab

CoreServicesUIAgent
Available for: macOS Sonoma
Impact: An app may be able to modify protected parts of the file system
Description: This issue was addressed with additional entitlement
checks.
CVE-2024-44295: an anonymous researcher

CoreText
Available for: macOS Sonoma
Impact: Processing a maliciously crafted font may result in the
disclosure of process memory
Description: The issue was addressed with improved checks.
CVE-2024-44240: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative
CVE-2024-44302: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

CUPS
Available for: macOS Sonoma
Impact: An attacker in a privileged network position may be able to leak
sensitive user information
Description: An issue existed in the parsing of URLs. This issue was
addressed with improved input validation.
CVE-2024-44213: Alexandre Bedard

DiskArbitration
Available for: macOS Sonoma
Impact: A sandboxed app may be able to access sensitive user data
Description: The issue was addressed with improved checks.
CVE-2024-40855: Csaba Fitzl (@theevilbit) of Kandji

Find My
Available for: macOS Sonoma
Impact: An app may be able to read sensitive location information
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2024-44289: Kirin (@Pwnrin)

Foundation
Available for: macOS Sonoma
Impact: Parsing a file may lead to disclosure of user information
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2024-44282: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

Game Controllers
Available for: macOS Sonoma
Impact: An attacker with physical access can input Game Controller
events to apps running on a locked device
Description: The issue was addressed by restricting options offered on a
locked device.
CVE-2024-44265: Ronny Stiftel

ImageIO
Available for: macOS Sonoma
Impact: Processing an image may result in disclosure of process memory
Description: This issue was addressed with improved checks.
CVE-2024-44215: Junsung Lee working with Trend Micro Zero Day Initiative

ImageIO
Available for: macOS Sonoma
Impact: Processing a maliciously crafted message may lead to a denial-
of-service
Description: The issue was addressed with improved bounds checks.
CVE-2024-44297: Jex Amro

Installer
Available for: macOS Sonoma
Impact: An app may be able to access user-sensitive data
Description: An access issue was addressed with additional sandbox
restrictions.
CVE-2024-44216: Zhongquan Li (@Guluisacat)

Installer
Available for: macOS Sonoma
Impact: A malicious application may be able to modify protected parts of
the file system
Description: The issue was addressed with improved checks.
CVE-2024-44287: Mickey Jin (@patch1t)

IOGPUFamily
Available for: macOS Sonoma
Impact: A malicious app may be able to cause a denial-of-service
Description: The issue was addressed with improved memory handling.
CVE-2024-44197: Wang Yu of Cyberserval

Kernel
Available for: macOS Sonoma
Impact: An app may be able to leak sensitive kernel state
Description: An information disclosure issue was addressed with improved
private data redaction for log entries.
CVE-2024-44239: Mateusz Krzywicki (@krzywix)

Kernel
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved validation of
symlinks.
CVE-2024-44175: Csaba Fitzl (@theevilbit) of Kandji

LaunchServices
Available for: macOS Sonoma
Impact: An application may be able to break out of its sandbox
Description: A logic issue was addressed with improved checks.
CVE-2024-44122: an anonymous researcher

Maps
Available for: macOS Sonoma
Impact: An app may be able to read sensitive location information
Description: This issue was addressed with improved redaction of
sensitive information.
CVE-2024-44222: Kirin (@Pwnrin)

Messages
Available for: macOS Sonoma
Impact: An app may be able to break out of its sandbox
Description: The issue was addressed with improved input sanitization.
CVE-2024-44256: Mickey Jin (@patch1t)

PackageKit
Available for: macOS Sonoma
Impact: An app may be able to bypass Privacy preferences
Description: A path deletion vulnerability was addressed by preventing
vulnerable code from running with privileges.
CVE-2024-44159: Mickey Jin (@patch1t)
CVE-2024-44156: Arsenii Kostromin (0x3c3e)

PackageKit
Available for: macOS Sonoma
Impact: An app may be able to modify protected parts of the file system
Description: A permissions issue was addressed with additional
restrictions.
CVE-2024-44196: Csaba Fitzl (@theevilbit) of Kandji

PackageKit
Available for: macOS Sonoma
Impact: An app may be able to modify protected parts of the file system
Description: The issue was addressed with improved checks.
CVE-2024-44253: Mickey Jin (@patch1t), Csaba Fitzl (@theevilbit) of
Kandji

PackageKit
Available for: macOS Sonoma
Impact: A malicious application may be able to modify protected parts of
the file system
Description: The issue was addressed with improved checks.
CVE-2024-44247: Un3xploitable of CW Research Inc
CVE-2024-44267: Bohdan Stasiuk (@Bohdan_Stasiuk), Un3xploitable of CW
Research Inc, Pedro Tôrres (@t0rr3sp3dr0)
CVE-2024-44301: Bohdan Stasiuk (@Bohdan_Stasiuk), Un3xploitable of CW
Research Inc, Pedro Tôrres (@t0rr3sp3dr0)
CVE-2024-44275: Arsenii Kostromin (0x3c3e)

PackageKit
Available for: macOS Sonoma
Impact: An attacker with root ...