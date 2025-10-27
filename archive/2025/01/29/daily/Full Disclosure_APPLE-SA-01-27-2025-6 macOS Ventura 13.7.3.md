---
title: APPLE-SA-01-27-2025-6 macOS Ventura 13.7.3
url: https://seclists.org/fulldisclosure/2025/Jan/17
source: Full Disclosure
date: 2025-01-29
fetch_date: 2025-10-06T20:11:43.019926
---

# APPLE-SA-01-27-2025-6 macOS Ventura 13.7.3

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

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-01-27-2025-6 macOS Ventura 13.7.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 27 Jan 2025 14:53:53 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-01-27-2025-6 macOS Ventura 13.7.3

macOS Ventura 13.7.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/122070.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AppleMobileFileIntegrity
Available for: macOS Ventura
Impact: An app may be able to access sensitive user data
Description: A downgrade issue was addressed with additional code-
signing restrictions.
CVE-2025-24109: Bohdan Stasiuk (@Bohdan_Stasiuk)

AppleMobileFileIntegrity
Available for: macOS Ventura
Impact: An app may be able to access information about a user's contacts
Description: A logic issue was addressed with improved restrictions.
CVE-2025-24100: Kirin (@Pwnrin)

AppleMobileFileIntegrity
Available for: macOS Ventura
Impact: An app may be able to modify protected parts of the file system
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-24114: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Ventura
Impact: An app may be able to modify protected parts of the file system
Description: A logic issue was addressed with improved checks.
CVE-2025-24121: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Ventura
Impact: An app may be able to modify protected parts of the file system
Description: A downgrade issue affecting Intel-based Mac computers was
addressed with additional code-signing restrictions.
CVE-2025-24122: Mickey Jin (@patch1t)

ARKit
Available for: macOS Ventura
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-24127: Minghao Lin (@Y1nKoc), babywu, and Xingwei Lin of
Zhejiang University

Audio
Available for: macOS Ventura
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-24106: Wang Yu of Cyberserval

Contacts
Available for: macOS Ventura
Impact: An app may be able to access contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2024-44172: Kirin (@Pwnrin)

CoreMedia
Available for: macOS Ventura
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-24123: Desmond working with Trend Micro Zero Day Initiative
CVE-2025-24124: Pwn2car & Rotiple(HyeongSeok Jang) working with Trend
Micro Zero Day Initiative

CoreRoutine
Available for: macOS Ventura
Impact: An app may be able to determine a user’s current location
Description: The issue was addressed with improved checks.
CVE-2025-24102: Kirin (@Pwnrin)

iCloud Photo Library
Available for: macOS Ventura
Impact: An app may be able to bypass Privacy preferences
Description: The issue was addressed with improved checks.
CVE-2025-24174: Arsenii Kostromin (0x3c3e), Joshua Jones

ImageIO
Available for: macOS Ventura
Impact: Processing an image may lead to a denial-of-service
Description: The issue was addressed with improved memory handling.
CVE-2025-24086: DongJun Kim (@smlijun) and JongSeong Kim (@nevul37) in
Enki WhiteHat, D4m0n

LaunchServices
Available for: macOS Ventura
Impact: An app may be able to access user-sensitive data
Description: A race condition was addressed with additional validation.
CVE-2025-24094: an anonymous researcher

LaunchServices
Available for: macOS Ventura
Impact: An app may be able to read files outside of its sandbox
Description: A path handling issue was addressed with improved
validation.
CVE-2025-24115: an anonymous researcher

LaunchServices
Available for: macOS Ventura
Impact: An app may be able to bypass Privacy preferences
Description: An access issue was addressed with additional sandbox
restrictions.
CVE-2025-24116: an anonymous researcher

libxslt
Available for: macOS Ventura
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed through improved state management.
CVE-2025-24166: Ivan Fratric of Google Project Zero

Login Window
Available for: macOS Ventura
Impact: A malicious app may be able to create symlinks to protected
regions of the disk
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-24136: 云散

PackageKit
Available for: macOS Ventura
Impact: An app may be able to modify protected parts of the file system
Description: The issue was addressed with improved checks.
CVE-2025-24130: Pedro Tôrres (@t0rr3sp3dr0)

Photos Storage
Available for: macOS Ventura
Impact: Deleting a conversation in Messages may expose user contact
information in system logging
Description: This issue was addressed with improved redaction of
sensitive information.
CVE-2025-24146: 神罚(@Pwnrin)

QuartzCore
Available for: macOS Ventura
Impact: Processing web content may lead to a denial-of-service
Description: The issue was addressed with improved checks.
CVE-2024-54497: Anonymous working with Trend Micro Zero Day Initiative

Sandbox
Available for: macOS Ventura
Impact: An app may be able to access removable volumes without user
consent
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-24093: Yiğit Can YILMAZ (@yilmazcanyigit)

SceneKit
Available for: macOS Ventura
Impact: Parsing a file may lead to disclosure of user information
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2025-24149: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

Security
Available for: macOS Ventura
Impact: An app may be able to access protected user data
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-24103: Zhongquan Li (@Guluisacat)

sips
Available for: macOS Ventura
Impact: Parsing a maliciously crafted file may lead to an unexpected app
termination
Description: The issue was addressed with improved checks.
CVE-2025-24139: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

SMB
Available for: macOS Ventura
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2025-24151: an anonymous researcher

Spotlight
Available for: macOS Ventura
Impact: A malicious application may be able to leak sensitive user
information
Description: This issue was addressed through improved state management.
CVE-2025-24138: Rodolphe BRUNETTI (@eisw0lf) of Lupus Nova

StorageKit
Available for: macOS Ventura
Impact: A local attacker may be able to elevate their privileges
Description: A permissions issue was addressed with improved validation.
CVE-2025-24176: Yann GASCUEL of Alter Solutions

WebContentFilter
Available for: macOS Ventura
Impact: An attacker may be able to cause unexpected system termination
or corrupt kernel memory
Description: An out-of-bounds write was addressed with improved input
validatio...