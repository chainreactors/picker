---
title: APPLE-SA-09-16-2024-9 macOS Sonoma 14.7
url: https://seclists.org/fulldisclosure/2024/Sep/40
source: Full Disclosure
date: 2024-09-18
fetch_date: 2025-10-06T18:30:18.305665
---

# APPLE-SA-09-16-2024-9 macOS Sonoma 14.7

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

[![Previous](/images/left-icon-16x16.png)](39)
[By Date](date.html#40)
[![Next](/images/right-icon-16x16.png)](41)

[![Previous](/images/left-icon-16x16.png)](39)
[By Thread](index.html#40)
[![Next](/images/right-icon-16x16.png)](41)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-16-2024-9 macOS Sonoma 14.7

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 16 Sep 2024 18:14:48 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-16-2024-9 macOS Sonoma 14.7

macOS Sonoma 14.7 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121247.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accounts
Available for: macOS Sonoma
Impact: An app may be able to access user-sensitive data
Description: The issue was addressed with improved permissions logic.
CVE-2024-44153: Mickey Jin (@patch1t)

App Intents
Available for: macOS Sonoma
Impact: An app may be able to access sensitive data logged when a
shortcut fails to launch another app
Description: This issue was addressed with improved redaction of
sensitive information.
CVE-2024-44182: Kirin (@Pwnrin)

AppleGraphicsControl
Available for: macOS Sonoma
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: The issue was addressed with improved memory handling.
CVE-2024-40846: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative
CVE-2024-40845: Pwn2car working with Trend Micro Zero Day Initiative

AppleGraphicsControl
Available for: macOS Sonoma
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: A memory initialization issue was addressed with improved
memory handling.
CVE-2024-44154: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: The issue was addressed with additional code-signing
restrictions.
CVE-2024-40847: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: An app may be able to bypass Privacy preferences
Description: This issue was addressed with improved checks.
CVE-2024-44164: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: An app may be able to modify protected parts of the file system
Description: A library injection issue was addressed with additional
restrictions.
CVE-2024-44168: Claudio Bozzato and Francesco Benvenuto of Cisco Talos

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: An attacker may be able to read sensitive information
Description: A downgrade issue was addressed with additional code-
signing restrictions.
CVE-2024-40848: Mickey Jin (@patch1t)

AppleVA
Available for: macOS Sonoma
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2024-40841: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

AppSandbox
Available for: macOS Sonoma
Impact: An app may be able to access protected files within an App
Sandbox container
Description: A permissions issue was addressed with additional
restrictions.
CVE-2024-44135: Mickey Jin (@patch1t)

Automator
Available for: macOS Sonoma
Impact: An Automator Quick Action workflow may be able to bypass
Gatekeeper
Description: This issue was addressed by adding an additional prompt for
user consent.
CVE-2024-44128: Anton Boegler

bless
Available for: macOS Sonoma
Impact: An app may be able to modify protected parts of the file system
Description: A permissions issue was addressed with additional
restrictions.
CVE-2024-44151: Mickey Jin (@patch1t)

Compression
Available for: macOS Sonoma
Impact: Unpacking a maliciously crafted archive may allow an attacker to
write arbitrary files
Description: A race condition was addressed with improved locking.
CVE-2024-27876: Snoolie Keffaber (@0xilis)

Dock
Available for: macOS Sonoma
Impact: An app may be able to access user-sensitive data
Description: A privacy issue was addressed by removing sensitive data.
CVE-2024-44177: an anonymous researcher

Game Center
Available for: macOS Sonoma
Impact: An app may be able to access user-sensitive data
Description: A file access issue was addressed with improved input
validation.
CVE-2024-40850: Denis Tokarev (@illusionofcha0s)

ImageIO
Available for: macOS Sonoma
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-27880: Junsung Lee

ImageIO
Available for: macOS Sonoma
Impact: Processing an image may lead to a denial-of-service
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2024-44176: dw0r of ZeroPointer Lab working with Trend Micro Zero
Day Initiative, an anonymous researcher

Intel Graphics Driver
Available for: macOS Sonoma
Impact: Processing a maliciously crafted texture may lead to unexpected
app termination
Description: A buffer overflow issue was addressed with improved memory
handling.
CVE-2024-44160: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

Intel Graphics Driver
Available for: macOS Sonoma
Impact: Processing a maliciously crafted texture may lead to unexpected
app termination
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2024-44161: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

IOSurfaceAccelerator
Available for: macOS Sonoma
Impact: An app may be able to cause unexpected system termination
Description: The issue was addressed with improved memory handling.
CVE-2024-44169: Antonio Zekić

Kernel
Available for: macOS Sonoma
Impact: Network traffic may leak outside a VPN tunnel
Description: A logic issue was addressed with improved checks.
CVE-2024-44165: Andrew Lytvynov

Mail Accounts
Available for: macOS Sonoma
Impact: An app may be able to access information about a user's contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2024-40791: Rodolphe BRUNETTI (@eisw0lf)

Maps
Available for: macOS Sonoma
Impact: An app may be able to read sensitive location information
Description: An issue was addressed with improved handling of temporary
files.
CVE-2024-44181: Kirin(@Pwnrin) and LFY(@secsys) from Fudan University

mDNSResponder
Available for: macOS Sonoma
Impact: An app may be able to cause a denial-of-service
Description: A logic error was addressed with improved error handling.
CVE-2024-44183: Olivier Levon

Notes
Available for: macOS Sonoma
Impact: An app may be able to overwrite arbitrary files
Description: This issue was addressed by removing the vulnerable code.
CVE-2024-44167: ajajfxhj

PackageKit
Available for: macOS Sonoma
Impact: An app may be able to modify protected parts of the file system
Description: This issue was addressed with improved validation of
symlinks.
CVE-2024-44178: Mickey Jin (@patch1t)

Safari
Available for: macOS Sonoma
Impact: Visiting a malicious website may lead to user interface spoofing
Description: This issue was addressed through improved state management.
CVE-2024-40797: Rifa'i Rejal Maynando

Sandbox
Available for: macOS Sonoma
Impact: A malicio...