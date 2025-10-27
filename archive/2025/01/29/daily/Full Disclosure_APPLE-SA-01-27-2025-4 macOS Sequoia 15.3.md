---
title: APPLE-SA-01-27-2025-4 macOS Sequoia 15.3
url: https://seclists.org/fulldisclosure/2025/Jan/15
source: Full Disclosure
date: 2025-01-29
fetch_date: 2025-10-06T20:11:49.834177
---

# APPLE-SA-01-27-2025-4 macOS Sequoia 15.3

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

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-01-27-2025-4 macOS Sequoia 15.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 27 Jan 2025 14:53:03 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-01-27-2025-4 macOS Sequoia 15.3

macOS Sequoia 15.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/122068.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AirPlay
Available for: macOS Sequoia
Impact: An attacker on the local network may be able to cause unexpected
system termination or corrupt process memory
Description: An input validation issue was addressed.
CVE-2025-24126: Uri Katz (Oligo Security)

AirPlay
Available for: macOS Sequoia
Impact: A remote attacker may cause an unexpected app termination
Description: A type confusion issue was addressed with improved checks.
CVE-2025-24129: Uri Katz (Oligo Security)

AirPlay
Available for: macOS Sequoia
Impact: An attacker in a privileged position may be able to perform a
denial-of-service
Description: The issue was addressed with improved memory handling.
CVE-2025-24131: Uri Katz (Oligo Security)

AirPlay
Available for: macOS Sequoia
Impact: A remote attacker may be able to cause a denial-of-service
Description: A null pointer dereference was addressed with improved
input validation.
CVE-2025-24177: Uri Katz (Oligo Security)

AirPlay
Available for: macOS Sequoia
Impact: A remote attacker may cause an unexpected application
termination or arbitrary code execution
Description: A type confusion issue was addressed with improved checks.
CVE-2025-24137: Uri Katz (Oligo Security)

AppKit
Available for: macOS Sequoia
Impact: An app may be able to access protected user data
Description: The issue was addressed with additional permissions checks.
CVE-2025-24087: Mickey Jin (@patch1t)

AppleGraphicsControl
Available for: macOS Sequoia
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-24112: D4m0n

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: An app may be able to access information about a user's contacts
Description: A logic issue was addressed with improved restrictions.
CVE-2025-24100: Kirin (@Pwnrin)

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A downgrade issue was addressed with additional code-
signing restrictions.
CVE-2025-24109: Bohdan Stasiuk (@Bohdan_Stasiuk)

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: An app may be able to modify protected parts of the file system
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-24114: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: An app may be able to modify protected parts of the file system
Description: A logic issue was addressed with improved checks.
CVE-2025-24121: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: An app may be able to modify protected parts of the file system
Description: A downgrade issue affecting Intel-based Mac computers was
addressed with additional code-signing restrictions.
CVE-2025-24122: Mickey Jin (@patch1t)

ARKit
Available for: macOS Sequoia
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-24127: Minghao Lin (@Y1nKoc), babywu, and Xingwei Lin of
Zhejiang University

Audio
Available for: macOS Sequoia
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-24106: Wang Yu of Cyberserval

CoreAudio
Available for: macOS Sequoia
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-24160: Google Threat Analysis Group
CVE-2025-24161: Google Threat Analysis Group
CVE-2025-24163: Google Threat Analysis Group

CoreMedia
Available for: macOS Sequoia
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-24123: Desmond working with Trend Micro Zero Day Initiative
CVE-2025-24124: Pwn2car & Rotiple (HyeongSeok Jang) working with Trend
Micro Zero Day Initiative

CoreMedia
Available for: macOS Sequoia
Impact: A malicious application may be able to elevate privileges. Apple
is aware of a report that this issue may have been actively exploited
against versions of iOS before iOS 17.2.
Description: A use after free issue was addressed with improved memory
management.
CVE-2025-24085

CoreRoutine
Available for: macOS Sequoia
Impact: An app may be able to determine a user’s current location
Description: The issue was addressed with improved checks.
CVE-2025-24102: Kirin (@Pwnrin)

FaceTime
Available for: macOS Sequoia
Impact: An app may be able to access user-sensitive data
Description: An information disclosure issue was addressed with improved
privacy controls.
CVE-2025-24134: Kirin (@Pwnrin)

iCloud
Available for: macOS Sequoia
Impact: Files downloaded from the internet may not have the quarantine
flag applied
Description: This issue was addressed through improved state management.
CVE-2025-24140: Matej Moravec (@MacejkoMoravec)

iCloud Photo Library
Available for: macOS Sequoia
Impact: An app may be able to bypass Privacy preferences
Description: The issue was addressed with improved checks.
CVE-2025-24174: Arsenii Kostromin (0x3c3e), Joshua Jones

ImageIO
Available for: macOS Sequoia
Impact: Processing an image may lead to a denial-of-service
Description: The issue was addressed with improved memory handling.
CVE-2025-24086: DongJun Kim (@smlijun) and JongSeong Kim (@nevul37) in
Enki WhiteHat, D4m0n

Kernel
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2025-24118: Joseph Ravichandran (@0xjprx) of MIT CSAIL

Kernel
Available for: macOS Sequoia
Impact: A malicious app may be able to gain root privileges
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-24107: an anonymous researcher

Kernel
Available for: macOS Sequoia
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A validation issue was addressed with improved logic.
CVE-2025-24159: pattern-f (@pattern_F_)

LaunchServices
Available for: macOS Sequoia
Impact: An app may be able to access user-sensitive data
Description: A race condition was addressed with additional validation.
CVE-2025-24094: an anonymous researcher

LaunchServices
Available for: macOS Sequoia
Impact: An app may be able to read files outside of its sandbox
Description: A path handling issue was addressed with improved
validation.
CVE-2025-24115: an anonymous researcher

LaunchServices
Available for: macOS Sequoia
Impact: An app may be able to bypass Privacy preferences
Description: An access issue was addressed with additional sandbox
restricti...