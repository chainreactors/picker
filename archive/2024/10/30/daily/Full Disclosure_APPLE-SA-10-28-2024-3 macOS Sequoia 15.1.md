---
title: APPLE-SA-10-28-2024-3 macOS Sequoia 15.1
url: https://seclists.org/fulldisclosure/2024/Oct/11
source: Full Disclosure
date: 2024-10-30
fetch_date: 2025-10-06T18:56:17.436192
---

# APPLE-SA-10-28-2024-3 macOS Sequoia 15.1

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

[![Previous](/images/left-icon-16x16.png)](10)
[By Date](date.html#11)
[![Next](/images/right-icon-16x16.png)](12)

[![Previous](/images/left-icon-16x16.png)](10)
[By Thread](index.html#11)
[![Next](/images/right-icon-16x16.png)](12)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-10-28-2024-3 macOS Sequoia 15.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 28 Oct 2024 16:16:35 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-10-28-2024-3 macOS Sequoia 15.1

macOS Sequoia 15.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121564.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Apache
Impact: Multiple issues existed in Apache
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2024-39573
CVE-2024-38477
CVE-2024-38476

App Support
Available for: macOS Sequoia
Impact: A malicious app may be able to run arbitrary shortcuts without
user consent
Description: A path handling issue was addressed with improved logic.
CVE-2024-44255: an anonymous researcher

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: A sandboxed process may be able to circumvent sandbox
restrictions
Description: A logic issue was addressed with improved validation.
CVE-2024-44270: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: An app may be able to modify protected parts of the file system
Description: A downgrade issue affecting Intel-based Mac computers was
addressed with additional code-signing restrictions.
CVE-2024-44280: Mickey Jin (@patch1t)

Assets
Available for: macOS Sequoia
Impact: A malicious app with root privileges may be able to modify the
contents of system files
Description: This issue was addressed by removing the vulnerable code.
CVE-2024-44260: Mickey Jin (@patch1t)

Contacts
Available for: macOS Sequoia
Impact: An app may be able to access information about a user's contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2024-44298: Kirin (@Pwnrin) and 7feilee

CoreMedia Playback
Available for: macOS Sequoia
Impact: A malicious app may be able to access private information
Description: This issue was addressed with improved handling of
symlinks.
CVE-2024-44273: pattern-f (@pattern_F_), Hikerell of Loadshine Lab

CoreServicesUIAgent
Available for: macOS Sequoia
Impact: An app may be able to modify protected parts of the file system
Description: This issue was addressed with additional entitlement
checks.
CVE-2024-44295: an anonymous researcher

CoreText
Available for: macOS Sequoia
Impact: Processing a maliciously crafted font may result in the
disclosure of process memory
Description: The issue was addressed with improved checks.
CVE-2024-44240: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative
CVE-2024-44302: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

CUPS
Available for: macOS Sequoia
Impact: An attacker in a privileged network position may be able to leak
sensitive user information
Description: An issue existed in the parsing of URLs. This issue was
addressed with improved input validation.
CVE-2024-44213: Alexandre Bedard

Find My
Available for: macOS Sequoia
Impact: An app may be able to read sensitive location information
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2024-44289: Kirin (@Pwnrin)

Foundation
Available for: macOS Sequoia
Impact: Parsing a file may lead to disclosure of user information
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2024-44282: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

Game Controllers
Available for: macOS Sequoia
Impact: An attacker with physical access can input Game Controller
events to apps running on a locked device
Description: The issue was addressed by restricting options offered on a
locked device.
CVE-2024-44265: Ronny Stiftel

ImageIO
Available for: macOS Sequoia
Impact: Processing an image may result in disclosure of process memory
Description: This issue was addressed with improved checks.
CVE-2024-44215: Junsung Lee working with Trend Micro Zero Day Initiative

ImageIO
Available for: macOS Sequoia
Impact: Processing a maliciously crafted message may lead to a denial-
of-service
Description: The issue was addressed with improved bounds checks.
CVE-2024-44297: Jex Amro

Installer
Available for: macOS Sequoia
Impact: An app may be able to access user-sensitive data
Description: An access issue was addressed with additional sandbox
restrictions.
CVE-2024-44216: Zhongquan Li (@Guluisacat)

Installer
Available for: macOS Sequoia
Impact: A malicious application may be able to modify protected parts of
the file system
Description: The issue was addressed with improved checks.
CVE-2024-44287: Mickey Jin (@patch1t)

IOGPUFamily
Available for: macOS Sequoia
Impact: A malicious app may be able to cause a denial-of-service
Description: The issue was addressed with improved memory handling.
CVE-2024-44197: Wang Yu of Cyberserval

IOSurface
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2024-44285: an anonymous researcher

Kernel
Available for: macOS Sequoia
Impact: An app may be able to leak sensitive kernel state
Description: An information disclosure issue was addressed with improved
private data redaction for log entries.
CVE-2024-44239: Mateusz Krzywicki (@krzywix)

Login Window
Available for: macOS Sequoia
Impact: A person with physical access to a Mac may be able to bypass
Login Window during a software update
Description: This issue was addressed through improved state management.
CVE-2024-44231: Toomas Römer

Login Window
Available for: macOS Sequoia
Impact: An attacker with physical access to a Mac may be able to view
protected content from the Login Window
Description: This issue was addressed through improved state management.
CVE-2024-44223: Jaime Bertran

Maps
Available for: macOS Sequoia
Impact: An app may be able to read sensitive location information
Description: This issue was addressed with improved redaction of
sensitive information.
CVE-2024-44222: Kirin (@Pwnrin)

Messages
Available for: macOS Sequoia
Impact: An app may be able to break out of its sandbox
Description: The issue was addressed with improved input sanitization.
CVE-2024-44256: Mickey Jin (@patch1t)

Notification Center
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2024-44292: Kirin (@Pwnrin)

Notification Center
Available for: macOS Sequoia
Impact: A user may be able to view sensitive user information
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2024-44293: Kirin (@Pwnrin) and 7feilee

PackageKit
Available for: macOS Sequoia
Impact: A malicious application may be able to modify protected parts of
the file system
Description: The issue was addressed with improved checks.
CVE-2...